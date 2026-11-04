"""作る層（設計書 §8.3）：読む層（tools/lib/）のモデルから、生成物と、手書きのページの目印の中身を作る。入口は
tools/gen_site.py。生成物の種類ごとに1つの部品にした。

  config.py / config.yml  作る層の設定（表示の言葉・どのページに何を生成するか・逆引きの分け方・公開から外す試作のページ）
  core.py      Gen：読む層の Atlas と設定を合わせ、公開の判定・リンク・表示の言葉・逆向きの参照を引く
  blocks.py    生成の部分（gen:begin 名前）の登録
  markers.py   目印の間を書く（gen・fact・link）。参考の節とページ下部の目印がなければ末尾に足す
  pagebits.py  参考の節（references）・ページ下部（page-links）・知識マップの図の場所（graph）
  facts.py     数値（fact の目印・fact-table）・機能の属性（feature）・比較の表（compare）
  routes.py    症状のページの振り分け（routes）・症状の原因別の表（causes）
  snippets.py  雛形の写し（snippet <id>/<名前>）
  reverse.py   逆引き（signs <type>）
  terms.py     用語索引と旧名（terms kana・latin・old）
  roadmap.py   ロードマップ（roadmap）
  ledger.py    古くなった助言の台帳（ledger）と年表（timeline）
  pages_out.py 生成するファイル：nav.yml・分野の入口・一覧・llms.txt・pages.json・graph.json
  build.py     生成物の全体（ファイル → 中身）と、消す古い生成物
  text.py      Markdown・YAML・JSON の書き方の部品

生成物は、同じ入力から同じ文字列になる（日時・ハッシュを入れない。design §8.4）。語彙は site.yml から読み、表示の言葉は
config.yml から読む（コードに語彙を書かない）。
"""
from . import facts, ledger, pagebits, reverse, roadmap, routes, snippets, terms  # noqa: F401（生成の部分を登録する）
from .blocks import REGISTRY
from .build import outputs, page_outputs
from .core import Gen, load_gen

__all__ = ["REGISTRY", "Gen", "load_gen", "outputs", "page_outputs"]
