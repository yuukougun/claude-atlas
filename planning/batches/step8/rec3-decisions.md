# 推奨R3：メインの判断に上げるもの

| ページ | 件 | 案（推す案を先に） |
| --- | --- | --- |
| command-cheatsheet | 表が手書き（`command-table` の目印がない）。`/skills`・`/hooks`・`/mcp`・`/plugin` の一言は公式の表で未確認 | 暫定で手書きを残し、目印の新設は backlog。一言は公式の表で確かめる担当を付ける。確かめられなければ該当の一言を行き先の題名だけにする |
| github-actions-with-claude | 雛形を載せる方針（カード §10 は載せない、目次と brief は載せる）。題の「最小権限」だが read に絞った効果は未確認 | 目次と brief を優先して 2 つ載せたまま。題は「権限を明示した workflow」へ直す（効果を未確認と書いてあるため） |
| progress-logs-for-long-jobs | 「ログが大きすぎた例」の（根拠：中）に公開の出典がない | 印を（根拠：弱）に直す。出典が取れたら中に戻す |
| postmortems | collins-premortem の「30% は理由の数」を原典で未確認 | 原典を開いて確かめる（担当を付ける）。確かめられなければその一文を削る |
| pairing-and-delegating・record-decisions・grow-review-checklists・build-observation-tools | sources が空で、根拠は（根拠：弱／中）の印だけ（出典は noai の恐れのあるドメインか、URL が束にない） | そのまま残す（rec1・rec2 の先例）。出典の追加は backlog。取れなければ「中」の印を「弱」にそろえる |
| choosing-mcp-servers | 第三者サーバーの名前の表の成熟度が「未確認」 | 表を残す（推薦ではないと本文に明記済み）。各サーバーの確認は backlog |
| choosing-a-plan | 料金の表がない（fact 待ち）。Ultra の量が旧 Max 20x と同じかを匿名で書いた | 料金の fact を入れてから目印を足す（backlog）。匿名の書き方はそのまま |
| cloud-schedules・bare-mode | 強制力が混在か、鍵に近い。冒頭と要点は手書き | 手書きのまま。data への値は backlog（cloud-schedules はなし、bare-mode は鍵） |
| rate-limits-and-errors | 「間隔にばらつきを足す」は公式にない定石で「この辞典の推奨」と明記 | 残す（印があるので十分） |
| share-targets-and-bounds | 要点に標準外の「根拠の強さ」項目 | 残す |
| prompt-patterns | snippets/prompt-patterns/analysis-request.md の Write が止められ、雛形が「準備中」のまま | メインが build-TR-R3.md の案で作り、gen_site --page prompt-patterns で埋める。止め方が作業に合わないなら作者に相談 |
| is-the-task-ai-suited・competition-day-operations | 仮想の場面が束にない／review 指摘 2 の文に出典がない | 仮想の場面は残す。指摘 2 の文は出典が取れなければ削る |

## メインの決め（2026-11-06）

- 直す（目印を置く段の担当に頼む）：progress-logs-for-long-jobs の公開の出典のない（根拠：中）を（根拠：弱）に。postmortems の原典で確かめていない「30% は理由の数」の一文を削る。competition-day-operations の review の指摘2の、出典のない一文を削る
- prompt-patterns の雛形 analysis-request.md は、TR-R3 の案のとおりにメインが置いた（担当の Write が止められたため）
- そのまま：ほかの9行は TR-R3 の推す案のとおり（github-actions-with-claude の雛形は、雛形をなるべく多く載せる決め〔2026-11-04〕で2つとも残す。強制力の値は DM4 が data に入れる）
