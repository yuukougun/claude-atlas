# 工程3 C1：start・changes・basics の目次の報告

- 担当：C1（2026-11-04）
- 書いたもの：[planning/catalog/start.yaml](../../catalog/start.yaml)・[changes.yaml](../../catalog/changes.yaml)・[basics.yaml](../../catalog/basics.yaml)
- 読んだもの：brief-catalog.md、design §1〜§13、catalog/README、schema/site.yml、registry、requirements §1・§3〜§6・§9、decisions 2026-11-03 の各節、00 §1〜§6、05 §1・§3、01 KQ4、11 第1〜3節の該当の行、research/21〜27 の該当の節。kyopro-atlas の入口のページの front matter（読むだけ）

## 1. 書いたファイルとページ数

| 分野 | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| start | 10 | 必須 10 | なし 10 | guide 5・hub 5 | 8（採る 7・まとめた 1）＋新規 3 |
| changes | 4 | 必須 1・推奨 3 | 使う 1・整える 1・なし 2 | ledger 2・concept 1・recipe 1 | 5（採る 4・まとめた 1） |
| basics | 20 | 必須 16・推奨 4 | 使う 6・整える 10・任せる 4 | concept 20 | 20（採る 20） |

- start：how-to-use・ai-and-sources（使い方と方針）／four-principles・six-causes（背骨）／reverse-index・glossary・terminology（辞書として引く）／product-map・roadmap・knowledge-map（地図と道順）
- changes：outdated-advice-ledger・change-timeline-2026（台帳と年表）／dating-information・checking-for-updates（古い情報を見分ける）
- basics：コンテキストと注意（8）・エージェントと思考（3）・答えの確かさ（6）・指示と仕組み（3）

## 2. まとめた候補・新しいページ・registry から変えたこと

**まとめた（merged）**

1. `human-pitfalls-intro` → `six-causes`：design §7 が「失敗の二つの軸と診断の入口」を1ページとする。人の側の五つだけの入口は judgment の `human-pitfalls`（総論）と同じ内容の薄いページになる。id は症状のページから指されやすい `six-causes` のままにし、題名を design §7 に合わせた
2. `old-and-new-names` → `glossary`：start の「用語索引と旧名の対応」と重なる（registry の notes の組）。design §7 も旧名の対応を用語索引に置く。旧名からの引き方は glossary、改名の時期と版は change-timeline-2026 に置き、同じ改名を三か所に持たない

採らなかった候補（dropped）はない。

**新しく足したページ（start、notes に「新規」）**

1. `knowledge-map`（知識マップ）：design §2.1・§7 にあり registry にない。生成（graph.json と JS）。必須・wave: 1
2. `ai-and-sources`（出典と AI 利用の方針）：design §7。**作者の承認が要るページ**（design §6.1 の8・§10.8）と notes に書いた。第一波の公開に注意書きとライセンスが要るので必須・wave: 1
3. `terminology`（用語集。独自の用語と公式の訳語）：design §6.2 は「用語集のページを正とし prh.yml を作る」とするが、registry にも design §7 にもない。生成の用語索引（glossary）とは別の手書きのページにした（kyopro-atlas と同じ分け方）。prh の元なので本文より先に要る。必須・wave: 1

**registry の見当から変えたこと（理由は各ページの notes と level_evidence）**

- 段階：`context-rot` 整える→使う（症状 forgets-in-long-chats（使う）の原因の説明で、使う→整えるの上がる条件「散らかっている」の中身）、`where-instructions-sit` 任せる→整える（プロジェクトの指示や最初の CLAUDE.md を置く段階で要る）
- 優先度：`sycophancy`・`reward-hacking` 推奨→必須（judgment・eval・symptoms の必須で第一波のページが前提にしやすいため。必須の前提は必須）
- 題名：`tokens` から「（日本語の場合）」を外した（日本語の量の本体は japanese の more-tokens-in-japanese）。`six-causes`・`reverse-index`（状況を足す）は design §7 に合わせた。basics の題名は公式の日本語版の多数派（サブエージェント・圧縮・プロンプトキャッシング・システムプロンプト・思考）にし、英語名を aliases に置いた（design §13 O、research/27 P11）。`unfaithful-reasoning` は「一致しない」を「一致するとは限らない」に和らげた
- 型：生成のページは start が hub、changes が ledger（catalog の形が type を必須とするため。notes に生成と書いた）

## 3. wave: 1 を付けたページ

- start：全10ページ。D10 の第一波の「入口」を分野00（入口と地図）の全体と読み、symptoms の全ページを核にした registry の扱いとそろえた（迷った点の1）
- changes：outdated-advice-ledger だけ（old-and-new-names は glossary にまとめ、glossary が wave: 1 を受けた）
- basics は核の分野でないので付けていない
- 検査の集計（この時点）：第一波 28 ページ（wave: 1 が 21、前提でたどって届くもの 7）。symptoms と japanese のファイルがまだなく、数は増える

## 4. ほかの分野への提案（open_issues の要約）

- **judgment**：human-pitfalls-intro は six-causes にまとめた。人の側の五つの本体と根拠の強さの区別（research/24 F1・§2.3）は human-pitfalls に置く（今の judgment.yaml は human-pitfalls の関連に six-causes を持っていて、提案と合う）
- **symptoms**：症状のページは six-causes を前提か関連に持つと、診断の順を繰り返さずに済む。forgets-in-long-chats は context-rot を、instructions-ignored は where-instructions-sit と request-vs-lock を、rewrote-tests-to-pass は reward-hacking を、caves-when-pushed は sycophancy を、forgot-after-compaction は what-survives-compaction を前提にできる（段階も優先度も合う）
- **cli（直してほしい点）**：cli.yaml の command-cheatsheet の related が `old-and-new-names`（glossary にまとめた）を指していて、全体の検査でエラーになる。`glossary` に替える
- **japanese**：more-tokens-in-japanese は tokens を前提にし、日本語の量の違いの本体を持つ
- **context**：promises-after-compaction は残したい約束の移し方に絞り、残るもの・消えるものの一覧は what-survives-compaction（公式の表）に一本化する
- **api**：stateless-messages-api は rereads-whole-history と同じ仕組みなので、タブにしてまとめるか、API に固有の操作に絞って rereads-whole-history を前提にする。tool-use-loop は agent-loop を前提にする
- **prompting・verify**：long-context-first は lost-in-the-middle（推奨）を前提にせず関連にとどめる。fact-checking（使う）は nondeterminism・summary-overgeneralization（整える）を前提にすると段階が逆転する（今の verify.yaml は関連にしていて問題ない）
- **registry の ledger**：2項目を足す提案。「Styles で応答の調子と形式を切り替える」（research/26 §3.1。置換）と「コンテキストを守るために subagent を使う」（現行の Best practices の「What you can stop doing」の行。research/23 §3.7。条件付き）
- **data/outdated-advice.yml（土台作り）**：00 §5 の注記のある値（think-hard-keywords の時期、important-caps の「強調は1行だけ」）は research/23 §3.5・§3.7 で入れる。「2026（公式の撤回表）」の行は「2026-10-27 ごろ（Best practices の改稿）」にできる
- **設計書・道具**：生成の本体を持つページの示し方（type か印のキーか）を決める。design §7 に用語集の行を足す。用語索引で旧名を「旧名」と示す手段（facts の名称の項目と aliases の照合）を土台作りで決める。台帳の35行のうち、どのページの outdated_advice からも指されない行がないかを検査に足す
- **全分野（工程4）**：題名の用語の表記を公式の日本語版の多数派にそろえる（registry には subagent・compaction・prompt caching・Hooks・Skill などの英語の表記が多い）。用語集（terminology）で決める
- **メイン**：ai-and-sources は作者の承認の対象。第一波の最初のバッチより前に、作者に見せる文の一覧に入れる
- `new_features` の提案はない（tracks は README §5 の id だけを使った）

## 5. 検査の結果

`python3 tools/check_catalog.py --field <field>`（最後の実行）

| 分野 | エラー | 警告 | 残した警告の理由 |
| --- | --- | --- | --- |
| start | 0 | 0 | |
| changes | 0 | 0 | |
| basics | 0 | 1 | 比例則1：why-prompt-caching（任せる）は費用の仕組みの説明で、任せる幅を広げる内容ではない（notes に書いた）。途中で出た「未処理の候補」5件は、prompting.yaml が書きかけだったためで、相手が書き進めて消えた |

- 書いている間に、ほかの担当がまとめた候補を指していたので、まとめた先に直した：product-map（unified-claude・claude-code-vs-cowork → 削除、agent-sdk-and-managed-agents → sdk-comparison）、outdated-advice-ledger（commands-became-skills → writing-skills、homemade-loops → goal-until-done）、why-prompt-caching（breaks-and-cache-expiry → compact-and-auto-compact、claude-code-costs は削除）、what-survives-compaction（spoken-prohibitions-fade は削除）、summary-overgeneralization（reading-top-solutions → learning-with-ai、read-specs-yourself を足した）、nondeterminism（stratified-and-worst-case は削除）
- 道具が見ない点も確かめた：summary の字数（最長 103 字）、題名・要約・サイン・別名の半角と全角の間の空白、題名・要約・サインの数字（年表の「2026 年」だけで、範囲を示す年）

## 6. 確かめていないこと・迷った点

**確かめていないこと**

- 一次資料は見ていない（Web を使わない指示）。`/doctor prompt-audit` と `/release-notes` の今の名前と動き（00・01 の材料）は checking-for-updates の notes に「書く前に確かめる」と書いた
- symptoms・api・japanese のファイルは最後の確認の時点でなかった。そこへの参照（six-causes の関連の症状9ページ、basics の関連の症状・API・日本語のページ、計33件）は registry の id で指しただけで、相手がまとめたり外したりするとエラーになりうる。全分野がそろった後に検査を流し直す必要がある
- 00 §4 の逆引き73項目は、自分の分野のページに当たる行だけを signs の材料にし、全項目の行き先は照合していない
- 11 の作業ノート（11a〜11c）と 10 の本文は読んでいない（11 第1〜3節と requirements の引用で足りる範囲だけ）

**迷った点**

1. start の全ページに wave: 1：第一波を絞るなら、生成のページ（roadmap・knowledge-map）の手書きの導入を後にできる
2. 用語索引と用語集の id：registry に合わせて glossary を用語索引（生成）にし、用語集を新しい terminology にした。kyopro-atlas は glossary を用語集、term-index を用語索引にしている。URL になるので、工程4で入れ替えるなら骨格の前に決める
3. knowledge-map を必須にした（生成で手間が小さく、ロードマップ・逆引き・用語索引とそろえた）。初版に JS が間に合わないなら推奨に下げられる
4. 人の側の五つの根拠の強さ：six-causes の summary・signs・notes で強さを断定せず、本体の human-pitfalls に任せた（research/24 F1 で requirements §3.2 の「強」は強すぎると直されたため）
5. rereads-whole-history の図を dynamic にした（requirements §2 が動く図の例に挙げるコンテキストの埋まり方）。公式に対話型の図があり、自作かリンクかは未決（research/21 §2.4）
6. change-timeline-2026 は registry の id のまま年ごとのページにした（過ぎた年の表は変わらない記録になる）。年をまたぐ1ページにするなら、骨格の前に id を変える
