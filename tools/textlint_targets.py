#!/usr/bin/env python3
"""textlint で検査する Markdown の一覧を出す。--run で、その一覧に textlint をかける（package.json の lint:text が使う）。

対象は docs/ の手書きの Markdown のうち、骨格（stub）でないもの（design §6.2・§8.6）。
  除くもの   stage が骨格の段のページ（schema/site.yml の stages の最初の段。骨格の要点と要約は目次を写しただけで、
             本文を書くときに書き直す）。生成物：docs/lists/ の下と、分野の入口 docs/<field>/index.md
             （field は site.yml の fields の id。design §8.2）
  入れるもの サイトのトップ docs/index.md のような front matter のない手書きの Markdown。公開から外した試作のページ
             （stage は draft 以上。試作の終わりの条件は、試作のページで書き方の検査が0件。design §10.1）。
             front matter が読めないか stage のないページ（検査を広く取る。front matter の誤りは front matter の検査が見る）
  手書きのページの中の生成部分（gen:begin〜gen:end）は、このファイルでは外さない

使い方:
  uv run python tools/textlint_targets.py                  対象を1行に1つ出す（リポジトリの根からの相対パス。名前の順）
  uv run python tools/textlint_targets.py --run            対象に textlint をかける（npm run lint:text）
  uv run python tools/textlint_targets.py --run -- --fix   -- の後ろを textlint に渡す（npm run lint:text:fix）
  uv run python tools/textlint_targets.py --root DIR       DIR を根にして読む（DIR/schema/site.yml と DIR/docs/。試験用）
終了コード: 0＝一覧を出した・textlint のエラーがない（警告だけなら 0）・対象がない、
           1 など＝textlint の終了コードをそのまま返す（エラーがある、設定や prh.yml の specs が誤っている）、
           2＝検査できない（site.yml が読めない・fields か stages がない、textlint が入っていない）
対象がないときは textlint を呼ばない（textlint は引数がないと使い方を出して 0 で終わり、検査したように見えるため）。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE_YML = Path("schema/site.yml")
DOCS = Path("docs")
GENERATED_DIRS = ("lists",)   # docs/ の直下の、生成物だけを置くフォルダ（design §8.2）
ENTRY_FILE = "index.md"       # 分野の入口（docs/<field>/index.md。生成）のファイル名（design §8.2）
TEXTLINT = Path("node_modules/.bin/textlint")
FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*\r?$", re.S | re.M)


class CannotCheck(Exception):
    """検査できない（終了コード 2）。"""


def load_vocab(root: Path) -> tuple[set[str], str]:
    """site.yml から、分野の id の集まりと、骨格の段（stages の最初）を読む。"""
    path = root / SITE_YML
    try:
        site = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise CannotCheck(f"{SITE_YML.as_posix()} がない") from None
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as e:
        raise CannotCheck(f"{SITE_YML.as_posix()} が読めない（{e}）") from None
    if not isinstance(site, dict):
        raise CannotCheck(f"{SITE_YML.as_posix()} の形が違う（マッピングでない）")
    fields = site.get("fields")
    field_ids = {f["id"] for f in fields if isinstance(f, dict) and isinstance(f.get("id"), str)} \
        if isinstance(fields, list) else set()
    if not field_ids:
        raise CannotCheck(f"{SITE_YML.as_posix()} に fields（分野の id）がない")
    stages = site.get("stages")
    if not isinstance(stages, list) or not stages or not isinstance(stages[0], str):
        raise CannotCheck(f"{SITE_YML.as_posix()} に stages（段の並び）がない")
    return field_ids, stages[0]


def read_stage(path: Path) -> tuple[str | None, str | None]:
    """ページの stage と、読めなかったときの理由を返す。front matter がなければ (None, None)。"""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return None, f"読めない（{e}）"
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None, None
    try:
        front = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        reason = getattr(e, "problem", None) or str(e).splitlines()[0]
        return None, f"front matter が読めない（{reason}）"
    if front is None:
        return None, None
    if not isinstance(front, dict):
        return None, "front matter がマッピングでない"
    stage = front.get("stage")
    return (str(stage) if stage is not None else None), None


def is_generated(rel: Path, field_ids: set[str]) -> bool:
    """docs/ からの相対パスが、まるごと生成するファイルか。"""
    if len(rel.parts) > 1 and rel.parts[0] in GENERATED_DIRS:
        return True
    return len(rel.parts) == 2 and rel.parts[0] in field_ids and rel.name == ENTRY_FILE


def targets(root: Path, warn=None) -> list[Path]:
    """検査の対象を、root からの相対パスで、名前の順に返す。warn は読めなかったページの知らせを受け取る。"""
    field_ids, skeleton = load_vocab(root)
    docs = root / DOCS
    if not docs.is_dir():
        return []
    found = []
    for path in sorted(docs.rglob("*.md")):
        if not path.is_file():
            continue
        rel = path.relative_to(docs)
        if is_generated(rel, field_ids):
            continue
        stage, problem = read_stage(path)
        if problem and warn:
            warn(f"警告: {path.relative_to(root).as_posix()}: {problem}。検査の対象に入れる")
        if stage == skeleton:
            continue
        found.append(path.relative_to(root))
    return found


def run_textlint(root: Path, files: list[Path], extra: list[str]) -> int:
    """対象に textlint をかけて、textlint の終了コードを返す。対象がなければ呼ばずに 0。"""
    if not files:
        print("textlint の対象がない（docs/ に、骨格でない手書きの Markdown がない）", file=sys.stderr)
        return 0
    exe = root / TEXTLINT
    if not exe.exists():
        raise CannotCheck(f"textlint がない（{TEXTLINT.as_posix()}）。リポジトリの根で npm ci を流す")
    # 設定（.textlintrc.json）は、根で動かして textlint に探させる
    return subprocess.run([str(exe), *extra, *[f.as_posix() for f in files]], cwd=root).returncode


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    extra: list[str] = []
    if "--" in argv:
        cut = argv.index("--")
        argv, extra = argv[:cut], argv[cut + 1:]
    parser = argparse.ArgumentParser(
        description="textlint で検査する Markdown の一覧を出す（--run で textlint をかける）",
        epilog="対象：docs/ の手書きの Markdown のうち、骨格の段でないもの（生成物の docs/lists/ と docs/<field>/index.md を除く）")
    parser.add_argument("--run", action="store_true", help="対象に textlint をかける（-- の後ろを textlint に渡す）")
    parser.add_argument("--root", type=Path, default=ROOT, help="リポジトリの根（試験用）")
    args = parser.parse_args(argv)
    if extra and not args.run:
        parser.error("-- の後ろの引数は --run のときだけ使える")
    root = args.root.resolve()

    def warn(message: str) -> None:
        print(message, file=sys.stderr)

    try:
        files = targets(root, warn)
        if args.run:
            return run_textlint(root, files, extra)
    except CannotCheck as e:
        print(f"検査できない: {e}", file=sys.stderr)
        return 2
    for f in files:
        print(f.as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
