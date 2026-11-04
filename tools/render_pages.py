#!/usr/bin/env python3
"""ビルドしたサイトのページを手元のヘッドレスの Chrome で描き、描いたときにだけ分かる崩れと、外のサイトへの
問い合わせを数える（設計書 §8.6 の「描画」の行・§8.5「外から読まない」）。

kyopro-atlas の tools/render_pages.py（同じ作者、MIT）を写して直したもの。数式（KaTeX）・動く図・ロードマップの集計の
検査は外し（claude-atlas にない）、外への問い合わせ（build-B1.md の提案4。tests/site/test_site_browser.py と同じく、
127.0.0.1 のほかの名前を引けなくした Chrome で、ページが読みに行った URL を見る）と、Mermaid の写しで図が描かれるかを
足した。Chrome の探し方と日本語のフォントの足し方は kyopro-atlas の tools/render_svg.py から写した。

使い方:
  uv run mkdocs build -d DIR/site                       先に作業用フォルダへビルドする（リポジトリの site/ には書かない）
  uv run python tools/render_pages.py DIR/site          全ページを幅 390px のライトとダークで開いて数える
  uv run python tools/render_pages.py DIR/site --page how-to-use --page symptoms/instructions-ignored
                                                        そのページだけ（id・URL のパス・docs/ のパス。くり返し・カンマ区切り可）
  uv run python tools/render_pages.py DIR/site --field symptoms   その分野（URL の最初のフォルダ）のページだけ
  uv run python tools/render_pages.py DIR/site --changed          git で変わったファイルに関わるページだけ（既定は
                                                        origin/main との分かれ目からの変更と、コミットしていない変更・
                                                        追跡していないファイル。下の「変えたページ」）
  uv run python tools/render_pages.py DIR/site --json DIR/render.json   指摘の一覧とページごとの数を JSON に書く
  uv run python tools/render_pages.py DIR/site --width 360,390 --scheme dark
                                                        幅（px。くり返し・カンマ区切り可。既定 390）と配色（light・dark。既定は両方）
  uv run python tools/render_pages.py DIR/site -j 8     同時に開くタブの数（既定 4。Chrome は 1 つ）
  uv run python tools/render_pages.py DIR/site -v       警告も全件を出す（既定は種類ごとに 3 件と件数）
  uv run python tools/render_pages.py DIR/site --chrome PATH  Chrome の場所（既定は環境変数 CA_CHROME、CHROME、
                                                        ~/.cache/puppeteer の chrome-headless-shell、chrome、PATH の順に探す）
終了コード: エラーがあれば 1（--strict なら警告だけでも 1）、なければ 0。Chrome がない・サイトがないときは 2

配り方: 127.0.0.1 の空いたポートで、sitemap.xml の URL のパス（/claude-atlas/）の下に配る（404.html は絶対パスで読むため）。
Chrome は --host-resolver-rules で 127.0.0.1 のほかの名前を引けなくして起動する（外へは実際には出ない）。ページが読みに
行った URL（CDP の Network.requestWillBeSent）のうち、配ったオリジンでないもの（data:・blob: などを除く）を
「外への問い合わせ」として数える。日本語のフォントは、fontconfig になければ WSL の Windows のフォントを足す。

Chrome の使い方: Chrome は 1 つだけ起動し、-j 個のタブを並べて開く。タブは 1 ページ・1 つの幅ごとに、新しい browser
context（別のプロファイルのようなもの。localStorage・キャッシュも別）の中に開き、調べ終えたら context ごと閉じる
（同じタブで開き直し続けると描画のプロセスにメモリがたまる。kyopro-atlas の #100）。

1 ページの調べ方: 画面を幅 W・高さ 844 のスマートフォン（mobile）にし、配色（prefers-color-scheme）を合わせて開く。
読み込みの後、Mermaid（15 秒まで）・画像（8 秒まで）・フォントを待ち、折りたたみ（details）を開き、タブの中身をすべて
見せてから測る（閉じた中身は読者が開いたときの形で見る。指摘に「折りたたみの中」「タブの中」と添える）。同じ幅のほかの
配色は、読み込み直さずに prefers-color-scheme だけを替え、Material が data-md-color-scheme を替え終わるのを待って調べ直す
（mkdocs.yml の palette の最初が「システムの設定に従う」なので、Material は prefers-color-scheme の変化に合わせて替える）。

エラー（公開すると崩れて見える・決まりに反する）
  外への問い合わせ      配ったサイトのほかの URL を読みに行った（フォント・Mermaid・画像・スクリプト・GitHub の API など）
  描かれない Mermaid の図  pre.mermaid が残る（写し overrides/assets/vendor/ と mermaid-local.js が働いていない）
  地の文に残った記法    本文の文字（コードと図の外）に残った ![・](・**・{#…}・{:…}・<!--、描かれなかった囲み・タブ・折りたたみの
                        印（!!! "…"・=== "…"・??? "…"）。.svg を指し、画像を包まないリンクも出す
  ページの横ずれ        document.documentElement.scrollWidth が画面の幅を超える。はみ出した要素（親ははみ出さず、横に
                        スクロールする入れ物・position: fixed の中でないもの）を右端の遠い順に 5 つまで出す
  読めない画像          <img> の読み込みが終わらない、または naturalWidth が 0 で decode できない
  開けないページ        読み込みが終わらない・検査の JS が止まった（タブを開き直して 1 回だけやり直す）
警告（読めるが直したい）
  画面の幅を超える表    表の右端が、横スクロールの入れ物 .md-typeset__scrollwrap（なければ親）の見える右端を超える
  縁が透ける図          SVG の画像を元の大きさで canvas に描き、上下左右の端から続く「半分より多い画素が透明な行・列」の幅を出す
                        （ダークモードで暗い帯になり、端の文字が読めない）
  JS のエラー           例外・console.error・読み込めないファイル（Log の error。配ったサイトの URL のものだけ。外の URL は
                        「外への問い合わせ」に出す）
変えたページ（--changed）: git の差分のファイルから、描き直すページを選ぶ（changed_pages）。
  docs/<…>.md               そのページ（gen_site.py の生成物も docs/ にあるので、data/ の変更は生成物の差分で拾う）
  snippets/<id>/…           id が <id> のページと、本文にそのファイル（snippets/ からのパス）を書いたページ
  docs/img/<id>/…           id が <id> のページと、本文にそのファイル（img/<id>/…）を書いたページ
  overrides/404.html        404.html
  共有のファイル            mkdocs.yml・nav.yml・pyproject.toml・uv.lock・overrides/ のほかのファイル・docs/assets/ と
                            docs/ のほかのファイル（docs/llms.txt を除く）。どのページにも効くので、全ページを流す
  そのほか（tools/・tests/・planning/・data/・stubs/ など）はサイトの見た目を変えないので見ない
同じ要素の同じ指摘が幅・配色の違う回に出たときは 1 件にまとめ、出た回を添える（例：［390 ライト・390 ダーク］）。
幅は手元のフォントで測るので、実機と数 px 違うことがある。標準ライブラリだけで動く（Chrome DevTools Protocol を WebSocket で話す）。
"""
from __future__ import annotations

import argparse
import base64
import collections
import html
import http.server
import json
import os
import queue
import re
import shutil
import signal
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEIGHT = 844                 # 画面の高さ（px）
WAIT_MS = 8000               # 画像を待つ上限
WAIT_MERMAID_MS = 15000      # Mermaid を待つ上限
MAX_CULPRITS = 5             # 横ずれのページで出す、はみ出した要素の数
CLEAR_FRAC = 0.5             # 縁の 1 行・1 列のうち、これより多くの画素が透明なら透ける帯とみなす
RESOLVER_RULES = "MAP * ~NOTFOUND, EXCLUDE 127.0.0.1"   # 127.0.0.1 のほかの名前を引けなくする（外へ出ない）
LOCAL_SCHEMES = ("data:", "blob:", "about:", "chrome:", "chrome-extension:", "devtools:", "javascript:")
SCHEME_NAMES = {"light": "ライト", "dark": "ダーク"}
SCHEME_ATTR = {"light": "default", "dark": "slate"}      # Material の data-md-color-scheme

# 種類：(表示名, 重さ)。並びは出力の順
KINDS = {
    "outside-request": ("外への問い合わせ", "error"),
    "mermaid-unrendered": ("描かれない Mermaid の図", "error"),
    "leaked-markup": ("地の文に残った記法", "error"),
    "page-overflow": ("ページの横ずれ", "error"),
    "img-broken": ("読めない画像", "error"),
    "load-failed": ("開けないページ", "error"),
    "wide-table": ("画面の幅を超える表", "warning"),
    "img-transparent": ("縁が透ける図", "warning"),
    "js-error": ("JS のエラー", "warning"),
}
SEVERITY_NAMES = {"error": "エラー", "warning": "警告"}

# 地の文に残ると崩れている記法（JS の正規表現）：画像とリンクの記法・太字の印・attr_list・HTML のコメント・
# 描かれなかった囲み（!!!）・タブ（===）・折りたたみ（???）の印
LEAK_RE = r"!\[|\]\(|\*\*|\{[#:][^}]*\}|<!--|(?:^|\s)(?:!!!|\?\?\?\+?) \w|(?:^|\s)=== \""

# Chrome の探し方（kyopro-atlas の render_svg.py を写し、環境変数 CA_CHROME を足した。tests/site と同じ名前）
INSTALL_HINT = ("ヘッドレスの Chrome が見つからない。次のどれかで用意する:\n"
                "  npx @puppeteer/browsers install chrome-headless-shell@stable --path ~/.cache/puppeteer\n"
                "または --chrome か環境変数 CA_CHROME（CHROME）で場所を渡す")
WIN_FONTS = Path("/mnt/c/Windows/Fonts")
FC_CACHE = Path.home() / ".cache" / "claude-atlas-fontconfig"   # Windows のフォントの索引（2回目から速い）

# ページの中で動かす検査（Runtime.evaluate。async の関数に cfg を渡す）。結果は JSON にできる値で返す
PROBE = r"""
async (cfg) => {
  const T0 = performance.now();
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const all = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  const until = async (cond, ms) => {
    for (;;) {
      let ok = false;
      try { ok = cond(); } catch (e) { ok = false; }
      if (ok) return true;
      if (performance.now() - T0 > ms) return false;
      await sleep(50);
    }
  };
  const frames = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
  const clip = (s, n) => {
    s = String(s == null ? "" : s).replace(/\s+/g, " ").trim();
    return s.length > n ? s.slice(0, n - 1) + "…" : s;
  };

  // 1. 描き終わるのを待つ（同じ読み込みで配色を替えて調べ直すときは、Material が配色を替え終わるのも待つ）
  const waited = {};
  if (cfg.scheme && document.body && document.body.hasAttribute("data-md-color-scheme")) {
    await until(() => document.body.getAttribute("data-md-color-scheme") === cfg.scheme, cfg.wait);
  }
  waited.mermaid = await until(() => !document.querySelector("pre.mermaid"), cfg.waitMermaid);
  all('img[loading="lazy"]').forEach((i) => { i.loading = "eager"; });
  waited.img = await until(() => all("img").every((i) => i.complete), cfg.wait);

  // 2. 閉じた中身を見せる（折りたたみを開き、タブの中身をすべて出す）。調べ直すときは、最初に閉じていたものを使う
  if (!window.__caClosed) {
    window.__caClosed = all("details:not([open])");
    window.__caClosed.forEach((d) => { d.open = true; });
    const style = document.createElement("style");
    style.textContent = ".md-typeset .tabbed-set > .tabbed-content > .tabbed-block { display: block !important; }";
    document.head.appendChild(style);
  }
  const closed = window.__caClosed;
  try { await document.fonts.ready; } catch (e) { /* 測るのは続ける */ }
  await frames();

  const doc = document.documentElement;
  const vw = doc.clientWidth;
  const content = document.querySelector(".md-content") || document.body;
  const heads = all("h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]", content);
  const headingOf = (el) => {
    let id = "";
    if (!content.contains(el)) return id;
    for (const h of heads) {
      if (h === el || (h.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) id = h.id;
      else break;
    }
    return id;
  };
  const place = (el) => {
    if (closed.some((d) => d.contains(el))) return "折りたたみの中";
    const tb = el.closest(".tabbed-block");
    if (tb && tb.parentElement && tb !== tb.parentElement.firstElementChild) return "タブの中";
    return "";
  };
  const items = {};
  const add = (kind, el, o) => {
    (items[kind] = items[kind] || []).push(Object.assign({ h: el ? headingOf(el) : "", where: el ? place(el) : "" }, o));
  };
  const counts = { tables: 0, img: all("img").length, mermaid: all(".mermaid").length,
                   details: closed.length, tabs: all(".tabbed-set").length };

  // 3. 地の文に残った記法
  const SKIP = "code, pre, kbd, samp, script, style, textarea, svg, .mermaid, .headerlink";
  const leak = new RegExp(cfg.leak);
  const tw = document.createTreeWalker(content, NodeFilter.SHOW_TEXT);
  for (let n = tw.nextNode(); n; n = tw.nextNode()) {
    const s = n.nodeValue;
    const m = s ? leak.exec(s) : null;
    if (!m || !n.parentElement || n.parentElement.closest(SKIP)) continue;
    const i = m.index;
    add("leaked-markup", n.parentElement, { mark: m[0].trim(), text: clip((i > 24 ? "…" : "") + s.slice(Math.max(0, i - 24), i + 36), 80) });
  }
  all("a[href]", content).forEach((a) => {
    if (/\.svg(?:$|[?#])/i.test(a.getAttribute("href")) && !a.querySelector("img")) {
      add("leaked-markup", a, { mark: "図へのリンク", text: clip(a.textContent, 60) + " → " + a.getAttribute("href") });
    }
  });

  // 4. 表（入れ物の見える右端より右に出るもの）
  const visibleRight = (box) => box.getBoundingClientRect().left + box.clientLeft + box.clientWidth;
  all("table", content).forEach((t) => {
    if (t.closest(".highlight, pre")) return;
    counts.tables++;
    const box = t.closest(".md-typeset__scrollwrap") || t.parentElement;
    if (!box || !box.clientWidth) return;
    const q = t.getBoundingClientRect();
    const lim = Math.min(visibleRight(box), vw);
    if (q.right > lim + 1) {
      const row = (t.tHead && t.tHead.rows[0]) || t.rows[0];
      const head = row ? Array.from(row.cells).map((c) => clip(c.textContent, 24)).join(" | ") : "";
      add("wide-table", t, { head: clip(head, 70), width: Math.round(q.width), box: box.clientWidth,
                             hidden: Math.round(q.right - lim), cols: row ? row.cells.length : 0 });
    }
  });

  // 5. Mermaid（Material が描くと pre.mermaid が div.mermaid に替わる）
  all("pre.mermaid").forEach((el) => add("mermaid-unrendered", el, { text: clip(el.textContent, 60) }));

  // 6. 画像（読めないもの。SVG は縁の透ける帯）
  for (const img of all("img")) {
    const src = img.getAttribute("src") || "";
    const alt = clip(img.getAttribute("alt"), 60);
    if (!img.complete) { add("img-broken", img, { src, alt, msg: "読み込みが終わらない" }); continue; }
    if (img.naturalWidth === 0) {
      let ok = true;
      try { await img.decode(); } catch (e) { ok = false; }
      if (!ok) { add("img-broken", img, { src, alt, msg: "読めない（naturalWidth が 0）" }); continue; }
    }
    let path = "";
    try { path = new URL(img.currentSrc || img.src, location.href).pathname; } catch (e) { path = ""; }
    const w = img.naturalWidth, h = img.naturalHeight;
    if (!/\.svg$/i.test(path) || w < 4 || h < 4 || w * h > 16e6) continue;
    const c = document.createElement("canvas");
    c.width = w; c.height = h;
    const g = c.getContext("2d", { willReadFrequently: true });
    let d;
    try { g.drawImage(img, 0, 0, w, h); d = g.getImageData(0, 0, w, h).data; } catch (e) { continue; }
    const clearX = (x, y0, y1) => { let k = 0; for (let y = y0; y < y1; y++) if (d[(y * w + x) * 4 + 3] < 8) k++; return k; };
    const clearY = (y, x0, x1) => { let k = 0; for (let x = x0; x < x1; x++) if (d[(y * w + x) * 4 + 3] < 8) k++; return k; };
    const band = (n, lineClear, len) => { let t = 0; while (t < n && lineClear(t) > cfg.clearFrac * len) t++; return t; };
    const sides = {};
    const top = band(h, (t) => clearY(t, 0, w), w);
    const bottom = band(h, (t) => clearY(h - 1 - t, 0, w), w);
    const left = band(w, (t) => clearX(t, 0, h), h);
    const right = band(w, (t) => clearX(w - 1 - t, 0, h), h);
    if (top) sides["上"] = top;
    if (bottom) sides["下"] = bottom;
    if (left) sides["左"] = left;
    if (right) sides["右"] = right;
    if (Object.keys(sides).length) add("img-transparent", img, { src, alt, sides, size: w + "×" + h });
  }

  // 7. ページの横ずれ（はみ出した要素：親がはみ出さず、横にスクロールする入れ物・position: fixed の中でないもの）
  const sw = doc.scrollWidth;
  let culprits = 0;
  if (sw > vw + 1) {
    const cs = new Map();
    const st = (el) => { let s = cs.get(el); if (!s) { s = getComputedStyle(el); cs.set(el, s); } return s; };
    const escapes = (el) => {
      for (let a = el; a && a !== document.body && a !== doc; a = a.parentElement) {
        const s = st(a);
        if (s.position === "fixed") return false;
        if (a !== el && s.overflowX !== "visible") return false;
      }
      return true;
    };
    const right = (el) => el.getBoundingClientRect().right;
    const sticks = (el) => { const b = el.getBoundingClientRect(); return (b.width > 0 || b.height > 0) && b.right > vw + 1; };
    const over = [];
    for (const el of all("body *")) {
      if (!sticks(el) || !escapes(el)) continue;
      const p = el.parentElement;
      if (p && p !== document.body && sticks(p) && escapes(p)) continue;
      over.push(el);
    }
    over.sort((a, b) => right(b) - right(a));
    const describe = (el) => {
      const t = el.closest("table");
      if (t) return "表 " + clip((t.rows[0] || t).textContent, 60);
      const cls = Array.from(el.classList).slice(0, 3).map((c) => "." + c).join("");
      return "<" + el.tagName.toLowerCase() + (el.id ? "#" + el.id : "") + cls + "> " + clip(el.textContent, 60);
    };
    culprits = over.length;
    over.slice(0, cfg.maxCulprits).forEach((el) => add("page-overflow", el, { what: describe(el), over: Math.round(right(el) - vw) }));
    if (!over.length) add("page-overflow", null, { what: "（はみ出した要素を特定できない）", over: sw - vw });
  }

  return {
    title: document.title, scheme: document.body ? document.body.getAttribute("data-md-color-scheme") : null,
    vw, sw, culprits, waited, counts, items, ms: Math.round(performance.now() - T0),
  };
}
"""


# ---------------------------------------------------------------- Chrome とフォント


def find_chrome(given: str | None) -> Path | None:
    """--chrome、環境変数 CA_CHROME・CHROME、~/.cache/puppeteer の chrome-headless-shell・chrome、PATH の順に探す。"""
    for c in (given, os.environ.get("CA_CHROME"), os.environ.get("CHROME")):
        if c:
            p = Path(c).expanduser()
            if p.is_file() and os.access(p, os.X_OK):
                return p
            w = shutil.which(c)
            return Path(w) if w else None
    cache = Path.home() / ".cache" / "puppeteer"
    for pattern in ("chrome-headless-shell/*/*/chrome-headless-shell", "chrome/*/*/chrome"):
        found = sorted((p for p in cache.glob(pattern) if p.is_file() and os.access(p, os.X_OK)),
                       key=lambda p: [int(x) if x.isdigit() else 0 for x in re.split(r"[.-]", p.parent.parent.name)])
        if found:
            return found[-1]                       # 新しい版
    for name in ("chrome-headless-shell", "google-chrome", "chromium", "chromium-browser"):
        w = shutil.which(name)
        if w:
            return Path(w)
    return None


def font_env(work: Path) -> tuple[dict[str, str] | None, str | None]:
    """日本語のフォントがなければ、WSL の Windows のフォントを足した fontconfig の設定を作る。(環境, 注意) を返す。"""
    try:
        r = subprocess.run(["fc-list", ":lang=ja"], capture_output=True, text=True, timeout=30)
        if r.stdout.strip():
            return None, None
    except (OSError, subprocess.TimeoutExpired):
        pass
    if WIN_FONTS.is_dir():
        conf = work / "fonts.conf"
        conf.write_text(
            "<?xml version='1.0'?><!DOCTYPE fontconfig SYSTEM 'fonts.dtd'><fontconfig>"
            "<include ignore_missing='yes'>/etc/fonts/fonts.conf</include>"
            f"<dir>{html.escape(str(WIN_FONTS))}</dir><cachedir>{html.escape(str(FC_CACHE))}</cachedir>"
            "</fontconfig>", encoding="utf-8")
        return {**os.environ, "FONTCONFIG_FILE": str(conf)}, f"日本語のフォントがないので {WIN_FONTS} を足して描く"
    return None, "注意: 日本語のフォントが見つからない。日本語は豆腐（□）になり、幅の測り方が実機と違う（fonts-noto-cjk などを入れる）"


# ---------------------------------------------------------------- WebSocket と Chrome DevTools Protocol


def _xor(data: bytes, mask: bytes) -> bytes:
    """WebSocket のマスク（4 バイトのくり返しとの排他的論理和）。"""
    n = len(data)
    if not n:
        return b""
    key = (mask * (n // 4 + 1))[:n]
    return (int.from_bytes(data, "little") ^ int.from_bytes(key, "little")).to_bytes(n, "little")


def encode_frame(opcode: int, payload: bytes, mask: bytes | None = None) -> bytes:
    """client から送るフレーム（FIN を立て、マスクする）。"""
    mask = os.urandom(4) if mask is None else mask
    n = len(payload)
    head = bytearray([0x80 | opcode])
    if n < 126:
        head.append(0x80 | n)
    elif n < 1 << 16:
        head.append(0x80 | 126)
        head += struct.pack(">H", n)
    else:
        head.append(0x80 | 127)
        head += struct.pack(">Q", n)
    return bytes(head) + mask + _xor(payload, mask)


class WebSocket:
    """CDP に要るだけの WebSocket（RFC 6455）の client。テキストのメッセージを送り、受ける。"""

    def __init__(self, url: str, timeout: float = 30.0):
        u = urllib.parse.urlsplit(url)
        self.sock = socket.create_connection((u.hostname, u.port or 80), timeout=timeout)
        self.buf = bytearray()
        self.parts: list[bytes] = []
        try:
            self._handshake(u, timeout)
        except BaseException:
            self.sock.close()
            raise

    def _handshake(self, u: urllib.parse.SplitResult, timeout: float) -> None:
        key = base64.b64encode(os.urandom(16)).decode()
        path = (u.path or "/") + (f"?{u.query}" if u.query else "")
        self.sock.sendall((f"GET {path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        while b"\r\n\r\n" not in self.buf:
            self._more(timeout)
        end = self.buf.index(b"\r\n\r\n")
        status = bytes(self.buf[:end]).split(b"\r\n", 1)[0].decode("latin-1")
        del self.buf[:end + 4]
        if status.split()[1:2] != ["101"]:
            raise ConnectionError(f"WebSocket に切り替わらない（{status}）")

    def _more(self, timeout: float) -> None:
        self.sock.settimeout(max(timeout, 0.001))
        chunk = self.sock.recv(1 << 16)
        if not chunk:
            raise ConnectionError("WebSocket の接続が切れた")
        self.buf += chunk

    def _take(self, n: int, timeout: float = 60.0) -> bytes:
        while len(self.buf) < n:
            self._more(timeout)
        data = bytes(self.buf[:n])
        del self.buf[:n]
        return data

    def send(self, text: str) -> None:
        self.sock.sendall(encode_frame(0x1, text.encode()))

    def recv(self, timeout: float) -> str:
        """次のテキストのメッセージ。timeout 秒のうちにフレームが始まらなければ TimeoutError。"""
        while True:
            while len(self.buf) < 2:
                self._more(timeout)
            b0, b1 = self._take(2)
            n = b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._take(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._take(8))[0]
            mask = self._take(4) if b1 & 0x80 else None
            data = self._take(n)
            if mask:
                data = _xor(data, mask)
            op = b0 & 0x0F
            if op == 0x8:
                raise ConnectionError("WebSocket が閉じられた")
            if op == 0x9:
                self.sock.sendall(encode_frame(0xA, data))
                continue
            if op == 0xA:
                continue
            self.parts.append(data)
            if b0 & 0x80:
                msg = b"".join(self.parts)
                self.parts.clear()
                return msg.decode("utf-8", errors="replace")

    def close(self) -> None:
        try:
            self.sock.sendall(encode_frame(0x8, b""))
        except OSError:
            pass
        self.sock.close()


class CDPError(RuntimeError):
    pass


class Tab:
    """1 つのページ（target）との CDP の会話。命令の答えを待つ間に来たイベントは events にためる。"""

    def __init__(self, ws_url: str):
        self.ws = WebSocket(ws_url)
        self.next_id = 0
        self.events: list[dict] = []

    def _recv(self, deadline: float) -> dict:
        left = deadline - time.monotonic()
        if left <= 0:
            raise TimeoutError("Chrome の答えが来ない")
        return json.loads(self.ws.recv(left))

    def call(self, method: str, params: dict | None = None, timeout: float = 30.0) -> dict:
        self.next_id += 1
        mid = self.next_id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        deadline = time.monotonic() + timeout
        while True:
            msg = self._recv(deadline)
            if msg.get("id") == mid:
                if "error" in msg:
                    raise CDPError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result", {})
            if "method" in msg:
                self.events.append(msg)

    def wait_event(self, method: str, timeout: float) -> dict:
        deadline = time.monotonic() + timeout
        while True:
            for e in self.events:
                if e["method"] == method:
                    return e
            msg = self._recv(deadline)
            if "method" in msg:
                self.events.append(msg)

    def close(self) -> None:
        self.ws.close()


NO_PROXY = urllib.request.build_opener(urllib.request.ProxyHandler({}))


@dataclass
class Page:
    """使い捨てのタブ（1 ページ・1 つの幅）。browser context ごと閉じる。"""
    tab: Tab
    context: str
    scheme: str | None = None


class Browser:
    """ヘッドレスの Chrome を 1 つ起動し、browser の target につなぐ。プロファイルは一時フォルダ（閉じると消す）。"""

    def __init__(self, chrome: Path, env: dict[str, str] | None, work: Path):
        self.dir = Path(tempfile.mkdtemp(prefix="chrome-", dir=work))
        self.log = open(self.dir / "chrome.log", "wb")
        args = [str(chrome), "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--no-first-run",
                "--no-default-browser-check", "--disable-extensions", "--mute-audio",
                "--disable-background-timer-throttling", "--disable-renderer-backgrounding",
                "--disable-backgrounding-occluded-windows", f"--host-resolver-rules={RESOLVER_RULES}",
                f"--user-data-dir={self.dir / 'profile'}",
                "--remote-debugging-port=0", f"--window-size=390,{HEIGHT}", "about:blank"]
        self.proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=self.log, stderr=self.log, env=env,
                                     start_new_session=True)
        self.conn: Tab | None = None
        self.lock = threading.Lock()
        self.closed = False
        try:
            self.port = self._port()
            with NO_PROXY.open(f"http://127.0.0.1:{self.port}/json/version", timeout=10) as r:
                self.conn = Tab(json.load(r)["webSocketDebuggerUrl"])
        except BaseException:
            self.close()
            raise

    def _port(self) -> int:
        f = self.dir / "profile" / "DevToolsActivePort"
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            if self.proc.poll() is not None:
                tail = (self.dir / "chrome.log").read_text(errors="replace").strip().split("\n")[-3:]
                raise RuntimeError(f"Chrome が起動しない（終了コード {self.proc.returncode}）" +
                                   ("\n  " + "\n  ".join(tail) if any(tail) else ""))
            try:
                lines = f.read_text().split()
                if len(lines) >= 2:
                    return int(lines[0])
            except (OSError, ValueError):
                pass
            time.sleep(0.05)
        raise RuntimeError("Chrome が 30 秒で起動しない")

    def call(self, method: str, params: dict | None = None) -> dict:
        with self.lock:
            if self.conn is None:
                raise ConnectionError("Chrome を閉じた")
            try:
                return self.conn.call(method, params)
            finally:
                self.conn.events.clear()

    def open_page(self) -> Page:
        """新しい browser context にタブを 1 つ開いてつなぐ（読みに行く URL を見るため Network も有効にする）。"""
        ctx = self.call("Target.createBrowserContext", {"disposeOnDetach": True})["browserContextId"]
        try:
            tid = self.call("Target.createTarget", {"url": "about:blank", "browserContextId": ctx})["targetId"]
            tab = Tab(f"ws://127.0.0.1:{self.port}/devtools/page/{tid}")
        except BaseException:
            self.call("Target.disposeBrowserContext", {"browserContextId": ctx})
            raise
        page = Page(tab, ctx)
        try:
            for m in ("Page.enable", "Runtime.enable", "Log.enable"):
                tab.call(m)
            tab.call("Network.enable", {"maxTotalBufferSize": 1 << 20, "maxResourceBufferSize": 1 << 16})
        except BaseException:
            self.close_page(page)
            raise
        return page

    def close_page(self, page: Page) -> None:
        try:
            page.tab.close()
        except OSError:
            pass
        self.call("Target.disposeBrowserContext", {"browserContextId": page.context})

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        if self.conn:
            try:
                self.conn.close()
            except OSError:
                pass
        if self.proc.poll() is None:
            try:
                os.killpg(self.proc.pid, signal.SIGTERM)
                self.proc.wait(5)
            except (OSError, subprocess.TimeoutExpired):
                try:
                    os.killpg(self.proc.pid, signal.SIGKILL)
                except OSError:
                    pass
        self.log.close()
        shutil.rmtree(self.dir, ignore_errors=True)


# ---------------------------------------------------------------- サイトを配る


def site_prefix(site: Path) -> str:
    """sitemap.xml の URL に共通のパス（例 /claude-atlas/）。読めなければ /。"""
    try:
        locs = [e.text.strip() for e in ET.parse(site / "sitemap.xml").getroot().iter() if e.tag.endswith("loc") and e.text]
    except (OSError, ET.ParseError):
        return "/"
    paths = [urllib.parse.urlsplit(x).path for x in locs]
    if not paths:
        return "/"
    pre = os.path.commonprefix(paths)
    pre = pre[:pre.rfind("/") + 1] if "/" in pre else "/"
    return pre if pre.startswith("/") else "/" + pre


class QuietServer(http.server.ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address) -> None:
        pass


def serve(site: Path, prefix: str) -> tuple[QuietServer, str]:
    """site を http://127.0.0.1:<空いたポート><prefix> で配る。(server, その URL)。"""
    class Handler(http.server.SimpleHTTPRequestHandler):
        extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                          ".js": "text/javascript", ".mjs": "text/javascript", ".json": "application/json",
                          ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff", ".wasm": "application/wasm"}

        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(site), **kw)

        def translate_path(self, path: str) -> str:
            p = urllib.parse.urlsplit(path).path
            if not p.startswith(prefix):
                return str(site / "__ca-render-pages-not-found__")
            return super().translate_path("/" + p[len(prefix):])

        def log_message(self, *a) -> None:
            pass

    server = QuietServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}{prefix}"


@dataclass
class SitePage:
    path: str                      # サイトの中の URL のパス（"symptoms/instructions-ignored/"、トップは ""、"404.html"）
    source: str | None = None      # 元の Markdown（docs/symptoms/instructions-ignored.md）。docs/ になければ None

    @property
    def label(self) -> str:
        return self.path or "/（トップ）"


def list_pages(site: Path, docs: Path | None = None) -> list[SitePage]:
    """site の index.html（と 404.html）のページを URL のパスの順に。assets/ と search/ の下は見ない。"""
    out = []
    for f in site.rglob("index.html"):
        rel = f.parent.relative_to(site).as_posix()
        if rel.split("/")[0] in ("assets", "search"):
            continue
        out.append(SitePage("" if rel == "." else rel + "/"))
    out.sort(key=lambda p: p.path)
    if (site / "404.html").is_file():
        out.append(SitePage("404.html"))
    if docs and docs.is_dir():
        for p in out:
            stem = p.path.rstrip("/")
            cands = ["index.md"] if not stem else [f"{stem}.md", f"{stem}/index.md"]
            for c in cands:
                if (docs / c).is_file():
                    p.source = f"docs/{c}"
                    break
    return out


def aliases(p: SitePage) -> tuple[set[str], str]:
    """(パスとしての名前, id)。id は URL の最後のフォルダ（docs/<field>/<id>.md の id）。トップは "index"。"""
    stem = p.path.rstrip("/")
    names = {p.path, stem, "/" + p.path, "/" + stem}
    if not stem:
        names.add("/")
    if p.source:
        names |= {p.source, p.source[len("docs/"):]}
    return {n for n in names if n}, (stem.rsplit("/", 1)[-1] if stem else "index")


def select_pages(pages: list[SitePage], want_pages: list[str], want_fields: list[str]) -> list[SitePage]:
    """--page・--field で絞る。どちらもなければ全部。合わない値があれば SystemExit。"""
    if not want_pages and not want_fields:
        return pages
    tops = {p.path.split("/")[0] for p in pages if "/" in p.path}
    keep: set[str] = set()
    for f in want_fields:
        if f not in tops:
            sys.exit(f"--field {f}: その分野のページがない（あるもの：{'・'.join(sorted(tops))}）")
        keep |= {p.path for p in pages if p.path.split("/")[0] == f}
    for x in want_pages:
        hit = [p.path for p in pages if x in aliases(p)[0]] or [p.path for p in pages if x == aliases(p)[1]]
        if not hit:
            sys.exit(f"--page {x}: そのページがない（id・URL のパス・docs/ のパスで書く）")
        keep |= set(hit)
    return [p for p in pages if p.path in keep]


# ---------------------------------------------------------------- 変えたページ（--changed）

SHARED = ("mkdocs.yml", "nav.yml", "pyproject.toml", "uv.lock")     # どのページにも効くファイル


def git_changed(top: Path, ref: str) -> tuple[list[str], str]:
    """top のリポジトリで、ref との分かれ目（merge-base）から変わったファイル（コミットしていない変更・追跡していない
    ファイルも。消したもの・名前を変えたものは両方の名前）。(top からのパス, 分かれ目の短い名前)。読むだけの git を使う。"""
    def git(*a: str) -> str:
        cp = subprocess.run(["git", "-C", str(top), *a], capture_output=True, text=True)
        if cp.returncode:
            sys.exit(f"--changed: git {' '.join(a)} が失敗した（{cp.stderr.strip()}）")
        return cp.stdout
    try:
        mb = git("merge-base", "HEAD", ref).strip()
    except FileNotFoundError:
        sys.exit("--changed: git がない")
    files = git("diff", "--name-only", "--no-renames", "-z", mb).split("\0")
    files += git("ls-files", "--others", "--exclude-standard", "-z").split("\0")
    return sorted({f for f in files if f}), mb[:9]


def changed_pages(files: list[str], pages: list[SitePage], docs: Path) -> tuple[list[str], list[str]]:
    """変わったファイル（リポジトリの根からのパス）から、描き直すページを選ぶ（docstring の「変えたページ」）。
    (ページのパス, 共有のファイル)。共有のファイルが 1 つでもあれば、ページは全部。docs はページの Markdown を読む場所。"""
    ids: dict[str, list[str]] = collections.defaultdict(list)
    for p in pages:
        ids[aliases(p)[1]].append(p.path)
    texts: dict[str, str] = {}

    def text(p: SitePage) -> str:
        if p.path not in texts:
            try:
                texts[p.path] = (docs / p.source[len("docs/"):]).read_text(encoding="utf-8") if p.source else ""
            except OSError:
                texts[p.path] = ""
        return texts[p.path]

    def citing(*marks: str) -> set[str]:
        return {p.path for p in pages if any(m in text(p) for m in marks)}

    keep: set[str] = set()
    shared = []
    for f in files:
        parts = f.split("/")
        if f in SHARED:
            shared.append(f)
        elif parts[0] == "docs":
            rel = "/".join(parts[1:])
            if f.endswith(".md"):
                keep |= {p.path for p in pages if p.source == f}
            elif parts[1:2] == ["img"]:
                keep |= set(ids.get(parts[2], [])) if len(parts) > 3 else set()
                keep |= citing(rel)
            elif f != "docs/llms.txt":
                shared.append(f)
        elif parts[0] == "snippets" and len(parts) > 1:
            rel = "/".join(parts[1:])
            if len(parts) > 2:
                keep |= set(ids.get(parts[1], []))
            keep |= citing(f"snippet {rel.rsplit('.', 1)[0]}", rel)
        elif parts[0] == "overrides":
            if f == "overrides/404.html":
                keep |= {p.path for p in pages if p.path == "404.html"}
            else:
                shared.append(f)
    if shared:
        return [p.path for p in pages], shared
    return [p.path for p in pages if p.path in keep], []


# ---------------------------------------------------------------- 1 ページを調べる


@dataclass(frozen=True)
class Variant:
    width: int
    scheme: str

    @property
    def label(self) -> str:
        return f"{self.width} {SCHEME_NAMES[self.scheme]}"


def short_url(text: str, base: str) -> str:
    """メッセージの中の配った URL（http://127.0.0.1:…/claude-atlas/）を / に縮める。"""
    return text.replace(base, "/")


def console_errors(events: list[dict], base: str) -> list[str]:
    """ためたイベントのうち、例外・console.error・Log の error（同じオリジンの URL のものだけ）。"""
    out = []
    u = urllib.parse.urlsplit(base)
    origin = f"{u.scheme}://{u.netloc}/"
    for e in events:
        p = e.get("params", {})
        if e["method"] == "Runtime.exceptionThrown":
            d = p.get("exceptionDetails", {})
            ex = d.get("exception", {})
            text = (ex.get("description") or d.get("text") or "例外").split("\n")[0]
            where = d.get("url") or ""
            out.append(f"例外: {text}" + (f"（{where}:{d.get('lineNumber', 0) + 1}）" if where else ""))
        elif e["method"] == "Runtime.consoleAPICalled" and p.get("type") in ("error", "assert"):
            args = [str(a.get("value", a.get("description", ""))) for a in p.get("args", [])]
            out.append("console.error: " + " ".join(args))
        elif e["method"] == "Log.entryAdded" and p.get("entry", {}).get("level") == "error":
            ent = p["entry"]
            url = ent.get("url") or ""
            if url and not url.startswith(origin):
                continue                # 外の URL は「外への問い合わせ」に出す
            out.append(ent.get("text", "") + (f"（{url}）" if url else ""))
    seen = []
    for m in (short_url(x, base) for x in out):
        m = re.sub(r"\s+", " ", m).strip()
        if m not in seen:
            seen.append(m)
    return seen


def outside_requests(events: list[dict], base: str) -> list[str]:
    """ためたイベントのうち、配ったオリジンでない URL への問い合わせ（Network.requestWillBeSent。重ねない）。"""
    u = urllib.parse.urlsplit(base)
    origin = f"{u.scheme}://{u.netloc}/"
    out: list[str] = []
    for e in events:
        if e.get("method") != "Network.requestWillBeSent":
            continue
        url = (e.get("params", {}).get("request") or {}).get("url") or ""
        if not url or url.startswith(origin) or url.startswith(LOCAL_SCHEMES):
            continue
        if url not in out:
            out.append(url)
    return out


def load(page: Page, url: str, v: Variant, timeout: float) -> str | None:
    """タブに 1 ページを 1 つの幅・配色で読み込む。開けなければその理由。"""
    tab = page.tab
    tab.call("Emulation.setDeviceMetricsOverride", {"width": v.width, "height": HEIGHT, "deviceScaleFactor": 1,
                                                    "mobile": v.width < 600})
    tab.call("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": v.scheme}]})
    page.scheme = v.scheme
    tab.events.clear()
    nav = tab.call("Page.navigate", {"url": url}, timeout=timeout)
    if nav.get("errorText"):
        return f"開けない（{nav['errorText']}）"
    tab.wait_event("Page.loadEventFired", timeout)
    return None


def probe(page: Page, v: Variant, base: str, timeout: float) -> dict:
    """読み込んだページを配色 v.scheme で調べる。配色が違えば prefers-color-scheme だけを替えて調べ直す。
    開けなければ {"failed": 理由}。JS のエラーと外への問い合わせは読み込みからのすべて。"""
    tab = page.tab
    again = page.scheme != v.scheme
    if again:
        tab.call("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": v.scheme}]})
        page.scheme = v.scheme
    cfg = {"wait": WAIT_MS, "waitMermaid": WAIT_MERMAID_MS, "leak": LEAK_RE, "maxCulprits": MAX_CULPRITS,
           "clearFrac": CLEAR_FRAC, "scheme": SCHEME_ATTR[v.scheme] if again else None}
    r = tab.call("Runtime.evaluate", {"expression": f"({PROBE})({json.dumps(cfg)})", "awaitPromise": True,
                                      "returnByValue": True},
                 timeout=timeout + max(WAIT_MS, WAIT_MERMAID_MS) / 1000)
    if "exceptionDetails" in r:
        d = r["exceptionDetails"]
        msg = (d.get("exception", {}).get("description") or d.get("text") or "").split("\n")[0]
        return {"failed": f"検査の JS が止まった（{msg}）"}
    res = r.get("result", {}).get("value")
    if not isinstance(res, dict):
        return {"failed": "検査の JS が結果を返さない"}
    res["console"] = console_errors(tab.events, base)
    res["outside"] = outside_requests(tab.events, base)
    return res


class Stopped(Exception):
    """止めた（Ctrl-C・kill）ので、worker を終える。"""


@dataclass
class Context:
    chrome: Path
    env: dict[str, str] | None
    work: Path
    base: str
    variants: list[Variant]
    timeout: float
    stop: threading.Event = field(default_factory=threading.Event)
    done: int = 0
    lock: threading.Lock = field(default_factory=threading.Lock)
    browser: Browser | None = None
    starting: threading.Lock = field(default_factory=threading.Lock)

    def current(self) -> Browser:
        with self.starting:
            if self.stop.is_set():
                raise Stopped
            if self.browser is None:
                self.browser = Browser(self.chrome, self.env, self.work)
            return self.browser

    def restart(self, old: Browser) -> None:
        with self.starting:
            if self.browser is old:
                self.browser = None
                old.close()

    def close(self) -> None:
        with self.starting:
            b, self.browser = self.browser, None
        if b:
            b.close()


def check_page(ctx: Context, url: str) -> list[tuple[Variant, dict]]:
    """1 ページを ctx.variants で調べる。幅ごとに 1 回読み込み、配色は読み込み直さずに替える。
    開けない回は、タブを開き直して 1 回だけやり直す（Chrome が答えなければ Chrome を起動し直す）。"""
    out = []
    for width in dict.fromkeys(v.width for v in ctx.variants):
        pending = [v for v in ctx.variants if v.width == width]
        tries: collections.Counter = collections.Counter()
        browser: Browser | None = None
        page: Page | None = None

        def drop() -> None:
            nonlocal page
            if page is not None and browser is not None:
                try:
                    browser.close_page(page)
                except OSError:
                    ctx.restart(browser)
                except (CDPError, ValueError):
                    pass
            page = None
        try:
            while pending:
                v = pending[0]
                try:
                    if page is None:
                        browser = ctx.current()
                        try:
                            page = browser.open_page()
                        except OSError:
                            ctx.restart(browser)
                            raise
                        failed = load(page, url, v, ctx.timeout)
                        res = {"failed": failed} if failed else probe(page, v, ctx.base, ctx.timeout)
                    else:
                        res = probe(page, v, ctx.base, ctx.timeout)
                except (OSError, RuntimeError, ValueError, KeyError) as e:
                    if ctx.stop.is_set():
                        raise Stopped from e
                    res = {"failed": f"{type(e).__name__}: {e}"}
                if "failed" in res:
                    drop()
                    tries[v] += 1
                    if tries[v] < 2:
                        continue
                out.append((v, res))
                pending.pop(0)
        finally:
            drop()
    return out


def worker(ctx: Context, tasks: queue.Queue, results: dict, progress) -> None:
    try:
        while not ctx.stop.is_set():
            try:
                page = tasks.get_nowait()
            except queue.Empty:
                return
            results[page.path] = check_page(ctx, ctx.base + page.path)
            with ctx.lock:
                ctx.done += 1
                progress(ctx.done)
    except Stopped:
        return


def run(site: Path, pages: list[SitePage], variants: list[Variant], chrome: Path, jobs: int, timeout: float,
        work: Path, env: dict[str, str] | None, progress=lambda n: None) -> dict[str, list[tuple[Variant, dict]]]:
    """pages を variants で開いて調べる。Chrome は 1 つで、jobs 個のタブを並べる。{ページのパス: [(Variant, 結果)]}。"""
    server, base = serve(site, site_prefix(site))
    ctx = Context(chrome, env, work, base, variants, timeout)
    tasks: queue.Queue = queue.Queue()
    for p in pages:
        tasks.put(p)
    results: dict[str, list[tuple[Variant, dict]]] = {}
    n = max(1, min(jobs, len(pages)))
    threads = []
    try:
        ctx.current()
        for _ in range(n):
            t = threading.Thread(target=worker, args=(ctx, tasks, results, progress), daemon=True)
            t.start()
            threads.append(t)
        for t in threads:
            while t.is_alive():
                t.join(0.2)
    finally:
        ctx.stop.set()
        ctx.close()
        for t in threads:
            t.join(10)
        server.shutdown()
        server.server_close()
    return results


# ---------------------------------------------------------------- まとめる


@dataclass
class Finding:
    kind: str
    page: SitePage
    heading: str
    where: str
    detail: str
    variants: list[str] = field(default_factory=list)
    data: dict = field(default_factory=dict)

    @property
    def severity(self) -> str:
        return KINDS[self.kind][1]

    def line(self) -> str:
        loc = self.page.label + (f"#{self.heading}" if self.heading else "")
        if self.page.source:
            loc += f"（{self.page.source}）"
        where = f"（{self.where}）" if self.where else ""
        return f"{loc}: {self.detail}{where}［{'・'.join(self.variants)}］"


def describe(kind: str, it: dict) -> str:
    if kind == "outside-request":
        return it.get("url", "")
    if kind == "leaked-markup":
        return f"「{it.get('text', '')}」の {it.get('mark', '')}"
    if kind == "page-overflow":
        return f"{it.get('over', 0)}px はみ出す：{it.get('what', '')}"
    if kind == "img-broken":
        return f"{it.get('src', '')}（{it.get('alt', '')}）: {it.get('msg', '')}"
    if kind == "img-transparent":
        sides = "・".join(f"{k} {v}px" for k, v in it.get("sides", {}).items())
        return f"{it.get('src', '')}（{it.get('size', '')}）: 縁が透ける（{sides}）"
    if kind == "wide-table":
        return (f"幅 {it.get('width')}px・右の {it.get('hidden')}px が隠れる（入れ物 {it.get('box')}px・{it.get('cols')} 列）: "
                f"{it.get('head', '')}")
    if kind == "mermaid-unrendered":
        return f"{WAIT_MERMAID_MS // 1000} 秒待っても描かれない: {it.get('text', '')}"
    return str(it.get("msg", it))


def collect(pages: list[SitePage], results: dict[str, list[tuple[Variant, dict]]]) -> tuple[list[Finding], list[str]]:
    """結果を指摘にまとめる。(指摘, 注意)。同じ要素の同じ指摘が幅・配色の違う回に出たものだけを 1 件にする（回の中で
    「種類・節・折りたたみ・文」が同じ指摘の何番目かで、ほかの回と突き合わせる）。"""
    found: dict[tuple, Finding] = {}
    notes = []

    def put(kind: str, page: SitePage, it: dict, v: Variant, seen: collections.Counter) -> None:
        detail = describe(kind, it)
        same = (kind, page.path, it.get("h", ""), it.get("where", ""), detail)
        key = same + (seen[same],)
        seen[same] += 1
        f = found.get(key)
        if f is None:
            f = found[key] = Finding(kind, page, it.get("h", ""), it.get("where", ""), detail, data=it)
        if v.label not in f.variants:
            f.variants.append(v.label)

    for page in pages:
        for v, res in results.get(page.path, []):
            seen: collections.Counter = collections.Counter()
            if "failed" in res:
                put("load-failed", page, {"msg": res["failed"]}, v, seen)
                continue
            for kind, items in res.get("items", {}).items():
                if kind not in KINDS:
                    continue
                for it in items:
                    put(kind, page, it, v, seen)
            for url in res.get("outside", []):
                put("outside-request", page, {"url": url}, v, seen)
            for m in res.get("console", []):
                put("js-error", page, {"msg": m}, v, seen)
            want = SCHEME_ATTR.get(v.scheme)
            if res.get("scheme") not in (None, want):
                notes.append(f"{page.label}（{v.label}）: 配色が {want} にならない（data-md-color-scheme={res.get('scheme')}）")
    order = {k: i for i, k in enumerate(KINDS)}
    paths = {p.path: i for i, p in enumerate(pages)}
    out = sorted(found.values(), key=lambda f: (order[f.kind], paths.get(f.page.path, 0)))
    return out, notes


def summarize(findings: list[Finding]) -> dict[str, dict]:
    s = {}
    for k, (name, sev) in KINDS.items():
        fs = [f for f in findings if f.kind == k]
        s[k] = {"name": name, "severity": sev, "findings": len(fs), "pages": len({f.page.path for f in fs})}
    return s


def totals(results: dict[str, list[tuple[Variant, dict]]]) -> dict[str, int]:
    """調べた要素の数（最初の回の数をページごとに足す）。"""
    t: collections.Counter = collections.Counter()
    for out in results.values():
        for _, res in out[:1]:
            t.update(res.get("counts", {}))
    return dict(t)


def report_json(path: Path, site: Path, chrome: Path | str, variants: list[Variant], pages: list[SitePage],
                results: dict, findings: list[Finding], notes: list[str], elapsed: float) -> None:
    data = {
        "site": str(site), "chrome": str(chrome), "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "variants": [{"width": v.width, "scheme": v.scheme} for v in variants],
        "pages": len(pages), "elapsed_seconds": round(elapsed, 1),
        "totals": totals(results), "summary": summarize(findings), "notes": notes,
        "findings": [{"kind": f.kind, "name": KINDS[f.kind][0], "severity": f.severity, "page": f.page.path,
                      "source": f.page.source, "heading": f.heading, "where": f.where, "detail": f.detail,
                      "variants": f.variants, "data": f.data} for f in findings],
        "results": [{"page": p.path, "source": p.source, "variant": v.label,
                     **{k: res.get(k) for k in ("failed", "title", "scheme", "vw", "sw", "culprits", "counts",
                                                "waited", "ms") if k in res},
                     "found": {k: len(x) for k, x in res.get("items", {}).items()},
                     "outside": len(res.get("outside", [])), "console": len(res.get("console", []))}
                    for p in pages for v, res in results.get(p.path, [])],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def print_report(findings: list[Finding], notes: list[str], verbose: bool, n_pages: int, tot: dict[str, int]) -> None:
    by_kind = collections.defaultdict(list)
    for f in findings:
        by_kind[f.kind].append(f)
    for k, (name, sev) in KINDS.items():
        fs = by_kind.get(k, [])
        if not fs:
            continue
        shown = fs if sev == "error" or verbose else fs[:3]
        print(f"\n{SEVERITY_NAMES[sev]}: {name}（{len(fs)} 件・{len({f.page.path for f in fs})} ページ）")
        for f in shown:
            print("  " + f.line())
        if len(shown) < len(fs):
            print(f"  …ほか {len(fs) - len(shown)} 件（-v で全件。--json で一覧を書ける）")
    for n in notes:
        print("注意: " + n)
    s = summarize(findings)
    print("\nまとめ（件数・ページ数）")
    for k, d in s.items():
        print(f"  {SEVERITY_NAMES[d['severity']]}  {d['name']}: {d['findings']} 件・{d['pages']} ページ")
    errs = sum(d["findings"] for d in s.values() if d["severity"] == "error")
    warns = sum(d["findings"] for d in s.values() if d["severity"] == "warning")
    print(f"\nページ {n_pages}・表 {tot.get('tables', 0)}・画像 {tot.get('img', 0)}・Mermaid {tot.get('mermaid', 0)}・"
          f"折りたたみ {tot.get('details', 0)}・タブ {tot.get('tabs', 0)}　エラー {errs} 件・警告 {warns} 件")


# ---------------------------------------------------------------- 入口


def parse_list(values: list[str]) -> list[str]:
    return [x.strip() for v in values for x in v.split(",") if x.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("site", type=Path, nargs="?", help="ビルドしたサイトのフォルダ（mkdocs build -d の先。index.html と sitemap.xml がある）")
    parser.add_argument("--page", action="append", default=[], help="そのページだけ（id・URL のパス・docs/ のパス。くり返し・カンマ区切り可）")
    parser.add_argument("--field", action="append", default=[], help="その分野のページだけ（URL の最初のフォルダ。くり返し・カンマ区切り可）")
    parser.add_argument("--changed", nargs="?", const="origin/main", metavar="REF",
                        help="git で変わったファイルに関わるページだけ（REF との分かれ目から。既定 origin/main）")
    parser.add_argument("--json", type=Path, help="結果を書く JSON のファイル")
    parser.add_argument("--docs", type=Path, default=ROOT / "docs",
                        help="指摘に添える元の Markdown を探す docs/（既定はリポジトリ。別の木からビルドしたとき）")
    parser.add_argument("--width", action="append", default=[], help="画面の幅（px。くり返し・カンマ区切り可。既定 390）")
    parser.add_argument("--scheme", action="append", default=[], help="配色 light・dark（くり返し・カンマ区切り可。既定は両方）")
    parser.add_argument("-j", "--jobs", type=int, default=4, help="同時に開くタブの数（既定 4。Chrome は 1 つ）")
    parser.add_argument("--timeout", type=float, default=30.0, help="1 ページの読み込みを待つ秒数（既定 30）")
    parser.add_argument("--chrome", help="Chrome の実行ファイル")
    parser.add_argument("--strict", action="store_true", help="警告があっても終了コード 1")
    parser.add_argument("-v", "--verbose", action="store_true", help="警告も全件を出す")
    args = parser.parse_args(argv)
    if args.site is None:          # --changed DIR/site と書くと、サイトが REF に入る
        if args.changed and Path(args.changed).expanduser().is_dir():
            args.site, args.changed = Path(args.changed), "origin/main"
        else:
            parser.error("ビルドしたサイトのフォルダ（site）がない")

    site = args.site.expanduser().resolve()
    if not (site / "index.html").is_file():
        print(f"{site} にビルドしたサイトがない（index.html がない）。先に uv run mkdocs build -d {site} でビルドする",
              file=sys.stderr)
        return 2
    try:
        widths = [int(x) for x in parse_list(args.width)] or [390]
    except ValueError:
        parser.error("--width は整数（px）")
    if min(widths) < 200 or max(widths) > 4000:
        parser.error("--width は 200〜4000")
    schemes = parse_list(args.scheme) or ["light", "dark"]
    if bad := [s for s in schemes if s not in SCHEME_NAMES]:
        parser.error(f"--scheme は light か dark（{'・'.join(bad)} は使えない）")
    variants = [Variant(w, s) for w in dict.fromkeys(widths) for s in dict.fromkeys(schemes)]
    docs = args.docs.expanduser().resolve()
    every = list_pages(site, docs)
    want_pages, want_fields = parse_list(args.page), parse_list(args.field)
    pages = select_pages(every, want_pages, want_fields)
    if args.changed is not None:
        try:
            cp = subprocess.run(["git", "-C", str(docs), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        except FileNotFoundError:
            sys.exit("--changed: git がない")
        if cp.returncode or not cp.stdout.strip():
            sys.exit(f"--changed: {docs} が git のリポジトリの中にない（--docs の木の差分を見る）")
        files, mb = git_changed(Path(cp.stdout.strip()), args.changed)
        paths, shared = changed_pages(files, every, docs)
        if shared:
            print(f"--changed: 共有のファイルが変わったので全ページを流す（{'・'.join(shared[:5])}"
                  f"{f' ほか {len(shared) - 5}' if len(shared) > 5 else ''}）")
        keep = set(paths) | ({p.path for p in pages} if want_pages or want_fields else set())
        pages = [p for p in every if p.path in keep]
        if not shared:
            names = "・".join(p.rstrip("/") or "/" for p in paths) if 0 < len(paths) <= 10 else ""
            print(f"--changed: {args.changed}（分かれ目 {mb}）から変わった {len(files)} ファイルに関わるページ {len(paths)}"
                  + (f"（{names}）" if names else ""))
        if not pages:
            print("--changed: 調べるページがない（Chrome は起動しない）")
            if args.json:          # 前の結果を新しいものと取り違えないよう、空の結果を書く
                report_json(args.json.expanduser(), site, find_chrome(args.chrome) or "", variants, [], {}, [], [], 0.0)
                print(f"JSON: {args.json}")
            return 0
    if not pages:
        print(f"{site} に調べるページがない", file=sys.stderr)
        return 2
    chrome = find_chrome(args.chrome)
    if chrome is None:
        print(INSTALL_HINT, file=sys.stderr)
        return 2

    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))     # kill で止めても Chrome を閉じる（finally を通す）
    tty = sys.stderr.isatty()
    total = len(pages)

    def progress(n: int) -> None:
        if tty:
            sys.stderr.write(f"\r  {n}/{total} ページ")
            sys.stderr.flush()
        elif n % 50 == 0 or n == total:
            print(f"  … {n}/{total} ページ", file=sys.stderr, flush=True)

    print(f"ページ {total}・{'／'.join(v.label for v in variants)}・タブ {max(1, min(args.jobs, total))} 個（{chrome}）")
    t0 = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="ca-render-pages-") as tmp:
        env, note = font_env(Path(tmp))
        if note:
            print(note)
        try:
            results = run(site, pages, variants, chrome, args.jobs, args.timeout, Path(tmp), env, progress)
        except (RuntimeError, OSError) as e:
            print(f"Chrome を動かせない: {e}", file=sys.stderr)
            return 2
        except KeyboardInterrupt:
            print("\n止めた", file=sys.stderr)
            return 130
    if tty:
        sys.stderr.write("\n")
    elapsed = time.monotonic() - t0
    findings, notes = collect(pages, results)
    print_report(findings, notes, args.verbose, total, totals(results))
    print(f"（{elapsed:.0f} 秒）")
    if args.json:
        report_json(args.json.expanduser(), site, chrome, variants, pages, results, findings, notes, elapsed)
        print(f"JSON: {args.json}")
    errors = sum(f.severity == "error" for f in findings)
    warnings = sum(f.severity == "warning" for f in findings)
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
