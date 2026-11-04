"""data/ を読む（設計書 §9.1・§6.8・DR-11・DR-18）。形は schema/keys.yml の各節と、そこから作る schema/*.schema.json。

  data/facts.yml            facts（変わりやすい値）・features（機能の属性）・names（名称と旧名）
  data/sources.yml          domains（AI の利用の指定を確かめたドメイン）・sources（出典）
  data/sources.d/<id>.yml   ページごとに執筆者が足す domains・sources（同じ形。道具が1つにまとめる）
  data/outdated-advice.yml  advice（古くなった助言の台帳）
  data/inspection.yml       last（前回の点検の版と日付。design §9.4）

項目は Item（Record）で、項目の名前は id（domains だけは domain）。同じ id が二度あっても読む層は捨てず、
entries に全部を残す（重なりの検査は検査の層）。index・facts などは最初のものを引く。
"""
from __future__ import annotations

import urllib.parse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from .base import Problem, Record, as_text
from .yamlio import read_yaml

DATA_DIR = "data"
DATA_FILES = {   # ファイル → 最上位のリスト（schema/keys.yml の facts・sources・outdated-advice の節と同じ。試験が照らす）
    "data/facts.yml": ("facts", "features", "names"),
    "data/sources.yml": ("domains", "sources"),
    "data/outdated-advice.yml": ("advice",),
}
SOURCES_D = "data/sources.d"
SOURCES_D_SECTIONS = ("domains", "sources")
INSPECTION_FILE = "data/inspection.yml"
INSPECTION_KEY = "last"
KEY_OF = {"domains": "domain"}            # 項目の名前のキー（ほかは id）


class Item(Record):
    """data の1項目。"""

    def __init__(self, raw: dict, file: str, section: str, index: int):
        super().__init__(raw, file, KEY_OF.get(section, "id"))
        self.section = section         # facts・features・names・domains・sources・advice
        self.index = index

    @property
    def label(self) -> str:
        return self.id or f"({self.section} の {self.index + 1} 番目)"

    @property
    def checked(self):
        """確認日（date か None）。"""
        return self.date("checked")

    @property
    def volatility(self) -> str:
        return self.text("volatility")


@dataclass
class DataFile:
    file: str
    present: bool
    raw: dict | None = None            # 読めてマッピングだったときだけ

    @property
    def readable(self) -> bool:
        return self.raw is not None


def host_of(url_or_host: str) -> str:
    """URL かホスト名から、ホスト名（小文字。末尾の点を除く）。"""
    s = url_or_host.strip()
    host = urllib.parse.urlsplit(s).hostname if "://" in s else s.split("/")[0].split(":")[0]
    return (host or "").lower().rstrip(".")


def url_key(url: str) -> str:
    """URL の重なりを見るための形：scheme とホストを小文字に、既定のポートと #… と、パスの末尾の / を除く。"""
    parts = urllib.parse.urlsplit(url.strip())
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower().rstrip(".")
    port = parts.port if parts.port and (scheme, parts.port) not in (("http", 80), ("https", 443)) else None
    path = parts.path.rstrip("/") if parts.path not in ("", "/") else ""
    return urllib.parse.urlunsplit((scheme, f"{host}:{port}" if port else host, path, parts.query, ""))


class Data:
    """data/ の全体（読む層の出力）。"""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.files: dict[str, DataFile] = {}
        self.items: dict[str, list[Item]] = defaultdict(list)
        self.inspection: dict | None = None
        self.problems: list[Problem] = []

    def entries(self, section: str) -> list[Item]:
        """その節の全項目（ファイルの順。sources と domains は data/sources.yml、sources.d/ の順）。"""
        return list(self.items.get(section, ()))

    def index(self, section: str) -> dict[str, Item]:
        """id（domains は domain の小文字）→ 項目。同じ id は最初のもの。"""
        out: dict[str, Item] = {}
        for it in self.items.get(section, ()):
            key = it.id
            if key is not None:
                out.setdefault(key.lower() if section == "domains" else key, it)
        return out

    @property
    def facts(self) -> dict[str, Item]:
        return self.index("facts")

    @property
    def features(self) -> dict[str, Item]:
        return self.index("features")

    @property
    def names(self) -> dict[str, Item]:
        return self.index("names")

    @property
    def sources(self) -> dict[str, Item]:
        return self.index("sources")

    @property
    def advice(self) -> dict[str, Item]:
        return self.index("advice")

    @property
    def domains(self) -> dict[str, Item]:
        return self.index("domains")

    def domain_entry(self, url_or_host: str) -> Item | None:
        """URL のホストに当たる domains の項目（いちばん長く一致するもの。sub.example.com は example.com にも当たる）。"""
        host = host_of(url_or_host)
        table = self.domains
        labels = host.split(".")
        for i in range(len(labels) - 1):
            hit = table.get(".".join(labels[i:]))
            if hit is not None:
                return hit
        return None

    def noai_domains(self) -> list[str]:
        """AI の利用を断る指定のあるドメイン（noai: true。design §10.5 の H1 の deny に要るもの）。"""
        return sorted(d for d, it in self.domains.items() if it.raw.get("noai") is True)

    def last_inspection(self) -> dict:
        v = self.inspection.get(INSPECTION_KEY) if isinstance(self.inspection, dict) else None
        return v if isinstance(v, dict) else {}


def _load_file(data: Data, shown: str, sections: tuple[str, ...]) -> DataFile:
    path = data.root / shown
    df = DataFile(shown, path.exists())
    data.files[shown] = df
    if not df.present:
        data.problems.append(Problem(shown, None, "ファイルがない（空の雛形は「節: []」の形）", "設定"))
        return df
    doc = read_yaml(path)
    data.problems.extend(doc.problems(shown))
    if doc.error is not None:
        return df
    if not isinstance(doc.data, dict):
        empty = "（空のファイル）" if doc.data is None else ""
        data.problems.append(Problem(shown, None, f"最上位をマッピング（{'・'.join(sections)}）にする{empty}", "形"))
        return df
    df.raw = doc.data
    for section in sections:
        items = doc.data.get(section)
        if isinstance(items, list):
            data.items[section].extend(Item(x, shown, section, i) for i, x in enumerate(items) if isinstance(x, dict))
    return df


def load_data(root: Path) -> Data:
    """data/ を読む。ないファイルは「設定」の Problem にして、空として読む。"""
    data = Data(root)
    for shown, sections in DATA_FILES.items():
        _load_file(data, shown, sections)
    sdir = data.root / SOURCES_D
    if sdir.is_dir():
        for path in sorted(sdir.iterdir()):
            shown = f"{SOURCES_D}/{path.name}"
            if path.is_file() and path.suffix == ".yml":
                _load_file(data, shown, SOURCES_D_SECTIONS)
            elif (path.is_file() and path.suffix in (".yaml", ".json")) or path.is_dir():
                data.problems.append(Problem(shown, None, f"{SOURCES_D}/ のファイルは <ページの id>.yml にする（読んでいない）",
                                             "置き場所"))
    df = _load_file(data, INSPECTION_FILE, ())
    data.inspection = df.raw
    return data


def sources_files(data: Data) -> list[str]:
    """出典を持つファイル（data/sources.yml と data/sources.d/*.yml）。"""
    return [f for f in data.files if f == "data/sources.yml" or f.startswith(SOURCES_D + "/")]


def page_of_sources_file(shown: str) -> str | None:
    """data/sources.d/<id>.yml の <id>（ほかのファイルなら None）。"""
    if not shown.startswith(SOURCES_D + "/") or not shown.endswith(".yml"):
        return None
    return as_text(shown[len(SOURCES_D) + 1:-len(".yml")]) or None
