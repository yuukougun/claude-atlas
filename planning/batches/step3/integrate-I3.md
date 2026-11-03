# 工程3 統合 I3 の報告：prompting・japanese・context

- 日付：2026-11-04
- 共通の指示：[brief-integrate.md](brief-integrate.md)（v1）
- 材料：`state/step3-integrate/I3-input.md`（A：open_issues 50件、B：逆引き5行）
- 書いたファイル：`planning/catalog/prompting.yaml`・`japanese.yaml`・`context.yaml` と、この報告。ほかのファイルは変えていない。git の操作も Web も使っていない
- 変えたページ：21（prompting 7・japanese 4・context 10）。変えたページの notes の末尾に「（2026-11-04 統合：…）」を足した
- 変えていないもの：ページの id、sections の anchor、priority、level、wave、prerequisites、ページの数と内訳（prompting 24・japanese 11・context 15）、各ファイルの open_issues（open-issues.md の元の記録なので残した）

## 1. 材料 A の扱い

| 番号 | 扱い | 変えたページ／反映しない理由 |
| --- | --- | --- |
| basics#1 | 取り込み済みを確かめた | japanese の can-i-prompt-in-japanese は basics の tokens を前提にし、節 tokens が日本語の量・費用と上限への効き方・数え方の本体を持つと notes にある（more-tokens-in-japanese はここにまとめ済み） |
| basics#2 | 反映した | context/promises-after-compaction：節 what-comes-back の題を「読み直される場所と、要約に溶ける約束」にし（anchor は同じ）、notes に「移し方（CLAUDE.md・rules・フック）に絞り、残るもの・消えるものの一覧は what-survives-compaction に一本化して繰り返さない」を足した。context/compact-and-auto-compact：notes に同じく一覧を繰り返さないことを足した。両ページが what-survives-compaction を前提に、when-to-lock#spoken-rules-fade を関連に持つのは確かめた |
| basics#7 | 取り込み済みを確かめた | prompting/long-context-first の前提は attention-budget（必須・使う）だけで、lost-in-the-middle（推奨）は related にある |
| models#4 | 取り込み済みを確かめた | emphasis-words・does-double-check-work → after-switching-models、suggest-or-do・state-the-scope・output-shape・does-double-check-work → model-quirks、compact-and-auto-compact・tidy-the-desk → 1m-context。emphasis-words → model-quirks は prompting#4 で足した |
| prompting#1 | 対象外（相手側への提案） | 対処の本体は safety の when-requests-are-refused、入口は symptoms の refused-or-blocked で、どちらも相互に指している。prompting は本体を持たない。give-reasons・asking-for-reasoning から when-requests-are-refused を指していること、受け持ちの3分野に「モデルを変える」を手段として書いた所がないこと（M5）を確かめた |
| prompting#2 | 反映した | context/handing-long-documents：summary を資料の形と量（分ける・テキストや Markdown に直す）を言う形に書き換え、notes に境界（並べ方・答えの前に引用を抜かせること・原文か要約かは long-context-first。quotes-first の節は要点と案内だけ）を足した。related の long-context-first はすでにあった |
| prompting#3 | 取り込み済みを確かめた | context/rewind-dont-correct の related に refine-in-conversation がある |
| prompting#4 | 反映した | prompting/emphasis-words の related に model-quirks を足した（強い言い方が過剰に効く癖）。after-switching-models の見直しの項目（emphasis-words・does-double-check-work）は models の側で入っている |
| prompting#5 | 取り込み済みを確かめた | does-double-check-work の前提は evidence-not-reports。verify の側の evidence-not-reports → does-double-check-work、define-done → four-specifics・ask-for-outcomes も入っている |
| prompting#6 | 対象外 | judgment の側。think-before-asking → ask-for-options は入っている |
| prompting#7 | 対象外 | recipes の側。spec-first → let-claude-ask、write-docs → requesting-prose は入っている |
| prompting#8 | 取り込み済みを確かめた | prompt-patterns・before-after-prompts・refine-in-conversation・share-targets-and-bounds は measure-changes を指す。measure-changes の例（eval の側）は eval#4 で取り込まれた |
| prompting#9 | 対象外 | 台帳 important-caps の「今どうするか」と時期は changes の側。emphasis-words の notes に時期の書き方がある |
| prompting#10 | 取り込み済みを確かめた | prompting のページは lower-temperature を指していない |
| context#1 | 取り込み済みを確かめた | 受け持ちの3分野に、まとめた4候補（managing-context-in-the-app ほか）を指す参照はない。全体の検査でも参照のエラーは0 |
| context#2 | 対象外 | symptoms の側。forgets-in-long-chats・going-in-circles → when-to-start-fresh・rewind-dont-correct・handoff-documents、forgot-after-compaction → promises-after-compaction・compact-and-auto-compact#idle-compaction は入っている |
| context#3 | 対象外 | basics の what-survives-compaction の側。compact-and-auto-compact と promises-after-compaction がこのページを前提にしているのは確かめた |
| context#4 | 反映した（notes だけ。M8） | context/inspect-context の notes の「動く図を自作するかは open_issues」を、M8（basics の rereads-whole-history の動く図は、執筆のときに公式の図と比べて決める。目次の visual は変えない）に書き換えた。visual と tidy-the-desk は変えていない |
| context#6 | 取り込み済みを確かめた | compact-and-auto-compact・promises-after-compaction → when-to-lock#spoken-rules-fade（anchor は enforce にある） |
| context#7 | 取り込み済みを確かめた | tidy-the-desk の related に using-projects・how-memory-works・long-chat-limits・where-to-put-instructions がある。app の側は tidy-the-desk#in-the-app を指している |
| context#8 | 取り込み済みを確かめた | progress-files ↔ progress-logs-for-long-jobs は related で結ばれている |
| context#9 | 取り込み済みを確かめた | when-to-start-fresh → how-usage-limits-work、always-on-costs → what-uses-up-limits |
| app#4 | 反映した | japanese/keep-replies-in-japanese：materials に research/27 #15 を足し、notes に「claude.ai には返答の言語を固定する設定がなく指示で頼むしかないので、app-and-api の節のアプリのタブから where-to-put-instructions を指す」を足した（related にはすでにあった） |
| cli#3 | 取り込み済みを確かめた | inspect-context → what-uses-up-limits#find-what-uses-it |
| cli#4 | 対象外（メイン） | 設計書 §4.2 の書き足しはメイン。context の when-to-start-fresh・compact-and-auto-compact が /clear・/compact の判断と操作を持つ形は変えていない |
| extend#3 | 反映した（M3） | context/research-in-subagents の outdated_advice の先頭と、context/tidy-the-desk の outdated_advice に subagents-to-save-context を足した（tidy-the-desk の四つの動作の「委任」を、コンテキストを守るためと書かないことも notes に足した）。extend の writing-subagents の側も入っている |
| extend#6 | 反映した（notes だけ） | context/always-on-costs の notes に「extend の claude-md-length・pruning-extensions がこのページを前提にするので、このページの前提に extend のページを足すときは循環に気をつける」を足した。前提は変えていない |
| verify#2 | 取り込み済みを確かめた | does-double-check-work の outdated_advice は add-double-check、permission-to-stop の related に protect-tests |
| eval#2 | 取り込み済みを確かめた | 受け持ちに stratified-and-worst-case への参照はない。misses-broken-evaluation は symptoms の側 |
| eval#4 | 反映した | japanese/keep-replies-in-japanese の related に measure-changes を足した（measure-changes が keep-replies-in-japanese#measure を指すので、相互にした） |
| enforce#2 | 反映した | prompting/state-the-scope の notes が、まとめられた spoken-prohibitions-fade（「会話で言った禁止事項のページ」）へのリンクを予定していたのに related になかったので、related に when-to-lock#spoken-rules-fade を足し、notes をまとめた先の名前に直した。context の2ページはすでに指している |
| enforce#6 | 取り込み済みを確かめた | textlint-hook の前提に hooks-basics、related に writing-safe-hooks、materials に research/28 #17 |
| safety#1 | 対象外 | symptoms・safety の側。prompting は対処の本体を持たないので、when-requests-are-refused を merged にする条件に当たらない |
| cost#3 | 取り込み済みを確かめた | can-i-prompt-in-japanese#tokens（anchor あり）、inspect-context → what-uses-up-limits#find-what-uses-it |
| japanese#1 | 対象外 | basics・extend の側。writing-skills → less-ai-sounding-japanese#proofreading-skill、hook-vs-skill → #lint-vs-judgment は入っており、参照のエラーはもうない |
| japanese#2 | 対象外（メイン・symptoms） | replies-in-english の診断の順は symptoms の側。keep-replies-in-japanese は整える（前提に置いても逆転しない）ことを確かめた |
| japanese#3 | 対象外 | basics の tokens の側（いまは can-i-prompt-in-japanese を anchor なしで指す）。can-i-prompt-in-japanese の notes は basics#1 の分け方に揃っている |
| japanese#4 | 対象外 | enforce の側。stop-hooks → keep-replies-in-japanese#stop-hook、hook-recipes → textlint-hook は入っている |
| japanese#5 | 反映した（こちらの側だけ） | japanese/consistent-politeness の related に skills-in-the-app#migrated-styles を足し、notes に移された Styles の書き方を app の where-to-put-instructions（節 styles）・skills-in-the-app（節 migrated-styles）に揃えると書いた。where-to-put-instructions を前提にはしていない（§7） |
| japanese#6 | 反映した（M3） | 台帳 styles-for-tone を japanese/align-japanese-output・consistent-politeness の outdated_advice に足した。think-hard-keywords の一次資料は changes の側 |
| japanese#7 | 対象外 | safety の側。disclosure-and-provenance ↔ less-ai-sounding-japanese は相互に入っている |
| japanese#8 | 反映した | eval#4 と同じ（keep-replies-in-japanese → measure-changes） |
| japanese#9 | 対象外 | cli の output-style-modes・settings-layers の側 |
| recipes#4 | 取り込み済みを確かめた | let-claude-ask（A-6）と prompt-patterns（A-8）の notes に、雛形は snippets の1か所に置いて取り込むと書いてある |
| recipes#9 | 取り込み済みを確かめた | documents-in-japanese → write-docs・research-and-reports、character-encodings → office-paperwork |
| team#3 | 取り込み済みを確かめた | progress-files の related に team の record-decisions がある |
| symptoms#2 | 取り込み済みを確かめた | keep-replies-in-japanese は整えるで、stop-hook の節は sections の level で仕組みにする |
| symptoms#3 | 取り込み済みを確かめた | four-specifics の notes は4点を公式の Best practices に拠らせ、研究の結論とは書かない。aliases に Write a specific prompt |
| symptoms#6 | 反映した | prompting/asking-for-reasoning の materials に research/26 #7 を足した（課金の注意は notes にすでにあった）。refused-or-blocked ↔ when-requests-are-refused は入っている |
| symptoms#8 | 反映した | context/always-on-costs の related に too-slow を足した。effort-levels・fast-mode-and-advisor の側は入っている |

注：M3 の台帳の2項目を付けたページは次のとおり。subagents-to-save-context は context の research-in-subagents・tidy-the-desk。styles-for-tone は japanese の align-japanese-output・consistent-politeness と、prompting の output-shape（提案にはないが、アプリの Styles が長さと形式を切り替える旧い手段なので、M3 の「関わるページ」とみた。notes に今の置き場所〔いつもなら Claude への指示、場面ごとならスキル〕を書き、related に where-to-put-instructions#styles を足した）。

## 2. 材料 B の扱い

| # | 項目 | 扱い |
| --- | --- | --- |
| 11 | 推論の過程を全部見せてほしい | 足さなかった。asking-for-reasoning に同じ意味の goal「なぜその答えになったのか、過程を全部見せてほしい」がある |
| 19 | どのタイミングで新しい会話にすべきか分からない | 足さなかった。when-to-start-fresh に goal「どのタイミングで新しい会話にすべきか知りたい」がある |
| 21 | 長い作業を明日も続けたい | context/progress-files に goal「長い作業を明日も続けたい」を足した。handoff-documents には同じ文がすでにある。どちらも直接答える続け方（一度の引き継ぎと、進捗の外部記憶）なので、逆引きで並ぶようにした。progress-files の既存の「何日もかかる作業の状態を、会話の外に持ちたい」は手段に寄った言い方なので、別の sign とみた |
| 22 | ちょっとした質問で本筋を汚したくない | 足さなかった。side-questions-btw に同じ文がある |
| 23 | 何がコンテキストを占めているか知りたい | inspect-context に同じ文がある。always-on-costs には足さなかった。直接答えるのは /context の内訳を読む inspect-context で、always-on-costs はその related の先頭から届く |

### 2.1 M2 に合わせて外した sign

M2 の「対処のページに同じ文を重ねて置かない」に合わせ、受け持ちの対処のページの signs のうち、症状のページの signs と同じ文のもの（7件）と、00 §4 の同じ項目をほぼそのまま言い換えたもの（3件）を外した。どの症状のページも、外した先のページを前提か関連で指している（choose-what-to-read だけは間接。§5 の2）。

| ページ | 外した sign | 同じ文を持つ症状のページ（00 §4 の番号） |
| --- | --- | --- |
| prompting/brief-a-new-colleague | 「いい感じに」と頼むと平凡なものが返ってくる | not-what-i-meant（#3。言い換え） |
| prompting/four-specifics | 頼んだものと違うものが出てくる | not-what-i-meant（#1） |
| prompting/suggest-or-do | 提案だけで止まり、実行してくれない | keeps-stopping（#4） |
| prompting/state-the-scope | 頼んでいない機能やファイルが増える | does-more-than-asked（#5） |
| prompting/output-shape | 回答が長すぎる・短すぎる | not-what-i-meant（#12） |
| japanese/consistent-politeness | です・ますとだ・であるが混ざる | inconsistent-japanese-style（#15） |
| japanese/consistent-notation | 「サーバー」と「サーバ」が混在する | inconsistent-japanese-style（#16） |
| context/tidy-the-desk | 会話が長くなると答えの質が落ちる気がする | forgets-in-long-chats（#17。言い換え） |
| context/choose-what-to-read | 大量のログやテスト出力で会話が埋まる | forgets-in-long-chats（#24。症状のページは「埋まっていく」） |
| context/always-on-costs | 入れた拡張が多すぎて重い | too-slow（#42） |

## 3. 題名を変えたページ（M1）

- context/always-on-costs：「常駐するもののコスト（CLAUDE.md・MCP・skills）」→「常駐するもののコスト（CLAUDE.md・MCP・スキル）」。英語の語を含む旧題を aliases の先頭に置いた
- context/research-in-subagents：「出力の多い調査は subagent に任せて要約だけ受け取る」→「出力の多い調査はサブエージェントに任せて要約だけ受け取る」。nav_title「調査を subagent に任せる」→「調査をサブエージェントに任せる」。英語名を含む別名（「調査は subagent に任せて要約だけ受け取る」「Explore subagent」）がすでに aliases にあるので、足していない

要約を変えたページ：

- context/promises-after-compaction（M1）：「deny や hook に移す」→「拒否ルールやフックに移す」
- context/always-on-costs（M1）：「skill の説明」→「スキルの説明」
- context/handing-long-documents（prompting#2）：「先に関係する箇所を引用として抜き出させてから答えさせ、必要なら分けたりテキストに直したりして渡す」→「分けたり、テキストや Markdown に直したりして、形と量を整えてから渡す」（2文目は同じ）

節の題を変えたもの（anchor は同じ）：promises-after-compaction の what-comes-back（basics#2）と caveats（skill → スキル）、side-questions-btw の which（subagent → サブエージェント）。

prompting と japanese の題名と要約には、M1 の表で揃える語がなかった（textlint-hook はすでに「フック」）。signs は読者の言葉なので変えていない。

## 4. 新しいページ、priority・level を変えたページ

なし。

## 5. メインへ

1. **M2 の重なり（受け持ちの外）**：対処のページの signs に症状のページと同じ文があるものが、私の検査の時点で受け持ちの外に16件ある。app 5（where-to-put-instructions「毎回同じ背景を説明している」、how-memory-works「別のプロジェクトの記憶が混ざる」、memory-faq「会話を消したのに覚えている」「別のプロジェクトの記憶が混ざる」、how-attachments-are-read「長い PDF の後半の図について答えられない」）、basics 3（context-rot「会話が長くなると精度が落ちる」、knowledge-cutoff「最近の出来事や新しい版について間違える」、sycophancy「こちらの誤った指摘にも、すぐ同意する」）、extend 3（how-skills-load「同じ手順書を何度も貼っている」、skill-descriptions「作った skill が使われない」、pruning-extensions「入れた拡張が多すぎて重い」）、verify 3（evidence-not-reports「「全部通りました」と言うが、信用できない」、checking-citations「もっともらしいが、出典が怪しい」、protect-tests「テストのほうを書き換えて通された」）、delegate 1（humans-set-the-parallel-limit「並列にしたら疲れた」）、safety 1（destructive-commands「ファイルを消された・消されそうで怖い」）。受け持ちでは §2.1 のとおり外した。全分野で揃えるか、言い回しの近いもの（§7 の1）も同じ文とみるかを決めてほしい
2. **symptoms への道（I7 へ）**：§2.1 で choose-what-to-read から「大量のログやテスト出力で会話が埋まる」を外したので、症状の forgets-in-long-chats から出力を絞る節への直接の道がない（いまは research-in-subagents の related を経て届く）。forgets-in-long-chats の related に `choose-what-to-read#trim-output` を足してほしい

## 6. 検査の結果

最後に走らせた結果（分野のファイル 23・ページ 361 を読んだ時点）：

- `python3 tools/check_catalog.py --field prompting`：エラー 0、警告 0
- `python3 tools/check_catalog.py --field japanese`：エラー 0、警告 0
- `python3 tools/check_catalog.py --field context`：エラー 0、警告 0
- 全体：エラー 0、警告 4（どれも比例則で、M9 の受け持ちの外のページ。ほかの担当の作業で減っている途中）

残した警告はない。

## 7. 確かめていないこと、迷った点

1. **M2 の線引き**：00 §4 の33項目と同じ文か、ほぼそのままの言い換えだけを外した。言い回しが違い、対処のページに固有の面を言うものは残した：keep-replies-in-japanese「ツールを使った直後の一言だけ英語で出る」（replies-in-english「ツールの結果を読んだ後の一言だけ英語になる」）と「日本語で話しているのに、途中から返事が英語になる」（「途中から英語に切り替わって戻らない」）、consistent-politeness「途中から文体が変わる」（inconsistent-japanese-style「指定した文体が長い文章の途中で崩れる」）、less-ai-sounding-japanese「日本語の文章が「AI っぽい」定型の言い回しばかりになる」（not-what-i-meant「文章が AI っぽい」）、share-targets-and-bounds「少し改善しただけで「これ以上は難しい」と言う」（wont-rethink-approach「少し試しただけで「これ以上は無理です」と言われる」）、permission-to-stop「テストが通らないと、テストのほうを変えて通そうとする」（rewrote-tests-to-pass「テストのほうを書き換えて通された」）、promises-after-compaction「最初に伝えた禁止事項を、途中から守らなくなった」（forgot-after-compaction「会話で禁止したことを圧縮の後にやられた」）。同じ文とみるなら外す
2. **always-on-costs の sign**：外した結果、goal の1つだけになった。B の #23 を足す案もあったが、直接答えるのは inspect-context なので足さなかった
3. **「拒否ルール」**：M1 の仮の訳語で promises-after-compaction の summary に使った。用語集で「deny ルール」に決まれば、この summary も直す
4. **japanese#5**：where-to-put-instructions を consistent-politeness・consistent-notation・align-japanese-output の前提にはしなかった。アプリのタブだけの前提で、ページ全体の前提ではないため（where-to-put-instructions はすでに第一波に入っているので、前提にしても第一波の数は変わらない）
5. **handing-long-documents の quotes-first の節**：anchor と題は残し、notes に「要点と long-context-first への案内だけにする」と書いた。執筆で薄すぎると分かれば、節を long-context-first への一行の案内にしてよい
6. **output-shape の styles-for-tone**：提案にない付け方（§1 の注）。アプリの画面に Styles のメニューが残るかは確かめていない（research/26 §5）
7. Web は開いていない。材料は調査資料（research/23・26・27、03）と、ほかの分野のファイル（読むだけ）
