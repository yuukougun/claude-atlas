"""手書きのページの生成の部分（<!-- gen:begin 名前 --> 〜 <!-- gen:end 名前 -->）の登録。

名前は「<生成の種類>[ <引数>]」（例：references・routes・signs symptom・snippet hooks-basics/block-rm）。種類ごとに
1つの関数を @block で登録する。関数は Ctx を受け取り、目印の間に書く Markdown（目印と textlint の印は含めない）を返す。
  kind="block"   目印をそれぞれ1行に置く（begin の行に目印のほかを書かない）。中身は複数の行
  kind="inline"  文の中に置く。中身は1行の文字
anchors は、その部分が作る見出しの anchor（ほかのページから id#anchor で指せるもの）を返す関数（任意）。
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

REGISTRY: dict[str, "Block"] = {}


@dataclass(frozen=True)
class Block:
    name: str
    kind: str                                  # block・inline
    doc: str
    render: Callable
    anchors: Callable | None = None
    param: str = ""                            # 引数の説明（なければ引数を取らない）
    param_optional: bool = False               # True なら引数を省ける（compare の列の指定）


@dataclass
class Ctx:
    """生成の部分を1つ書くときの材料。page は目印のあるページ（docs/index.md のときは None）。"""

    gen: object                                # core.Gen
    page: object | None                        # lib.pages.Page
    host: str                                  # docs/ の中のパス（start/how-to-use.md・index.md）
    url: str                                   # そのページの URL（サイトの根から。start/how-to-use/）
    param: str                                 # 名前の引数（signs symptom の symptom）
    name: str                                  # 名前の全体


def block(name: str, kind: str = "block", doc: str = "", anchors: Callable | None = None, param: str = "",
          param_optional: bool = False):
    def deco(fn):
        REGISTRY[name] = Block(name, kind, doc, fn, anchors, param, param_optional)
        return fn
    return deco


def split_name(name: str) -> tuple[str, str]:
    """目印の名前 → (種類, 引数)。"""
    head, _, rest = " ".join(name.split()).partition(" ")
    return head, rest


def lookup(name: str) -> tuple[Block | None, str]:
    head, param = split_name(name)
    return REGISTRY.get(head), param
