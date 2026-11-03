# 工程3 C7：enforce（仕組みで縛る）・safety（安全とデータ）の目次の報告

- 担当：C7（2026-11-04）
- 書いたもの：[planning/catalog/enforce.yaml](../../catalog/enforce.yaml)・[planning/catalog/safety.yaml](../../catalog/safety.yaml)
- 従ったもの：brief-catalog.md、catalog/README.md、design §1〜§7、decisions 2026-11-03（特に「安全の既定の勧め方」「書き方の方針（安全・面・表現）」の B1・B2）

## 1. 書いたファイルとページ数

| 分野 | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| enforce | 15 | 必須 9・推奨 5・任意 1 | 任せる 6・仕組みにする 9 | concept 3・feature 9・comparison 1・recipe 2 | 15（採る 14・まとめた 1）＋新規 1 |
| safety | 18 | 必須 11・推奨 7 | 使う 3・整える 9・任せる 5・仕組みにする 1 | concept 12・judgment 1・feature 1・comparison 1・recipe 3 | 17（採る 17）＋新規 1 |

章：

- enforce：何を縛るか（when-to-lock・request-lock-table・move-judgment-into-scripts）／権限と封じ込め（permission-rules・what-auto-mode-stops・sandboxing・protected-paths・managed-settings-enforcement）／フック（hooks-basics・block-with-exit-2・writing-safe-hooks・hook-recipes・stop-hooks）／縛りの運用（freeze-eval-assets・lock-side-effects）
- safety：既定と承認（default-safety-settings・approval-fatigue・where-bypass-is-ok）／データの扱い（where-your-data-goes・what-feedback-sends・shared-artifacts-and-files・entrusted-data）／悪意ある入力（prompt-injection-in-practice・instructions-hidden-in-materials・lethal-trifecta・before-opening-unknown-repos・vetting-extensions・browser-agent-cautions）／秘密と壊す操作（protecting-secrets・destructive-commands）／規則と開示（checking-ai-rules・disclosure-and-provenance・when-requests-are-refused）

安全の既定の勧め方（decisions 2026-11-03）の受け持ち：

- 基準と限界：what-auto-mode-stops（auto モードの分類器が止めるもの・すり抜け・「安全を保証しない」）
- 段階ごとの既定の正本：default-safety-settings の節 by-stage（面ごとの既定は数値ファイルから生成。段階ごとの勧めは安全の既定なので、変えるときは作者の承認が要る。design §9.4）
- 任せる段階からのサンドボックスと秘密の読み取りの禁止：sandboxing・protecting-secrets（どちらも level は任せる）
- 無人の実行は使い捨ての環境：where-bypass-is-ok（題名を広げた）
- 預かったデータは契約のある面だけ：entrusted-data
- 法令の解釈と社内規則の回避を書かないことは、関わるページの notes に書いた（default-safety-settings・entrusted-data・protecting-secrets・checking-ai-rules）

方針 B1・B2：攻撃の手口は型と仕組みまで、無害な再現だけ（prompt-injection-in-practice・instructions-hidden-in-materials・before-opening-unknown-repos・vetting-extensions の notes）。安全とデータの雛形は、拒否ルール・止めるフック・サンドボックス・管理設定・確認表・無害な再現をすべて `safety: true` にした（enforce 10件・safety 7件）。整形・テスト出力の絞り込み・Stop フック・担当の commit の禁止の雛形（enforce 4件）は安全とデータではないので `false`。

## 2. まとめた候補・落とした候補・新しいページ

**まとめた（merged）**

| 候補 | まとめた先 | 理由 |
| --- | --- | --- |
| spoken-prohibitions-fade（会話で言った禁止事項は圧縮で消える） | when-to-lock（節 spoken-rules-fade） | 「なぜ消えるか」は basics の what-survives-compaction、約束の残り方は context の promises-after-compaction、症状は symptoms の forgot-after-compaction が持つ。enforce に固有なのは「だから拒否ルールに書く」の判断だけ。旧題は aliases に残した |

**落とした（dropped）**：なし

**新しいページ**

| id | 題名 | 理由 |
| --- | --- | --- |
| lock-side-effects（enforce、推奨・仕組みにする） | 縛りすぎの害と見直し（止めすぎ・回り込み） | 縛る分野が鍵を足す話だけになり、縛りすぎの害を受け持つページがない。design §10.5 の5つの決まり（ユーザーの注意から作った）を読者向けの判断にする。根拠は公式の文書（matcher の正規表現・Claude に渡す文の書き方・記録を取るイベント。research/28）と制作の記録。頻度の研究はないので、本文で根拠の強さを書く |
| when-requests-are-refused（safety、推奨・使う） | 正当な依頼が断られたとき | research/26 §3.3 で公式の案内が確かめられ、decisions 2026-11-03「断られたときの頼み直し」で書く範囲が決まったのに、受け持つページが registry にない。提供元の規則（利用ポリシー）と安全の仕組み（分類器）の話なので safety に置いた。symptoms か prompting が対処の本体を持つなら merged にしてよい |

**registry の値を変えたもの**（理由はどれもページの notes に書いた）

| 候補 | 変えたもの | 理由 |
| --- | --- | --- |
| checking-ai-rules | 推奨 → 必須 | design §4.2 で contest の competition-rules・practice-vs-contest-day（必須）がこの確認表を前提にする。contest の担当（C10）の open_issues の依頼にも合う |
| where-bypass-is-ok | 推奨 → 必須、題名「bypassPermissions と無人の実行はどこで動かすか」 | 安全の既定の「無人の実行は使い捨ての環境」を受け持たせた。delegate の回すのページの比例則の受け皿 |
| entrusted-data | 推奨 → 必須 | 安全の既定の「預かったデータは契約のある面だけ」を受け持つ |
| writing-safe-hooks | 推奨 → 必須 | 止める用途のフックは既定で失敗すると操作を通す（research/28 #17）。必須の hook-recipes の前提にするため |
| shared-artifacts-and-files | 任意 → 推奨、題名「共有リンクと公開アーティファクトの扱い」 | research/26 §3.2 で会話の共有の仕様が確かめられ、app の分野に共有のページがない。公式も「公開リンクは公開したものとして扱う」と勧める流出の経路 |
| sandboxing | level 仕組みにする → 任せる | decisions 2026-11-03「安全の既定の勧め方」（任せる段階からはサンドボックス） |
| approval-fatigue | 型 concept → judgment | 人の側の慣れの話で、判断例（どの確認を残すか）と握るものが本体（落とし穴「預けすぎる」） |
| block-with-exit-2 | 題名「フックで止めて理由を返す（exit 2 と JSON）」 | 理由と代わりを構造立てて返せるのは JSON（research/28 #15） |
| browser-agent-cautions | 題名「ブラウザや画面の操作を任せるときの注意」 | 対象が分かる題名にした |
| 題名の用語 | Hooks → フック、sandbox → サンドボックス、auto mode → auto モード、managed settings → 管理設定、plugins・skills → プラグイン・スキル、prompt injection → プロンプトインジェクション | design §6.2（公式の日本語版の多数派。research/27 §3.1）。英語は aliases に残した。extend の担当（C6）も同じ案に合わせている |

## 3. wave: 1

なし（enforce と safety は第一波の核の分野ではない）。

## 4. ほかの分野への提案と new_features

**ほかの担当の依頼に応えたもの**（各ファイルの open_issues を読んで反映した）

- contest（C10）：checking-ai-rules を必須に上げた
- delegate（C9）：what-auto-mode-stops・default-safety-settings の related に five-questions-before-delegating・headless-basics を、sandboxing の related に dynamic-workflows を足した（where-bypass-is-ok は元から両方を持つ）
- extend（C6）：when-to-lock の related を what-to-put-in-claude-md#what-to-leave-out に直した（what-to-leave-out-of-claude-md がまとめられたため）
- recipes（C11）：move-judgment-into-scripts に bisect-regressions、freeze-eval-assets に build-test-harness、where-your-data-goes と entrusted-data に data-analysis・office-paperwork を足した
- team（C9）：managed-settings-enforcement は設定のキーと強制の仕組みだけにし（節「配る経路」を外した）、配る経路・グループごとの設定・MCP の許可は org-managed-settings-and-mcp に任せた。approval-fatigue の related に review-bottlenecks を足した
- surfaces（C2）：screen-control が browser-control にまとめられたので、browser-agent-cautions の related から外した（browser-control は元から持つ）

**こちらからの提案**（open_issues の要約）

1. 全体・用語：registry とほかの分野に残る英語の表記（Hooks・sandbox・auto mode など）を、用語集と prh の段でそろえる
2. symptoms：症状のページ「正当な依頼が断られる・止められる」を足し、when-requests-are-refused へ振り分ける。instructions-ignored・forgot-after-compaction → when-to-lock、stuck-in-a-check-loop → stop-hooks#avoid-loops、keeps-stopping・wrong-amount-of-approvals → what-auto-mode-stops・lock-side-effects
3. 全分野：spoken-prohibitions-fade を指すなら when-to-lock#spoken-rules-fade（related）か when-to-lock（prerequisites）に直す。context・basics・symptoms の圧縮のページから、この節へ related を張る
4. verify・eval：protect-tests・verifier-three-conditions・lockbox-and-holdout から freeze-eval-assets（止める設定の手順）へ
5. delegate：headless-basics・github-actions-with-claude・cloud-schedules・five-questions-before-delegating の前提か関連に where-bypass-is-ok、parallel-with-worktrees・goal-until-done に sandboxing
6. app：permission-modes-in-the-app → what-auto-mode-stops・lethal-trifecta、incognito-chats → where-your-data-goes、artifacts-overview → shared-artifacts-and-files（app に会話の共有のページがないので、仕様は safety が持つ）
7. extend：writing-subagents・what-subagents-dont-inherit に、disallowedTools の指定子は Bash 全体を外すこと、担当にだけ禁じるには hook-recipes#subagent-only（research/28 #14）。担当（C6）はすでに related を張っている
8. japanese：textlint-hook の前提に hooks-basics、related に writing-safe-hooks
9. cli：permission-modes-overview → what-auto-mode-stops・permission-rules、settings-layers → managed-settings-enforcement
10. basics：data-vs-instructions → prompt-injection-in-practice。team：ai-usage-guidelines の前提か関連に checking-ai-rules・entrusted-data。cost：check-billing-path と protecting-secrets を相互に。start：four-principles とロードマップから default-safety-settings#by-stage

**new_features**（safety.yaml の末尾）

- `feedback`：/feedback・/bug とトランスクリプトの共有（what-feedback-sends が指す）
- `chat-sharing`：claude.ai の会話の共有（招待と公開リンク。shared-artifacts-and-files が指す）

## 5. 検査の結果

`python3 tools/check_catalog.py --field enforce` と `--field safety`：どちらもエラー 0 件・警告 0 件（最後の実行は分野のファイル 13・ページ 178 を読んだ時点）。

途中で出て直したもの：ほかの分野でまとめられた候補を指していた参照のエラー2件（what-to-leave-out-of-claude-md、screen-control）、summary の「扱う」の警告2件。残した警告はない。

## 6. 確かめていないこと・迷った点

**確かめていないこと**

- 一次資料は見ていない（Web を使わない指示）。事実は research/22〜28 と 00・01・02・05・11 の、訂正と注記を踏まえた記述による。summary・signs・題名に、変わりやすい値と、注記の付いた主張（承認の割合、11 p34#200 の注入の成功率など）を使っていない
- まだファイルのない分野（basics・cli・context・app・verify・eval・symptoms・prompting・japanese・cost・api）のページへの参照は、検査が解決を確かめていない。その分野の担当が候補をまとめたり落としたりすると、参照のエラーが出うる
- 公式の日本語版での protected paths・prompt injection の訳語は確かめていない（research/27 §3.1 の表にない）。前者は題名の括弧に英語を残した
- ワークフローの担当でフックが走るかは文書になく未確認（research/28 #4）。hooks-basics と hook-recipes の notes に書いた

**迷った点**

1. **断られたときのページの置き場所**：symptoms（症状）、prompting（頼み直し）、safety（利用ポリシーと分類器）のどれが対処の本体を持つか。safety に置き、symptoms への提案にした。重なれば工程4で一つにする
2. **優先度を上げた数**：00 の優先度を基本にする規則に対して、5件を上げた（うち3件は安全の既定、1件は必須の前提の閉じ方、1件は共有の流出の経路）。safety は必須が18ページ中11ページになった
3. **sandboxing の level**：決定に合わせて「任せる」に下げた。00 の L4 と違う
4. **managed-settings-enforcement と team の境界**：team の担当の案（設定のキーと強制はこちら、配る経路は team）に合わせた。優先度は任意のまま
5. **lock-side-effects の根拠**：公式の文書と制作の記録だけで、研究はない。推奨にとどめ、必須のページの前提にしない
6. **instructions-hidden-in-materials を prompt-injection-in-practice にまとめるか**：「利用の規則の合図」という型と「規則を先に確かめる」判断が固有なので、別のページに残した。AI を禁じる課題の隠し指示を外す方法は書かない（方針 B1）
