# 工程3 C2：surfaces・models・cost の目次の報告

- 担当：C2（2026-11-04）
- 書いたもの：[planning/catalog/surfaces.yaml](../../catalog/surfaces.yaml)・[models.yaml](../../catalog/models.yaml)・[cost.yaml](../../catalog/cost.yaml)
- 読んだもの：brief-catalog.md、design.md §1〜§7、catalog/README.md、schema/site.yml、registry.yaml、requirements.md §1・§3〜§6、decisions.md の 2026-11-03 の節、00 §3（分野02・03・14）・§4・§5、11 第1節・第2節（分野02・03・14）と第4節の関わる行、research/21 §2・22・23・25（P5）・26・27 §3.1、詳しい調査 01（L・M・P）・02（§1〜§3・§4-13・§5-8・§5-9）・03（$2・F7・N4・P6）・04（Q2〜Q4）・10（第14〜16章・第23章）

## 1. 書いたファイルとページ数

registry の候補37を、ページ28とまとめた9に分けた（採らない 0・新しいページ 0）。

| 分野 | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| surfaces | 6 | 必須 2・推奨 3・任意 1 | 使う 1・整える 2・任せる 1・なし 2 | comparison 2・concept 1・feature 1・ledger 1・hub 1 | 11（採る 6・まとめた 5） |
| models | 11 | 必須 6・推奨 4・任意 1 | 使う 2・整える 4・任せる 5 | concept 6・feature 3・comparison 1・recipe 1 | 14（採る 11・まとめた 3） |
| cost | 11 | 必須 4・推奨 5・任意 2 | 使う 3・整える 4・任せる 2・仕組みにする 2 | concept 9・feature 1・comparison 1 | 12（採る 11・まとめた 1） |
| 計 | 28 | 必須 12・推奨 12・任意 4 | 使う 6・整える 10・任せる 8・仕組みにする 2・なし 2 | | 37（採る 28・まとめた 9） |

- 優先度は registry（00 の表）のまま変えていない。「使う」は6ページ（21%）
- volatility は、値を本文に多く持つページを 高 にした（28のうち 高 23、中 5。中は harness-over-model・suspected-degradation・what-uses-up-limits・saving-priorities・when-ai-is-unavailable）
- 値（料金・上限・既定のモデルと effort・プランの名前・モデルの世代）は summary・signs・title に書かず、節の名前で「数値ファイルの表」を置く場所を決めた。プランの名前は aliases にも書いていない

### registry から変えた型・レベル・題名

| id | 変えたこと | 理由 |
| --- | --- | --- |
| what-each-surface-cannot-do | comparison・整える → ledger・level なし。題名「面ごとにできないこと（早見表）」 | 中身が数値ファイルから生成する面 × 機能の対応表（design §2.2・§3.1 の規則2） |
| browser-control | 整える → 任せる。題名「Claude in Chrome と computer use（ブラウザと画面の操作）」 | ログイン済みのブラウザや手元のアプリの操作は任せる幅を広げる。screen-control をまとめた |
| 1m-context | 題名「広いコンテキストウィンドウとの付き合い方」 | 題名から数値（1M）を外し aliases に置いた。id は公式の機能名（1M context）のまま |
| opusplan | 題名「計画・実装・サブエージェントでモデルを分ける（opusplan など）」 | 組み合わせが変わりうるモデルの名前を題名から外した（旧い言い方は aliases） |
| what-uses-up-limits | 題名「上限を早く使う要因」 | 公式が挙げる要因の数（七つ）は変わりうる |
| choosing-a-plan | 題名「プランの選び方」 | 「（確認日付き）」は題名の役でない（表に確認日を付ける） |
| peripheral-products | 題名「周辺製品の一覧」 | research preview の製品名は変わりやすいので aliases に置いた |
| usage-credits-basics | 題名「usage credits（上限を超えた分の従量課金）」 | 言い換えだけ |

### 工程2で確かめた事実を扱うページ

| 事実 | 扱うページと節 |
| --- | --- |
| 2026-10-30 に旧 Max 20x が Ultra に改名、Max は月 $100 の1段（research/22 #32・26 #19） | cost の choosing-a-plan#plan-table（表は数値ファイルから。台帳 max-5x-or-20x を outdated_advice に）、how-usage-limits-work#limit-types（確認済みの Ultra の口座は週の上限だけ）、before-using-fable#which-limit、check-billing-path#monthly-api-credits。旧名からの引き方は start の glossary と changes の change-timeline-2026（提案）。旧 20x と Ultra で使える量が同じかは断定しない（research/22 #44） |
| 既定の effort は面で違う（Sonnet 5.5 は API が high、Claude Code とアプリは medium。research/23 #8） | models の effort-levels#defaults-by-surface（数値ファイルの「モデル × 面」の表）。suspected-degradation（effort を先に確かめる）と after-switching-models（effort を持ち越さない）が前提にする |
| `ANTHROPIC_API_KEY` があると `claude -p` は確認なしに従量の課金（research/26 §3.8） | cost の check-billing-path#api-key-in-env（雛形は safety: true）。delegate の headless-basics#billing-path・bare-mode#authentication、api の agent-sdk-basics#billing と相互に結んだ |

## 2. まとめた候補と理由

| id | まとめた先 | 理由（要約） |
| --- | --- | --- |
| unified-claude | choosing-a-surface（節 app-chat-and-tasks） | 2026-09 の統合で、アプリがチャットとタスクを一つの会話で扱うことは面を選ぶ前提そのもの。独自の判断（どこで動き何に触れるかで選ぶ）が choosing-a-surface・where-it-runs と同じ |
| claude-code-vs-cowork | choosing-a-surface（節 app-tasks-or-claude-code） | 統合の後の Cowork はアプリのタスクの機能で、「アプリのタスクか Claude Code か」は choosing-a-surface の比較の中心と同じ軸 |
| screen-control | browser-control（節 computer-use） | computer use は beta で概念と注意が中心。公式の優先順（connector → ブラウザ → 画面操作）は Claude in Chrome との選び分けで一つの判断 |
| office-and-workspace | peripheral-products（節 office-add-ins） | requirements §6.3 で周辺製品は一覧だけ |
| agent-sdk-and-managed-agents | api の sdk-comparison | design §4.2 で API・SDK の概念は api。api も managed-agents-basics を同じページにまとめた |
| fable-and-mythos | current-models（節 fable-and-mythos） | Mythos は検証の制度を通した組織だけで、読者が選び分ける組ではない。透かしは2モデルに限らない（research/25 P5b） |
| model-retirements | after-switching-models（節 retirements-and-default-changes） | 退役と既定の変化は「替えたら見直す」の引き金の一つ |
| when-to-use-haiku | opusplan（節 lighter-models） | 軽いモデルの使いどころは、サブエージェントや大量の処理へのモデルの割り当ての判断の一部 |
| claude-code-costs | cost の what-uses-up-limits（節 find-what-uses-it） | /usage の内訳は「何が枠を使っているか」を確かめる手段で同じ問い。面に固有の操作の本体は cli の usage-context-statusline（cli の担当の提案と同じ境界） |

## 3. wave: 1

付けていない（3分野とも核の分野でない）。核からの前提では、symptoms の keeps-stopping → effort-levels が第一波に入る（effort-levels の前提 how-thinking-works も必須）。

## 4. ほかの分野への提案と new_features

open_issues の要約（取り込み済みのものは各ファイルの最後の項目に書いた）：

1. **api**：sdk-comparison に「面の中での位置づけ（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で対話する）」の観点と、related に choosing-a-surface を入れる
2. **start・changes**：プランの改名と上限の呼び方（session limit → 5-hour limit）を glossary と change-timeline-2026 に数値ファイルから入れる。台帳の budget-tokens・avoid-opus-as-expensive の「今どうするか」から effort-levels・choosing-a-model へ
3. **数値ファイル（土台作り）**：面の属性の表、既定の effort の「モデル × 面」の表、ultrathink が上げる段と版と面、fast mode の対象・料金・削除の日付、退役の予定、プランの表、上位のモデルの枠（料金のページと記事の書き方の食い違いを両方の出典つきで。research/26 #22）、usage credits の日本での失効、API の料金、agent teams の倍率とその条件（teammate が plan mode のとき。research/23 #7）
4. **app・features**：アプリのタスク（Cowork）の機能の id が README §5 にない

私のまとめに合わせて、ほかの担当がすでに直したもの：app の permission-modes-in-the-app・tasks-and-schedules-in-the-app（前提を unified-claude から choosing-a-surface へ）、cli の usage-context-statusline と context の inspect-context（claude-code-costs から what-uses-up-limits#find-what-uses-it へ）、start の product-map（まとめた候補を外した）。symptoms は seems-less-capable → suspected-degradation、hits-limits-quickly → what-uses-up-limits・saving-priorities、keeps-stopping・does-more-than-asked → model-quirks を入れた。

取り込んだほかの担当の提案：team（choosing-a-plan → enterprise-vs-team-plans）、delegate（parallel-and-loop-costs → agent-teams-experimental）、safety（check-billing-path ⇔ protecting-secrets、browser-control → browser-agent-cautions）、api（キャッシュ・バッチの倍率と Managed Agents の時間の料金を reading-api-pricing に）、app（choosing-a-surface → permission-modes-in-the-app、peripheral-products → artifacts-overview#claude-design）、cli（for-non-engineers のサイン「コードを書かない仕事に Claude Code を使いたい」を choosing-a-surface に置いた）。changes の old-and-new-names → glossary、japanese の more-tokens-in-japanese → can-i-prompt-in-japanese のまとめに合わせて参照を直した。

new_features（4件）：

| id | 題名 | 追うページ |
| --- | --- | --- |
| advisor | advisor（Claude Code の /advisor と API の Advisor tool） | fast-mode-and-advisor |
| api-credits | 月の API credits（プランに付く API の残高） | check-billing-path・usage-credits-basics |
| auto-continue | 上限での自動の継続（autoContinueAtUsageLimit） | how-usage-limits-work・when-ai-is-unavailable |
| wrap-up-allowance | Wrap-Up Allowance（上限に達した応答を区切りまで続ける） | how-usage-limits-work |

## 5. 検査の結果

`python3 tools/check_catalog.py --field <分野>`（最後に流したとき。分野のファイル 23・ページ 361）：

| 分野 | エラー | 警告 |
| --- | --- | --- |
| surfaces | 0 | 0 |
| models | 0 | 0 |
| cost | 0 | 0 |

- 途中では、symptoms・japanese・prompting が書きかけのための「未処理の候補」の警告が出ていたが、最後に流したときは消えていた。私のまとめを指していたほかの分野のエラー（app 3件・cli 1件・context 1件・start）も、各担当が直して 0 になった
- 比例則：任せる以上の10ページはすべて verify・eval・enforce・safety のページを前提か関連に持つ
- 自分で追加で確かめたこと：summary・signs・title に数値・プラン名・世代・料金がないこと（「待ち時間」「1ターン」「倍率は表で」などの言い回しだけ）、aliases が題名の語と重ならないこと、ほかの分野を指す id#anchor がすべて相手の sections にあること
- ほかの担当がまだ書いている分野がある。後でまとめ・採らないが増えると、私のファイルの参照がエラーになりうる（§6 の8）

## 6. 確かめていないこと・迷った点

1. **一次資料は開いていない**（Web を使わない指示）。値と挙動は research/22〜26（2026-11-03 の確認）による。00 の「/doctor prompt-audit」（after-switching-models の材料）、Anthropic の登録番号と消費税の扱い（paying-in-yen。04 の二次情報）、障害の事例（when-ai-is-unavailable。research/24 B-57 で未検証）は、書く前に一次資料で確かめる必要がある
2. **unified-claude をまとめたこと**：app の担当は unified-claude を「統合の経緯と面ごとの差」のページとして前提にしていた。独自の判断が choosing-a-surface・where-it-runs と重なり、経緯は changes に置けるのでまとめたが、メインが別のページを残すと決めるなら、短い feature のページに戻せる（id は registry のまま）
3. **題名のモデルの系統名**：before-using-fable の題名「Fable を使う前に」と current-models の aliases には系統の名前（Fable・Opus など）を残した。世代（5.5 など）ではなく、読者が引く名前と考えた。系統そのものが替われば題名を直す
4. **aliases の値**：how-usage-limits-work の five-hour limit・weekly limit・session limit、1m-context の 1M コンテキストは、公式の名前と旧名として aliases に置いた（規則は summary・signs・title だけを禁じる）。数値ファイルの値と食い違う検査の対象にするかはメインの判断
5. **表記**：opusplan の題名と summary は、公式の日本語版の多数派の「サブエージェント」にした（registry のほかの題名は subagent が多い）。cost の題名は分野名に合わせて「利用上限」にし、公式の日本語版の「利用制限」を aliases に置いた。どちらも用語集で決める点
6. **choosing-a-model の三段階**は、公式の API 向けの選択ガイドを、アプリと Claude Code の既定から始める形に言い換えたもの（02 §3 の Inferences）。公式の効率を先にする始め方（軽いモデルから上げる）も節で並べる
7. **harness-over-model の置き場所**：11 は分野02 の案も挙げる。モデルを替えるかの判断の直前に読まれるので models に置いた。根拠は一つの比較の実験と公式の記事（中）なので推奨のまま
8. **ほかの分野の任意の候補への参照**：書き始めの時点でファイルのなかった分野の任意の候補は指さず、ファイルができてページになったもの（using-ides・control-from-phone・voice-and-mobile・batch-api-basics・agent-teams-experimental・enterprise-vs-team-plans・via-cloud-providers）だけを後から指した。ほかの担当が後でまとめると参照のエラーになりうる
