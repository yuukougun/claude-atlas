#!/usr/bin/env python3
"""CI と同じ検査の組を、手元で1回に流す入口（設計書 §8.6・DR-16。commit の前に流す。CLAUDE.md）。
CI の .github/workflows/check.yml は、これを `uv run python tools/check_all.py` で流す（同じ組になる）。

使い方:
  uv run python tools/check_all.py                 全部の段を順に流し、最後にまとめを出す（落ちた段があっても続ける）
  uv run python tools/check_all.py --list          段の一覧（名前・コマンド・何を見るか）を出す
  uv run python tools/check_all.py --only check_pages,tests-tools   その段だけ（くり返し・カンマ区切り可）
  uv run python tools/check_all.py --skip mkdocs,tests-site          その段を飛ばす（くり返し・カンマ区切り可）
  uv run python tools/check_all.py -x              最初に落ちた段で止める
  uv run python tools/check_all.py --render        描画の検査（render_pages.py。Chrome が要る）も流す。サイトを作業用の
                                                   一時フォルダにビルドして全ページを描く（既定の組には入れない）
  uv run python tools/check_all.py --root DIR      DIR を根にして流す（試験用）
終了コード: 0＝流した段がすべて通った（飛ばした段は数えない）、1＝落ちた段がある、2＝--only・--skip の名前が違う

段（並びは軽い順。名前は --only・--skip で使う）:
  make_schema       schema/*.schema.json が keys.yml と site.yml から作り直したものと同じ（tools/make_schema.py --check）
  gen_site          生成物と目印の中身が最新（tools/gen_site.py --check。道具がなければ飛ばす）
  check_pages       front matter・参照・本文・数値と出典・確認日（tools/check_pages.py。確認日の期限切れは警告）
  check_catalog     目次の検査（tools/check_catalog.py。骨格〔工程6c〕の後に外す）
  check_templates   雛形の静的な検査（tools/check_templates.py）
  check_svg         図の SVG（tools/check_svg.py。警告は出すだけ）
  textlint          書き方の検査（tools/textlint_targets.py --run。Node と npm ci が要る）
  mkdocs            サイトのビルド（mkdocs build --strict。一時フォルダに作り、site/ は書かない）
  tests-tools       道具の試験（tests/tools）
  tests-site        サイトの設定・見た目の試験（tests/site。Chrome を使う試験は CA_CHROME があるときだけ）
  tests-hooks-python3   フックの試験を、標準のライブラリだけの python3 で（tests/hooks。読者の環境に近い）
  tests-hooks       フックの試験を uv の Python 3.12 で
  tests-guides      手引きとチェックリストの試験（tests/guides）
  render            描画の検査（--render のときだけ。tools/render_pages.py）
各段は、根をフォルダにして別のプロセスで流す。環境に NO_MKDOCS_2_WARNING=1 を足す（Material 9.8 の知らせを消す）。
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable


@dataclass
class Step:
    name: str
    command: list[str]
    what: str
    needs: str | None = None            # この段に要るファイル（根からの相対。なければ飛ばす）
    optional: bool = False              # 既定の組に入れない（--render など）
    env: dict[str, str] = field(default_factory=dict)

    def shown(self) -> str:
        cmd = ["uv run python" if c == PY else c for c in self.command]
        return " ".join(cmd)


def steps(work: Path) -> list[Step]:
    site = str(work / "site")
    return [
        Step("make_schema", [PY, "tools/make_schema.py", "--check"], "schema/*.schema.json が最新"),
        Step("gen_site", [PY, "tools/gen_site.py", "--check"], "生成物と目印の中身が最新", needs="tools/gen_site.py"),
        Step("check_pages", [PY, "tools/check_pages.py"], "front matter・参照・本文・数値と出典・確認日"),
        Step("check_catalog", [PY, "tools/check_catalog.py", "-q"], "目次の検査（骨格の後に外す）",
             needs="tools/check_catalog.py"),
        Step("check_templates", [PY, "tools/check_templates.py"], "雛形の静的な検査"),
        Step("check_svg", [PY, "tools/check_svg.py"], "図の SVG（警告は出すだけ）"),
        Step("textlint", [PY, "tools/textlint_targets.py", "--run"], "書き方の検査（Node と npm ci が要る）"),
        Step("mkdocs", [PY, "-m", "mkdocs", "build", "--strict", "-q", "-d", site], "サイトのビルド（一時フォルダに作る）"),
        Step("tests-tools", [PY, "-m", "unittest", "discover", "-s", "tests/tools"], "道具の試験", needs="tests/tools"),
        Step("tests-site", [PY, "-m", "unittest", "discover", "-s", "tests/site"], "サイトの設定・見た目の試験",
             needs="tests/site"),
        Step("tests-hooks-python3", ["python3", "-m", "unittest", "discover", "-s", "tests/hooks"],
             "フックの試験（標準のライブラリだけの python3）", needs="tests/hooks"),
        Step("tests-hooks", [PY, "-m", "unittest", "discover", "-s", "tests/hooks"], "フックの試験（uv の Python）",
             needs="tests/hooks"),
        Step("tests-guides", [PY, "-m", "unittest", "discover", "-s", "tests/guides"], "手引きとチェックリストの試験",
             needs="tests/guides"),
        Step("render", [PY, "tools/render_pages.py", site], "描画の検査（Chrome が要る。mkdocs の段の後に流す）",
             optional=True),
    ]


@dataclass
class Result:
    step: Step
    status: str                          # 通った・落ちた・飛ばした
    code: int | None = None
    seconds: float = 0.0
    note: str = ""


def run_step(step: Step, root: Path, env: dict[str, str]) -> Result:
    if step.needs and not (root / step.needs).exists():
        return Result(step, "飛ばした", note=f"{step.needs} がない")
    exe = step.command[0]
    if exe != PY and shutil.which(exe) is None:
        return Result(step, "飛ばした", note=f"{exe} がない")
    t0 = time.monotonic()
    sys.stdout.flush()
    try:
        cp = subprocess.run(step.command, cwd=root, env={**env, **step.env})
    except OSError as e:
        return Result(step, "落ちた", None, time.monotonic() - t0, f"動かせない: {e}")
    status = "通った" if cp.returncode == 0 else "落ちた"
    return Result(step, status, cp.returncode, time.monotonic() - t0)


def select_steps(all_steps: list[Step], only: list[str], skip: list[str], render: bool) -> list[Step]:
    """流す段（--only がなければ既定の組。--render で描画の検査を足す。描画の検査には mkdocs の段も足す）。"""
    wanted = set(only) if only else {s.name for s in all_steps if not s.optional}
    if render:
        wanted.add("render")
    if "render" in wanted:
        wanted.add("mkdocs")                 # 描画の検査は mkdocs の段が作ったサイトを描く
    return [s for s in all_steps if s.name in wanted and s.name not in skip]


def parse_names(values: list[str]) -> list[str]:
    return [x.strip() for v in values for x in v.split(",") if x.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="check_all.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", action="store_true", help="段の一覧を出して終わる")
    parser.add_argument("--only", action="append", default=[], metavar="NAME", help="その段だけを流す")
    parser.add_argument("--skip", action="append", default=[], metavar="NAME", help="その段を飛ばす")
    parser.add_argument("-x", "--fail-fast", action="store_true", help="最初に落ちた段で止める")
    parser.add_argument("--render", action="store_true", help="描画の検査（Chrome が要る）も流す")
    parser.add_argument("--root", metavar="DIR", help="根（既定はこのリポジトリ）")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else ROOT

    with tempfile.TemporaryDirectory(prefix="ca-check-all-") as tmp:
        all_steps = steps(Path(tmp))
        names = [s.name for s in all_steps]
        if args.list:
            for s in all_steps:
                mark = "（--render のとき）" if s.optional else ""
                print(f"{s.name:22s} {s.what}{mark}\n{'':22s} {s.shown()}")
            return 0
        only, skip = parse_names(args.only), parse_names(args.skip)
        bad = [n for n in only + skip if n not in names]
        if bad:
            print(f"知らない段：{'・'.join(bad)}（あるもの：{'・'.join(names)}）", file=sys.stderr)
            return 2
        chosen = select_steps(all_steps, only, skip, args.render)
        env = {**os.environ, "NO_MKDOCS_2_WARNING": "1"}
        results: list[Result] = []
        for n, s in enumerate(chosen, 1):
            print(f"\n== [{n}/{len(chosen)}] {s.name}：{s.shown()}", flush=True)
            r = run_step(s, root, env)
            if r.status == "飛ばした":
                print(f"飛ばした（{r.note}）")
            results.append(r)
            if args.fail_fast and r.status == "落ちた":
                break
        print("\nまとめ（check_all.py）")
        for r in results:
            extra = f"（{r.note}）" if r.note else (f"（終了コード {r.code}）" if r.status == "落ちた" and r.code is not None else "")
            print(f"  {r.status}  {r.step.name}{extra}　{r.seconds:.1f} 秒")
        counts = {k: sum(1 for r in results if r.status == k) for k in ("通った", "落ちた", "飛ばした")}
        rest = len(chosen) - len(results)
        tail = f"・流さなかった {rest}（-x で止めた）" if rest else ""
        print(f"通った {counts['通った']}・落ちた {counts['落ちた']}・飛ばした {counts['飛ばした']}{tail}")
        return 1 if counts["落ちた"] else 0


if __name__ == "__main__":
    sys.exit(main())
