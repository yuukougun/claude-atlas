"""作る層の全体の材料（Gen）：読む層のモデル（lib.Atlas）・作る層の設定・サイトの名前と URL と、生成物が共通に使う
部品（公開の判定・リンクの書き方・表示の言葉・逆向きの参照）。

公開（design §8.4）：読む層の Atlas.is_published（docs/ にあり、stage が site.yml の published_stages、作る層の設定の
held_back にない）。生成物（nav・入口・一覧・逆引き・索引・ロードマップ・知識マップ・llms.txt・サイト用のデータ）には
公開するページだけを載せる。ページ下部と本文の目印が未公開のページを指すときは「題名（準備中）」の平文にする。
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from lib import Atlas, load_atlas
from lib.base import FIELD_PREFIX, Ref, as_text

from . import blocks as B
from .config import Config, SiteInfo, load_config, load_site_info
from .text import join_marks, md_text, rel_md


class Gen:
    def __init__(self, root: Path, atlas: Atlas, config: Config, info: SiteInfo):
        self.root = Path(root)
        self.atlas = atlas
        self.site = atlas.site
        self.config = config
        self.info = info
        self.notes: list[str] = list(config.problems)
        # ページ（同じ id は読む層の by_id のほう＝docs/ を先に読んだもの）。ナビゲーションの順
        self.pages = [p for p in atlas.ordered() if p.id and atlas.by_id.get(p.id) is p]
        self.rank = {p.id: i for i, p in enumerate(self.pages)}
        self.published = [p for p in self.pages if atlas.is_published(p)]
        self.pub_ids = {p.id for p in self.published}
        # 役（config.yml の roles）
        self.symptom_type = config.role("symptom_type")
        self.feature_type = config.role("feature_type")
        self.symptom_field = config.role("symptom_field")
        self.confirmed = config.role("fact_confirmed")
        # 逆向きの参照
        self.dependents: dict[str, list] = defaultdict(list)     # 前提の id → それを前提にするページ（ナビの順）
        self.routed_from: dict[str, list] = defaultdict(list)    # 振り分け先の id → 振り分ける症状のページ
        self.advice_pages: dict[str, list] = defaultdict(list)   # 台帳の id → outdated_advice で指すページ
        for p in self.pages:
            for r in dict.fromkeys(x.target for x in p.prerequisites):
                self.dependents[r].append(p)
            if p.type == self.symptom_type:
                for r in dict.fromkeys(x.target for x in p.route_targets()):
                    self.routed_from[r].append(p)
            for a in dict.fromkeys(p.outdated_advice):
                self.advice_pages[a].append(p)
        self._anchors: dict[str, set[str]] = {}
        # ページ → 生成の部分（fact-table）が使う数値の id（期限の日に数える。fact の目印は読む層が数える）
        self.extra_facts: dict[str, list[str]] = {}
        for p in self.pages:
            ids = [B.split_name(m.arg)[1] for m in p.markers_of("gen") if B.split_name(m.arg)[0] == "fact-table"]
            if any(ids):
                self.extra_facts[p.id] = [x for x in ids if x]
        self._expiry: dict[str, object] = {}

    def expiry_of(self, page):
        """期限の日（読む層の Atlas.expiry に、生成の部分が使う数値も数える）。"""
        if page.id not in self._expiry:
            self._expiry[page.id] = self.atlas.expiry(page, extra_facts=self.extra_facts.get(page.id, ()))
        return self._expiry[page.id]

    # ---- 注意

    def note(self, msg: str) -> None:
        if msg not in self.notes:
            self.notes.append(msg)

    # ---- ページ

    def is_pub(self, page) -> bool:
        return page is not None and page.id in self.pub_ids

    @staticmethod
    def doc_rel(page) -> str:
        """docs/ の中のパス（stubs/ のページは docs/ へ移したときのパス）。"""
        return f"{page.field}/{page.stem}.md"

    @staticmethod
    def title(page) -> str:
        return page.title or page.id

    def section_title(self, page, anchor: str) -> str | None:
        for s in page.sections:
            if as_text(s.get("anchor")) == anchor:
                return as_text(s.get("title")) or None
        return None

    @staticmethod
    def hand_anchors(page) -> set[str]:
        """手書きの見出し（生成の部分の外）の {#anchor}。"""
        spans = [(m.line, m.end_line) for m in page.markers_of("gen") if m.closed]
        return {h.anchor for h in page.headings if h.anchor and not any(a < h.line < b for a, b in spans)}

    def anchors(self, page) -> set[str]:
        """そのページで #anchor として指せる見出し：手書きの見出しの {#anchor}（生成の部分の外）と、生成の部分が作る
        見出しの anchor（今のファイルの中身によらず、生成の部分から数える）。"""
        if page.id in self._anchors:
            return self._anchors[page.id]
        out = self.hand_anchors(page)
        names = [m.arg for m in page.markers_of("gen") if m.closed]
        from .markers import implicit_blocks         # 循環を避ける
        names += implicit_blocks(self, page)
        for name in names:
            blk, param = B.lookup(name)
            if blk is not None and blk.anchors is not None:
                out |= set(blk.anchors(self, page, param))
        self._anchors[page.id] = out
        return out

    # ---- 表示の言葉

    def label(self, kind: str, value: str) -> str:
        labels = self.config.labels(kind)
        if value in labels:
            return labels[value]
        if value:
            self.note(f"tools/gen/config.yml の labels.{kind} に「{value}」がない（値をそのまま表示した）")
        return value

    def text(self, key: str, default: str) -> str:
        return self.config.label_text(key, default)

    def field_title(self, field: str) -> str:
        return self.site.field_titles.get(field) or field

    def unpublished(self, text: str) -> str:
        return f"{text}（{self.text('unpublished', '準備中')}）"

    def draft_mark(self, page) -> str:
        """一覧などで draft のページに添える印の言葉（ほかの段階は空）。"""
        stages = self.site.stages
        return self.text("draft_mark", "下書き") if len(stages) > 1 and page.stage == stages[1] else ""

    def level_text(self, page) -> str:
        return page.level if page.level in self.site.levels else ""

    def kind_marks(self, page) -> str:
        """逆引きなどの行き先に付ける短い印：面と型（DR-15：「アプリ・Claude Code、考え方」）。"""
        surfaces = "・".join(self.label("surfaces", s) for s in page.surfaces)
        typ = self.label("types", page.type) if page.type else ""
        inner = "、".join(x for x in (surfaces, typ) if x)
        return f"（{inner}）" if inner else ""

    def list_marks(self, page, with_field: bool = False) -> str:
        """一覧と入口の行の印：分野（with_field のとき）・レベル・下書き。"""
        parts = [self.field_title(page.field) if with_field else "", self.level_text(page), self.draft_mark(page)]
        return join_marks(parts)

    # ---- リンク

    def page_link(self, host: str, page, anchor: str | None = None, table: bool = False, text: str | None = None) -> str:
        """ページへのリンク。未公開なら「題名（準備中）」の平文。anchor はそのページで指せるときだけ付ける。"""
        label = text if text is not None else md_text(self.title(page), table)
        if anchor:
            sec = self.section_title(page, anchor)
            if sec and text is None:
                label += " › " + md_text(sec, table)
        if not self.is_pub(page):
            return self.unpublished(label)
        href = rel_md(host, self.doc_rel(page))
        if anchor:
            if anchor in self.anchors(page):
                href += "#" + anchor
            else:
                self.note(f"{host}: {page.id}#{anchor} の見出しが {page.id} の本文にない（ページへのリンクにした）")
        return f"[{label}]({href})"

    def field_link(self, host: str, field: str, table: bool = False) -> str:
        """分野の入口（<分野>/index.md）へのリンク（link の目印の field:<分野の id>。表示は分野の名前）。
        分野がない・公開するページがなければ、分野の名前（準備中）の平文。"""
        if field not in self.site.fields:
            self.note(f"{host}: 「{FIELD_PREFIX}{field}」の分野が schema/site.yml の fields にない（文字のまま書いた）")
            return md_text(FIELD_PREFIX + field, table)
        label = md_text(self.field_title(field), table)
        if not any(p.field == field for p in self.published):
            return self.unpublished(label)
        return f"[{label}]({rel_md(host, field + '/index.md')})"

    def ref_link(self, host: str, ref: Ref | str, table: bool = False) -> str:
        """参照（id か id#anchor）へのリンク。相手のページがなければ参照の文字のまま（注意に出す）。"""
        if isinstance(ref, str) and ref.strip().startswith(FIELD_PREFIX):
            return self.field_link(host, ref.strip()[len(FIELD_PREFIX):].strip(), table)
        ref = Ref.parse(ref) if isinstance(ref, str) else ref
        page = self.atlas.resolve(ref)
        if page is None:
            self.note(f"{host}: 「{ref.raw}」のページがない（文字のまま書いた）")
            return md_text(ref.raw, table)
        return self.page_link(host, page, ref.anchor, table)

    def resolve(self, ref: Ref | str):
        return self.atlas.resolve(ref)

    # ---- data

    def feature(self, fid: str):
        data = self.atlas.data
        return data.features.get(fid) if data is not None else None

    def features_of_page(self, pid: str) -> list:
        """そのページを主のページ（page）にする機能（data の features の並び）。"""
        data = self.atlas.data
        if data is None:
            return []
        return [f for f in data.entries("features") if f.text("page") == pid]

    def is_confirmed(self, item) -> bool:
        return bool(self.confirmed) and item.text("status") == self.confirmed


def load_gen(root: Path) -> Gen:
    """根の site.yml・ページ・data・作る層の設定・mkdocs.yml を読む（読めなければ lib.Fatal）。"""
    root = Path(root)
    config = load_config(root)
    atlas = load_atlas(root, held_back=config.held_back)
    return Gen(root, atlas, config, load_site_info(root))
