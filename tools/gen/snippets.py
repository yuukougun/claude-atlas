"""雛形の写し（design §6.9・§8.7。README の判断「安全とデータの雛形の扱い」・brief-build2 §2）。

  <!-- gen:begin snippet <ページの id>/<名前> -->

snippets/<id>/<名前>.<拡張子>（<名前>.expect.yaml を除く1つのファイル）を、折りたたみの中のコードにして写す。
写すのは、動作確認を通ったもの（snippets/<id>/verified.yaml の <名前> の result が pass）だけ。通っていないものは
「雛形「<名前>」は、動作確認の後に載せる。」とだけ書く。確かめた環境（版・系列・モデル・OS・日付）と、要る最低の版
（expect.yaml の features か、ページの tracks の機能の since.claude_code のうち新しいもの）を道具が書く。

verified.yaml の形（案。雛形の動作の検証役か check_templates.py --live が書く。キーの台帳に足すのはメイン）:
  <名前>:
    result: pass                 # pass か fail
    date: 2026-11-20
    claude_code: 2.1.317
    channel: latest              # latest か stable
    models: [claude-opus-5-5]
    os: WSL2 Ubuntu 24.04
expect.yaml から読むのは title（折りたたみの題。なければ名前）と features（要る最低の版の元。なければ tracks）だけ。
"""
from __future__ import annotations

import re
from pathlib import Path

from lib.base import as_strings, as_text
from lib.yamlio import read_yaml

from .blocks import block
from .text import md_text

LANGS = {"json": "json", "jsonc": "json", "yaml": "yaml", "yml": "yaml", "sh": "bash", "bash": "bash", "py": "python",
         "md": "markdown", "toml": "toml", "txt": "text", "js": "javascript", "ts": "typescript"}
PASS = "pass"
SNIPPET_RE = re.compile(r"^(?P<id>[a-z0-9]+(?:-[a-z0-9]+)*)/(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)$")


def _version_key(v: str) -> tuple[int, ...] | None:
    return tuple(int(x) for x in v.split(".")) if re.fullmatch(r"\d+(\.\d+)*", v) else None


def _read_map(path: Path, gen, shown: str) -> dict:
    if not path.exists():
        return {}
    doc = read_yaml(path)
    if doc.error is not None or not isinstance(doc.data, dict):
        gen.note(f"{shown} が読めない（{doc.error or 'マッピングでない'}）")
        return {}
    return doc.data


def min_version(gen, feature_ids: list[str]) -> str:
    best, best_key = "", None
    for fid in feature_ids:
        f = gen.feature(fid)
        since = f.raw.get("since") if f is not None else None
        ver = as_text(since.get("claude_code")) if isinstance(since, dict) else ""
        key = _version_key(ver) if ver else None
        if key is not None and (best_key is None or key > best_key):
            best, best_key = ver, key
    return best


def fence_for(text: str) -> str:
    longest = max((len(m.group(0)) for m in re.finditer(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


@block("snippet", param="<ページの id>/<名前>", doc="雛形の写し（snippets/<id>/<名前>.*。動作確認を通ったものだけ）")
def b_snippet(ctx) -> str:
    gen = ctx.gen
    m = SNIPPET_RE.match(ctx.param)
    if not m:
        gen.note(f"{ctx.host}: 生成の部分「{ctx.name}」の引数は <ページの id>/<名前> にする（空にした）")
        return ""
    sid, name = m.group("id"), m.group("name")
    cfg = gen.config
    base = cfg.text("snippets", "dir", "snippets")
    folder = gen.root / base / sid
    shown = f"{base}/{sid}"
    pending = gen.text("snippet_pending", "雛形「{name}」は、動作確認の後に載せる。").replace("{name}", md_text(name))
    files = sorted(p for p in folder.glob(f"{name}.*") if p.is_file() and not p.name.endswith(".expect.yaml")) \
        if folder.is_dir() else []
    if len(files) != 1:
        what = "ない" if not files else f"{len(files)} つある（{'・'.join(p.name for p in files)}）"
        gen.note(f"{ctx.host}: 雛形 {shown}/{name}.* が{what}（「動作確認の後に載せる」と書いた）")
        return pending
    verified = _read_map(folder / "verified.yaml", gen, f"{shown}/verified.yaml")
    result = verified.get(name)
    if not (isinstance(result, dict) and as_text(result.get("result")) == PASS):
        return pending
    path = files[0]
    try:
        code = path.read_text(encoding="utf-8").rstrip("\n")
    except (OSError, UnicodeDecodeError) as e:
        gen.note(f"{shown}/{path.name} が読めない（{e}。「動作確認の後に載せる」と書いた）")
        return pending
    expect = _read_map(folder / f"{name}.expect.yaml", gen, f"{shown}/{name}.expect.yaml")
    title = as_text(expect.get("title")) or name
    lang = LANGS.get(path.suffix.lstrip(".").lower(), "")
    fence = fence_for(code)
    fold = cfg.text("snippets", "fold", '??? example "雛形：{name}"').replace("{name}", md_text(title).replace('"', "'"))
    env = []
    ver = as_text(str(result.get("claude_code") or ""))
    chan = as_text(result.get("channel"))
    if ver:
        env.append(f"Claude Code {md_text(ver)}" + (f"（{md_text(chan)}）" if chan else ""))
    env += [md_text(x) for x in as_strings(result.get("models"))]
    if as_text(result.get("os")):
        env.append(md_text(result.get("os")))
    if as_text(str(result.get("date") or "")):
        env.append(str(result.get("date")))
    feats = as_strings(expect.get("features")) or (ctx.page.tracks if ctx.page is not None else [])
    need = min_version(gen, feats)
    tail = []
    if env:
        tail.append(f"{cfg.text('snippets', 'verified_with', '確かめた環境')}：{'・'.join(env)}")
    if need:
        tail.append(f"{cfg.text('snippets', 'min_version', '要る最低の版')}：Claude Code {md_text(need)}")
    lines = [fold, "", f"    {fence}{lang}"]
    lines += [("    " + x) if x else "" for x in code.split("\n")]
    lines += [f"    {fence}"]
    if tail:
        lines += ["", "    " + "。".join(tail) + "。"]
    return "\n".join(lines)
