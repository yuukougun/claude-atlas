"""作る層の設定（tools/gen/config.yml）と、mkdocs.yml のサイトの名前・URL を読む。

設定は <根>/tools/gen/config.yml（--root で試験の置き場所を渡したときに、そこになければ、この道具の隣の config.yml）。
値の形が違うものは既定に倒して読み、problems に記録する（gen_site.py が「注意」に出す）。読めないときは Fatal。
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from lib.base import Fatal, as_strings, as_text
from lib.yamlio import read_yaml

CONFIG_FILE = "tools/gen/config.yml"
OWN_CONFIG = Path(__file__).resolve().parent / "config.yml"
MKDOCS_FILE = "mkdocs.yml"


@dataclass
class Config:
    raw: dict
    file: str
    problems: list[str] = field(default_factory=list)

    # ---- 値の引き方

    def section(self, name: str) -> dict:
        v = self.raw.get(name)
        if v is None:
            return {}
        if not isinstance(v, dict):
            self.problems.append(f"{self.file}: {name} がマッピングでない（読まない）")
            return {}
        return v

    def text(self, section: str, key: str, default: str = "") -> str:
        v = self.section(section).get(key)
        if v is None:
            return default
        if isinstance(v, (str, int)) and not isinstance(v, bool):
            return str(v)
        self.problems.append(f"{self.file}: {section}.{key} が文字列でない（既定の「{default}」を使う）")
        return default

    def number(self, section: str, key: str, default: int) -> int:
        v = self.section(section).get(key)
        if isinstance(v, int) and not isinstance(v, bool) and v > 0:
            return v
        if v is not None:
            self.problems.append(f"{self.file}: {section}.{key} が正の整数でない（既定の {default} を使う）")
        return default

    @property
    def held_back(self) -> list[str]:
        return as_strings(self.raw.get("held_back"))

    def role(self, name: str) -> str:
        return as_text(self.section("roles").get(name))

    def labels(self, kind: str) -> dict[str, str]:
        """labels の kind（types・stages・surfaces など）：値 → 表示の言葉。"""
        v = self.section("labels").get(kind)
        if not isinstance(v, dict):
            return {}
        return {str(k): str(x) for k, x in v.items() if x is not None}

    def label_text(self, key: str, default: str) -> str:
        """labels の1つの言葉（unpublished・draft_mark など）。"""
        v = self.section("labels").get(key)
        return v if isinstance(v, str) else default

    def hosts(self) -> dict[str, list[str]]:
        """ページの id → そのページに置く生成の部分の名前。"""
        out = {}
        for pid, names in self.section("hosts").items():
            out[str(pid)] = [" ".join(n.split()) for n in as_strings(names)]
        return out

    def list_pages(self) -> list[dict]:
        items = self.section("lists").get("pages")
        out = []
        for x in items if isinstance(items, list) else []:
            if isinstance(x, dict) and as_text(x.get("file")) and as_text(x.get("key")) and as_text(x.get("vocab")):
                if not re.fullmatch(r"[a-z0-9][a-z0-9-]*\.md", as_text(x.get("file"))):
                    self.problems.append(f"{self.file}: lists.pages の file「{x.get('file')}」は英小文字・数字・ハイフンの .md にする")
                    continue
                out.append(x)
            else:
                self.problems.append(f"{self.file}: lists.pages の項目に file・key・vocab がない（{x!r}）")
        return out

    def entrance_extra(self) -> list[dict]:
        items = self.section("entrance").get("extra")
        return [x for x in items if isinstance(x, dict) and as_text(x.get("field")) and as_text(x.get("key"))
                and x.get("value") is not None] if isinstance(items, list) else []

    def reverse_group(self, sign_type: str) -> str:
        g = self.section("reverse").get("group")
        return as_text(g.get(sign_type)) if isinstance(g, dict) else ""

    def field_to_symptom_chapter(self) -> dict[str, str]:
        v = self.section("reverse").get("field_to_symptom_chapter")
        return {str(k): str(x) for k, x in v.items() if isinstance(x, str)} if isinstance(v, dict) else {}


def load_config(root: Path) -> Config:
    """<根>/tools/gen/config.yml を読む（なければ、この道具の隣の config.yml）。読めなければ Fatal。"""
    path = Path(root) / CONFIG_FILE
    if not path.exists():
        path = OWN_CONFIG
    shown = CONFIG_FILE if path != OWN_CONFIG or (Path(root) / CONFIG_FILE).exists() else str(OWN_CONFIG)
    doc = read_yaml(path)
    if doc.error is not None:
        raise Fatal(f"{shown} が読めない: {doc.error}")
    if not isinstance(doc.data, dict):
        raise Fatal(f"{shown} の最上位がマッピングでない")
    cfg = Config(doc.data, shown)
    cfg.problems += [p.format() for p in doc.problems(shown)]
    return cfg


# ---------------------------------------------------------------- mkdocs.yml


class _TagTolerantLoader(yaml.SafeLoader):
    """mkdocs.yml の !!python/… の印を None として読む（site_url などのキーだけを見るため）。"""


_TagTolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)


@dataclass(frozen=True)
class SiteInfo:
    name: str
    url: str            # 末尾は /
    description: str


def load_site_info(root: Path) -> SiteInfo:
    """mkdocs.yml の site_name・site_url・site_description（ないものは空。読めなければ Fatal）。"""
    path = Path(root) / MKDOCS_FILE
    try:
        raw = yaml.load(path.read_text(encoding="utf-8"), Loader=_TagTolerantLoader)  # noqa: S506（印を None にする読み方）
    except FileNotFoundError:
        raise Fatal(f"{MKDOCS_FILE} がない") from None
    except (OSError, yaml.YAMLError) as e:
        raise Fatal(f"{MKDOCS_FILE} が読めない: {e}") from None
    raw = raw if isinstance(raw, dict) else {}
    url = as_text(raw.get("site_url"))
    if url and not url.endswith("/"):
        url += "/"
    return SiteInfo(as_text(raw.get("site_name")), url, as_text(raw.get("site_description")))
