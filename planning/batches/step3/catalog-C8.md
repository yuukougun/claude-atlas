# 工程3 C8：verify（確かめる）・eval（評価と実験）の目次の報告

- 担当：C8（2026-11-04）
- 書いたもの：[planning/catalog/verify.yaml](../../catalog/verify.yaml)（17ページ）、[planning/catalog/eval.yaml](../../catalog/eval.yaml)（13ページ）
- 境界（D4・design §4.2）：完了・事実・レビューの確かめ方は verify、検証器を作って守る・実験を回す・評価の指標は eval。requirements §4.3 の eval の候補と、verify に足す4ページ（見た目は品質の証拠ではない・AI に書かせたテストの落とし穴・別のモデルに第二の意見を求める・良すぎる結果を疑う）を受け持った
- ほかの担当と並行して書いたので、途中でほかの分野のファイルを読み、こちらへの提案を取り込み、こちらの提案が取り込まれたかを確かめた（§4）

## 1. 分野ごとのページ数

| 分野 | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| verify | 17 | 必須 7・推奨 9・任意 1 | 使う 1・整える 3・任せる 11・仕組みにする 1・回す 1 | concept 12・feature 1・recipe 4 | 17（採る 17） |
| eval | 13 | 必須 7・推奨 5・任意 1 | 整える 1・任せる 6・仕組みにする 6 | concept 6・feature 1・recipe 5・judgment 1 | 13（採る 12・まとめた 1）＋新規 1 |

章（ナビゲーションの小見出し）：

- verify：完了を確かめる（define-done・evidence-not-reports・verification-ladder・visual-checks・checking-unattended-runs）／事実を確かめる（fact-checking・checking-citations）／テストで確かめる（tests-first・pitfalls-of-ai-written-tests・protect-tests）／レビューで確かめる（independent-review・instructing-reviewers・diffs-humans-must-read・own-generated-code・second-opinion-from-another-model）／結果を疑う（looks-are-not-quality・suspect-too-good-results）
- eval：総論（verifier-defines-problem）／変化を測る（felt-vs-measured・measure-changes・insights-and-usage-review）／検証器を作る（verifier-three-conditions・test-the-verifier・check-the-metric・differential-testing・model-based-grading）／実験を回す（selection-pressure・experiment-log・lockbox-and-holdout・measure-the-upper-bound）

前提の骨組み（必須のページの前提は必須、段の逆転なし）：

- verify：agent-loop → define-done → evidence-not-reports →（＋request-vs-lock）verification-ladder → protect-tests（＋reward-hacking）・independent-review（＋subagent-isolation）・checking-unattended-runs。why-hallucinations → fact-checking → checking-citations
- eval：verification-ladder → 総論 → verifier-three-conditions（＋reward-hacking）→ test-the-verifier・differential-testing・model-based-grading。human-pitfalls → felt-vs-measured → measure-changes（＋nondeterminism・define-done）→ selection-pressure → experiment-log・lockbox-and-holdout

### registry の見当から変えたもの（理由は各ページの notes）

| ページ | 変えた点 | 理由 |
| --- | --- | --- |
| protect-tests | 推奨→必須、仕組みにする→任せる | 逆引き「テストのほうを書き換えて通された」の受け皿で、必須の症状 rewrote-tests-to-pass（任せる）の対処の本体。requirements §1 の核「検証器を作って守る」。書き換えは反復を任せる段で起きる。止める設定は enforce の freeze-eval-assets が持つ（enforce と同じ分担） |
| felt-vs-measured | 推奨→必須、任せる→整える、concept→judgment | 人の側の落とし穴エのページ。judgment の総論とア・イ・ウ・オのページ（必須、主に整える）とそろえた |
| measure-changes | 推奨→必須、仕組みにする→任せる | 逆引き「CLAUDE.md を変えて良くなったか知りたい」の受け皿で、eval のほかのページの多くの前提。api の prompt-evals-intro の受け皿にもなった（§2） |
| selection-pressure | 推奨→必須 | 実験台帳（必須）とロックボックスの前提で、「実験を回す」の考え方の中心（10 第9章は台帳とロックボックスを選択圧への防ぎとして並べる）。delegate の open-ended-loop-trap と contest の running-contest-experiments も前提にしている |
| type | fact-checking・checking-citations・tests-first・checking-unattended-runs を concept→recipe | 手順が本体のため |
| 題名 | experiment-log の「評価器の版」→「検証器の版」 | eval の用語を「検証器」にそろえた（評価器は aliases と本文の言い換え） |

instructing-reviewers は 00 のとおり仕組みにするのまま（team の grow-review-checklists が前提にしている）。verifier-three-conditions は recipes・contest・symptoms の前提なので、任せるより上にしない（recipes・contest の依頼）。

## 2. merged・dropped と新しいページ

- **merged：stratified-and-worst-case → measure-changes（節 by-stratum、節の level は仕組みにする）**。11 が「小項目」とし、根拠は1行（p34#52）。結果を合計や平均で読まず層別と最悪ケースで見るのは測った結果の読み方なので節にした。必須のページに入るので第一波にも入る。ほかの分野の5ページが先にこの候補を指していたが、recipes（3）・contest（1）は measure-changes#by-stratum に、prompting・symptoms は measure-changes に直した（参照のエラーは今は0）
- **dropped**：なし
- **新規：model-based-grading「Claude に採点させる（人の判定で較正する）」**（eval・推奨・仕組みにする・recipe）。design §4.2 で eval が持つ「評価の指標」のうち、AI に採点させるときの較正が候補になかった。材料は公式（05 5-2 の grader の種類とモデルの採点の較正、11 第2節 p34#226・p34#166 の QA 役の較正、11 第3節 3-2 #7 の完了の判定役）。文章や日本語の品質のように機械で判定しにくい評価で要る
- **ほかの分野から受けたまとめ**：api が prompt-evals-intro（プロンプトの評価入門）を measure-changes にまとめた（こちらの提案と同じ）。依頼どおり、成功の基準を先に決めること（02 4-0）、task・trial・grader・transcript・outcome の語と pass@k・pass^k（節 terms・graders）、batch-api-basics への関連、旧い題名の別名を measure-changes に入れた
- **雛形の置き場所を他分野と分けた**：A-4（評価資産を守る設定）は enforce の freeze-eval-assets、A-9 後半（差分の点数の assert）は contest の search-code-checklist、A-16（理解を確かめる問い・上位解法の要約）は judgment の learning-with-ai。verify・eval にはそれぞれの考え方と依頼の文例を置き、リンクする

## 3. wave: 1 を付けたページ（eval だけ）

verifier-defines-problem（総論）・felt-vs-measured・measure-changes・verifier-three-conditions の4つ。総論と、eval のほかのページの多くが前提にするもの（直接と推移で数えて、総論 8・felt-vs-measured 7・measure-changes 5・verifier-three-conditions 4 ページが前提にする）に付けた。

- registry の wave_core の **test-the-verifier と experiment-log には付けていない**。どちらも eval のどのページの前提にもならない葉のレシピだから（必須なので初版には入る）。第一波に検証器の確かめ方と実験台帳まで出したいなら、この2つに wave: 1 を足す。前提はすでに第一波にあるので、増えるのはこの2ページだけ。判断はメインに残した（eval.yaml の open_issues）
- 全体の検査（2026-11-04、23ファイル・361ページ）で第一波に入る自分のページ：eval 6（wave の4つと、symptoms の misses-broken-evaluation の前提の check-the-metric、delegate の open-ended-loop-trap の前提の selection-pressure）、verify 5（define-done・evidence-not-reports・verification-ladder・fact-checking・checking-citations）。全体の第一波は122ページ

## 4. ほかの分野への提案と new_features

こちらの提案の多くは、ほかの担当がすでに取り込んだ（delegate・judgment・enforce・recipes・contest・team・symptoms・prompting の前提と関連。各ファイルの open_issues に「取り込まれた提案」として記録した）。残っている提案：

1. **safety**：vetting-extensions の related に looks-are-not-quality（見た目の整った拡張やリポジトリを信用しない）
2. **models**（任意）：suspected-degradation は felt-vs-measured を、after-switching-models は measure-changes を、related でなく前提にもできる（段と優先度が合う）
3. **メイン**：§3 の wave の判断（test-the-verifier と experiment-log）

受けた提案：basics（reward-hacking を必須にしたので protect-tests・verifier-three-conditions の前提に）、recipes（related の追加7件）、contest（A-9 後半を search-code-checklist へ）、judgment（own-generated-code は出荷の基準、学ぶ手順は learning-with-ai と書き分け）、enforce（protect-tests はなぜと見つけ方、止める設定は freeze-eval-assets）、api（prompt-evals-intro の中身を measure-changes へ）、prompting・japanese（measure-changes の例にプロンプトの変更と英語への回帰の測り方）、symptoms（research/22 #18・#24 の例は evidence-not-reports にある）。

new_features（verify.yaml の末尾）：

- `verify-skill`：/verify（アプリを起動して確かめる組み込みの skill）。visual-checks が指す
- `code-review`：/code-review（会話を見ていないサブエージェントによるレビュー）。independent-review・verification-ladder・instructing-reviewers が指す。delegate の管理された Code Review・/ultrareview とは別の項目にする案

## 5. 検査の結果

`python3 tools/check_catalog.py --field verify` と `--field eval`（2026-11-04、23ファイル・361ページを読んだ時点）：

- verify：エラー 0、警告 0
- eval：エラー 0、警告 0
- 手元の確認：summary はすべて120字以内・2文以内で、使わない語と数字を含まない。title と signs に数字を書いていない。前提は4つまで、related は20件まで。ほかの分野から verify・eval のページを前提に置いた箇所で、段の逆転と「必須の前提が必須でない」は0件
- 自分のまとめが原因の他分野の参照のエラー：今は0件（途中では stratified-and-worst-case を指す5件があったが、各担当が直した）

## 6. 確かめていないこと、迷った点

- 一次資料は開いていない（指示どおり）。研究の値は research/24・25 の確認を頼りにし、summary・signs・題名には研究の値と閾値を使っていない。根拠の弱い行と、Claude 以外のモデルの結果（偽の高速化の例・可視と非公開の差が極端な C コンパイラ・評価のループの比較・止まる権利の効果）は、各ページの notes に書いた
- summary の「検証器」「判定役」「フック」などの言い方は、公式の日本語版の訳語（research/27 §3.1）と工程4の用語集でそろえ直す必要がありうる
- verify のページの前提の付け方（「これを知らないと読めない」かどうか）は判断が入る。own-generated-code は judgment のページと前提にし合うと循環しうるので、前提を空にして related で結んだ
- second-opinion-from-another-model は他社のモデルを使う話で根拠は中から弱（小さな事例研究と逸話）。任意のまま残した
- looks-are-not-quality は own-generated-code との統合も考えられる（11 の案）が、requirements §4.3 が独立に足すので残した
- stratified-and-worst-case はほかの分野の5ページが先に指していた。まとめたままにしたのは、各担当がすでに節を指すように直したから。独立のページに戻す案も成り立つ（その場合も measure-changes の節 by-stratum は残す）
- ほかの分野のファイルは並行して書き換わっている。この報告の数（第一波・参照）は 2026-11-04 の最後に検査した時点のもの
