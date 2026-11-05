# build-NP：書かないページを道具が見分ける（2026-11-06）

## 変えたこと
- `tools/gen/config.yml`：`unplanned_priorities: [任意]` を足した（最上位。`held_back` と同じ並び）。優先度がこれに当たり、stage が site.yml の stages の先頭（stub）のページを「書かないページ」とする
- `tools/gen/config.py`：`Config.unplanned_priorities`
- `tools/gen/core.py`：`Gen.is_unplanned(page)`・`Gen.is_unplanned_ref(ref)`。`page_link` は書かないページなら題名だけを返す（リンクなし・「（準備中）」なし。`id#anchor` も同じで、節の題名も付けない）。`link` の目印・facts の比較の表・用語索引などは `page_link` を通るので全部これに従う
- `tools/gen/pagebits.py`：ページ下部（page-links）の前提・次に読む（routes の先と、このページを前提にするページ）・関連から外す。前提がすべて外れたら「なし」
- `tools/gen/routes.py`：routes の表の行き先から外す（全部外れた行は「—」）
- `tools/gen/ledger.py`：台帳の「関わるページ」から外す
- nav・逆引き・用語索引・分野の入口・一覧・llms.txt・graph.json は、もともと `gen.published`（stub は未公開）だけを載せるので変更なし
- front matter の値は書き換えない
- 検査（tools/checks/）は変更なし。目印の外の手書きのリンクが骨格を指す誤りは今まで通り（目印にすれば題名だけが出る）。link の目印は検査で誤りにならない
- `planning/guides/card.md` §9：1行足した（223行）
- 試験：`tests/tools/test_gen_site.py` に `TestUnplanned`（6件）。一時フォルダに任意の骨格を足し、link の目印が題名だけ（節を指す形も）、ページ下部の前提・関連・次に読む・routes の表・一覧から外れること、front matter が変わらないこと、設定を `[]` にすれば「（準備中）」に戻ることを見る。既存の試験の期待は直さずに通った

## 試験の結果
- `unittest discover -s tests/tools`：693件、失敗1（`test_gen_catalog.TestRealRepository.test_generated_files_are_fresh`）。本物のリポジトリの生成物が、設定を足したことで古くなっただけ（想定どおり。メインが生成すれば直る）。ほかは通った
- `tests/guides`：17件 OK
- `gen_site.py --check`：113ファイルが「古い」（生成待ち）

## メインに判断してほしいこと
- `uv run python tools/gen_site.py` で生成して commit する（本物の docs/ の「題名（準備中）」173＋関連140か所が、骨格の任意では題名だけ・一覧から外れる形に変わる）
- 任意の骨格を指す関連・前提がページ下部から消えるので、読者は関連として見られない。残したいものは、骨格を書くか優先度を変える
- 書かないページを指す routes の行き先も表から外した（仕様の「生成の一覧」に含めた判断）

## 道具の呼び出し
約20回（Bash 12・Read 2・Edit/Write 3 ほか）
