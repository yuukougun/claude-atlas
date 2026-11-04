"""雛形の静的な検査（設計書 §8.7・DR-07。入口は tools/check_templates.py）。

見るもの:
  snippets/<id>/…           雛形（<id> はページの id）。JSON・YAML・front matter の形、スキルとサブエージェントの
                            front matter の必須の項目、settings の雛形のキー、期待（<名前>.expect.yaml）と結果
                            （verified.yaml）の形
  .claude/settings.json     このリポジトリの縛り。入れた hooks と permissions も雛形として扱う（design §10.5）

決まり（試作で直す。build-C.md §3）:
  settings の雛形           名前が settings.json で終わる JSON（settings.json・settings.local.json・managed-settings.json
                            など）。キーは tools/checks/template_keys.yml の許す一覧で見る。schema/claude-code-settings.schema.json
                            （SchemaStore のスキーマに使うキーを足した写し）があれば、それも当てる
  スキル                    SKILL.md。name と description を必ず書く（Claude Code ではどちらも任意だが、Agent Skills の
                            仕様と claude.ai は name〔1〜64 字、英小文字・数字・ハイフン、親のフォルダ名と同じ〕と
                            description〔1〜1024 字〕を求める。research/28 #48）。親のフォルダがページの id のフォルダ
                            のときは、フォルダ名との一致を見ない
  サブエージェント          agents/ のフォルダの中の .md。name と description が必須、name は 256 字まで・「:」を含めない・
                            「-」で始めない（research/28 #47）
  期待と結果                <名前>.expect.yaml と verified.yaml は YAML のマッピング。<名前>.expect.yaml には同じ名前の
                            雛形がある。中の項目の形は試作（工程7）で決める
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import yaml

from lib.markdown import split_front_matter
from lib.yamlio import parse_yaml, read_yaml

from .context import Context
from .core import ERROR, TEMPLATES, WARNING, Finding, check, joined

SNIPPETS = "snippets"
SETTINGS_FILE = ".claude/settings.json"
KEYS_FILE = Path(__file__).resolve().parent / "template_keys.yml"
SETTINGS_SCHEMA = "schema/claude-code-settings.schema.json"
EXPECT_SUFFIX = ".expect.yaml"
VERIFIED_NAME = "verified.yaml"
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RULE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*(\((?P<spec>.*)\))?$")


@dataclass
class Template:
    path: Path
    shown: str              # 根からの相対パス
    page: str               # snippets/<id>/ の <id>（.claude/settings.json は「-」）
    rel: str                # snippets/<id>/ からの相対パス

    @property
    def name(self) -> str:
        return Path(self.rel).name


def snippet_files(ctx: Context) -> list[Template]:
    base = ctx.root / SNIPPETS
    out = []
    if base.is_dir():
        for p in sorted(base.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(base).as_posix()
            parts = rel.split("/")
            page = parts[0] if len(parts) > 1 else "-"
            out.append(Template(p, f"{SNIPPETS}/{rel}", page, "/".join(parts[1:]) if len(parts) > 1 else rel))
    return out


def settings_targets(ctx: Context) -> list[Template]:
    out = [t for t in snippet_files(ctx) if t.name.endswith("settings.json")]
    own = ctx.root / SETTINGS_FILE
    if own.is_file():
        out.append(Template(own, SETTINGS_FILE, "-", SETTINGS_FILE))
    return out


def finding(t: Template, message: str, line: int | None = None, severity: str | None = None) -> Finding:
    pages = frozenset({t.page}) if t.page != "-" else frozenset()
    return Finding(t.shown, line, t.page, message, pages, severity)


def load_keys() -> dict:
    data = yaml.safe_load(KEYS_FILE.read_text(encoding="utf-8"))
    return data.get("settings", {}) if isinstance(data, dict) else {}


# ---------------------------------------------------------------- 置き場所と形


@check("雛形の置き場所", ERROR, TEMPLATES)
def check_template_place(ctx: Context) -> Iterator[Finding]:
    """雛形が snippets/<id>/ の下にない、<id> がページの id でない（design §8.7：snippets/<id>/<名前>.<拡張子>）"""
    for t in snippet_files(ctx):
        if t.page == "-":
            yield finding(t, "雛形は snippets/<ページの id>/ の下に置く")
        elif ctx.page(t.page) is None:
            yield finding(t, f"snippets/ のフォルダ名「{t.page}」がページの id でない")


@check("雛形の形", ERROR, TEMPLATES)
def check_template_syntax(ctx: Context) -> Iterator[Finding]:
    """JSON・YAML として読めない。Markdown の front matter（--- で始まるもの）が閉じていない・読めない"""
    for t in snippet_files(ctx):
        suffix = t.path.suffix.lower()
        try:
            text = t.path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            yield finding(t, f"読めない（{e}）")
            continue
        if suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as e:
                yield finding(t, f"JSON が読めない: {e.msg}", e.lineno)
        elif suffix in (".yml", ".yaml"):
            doc = parse_yaml(text)
            for pr in doc.problems(t.shown):
                yield finding(t, pr.message, pr.line)
        elif suffix == ".md" and text.startswith("---"):
            fm, _, _, err = split_front_matter(text)
            if err:
                yield finding(t, err, 1)
            elif fm is not None:
                doc = parse_yaml(fm, line_offset=1)
                for pr in doc.problems(t.shown):
                    yield finding(t, f"front matter: {pr.message}", pr.line)


@check("期待の形", ERROR, TEMPLATES)
def check_expectations(ctx: Context) -> Iterator[Finding]:
    """<名前>.expect.yaml と verified.yaml が YAML のマッピングでない。<名前>.expect.yaml と同じ名前の雛形がない
    （中の項目の形は試作で決める）"""
    files = snippet_files(ctx)
    stems = {(t.page, str(Path(t.rel).parent), t.path.stem) for t in files
             if not t.name.endswith(EXPECT_SUFFIX) and t.name != VERIFIED_NAME}
    for t in files:
        if not (t.name.endswith(EXPECT_SUFFIX) or t.name == VERIFIED_NAME):
            continue
        doc = read_yaml(t.path)
        if doc.error is None and not isinstance(doc.data, dict):
            yield finding(t, "YAML のマッピングにする")
        if t.name.endswith(EXPECT_SUFFIX):
            stem = t.name[:-len(EXPECT_SUFFIX)]
            if (t.page, str(Path(t.rel).parent), stem) not in stems:
                yield finding(t, f"期待に対応する雛形（{stem}.<拡張子>）が同じフォルダにない")


def front_matter(t: Template) -> tuple[dict | None, str | None]:
    try:
        text = t.path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, None
    if not text.startswith("---"):
        return None, "front matter がない（1行目を --- にする。1行目でないと front matter として読まれない）"
    fm, _, _, err = split_front_matter(text)
    if err or fm is None:
        return None, None              # 「雛形の形」が出す
    doc = parse_yaml(fm, line_offset=1)
    if doc.error is not None:
        return None, None
    return (doc.data if isinstance(doc.data, dict) else {}), None


@check("スキルの front matter", ERROR, TEMPLATES)
def check_skill_front_matter(ctx: Context) -> Iterator[Finding]:
    """SKILL.md の front matter に name と description がない。name が 1〜64 字の英小文字・数字・ハイフンでない、
    親のフォルダ名と違う。description が 1024 字を超える（research/28 #48）"""
    for t in snippet_files(ctx):
        if t.name != "SKILL.md":
            continue
        fm, why = front_matter(t)
        if why:
            yield finding(t, why, 1)
            continue
        if fm is None:
            continue
        name, desc = fm.get("name"), fm.get("description")
        if not isinstance(name, str) or not name.strip():
            yield finding(t, "front matter に name がない（Agent Skills の仕様と claude.ai は必須）", 1)
        else:
            if len(name) > 64 or not SKILL_NAME_RE.match(name):
                yield finding(t, f"name「{name}」が 1〜64 字の英小文字・数字・ハイフンでない", 1)
            folder = Path(t.rel).parent.name
            if folder and folder != name:
                yield finding(t, f"name「{name}」が親のフォルダ名「{folder}」と違う", 1)
        if not isinstance(desc, str) or not desc.strip():
            yield finding(t, "front matter に description がない（ないと本文の最初の行が使われる）", 1)
        elif len(desc) > 1024:
            yield finding(t, f"description が {len(desc)} 字（1024 字まで）", 1)


@check("サブエージェントの front matter", ERROR, TEMPLATES)
def check_subagent_front_matter(ctx: Context) -> Iterator[Finding]:
    """agents/ のフォルダの中の .md の front matter に name と description がない。name が 256 字を超える・「:」を含む・
    「-」で始まる（name がないと文書として扱われ、description がないと飛ばされる。research/28 #47）"""
    for t in snippet_files(ctx):
        if not t.name.endswith(".md") or "agents" not in Path(t.rel).parts[:-1]:
            continue
        fm, why = front_matter(t)
        if why:
            yield finding(t, why, 1)
            continue
        if fm is None:
            continue
        name, desc = fm.get("name"), fm.get("description")
        if not isinstance(name, str) or not name.strip():
            yield finding(t, "front matter に name がない（ないとサブエージェントとして読まれない）", 1)
        elif len(name) > 256 or ":" in name or name.startswith("-"):
            yield finding(t, f"name「{name}」が使えない形（256 字まで・「:」を含めない・「-」で始めない）", 1)
        if not isinstance(desc, str) or not desc.strip():
            yield finding(t, "front matter に description がない（ないと飛ばされる）", 1)


# ---------------------------------------------------------------- settings


def settings_problems(data, keys: dict) -> Iterator[str]:
    """settings の JSON の、許す一覧にないキーと形の誤り。"""
    if not isinstance(data, dict):
        yield "最上位を JSON のオブジェクトにする"
        return
    allowed = lambda k: keys.get(k) or []      # noqa: E731
    for k in data:
        if k not in allowed("top"):
            yield f"最上位のキー「{k}」が許す一覧（tools/checks/template_keys.yml）にない"
    perms = data.get("permissions")
    if perms is not None:
        if not isinstance(perms, dict):
            yield "permissions をオブジェクトにする"
        else:
            for k, v in perms.items():
                if k not in allowed("permissions"):
                    yield f"permissions の「{k}」が許す一覧にない"
                if k in ("allow", "ask", "deny"):
                    if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                        yield f"permissions.{k} を文字列のリストにする"
                        continue
                    for rule in v:
                        if not (RULE_RE.match(rule) or rule.startswith("mcp__")):
                            yield f"permissions.{k} の「{rule}」が規則の形（ツール名か ツール名(指定)）でない"
    sandbox = data.get("sandbox")
    if isinstance(sandbox, dict):
        for k in sandbox:
            if k not in allowed("sandbox"):
                yield f"sandbox の「{k}」が許す一覧にない"
    hooks = data.get("hooks")
    if hooks is not None:
        if not isinstance(hooks, dict):
            yield "hooks をオブジェクトにする"
            return
        for event, entries in hooks.items():
            if event not in allowed("hook_events"):
                yield f"hooks のイベント「{event}」が許す一覧にない"
            if not isinstance(entries, list):
                yield f"hooks.{event} をリストにする"
                continue
            for i, entry in enumerate(entries):
                where = f"hooks.{event}[{i}]"
                if not isinstance(entry, dict):
                    yield f"{where} をオブジェクトにする"
                    continue
                for k in entry:
                    if k not in allowed("hook_entry"):
                        yield f"{where} の「{k}」が許す一覧にない"
                if "matcher" in entry and not isinstance(entry["matcher"], str):
                    yield f"{where}.matcher を文字列にする（配列は無効で、同じファイルのほかの hooks も読まれなくなる。research/28 #5）"
                inner = entry.get("hooks")
                if not isinstance(inner, list):
                    yield f"{where}.hooks をリストにする"
                    continue
                for j, h in enumerate(inner):
                    hw = f"{where}.hooks[{j}]"
                    if not isinstance(h, dict):
                        yield f"{hw} をオブジェクトにする"
                        continue
                    for k in h:
                        if k not in allowed("hook"):
                            yield f"{hw} の「{k}」が許す一覧にない"
                    if h.get("type") == "command" and not (isinstance(h.get("command"), str) and h["command"].strip()):
                        yield f"{hw} は type が command なので command を書く"
                    t = h.get("timeout")
                    if t is not None and (isinstance(t, bool) or not isinstance(t, (int, float)) or t <= 0):
                        yield f"{hw}.timeout を正の数（秒）にする"
                    of = h.get("onFailure")
                    if of is not None and of not in allowed("on_failure"):
                        yield f"{hw}.onFailure の「{of}」は使えない（{joined(allowed('on_failure'))}）"


@check("settings のキー", ERROR, TEMPLATES)
def check_settings_keys(ctx: Context) -> Iterator[Finding]:
    """settings の雛形（名前が settings.json で終わる JSON）と .claude/settings.json のキーが、許す一覧
    （tools/checks/template_keys.yml。一次資料で確かめたキーだけ）にない。permissions・hooks の形が違う（matcher を
    配列にする、command のない command の hook、timeout・onFailure の値など）"""
    keys = load_keys()
    for t in settings_targets(ctx):
        try:
            data = json.loads(t.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
            if t.page == "-":            # snippets/ の JSON は「雛形の形」が出す
                yield finding(t, f"JSON が読めない: {e}", getattr(e, "lineno", None))
            continue
        for msg in settings_problems(data, keys):
            yield finding(t, msg)


@check("settings のスキーマ", ERROR, TEMPLATES)
def check_settings_schema(ctx: Context) -> Iterator[Finding]:
    """schema/claude-code-settings.schema.json（SchemaStore のスキーマに使うキーを足した写し。research/28 #46）が
    あれば、settings の雛形と .claude/settings.json に当てる（jsonschema を使う。写しがなければ警告を1件出す）"""
    path = ctx.root / SETTINGS_SCHEMA
    targets = settings_targets(ctx)
    if not path.exists():
        if targets:
            yield Finding(SETTINGS_SCHEMA, None, "-", "settings のスキーマの写しがない（写した日と相当の版を書いて置く。"
                                                       "置くまでは許す一覧だけで見る）", severity=WARNING)
        return
    try:
        import jsonschema
        schema = json.loads(path.read_text(encoding="utf-8"))
        validator = jsonschema.validators.validator_for(schema)(schema)
    except Exception as e:  # noqa: BLE001  （写しが読めない・jsonschema がない）
        yield Finding(SETTINGS_SCHEMA, None, "-", f"settings のスキーマを使えない: {e}", severity=WARNING)
        return
    for t in targets:
        try:
            data = json.loads(t.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
            where = ".".join(str(x) for x in err.absolute_path) or "最上位"
            yield finding(t, f"{where}: {err.message}")
