#!/usr/bin/env python3
"""textlint で検査する Markdown の一覧を出す。--run で、その一覧に textlint をかける（package.json の lint:text が使う）。

対象は docs/ の手書きの Markdown のうち、骨格（stub）でないもの（design §6.2・§8.6）。
  除くもの   stage が骨格の段のページ（schema/site.yml の stages の最初の段。骨格の要点と要約は目次を写しただけで、
             本文を書くときに書き直す）。生成物：docs/lists/ の下と、分野の入口 docs/<field>/index.md
             （field は site.yml の fields の id。design §8.2）
  入れるもの サイトのトップ docs/index.md のような front matter のない手書きの Markdown。公開から外した試作のページ
             （stage は draft 以上。試作の終わりの条件は、試作のページで書き方の検査が0件。design §10.1）。
             front matter が読めないか stage のないページ（検査を広く取る。front matter の誤りは front matter の検査が見る）
  --run のとき、生成の目印の間は検査から外す（書き手の文ではない。link:begin〜link:end の間の他ページの題名など）。
             外す目印：<!-- link:begin … -->〜<!-- link:end -->、<!-- gen:begin … -->〜<!-- gen:end … -->、
             <!-- fact:begin … -->〜<!-- fact:end -->。目印のあるページは、目印の中に textlint-disable／enable の
             コメント（textlint-filter-rule-comments）を足した写しを根の下の一時フォルダに作って検査し、出力の
             パスを元のページに戻す（行番号は変わらない。--fix のときは写しでなく元のページを直す）

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
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE_YML = Path("schema/site.yml")
DOCS = Path("docs")
GENERATED_DIRS = ("lists",)   # docs/ の直下の、生成物だけを置くフォルダ（design §8.2）
ENTRY_FILE = "index.md"       # 分野の入口（docs/<field>/index.md。生成）のファイル名（design §8.2）
TEXTLINT = Path("node_modules/.bin/textlint")
FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*\r?$", re.S | re.M)
# 生成の目印（tools/lib/markdown.py と同じ）。begin の直後に disable、end の直前に enable を足す
GEN_BEGIN_RE = re.compile(r"<!--\s*(?:link|gen|fact):begin\b[^>]*?-->")
GEN_END_RE = re.compile(r"<!--\s*(?:link|gen|fact):end\b[^>]*?-->")
DISABLE = "<!-- textlint-disable -->"
ENABLE = "<!-- textlint-enable -->"


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


def mask_generated(text: str) -> str:
    """生成の目印の間を textlint の検査から外すコメントを足す（行数は変えない）。"""
    text = GEN_BEGIN_RE.sub(lambda m: m.group(0) + DISABLE, text)
    return GEN_END_RE.sub(lambda m: ENABLE + m.group(0), text)


def has_generated_marker(text: str) -> bool:
    return bool(GEN_BEGIN_RE.search(text))


def run_textlint(root: Path, files: list[Path], extra: list[str]) -> int:
    """対象に textlint をかけて、textlint の終了コードを返す。対象がなければ呼ばずに 0。"""
    if not files:
        print("textlint の対象がない（docs/ に、骨格でない手書きの Markdown がない）", file=sys.stderr)
        return 0
    exe = root / TEXTLINT
    if not exe.exists():
        raise CannotCheck(f"textlint がない（{TEXTLINT.as_posix()}）。リポジトリの根で npm ci を流す")
    # 設定（.textlintrc.json）は、根で動かして textlint に探させる
    base = [str(exe), *extra]
    if "--fix" in extra:   # 写しを直しても元に戻せないので、元のページを直す（生成の部分は gen_site.py が書き直す）
        return subprocess.run([*base, *[f.as_posix() for f in files]], cwd=root).returncode
    masked: dict[Path, Path] = {}   # 元のページ → 写し（どちらも root からの相対パス）
    tmp = Path(tempfile.mkdtemp(prefix=".textlint-mask-", dir=root))
    try:
        for f in files:
            try:
                text = (root / f).read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue   # 読めないページは元のまま textlint に任せる
            if has_generated_marker(text):
                copy = tmp / f
                copy.parent.mkdir(parents=True, exist_ok=True)
                copy.write_text(mask_generated(text), encoding="utf-8")
                masked[f] = copy.relative_to(root)
        if not masked:
            return subprocess.run([*base, *[f.as_posix() for f in files]], cwd=root).returncode
        args = [(masked.get(f, f)).as_posix() for f in files]
        done = subprocess.run([*base, *args], cwd=root, capture_output=True, text=True)
        out, err = done.stdout, done.stderr
        for orig, copy in masked.items():   # 出力のパス（絶対でも相対でも）を元のページに戻す
            out = out.replace((root / copy).as_posix(), (root / orig).as_posix()).replace(copy.as_posix(), orig.as_posix())
            err = err.replace((root / copy).as_posix(), (root / orig).as_posix()).replace(copy.as_posix(), orig.as_posix())
        sys.stdout.write(out)
        sys.stderr.write(err)
        return done.returncode
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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
