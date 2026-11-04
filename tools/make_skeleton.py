#!/usr/bin/env python3
"""目次（planning/catalog/）から、全ページの骨格（stub）を stubs/<field>/<id>.md に作る（設計書 §5.2 の5・§8.5・
§10.1 の 6c）。骨格の後は front matter が正になり、目次は凍結して執筆の指示（materials・templates・visual・notes）
としてだけ使う。骨格のページは公開しない（docs/ の外に置き、draft にするときに docs/<field>/<id>.md へ移す）。

使い方:
  uv run python tools/make_skeleton.py              目次のページのうち、まだないものの骨格を作る（docs/ か stubs/ に同じ id の
                                                    ページがあれば書かない）
  uv run python tools/make_skeleton.py --dry-run    書かずに、作る・作り直す・そのままの数を出す（--force と組める）
  uv run python tools/make_skeleton.py --force      stubs/ にある骨格も目次から作り直す（updated のほかが同じものは書かない。
                                                    docs/ のページには触れない）
  uv run python tools/make_skeleton.py --check      目次と stubs/ の front matter の差を出す（書かない。差があれば終了コード 1）
  uv run python tools/make_skeleton.py --date 2026-11-05   updated に書く日（既定は今日）
  uv run python tools/make_skeleton.py --root DIR   DIR を根にする（試験用。DIR/schema・DIR/planning/catalog・DIR/docs・DIR/stubs）
終了コード: 0＝書き終えた（--dry-run は数え終えた）・--check で差がない、1＝--check で差がある、
           2＝作れない（site.yml・keys.yml・page.schema.json・目次が読めない、目次から作った front matter が
           page.schema.json に通らない。このときは1ページも書かない）

front matter（キーの並びは schema/keys.yml の page の節の順＝design §3.3 の台帳の表の順）:
  目次から写すキー   keys.yml で catalog: true のキー（id・title・nav_title・…・sections）。目次にないキーと、値が null の
                     キーは書かない（null は書かないのと同じに読まれる）。空のリストは目次のとおり書く
  道具が足すキー     field（目次の分野のファイル）・order（分野のファイルの pages の並び。10 刻み）・stage（site.yml の
                     stages の最初＝骨格の段）・updated（--date。既定は今日）
  執筆者のキー       sources は、keys.yml の required でそのページに必須のときだけ空のリストにする（guide・hub は書かない）。
                     verified・verified_with・checked は書かない
  写さない目次の項目 materials・templates・visual・level_evidence・notes（執筆の指示として目次に残る）
本文（型ごとの手引き planning/guides/<型>.md の構成は目安で、固定の型にしない。design §2.2・guides/common.md §4）:
  sections の見出し  目次の sections を並びのとおり「## <title> {#<anchor>}」で置く（ほかのページが id#anchor で指す節で、
                     draft にすると check_pages.py「sections」が本文に求める。anchor は骨格の後に変えない）
  routes の目印       routes を持つページ（症状）は、診断の節（anchor が diagnosis）の見出しの下に
                     <!-- gen:begin routes --> と <!-- gen:end routes --> を置く（guides/symptom.md §3。間は gen_site.py が
                     書く）。診断の節がなければ本文の最後に置いて「注意」に出す
  置かないもの       H1（題名はテンプレートが出す）・要点の囲み・別名の行・型の目安の見出し・本体を生成するページの
                     目印（置く節は書く人が決める。ないと gen_site.py が「注意」に出す）
書く前に、作った front matter を page.schema.json に当て、YAML として読み直して同じ値になるかを確かめる。
"""
from __future__ import annotations

import argparse
import datetime
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.base import Fatal, as_text, parse_date  # noqa: E402
from lib.catalog import CatalogPage, load_catalog  # noqa: E402
from lib.ledger import CONDITION_KEY, CONDITION_POOL, Condition, load_ledger  # noqa: E402
from lib.pages import DOCS_DIR, INDEX_NAME, STUBS_DIR, Page, load_docs  # noqa: E402
from lib.schema import SchemaError, load_validator  # noqa: E402
from lib.site import load_site  # noqa: E402
from lib.yamlio import parse_yaml, to_jsonable  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PAGE_SCHEMA = "schema/page.schema.json"
ORDER_STEP = 10                          # order の刻み（後でページを挟めるように）
MADE_KEYS = ("field", "order", "stage", "updated")   # 道具が足すキー（keys.yml の page の節のキー）
EMPTY_WHEN_REQUIRED = ("sources",)       # 執筆者が書くキーのうち、そのページに必須なら空のリストで置くもの
COMPARED_EXTRA = ("field", "order")      # --check で、目次から写すキーのほかに比べるキー
ROUTES_BLOCK = "routes"                  # 症状のページの診断の節に置く生成の部分（tools/gen/routes.py）
ROUTES_SECTION = "diagnosis"             # 診断の節の anchor（guides/symptom.md §3・planning/catalog/symptoms.yaml の冒頭）
ROUTES_MARKER = (f"<!-- gen:begin {ROUTES_BLOCK} -->", f"<!-- gen:end {ROUTES_BLOCK} -->")

CREATE, REWRITE, SAME, KEEP = "create", "rewrite", "same", "keep"


# ---------------------------------------------------------------- YAML の書き方


def flow(value) -> str:
    """値を1行の YAML（流れの書き方。[a, b]・{k: v}）にする。引用符は要るときだけ PyYAML が付ける。"""
    text = yaml.dump([value], Dumper=yaml.SafeDumper, default_flow_style=True, allow_unicode=True, width=1 << 30,
                     sort_keys=False).rstrip("\n")
    return text[1:-1]


def dump_front_matter(meta: dict, date_keys: set[str]) -> str:
    """front matter の YAML（--- を除く）。design §3.3 の例の形：値は1行、マッピングのリストは1項目1行。日付は
    引用符を付けずに書く（ほかの、日付に見える文字列は引用符で囲まれる）。"""
    lines = []
    for key, value in meta.items():
        if key in date_keys and parse_date(value) is not None:
            value = parse_date(value)
        if isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
            lines.append(f"{key}:")
            lines += [f"  - {flow(x)}" for x in value]
        else:
            lines.append(f"{key}: {flow(value)}")
    return "\n".join(lines) + "\n"


def show(value) -> str:
    return "（なし）" if value is None else flow(value)


# ---------------------------------------------------------------- 骨格の1ページ


@dataclass
class Stub:
    page: CatalogPage
    order: int
    rel: str                             # 根からの相対パス（stubs/<field>/<id>.md）
    meta: dict                           # front matter（JSON の形。日付は文字列）
    body: str
    text: str = ""                       # ファイルの中身
    action: str = ""                     # create・rewrite・same（--force で同じ）・keep（書かない）
    why: str = ""                        # keep の理由

    @property
    def id(self) -> str:
        return self.page.id or ""

    @property
    def catalog_file(self) -> str:
        return self.page.file


@dataclass
class Plan:
    stubs: list[Stub]
    notes: list[str] = field(default_factory=list)
    extra: list[Page] = field(default_factory=list)       # stubs/ にあって、目次にない id のページ

    def of(self, action: str) -> list[Stub]:
        return [s for s in self.stubs if s.action == action]


class Skeleton:
    """目次・キーの台帳・site.yml・page.schema.json と、いまある docs/ と stubs/ のページを読んだもの。"""

    def __init__(self, root: Path, date: str):
        self.root = Path(root)
        self.date = date
        self.site = load_site(self.root)                       # 読めなければ Fatal
        ledger = load_ledger(self.root)                        # 読めなければ Fatal
        if ledger.errors:
            raise Fatal(f"{ledger.file} に誤りがある: " + " / ".join(ledger.errors))
        page = ledger.section("page")
        if page is None:
            raise Fatal(f"{ledger.file} に page の節がない")
        self.specs = page.keys
        self.catalog_keys = [k for k in ledger.catalog_keys() if k in self.specs]
        self.date_keys = {k for k, s in self.specs.items() if s.format == "date"}
        missing = [k for k in MADE_KEYS + EMPTY_WHEN_REQUIRED if k not in self.specs]
        if missing:
            raise Fatal(f"{ledger.file} の page の節に {'・'.join(missing)} がない（道具が書くキー）")
        if not self.site.stages:
            raise Fatal("site.yml に stages がない（骨格の段は stages の最初）")
        self.stage = self.site.stages[0]
        self.catalog = load_catalog(self.root, self.site)
        if self.catalog.problems:
            raise Fatal("目次が読めない（tools/check_catalog.py で直す）:\n  "
                        + "\n  ".join(p.format() for p in self.catalog.problems))
        if not self.catalog.files:
            raise Fatal("目次に分野のファイル（planning/catalog/<field>.yaml）がない")
        if not (self.root / PAGE_SCHEMA).is_file():
            raise Fatal(f"{PAGE_SCHEMA} がない（uv run python tools/make_schema.py で作る）")
        try:
            self.validator = load_validator(self.root / PAGE_SCHEMA)
        except SchemaError as e:
            raise Fatal(str(e)) from None
        self.docs = load_docs(self.root, self.site)

    # ---- front matter と本文

    def holds(self, cond: Condition, meta: dict) -> bool:
        """keys.yml の required の条件が、このページに当たるか（lib/ledger.py の Builder.condition と同じ読み方）。"""
        if cond.kind in ("all", "optional"):
            return cond.kind == "all"
        if cond.kind in ("with", "without"):
            return (meta.get(cond.value) is not None) == (cond.kind == "with")
        key = CONDITION_KEY[cond.kind]
        pool = self.site.vocab(CONDITION_POOL[key]) or []
        listed = (self.site.vocab(cond.value) if isinstance(cond.value, str) else list(cond.value)) or []
        values = [v for v in pool if v not in listed] if cond.kind.endswith("_except") else [v for v in listed if v in pool]
        return meta.get(key) in values

    def front_matter(self, p: CatalogPage, order: int) -> dict:
        made = {"field": p.field, "order": order, "stage": self.stage, "updated": self.date}
        meta: dict = {}
        for name in self.specs:
            if name in self.catalog_keys:
                value = p.raw.get(name)
                if value is not None:
                    meta[name] = to_jsonable(value)
            elif name in made:
                meta[name] = made[name]
        for name in EMPTY_WHEN_REQUIRED:
            if self.holds(self.specs[name].required, meta):
                meta[name] = []
        return {k: meta[k] for k in self.specs if k in meta}

    def body(self, p: CatalogPage, rel: str, notes: list[str]) -> str:
        lines: list[str] = []
        anchors = []
        for s in p.sections:
            title, anchor = as_text(s.get("title")), as_text(s.get("anchor"))
            lines += ["", f"## {title} {{#{anchor}}}"]
            anchors.append(anchor)
            if p.routes and anchor == ROUTES_SECTION:
                lines += ["", *ROUTES_MARKER]
        if p.routes and ROUTES_SECTION not in anchors:
            lines += ["", *ROUTES_MARKER]
            notes.append(f"{rel}: 診断の節（anchor が {ROUTES_SECTION}）がないので、routes の目印を本文の最後に置いた")
        return "\n".join(lines) + "\n" if lines else ""

    def render(self, meta: dict, body: str) -> str:
        return "---\n" + dump_front_matter(meta, self.date_keys) + "---\n" + body

    # ---- 計画

    def build(self) -> Plan:
        """目次の全ページの骨格を作り（書かない）、page.schema.json と読み直しで確かめる。誤りがあれば Fatal。"""
        stubs: list[Stub] = []
        notes: list[str] = []
        errors: list[str] = []
        seen: dict[str, str] = {}
        for ff in self.catalog.files.values():
            for i, p in enumerate(ff.pages):
                if p.id is None or p.id + ".md" == INDEX_NAME:
                    errors.append(f"{ff.file}: {p.label}: id がない・使えない（{INDEX_NAME} は分野の入口の名前）")
                    continue
                if p.id in seen:
                    errors.append(f"{ff.file}: {p.id}: 同じ id のページが {seen[p.id]} にもある")
                    continue
                seen[p.id] = ff.file
                order = (i + 1) * ORDER_STEP
                rel = f"{STUBS_DIR}/{p.field}/{p.id}.md"
                meta = self.front_matter(p, order)
                for issue in self.validator.errors(meta):
                    errors.append(f"{ff.file}: {p.id}: {issue.format()}")
                stub = Stub(p, order, rel, meta, self.body(p, rel, notes))
                stub.text = self.render(meta, stub.body)
                doc = parse_yaml(dump_front_matter(meta, self.date_keys))
                if doc.error is not None or to_jsonable(doc.data) != meta:
                    errors.append(f"{ff.file}: {p.id}: 書いた front matter を読み直すと値が変わる（{doc.error or '値の違い'}）")
                stubs.append(stub)
        if errors:
            raise Fatal(f"目次から作った front matter が {PAGE_SCHEMA} に通らない（1ページも書かない）:\n  "
                        + "\n  ".join(errors))
        return Plan(stubs, notes)

    def same_but_updated(self, stub: Stub, old: Page) -> bool:
        """いまの骨格のファイルが、updated のほかは作り直したものと同じか。"""
        updated = old.raw.get("updated") if old.md.meta is not None else None
        if parse_date(updated) is None:
            return False
        meta = dict(stub.meta, updated=str(updated))
        return self.render(meta, stub.body) == old.md.text.replace("\r\n", "\n")

    def plan(self, force: bool) -> Plan:
        """骨格ごとに、作る・作り直す・同じ・書かないを決める（書かない）。"""
        plan = self.build()
        by_id: dict[str, list[Page]] = {}
        for q in self.docs.pages:
            by_id.setdefault(q.id, []).append(q)
        catalog_ids = {s.id for s in plan.stubs}
        for stub in plan.stubs:
            here = by_id.get(stub.id, [])
            docs_rel = f"{DOCS_DIR}/{stub.page.field}/{stub.id}.md"
            in_docs = [q for q in here if q.in_docs]
            own = next((q for q in here if not q.in_docs and q.md.shown == stub.rel), None)
            elsewhere = [q for q in here if not q.in_docs and q is not own]
            if in_docs or (self.root / docs_rel).exists():
                stub.action, stub.why = KEEP, "docs"
                where = in_docs[0].md.shown if in_docs else docs_rel
                if own is not None or elsewhere:
                    plan.notes.append(f"{stub.id}: {where} と stubs/ の両方にある（docs/ へ移したら stubs/ のほうを消す）")
            elif elsewhere:
                stub.action, stub.why = KEEP, "elsewhere"
                plan.notes.append(f"{stub.id}: {elsewhere[0].md.shown} にある（目次の分野は {stub.page.field}。{stub.rel} へ"
                                  "移すか、目次を直す）")
            elif own is not None or (self.root / stub.rel).exists():
                if not force:
                    stub.action, stub.why = KEEP, "stubs"
                elif own is not None and self.same_but_updated(stub, own):
                    stub.action = SAME
                else:
                    stub.action = REWRITE
            else:
                stub.action = CREATE
        plan.extra = [q for q in self.docs.pages if not q.in_docs and q.id not in catalog_ids]
        if plan.extra:
            plan.notes.append(f"目次にない id の骨格のページ {len(plan.extra)}（--check で一覧を出す）")
        return plan

    def write(self, plan: Plan) -> None:
        for stub in plan.of(CREATE) + plan.of(REWRITE):
            path = self.root / stub.rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(stub.text, encoding="utf-8")

    # ---- 目次との差（--check）

    def differences(self, stub: Stub, old: Page) -> list[str]:
        got = to_jsonable(old.raw)
        out = []
        for key in self.specs:
            if key not in self.catalog_keys and key not in COMPARED_EXTRA:
                continue
            want, have = stub.meta.get(key), got.get(key)
            if want == have:
                continue
            if isinstance(want, list) and isinstance(have, list):
                only_want = [x for x in want if x not in have]
                only_have = [x for x in have if x not in want]
                if not only_want and not only_have:
                    out.append(f"{key}: 並びか数が違う（目次 {show(want)}・stub {show(have)}）")
                    continue
                parts = ([f"目次にだけ {show(only_want)}"] if only_want else []) + \
                        ([f"stub にだけ {show(only_have)}"] if only_have else [])
                out.append(f"{key}: " + "・".join(parts))
            else:
                out.append(f"{key}: 目次 {show(want)}・stub {show(have)}")
        return out

    def check(self, plan: Plan) -> tuple[list[str], dict[str, int]]:
        """目次と stubs/ の front matter の差（1件1行）と数。docs/ にあるページは比べない（front matter が正）。"""
        lines: list[str] = []
        count = Counter()
        stubs_by_id: dict[str, list[Page]] = {}
        for q in self.docs.pages:
            if not q.in_docs:
                stubs_by_id.setdefault(q.id, []).append(q)
        for stub in plan.stubs:
            found = stubs_by_id.get(stub.id, [])
            if stub.why == "docs":
                count["docs"] += 1
                for q in found:
                    lines.append(f"重なり: {q.md.shown}: docs/ にも同じ id のページがある（docs/ へ移したなら stubs/ のほうを消す）")
                    count["dup"] += 1
                continue
            if not found:
                lines.append(f"ない: {stub.rel}（{stub.catalog_file} の pages の {stub.order // ORDER_STEP} 番目）")
                count["missing"] += 1
                continue
            count["stubs"] += 1
            changed = False
            for q in found:
                if q.md.shown != stub.rel:
                    lines.append(f"置き場所: {q.md.shown}: 目次の分野は {stub.page.field}（{stub.rel} に置く）")
                    count["placed"] += 1
                if q.md.meta is None:
                    lines.append(f"読めない: {q.md.shown}: front matter が読めない（check_pages.py で直すか、--force で作り直す）")
                    count["broken"] += 1
                    continue
                diffs = self.differences(stub, q)
                lines += [f"差: {q.md.shown}: {d}" for d in diffs]
                count["keys"] += len(diffs)
                changed = changed or bool(diffs)
            count["changed"] += changed
        for q in plan.extra:
            lines.append(f"目次にない: {q.md.shown}（目次の pages にない id。目次から外したなら消す）")
            count["extra"] += 1
        return lines, count


# ---------------------------------------------------------------- 入口


def field_counts(site_fields: list[str], stubs: list[Stub]) -> str:
    c = Counter(s.page.field for s in stubs)
    return "・".join(f"{f} {c[f]}" for f in site_fields if c[f])


def report_write(sk: Skeleton, plan: Plan, dry_run: bool, force: bool) -> None:
    made, redo, same, keep = plan.of(CREATE), plan.of(REWRITE), plan.of(SAME), plan.of(KEEP)
    why = Counter(s.why for s in keep)
    verb = ("作る", "作り直す") if dry_run else ("作った", "作り直した")
    head = f"目次 {len(plan.stubs)} ページ（{len(sk.catalog.files)} 分野）：{verb[0]} {len(made)}"
    if force:
        head += f"・{verb[1]} {len(redo)}・目次と同じ {len(same)}"
    head += f"・書かない {len(keep)}（docs/ にある {why['docs']}・stubs/ にある {why['stubs']}・ほかの分野にある {why['elsewhere']}）"
    print(head + ("。--dry-run なので書いていない" if dry_run else ""))
    if made:
        print(f"  {verb[0]}骨格の分野ごとの数：{field_counts(sk.site.fields, made)}")
    for s in redo:
        print(f"  {verb[1]} {s.rel}")
    for n in plan.notes:
        print(f"注意: {n}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="make_skeleton.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="目次と stubs/ の front matter の差を出す（書かない）")
    mode.add_argument("--dry-run", action="store_true", help="書かずに数を出す")
    parser.add_argument("--force", action="store_true", help="stubs/ にある骨格も目次から作り直す（docs/ には触れない）")
    parser.add_argument("--date", type=datetime.date.fromisoformat, metavar="YYYY-MM-DD",
                        help="updated に書く日（既定は今日）")
    parser.add_argument("--root", metavar="DIR", help="置き場所の根（既定はこのリポジトリ）")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.check and args.force:
        parser.error("--check と --force は一緒に使えない")
    root = Path(args.root).resolve() if args.root else ROOT
    date = (args.date or datetime.date.today()).isoformat()
    try:
        sk = Skeleton(root, date)
        plan = sk.plan(args.force)
    except Fatal as e:
        print(f"作れない: {e}", file=sys.stderr)
        return 2
    if args.check:
        lines, n = sk.check(plan)
        for line in lines:
            print(line)
        scope = f"目次 {len(plan.stubs)} ページ：stubs/ にある {n['stubs']}・docs/ にあり比べない {n['docs']}"
        if not lines:
            print(f"目次と stubs/ の front matter は同じ（{scope}）")
            return 0
        print(f"差がある：ない {n['missing']}・値の違う {n['changed']} ページ（{n['keys']} キー）・置き場所 {n['placed']}・"
              f"読めない {n['broken']}・重なり {n['dup']}・目次にない {n['extra']}（{scope}）。目次に合わせるなら "
              "make_skeleton.py（stubs/ にあるものは --force）")
        return 1
    report_write(sk, plan, args.dry_run, args.force)
    if not args.dry_run:
        sk.write(plan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
