# write.md：does-more-than-asked

## 書いたファイル
- docs/symptoms/does-more-than-asked.md（stub から移して draft。stubs 側は削除）。front matter で変えたキー：sections（forms・examples・prevention を足した。diagnosis の anchor は変えず）、stage（draft）、updated（2026-11-05）、sources（束の一覧の 7 件）
- snippets/does-more-than-asked/scope-audit.md と scope-audit.expect.yaml（作業ツリーの洗い出しの依頼。目次の templates の案はなし、診断 2 のために足した）
- data/sources.d は不要（使った出典はすべて data/sources.yml にある）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめられる順）：#diagnosis（見えていない → 確かめていない → 合っていない。prevents の並び）
- 人の側の落とし穴：持たない。pitfalls が空で、診断に関わる落とし穴がないため（「好みの方式を伝えていない」は 見えていない の項に含めた）
- 原因ごとの振り分け先（routes）：#diagnosis の末尾の `routes` の目印
- 構成の目安：要点 → #forms → #diagnosis → routes → #examples → #prevention

## メインに判断してほしいこと
- 古くなった助言の台帳は `outdated-advice-ledger#keep-going-dont-be-lazy` で指した。related にも prerequisites にも入っていないので、リンクの検査の結果を見てほしい
- 診断 2 の洗い出しは、研究（過剰な不適合判定）を理由に「判定・修正案を求めない」雛形にした。根拠は旧世代のモデルを含む研究で、（根拠：中・類推）と書いた

## 提案
- facts の提案なし（本文に変わりやすい値は書いていない。モデル名は公式文書の題名にだけ出る）
- 他の提案なし

## 検査の結果
- 1 回目：エラー 0・警告 9（算用数字 7、文の長さ 1、助詞の重なり 1）。直して 2 回目：エラー 0・警告 1（139 行目の助詞「に」の重なり）。そのあと該当の文を書き換えたが、検査は規定の 2 回なので再度は流していない

## 確かめていないこと
- 書き換えた最後の 1 文で警告が消えたか
- リンクの `outdated-advice-ledger#keep-going-dont-be-lazy` の anchor が実在するか（検査は通ったが、台帳の行の anchor の規則は束に書かれていない）
- 公式の Prompting Claude Opus 5 の「範囲を広げることがある」は 2026-11-05 に取得して確認した。Prompting best practices の Opus 4.5・4.6 の過剰設計の記述は束の写しのまま（再取得していない）
- アプリでの動き（未確認と本文に書いた）、Claude Code の `/simplify` は本文で扱っていない（出典の marmelab は使っていないが sources に残した）
- 雛形 scope-audit は動作を試していない

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 1 回（Prompting Claude Opus 5）
