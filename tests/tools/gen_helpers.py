"""作る層の試験の共通の部品（test_gen_*.py が import する）。

fixtures/gen/ は作る層の試験用の小さなサイト：schema/site.yml（本物の写し）・mkdocs.yml（テーマの上書きを読まない試験用。
markdown_extensions は本物と同じ組）・docs/ のページ19（うち1つは stage が stub、1つは held_back で外す試作のページ）・
docs/index.md・stubs/ の骨格のページ2・data/ の各ファイル・snippets/ の雛形。値はすべて作りもので、URL は example.* だけ。
GenCase は、それを一時フォルダに写し、本物の作る層の設定（tools/gen/config.yml）に held_back（writing-safe-hooks）を
足したものを <根>/tools/gen/config.yml に置く。
"""
from __future__ import annotations

import contextlib
import io
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "gen"
CONFIG = REPO / "tools" / "gen" / "config.yml"
HELD = "writing-safe-hooks"

import gen_site  # noqa: E402
from lib.markdown import fence_spans, fenced_mask, find_markers, split_front_matter  # noqa: E402


def run_cli(*args: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = gen_site.main(list(args))
    return code, out.getvalue(), err.getvalue()


def outside_markers(text: str) -> str:
    """目印の間を空にした本文（目印の外が変わっていないかを比べるため）。"""
    _, body, _, _ = split_front_matter(text)
    lines = body.split("\n")
    markers, _ = find_markers(body, lines, fenced_mask(lines, fence_spans(lines)), 1)
    out, pos, covered = [], 0, -1
    for m in sorted(markers, key=lambda m: m.start):
        if not m.closed or m.start < covered:
            continue
        out.append(body[pos:m.inner_start])
        pos, covered = m.inner_end, m.stop
    out.append(body[pos:])
    return text[:len(text) - len(body)] + "".join(out)


def block_content(text: str, name: str) -> str:
    """<!-- gen:begin name --> 〜 <!-- gen:end name --> の間（なければ失敗）。"""
    m = re.search(r"<!-- gen:begin " + re.escape(name) + r" -->(.*?)<!-- gen:end " + re.escape(name) + " -->", text, re.S)
    if m is None:
        raise AssertionError(f"生成の部分 {name} がない")
    return m.group(1)


class GenCase(unittest.TestCase):
    """fixtures/gen を一時フォルダに写し、held_back を足した作る層の設定を置く。"""

    held_back = (HELD,)

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "site"
        shutil.copytree(FIXTURE, self.root)
        self.write_config()

    def tearDown(self):
        self._tmp.cleanup()

    def write_config(self, replace: dict[str, str] | None = None) -> None:
        text = CONFIG.read_text(encoding="utf-8")
        held = "[" + ", ".join(self.held_back) + "]"
        # 本物の設定の held_back（[] でも、試作のページの箇条書きでも）を、試験の値に置き換える
        m = re.search(r"\nheld_back:[^\n]*\n(?:  (?:- |#)[^\n]*\n)*", text)
        self.assertIsNotNone(m, "tools/gen/config.yml に held_back がない")
        text = text[:m.start()] + f"\nheld_back: {held}\n" + text[m.end():]
        for old, new in (replace or {}).items():
            self.assertIn(old, text)
            text = text.replace(old, new)
        path = self.root / "tools" / "gen" / "config.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def cli(self, *args: str) -> tuple[int, str, str]:
        return run_cli("--root", str(self.root), *args)

    def generate(self) -> str:
        code, out, err = self.cli()
        self.assertEqual(code, 0, out + err)
        return out

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def replace(self, rel: str, old: str, new: str) -> None:
        text = self.read(rel)
        self.assertIn(old, text)
        self.write(rel, text.replace(old, new, 1))
