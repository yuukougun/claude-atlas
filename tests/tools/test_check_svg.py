"""tools/check_svg.py（図の SVG の大きさ・文字・背景の検査。kyopro-atlas から写したもの）の試験。
`uv run python -m unittest discover -s tests/tools` で動く。一時フォルダの docs/img/<id>/ に SVG を置いて流す。
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

import check_svg  # noqa: E402

GOOD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">'
        '<rect width="400" height="200" fill="#ffffff"/><text x="10" y="30" font-size="16">お願い</text></svg>')


class SvgCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def svg(self, name: str, text: str) -> Path:
        p = self.root / "docs" / "img" / "request-vs-lock" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def warns(self, text: str) -> list[str]:
        warns, err = check_svg.check(self.svg("a.svg", text))
        self.assertIsNone(err)
        return warns

    def run_cli(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check_svg.main(["--root", str(self.root), *args])
        return code, out.getvalue()


class TestCheck(SvgCase):
    def test_good(self):
        self.assertEqual(self.warns(GOOD), [])

    def test_size_and_ratio(self):
        w = self.warns(GOOD.replace('width="400" height="200"', 'width="400" height="300"'))
        self.assertTrue(any("比が違う" in x for x in w))
        w = self.warns(GOOD.replace(' width="400" height="200"', ""))
        self.assertTrue(any("width・height がない" in x for x in w))
        w = self.warns(GOOD.replace('viewBox="0 0 400 200" width="400" height="200"', 'viewBox="0 0 800 200" width="800" height="200"')
                       .replace('width="400" height="200" fill', 'width="800" height="200" fill'))
        self.assertTrue(any("目安" in x for x in w))

    def test_small_text_and_no_text(self):
        w = self.warns(GOOD.replace('font-size="16"', 'font-size="6"'))
        self.assertTrue(any("未満の文字" in x for x in w))
        w = self.warns(GOOD.replace('<text x="10" y="30" font-size="16">お願い</text>', '<circle r="5"/>'))
        self.assertTrue(any("<text> がない" in x for x in w))

    def test_background(self):
        w = self.warns(GOOD.replace('<rect width="400" height="200" fill="#ffffff"/>', ""))
        self.assertTrue(any("白い背景の rect がない" in x for x in w))
        w = self.warns(GOOD.replace('<rect width="400" height="200"', '<rect width="300" height="200"'))
        self.assertTrue(any("右 100" in x for x in w))
        w = self.warns(GOOD.replace('<rect width="400" height="200" fill="#ffffff"/>',
                                    '<g transform="translate(0,0)"><rect width="100%" height="100%" style="fill: white"/></g>'))
        self.assertEqual(w, [])


class TestCli(SvgCase):
    def test_exit_codes(self):
        self.svg("a.svg", GOOD)
        self.assertEqual(self.run_cli()[0], 0)
        self.svg("b.svg", GOOD.replace('font-size="16"', 'font-size="6"'))
        code, out = self.run_cli()
        self.assertEqual(code, 0)
        self.assertIn("警告: docs/img/request-vs-lock/b.svg", out)
        self.assertEqual(self.run_cli("--strict")[0], 1)
        self.assertEqual(self.run_cli("--page", "other")[0], 0)
        self.svg("c.svg", "<svg")
        code, out = self.run_cli("--page", "request-vs-lock")
        self.assertEqual(code, 1)
        self.assertIn("エラー: docs/img/request-vs-lock/c.svg", out)

    def test_no_images(self):
        code, out = self.run_cli()
        self.assertEqual(code, 0)
        self.assertIn("図 0 枚", out)


if __name__ == "__main__":
    unittest.main()
