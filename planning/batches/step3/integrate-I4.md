# 工程3 I4：目次の統合（cli・extend・contest）

- 担当：I4（2026-11-04）
- 共通の指示：[brief-integrate.md](brief-integrate.md)（v1）。材料：`state/step3-integrate/I4-input.md`（A 43件・B 9行）
- 書いたファイル：[cli.yaml](../../catalog/cli.yaml)・[extend.yaml](../../catalog/extend.yaml)・[contest.yaml](../../catalog/contest.yaml)・この報告。registry・features・設計書・ほかの分野のファイルは変えていない。git の操作も Web も使っていない
- ページの id・sections の anchor・priority・level・wave は変えていない。ページの追加・移動・統合・削除もしていない
- 変えたページは25（cli 10・extend 14・contest 1）。どれも notes の末尾に「（2026-11-04 統合：<番号>）」を足した。番号は材料 A の番号、B の行は「B#<行>」、メインの決定は「M<番号>」

## 1. 材料 A の各項目の扱い

| 番号 | 扱い | 変えたページ・反映しないときの理由 |
| --- | --- | --- |
| basics#6 | 反映した | cli/init-and-first-claude-md の prerequisites に where-instructions-sit（basics、整える・必須）を置いた。同じ段で逆転はなく、循環もない。symptoms・app の部分は対象外 |
| surfaces#4 | 取り込み済みを確かめた | cli/using-ides → claude-code-surfaces（前提）、cloud-sessions-and-teleport → where-it-runs（前提）、control-from-phone → where-it-runs（related） |
| models#4 | 取り込み済みを確かめた | extend/writing-subagents の related に effort-levels#subagents-and-org-limits と opusplan がある |
| context#1 | 取り込み済みを確かめた | 受け持ちの3ファイルに、context がまとめた4候補を指す参照はない（notes の文に名前が出るだけ）。sessions-as-branches の行き先は cli/resume-and-branch |
| app#6 | 対象外 | memory-faq を残すかは app と工程4の判断。extend/using-auto-memory は how-memory-works と memory-faq を related で指すので、まとめたときは memory-faq の参照を直す（§7） |
| cli#2 | 対象外 | symptoms（I7）への提案。cli の側の参照（isolate-with-safe-mode → instructions-ignored・seems-less-capable・replies-in-english・blames-the-tools、permission-modes-overview → wrong-amount-of-approvals、checkpoints-and-rewind・recover-lost-work → deleted-something-important）はあり、symptoms の側からも今は指している |
| cli#3 | 取り込み済みを確かめた | cli/usage-context-statusline → what-uses-up-limits#find-what-uses-it（anchor は解決する） |
| cli#4 | 対象外（メインが扱う） | 設計書 §4.2 への提案。cli.yaml の冒頭の注記はこの境界のとおり |
| cli#5 | 取り込み済みを確かめた | cli/when-to-plan の題名は M1 の仮の表記「plan モード」で、aliases に「プランモード」「plan mode」がある。用語集（M7）は start の担当 |
| cli#6 | 対象外 | changes の checking-for-updates への提案。cli/ask-claude-code は checking-for-updates を related で指し、notes に research/22 #3 がある |
| cli#7 | 対象外 | delegate への提案。cli の4ページから delegate のページへの related はある |
| cli#8 | 対象外 | enforce と safety への提案。cli/permission-modes-overview は what-auto-mode-stops・where-bypass-is-ok・sandboxing を related で指す |
| cli#9 | 取り込み済みを確かめた | extend → cli（what-to-put-in-claude-md → init-and-first-claude-md、claude-md-length → init-and-first-claude-md#prune、claude-md-vs-rules-skills-styles → output-style-modes#vs-claude-md）と、cli → extend の両方の向きがある |
| cli#10 | 取り込み済みを確かめた | cli/command-cheatsheet → glossary#old-names |
| extend#1 | 取り込み済みを確かめた | cli/init-and-first-claude-md の参照は what-to-put-in-claude-md に直っている。受け持ちのほかのページにも、まとめた2候補への参照はない |
| extend#2 | 反映しない（cli に残す） | 出力スタイルの機能のページは cli/output-style-modes のままにした。組み込みのスタイルの切り替えの操作が中心で、整えるの段で要る（extend のページは任せる以上）。extend の比較のページと相互に指す形を保ち、判断を output-style-modes の notes に書いた。設計書の境界の表への書き足しは §5 |
| extend#3 | 反映した | extend/writing-subagents の outdated_advice に subagents-to-save-context（M3）を足した。tell-it-to-use-subagents とは出典と中身が違うので両方を指す |
| extend#4 | 取り込み済みを確かめた | extend の claude-md-length・writing-skills・skill-descriptions → measure-changes。例を足すかは eval の担当に任せる |
| extend#5 | 反映した | cli/init-and-first-claude-md の materials に「03 Q2 C6（/init による自動生成の是非の両論）」を足し、notes に両論はこのページが持つと書いた。extend/what-to-put-in-claude-md の notes に、/init は cli が持ち related で指すだけと書いた |
| extend#6 | 対象外 | context への境界の連絡。今の always-on-costs の前提は rereads-whole-history だけで、claude-md-length・pruning-extensions との循環はない |
| extend#7 | 取り込み済みを確かめた | extend の7ページ（connecting-mcp・choosing-mcp-servers・plugins-and-marketplaces・mods・writing-skills・pruning-extensions・code-intelligence-plugins）→ vetting-extensions |
| extend#8 | 対象外 | app への境界の連絡。extend の側の related（how-skills-load → skills-in-the-app、connecting-mcp → connectors-in-the-app、plugins-and-marketplaces → plugins-in-the-app）はある |
| extend#9 | 対象外 | symptoms への提案。extend の側から症状のページへの related はある |
| extend#10 | 対象外 | team への提案。claude-md-length に節 team（anchor `team`）がある |
| extend#12 | 反映しない（工程4へ） | choosing-mcp-servers はそのまま残した。例を出さない形にするか mcp-or-cli にまとめるかは「工程4の見直しで決めてよい」項目で、id が消えるまとめは統合ではしない |
| eval#2 | 取り込み済みを確かめた | contest/running-contest-experiments → measure-changes#by-stratum。symptoms の部分は対象外 |
| eval#4 | 取り込み済みを確かめた | contest の側：evaluators-by-format の前提 verifier-three-conditions（任せる。同じ段のまま）、running-contest-experiments の前提 experiment-log・selection-pressure、A-9 の後半は search-code-checklist の雛形 |
| enforce#1 | 反映した | extend の題名はすでに M1 の表記だった。cli の要約に残っていた skill・hook・plugins などを M1 にそろえた（§3） |
| enforce#5 | 取り込み済みを確かめた | hook-vs-skill → hooks-basics。writing-subagents・what-subagents-dont-inherit → hook-recipes#subagent-only、notes に disallowedTools の注意（research/28 #14）がある |
| enforce#8 | 取り込み済みを確かめた | permission-modes-overview → what-auto-mode-stops・permission-rules、settings-layers → managed-settings-enforcement |
| safety#2 | 反映しない | competition-rules の前提に checking-ai-rules（使う・必須）はある。practice-vs-contest-day には直接置かない：competition-rules を通して推移的に届き、直接の前提だけを書く規則（catalog/README §4.4-1）に従う（C10 の判断を確かめた） |
| delegate#3 | 反映した | cli/permission-modes-overview の related に headless-basics#permissions（-p の権限モードの既定と承認の要る呼び出し）と agent-teams-experimental（teammate がリードの権限モードを受け継ぐか）を足した |
| delegate#7 | 取り込み済みを確かめた | extend/writing-subagents、cli/cloud-sessions-and-teleport・completion-notifications は delegate のページを related で、contest/format-cheatsheet は is-the-task-ai-suited を前提で指す |
| cost#3 | 取り込み済みを確かめた | contest/competition-day-operations → check-billing-path・what-uses-up-limits・when-ai-is-unavailable、cli/usage-context-statusline → what-uses-up-limits#find-what-uses-it |
| japanese#1 | 反映した | まとめた先のページに直っていた参照に節を付けた：extend/writing-skills → less-ai-sounding-japanese#proofreading-skill、hook-vs-skill → less-ai-sounding-japanese#lint-vs-judgment（lint に任せる所と判断の要る所。フックとスキルの対比に当たる） |
| japanese#9 | 反映した | cli/output-style-modes：related を keep-replies-in-japanese#instructions に替え、what-subagents-dont-inherit を足し、notes に「出力スタイルは指示で、fork でないサブエージェントに届かない（research/27 §3.2）」と、japanese と extend にそろえることを書いた。cli/settings-layers：related に keep-replies-in-japanese#language-setting と commit-and-comment-language#override を足した |
| recipes#2 | 対象外 | eval への提案。contest の側の evaluators-by-format → build-test-harness はあり、verifier-three-conditions は任せるのまま |
| team#3 | 取り込み済みを確かめた | cli/settings-layers・cloud-sessions-and-teleport → share-team-settings、extend/what-to-put-in-claude-md → share-team-settings・ai-usage-guidelines、plugins-and-marketplaces → share-team-settings・org-managed-settings-and-mcp、contest/long-team-competitions の前提 separate-roles |
| contest#1 | 取り込み済みを確かめた | competition-rules の前提 checking-ai-rules（safety、使う・必須）。必須の前提は必須で、段の逆転もない |
| contest#2 | 取り込み済みを確かめた | contest がまとめた3候補を指す参照は、全分野にない（全体の検査でエラー0）。recipes・team・delegate の提案は入っている |
| contest#3 | 取り込み済みを確かめた | eval の differential-testing が受けた（A-9 の前半は eval、後半の assert は search-code-checklist）。search-code-checklist の notes の「置く案」を、決まった形に直した |
| contest#4 | 対象外（メインが扱う） | data/facts.yml と設計書 §9.1 への提案 |
| symptoms#4 | 取り込み済みを確かめた | extend/when-to-add-what（任せる）→ repeating-the-same-explanation（整える）は related のまま |

### 1.1 メインの決定（M1〜M11）の扱い

| 決定 | 扱い |
| --- | --- |
| M1 題名の表記 | §3 のとおり。extend と contest の題名と要約はほぼそろっていた。仮の表記は plan モード（cli/when-to-plan の題名）と許可ルール（cli/settings-layers の要約）の2か所で使っている |
| M2 逆引き | §2 のとおり。足すほかに、症状の項目と同じ文のサイン3つを対処のページから外した |
| M3 台帳 | subagents-to-save-context を extend/writing-subagents で指した。styles-for-tone は受け持ちに入れなかった（アプリの Styles の助言で、cli/output-style-modes は Claude Code の別の機能。notes で別の機能と書いてある） |
| M4 機能の id | tracks は変えていない。new_features も足していない（tracks はすべて解決する） |
| M5 断られたとき | cli/isolate-with-safe-mode の materials に「断られたときの切り分けに --safe-mode」（research/26 §3.3 (b)）がある。notes に、使うのは設定に入った引き金（推論の全文を求める指示など）を見つけて外すためで、判定を避けるためではない、と書いた。ほかに断られたときの話を持つページはない |
| M6・M7・M8・M10 | 受け持ちに当たる変更はない（wave は受け持ちの分野にない） |
| M9 比例則 | extend/agents-md：中身は指示ファイルの読み方と共有で、任せる幅を広げない。level は前提の claude-md-loading-order と同じ任せるが合う。notes に理由を書き、警告を残した。extend/how-skills-load：読み込みの仕組みの説明で広げない。level も任せるが合う（同じ手順を仕組みに移すかを判断する段。作るのは仕組みにするの writing-skills）。ただ、補助のスクリプトを中身を読まずに実行する点を書くので、入れる前の確認の safety/vetting-extensions を related の末尾に置いた。これで警告は消えたが、判断は「広げない」のまま notes に書いた |
| M11 生成のページ | cli/command-cheatsheet に印のキーは足していない。notes もそのまま |

## 2. 材料 B の行の扱い

| # | 項目 | 扱い | ページと sign の文 |
| --- | --- | --- | --- |
| 21 | 長い作業を明日も続けたい | 足した | cli/resume-and-branch に `{goal: 長い作業を明日も続けたい}`。既存の「昨日のセッションの続きから再開したい」は止めた後の再開で、続ける前提で区切る場面とは引き方が違うので、両方を置いた。何を書き残すかは context の handoff-documents・progress-files（同じ文がある） |
| 30 | CLAUDE.md が長くなってきた | 種類を直した・足した | extend/claude-md-length の同じ文のサインを symptom → situation にした。extend/path-scoped-rules に `{situation: CLAUDE.md が長くなってきた}` を足した（フォルダごとの規約を外に出すのが直接の答えの一つ） |
| 31 | CLAUDE.md に何を書けばよいか分からない | 足さない | extend/what-to-put-in-claude-md に同じ意味の goal「CLAUDE.md に何を書けばよいか知りたい」がある |
| 32 | 特定のディレクトリだけのルールを書きたい | 足さない | extend/path-scoped-rules に同じ文の goal がある |
| 35 | デプロイ用の skill を勝手に動かされたくない | 足さない | extend/manual-only-skills に同じ意味の goal「デプロイ用の手順を、勝手に動かされたくない」がある |
| 39 | skill と subagent のどちらにすべきか | 種類と文を直した | extend/skill-vs-subagent の symptom「skill と subagent のどちらにすべきか分からない」を、表の種類と文の goal「skill と subagent のどちらにすべきか」に置き換えた（同じ意味なので足してはいない） |
| 40 | MCP を入れるか CLI で済ませるか | 足さない | extend/mcp-or-cli に同じ意味の goal「外部ツールをつなぐか、コマンドで済ませるかを決めたい」がある（題名も「MCP か CLI か」） |
| 41 | 他のエージェントツールと指示を共有したい | 足さない | extend/agents-md に同じ文の goal（表記は「ほかの」）がある |
| 43 | チームで同じ設定を使いたい | 種類を直した | extend/plugins-and-marketplaces の同じ文のサインを situation → goal にした（表と team/share-team-settings と同じ種類） |

M2 の3点目（症状の項目の文を対処のページに重ねない）：

- 既存のサインのうち、症状のページと同じ文の3つを外した。どれも症状のページから対処のページを related で指しているので、振り分けの道は残る
  - #33「同じ手順書を何度も貼っている」：extend/how-skills-load から外した（symptoms/repeating-the-same-explanation が持つ）
  - #34「作った skill が使われない」：extend/skill-descriptions から外した（symptoms/instructions-ignored が持つ）。サインが1つになるので、やりたいことの形の `{goal: 作ったスキルを、使ってほしい場面で確実に使わせたい}` を置いた
  - #42「入れた拡張が多すぎて重い」：extend/pruning-extensions から外した（symptoms/too-slow が持つ）
- catalog-C12 §7 で向く先に受け持ちのページが挙がっていた症状の項目（#2 → when-to-add-what、#33 → how-skills-load・writing-skills、#34 → skill-descriptions、#42 → pruning-extensions、#55 → cli/checkpoints-and-rewind）は、足していない
- extend/when-to-add-what の「同じ注意を何度も繰り返している」は、症状の33項目ではないが enforce/when-to-lock に同じ文が situation である。読者の置かれた状況なので、種類を symptom → situation にそろえた
- 受け持ちのほかの symptom のサイン（サブエージェントの報告だけ英語、圧縮の後にフォルダの規約が効かない、など）は、症状の項目より狭い、そのページに固有の場面なので残した

## 3. 題名を変えたページ（前 → 後）

| ページ | 前 | 後 | aliases |
| --- | --- | --- | --- |
| cli/usage-context-statusline | /usage・/context・status line で状態を見る（nav_title：/usage・/context・status line） | /usage・/context・ステータスラインで状態を見る（nav_title：/usage・/context・ステータスライン） | status line はもとからある |
| extend/using-auto-memory | 自動メモリ（auto memory） | 自動メモリ | auto memory を足した |

要約と節の見出しだけを変えたもの（M1。anchor は変えていない）：

- cli/input-symbols：要約と節 `slash` の skill → スキル
- cli/recover-lost-work：要約と節 `transcripts` の transcript → トランスクリプト（research/27 §3.1）
- cli/usage-context-statusline：要約と節 `statusline` の status line → ステータスライン（features.yaml の statusline の表記）
- cli/isolate-with-safe-mode：要約の skills・plugins・hooks → スキル・プラグイン・フック
- cli/settings-layers：要約の「許可の一覧」→「許可ルール」（M1 の仮の表記）
- cli/output-style-modes：節 `vs-claude-md` の skill → スキル
- cli/completion-notifications：要約の hook → フック

題名・nav_title・要約・節の見出し・章を、M1 と research/27 §3.1 の英語の語で走査し、残りは0件だった。signs と aliases の英語は読者の言葉と別名なので変えていない。

## 4. 新しいページ、priority・level を変えたページ

- 新しいページ：なし
- priority・level を変えたページ：なし（M9 で agents-md と how-skills-load の level を見直したが、どちらも任せるのままにした。理由は §1.1）

## 5. メインへ

1. **設計書 §4.2（出力スタイルの置き場所）**：extend#2 を cli に残すと決めたので、境界の表の「CLAUDE.md・rules・skills・subagents・MCP・plugins（文脈と指示の置き場所）→ extend」の行に、「出力スタイルの機能のページは cli（output-style-modes。切り替えの操作）、置き場所の比べ方は extend（claude-md-vs-rules-skills-styles）」と書き足す案。今の表では extend の持ち物にも読める
2. **逆引きの重複の検査（M2 の3点目、道具への提案）**：症状のページの signs と同じ文が対処のページにあるかを、check_catalog.py の警告にする案（「symptoms のページの symptom のサインと同じ文が、ほかの分野のページにある」）。統合の途中では受け持ちの外にも3件（basics の2ページ・delegate の1ページ）あったが、最後の確認では全分野で0件だった。工程4で signs を足し直すときの戻りを防ぐため
3. **表記（用語集・M7）**：status line（ステータスライン）と transcript（トランスクリプト）を用語集に入れる。status line の公式の日本語版の多数派は research/27 で数えていないので、確かめる。クラウドのセッションは cli の題名が「クラウドセッションと teleport」、features.yaml が「クラウドのセッション」で揺れている（題名は変えていない）。code intelligence の公式の日本語の表記も確かめていない

## 6. 検査の結果

`python3 tools/check_catalog.py --field <field>`（2026-11-04 の最後。分野のファイル23・ページ361）：

| 分野 | 始めの時点 | 最後 |
| --- | --- | --- |
| cli | エラー 0・警告 0 | エラー 0・警告 0 |
| extend | エラー 0・警告 2（比例則：agents-md・how-skills-load） | エラー 0・警告 1（比例則：agents-md） |
| contest | エラー 0・警告 0 | エラー 0・警告 0 |

- 残した警告：extend/agents-md の比例則。任せる幅を広げない内容で、notes に理由を書いた（§1.1 の M9）
- 全体の検査（`python3 tools/check_catalog.py`）：エラー 0・警告 4（すべて比例則。extend の agents-md、api の feature-to-api-mapping・prompt-caching-in-practice、team の ideate-independently。少し前の回では basics の why-prompt-caching を含む5件だった）
- 道具が見ない点も手元のスクリプトで確かめた：題名と同じ aliases はない（cli/output-style-modes の「出力スタイル」は nav_title と同じだが、用語索引で引くために残した）。M1 の語の残りは0件。変えた25ページの notes の末尾に印がある。要約は120字以内（いちばん長いのは isolate-with-safe-mode の102字）。症状のページと同じ文のサインは、受け持ちに残っていない。材料 A の「取り込み済み」と「確認」の参照（約70組）は、すべて今のファイルにあった

## 7. 確かめていないこと、迷った点

- **ステータスライン**：公式の日本語版の本文の多数派は確かめていない（research/27 の29ページに入っていない）。メインの features.yaml の表記と、ほかの語のカタカナの傾向に合わせた。用語集で違うと決まれば、題名・要約・節の見出しを戻す
- **許可ルール**：M1 の仮の表記を cli/settings-layers の要約に使った。工程5で変われば直す
- **B#21 を足したこと**：既存の「昨日のセッションの続きから再開したい」と同じ意味と読めば足さなくてよい。逆引きで context の2ページと同じ項目に並ぶほうが引きやすいと見て足した
- **M2 の3点目を既存のサインにも当てはめたこと**：足すときの規則として書かれているが、理由（逆引きで同じ文が二か所に出ると症状のページの振り分けを飛ばす）は既存のサインにも当てはまると読んだ。外したサインの代わりに skill-descriptions に goal を1つ足したのは私の判断
- **when-to-add-what のサインの種類**：enforce/when-to-lock の今の種類（situation）にそろえた。enforce の担当が同時に変えれば、またずれる
- **how-skills-load の vetting-extensions**：比例則の警告を消すためでなく、補助のスクリプトを読まずに実行する点のために置いた。「広げない内容」という判断は変えていない。警告を残すほうがメインの見方に合うなら、外してよい
- **extend#2（出力スタイル）**：cli に残した。extend に移すなら工程4で、分野をまたぐ移動としてメインが決める
- **extend#12・app#6**：工程4の項目のまま。app が memory-faq を how-memory-works にまとめれば、extend/using-auto-memory の related の memory-faq を直す
- **B#31・#40 の文**：同じ意味のサインがあるので、00 §4 の文にそろえなかった。逆引きの表の文と一致させたいなら、文を置き換えればよい（種類はどちらも goal で同じ）
- **contest**：変えたのは search-code-checklist の notes だけ。M1・M2・M9 に当たるものはなかった
- registry の題名には英語の表記が残る（registry は変えていない。用語集と工程4でそろえる）
- 一次資料は開いていない。表記の判断は research/27 §3.1 と features.yaml による
