# 工程4 V3：V2 の指摘へのメインの直しを確かめた報告

- 担当：V3（[README.md](README.md) の3段目。共通の指示は [brief-verify.md](brief-verify.md)）
- 日付：2026-11-04
- 書いたファイル：この報告だけ。ほかのファイルは読むだけにした。git の操作と Web は使っていない。`../kyopro-atlas` は読んでいない
- 道具は `python3 -B` で流した（リポジトリに __pycache__ を書かないため。tools/・tests/tools/ の __pycache__ の日時は 04:07 のまま）

## 1. 見た範囲と方法

**読んだもの**：brief-verify.md、verify-V2.md（全部）、fix-aliases.md（全部）、design-review.md の DR-13・DR-19 の表・§3・§6、design.md の §2.3・§3（表と front matter の例）・§5・§6.10・§8.4〜§8.6・§10.1・§10.7・§12・変更履歴、catalog/README.md（全部）。目次は、V2 の指摘と §4 が名指ししたページと、メインの注記（「2026-11-04 メイン」）のあるページの値と notes を、道具の読む層で読んだ

**方法**

- 一時の道具（scratchpad。リポジトリの外）から check_catalog.py の読む層（load_catalog・first_wave・target_priority）を呼び、第一波の優先度ごとの数、推奨のページの一覧、必須の数を数えた
- 直しの前との比べ：V2 が scratchpad に残した症状のページの書き出し（04:51。メインの直しの 05:17〜05:19 より前。優先度・level・level_evidence・summary・前提・routes・related・signs・aliases）と、今の値を同じ道具で書き出して diff を取った。第一波の数の差（136→135）は、diff で変わった値をメモリの上で V2 の時点に戻して数え直し、どのページが外れたかを確かめた。別名は、scratchpad の 03:31 の写しとも比べた
- 表：design.md・design-review.md・fix-aliases.md・catalog/README.md のすべての表で、行ごとのセルの数を数えた（表の行のコードの中に `|` がないことも確かめた）
- 別名：小文字にして空白を除き、2ページ以上にある語・ほかのページの title と nav_title と同じ語・自分の title と nav_title と同じ語・同じページの中の重複を数えた。括弧と記号も除いた比べ方でも流した。fix-aliases.md の49行を1行ずつ照らした
- 症状のページ34で、routes の先と前提・related の重なり、related の並びを数えた。notes に書かれた優先度・level と今の値の食い違いを引いた

### 1.1 道具の結果

- `python3 -B tools/check_catalog.py --stats`：**エラー0件、警告3件**（比例則：agents-md・feature-to-api-mapping・prompt-caching-in-practice。V2 と同じ）。357ページ（必須177・推奨144・任意36）。症状のページは必須19・推奨15、level は使う10・整える16・任せる7・回す1
- 第一波（first）：**135ページ**（wave: 1 が62、前提で届くもの24、routes から49、named から0）。必須119・推奨16（推奨の症状のページ15と、その前提の summary-overgeneralization）。none は88、all は206。必須の先がない cause は0
- 推奨を上げると必須は 177 + 16 = **193**
- 使用量（1ページ35〜45万トークン）：135ページで4,725万〜6,075万、193ページで6,755万〜8,685万、357ページで1億2,495万〜1億6,065万
- `python3 -B -m unittest discover -s tests/tools`：168件、すべて通った

design §12 の1・19 の数（135・62・24・49・119・16〔15と1〕・177→193・88・206、約4,700万〜6,100万・約6,800万〜8,700万・約1.2億〜1.6億）は、道具の数と合っている。

## 2. 指摘の一覧

| 番号 | 重さ | 場所 | 問題 | 根拠 | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | symptoms.yaml の doesnt-know-latest（routes 311行・related 313行・notes 320行） | V2 の指摘9 の直しで、見えていないの先頭に choose-what-to-read を置いた（案は2番目）。そのため、それまで最初の必須の先だった app の search-research-thinking（web 検索・リサーチ・拡張思考の使い分け。必須）が第一波から外れた（第一波の 136→135、routes からの 50→49 の差は、このページだけ）。第一波では、この原因の先で公開されるのは choose-what-to-read（@参照と、何を読ませるかの絞り込み）だけになる。summary の順（検索・公式の資料・日付の確かめ方）の最初の検索と、1つ目の sign（最近の出来事）への先が「準備中」になる。notes も直す前のまま（routes は「web 検索とリサーチ・Claude Code 自身に…」、「related の choose-what-to-read から案内する」。今の related に choose-what-to-read はない） | DR-02（原因ごとに中心の対処を近い順に）、design-review §6 の1（第一波は各原因の最初の必須の先）、V2 の指摘9 の案、305行の summary | V2 の案どおり search-research-thinking を先頭、choose-what-to-read を2番目にする（choose-what-to-read は uses-nonexistent-apis から第一波に入っているので、両方が第一波に入る。数え直すと第一波136・routes から50・必須120・推奨16、使用量は約4,800万〜6,100万になるので、§12 の1・19 と §10.7 も合わせる）。先頭のままにするなら、notes の routes の文と related の記述を直し、web 検索のページが第一波に入らないことを notes に書く |
| 2 | 直したほうがよい | design §10.7（730行） | 使用量の概算が直す前の数のまま（「第一波（125ページの場合）で約4,400万〜5,600万、必須で約6,100万〜7,800万、全部で約1.3億〜1.6億」）。§12 の19 は今の数（135ページ・193ページ・357ページ）にしたので、どちらも「工程5で示す」概算が、設計書の中で2通りになった | DR-13（反映先は design §10.7 と §12）、V2 の指摘14、§12 の19 | §10.7 を §12 の19 の値にする（193は推奨を上げた後の必須の数だと添える）。§10.7 から §12 の19 を指す形でもよい |
| 3 | 直したほうがよい | verify.yaml の independent-review の notes（388行） | V2 の指摘11(b) の直しで、別名 /security-review を delegate の automated-pr-review から外して、このページ（358行）に移した。ところが notes は「/security-review の別名は delegate の automated-pr-review にだけ置き、ここには重ねない」のままで、今の別名と逆のことを言う（V2 の指摘3 と同じ型）。移したことは、notes にも fix-aliases.md にも書かれていない | V2 の指摘11(b)・指摘3、features.yaml の security-review（by: verify） | 「別名 /security-review は、機能 security-review の節を持つこのページを主にし、automated-pr-review から外した（2026-11-04 メイン。V2 の指摘11）」に書き換える |
| 4 | 軽い | extend.yaml の claude-md-vs-rules-skills-styles の別名（248行） | V2 の指摘11(c) のうち、別名「指示の置き場所」が app の where-to-put-instructions の nav_title（13行）と同じ件が残っている（hooks と Hooks の重なりは直った）。なお、cli の output-style-modes の別名「出力スタイル」は自分の nav_title（420・421行）と同じ（工程4の前からある）。§5.3 と catalog/README §4.5 の2 の規則は「題名」のことしか書いていない | V2 の指摘11(c)、design §5.3、catalog/README §4.5 の2 | どちらか一方を外す。nav_title も「題名」に含めるかを §5.3 に書けば、output-style-modes の扱いも決まる |
| 5 | 軽い | catalog/README の版の行（7行） | V2 の指摘6 の後半（版の行に V1 の指摘による直しを足す）が反映されていない。冒頭（5行）は直っているが、その直しも版の行に書かれていない | V2 の指摘6 | 版の行に、工程4の確かめ（V1・V2）を受けて §3 の例・§4.2 の2・§4.3 の4・§4.5 の2〜4・§5・冒頭を直したことを足す |
| 6 | 軽い | symptoms.yaml の misses-broken-evaluation（related 783行・notes 790行） | V2 の指摘2 の直しで selection-pressure と open-ended-loop-trap を related に足したが、末尾（six-causes の後）に置いた。ほかの症状のページ33はどれも six-causes を最後に置いている。related は近い順に書く規則なので、この2ページがいちばん遠いと読める。notes に「選び続けた・長く回した」の枝も書かれていない（たどる道がないという問題は解けた） | V2 の指摘2、catalog/README §4.4 の5（related は近いものから順に） | 2つを six-causes より前（案では先頭）に移し、notes に枝を1文足す |
| 7 | 軽い | notes：symptoms の too-slow（1130行）・secrets-exposed（998行）、judgment の how-much-understanding-to-keep（324行）、basics の how-thinking-works（266行） | 直した後も古い文が残っている。too-slow は、散らかっているの routes の順を「常駐するもののコスト・拡張の剪定・新しい会話」と書く（今は新しい会話が先頭）。secrets-exposed は「優先度は推奨。」が残り、末尾の「（メイン：必須に上げた…）」と食い違う（V2 の指摘8 の choosing-an-org-plan は、前の文を消して直した）。how-much-understanding-to-keep の「このページを用語索引の主にした（…11 の材料も「理解が追いつかないままコードが増える」を生成コードを自分のものにする話に置く。fix-aliases）」は、括弧の中の理由が own-generated-code を主にする理由のままで、文の筋が逆になっている。how-thinking-works には「同じ語の日本語と英語で主が分かれる点は…メインへ」が残っているが、拡張思考もこのページに移ったので、今は分かれていない | V2 の指摘3・8・9、fix-aliases.md の表（認知負債・拡張思考） | too-slow の順を今の順にする。secrets-exposed の「優先度は推奨。」は消すか、今の優先度に合わせる。how-much-understanding-to-keep の括弧の後半と、how-thinking-works の括弧を消す |
| 8 | 軽い | design §3.3 の front matter の例（154〜189行） | wave をキーの台帳に移し、骨格で写すキーにした。ところが、例の症状のページ instructions-ignored（目次では wave: 1。symptoms.yaml 562行）に wave がない。catalog/README §3 の例には wave がある | V2 の指摘1、design §3.3 の wave の行、§5.3（症状辞典は全ページ） | 例に `wave: 1` を足す |
| 9 | 軽い | design-review §6 の見出し（228行） | 見出しが「担当 D1 の報告のメインへ12件」のままだが、表は17行ある（13は T3、14〜17は V2 の報告から） | design-review §6 の13〜17 | 見出しを、D1 の12件と T3・V2 の報告から決めたことだと分かる形にする |

件数：直す0・直したほうがよい3・軽い6（計9）。

## 3. 決定どおりと確かめたもの

- **V2 の指摘1**：§3.2 の分類の軸の表は4列14行で、前提と関連の行が元に戻った。§3.3 のキーの台帳（5列22行）に wave の行がある（案どおりの文）。§5.1 の「§3.3」の参照先もある。design.md の18の表は、どれも行ごとの列の数がそろっている
- **指摘3**：keep-replies-in-japanese・own-generated-code・when-requests-are-refused・permission-modes-overview の notes は今の別名と合う。how-thinking-works・how-much-understanding-to-keep も、主を書いた文は合っている（残った括弧は指摘7）
- **指摘4・5**：§5.3 に「自分の題名とも」、§8.5 のページ下部に「未公開のページ（§8.4）」が入った
- **指摘6**：catalog/README の冒頭に、notes の見せ方と、wave・routes を写すことが入った（版の行は指摘5）
- **指摘7**：7ページの notes が routes の言い方になった。書かれた振り分け（repeating-the-same-explanation → where-to-put-instructions など7組）は、どれも今の routes にある。verification-ladder の古い1文は書き換わった
- **指摘8**：choosing-an-org-plan の notes から「id は変えない」が消え、改名の向きが正しくなった。DR-19 n に4つ目の改名が足された
- **指摘9**：too-slow は when-to-start-fresh が先頭になった（notes は指摘7）。doesnt-know-latest は指摘1
- **指摘10**：parallel-fatigue は level が回す、level_evidence は出会う段階（design §3.1 の表）で書き直された。前提の逆転の警告はない
- **指摘11**：(a) 例外の2語は fix-aliases.md の表に扱いが書かれた。(b) how-thinking-works の別名 effort が外れ、/security-review は independent-review に移った（notes は指摘3）。(c) hooks-basics の Hooks が外れた。小文字にして空白を除いて比べると、2ページ以上にある別名は例外の2語だけで、ほかのページの題名と同じ別名と、同じページの中の重複は0。fix-aliases.md の49行は、45行が表どおり、承認疲れ（主のページの題名がその語）と自動化バイアス（外す側はまとめたページ）も合っていて、残る2語が例外
- **指摘12**：data-vs-instructions の situation が、束ねた文「Web ページやメールを読ませるのが不安」と同じになった（3ページで同じ文）
- **指摘13・§6 の17**：目次の検査は警告のまま（catalog/README §6 の表も警告）。キーの台帳では routes が symptom で必須なので、骨格の後の front matter の検査で誤りにする形と合う
- **指摘14**：§12 の1・19 は道具の数と合う（§1.1）。kyopro-atlas との書き方の食い違いは §12 の23 に入った（design-review §3 の「知らせるだけのもの」と同じ中身）。§10.7 は指摘2
- **§4 の1・§6 の14**：design §6.10 と §10.1 の7 が、試作の始めにメインが planning/shows.md に作る一覧を指し、目次の notes はその材料だとしている。§5.2 の5・catalog/README の冒頭とも食い違わない
- **§4 の2・§6 の15**：secrets-exposed は必須になった（前提の where-your-data-goes も必須。notes にメインの理由がある）。ほかのファイルに secrets-exposed を推奨と書いた箇所はない（notes の残りの1文は指摘7）
- **§4 の3・§6 の16**：old-advice-doesnt-work の「確かめていない」の3番目に outdated-advice-ledger#find-in-your-setup（必須・核。節がある）があり、第一波では、推奨の dating-information・checking-for-updates に代わってこの枝を受ける
- **重なり**：症状のページ34で、routes の先と前提・related の重なりは0。related が20件を超えるページはない

## 4. 決定の中の食い違い

なし。

## 5. 確かめていないこと

- 直す前との diff は、V2 が残した症状のページの書き出しにある値だけで取った（notes・題名・節などは入っていない）。ほかの分野のファイルには直す前の写しがないので、V2 の指摘に引かれた文と、メインの注記があるページの notes を読んで確かめた。357ページの notes は全部は読んでいない
- doesnt-know-latest で choose-what-to-read を先頭にしたのが、意図したことかどうかは分からない（記録がない）
- parallel-fatigue の段を回すにしたことの良し悪しは見ていない（level_evidence の書き方と逆転がないことだけを見た）
- 表は列の数だけを数えた。描画は試していない
- progress.md は、確かめている間（05:20）に更新された。受け持ちの外なので、26行（数は道具と合う）のほかは読んでいない
