## choosing-a-surface/write.md
[メインに判断してほしいこと]
- 比較の表：数値ファイルに claude-code と api の機能が tracks にないため、`compare` の表は app-tasks の 1 行になった。3 面を並べる軸の表（誰が手を動かすか・何に触れるか・どこで動くか）は、変わりやすい値を含まない構造の説明として手書きした。「data から作る表を手で書かない」との兼ね合いを見てほしい（下の提案）
- 二次情報（日本語の実務記事）の「Cowork から始め、繰り返す作業になったら Code へ」と、非エンジニアが Desktop の Code タブで使う案内は、根拠：弱で書いた。書き方が強すぎないか見てほしい
- 「統合の後に残る制約」（Incognito・Add from GitHub・分岐）は 2026-10-29 の確認日を本文に付けた。変わりやすい値の扱いが要るなら、facts への提案にしてほしい
[提案]
```yaml
frontmatter:
  - {id: choosing-a-surface, key: sections, before: "5 節", after: "6 節（組み合わせ方 {#combine} を末尾に追加）", reason: "構成の目安の「組み合わせ方」を節にした。既にある anchor は変えていない"}
proposals:
  - fact: {id: surface-attributes, title: "面（アプリ・Claude Code・API）の属性（誰が手を動かすか・何に触れるか・どこで動くか）", value: "3 面を機能として features に足し、tracks に入れる", sources: [hc-cowork-and-chat, cc-docs-claude-code-on-the-web, cc-docs-agent-sdk-overview], checked: 2026-11-05, status: 提案}
    used_in: [choosing-a-surface#compare-surfaces]
```
- catalog：`choosing-a-surface` の tracks に claude-code・api 側の機能の id を足すと、`compare` の表が 3 面を並べられる（open_issues の提案の続き）

## choosing-a-surface/review.md
[メインに判断してほしいこと]
- 手書きの 3 軸の表を残すか（write.md の提案どおり、catalog の tracks に claude-code・api の機能を足せば compare で置き換えられる）。

## where-it-runs/write.md
[メインに判断してほしいこと]
- 目次の図の案（実行場所と届くものの対応図）は、図でなく `#three-locations` の表にした。SVG の図が要るなら別途指示がほしい
- 「2026-10-06 から Pro・Max・Ultra の新しいタスクはクラウドで動く」は日付とプランの名前なので本文に書かず、`tasks-and-schedules-in-the-app#where-it-runs` を指した。data の app-tasks の note にあるので、必要なら主のページ側で扱う
- 競技の材料（11 第1節 p12#47、根拠が中〜弱で時点依存）は使わなかった
[提案]
- 用語集：プラグイン（plugin の訳）は prh が `plugin` を弾いたので本文を「プラグイン」にした。問題はない
- front matter の変更の提案はなし

## where-it-runs/review.md
[メインに判断してほしいこと]
- 比喩付きの図（目次の図の案）が無い。表で足りると見たが、SVG が要るなら別途指示を
- 事実の確かめはしていない（write.md の「確かめていないこと」のとおり）

## current-models/write.md
[メインに判断してほしいこと]
1. データに現行モデルの一覧表（型番・API ID・料金・窓）がなく、tracks の機能が model-selection の 1 つだけで `compare` の目印が表にならない。そこで #lineup は、型番・料金の数値を使わない定性の表にした（系統名だけ、世代は書かない）。facts-proposal.yml の current-models-lineup を facts に足したら、#lineup の表の後に `fact-table current-models-lineup` を置いてほしい
2. #fable-and-mythos は、提供範囲を本文に書かず「公式の発表で確かめる」にした。mythos-availability を足したら fact の目印で置ける。透かしは catalog の notes に従い、2 つの違いとして書かず、日付も本文に書かなかった
3. 自動の切り替え（分類器が止めた依頼を別のモデルで答え直す）は、仕組みの説明 1 段落だけにした。safety の持ち主のページ（when-requests-are-refused）を link で指していない（束の「指せる節」にないため）。足してよければ指したい
4. 「確認日 2026-10-29」を #lineup の表の下に手書きした（束の 3-1 の確認日）。目印の外の日付で、fact-table を足したら表の下の出典の行に置き換えてよい
[提案]
- 数値の提案：facts-proposal.yml（current-models-lineup・haiku-4-5-removed-from-app-selector・sonnet-4-5-retirement・mythos-availability）
- front matter の提案はなし

## current-models/review.md
[メインに判断してほしいこと]
- 警告 1 件（上記）。link の題名が入る文なので、前後の文を短く割る直しが要るなら次の回で。
- write.md の判断 1〜4（fact-table の追加・mythos-availability・自動切り替えの link・確認日）を引き続き判断してほしい。

## choosing-a-model/write.md
[メインに判断してほしいこと]
- 原因「合っていない」の定義を、束にある情報だけから「選んだモデルや effort が作業の重さに合っていない」と書いた。site.yml の定義と合うか確認してほしい
- 具体的なモデル名・料金・既定値は、names/facts の id が束になかったので本文に書かず、current-models と effort-levels の節を指した。数値の目印は 0 個
[提案]
- なし（数値・用語集・front matter の提案なし）

## choosing-a-model/review.md
[メインに判断してほしいこと]
- 原因「合っていない」の定義が site.yml と合うかの確認（write.md と同じ）
- 要点に「確かめ方」の項目を足してある（カードの例にない項目）。問題なければそのまま

## thinking-keywords/write.md
[メインに判断してほしいこと]
- ultrathink の機能の項目の `enforcement` が null で、冒頭の強制力が「—」と出る。「お願い」にする提案（下）を反映するか判断してほしい。
[提案]
- data/facts.yml の features の ultrathink に `enforcement: お願い`（プロンプトに指示を足す働きで、何も止めない）を足す
- 版・引き上げる先・対象モデルの数値は facts-proposal.yml。本文は数字なしで読めるようにしてあり、fact の目印は置いていない（反映後に #ultrathink へ置く）
- 台帳の行 think-hard-keywords への link は `outdated-advice-ledger#think-hard-keywords`。台帳の sections にこの anchor があるかは、check_page では通ったが、持つ anchor の一覧では確かめていない

## thinking-keywords/review.md
[メインに判断してほしいこと]
- ultrathink の enforcement を「お願い」にする提案（write.md）を反映するか。反映後は要点の「—」が消える。
- find-old-keywords の雛形に「要る最低の版：Claude Code 0.2.44」が出るが grep には不要。features を外す案。

## after-switching-models/write.md
[メインに判断してほしいこと]
- 退役の日付・既定の値・API の版は変わりやすいので本文に書かず、台帳・年表・公式の文書への link に任せた。提案の fact を数値ファイルに入れたら、`#retirements-and-default-changes`・`#api-parameters` に目印で足せる
- `#api-parameters` の表は、台帳の行の説明を繰り返さず、エラーの出方 → 引数 → 台帳の行の引き方にした。モデルの名前（Opus 5 など）は、変わりやすいので本文に出さず、台帳の add-double-check に任せた。読者に不親切なら、names か fact の目印で足す案を出してほしい
- front matter の提案はなし
[提案]
- 数値の提案：`facts-proposal.yml`（4 件。`/doctor prompt-audit` の最低の版は今日 Commands の文書で確かめた。ほかは束の調査資料の値で、確認日は 2026-11-04 のまま）
- 用語集・prh への提案：なし

## after-switching-models/review.md
[メインに判断してほしいこと]
- 指摘 7：モデル名を names の目印で足すか

## show-examples/write.md
[メインに判断してほしいこと]
- 「何個見せるか」の公式の個数（3〜5 個。確認日 2026-10-29、research/02 §4-3）を、数値ファイルに無いので本文に書かず、#how-many は数字なしで書いた。提案の fact を data に入れた後、目印を #how-many に置くか判断してほしい
- 節を 3 つ足した（#before-after・#why・#limits）。技法の型の構成に合わせたため。不要なら統合してよい
- #own-writing のアプリのタブに、Projects の資料に置く方法を「面ごとの置き方は未確認」と付けて書いた。未確認のままで残すか、削るか
[提案]
```yaml
proposals:
  - fact: {id: few-shot-recommended-count, title: 公式が勧める例の個数（few-shot）, value: "3〜5 個", sources: [api-docs-prompting-best-practices], checked: 2026-10-29, status: 公式の推奨}
    used_in: [show-examples#how-many]
```
- 上の fact は束の research/02 §4-3 の写し（確認日 2026-10-29）による。一次資料の再確認はしていない

## show-examples/review.md
[メインに判断してほしいこと]
- few-shot-recommended-count の提案（write.md）を data に入れた後、#how-many に fact の目印を置くか。置くまで個数は本文に無い
- #own-writing のアプリのタブの「面ごとの置き方は未確認」は残した

## say-what-you-want/write.md
[メインに判断してほしいこと]
- 本文の「禁じた語が文脈に載る」は公式の説明ではなく、推論と明記した。残すか削るか
- two-layers の「フックが止めるときに返す文は Claude に届く」は、Claude Code のフックの仕様（exit 2 の stderr）に基づく。束にはない記憶による記述なので、確かめてほしい
- 「開発の例」の `docker compose` と test 用データベースは、例として置いた架空の設定
[提案]
- front matter の提案：なし
- 用語集・prh への提案：なし

## say-what-you-want/review.md
[メインに判断してほしいこと]
- write.md が挙げた、フックの返す文が Claude に届くという記述の確認は、事実の検証の担当に残る（ここでは見ていない）

## emphasis-words/write.md
[メインに判断してほしいこと]
- 台帳の行を指す link に `outdated-advice-ledger#keep-going-dont-be-lazy` と `#important-caps` を使った（カード §11 の指示）。束の「指せる節」にはない行 id なので、検査は通ったが、公開側の解決を確かめてほしい
- モデル名は本文に書かなかった（「システムプロンプトに強く反応するモデルがある」と書き、model-quirks へ送った）。名前を出すなら names か facts への追加が要る
[提案]
- 用語集：「強調語」を本文で短く定義した（IMPORTANT・YOU MUST・全部が大文字・「絶対に」「必ず」）。用語集に追加するか、判断を
- 数値の提案はなし

## emphasis-words/review.md
[メインに判断してほしいこと]
- write.md の2点（台帳の行 id へのリンク、用語集への「強調語」の追加）に同意。#stances の4の印の扱いも判断を

## images-and-voice/write.md
[メインに判断してほしいこと]
- 判断例を 1 つ置いた（エラーは画像か文字か）。画像の貼り付けは Claude Code の公式（common-workflows）で確かめた手順だけ。アプリ側の画像添付の手順は束と取得で確かめられず、how-attachments-are-read へ回した
- 音声の既定のキー・録音の上限時間・版・成熟度の数値は本文に書かず、成熟度は `compare 面 成熟度` の目印で出した
[提案]
```yaml
frontmatter:
  - {id: images-and-voice, key: related, before: [visual-checks, how-attachments-are-read, voice-and-mobile, input-symbols, let-claude-ask], after: [visual-checks, how-attachments-are-read, voice-and-mobile, input-symbols, let-claude-ask, keep-replies-in-japanese], reason: "音声入力の言語は language の設定が決める。束の備考どおり、japanese の keep-replies-in-japanese の language-setting の節を指したい（束に指せる節がなく、本文では指せていない）"}
```
- 用語集：追加の提案なし

## images-and-voice/review.md
[メインに判断してほしいこと]
- 4番：Windows・WSL の貼り付けのキーを、数値ではない事実として公式から確かめて足すか
- write.md の提案（related に keep-replies-in-japanese を足す）は、指せる節が束にないため本文では未対応のまま

## let-claude-ask/write.md
[メインに判断してほしいこと]
- A-6 の雛形は `snippets/let-claude-ask/` に置いた。目次の notes は「spec-first と取り込みで共有する」と書くので、spec-first のページの担当が同じものを別に置くと重複する。共有の置き場所を決めてほしい
- A-6 の元の文はツール名 AskUserQuestion を出すが、notes と research/26 #17 に従い「インタビューして」の形に直した
- 数値（1 回の問数と選択肢の数、timeout の値）は本文に書かず、下の提案にした。数値ファイルに入った後、`how`・`limits` の「上限がある」の所へ目印を置きたい
[提案]
- 数値の提案：facts-proposal.yml（ask-user-question-limits・ask-user-question-timeout）。Agent SDK の文書（Handle approvals and user input）は sources に id がなく、research/26 §3.9 の写しに基づく
- 用語集：「インタビューして仕様を作る」の用語は追加不要と見た

## let-claude-ask/review.md
[メインに判断してほしいこと]
- write.md の指摘どおり、A-6 の雛形が spec-first と重複しないか、共有の置き場所を決めてほしい

## before-after-prompts/write.md
[メインに判断してほしいこと]
- 本文の例（バグ修正・要約・外れ値・リファクタ・移行調査など）はこのページ用に作った例で、動作は未確認。出典は公式 Best practices の「Instead of / Try」の考え方だけ
- 「アプリで Claude が自分でコードを実行できるか」は書かず、「確かめていない」と書いた
- 目次の備考にある「30 例程度は目安」に従い、例は 9 組にとどめた
[提案]
- なし（用語集・prh・data・front matter の直しの提案はない）

## tidy-the-desk/write.md
[メインに判断してほしいこと]
- 「任せる」のアプリでの手段は、束に材料がなく確かめていない。「別のチャットで調べて結論だけ持ち帰る手作業」を（推論・実践例なし）の印付きで 1 文だけ書いた。不要なら削る
- 節の題 `{#four-actions}` の「四つの動作」は、既存の title を変えなかった（カード §4 の「四つ」の警告は出なかった）
[提案]
- 用語集・prh・data・front matter への提案なし
- 数値の提案なし（本文に数値・既定値・版を書いていない。idle compaction の条件は compact-and-auto-compact#idle-compaction へ送った）

## tidy-the-desk/review.md
[メインに判断してほしいこと]
- 指摘 4・5（アプリの「任せる」の推論の 1 文、「アプリにない」の断定）

## compact-and-auto-compact/write.md
[メインに判断してほしいこと]
- 機能 compaction に `enforcement` がない。`なし` かそれ以外にするか決めてほしい（本文は手書き。データが入れば feature の目印に差し替える）
- 「入った版」は feature の属性でなく、`<!-- gen:begin feature 入った版 -->` が使えなかった（警告）。入った版のバッジはテンプレートに任せ、本文からは外した
- アプリに手で圧縮する操作があるかは確かめていない。本文は「未確認」と書いた
[提案]
- 数値の提案：facts-proposal.yml（idle compaction の大きさ・放置の時間・端末の版・IDE の版、autoCompactWindow の範囲）。本文は数字なしで読める形にし、used_in の節に目印を置く場所を残した
- front matter の提案：なし

## compact-and-auto-compact/review.md
[メインに判断してほしいこと]
- 強制力を手書きにしている件（write.md と同じ）。facts に enforcement が入ったら feature の目印へ
- 助詞の警告 4 件は残した

## handing-long-documents/write.md
[メインに判断してほしいこと]
- 比喩の図は置いていない（attention-budget に持ち主の図がある前提で、link で指した）。足すかは判断を仰ぐ
- Claude Code と API 側の PDF の読み込みの上限は、束にも data にもないので本文で数えず「未確認」「該当ページへ」とした
[提案]
- 数値の提案なし（アプリの PDF の上限は既存の facts の app-pdf-visual-pages・app-pdf-text-only-pages を fact の目印で指した）
- 参考：at-reference-read-limit は status 未確認のため本文で使っていない

## handing-long-documents/review.md
[メインに判断してほしいこと]
- 図なしのままでよいか（write.md と同じ）

## research-in-subagents/write.md
[メインに判断してほしいこと]
- `sections` に 2 節を足した。不要なら外すが、`#effects` は concept の必須（原理・原因の名指し）を置く節
- `#cost` で、公式の頼み方の手引きの題名（Prompting Claude Opus 5）にモデル名が入る。本文でモデル名を目印なしに書くのは避けたので、題名のリンクとして 1 回だけ出した
- `outdated-advice-ledger#<行の id>` の link が未公開の相手を指す場合の表示は道具に任せた（検査は通った）
[提案]
- 数値の提案なし（本文に数値・既定値を書いていない。環境変数の名前だけを書いた：data の台帳 tell-it-to-use-subagents の now と同じ）
- 用語集・prh・front matter への提案なし

## using-projects/write.md
[メインに判断してほしいこと]
- 「1 プロジェクト 1 目的」は企業の解説記事 1 件（根拠：弱）としか確かめられていない。本文は公式の規則ではないと明記した
- Free で project instructions が使えるかの食い違いは、pitfalls に書いた（プラン中立・数値なし・確認日 2026-11-03 の表現）。packet の features には「5 件まで」があるが、数値なので本文に書かず、目印もない
[提案]
```yaml
proposals:
  - fact: {id: projects-free-limit, title: Free で作れるプロジェクトの数, value: 5, sources: [hc-projects-manage], checked: 2026-11-04, status: 確認済み}
    used_in: [using-projects#pitfalls]
```
（本文は数字なしで読める。置くかどうかは任せる）

## using-projects/review.md
[メインに判断してほしいこと]
- 提案 projects-free-limit（write.md）は、本文が数字なしで読めるので急がない
- 2 の裏付けの確認を事実検証の担当へ

## files-and-code-execution/write.md
[メインに判断してほしいこと]
- ネットワークの既定・30MB の上限・共有の制限は、数値ファイルに置き場がない。本文は値なしで書いた（「参考に挙げた公式の文書で確かめる」）。facts-proposal.yml の 3 件を data へ入れれば `fact-table` で出せる
- 2 機能の enforcement が null。ネットワークの設定を「鍵」と見るか、機能ごとに何を入れるかを決めてほしい
- 本文で「依頼の文はお願いで、設定が鍵」と書いた。この言い方でよいか
[提案]
- facts-proposal.yml（3 件の fact と、tracks/enforcement の確認）

## files-and-code-execution/review.md
[メインに判断してほしいこと]
- 2 機能の enforcement が null のため、強制力のバッジが出ない。data で値を決めるか確認してほしい（write.md と同じ）

## artifacts-overview/write.md
[メインに判断してほしいこと]
- 強制力の要点の項目：data の artifacts に強制力がなく、要点に足していない。足すなら data へ値の提案が要る
- 成熟度・プラン・上限・2026-09-16 の日付は本文に書かず、facts-proposal.yml に提案した。採用後は #templates の表に fact-table 等の目印を置く案（今の本文はプランと成熟度を公式の記事へ誘導している）
- 書き出し先の形式（Word・PDF など）を本文の表に確認日つきで手書きした。変わりやすい値に当たるなら、数値の提案へ移す
[提案]
- facts-proposal.yml（5 件）
- 用語集：legacy artifacts を短く定義して足す案

## artifacts-overview/review.md
[メインに判断してほしいこと]
- 強制力の値を data に足すか。足すなら要点に項目を置く
- 書き出し先の形式を数値の提案へ移すか

## connectors-in-the-app/write.md
[メインに判断してほしいこと]
- 要点の「強制力」：data の connectors に enforcement がなく、feature の目印では「未確認」になる。値を目印で出さず、文で「鍵ではない。止められるのは道具ごとの許可で締めた操作だけ」と書いた。data に enforcement を足すか判断してほしい
- 雛形 connector-request の control（読み取りだけの行がないと下書きまで作ろうとすることがある）は未検証の記録
[提案]
```yaml
proposals:
  - fact: {id: custom-connector-free-limit, title: 個人の Free プランの Custom connectors の上限, value: 1 件, sources: [hc-connectors], checked: 2026-11-05, status: 確認済み}
    used_in: [connectors-in-the-app#types]
  - fact: {id: connectors-on-demand-recommend-threshold, title: On demand を勧める有効なコネクタの数の目安, value: 10 個以上, sources: [hc-connectors], checked: 2026-11-05, status: 確認済み}
    used_in: [connectors-in-the-app#on-demand]
```
- 上の 2 件は、本文では数字を書かず公式を見る旨にしてある。目印を置く場合の位置が used_in。値は束の 02 §1-11（確認日 2026-10-29）による。Free の上限は data の connectors の note と一致

## connectors-in-the-app/review.md
[メインに判断してほしいこと]
- 要点の強制力を文で書いている（data に enforcement がない）件は write.md のとおり。判断を要する

## permission-modes-in-the-app/write.md
[メインに判断してほしいこと]
- 本文はプラン名と既定を書かず、default-safety-settings#defaults-by-surface を指した。アプリの既定を数値ファイルに置くなら下の提案を採るか判断してほしい
- 「コネクタの許可は届く先を絞る」は、目次の図の案からの書き方で、束の公式の抜き出しに直接の記述がない。本文では穏やかに書いた
[提案]
```yaml
proposals:
  - fact: {id: app-permission-mode-defaults, title: アプリの新しい会話の権限モードの既定（プラン別）, value: "要確認（束の data には Pro・Max・Ultra・Team は Auto、Enterprise は Manual とある。調査資料 02 は Pro・Max・Team の Auto、Enterprise の Manual。Ultra の扱いが食い違う）", sources: [hc-cowork-start, hc-cowork-and-chat], checked: 2026-11-05, status: 要確認}
    used_in: [permission-modes-in-the-app#modes]
```
- 本文には目印を置いていない。採用されたら #modes の「新しい会話の既定の段」の文に fact の目印を足す

## permission-modes-in-the-app/review.md
[メインに判断してほしいこと]
- write.md の提案（アプリの既定の fact）と、コネクタの許可の記述の扱い

## tasks-and-schedules-in-the-app/write.md
[メインに判断してほしいこと]
- 強制力：data の features app-tasks に `enforcement` がない。型の手引きは要点に強制力を求める。値を足すかの判断（足すなら「お願い」が近いが、権限モードやフォルダ許可は鍵に当たるので、1 値に丸めにくい）
- 面のタブ：surfaces が app だけなので省いた
[提案]
```yaml
frontmatter: []
facts: 該当なし（変わりやすい値は本文に書かず、プラン名・日付・頻度の細目は出典で確かめる書き方にした）
glossary:
  - {term: 定期タスク, note: "Scheduled tasks の訳として本文で使った。用語集にあれば表記を合わせる"}
  - {term: 信頼境界, note: "Use Claude Cowork safely の trusted boundary の訳として使った"}
```

## tasks-and-schedules-in-the-app/review.md
[メインに判断してほしいこと]
- 強制力の値を data の app-tasks に足すか（write.md と同じ）

## must-know-operations/write.md
[メインに判断してほしいこと]
- キーの割り当て（Shift+Tab・Ctrl+G・Ctrl+O・Ctrl+B・画像の貼り付けなど）を、目次の notes どおり data に置くか。今は data に項目がないので、本文はバッククォートで手書きした。facts-proposal.yml に案がある。置くなら、本文の該当箇所を目印に差し替える
- 目次の templates は「なし」だったが、分かりやすさのために雛形を 2 つ足した（長い指示の骨組み・画像で渡す依頼文）。不要なら外す
[提案]
- front matter：直さない（sections・stage・updated・sources のみ変更）
- 数値の提案：facts-proposal.yml（キー割り当て 4 件）
- 用語集・prh：なし

## must-know-operations/review.md
[メインに判断してほしいこと]
- 4 の重なりを減らすなら、#pitfalls の `@`・Esc の項を外す案がある。
- 事実と出典は見ていない。キーの割り当ては実機未確認のまま。

## when-to-plan/write.md
[メインに判断してほしいこと]
- 「diff を一文で説明できるなら計画を省いてよい」は、本文で「公式の文書では確かめられていない、この辞典の経験則」と明記して使った。現行の Best practices を取得して確かめたが、plan mode にもこの文にも触れる箇所がなかった（束の notes のとおり）。不要なら `#when` の該当の段落を削る
- 計画の承認後の選択肢の表示文（`Yes, and use auto mode` など）を原文のまま載せた（permission-modes、確認日 2026-11-04）。版や設定で変わるので「文言は版や設定で変わる」と添えた
[提案]
```yaml
frontmatter: []
```
- 用語集・prh への提案はなし。ただし「bypass permissions」が prh で「権限」への置き換えに当たるため、本文では `bypassPermissions`（コードの書式）で書いた。ページの別の箇所で「bypass permissions」を平文で書く場合の扱いを、用語集で決めてほしい
- 数値の提案はなし（facts-proposal.yml は作っていない）

## when-to-plan/review.md
[メインに判断してほしいこと]
- 「bypass permissions」の平文表記の扱いを用語集で決める（write.md の提案どおり）

## usage-context-statusline/write.md
[メインに判断してほしいこと]
- {#instruments} の compare 表で context-window の行が「— / —」になる（data にコストと since がない）。表を外すか、data に値を足すか
- 5 時間の上限の呼び方（5-hour limit）は本文に書かず「短い周期の上限」とした。呼び方を本文に出すなら名前の fact が要る
[提案]
```yaml
proposals:
  - fact: {id: statusline-json-context-used-percentage, title: ステータスラインに渡る JSON の項目（文脈の使用率）, value: context_window.used_percentage, sources: [cc-docs-statusline], checked: 2026-11-05, status: 未確認}
    used_in: [usage-context-statusline#statusline]
  - fact: {id: statusline-json-five-hour-used-percentage, title: ステータスラインに渡る JSON の項目（5-hour limit の使用率）, value: rate_limits.five_hour.used_percentage, sources: [cc-docs-statusline], checked: 2026-11-05, status: 未確認}
    used_in: [usage-context-statusline#statusline]
```
- 上の値は束（research/01 I-2、research/11 p34#171）の写しで、公式の文書を直接開いて確かめていない。雛形のスクリプトだけがこの名前を使い、本文は名前を書いていない
- 用語集：「ステータスライン」を正とし、status line を別名にする案（束の notes が用語集で確かめるとしている）

## usage-context-statusline/review.md
[メインに判断してほしいこと]
- compare 表の context-window の行（「— / —」）を、data に値を足すか表から外すか
- 「短い周期の上限」の呼び方（5-hour limit）を fact にして本文で出すか

## when-to-add-what/write.md
[メインに判断してほしいこと]
- 図：目次の visual 案（繰り返しの種類と移す先を結ぶ static 図）は作っていない。`#triggers` の表で同じ内容を出している。図が要るなら別の担当に頼む
- 比喩を使っていない（`#why` に「広い机」を使える所はあるが、無理に入れなかった）
- `#why` の「実践者の幅」は、個人名を出さず、根拠：弱で書いた（束の 6.4 と 6.5 の写しによる）
[提案]
回数（公式の「Build your setup over time」の表の値）は変わりやすい値なので、本文に書かず、種類だけの表にした。数値ファイルに入れれば、`#triggers` の表の下の段落に目印を置ける。値は束の 6.3 の表記（同じ規約・コマンドを 2 回間違えた→CLAUDE.md、同じ手順書を 3 回目に貼った→スキル）による。公式の表の原文で再確認が要る。

```yaml
proposals:
  - fact: {id: add-trigger-claude-md-mistake-count, title: CLAUDE.md に足す目安（同じ規約・コマンドを間違えた回数）, value: 2 回, sources: [cc-docs-features-overview], checked: 2026-11-05, status: 要確認}
    used_in: [when-to-add-what#triggers]
  - fact: {id: add-trigger-skill-paste-count, title: スキルに足す目安（同じ手順書を貼った回数）, value: 3 回目, sources: [cc-docs-features-overview], checked: 2026-11-05, status: 要確認}
    used_in: [when-to-add-what#triggers]
frontmatter: []
```

## when-to-add-what/review.md
[メインに判断してほしいこと]
- 図（visual 案）と比喩が未作成。write.md の判断事項のとおり

## extensions-at-a-glance/write.md
[メインに判断してほしいこと]
- 本文の「4 つの層」は 01 KQ1 Takeaway の構造（後半の注記つきの文は使っていない）を要約した。公式の分け方そのものではないので「この辞典が要約したもの」と書いた。この言い方でよいか
- 「重なり方」の 4 項目（CLAUDE.md は加算、スキルとサブエージェントは名前で上書き、MCP は名前で上書き、フックはマージ）は、01 0-4 の写しから書いた。data の facts にないので出典は features-overview のみ。優先度の順は書かず公式へ誘導した
[提案]
- 数値の提案なし
- data：`rules` の `survives_compaction` は条件付きで、表に「条件による」と出る前提で本文を書いた（すでに `conditional` あり）。`subagents` の強制力、`mcp` の圧縮の扱い、`plugins`・`code-intelligence` の強制力は null か欠で「未確認」と出る。本文の「空欄の読み方」でその理由を説明した。表に「未確認」が多く見えるのが気になるなら、data 側で「1 語で言えない」という値の表現を持てるかを検討してほしい

## extensions-at-a-glance/review.md
[メインに判断してほしいこと]
- 表で多数の「未確認」「—」が見える点は write.md の提案どおり。data 側の表現の検討を

