"""YAML を読む（読む層の部品）。tools/check_catalog.py の読み方（_Loader・LineDict・read_yaml）を写して、次を足した。

- マッピングは LineDict：行番号（.line。マッピングの始まり）と、キーごとの行（.key_lines）を持つ dict
- 同じマッピングに同じキーが2回あるものを記録する（YAML では後のものだけが残り、気づきにくい）
- 日付（2026-11-04）は文字列のまま読む（YAML の timestamp にしない）。front matter と data の日付を JSON Schema の
  format: date で検査できる形にそろえ、2026-13-45 のような値でも読むのが止まらないようにするため。日付として
  使うときは base.parse_date で読む
- line_offset：front matter のように、ファイルの途中から始まる YAML の行番号を、ファイルの行に直す
"""
from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .base import Problem

TIMESTAMP_TAG = "tag:yaml.org,2002:timestamp"
MERGE_TAG = "tag:yaml.org,2002:merge"


class LineDict(dict):
    """行番号（1 から。ファイルの行）を持つ dict。line はマッピングの始まり、key_lines はキー（文字列）ごとの行。"""

    line: int | None = None
    key_lines: dict = {}            # 作るときにインスタンスごとに置き換える（この既定は空のまま使わない）


def line_of(x) -> int | None:
    return getattr(x, "line", None)


class _Loader(yaml.SafeLoader):
    """SafeLoader に、マッピングの行番号・同じキーの記録・行のずらし・日付を文字列のままにすることを足したもの。"""

    def __init__(self, stream, line_offset: int = 0):
        super().__init__(stream)
        self.line_offset = line_offset
        self.duplicate_keys: list[tuple[str, int, int]] = []   # (キー, 行, 先にあった行)

    def construct_mapping(self, node, deep=False):
        if isinstance(node, yaml.MappingNode):
            seen: dict[str, int] = {}
            for key_node, _ in node.value:
                if isinstance(key_node, yaml.ScalarNode) and key_node.tag != MERGE_TAG:
                    line = key_node.start_mark.line + 1 + self.line_offset
                    if key_node.value in seen:
                        self.duplicate_keys.append((key_node.value, line, seen[key_node.value]))
                    else:
                        seen[key_node.value] = line
        return super().construct_mapping(node, deep=deep)


# 日付を timestamp にしない（文字列のまま読む）。SafeLoader の表は変えない
_Loader.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag != TIMESTAMP_TAG]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _construct_map(loader: _Loader, node):
    data = LineDict()
    data.line = node.start_mark.line + 1 + loader.line_offset
    data.key_lines = {}
    yield data
    data.update(loader.construct_mapping(node))
    for key_node, _ in node.value:
        if isinstance(key_node, yaml.ScalarNode) and key_node.tag != MERGE_TAG:
            data.key_lines[key_node.value] = key_node.start_mark.line + 1 + loader.line_offset


_Loader.add_constructor("tag:yaml.org,2002:map", _construct_map)


@dataclass
class YamlDoc:
    """YAML を読んだ結果。読めなければ error に理由（data は None）。"""

    data: object = None
    error: str | None = None
    error_line: int | None = None
    duplicates: list[tuple[str, int, int]] = field(default_factory=list)

    def problems(self, file: str, id: str = "-") -> list[Problem]:
        """読めない・同じキーが2回ある、を指摘にする（種類は YAML）。"""
        out = []
        if self.error is not None:
            out.append(Problem(file, self.error_line, self.error, "YAML", id))
        for key, line, first in self.duplicates:
            out.append(Problem(file, line, f"同じキー「{key}」が2回ある（{first} 行にもある。後のものだけが読まれる）",
                               "YAML", id))
        return out


def parse_yaml(text: str, line_offset: int = 0) -> YamlDoc:
    """YAML の文字列を読む。line_offset は、文字列の1行目がファイルの何行目の次か（front matter なら 1）。"""
    loader = _Loader(text, line_offset)
    try:
        return YamlDoc(data=loader.get_single_data(), duplicates=loader.duplicate_keys)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None) or getattr(e, "context_mark", None)
        problem = " ".join(str(getattr(e, "problem", None) or e).split())
        context = getattr(e, "context", None)
        line = mark.line + 1 + line_offset if mark else None
        where = f"{line} 行 {mark.column + 1} 列" if mark else "位置は不明"
        return YamlDoc(error=f"YAML が読めない（{where}）: {problem}" + (f"（{context}）" if context else ""),
                       error_line=line)
    except (ValueError, TypeError, RecursionError) as e:   # 明示の !!timestamp の誤りなど、値を作れないもの
        return YamlDoc(error=f"YAML の値が読めない: {e}")
    finally:
        loader.dispose()


def read_yaml(path: Path) -> YamlDoc:
    """ファイルを読む（UTF-8。先頭の BOM は除く）。"""
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError) as e:
        return YamlDoc(error=f"ファイルが読めない（{e}）")
    return parse_yaml(text)


def to_jsonable(v):
    """JSON Schema で検査できる形にする（キーは文字列、日付は ISO の文字列、集合はリスト）。"""
    if isinstance(v, dict):
        return {str(k): to_jsonable(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [to_jsonable(x) for x in v]
    if isinstance(v, (set, frozenset)):
        return sorted((to_jsonable(x) for x in v), key=repr)
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()
    return v


def line_at(data, path) -> int | None:
    """path（キーと位置の並び。schema の検査器の誤りの場所）が指す所の行。いちばん深く分かる所の行を返す。"""
    line = line_of(data)
    node = data
    for part in path:
        if isinstance(node, dict):
            key = part if part in node else next((k for k in node if str(k) == str(part)), None)
            if key is None:
                break
            line = (getattr(node, "key_lines", None) or {}).get(str(key), line)
            node = node[key]
        elif isinstance(node, list) and isinstance(part, int) and 0 <= part < len(node):
            node = node[part]
            line = line_of(node) or line
        else:
            break
    return line
