---
id: after-switching-models
title: 新しいモデルに替えたら見直すこと
aliases: [モデルの移行, 既定のモデルが変わったとき, 旧モデルの退役, モデルの非推奨]
type: recipe
field: models
chapter: 替えたとき・劣化を疑うとき
order: 90
level: 任せる
priority: 必須
surfaces: [claude-code, api, app]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: モデルを替えたときや既定が変わったときに、effort の持ち越し・古い強調や検証の指示・使えなくなった API の引数を見直せる。外すものは一つずつ外し、効果を測る。
signs:
  - {type: situation, text: 既定のモデルが新しくなったと知った}
  - {type: symptom, text: モデルを替えてから、API がエラーを返すようになった}
  - {type: goal, text: 旧いモデルが使えなくなる前に、移行を済ませたい}
prerequisites: [choosing-a-model, effort-levels, measure-changes]
related: [model-quirks, harness-over-model, emphasis-words, verification-ladder#verbal-checks, structured-outputs-basics, claude-md-length, outdated-advice-ledger, change-timeline-2026]
tracks: [model-selection, effort, adaptive-thinking]
outdated_advice: [budget-tokens, prefill-for-json, lower-temperature, important-caps, add-double-check]
sources: [cc-docs-model-config, cc-docs-commands, cc-docs-best-practices, api-docs-effort, api-docs-thinking, api-docs-structured-outputs, api-docs-model-deprecations, api-docs-migration-2026-10-21, api-docs-prompting-best-practices, api-docs-prompting-opus-5, api-docs-prompting-opus-5-5, api-release-notes]
volatility: 高
sections:
  - {title: 先に整える守り, anchor: before-you-start}
  - {title: 見直す順, anchor: checklist}
  - {title: API の引数とモデルの世代, anchor: api-parameters}
  - {title: ハーネスの部品を一つずつ外して測る, anchor: remove-one-at-a-time}
  - {title: 全体を確かめる, anchor: verify-whole}
  - {title: 退役と既定の変化に気づく, anchor: retirements-and-default-changes}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：モデルを替えたときや既定が変わったときに、effort の持ち越し・古い強調や検証の指示・使えなくなった API の引数を見直せる。
    - **いつ引くか**：既定のモデルが新しくなったと知ったとき、モデルを替えてから API がエラーを返すようになったとき、旧いモデルが使えなくなる前に移行を済ませたいとき。
    - **前提**：<!-- link:begin choosing-a-model -->[モデルの選び方（三段階）](choosing-a-model.md)<!-- link:end -->、<!-- link:begin effort-levels -->[effort の段階と使い分け](effort-levels.md)<!-- link:end -->、<!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：モデルの移行・既定のモデルが変わったとき・旧モデルの退役・モデルの非推奨
<!-- textlint-enable -->

このページは、モデルを替えた直後や既定のモデルが変わった直後に、古い前提で書いた設定を点検する手順である。見るのは、effort の持ち越し、古い強調や検証の指示、世代によって受け付けられなくなった API の引数の 3 つだ。外すものは 1 つずつ外し、そのたびに効果を測る。

## 先に整える守り {#before-you-start}

モデルを替える前に、替えたあとで比べる物差しと、元に戻す手段を用意する。見直しは設定を変える作業なので、物差しがないと、良くなったのか悪くなったのかが分からない。

古い設定が問題になるのは、そのモデルの弱点を補う回避策だったからだ。モデルが替わると、回避策は不要になるだけでなく、効きすぎたり、エラーを起こしたりする。この規則性は <!-- link:begin outdated-advice-ledger#workarounds -->[古くなった助言の台帳 › 回避策は正式な仕組みに置き換わる](../changes/outdated-advice-ledger.md#workarounds)<!-- link:end --> が説明している。

- **物差し**：最近うまくいかなかったタスクを数件選び、今のモデルで何度か走らせて結果を残す。手順は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にあり、試行の数の考え方は <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> にある。
- **戻す手段**：CLAUDE.md、`.claude/`、API を呼ぶコードを commit してから触る。モデルの指定も、元の値を控えておく。
- **順番**：モデルを替える前に、effort の調整で足りないかを見る。理由は <!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](choosing-a-model.md#effort-first)<!-- link:end --> が書いている。
- **任せる幅**：ループや夜間の自動実行のように任せる幅が大きい運用は、この見直しを終え、物差しで前と同じ結果が出ることを確かめてから再開する。

## 見直す順 {#checklist}

見直しは、影響が大きく確かめやすい順に 5 つの段で進める。1 つの段を終えるたびに、物差しのタスクを走らせて結果を記録する。

1. **effort を確かめる**。替えたモデルの既定の段は、前のモデルと違うことがある。公式は、世代を替えるとき以前の段を持ち越さず、新しいモデルの既定から始めて自分の作業で振るよう勧める。モデルと面ごとの既定は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](effort-levels.md#defaults-by-surface)<!-- link:end --> で引ける。終わりの確かめ：今の段が、意図して選んだ段になっている。
2. **API の引数を直す**。世代によって 400 エラーになる引数を、API を呼ぶコードから探して消す。詳しくは、下の「API の引数とモデルの世代」の節にある。終わりの確かめ：物差しのタスクが、エラーなしで最後まで走る。
3. **強調語を和らげる**。CLAUDE.md・rules・スキルで、IMPORTANT や YOU MUST の行を探し、普通の言葉に直す。強調は守らせる力にならず、かえって規則の当てはめすぎを招くことがある。理由は <!-- link:begin emphasis-words#overreaction -->[強調語（IMPORTANT・必ず）の現在 › 強い言い方が過剰に効く](../prompting/emphasis-words.md#overreaction)<!-- link:end --> にある。直したあとに守られなくなる行は、ファイルを短くするか、例外を許さない規則ならフックか deny ルールに移す。短くする問いは <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](../extend/claude-md-length.md#deletion-test)<!-- link:end --> にある。終わりの確かめ：直した行の指示が、前と同じように守られる。
4. **確認を命じる一文を外して比べる**。「最後に double-check して」のような一文は、公式の手引きが「このモデルは言われなくても自分の作業を確かめる」と書くモデルでは、確かめすぎで時間とトークンを増やす。ほかのモデルでは今も効く。外す前に、使うモデルの手引きを確かめる。台帳の行は <!-- link:begin outdated-advice-ledger#add-double-check -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#add-double-check)<!-- link:end --> にある。外した代わりに入れるのは、確かめる手段（テスト・型の検査・照らす基準）だ。選び方は <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> にある。終わりの確かめ：外す前後で、誤りの出方が変わらない。
5. **補助の部品を 1 つずつ外す**。フック・補助のスクリプト・手順の細かい指示を、1 つずつ外して測る。進め方は、下の「ハーネスの部品を一つずつ外して測る」の節にある。

effort を確かめる場所は、面で違う。

=== "アプリ"

    送信ボタンの横のモデルのメニューで、今のモデルと effort を見て選ぶ。

=== "Claude Code"

    `/effort status` で今の段を表示し、`/effort` で変える。`/model` で選んだモデルは、新しいセッションの既定として保存される。

=== "API"

    要求に `effort` を明示しているかを見る。省いたときの既定は、モデルで違う。

見直す候補は、手で探すほかに、道具に洗い出させることもできる。Claude Code の `/doctor prompt-audit` は、古いモデル向けに書いた指示や、食い違う指示を洗い出し、直しは確認を取ってから適用する。使うには <!-- fact:begin doctor-prompt-audit-min-version -->Claude Code 2.1.283 以上が要る（2026-11-04 時点）<!-- fact:end -->（[Commands](https://code.claude.com/docs/en/commands) で確かめる）。候補の洗い出しを依頼の形で出すなら、次の雛形を使う。

<!-- gen:begin snippet after-switching-models/audit-request -->
<!-- textlint-disable -->

??? example "雛形：見直す候補を洗い出させる依頼"

    ```markdown
    モデルを新しい世代に替える予定がある。設定を直す前に、見直す候補を洗い出してほしい。ファイルは書き換えず、読むだけにする。

    調べるのは、CLAUDE.md、`.claude/rules/`、`.claude/skills/` と、サブエージェントの定義にある次の 3 種類の記述だ。

    1. 強調の語（IMPORTANT・YOU MUST・NEVER・全部が大文字の行）
    2. 確認を命じる一文（「最後に見直して」「double-check して」、確かめ役のサブエージェントを使わせる指示）
    3. 古いモデルの弱点に合わせた補助の記述（短く答えさせる指示、手順を細かく刻む指示など）

    結果は表で返す。列は「ファイル・行」「引用」「種類（1〜3）」「外す理由の見立て」「外すと困ることがあるか」とする。見立ては推測なので、そう分かるように書く。終わりに、1 つずつ外して比べる順番の案を出す。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet after-switching-models/audit-request -->

API を呼ぶコードの側は、次のスクリプトで候補を探せる。

<!-- gen:begin snippet after-switching-models/find-old-settings -->
<!-- textlint-disable -->

??? example "雛形：見直す対象の候補を探すスクリプト"

    ```bash
    #!/usr/bin/env bash
    # モデルを替える前に、見直す対象の候補を探す。読むだけで、何も書き換えない。
    # プロジェクトのルートで実行する。
    set -u

    echo "== API の引数（budget_tokens・temperature・top_p・top_k）=="
    grep -rnE 'budget_tokens|temperature|top_p|top_k' \
      --include='*.py' --include='*.ts' --include='*.js' --include='*.json' \
      --include='*.yaml' --include='*.yml' \
      --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=.venv . || true

    echo
    echo "== 強調語と、確認を命じる一文 =="
    grep -rnE 'IMPORTANT|YOU MUST|NEVER|double-check|re-verify|最後に見直|最後に確認' \
      CLAUDE.md .claude 2>/dev/null || true

    echo
    echo "メモ：最後が assistant のメッセージで終わる要求（prefill）は grep では見つけにくい。"
    echo "messages を組み立てるコードを目で読んで確かめる。"
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet after-switching-models/find-old-settings -->

段ごとの記録に使う点検表を、次に置く。

<!-- gen:begin snippet after-switching-models/switch-checklist -->
<!-- textlint-disable -->

??? example "雛形：モデルを替えたときの見直しの点検表"

    ```markdown
    # モデルを替えたときの見直しの点検表

    - 替えた日：
    - 替える前のモデル／替えたあとのモデル：
    - 使う面（アプリ・Claude Code・API）：
    - 物差しにするタスク（失敗したものを数件）：

    ## 先に整える

    - [ ] 設定ファイルと API を呼ぶコードを commit した（戻せる）
    - [ ] 物差しのタスクを、替える前のモデルで複数回走らせて記録した
    - [ ] 替えずに effort の調整で足りないかを先に見た

    ## 見直す（1 つ直したら、物差しのタスクを走らせて記録する）

    - [ ] 1. effort：今の段を確かめた。前のモデルの段を持ち越していない
    - [ ] 2. API の引数：`budget_tokens`、最後が assistant のメッセージの要求、`temperature`・`top_p`・`top_k` を探した
    - [ ] 3. 強調語：IMPORTANT・YOU MUST などを探し、普通の言葉に直した（守られなくなった行は、短くするかフックにする）
    - [ ] 4. 確認を命じる一文：使うモデルの公式の手引きを確かめてから、外して比べた
    - [ ] 5. 補助の部品：1 つ外して記録し、悪化したら戻した

    ## 退役と既定の変化

    - [ ] 使っているモデルの名前が、退役の予定に入っていないかを確かめた
    - [ ] モデルの指定が、別名か固定の名前かを確かめた
    - [ ] 組織やチームの設定で、使えるモデルが絞られていないかを確かめた

    ## 記録

    - 外したもの／残したもの／戻したもの：
    - 前後の結果の差：
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet after-switching-models/switch-checklist -->

## API の引数とモデルの世代 {#api-parameters}

モデルを替えたあとの API のエラーは、同じコードがモデルの世代や API の版によって受け付けられなくなったことから起きることが多い。エラーの出方から、疑う引数を引く。

| エラーの出方 | 疑う引数 | 直し方 | 台帳 |
| --- | --- | --- | --- |
| thinking に手動の予算を付けた要求が 400 になる | `budget_tokens` | thinking の type を adaptive にし、深さは effort で決める | <!-- link:begin outdated-advice-ledger#budget-tokens -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#budget-tokens)<!-- link:end --> |
| 最後が assistant のメッセージの要求が 400 になる | prefill（応答の書き出しを先に書く） | structured outputs で形を保証する。移行は <!-- link:begin structured-outputs-basics#from-prefill -->structured outputs（形式を保証する） › prefill からの移行（準備中）<!-- link:end --> | <!-- link:begin outdated-advice-ledger#prefill-for-json -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#prefill-for-json)<!-- link:end --> |
| `temperature`・`top_p`・`top_k` を送ると 400 になる | この 3 つの引数 | 引数を消し、指示で振る舞いを導く。代わりの設定はない | <!-- link:begin outdated-advice-ledger#lower-temperature -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#lower-temperature)<!-- link:end --> |

どの世代・どの API の版から断られるかは、台帳の行に日付と版つきで載っている。本文には書かない。

- **モデルを戻す前に、引数を疑う**。400 は、モデルが悪いのではなく、要求の形が合っていないことを示す。旧いモデルに戻せば消えるが、旧いモデルはいずれ退役する。
- **SDK を上げたときも同じエラーが出る**。新しい SDK は新しい API の版を既定で送ることがあり、その版では引数が外されている。モデルを替えていなくても、SDK を上げて 400 が出たら、この表を見る。公式の移行の案内は [Migrating to API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21) にある。
- **旧いモデルには今も効く引数がある**。引数を外すのは、モデルを替える側の移行の一部だ。旧いモデルを古い API の版で使い続ける間は、手を付けなくてよい。
- **thinking の切り替え**。新しいモデルには、thinking を切れないものがある。切れる前提のコードは、エラーか無視のどちらかになる。確かめる所は <!-- link:begin effort-levels#thinking-toggle -->[effort の段階と使い分け › thinking の切り替え](effort-levels.md#thinking-toggle)<!-- link:end --> にある。

引数を直したあと、出力の安定性が変わったと感じたら、引数の代わりを探さず、指示で形と振る舞いを書き、物差しで確かめる。

## ハーネスの部品を一つずつ外して測る {#remove-one-at-a-time}

ハーネスとは、CLAUDE.md、フック、補助のスクリプト、検証の指示のように、モデルの外側で結果を支える部品の全体だ。意味は <!-- link:begin harness-over-model#what-is-harness -->モデルの差よりハーネスの差 › ハーネスとは何か（準備中）<!-- link:end --> にある。各部品は「モデルが単独ではできないこと」についての仮定である。モデルが替わると、その仮定が古くなっている部品が出てくる。

仮定が古くなった部品を探すとき、一度にまとめて外してはいけない。結果が落ちたときに、どの部品が効いていたのかが分からなくなるからだ。1 つ外して測り、結果を見てから次に進む。

1. 外す候補を並べる。優先は、強調語、確認を命じる一文、手順の細かい指示、補助のスクリプトの順にする。候補の洗い出しは、「見直す順」の節にある 2 つの雛形（依頼の形と、スクリプトの形）を使う。
2. 1 つだけ外す。ほかの設定は変えない。
3. 物差しのタスクを同じ回数だけ走らせ、前と比べる。1 回の結果では判断しない。手順は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end -->、読み方は <!-- link:begin measure-changes#read-transcripts -->[変更が効いたかを測る（小さな eval） › transcript を読む](../eval/measure-changes.md#read-transcripts)<!-- link:end --> にある。
4. 変わらないか良くなったら、外したままにする。悪くなったら戻す。結果を記録に残す。
5. 次の候補に進む。

外さないものもある。フックと deny ルールのように、モデルの判断に頼らず仕組みで止めている規則は、モデルが賢くなっても外す理由にならない。この手順の対象は、お願いとして書いた指示と、モデルの弱点を補う部品だ。

!!! example "判断例：CLAUDE.md の古い指示をまとめて消すか"
    - **状況**：新しいモデルに替えた。CLAUDE.md に、IMPORTANT の付いた行が数行と、「完了前に必ず double-check する」の行と、手順を細かく刻む節がある。
    - **迷う候補**：古い前提の指示だから、まとめて消して短くする。または、1 つずつ外して、そのたびに測る。
    - **選んだもの**：1 つずつ外して測る。まず強調語を普通の言葉に直し、次に確認を命じる行を外す。
    - **理由**：まとめて消して結果が落ちると、どの行が効いていたのか分からず、全部を戻すしかなくなる。1 つずつなら、落ちた変更だけを戻せる。測る手間は、最初の物差しを作ってあるので小さい。

## 全体を確かめる {#verify-whole}

「見直す順」の 5 つの段を終えたら、替える前に記録した物差しのタスクを、全体として走らせ直す。見直しの前後を並べて、新しい設定が前より悪くなっていないことを確かめる。

- **合計だけで判断しない**。平均が同じでも、特定の種類のタスクだけが落ちていることがある。層ごとに見て、最悪のケースも見る。見方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> にある。
- **結果だけでなく過程を読む**。同じ結果でも、確認の回数やツールの使い方が変わっていることがある。見方は <!-- link:begin measure-changes#read-transcripts -->[変更が効いたかを測る（小さな eval） › transcript を読む](../eval/measure-changes.md#read-transcripts)<!-- link:end --> にある。
- **モデルの癖の記録を残す**。止まりすぎ・やりすぎなどの傾向は、世代で変わる。自分の環境で観察した傾向を記録に残す。公式の指針は <!-- link:begin model-quirks#official-guidance -->モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向（準備中）<!-- link:end -->、記録の付け方は <!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end --> にある。
- **差が小さいとき**。ばらつきの範囲に収まる差は、見直しの効果としない。試行を増やして確かめ直す。増やしても差が埋もれるなら、その差は外す根拠にも残す根拠にもしない。

## 退役と既定の変化に気づく {#retirements-and-default-changes}

モデルを替えるきっかけは、自分で決める場合のほかに、外から来る場合がある。旧いモデルの退役と、既定のモデルの変化の 2 つだ。どちらも気づくのが遅れると、移行を急ぐことになる。

- **退役**。API のモデルは、モデルごとに退役の日が告知される。アプリでは、選択肢から旧いモデルを外す例がある。旧いモデルで始めた会話の続きは、置き換え先のモデルが答える。Claude Code や API には残る場合もあり、面ごとに違う。
- **既定の変化**。新しいモデルが出るたびに、既定のモデルや既定の effort は替わりうる。Claude Code の `/model` で選んだモデルは新しいセッションの既定として保存される。自分で選んでいない既定は、いつの間にか替わっている。

気づくための確認を、次に挙げる。

1. 使っているモデルの指定が、別名か固定の名前かを確かめる。どちらがいつ替わるかは、[Model configuration](https://code.claude.com/docs/en/model-config) で確かめる。
2. API で使うモデルの名前が、退役の予定に入っていないかを、[Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) で確かめる。
3. 日付つきの変更は、[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) と、Claude Code の CHANGELOG で拾う。このサイトでは、<!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> に主な変更が日付つきで並ぶ。
4. 組織で使えるモデルが絞られているときは、管理者の設定を確かめる。

退役の日付と、各モデルの既定の値は変わりやすいので、このページには書かず、上の文書と年表で引く。

## 失敗したとき {#when-it-fails}

見直しの途中で起きやすい失敗を、症状から引く。

- **API が 400 を返す**。「API の引数とモデルの世代」の節の表で、疑う引数を探す。
- **替えたら結果が悪くなった**。設定の古さではなく、劣化として疑う場合は <!-- link:begin suspected-degradation -->[劣化を疑ったら測って確かめる](suspected-degradation.md)<!-- link:end --> へ進む。モデルの差に見えて、実際はハーネスの差だった例がある。確かめ方は <!-- link:begin harness-over-model#compare-with-your-eval -->モデルの差よりハーネスの差 › 比べるときは自分の評価で（準備中）<!-- link:end --> にある。
- **外したら悪くなった**。その部品を戻して、次の候補に進む。悪くなった部品は、そのモデルでもまだ効いている可能性が高い。
- **結果がぶれて判断できない**。試行の数を増やす。考え方は <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> にある。
- **何から手を付けるか分からない**。「見直す順」の節の点検表を上から順に、1 つずつ済ませる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)：Anthropic・英語・確認日 2026-11-04
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)：Anthropic・英語・確認日 2026-11-04
- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)：Anthropic・英語・確認日 2026-11-04
- [Migrating to API version 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [モデルの選び方（三段階）](choosing-a-model.md)
- [effort の段階と使い分け](effort-levels.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

**関連**

- モデル別の癖と、プロンプトの合わせ方（準備中）
- モデルの差よりハーネスの差（準備中）
- [強調語（IMPORTANT・必ず）の現在](../prompting/emphasis-words.md)
- [検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)
- structured outputs（形式を保証する）（準備中）
- [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 2026 年の主な変更の年表（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
