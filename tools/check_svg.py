#!/usr/bin/env python3
"""図の SVG（docs/img/**/*.svg）の大きさと文字の大きさと背景を機械的に調べる（設計書 §8.6・planning/guides/common.md
§13「図と表」）。kyopro-atlas の tools/check_svg.py（同じ作者、MIT）を写し、置き場所と案内だけを直したもの。

使い方:
  uv run python tools/check_svg.py                    全部の図を調べ、警告を出す
  uv run python tools/check_svg.py --page <id>        そのページの図（docs/img/<id>/）だけ（くり返し・カンマ区切り可）
  uv run python tools/check_svg.py docs/img/x/a.svg   その図だけ
  uv run python tools/check_svg.py --strict           警告があれば終了コード 1（既定は 0。読めない SVG だけ 1）
  uv run python tools/check_svg.py --root DIR         DIR/docs/img を見る（試験用）

見るもの（どれも警告。common.md §13：文字はテキストのまま、viewBox と同じ比の width・height、背景を白、幅は 400 程度）:
  viewBox・width・height がない、width:height が viewBox と違う
  幅が 450 を超える           「幅は 400 程度まで」の目安から大きく外れる（横に広いものは2枚に分ける）
  文字が小さい                スマホの本文の幅（328px）で表示したときに 9px 未満になる文字
                              （倍率 = min(width, 328) / viewBox の幅、文字 = font-size × 倍率。上付き・下付きの tspan は除く）
  文字がない                  <text> が1つもない（文字を画像やパスにすると、検索と翻訳と読み上げに出ない）。図形だけの図は
                              そのまま置いてよい
  白い背景が viewBox を覆わない
                              文書の順で最初の白い rect（defs などの中は除く。親の fill を継ぐ）を背景とみなし、viewBox
                              （なければ 0 0 width height）を覆うかを見る。覆わない帯は透けて、ダークモードで地の色が出る。
                              width="100%" の % は viewBox の幅・高さに対してなので、viewBox の左端が 0 でなければ x も要る。
                              親と自分の transform は translate だけを足し合わせ、ほかの transform の中の rect は見ない。白い
                              rect がないときも警告する
読めない SVG（XML として壊れている）はエラー。標準ライブラリだけで動く。描いた結果は tools/render_pages.py で見る。
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = "docs/img"
AVAIL = 328.0       # スマホ（360px）で本文に使える幅
MIN_TEXT = 9.0      # 表示したときの文字の大きさの下限（px）
MAX_WIDTH = 450.0   # 「幅は 400 程度まで」の目安から大きく外れる幅
NS = "{http://www.w3.org/2000/svg}"
WHITE = {"#fff", "#ffffff", "white", "rgb(255,255,255)"}
NOT_DRAWN = {"defs", "marker", "pattern", "clipPath", "mask", "symbol", "style", "title", "desc", "metadata",
             "linearGradient", "radialGradient", "filter"}
NUMBER = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
TRANSLATE_RE = re.compile(rf"\s*translate\(\s*({NUMBER})(?:\s*,?\s*({NUMBER}))?\s*\)\s*")
GAP = 0.01          # 背景の rect と viewBox の差をこれより大きいときだけ透けるとみなす（小数の誤差）


def num(s: str | None) -> float | None:
    if s is None:
        return None
    m = re.match(r"\s*([0-9.]+)\s*(px)?\s*$", s)
    return float(m.group(1)) if m else None


def font_size(el: ET.Element, parent: float) -> float:
    v = el.get("font-size")
    m = re.search(r"font-size\s*:\s*([^;]+)", el.get("style") or "")
    if m:
        v = m.group(1)
    if v is None:
        return parent
    v = v.strip()
    try:
        if v.endswith("em"):
            return parent * float(v[:-2])
        if v.endswith("%"):
            return parent * float(v[:-1]) / 100
    except ValueError:
        return parent
    n = num(v)
    return n if n else parent


def texts(el: ET.Element, fs: float, scale: float, out: list[tuple[float, str]]) -> None:
    fs = font_size(el, fs)
    m = re.search(r"scale\(\s*([0-9.]+)", el.get("transform") or "")
    if m:
        scale *= float(m.group(1))
    tag = el.tag.replace(NS, "")
    if tag in ("text", "tspan"):
        own = (el.text or "").strip()
        fsa = el.get("font-size") or ""
        sub = tag == "tspan" and (el.get("baseline-shift") or fsa.endswith("em"))
        if own and not sub:
            out.append((fs * scale, own[:30]))
    for c in el:
        texts(c, fs, scale, out)


def fill_of(el: ET.Element, inherited: str) -> str:
    """el の fill（style が属性より強い。なければ親の値）。空白を除いた小文字。"""
    m = re.search(r"(?:^|;)\s*fill\s*:\s*([^;]+)", el.get("style") or "")
    v = m.group(1) if m else el.get("fill")
    return re.sub(r"\s+", "", v.lower()) if v is not None else inherited


def background(el: ET.Element, fill: str = "", dx: float = 0.0, dy: float = 0.0):
    """文書の順で最初の白い rect：(要素, 足し合わせた translate の x, y)。translate 以外の transform の中にあれば
    "transform"、なければ None。"""
    for c in el:
        tag = c.tag.replace(NS, "")
        if tag in NOT_DRAWN:
            continue
        f = fill_of(c, fill)
        tx, ty = dx, dy
        if c.get("transform"):
            m = TRANSLATE_RE.fullmatch(c.get("transform"))
            if not m:
                if tag == "rect" and f in WHITE or background(c, f) is not None:
                    return "transform"
                continue
            tx, ty = tx + float(m.group(1)), ty + float(m.group(2) or 0)
        if tag == "rect" and f in WHITE:
            return c, tx, ty
        r = background(c, f, tx, ty)
        if r is not None:
            return r
    return None


def length(v: str | None, ref: float) -> float | None:
    """rect の x・y・width・height の長さ（ない属性は 0。% は ref に対して）。px 以外の単位は None。"""
    if v is None:
        return 0.0
    m = re.fullmatch(rf"\s*({NUMBER})\s*(px|%)?\s*", v)
    if not m:
        return None
    x = float(m.group(1))
    return x * ref / 100 if m.group(2) == "%" else x


def background_gaps(root: ET.Element, box: tuple[float, float, float, float]) -> str | None:
    """白い背景が box（viewBox）を覆わないときの警告の文。"""
    bg = background(root, fill_of(root, ""))
    if bg is None:
        return "白い背景の rect がない（背景を白で塗る。透明だとダークモードで読めない）"
    if bg == "transform":
        return None
    el, tx, ty = bg
    bx, by, bw, bh = box
    x, y = length(el.get("x"), bw), length(el.get("y"), bh)
    w, h = length(el.get("width"), bw), length(el.get("height"), bh)
    if None in (x, y, w, h):
        return None
    x, y = x + tx, y + ty
    gaps = [("左", x - bx), ("上", y - by), ("右", bx + bw - (x + w)), ("下", by + bh - (y + h))]
    bad = [f"{k} {round(v, 2):g}" for k, v in gaps if v > GAP]
    if not bad:
        return None
    return (f"最初の白い rect（背景）が viewBox を覆わない（{'・'.join(bad)} が透けて、ダークモードで地の色が出る）。"
            f'<rect x="{bx:g}" y="{by:g}" width="{bw:g}" height="{bh:g}" fill="#ffffff"/> にする')


def check(path: Path) -> tuple[list[str], str | None]:
    """(警告の一覧, 読めないときの理由)。"""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return [], f"SVG として読めない: {e}"
    warns = []
    vb = root.get("viewBox")
    w, h = num(root.get("width")), num(root.get("height"))
    vbx = vby = vbw = vbh = None
    if vb:
        try:
            a = [float(x) for x in re.split(r"[ ,]+", vb.strip())]
            vbx, vby, vbw, vbh = a[0], a[1], a[2], a[3]
        except (ValueError, IndexError):
            warns.append(f"viewBox が読めない: {vb}")
    else:
        warns.append("viewBox がない")
    if root.get("width") is None or root.get("height") is None:
        warns.append("width・height がない（viewBox と同じ比で付ける）")
    elif w and h and vbw and vbh and abs(w / h - vbw / vbh) > 0.01 * vbw / vbh:
        warns.append(f"width:height（{w:g}:{h:g}）が viewBox（{vbw:g}:{vbh:g}）と比が違う")
    width = w or vbw
    if width and width > MAX_WIDTH:
        warns.append(f"幅 {width:g} が目安（400 程度）を超える（横に広いものは2枚に分ける）")
    out: list[tuple[float, str]] = []
    texts(root, 16.0, 1.0, out)
    if not any(el.tag.replace(NS, "") == "text" for el in root.iter()):
        warns.append("<text> がない（文字はテキストのまま置く。図形だけの図なら、このままでよい）")
    base = vbw or w
    if base:
        shown = min(w, AVAIL) if w else AVAIL
        sc = shown / base
        small = [(f * sc, t) for f, t in out if f * sc < MIN_TEXT]
        if small:
            mn = min(e for e, _ in small)
            ex = "・".join(t for _, t in small[:3])
            warns.append(f"幅 {AVAIL:g}px で {MIN_TEXT:g}px 未満の文字が {len(small)} 個（最小 {mn:.1f}px。例：{ex}）")
    box = (vbx, vby, vbw, vbh) if vbw and vbh else ((0.0, 0.0, w, h) if not vb and w and h else None)
    if box and (msg := background_gaps(root, box)):
        warns.append(msg)
    return warns, None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", type=Path, help="調べる SVG（なければ docs/img の全部）")
    parser.add_argument("--page", action="append", default=[], help="そのページの図だけ（id。くり返し・カンマ区切り可）")
    parser.add_argument("--strict", action="store_true", help="警告があれば終了コード 1")
    parser.add_argument("--root", type=Path, help="置き場所の根（既定はこのリポジトリ）")
    args = parser.parse_args(argv)
    root = (args.root or ROOT).resolve()
    img = root / IMG_DIR
    if args.files:
        targets = [p.resolve() for p in args.files]
    else:
        ids = [x.strip() for v in args.page for x in v.split(",") if x.strip()]
        dirs = [img / i for i in ids] if ids else [img]
        targets = sorted(p for d in dirs if d.is_dir() for p in d.rglob("*.svg"))
    n_warn = n_files = 0
    errors = []
    for p in targets:
        warns, err = check(p)
        rel = p.relative_to(root) if p.is_relative_to(root) else p
        if err:
            errors.append(f"{rel}: {err}")
            continue
        if warns:
            n_files += 1
            n_warn += len(warns)
            for w in warns:
                print(f"警告: {rel}: {w}")
    for e in errors:
        print("エラー: " + e)
    print(f"図 {len(targets)} 枚・警告 {n_warn} 件（{n_files} 枚）・エラー {len(errors)} 件")
    return 1 if errors or (args.strict and n_warn) else 0


if __name__ == "__main__":
    sys.exit(main())
