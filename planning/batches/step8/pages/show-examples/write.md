# write.md：show-examples（concept・prompting）

## 書いたファイル
- docs/prompting/show-examples.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 3 つに、sections を 7 節に）
- front matter で変えたキー：`sections`（before-after・why・limits を足した。既存の 4 つの anchor は変えず）・`stage`・`updated`・`sources`（いずれも data/sources.yml に既にある id：api-docs-prompting-best-practices・arxiv-2403-08937・jinrai-claude-japanese）
- snippets/show-examples/：release-notes・own-writing・review-examples（各 .txt と .expect.yaml）
- data/sources.d/show-examples.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`「見せる」・`prevents`「見えていない」を本文で名指す）：#why（冒頭で両方を名指し）
- level を持つ（整える）・要点の最初が「何が分かるか」：front matter と冒頭の囲み
- 技法の構成（Before/After → 何が変わるか → なぜ効くか → 効かない場面・やりすぎ）：#before-after（Before/After と変わること）→ #why → #choose・#how-many・#own-writing → #overfit・#limits
- `pitfalls`：front matter に無いので名指しは無し

## メインに判断してほしいこと
- 「何個見せるか」の公式の個数（3〜5 個。確認日 2026-10-29、research/02 §4-3）を、数値ファイルに無いので本文に書かず、#how-many は数字なしで書いた。提案の fact を data に入れた後、目印を #how-many に置くか判断してほしい
- 節を 3 つ足した（#before-after・#why・#limits）。技法の型の構成に合わせたため。不要なら統合してよい
- #own-writing のアプリのタブに、Projects の資料に置く方法を「面ごとの置き方は未確認」と付けて書いた。未確認のままで残すか、削るか

## 提案
```yaml
proposals:
  - fact: {id: few-shot-recommended-count, title: 公式が勧める例の個数（few-shot）, value: "3〜5 個", sources: [api-docs-prompting-best-practices], checked: 2026-10-29, status: 公式の推奨}
    used_in: [show-examples#how-many]
```
- 上の fact は束の research/02 §4-3 の写し（確認日 2026-10-29）による。一次資料の再確認はしていない

## 検査の結果
- 1 回目：エラー 0・警告 5（max-ten 1・no-doubled-joshi 4）。文を直した
- 2 回目：エラー 0・警告 1（#own-writing の文の no-doubled-joshi。リンクの題名の「一緒に」と「にある」の重複）。文末を「が扱う」に直したが、直した後の再検査は回数の決まりで流していない

## 確かめていないこと
- 雛形 3 つの動作（Claude に実際に流していない。expect は予想の観察）
- Tambon らの研究（arxiv-2403-08937）の類型名「プロンプトの例にしか合わないコード」と、対象のモデルの世代。束の写し（research/11）による。本文は「研究時点のモデルの結果」と書き、世代名は書いていない
- 仁頼の報告（jinrai-claude-japanese）は束の写し（research/04 Q3）による。原文は開いていない
- 「珍しい入力ばかりだと標準の形と受け取られやすい」は推論（本文に印あり）
- アプリでの手本のファイル添付・Projects・Claude Code でのパス指定・API の system に置く説明は、一般的な使い方としての記述で、面ごとの動作を確かめていない
- 最後の直しの再検査（上記）

## 使用量
- 道具の呼び出し：約 14 回（Read 3・Bash 7・Write 2〜3・check_page 2）。Web の取得：0
