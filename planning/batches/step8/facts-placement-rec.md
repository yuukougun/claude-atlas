# 数値の目印を置く場所の一覧（工程8 DM4、推奨のページ）

data/facts.yml に足した facts（64 件）と、既存の id を使う提案（5 件）、強制力を入れた機能（17 件）を、ページの順（id の英字順）に並べた。目印を置くのは後の担当で、DM4 はページ（docs/）を直していない。

- 置き方の記号：fact の目印は `<!-- fact:begin <id> --><!-- fact:end -->`、組は `<!-- gen:begin fact-table <id> -->`〜`<!-- gen:end fact-table <id> -->`、機能の属性は `<!-- gen:begin feature <id>/enforcement -->`〜`<!-- gen:end feature <id>/enforcement -->`。値と決まった文（sentence）と確認日は道具が書く。置いたら `gen_site.py --page <id>` で埋める
- 状態が未確認の fact は、道具が値を出さず「未確認」とだけ書く。該当の行の置き方に「未確認」と書いた。値が出るのは、検証役が確かめて status を確認済みにした後。未確認の目印は、括弧・「は、〜である」の形に置くと、「未確認」が文として読める（build-DM3.md と同じ）
- 「該当の文なし」は、いまのページに値を指す文がなく、近い文に足すか、一文を新設する行。置く担当が本文を直す
- 表の fact は、行の名前に空白があると、セルの inline の目印にできない。表全体は fact-table で置く
- 今回の facts には `match`（目印の外の手書きを見つける型）を付けていない。置くとき、目印の外に同じ値を手で残さない
- 同じ値の合流：cloud-scheduled-task-min-interval（loop-and-scheduling と cloud-schedules の 2 件）、prompt-cache-default-ttl（why-prompt-caching と prompt-caching-in-practice）、prompt-cache-price-multipliers（同）、refusals-billing-by-category（when-requests-are-refused と asking-for-reasoning）。既存の id を使うもの：permission-mode-default-noninteractive（agent-sdk-basics の権限モードの既定）、shared-chat-with-created-files-restriction（shared-artifacts-and-files のファイルを含む会話の公開）、claude-md-on-demand-char-limit（claude-md-loading-order の上限）、artifacts-storage-limit（artifacts-as-apps の保存の上限。確認済みに上げた）、incognito-retention-period（確認済みに上げた。incognito-chats#retention にはすでに目印がある）
- 強制力の行は、要点の手書きがあるページだけ書いた。手書きがない機能（agent-sdk・cloud-sessions・sessions・app-context-management・feedback・cross-session-messaging・projects・usage-credits）は、テンプレートが tracks の先頭の機能のバッジを出すので、目印を足さない（tracks の先頭が別の機能なら、その機能の `feature <id>/enforcement` を要点に足すかを置く担当が決める）

| fact または機能の id | ページ | 節の anchor | 目印を置く文（いまのページの文） | 置き方 |
| --- | --- | --- | --- | --- |
| `agent-sdk-setting-sources-default` | agent-sdk-basics | #setting-sources | 「省いたときに何を読むかは、版で変わりうる。今の公式の文書は、省くと CLI と同じ設定を読むと書いている。」 | 段落の中の fact の目印（「CLI と同じ設定を読む」を目印に。「版で変わりうる」は残す） |
| `permission-mode-default-noninteractive`（既存） | agent-sdk-basics | #permissions | 「権限モードを決めない実行の既定と、承認の要る呼び出しの扱いは、版で変わってきた。」 | 段落の中の fact の目印（既存の id。-p と Agent SDK の既定を値で書く） |
| `agent-view/enforcement` | agent-view-and-background | 冒頭の要点 | 「止められるもの：状態を見て返事をする画面であり、作業の中身は縛らない。縛りは権限とフックで先に置く。」 | feature の目印（なし。手書きの強制力の文を替える） |
| `agents-md-direct-read-min-version` | agents-md | #limits | 「読み込みの設定で AGENTS.md を読む機能は、ある版以降のものである。」 | 段落の中の fact の目印（「ある版」に） |
| `agents-md-direct-read-min-version` | agents-md | #outdated | 「読み込みの設定が入った版と、設定名の変更の経緯は、変わりやすい値なので本文に書かない。」 | 段落の中の fact の目印（版を値で書く文に直す。上の項目と同じ id） |
| `agents-md-instruction-files-default` | agents-md | #choose | 「読み込みの設定に任せるときの初期の動きは、次のとおりだ。」 | 段落の中の fact の目印（初期の値の名前を足す。後続の説明は残す） |
| `agents-md-instruction-files-default` | agents-md | #limits | 「CLAUDE.md が 1 つでもある：初期の設定では、作業ディレクトリかその上に CLAUDE.md か CLAUDE.local.md があると AGENTS.md は読まれない。」 | 段落の中の fact の目印（任意。上の項目と同じ id） |
| `agents-md-plugin-id-rename` | agents-md | #templates | （該当の文なし。雛形の設定の `"cc-plugin-agents-md@builtin"` の前の説明に一文を足す） | 段落の中の fact の目印（雛形の中には置けない。名称の変更なので names に移す案もある） |
| `artifacts-storage-limit`（既存） | artifacts-as-apps | #runtime | 「データを残す：道具を閉じても残るデータを持てる。」 | 段落の中の fact の目印（箇条に上限を足す） |
| `artifact-runtime-plans` | artifacts-as-apps | #runtime | 「アーティファクトが持てる実行時の能力は 3 つある。公式の記事（確認日 2026-11-05）で確かめた内容を、次に分けて書く。」 | 段落の中の fact の目印（「どのプランで使えるか」を値で書く） |
| `artifact-runtime-plans` | artifacts-as-apps | #pitfalls | 「プランで使えないことがある：接続とデータ保存は、使えるプランが限られる。」 | 段落の中の fact の目印（「使えるプランが限られる」の具体に。上の項目と同じ id） |
| `refusals-billing-by-category` | asking-for-reasoning | #refusal | 「出力の前に止まった拒否でも、課金される分類がある。」 | 段落の中の fact の目印（未確認なので「未確認」と出る。「課金される分類がある」を目印を使う文に） |
| `reasoning-extraction-since` | asking-for-reasoning | #refusal | 「推論の全文や決まった形（`<thinking>` の欄、JSON の `reasoning` の欄など）を本文に書かせる指示は、`reasoning_extraction` という拒否の分類に当たる」 | 段落の中の fact の目印（分類が足された日として。未確認） |
| `bare-mode-default-plan` | bare-mode | #pitfalls | （該当の文なし。#pitfalls に「-p の既定は将来 --bare になる予定」の一文を足す） | 段落の中の fact の目印（予定の有無） |
| `setting-sources-leak-fix-version` | bare-mode | #pitfalls | 「外した設定が漏れる古い版：`--setting-sources` で外した設定ファイルの一部が、渡り続ける不具合が過去にあった。」 | 段落の中の fact の目印（「古い版」に直った版を。未確認） |
| `bare-mode-partial-limits-before` | bare-mode | #what-is-skipped | 「システムリマインダー（実行中に Claude へ差し込まれる、状態の変化の通知）」 | 段落の中の fact の目印（MCP・システムリマインダー・バックグラウンドの制限が一部だけだった版を、3 項目のあとの一文に足す） |
| `top-model-by-plan` | before-using-top-model | #which-limit | 「引かれる先は、プランで 4 通りに分かれる。Team と Enterprise では、席の種類（premium seat と standard seat）で分かれる。」 | 段落の中の fact の目印（箇条 4 つを値で置き換える。未確認なので「未確認」と出る。公式同士の食い違いの節（料金のページ・Max と Ultra の記事・最上位のモデルの記事）は残す） |
| `top-model-weekly-share` | before-using-top-model | #which-limit | 「含まれる割合と、各プランの上限の大きさは、このページに書かない。割合は料金のページで」 | 段落の中の fact の目印（割合を値で書く。「書かない」を直す） |
| `top-model-claude-code-min-version` | before-using-top-model | #which-limit | 「最上位のモデルを Claude Code で選ぶには、最低…」 | 段落の中の fact の目印（最低の版の具体に） |
| `chrome-extension-requirements` | browser-control | #claude-in-chrome | 「API キーや長期のトークンで認証しているセッションでは、この連携は有効にならない。`/login` でのログインが要る。」 | 段落の中の fact の目印（要件の一覧に。道具が conflict を「食い違い」として出す） |
| `computer-use-requirements` | browser-control | #computer-use | 「対象のプランと OS は公式の Help Center（確認日 2026-11-05）で確かめ…」 | 段落の中の fact の目印（未確認なので「未確認」と出る） |
| `edit-refuses-non-utf8-since` | character-encodings | #claude-code | 「Claude Code の編集の道具（Edit と Write）は、UTF-8 でないファイルを扱うのが苦手である。変更の記録で 2026-11-03 に確かめた経緯は次のとおり」 | 段落の中の fact の目印（経緯の箇条の Edit の版に。未確認） |
| `write-refuses-non-utf8-since` | character-encodings | #claude-code | （同じ文の経緯の箇条） | 段落の中の fact の目印（経緯の箇条の Write の版に。未確認） |
| `api-credits-eligible-plans-and-amounts` | check-billing-path | #monthly-api-credits | 「対象のプランと月の額は、時期で変わるので本文に書かない。今の対象は上の記事で確かめる。」 | fact-table の組（この段落の後ろ。段落を「下の表のとおり」に直す。未確認） |
| `api-key-env-p-mode-uses-key-without-confirmation` | check-billing-path | #api-key-in-env | 表の行 `claude -p` の「変数があれば、確認なしで必ずその鍵を使う」 | 表のセルの中の fact の目印（未確認。表のセルは「未確認」だけになるので、確認済みになってから替えるのでもよい） |
| `auth-precedence-order` | check-billing-path | #how-the-path-is-chosen | 「順は公式文書の Authentication にあり、2026-11-04 に確かめた」 | 段落の中の fact の目印（順の 7 項目を値で置き換える。未確認） |
| `claude-code-stable-channel-delay` | checking-for-updates | #steps | （該当の文なし。近い文：「latest と stable が今どの版を指すかを見る。」〔コードの注釈〕と、手順 1「手元の版と更新の通り道を控える」） | 段落の中の fact の目印（手順 1 の本文に「stable は latest より遅れる」の一文を足す） |
| `top-model-by-plan` | choosing-a-model | #plans | 「上位のモデルの扱いはプランで違う：枠に含まれるか、追加の支払いから引かれるかが、プランによって違う。」 | 段落の中の fact の目印（任意。before-using-top-model と同じ id。未確認） |
| `top-model-by-plan` | choosing-a-plan | #plan-table | 「上位のモデルの扱い：最上位のモデルは、プランによって、枠に含まれるか usage credits から引かれるかが違う。」 | 段落の中の fact の目印（任意。同じ id。未確認） |
| `plan-prices-individual` | choosing-a-plan | #plan-table | 「月額：表にない。月額と、年払いが選べるかは、プランで違う。Plans & pricing で確かめる。」 | fact-table の組（#plan-table の表の直後。「表にない」を直す。未確認） |
| `claude-md-import-max-hops` | claude-md-loading-order | #import | 「取り込みは入れ子にでき、上…」 | 段落の中の fact の目印（入れ子の上限の段数に） |
| `claude-md-on-demand-char-limit`（既存） | claude-md-loading-order | #limits | 「後から読まれる分には大きさの上限がある：サブフォルダの CLAUDE.md や、後から読まれる rules が上限を超えると、先頭だけが渡る。」 | 段落の中の fact の目印（既存の id。上限の値を表で足す。DM3 が path-scoped-rules に fact-table を置いた id と同じ） |
| `cloud-scheduled-task-min-interval` | cloud-schedules | #triggers | （該当の文なし。近い文：「時刻：`/schedule` の依頼は、時刻を自然な文で書ける。ちょうど正時に置くと数分遅れることがある。」） | 段落の中の fact の目印（箇条「時刻」に最小の間隔を足す。loop-and-scheduling と同じ id） |
| `scheduled-tasks-plans` | cloud-schedules | #triggers | （該当の文なし。#triggers の冒頭に使えるプランの一文を足す） | 段落の中の fact の目印（使えるプラン） |
| `scheduled-tasks-github-lapse` | cloud-schedules | #pitfalls | 「GitHub の接続が切れると、実行は飛ばされ、長く戻らないとタスクが止まる。」 | 段落の中の fact の目印（「長く戻らない」に期間を） |
| `scheduled-tasks-schedule-warning-version` | cloud-schedules | #least-privilege | 「連携先。作るときは、自分につないである連携先がすべて付く。」 | 段落の中の fact の目印（警告が出るようになった版を足す。未確認） |
| `scheduled-tasks-run-history-question-version` | cloud-schedules | #success-and-results | 「使える版は公式で確かめる。」 | 段落の中の fact の目印（「使える版」に） |
| `code-intelligence/enforcement` | code-intelligence-plugins | 冒頭の要点 | 「強制力：Claude に何かを禁じる機能ではない。診断は編集の後に自動で返り、シンボルの検索は読み取り専用の道具である。」 | feature の目印（手書きの文を替える。冒頭を目印にし、補足は残す） |
| `workflow-large-warning` | dynamic-workflows | #when-and-start-small | 「進捗の行に `Large workflow` の警告が出る場合がある。担当の数が多いか、トークンの見込みが大きいときである。」 | 段落の中の fact の目印（「担当の数が多いか」の具体に） |
| `workflow-concurrent-agents` | dynamic-workflows | #when-and-start-small | （該当の文なし。#when-and-start-small に同時に動かせる担当の数の一文を足す） | 段落の中の fact の目印 |
| `workflow-agent-caps` | dynamic-workflows | #when-and-start-small | （該当の文なし。同上） | 段落の中の fact の目印 |
| `workflow-size-guideline` | dynamic-workflows | #when-and-start-small | （該当の文なし。同上） | 段落の中の fact の目印 |
| `workflows/enforcement` | dynamic-workflows | 冒頭の要点 | 「止められるもの：担当の道具の呼び出しには、権限ルールとサンドボックスが効く。規模の警告は助言で、実行を止めない。」 | feature の目印（なし。「止められるもの」の行に添える） |
| `insights/enforcement` | insights-and-usage-review | 冒頭の要点 | 「強制力：なし。報告と内訳を見せるだけで、見ても設定と動作は変わらない。」 | feature の目印（手書きの「なし」を替える） |
| `loop-recurring-expiry-days` | loop-and-scheduling | #loop | 「繰り返しの期限は、作ってから一定の日数で切れる。期限の日数は変わりうるので、公式の文書で確かめる。」 | 段落の中の fact の目印（「一定の日数」に。「確かめる」は残すか削る） |
| `loop-max-tasks-per-session` | loop-and-scheduling | #loop | （該当の文なし。#loop の制約の箇条に足す） | 段落の中の fact の目印 |
| `loop-self-paced-interval-range` | loop-and-scheduling | #loop | 「依頼だけ：`/loop check the deploy`：反復のたびに、Claude が次の間隔を決める」（表の行）／「間隔を省いた形は、状態が変わらないと長めに待つ。」 | 段落の中の fact の目印（「長めに待つ」の範囲に） |
| `loop-min-interval` | loop-and-scheduling | #where-to-run | 「間隔の下限と失効の日数は、方式ごとに違う。クラウドは下限が最も長い。数値は変わりうるので、公式の文書で確かめる。」 | 段落の中の fact の目印（/loop の下限として。次の 2 項目と同じ文） |
| `desktop-scheduled-task-min-interval` | loop-and-scheduling | #where-to-run | （同じ文） | 段落の中の fact の目印（Desktop の下限として） |
| `cloud-scheduled-task-min-interval` | loop-and-scheduling | #where-to-run | （同じ文） | 段落の中の fact の目印（クラウドの下限として。cloud-schedules と同じ id） |
| `model-prompting-tendencies` | model-quirks | #official-guidance | 「公式はモデルごとのプロンプトの指針を出しており、モデルと effort の組ごとに出やすい偏りを挙げている。」 | fact-table の組（モデル × 偏りと対処。いまの表は「偏りの種類」ごとの形なので、置き換えか併記かを置く担当が決める。未確認なので「未確認」と出る） |
| `output-style-concise-min-version` | output-style-modes | #built-in | 「Concise は新しい組み込みで、古い版の Claude Code にはない。使えるか迷うときは版を確かめる。」 | 段落の中の fact の目印（「新しい」を版に） |
| `output-style-command-min-version` | output-style-modes | #switch | 「`/output-style <名前>`：その場で切り替える。…新しい版が要る。」 | 段落の中の fact の目印（「新しい版」に） |
| `output-style-setting-case-sensitive` | output-style-modes | #switch | 「設定ファイルの `outputStyle`：値を直接書く。大文字小文字を区別するので、`Explanatory` と書く。」 | 段落の中の fact の目印（「区別する」に。値は文字列「区別する」） |
| `plugins/enforcement` | plugins-and-marketplaces | 冒頭の要点 | 「止めるもの：プラグインは道具を束ねて配るだけで、何も止めない。」 | feature の目印（「止めるもの」の行の頭に「強制力：」として。手書きの「何も止めない」を替える） |
| `monitor-default-deadline` | progress-logs-for-long-jobs | #steps | 「見張りには期限があり、期限が来ると見張りは終わって、Claude には 1 回だけ知らせが来る。まだ要るなら張り直させる。」 | 段落の中の fact の目印（「期限」に既定を。次の 2 項目と同じ文） |
| `monitor-max-deadline` | progress-logs-for-long-jobs | #steps | （同じ文） | 段落の中の fact の目印（対話の上限として） |
| `monitor-print-mode-max-deadline` | progress-logs-for-long-jobs | #steps | （同じ文） | 段落の中の fact の目印（-p の上限として） |
| `monitor-min-version-restricted-envs` | progress-logs-for-long-jobs | #steps | 「Claude Code では、Monitor の道具が、背景のコマンドの出力を 1 行ずつ Claude に返す。」 | 段落の中の fact の目印（提供経路・通信の抑制の環境変数があるときの最低の版として、この項目に足す） |
| `prompt-cache-default-ttl` | prompt-caching-in-practice | #pitfalls | 「しばらく間を空けると読み取りが 0 に戻る：キャッシュの寿命が切れている。寿命は使うたびに延びるので」 | 段落の中の fact の目印（既定の寿命を足す） |
| `prompt-cache-min-length` | prompt-caching-in-practice | #pitfalls | 「書き込みと読み取りがどちらも 0 のまま：区切りの前の長さが、モデルの最小の長さに届いていない可能性がある。」 | 段落の中の fact の目印（「最小の長さ」に。未確認） |
| `prompt-cache-price-multipliers` | prompt-caching-in-practice | #breakpoints | 「区切りの数には上限がある。上限と、キャッシュの寿命、書き込みと読み取りの料金の倍率、キャッシュできる最小の長さは、モデルによ…」 | 段落の中の fact の目印（「料金の倍率」に。why-prompt-caching と同じ id） |
| `prompt-cache-max-breakpoints` | prompt-caching-in-practice | #breakpoints | （同じ文） | 段落の中の fact の目印（「区切りの数の上限」に。未確認） |
| `block-writes-outside-min-version` | protected-paths | #outside-working-directory | 「キーが入ったのは比較的新しい版なので、手元の版が古いと効かない。手元の版で使えるかは、公式の変更履歴で確かめる。」 | 段落の中の fact の目印（「比較的新しい版」に。「提案済み」の文があれば消す） |
| `sdk-auto-retry-default` | rate-limits-and-errors | #retry | 「SDK の自動の再試行の回数と、Claude Code の自動の再試行の回数は、変わりやすい既定である。回数は公式の文書で確かめ」 | 段落の中の fact の目印（SDK の回数として） |
| `claude-code-auto-retry-default` | rate-limits-and-errors | #retry | （同じ文） | 段落の中の fact の目印（Claude Code の回数として） |
| `claude-code-auto-retry-default` | rate-limits-and-errors | #in-claude-code | 「一時的な 429 は、Claude Code が自動で再試行する。再試行の回数と間隔の既定は、変わりやすいので公式の errors のページで確かめる。」 | 段落の中の fact の目印（「回数と間隔の既定」に。上の項目と同じ id） |
| `chat-sharing-plans` | shared-artifacts-and-files | #who-can-see | 「プランごとの可否、期間、上限の数は変わりやすい。契約しているプランで何が使えるかは、公式の共有の記事で確かめる。」 | fact-table の組（箇条「招待」「公開リンク」の前後。箇条の「全プランで使える」「個人向けのプランだけ」を表に替える） |
| `chat-sharing-invite-expiry` | shared-artifacts-and-files | #who-can-see | 「招待：全プランで使える。開かれない招待は一定の期間で切れる。1 日に招待できる人数にも上限がある。」 | 段落の中の fact の目印（「一定の期間」に。未確認。1 日の人数は材料にない） |
| `shared-chat-with-created-files-restriction`（既存） | shared-artifacts-and-files | #who-can-see | 「ファイルを含む会話の公開：コードの実行とファイル作成で作ったファイルを含む会話は、個人向けのプランでは公開リンクで共有できない」 | 段落の中の fact の目印（既存の id。files-and-code-execution で使う id と同じ） |
| `btw/enforcement` | side-questions-btw | 冒頭の要点 | 「強制力：なし。質問の道を別に用意するだけで、Claude のふるまいを縛る機能ではない。」 | feature の目印（手書きの「なし」を替える。id は `feature btw/enforcement`） |
| `opusplan-alias-mapping` | split-models-by-role | #patterns | 「Claude Code には `opusplan` というエイリアスがある。plan mo…」 | 段落の中の fact の目印（割り当ての一文を値に） |
| `message-threads-lifetime` | stateless-messages-api | #message-threads | 「スレッドの寿命は短い：最後の要求から短い時間でスレッドが切れ、最後に使ってから一定の時間以内に消える。」 | 段落の中の fact の目印（「短い時間」「一定の時間」を値で。未確認） |
| `tool-choice-default` | tool-use-loop | #forcing | 「`tool_choice` が auto のとき、Claude はターンごとに道具を呼ぶか直接答えるかを判断する。」 | 段落の中の fact の目印（既定の値 auto に） |
| `usage/enforcement` | usage-context-statusline | 冒頭の要点（または #limits） | 「見るだけで、止めない：ステータスラインと /usage は、使用量を抑えない。作業を止める力はなく、強制力は持たない道具である。」（末尾の節の箇条） | feature の目印（「強制力は持たない」を替える。要点には強制力の行がない） |
| `usage-credits-expiry-japan` | usage-credits-basics | #how-it-works | 「購入した分には失効の期限がある。日本などでは、ある日付以降の購入分が、一定の期間で失効する。」 | 段落の中の fact の目印（「ある日付」「一定の期間」に。未確認） |
| `auto-memory-default-local` | using-auto-memory | #usage | 「セッションの中で `/memory` を開く。CLAUDE.md の場所の一覧、自動メモリのオンとオフの切り替え、自動メモリのフォルダを開く選択肢が出る。」 | 段落の中の fact の目印（手順 1 の前に「既定の状態」の一文を足す。ローカルのセッションの既定） |
| `research/enforcement` | using-research | 冒頭の要点 | 「強制力：リサーチは調べる機能で、範囲や出典の条件は依頼に書くお願いである。」 | feature の目印（手書きの「お願い」を替える） |
| `verify-skill/enforcement` | visual-checks | 冒頭の要点 | 「強制力：`<!-- gen:begin feature verify-skill/enforcement -->—<!-- gen:end ... -->`（値は数値ファイルの登録待ち）。確かめる手段を渡すだけ」 | feature の目印（すでにある。`gen_site.py --page visual-checks` で「お願い」が入る。「値は数値ファイルの登録待ち」の括弧を外す） |
| `feedback-transcript-share-retention-months` | what-feedback-sends | #what-is-sent | 「記録の共有：評価の後に、記録を見てよいかを聞かれる。ここで Yes を選んだときだけ、記録が送られる。」 | 段落の中の fact の目印（共有した記録の最長の保持期間を足す。未確認） |
| `refusals-auto-switch-default` | when-requests-are-refused | #by-surface | 「自動の切り替え：リクエストに `fallbacks` を設定して使う。」 | 段落の中の fact の目印（面ごとの既定。アプリと Claude Code の項目にも同じ id。未確認） |
| `refusals-cc-per-category-switch-min-version` | when-requests-are-refused | #by-surface | 「サイバーの分類：別の表示になり、検証の制度へのリンクが付く。自動の切り替えがあるモデルでは表示の文が違い」 | 段落の中の fact の目印（分類ごとの切り替えが要る版を足す。未確認） |
| `refusals-api-categories` | when-requests-are-refused | #by-surface | 「拒否の形：拒否はエラーではなく、HTTP 200 の普通の応答である。`stop_reason` が `refusal` になり、`stop_details.category` が分野を示す。」 | 段落の中の fact の目印（分野の値の一覧に。未確認） |
| `refusals-billing-by-category` | when-requests-are-refused | #by-surface | 「課金：拒否の課金の扱いは分野で違い、何度か変わった。出力の前に止まっても課金される分類がある。」 | 段落の中の fact の目印（asking-for-reasoning と同じ id。未確認） |
| `refusals-cvp-tiers` | when-requests-are-refused | #official-steps | 「サイバーは Cyber Verification Program がある。個人で申し込める範囲は変わるので」 | 段落の中の fact の目印（段階と個人の範囲に。未確認） |
