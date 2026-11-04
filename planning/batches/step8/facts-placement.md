# 数値の目印を置く場所の一覧（工程8 DM1）

data/facts.yml に足した facts（56 件）を、ページの順（id の英字順）に並べた。目印を置くのは後の担当で、DM1 はページ（docs/）を直していない。

- 置き方の記号：fact の目印は `<!-- fact:begin <id> --><!-- fact:end -->`、組は `<!-- gen:begin fact-table <id> -->`〜`<!-- gen:end fact-table <id> -->`。値と決まった文（sentence）と確認日は道具が書く。置いたら `gen_site.py --page <id>` で埋める
- 状態が未確認の fact は、道具が値を出さず「未確認」とだけ書く。該当の行の置き方に「未確認」と書いた。値が出るのは、検証役が確かめて status を確認済みにした後
- 提案の合流：evidence-not-reports と claims-done-but-isnt は同じ 2 つの id、going-in-circles と when-to-start-fresh は clear-after-failed-corrections、goal-until-done と how-usage-limits-work は auto-continue-max-times、how-attachments-are-read と skipped-later-pages は app-pdf-*、knowledge-cutoff と doesnt-know-latest は model-knowledge-cutoffs、effort-levels と how-thinking-works は effort-default-by-model-surface、permission-modes-overview と default-safety-settings は permission-mode-default-*
- 表の fact は、行の名前に空白があると、セルの inline の目印（`fact:begin <id> <行> <列>`）にできない（effort の表・model-knowledge-cutoffs の「Opus 4.6」など）。表全体は fact-table で置く
- 今回の facts には `match`（目印の外の手書きを見つける型）を付けていない。置くとき、目印の外に同じ値を手で残さない

| fact の id | ページ | 節の anchor | 目印を置く文（いまのページの文） | 置き方 |
| --- | --- | --- | --- | --- |
| `checkpoint-retention-count` | checkpoints-and-rewind | #what-is-restored | 「ファイルの控えには保存の数と期間があり」 | 段落の中の fact の目印（「保存の数」に。文を「保存の数（直近の N 個）と期間（約 N 日）があり」に直す） |
| `checkpoint-retention-days` | checkpoints-and-rewind | #what-is-restored | 「長く残したいときは設定 `cleanupPeriodDays` を調べる」 | 段落の中の fact の目印（既定の期間として。上の項目と同じ文に置く） |
| `at-reference-read-limit` | choose-what-to-read | #caveats | 「上限の値はバージョンで変わりうるので、ここには書かない」 | 段落の中の fact の目印（未確認なので「未確認」と出る。「ここには書かない」を目印を使う文に直す） |
| `claude-code-search-truncation-fix-version` | claims-done-but-isnt | #forms | 「のちの版で直った（CHANGELOG の記録）」 | 段落の中の fact の目印（「のちの版」を版に。検索の不具合の版） |
| `claude-code-p-startup-failure-exit-code-fix-version` | claims-done-but-isnt | #forms | 「起動に失敗しても終了コード 0 で終わる不具合があり」 | 段落の中の fact の目印（起動の失敗の版。未確認） |
| `mcp-output-token-limits` | connecting-mcp | #limits | 「ツールの出力が一定を超えると警告が出て、さらに大きいと上限で扱いきれなくなる」 | 段落の中の fact の目印（「一定」に。未確認なので「未確認」と出る） |
| `permission-mode-default-interactive` | default-safety-settings | #defaults-by-surface | 「権限：既定の開始モードは版で変わってきた」 | 段落の中の fact の目印（箇条「権限」。対話の端末と VS Code の既定） |
| `permission-mode-default-noninteractive` | default-safety-settings | #defaults-by-surface | 「非対話の実行は対話と既定が違う（同じ箇条）」 | 段落の中の fact の目印（箇条「権限」。-p と Agent SDK の既定） |
| `sandbox-default-state` | default-safety-settings | #defaults-by-surface | 「通信と読み書き：Claude が動かすコマンドの囲いは、サンドボックスが担う」 | 段落の中の fact の目印（箇条「通信と読み書き」。既定の状態。未確認） |
| `app-default-permission-mode` | default-safety-settings | #defaults-by-surface | （アプリのタブ）既定はプランと管理者の設定で変わりうる | 段落の中の fact の目印（アプリのタブ「権限」。未確認） |
| `incognito-retention-period` | default-safety-settings | #defaults-by-surface | （アプリのタブ）記録と記憶は、会話ごとの設定とシークレットチャットで調整する | 段落の中の fact の目印（アプリのタブ「記録と記憶」。未確認） |
| `model-knowledge-cutoffs` | doesnt-know-latest | #diagnosis | 「日付は、モデルごとの公式の文書で確かめる」 | 段落の中の fact の目印（表のセル：行「現行のモデル」・列 reliable／training。行「Opus 4.6」は空白を含み inline にできないので使わない）。置かずに knowledge-cutoff#why を link してもよい |
| `effort-default-by-model-surface` | effort-levels | #defaults-by-surface | 「各モデルの既定の値は、変わりやすいので、この節に手で書かない」 | fact-table の組（段落「各モデルの既定の値は…」の直後。段落を「下の表のとおり。公式で確かめる」に直す） |
| `effort-model-settings-min-version` | effort-levels | #how-to-set | 「モデルごとの保存には、新しい版の Claude Code が要る」 | 段落の中の fact の目印（「新しい版」に。「版は公式の Settings で確かめる」は残すか削る） |
| `subagent-own-model-effort-min-version` | effort-levels | #subagents-and-org-limits | 「本体と別のモデルで動くサブエージェントやチームメイトは、セッションの段を受け継がない」 | 段落の中の fact の目印（この挙動が入った版として。未確認） |
| `claude-code-search-truncation-fix-version` | evidence-not-reports | #tool-output | 「直った版は CHANGELOG で確かめる」 | 段落の中の fact の目印（箇条「途中で切れた検索」に版を。claims-done-but-isnt と同じ id） |
| `claude-code-p-startup-failure-exit-code-fix-version` | evidence-not-reports | #tool-output | 「`claude -p` が、起動に失敗しても何も出さず、終了コード 0 で終わっていた」 | 段落の中の fact の目印（箇条「失敗を成功として返す起動」に版を） |
| `compaction-bugfix-version` | forgot-after-compaction | #diagnosis | 「圧縮まわりの不具合は、版を上げて直ったものがある」 | 段落の中の fact の目印（項目 6。未確認） |
| `goal-condition-max-chars` | goal-until-done | #writing-conditions | 「条件の長さには上限がある。値は変わりうるので、手元の公式の説明で確かめる」 | 段落の中の fact の目印（「値は…確かめる」を目印を使う文に） |
| `goal-idle-checkins-max` | goal-until-done | #evaluator-reads-conversation | 「背景の作業を待つ時間が長くなると、確認の呼びかけが入る」 | 段落の中の fact の目印（呼びかけの回数の上限を足す） |
| `goal-checkin-minutes` | goal-until-done | #evaluator-reads-conversation | 「待つ間隔は呼びかけのたびに延びる」 | 段落の中の fact の目印（最初の間隔として） |
| `goal-auto-retry-max` | goal-until-done | #at-usage-limits | 「待ち時間つきの通知が出て、回数に上限がある」 | 段落の中の fact の目印（箇条「再試行する」の「回数」に） |
| `auto-continue-max-times` | goal-until-done | #at-usage-limits | 「続ける回数には上限があり、`/goal` も同じ回数に数える」 | 段落の中の fact の目印（「回数」に） |
| `clear-after-failed-corrections` | going-in-circles | #choose | 「同じ点の訂正が重なっても直らないときは、さらに訂正を足さないよう勧める」 | 段落の中の fact の目印（「重なっても」を回数にする文へ） |
| `hook-event-count` | hooks-basics | #events | 「イベントの数は多く、全部の網羅は公式のフックのリファレンスに任せる」 | 段落の中の fact の目印（「多く」に。未確認） |
| `hook-handler-types` | hooks-basics | #deterministic | 「フックには複数のハンドラ（走らせるものの種類）があり」 | 段落の中の fact の目印（「複数」に。未確認） |
| `hook-monitor-min-version` | hooks-basics | #limits | 「Bash に当てたフックは、新しい版では Monitor の道具が起動するシェルコマンドにも走る」 | 段落の中の fact の目印（「新しい版」に。未確認） |
| `hook-agent-id-min-version` | hooks-basics | #locations | 「フックへの入力には `agent_id` が付き」 | 段落の中の fact の目印（`agent_id` が付く最低の版を足す。未確認） |
| `app-pdf-visual-pages` | how-attachments-are-read | #pdf-and-others | 「境目のページ数と、ファイルの大きさ・数の上限は、変わりうる値である」 | 段落の中の fact の目印（「境目のページ数」を目印を使う文に。視覚要素の範囲） |
| `app-pdf-text-only-pages` | how-attachments-are-read | #pdf-and-others | 「その先は文字だけが処理され、図は解析されない。さらに先は受け付けられない」 | 段落の中の fact の目印（文字だけの範囲と受け付けない境目） |
| `app-upload-file-size-count` | how-attachments-are-read | #pitfalls | 「会話へのアップロードの記事と、ファイルの作成の記事で、1 ファイルの大きさの上限が違って書かれている」 | 段落の中の fact の目印（食い違いのある値。道具が conflict を「食い違い」として出す） |
| `memory-default-by-plan` | how-memory-works | #what-is-saved | 「メモリが既定で有効かどうかは、プランで違う」 | 段落の中の fact の目印（既定の一覧を足す） |
| `chat-search-plans` | how-memory-works | #chat-search | 「使えるのは有料のプランで、web・Desktop・Mobile のどれからでも使える」 | 段落の中の fact の目印（「有料のプラン」を具体のプランに） |
| `usage-limit-types-by-plan` | how-usage-limits-work | #limit-types | 「プランによって、この 2 種類の持ち方と倍率が違う」 | fact-table の組（この文の後ろ。節題から「（プランごとの表）」を外さずに済む） |
| `auto-continue-max-times` | how-usage-limits-work | #when-you-hit-the-limit | 「続ける回数には上限があり、上限を超えると止まる」 | 段落の中の fact の目印（箇条の「回数」に） |
| `wrap-up-allowance-frequency` | how-usage-limits-work | #when-you-hit-the-limit | 「続けられる量には上限があり、回数はプランで違う」 | fact-table の組（段落の後ろ） |
| `wrap-up-allowance-min-version` | how-usage-limits-work | #when-you-hit-the-limit | 「もう 1 つ、Claude Code には Wrap-Up Allowance がある」 | 段落の中の fact の目印（資格に要る版として） |
| `auto-mode-no-verdict-display-fixed` | keeps-stopping | #diagnosis | 「その不具合は後の版で修正されている」 | 段落の中の fact の目印（項目 1 の「後の版」に。未確認） |
| `model-knowledge-cutoffs` | knowledge-cutoff | #why | 「日付の値は、モデルが替わるたびに変わる。このページには書かない」 | fact-table の組（この段落の後ろ。段落を直す） |
| `long-context-order-quality-gain` | long-context-first | #order | 「公式は、この並べ方で自社のテストの品質が上がり、複数の文書を渡す場合に特に効いたと述べる」 | 段落の中の fact の目印（「品質が上がり」に、最大の向上の割合として） |
| `long-context-quote-first-length-threshold` | long-context-first | #quote-first | 「公式の Reduce hallucinations は、とくに長い文書では、先に逐語の引用を抜き出させ」 | 段落の中の fact の目印（「とくに長い文書」の目安として） |
| `permission-mode-default-interactive` | permission-modes-overview | #defaults | 「対話のセッションの既定は、版が進む中で Manual から auto モードへ移った」 | 段落の中の fact の目印（今の既定と版を足す） |
| `permission-mode-default-noninteractive` | permission-modes-overview | #defaults | 「対話の端末と VS Code の拡張、`claude -p` と Agent SDK で既定が違う」 | 段落の中の fact の目印（手順 3 の「既定が違う」の具体に） |
| `sandbox-default-reads` | sandboxing | #default-reads | 「サンドボックスの既定では、読み取りは機械全体に及ぶ」 | 段落の中の fact の目印（手書きの「機械全体」を目印に替える） |
| `sandbox-fail-open-default` | sandboxing | #fail-if-unavailable | 「サンドボックスは既定で黙って無効のまま、コマンドを囲わずに動かす」 | 段落の中の fact の目印（手書きの既定の説明を目印に替える） |
| `web-search-call-guide` | search-research-thinking | #comparison | 「公式の使い分けの記事は、呼び出しの回数と所要時間の目安も挙げている」 | 段落の中の fact の目印（web 検索の目安） |
| `research-call-guide` | search-research-thinking | #comparison | （同じ文） | 段落の中の fact の目印（リサーチの目安） |
| `fishtest-retry-cap` | selection-pressure | #retry-cap | 「Fishtest の FAQ は、同じアイデアの再挑戦に、回数の上限を置いている」 | 段落の中の fact の目印（「回数の上限」に。未確認） |
| `app-pdf-visual-pages` | skipped-later-pages | #diagnosis | 「PDF は先頭から一定のページまでは文字と図表の両方が読まれ」 | 段落の中の fact の目印（「一定のページ」に） |
| `app-pdf-text-only-pages` | skipped-later-pages | #diagnosis | 「その先は文字だけになる」 | 段落の中の fact の目印（文字だけの範囲） |
| `hook-on-failure-block-min-version` | textlint-hook | #failure-and-few | 「command か http のフックで使え、新しい版から入った」 | 段落の中の fact の目印（「新しい版」に） |
| `tokenizer-token-increase-opus-4-7` | tokens | #what-happens | 「増える割合は用語集にあり、このページには固定して書かない」 | 段落の中の fact の目印（文を直す。用語集の割合を目印で書く） |
| `chars-per-token-earlier-models` | tokens | #why | 「1 トークンが表す文字数は、モデルと言語による」 | 段落の中の fact の目印（4.7 より前のモデルの目安として足す） |
| `tokenizer-token-range-opus-5-5` | tokens | #why | 「移行の手引きも、増え方は内容による、と範囲で案内するだけである」 | 段落の中の fact の目印（「範囲」に。未確認） |
| `auto-mode-block-pause-thresholds` | what-auto-mode-stops | #limits | 「ブロックが連続、または合計で一定の回数に達すると、auto モードは一時停止して手動の確認に戻る」 | 段落の中の fact の目印（「一定の回数」に。未確認） |
| `compaction-reread-files-max` | what-survives-compaction | #reloaded | 「読んだか編集したファイル：最近変更されたものから、決まった個数まで再び読み込まれる」 | 段落の中の fact の目印（「決まった個数」に） |
| `compaction-reread-file-tokens-max` | what-survives-compaction | #reloaded | 「大きなファイルは中身なしで、パスの参照として戻る」 | 段落の中の fact の目印（「大きな」の目安として） |
| `auto-memory-startup-load` | what-survives-compaction | #reloaded | 「MEMORY.md の頭の部分が、ディスクから入れ直される」 | 段落の中の fact の目印（「頭の部分」に） |
| `hook-output-max-chars` | what-survives-compaction | #kept | 「フックの出力には大きさの上限がある」 | 段落の中の fact の目印（「上限」に） |
| `clear-after-failed-corrections` | when-to-start-fresh | #signals | 「回数の目安は公式を見る」 | 段落の中の fact の目印（この一文を目印を使う文に差し替える） |
| `deleted-chat-backend-days` | where-your-data-goes | #retention | 「バックエンドからは標準の保持期間のうちに消える」 | 表のセルの中の fact の目印（表の行「消した会話」） |
| `training-opt-in-retention-years` | where-your-data-goes | #retention | 「匿名化した形で、学習のパイプラインに長く残る」 | 表のセルの中の fact の目印（表の行「許可した学習の対象」） |
| `violation-retention` | where-your-data-goes | #retention | 「入出力が長く残り、安全の分類のスコアはさらに長く残る」 | 表のセルの中の fact の目印（表の行「利用ポリシーの違反と判定された会話」） |
| `feedback-retention-years` | where-your-data-goes | #retention | 「表の行「フィードバックと報告」の「長く残る」」 | 表のセルの中の fact の目印（表の行「フィードバックと報告」） |
| `local-transcript-cleanup-days` | where-your-data-goes | #local-transcripts | 「既定では一定の期間残す」 | 段落の中の fact の目印（「一定の期間」に） |
| `incognito-retention-period` | where-your-data-goes | #misconceptions | 「シークレットチャットも、学習に使わないだけで、標準の期間は保持される」 | 段落の中の fact の目印（任意。「標準の期間」の具体として。未確認） |
