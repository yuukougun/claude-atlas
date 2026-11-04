# lethal-trifecta 執筆の報告

## 書いたファイル
- `docs/safety/lethal-trifecta.md`（stub から mv。front matter は stage を draft、updated を 2026-11-05、sections に example・what-it-prevents・misconceptions を足し、sources に既存の 6 件を入れた。ほかのキーは変えていない）
- `docs/img/lethal-trifecta/trifecta.svg`（3 つの円が重なる図。円は実線・破線・点線で区別）
- 雛形なし（目次の templates が空）。`data/sources.d/lethal-trifecta.yml` は作っていない（使った出典は data/sources.yml に既にある）

## 必ず持つものの対応
- どの原理に関わるか（`principle`＝縛る）：`what-it-prevents`（「このページの考え方は、原理「縛る」に当たる」）
- どの原因に関わるか（`prevents`＝境界がない）：`what-it-prevents`（「防ぐ原因は、Claude 側の「境界がない」」）
- `pitfalls`：空のため名指す対象なし
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`example`（何が起きるか）／`three-capabilities`（なぜ・図）／`what-it-prevents`（何に効くか）／`misconceptions`（誤解）／関連はテンプレートが出す

## メインに判断してほしいこと
- 目次の備考「アプリの二条件との対応を by-surface に書く」は、条件 1＝A、条件 2＝C と置き、B を数えない点を「この辞典の読み方（推論・実践例なし）」と書いた。この読みでよいか
- 材料 5（research/22 #27：クラウドの予定のタスクに頼んでいないコネクタが付いたときの警告）は、入った版（v2.1.317）が要る事実で、fact の id がまだないため本文に書かなかった。facts への追加と、tasks-and-schedules-in-the-app 側での扱いを検討してほしい

## 提案
- 数値の提案なし。用語集・prh・front matter への提案なし

## 検査の結果
- `check_page.py lethal-trifecta` を 1 回：エラー 0・警告 12。警告は textlint の文体（no-doubled-joshi 9 件・sentence-length 1 件〔76 行〕・max-ten 1 件〔147 行〕・ja-no-redundant-expression 1 件〔70 行の「攻撃を行う」。論文の説明の言い回し〕）。直した後の再検査はしていない。分かりやすさの担当が直すか判断してほしい

## 確かめていないこと
- 「12 の防御で成功率 90% 超」の論文は、ニュースレターの二次の引用のままで、原典と対象のモデルは未確認（本文にそう書いた）
- Docker の記事の WhatsApp の事例は二次の紹介のまま。原典の Invariant Labs の記事は開いていない
- Web は取得していない。出典の内容は束の写しだけに基づく
- 図の見え方（描画）は確かめていない。Claude Code の節は WSL・Linux 基準で、他の OS と IDE 拡張は未確認と書いた
- API の節の設計の勧め（tool を A・B・C に分類する）は、Rule of Two の考えからの当てはめで、公式の手順ではない

## 使用量
- 道具の呼び出し 約 12 回（Read 4・Bash 5・Write 3）。Web の取得 0 回
