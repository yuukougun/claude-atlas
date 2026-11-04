## term-index/write.md
[メインに判断してほしいこと]
- 生成の中身は表ではなく見出し付きの箇条の一覧で出た（束・カードは「表」と書く）。本文は「一覧」に揃えた
- 検査後に生成が走った結果、旧名の欄に「default モード → Manual（設定の値は default）」など数値ファイル由来の行が入っている（束 6.6 の件。手書きはしていない）

## term-index/review.md
[メインに判断してほしいこと]
- 漢字の群を頭文字の読みで分ける（または語頭の字ごとに区切る）生成の改善を、tools 側で検討してほしい（指摘 5）

## product-map/write.md
[メインに判断してほしいこと]
- `#identify-surface` の見分けの手がかり 4 項目（`claude` コマンド・Messages API・チャット画面・Office のサイドパネル）は、束の材料からの言い換えで、一次資料では確かめていない。載せるか確認してほしい
- 旧称の読み替え 3 件（Claude Code on the web・Claude in Slack・Claude Code SDK）の旧称は手で書き、今の名前は name の目印にした。旧称の手書きが方針に合うか確認してほしい
[提案]
- なし（数値・用語集・front matter の提案はない）

## product-map/review.md
[メインに判断してほしいこと]
- write.md の 2 点（見分けの手がかりの言い換え、旧称の手書き）は未確認のまま。事実の検証役に回してほしい

## roadmap/write.md
[メインに判断してほしいこと]
- 目次の図の案「委任の段階のはしご」（static）は SVG にしていない。段の表（`#levels`）が同じ内容を持つため。必要なら別途図を足す
- `#hypothesis` の根拠の印（弱／中・類推）の付け方が適切か
- 表の「この段で強める確かめと縛り」列の割り当て（整える→verification-ladder#four-steps ほか）は、各ページの要約と節名からの私の対応づけで、持ち主のページの内容と照らしていない
[提案]
- front matter の直し・用語集・data への提案はなし

## roadmap/review.md
[メインに判断してほしいこと]
- 表の最右列（強める確かめと縛り）の割り当てが持ち主のページと合うか
- 目次の図「委任の段階のはしご」は未作成（表が代わり）

## knowledge-map/write.md
[メインに判断してほしいこと]
- #how-to-read の「分野ごとの表示」「祖先と子孫だけの表示」は design §8.5 の方式を書いた。JS の実装がこの 2 つの表示を出すかは未確認。実装が違うなら書き直す。
- #how-to-read の「載せるのは下書き以上の段階だけ」は目次の notes（DR-01）に基づく。

## knowledge-map/review.md
[メインに判断してほしいこと]
- 指摘 4：図で「ページを選ぶ」方法と 2 つの表示の切り替えの実装を確かめ、本文の説明を合わせる。
- 指摘 5：図が出ない環境向けの一文を足すか。

## attention-budget/write.md
[メインに判断してほしいこと]
- 窓の大きさの数値は本文に書かず、数値の目印も置いていない（束に該当の facts id が無いため）。large-context-window を指すだけにした
- #why の n の 2 乗の説明は、束の Inferences（提案）と記憶に基づく。Anthropic の記事（anthropic-eng-effective-context-engineering-ai）を本文で開いて確かめていない。「（根拠：中）」を付けたので、検証で原文との突き合わせが要る

## attention-budget/review.md
[メインに判断してほしいこと]
- n の 2 乗の説明（根拠：中）は原文と未突き合わせ。事実の検証役が要る

## rereads-whole-history/write.md
[メインに判断してほしいこと]
- 図の主にする「公式の Explore the context window」の対話型の図へのリンクは、URL を確かめていないので入れていない。URL を渡してもらえれば足す
- `effects` に判断例を 1 つ置いた（続けるか新しい会話にするか）。when-to-start-fresh と重なるなら削ってよい
[提案]
- 用語集：「読み直す受験者」「積み木（キャッシュ）」の比喩は、既存の一覧どおり使った。追加の提案なし
- front matter の提案なし

## rereads-whole-history/review.md
[メインに判断してほしいこと]
- 公式の対話型の図へのリンクは未記入（write.md のとおり）。判断例は when-to-start-fresh と重なりうる

## what-survives-compaction/write.md
[メインに判断してほしいこと]
- 4 つの群の見出しと、公式の表の項目の対応は次のとおり。「動き続ける」「もう一度走る」を kept に、「作り直して入れ直す」「上限付きで入れ直す」「一部を読み直す」を reloaded にまとめた
- compare の表に compaction 自身の行が「未確認」で出る。tracks に compaction があるため。表から外すには tools 側の対応か tracks の見直しが要る（提案）
- 数値は skill-reattach-tokens-each/total の目印だけ使い、他は本文に書かず facts-proposal.yml に提案した。目印を置く場所は reloaded と kept
[提案]
- facts-proposal.yml の 4 件（used_in を付けた）。取り込まれたら、reloaded のファイルの項と kept のフックの項に目印を足してほしい
- 用語集：prh が「サブエージェント」「自動メモリ」「出力スタイル」「システムプロンプト」を求めた。本文はそれに従った

## what-survives-compaction/review.md
[メインに判断してほしいこと]
- 表の compaction 行「未確認」の扱い（write.md と同じ）

## subagent-isolation/write.md
[メインに判断してほしいこと]
- 面タブは置かなかった。surfaces に api があるが、束に API の手段の根拠がない（research/22 §3.7 は題と要約だけ）。本文に「API の分け方は扱わない」と一言書いた。API の節を足すなら別途の調査が要る。
- pitfalls が front matter にない。必要なら、どの人間側の落とし穴に結ぶかの提案を求む。
[提案]
- なし（用語集・prh・data への提案なし）

## subagent-isolation/review.md
[メインに判断してほしいこと]
- write.md の2点（面タブなし、pitfalls なし）に同意。追加はなし

## how-thinking-works/write.md
[メインに判断してほしいこと]
- 本文で「新しいモデルの中には thinking を切れないものがある」とだけ書き、どのモデルかは書いていない（束の未確認 11 3-2 #11 に従う）
[提案]
- facts-proposal.yml：effort の既定の段の「モデル × 面」の表（effort-levels#defaults-by-surface が使う想定。このページの本文では使っていない）

## how-thinking-works/review.md
[メインに判断してほしいこと]
- 「推論を本文に書かせる指示は断られることがある」は、事実の検証をしていない（U の範囲外）。事実の担当に確認を

## knowledge-cutoff/write.md
[メインに判断してほしいこと]
- 「なぜ」の節に図（比喩付き）を置かなかった。目次の visual が「なし」で、cutoff には手持ちの比喩の一覧に合うものがないため。必要なら図の案を足す
- 面のタブの Claude Code は、材料の束に根拠がないので「日付を渡しているかは確かめていない」と書いた。調べる担当がいれば埋めたい
[提案]
```yaml
proposals:
  - fact: {id: model-knowledge-cutoffs, title: モデルごとの reliable knowledge cutoff と training data cutoff（別々の欄で持つ）, value: "現行のモデルは両方とも 2026年6月（research/26 #12・§3.7）。古いモデルは差がある（例：Opus 4.6 は reliable が 2025年5月、training が 2025年8月）。モデルごとの表にする", sources: [api-docs-models-overview, hc-up-date-training-data], checked: 2026-11-05, status: 要確認}
    used_in: [knowledge-cutoff#why]
```
- 本文は日付なしで読める形にした。fact の id が data に入ったら、`#why` の「各モデルの日付は…載っている」の所に `fact-table` か `fact` の目印を置ける
- 用語集に reliable knowledge cutoff・training data cutoff を足す案（本文では表で短く定義した）

## knowledge-cutoff/review.md
[メインに判断してほしいこと]
- #what-helps 冒頭の「が」の警告は、検査を使い切ったため残した。「…である。」の後で文を切れば消える
- Claude Code タブは「日付を渡しているかは確かめていない」のまま。調べる担当がいれば埋めたい

## nondeterminism/write.md
[メインに判断してほしいこと]
- 図（目次の visual 案「同じレシピでも味が違う料理人」）は文章の比喩だけにして、SVG は作っていない。要るなら別途
- 雛形は目次の templates が空なので置いていない
[提案]
- 用語集：「非決定性」を、同じ依頼を出し直すと答えが変わる性質として追加する案
- 数値の提案はなし

## nondeterminism/review.md
[メインに判断してほしいこと]
- 図（料理人の比喩）が未作成。必要なら別途

## summary-overgeneralization/write.md
（ファイルがない）

## summary-overgeneralization/review.md
[メインに判断してほしいこと]
- write.md が無い。`data/sources.d/summary-overgeneralization.yml` と `snippets/` も無い（sources は既存 id を指す）。
- 「新しいモデルは古いモデルより一般化の正確さが低い傾向」「査読前」「DeepSeek・ChatGPT-4o・LLaMA 3.3 70B」は束の材料にない。事実の検証役に出典照合を依頼したい（本担当は事実を見ていない）。

## reward-hacking/write.md
[メインに判断してほしいこと]
- 比喩は、一覧にある比喩に当たるものがないため、「採点表だけを渡された受験生」を #why に 1 回だけ使った。比喩の一覧に足すか、直すかを決めてほしい
- 「なぜそうなるか」の訓練の側は、束の「誘因がありうる」までしか書いていない。仕組みの詳しい説明は一次資料を開いていない

## reward-hacking/review.md
[メインに判断してほしいこと]
- 比喩「採点表だけを渡された受験生」を一覧に足すか（#why）
- #why の「訓練の側」の「高く評価されて強まりうる」は束にない説明の補い。事実担当の確認が要る

## where-instructions-sit/write.md
[メインに判断してほしいこと]
- `compare` の表（`#duration`）は、アプリの 2 機能の「読み込みの時期」「圧縮で残るか」が null のため「未確認」と出る。data 側で埋められるなら埋めてほしい（埋まらなければ「未確認」のままで読める書き方にしてある）
- ledger の link（`outdated-advice-ledger#important-caps`）は、台帳ページに anchor がなければ止まる。check は通った
[提案]
- なし（数値・用語集・prh への提案なし）。front matter のほかのキーの直しもなし

## where-instructions-sit/review.md
[メインに判断してほしいこと]
- 表の「—」（アプリ2機能の読み込みの時期）は data 側の null による。埋められるなら埋めてほしい（write.md と同じ）

## data-vs-instructions/write.md
[メインに判断してほしいこと]
- 「境界がない」の意味を、本文では「信頼できる指示と信頼できない資料の間に、文脈の中で仕切りがない状態」と書いた。原因の定義が別にあれば直してほしい
- 「バグではなく文脈に並ぶ仕組みから来る性質として扱うのが安全」は（推論）を付けた。強すぎれば弱めてよい
[提案]
```yaml
frontmatter:
  - {id: data-vs-instructions, key: related, before: [prompt-injection-in-practice, lethal-trifecta, instructions-hidden-in-materials, before-opening-unknown-repos, vetting-extensions, browser-agent-cautions, sandboxing], after: [request-vs-lock, prompt-injection-in-practice, lethal-trifecta, instructions-hidden-in-materials, before-opening-unknown-repos, vetting-extensions, browser-agent-cautions, sandboxing], reason: "本文で request-vs-lock を指した（お願いと鍵の比喩）。request-vs-lock 側の related には既に本ページがある"}
```
- 用語集：「prompt injection」（読ませた資料に紛れた文が Claude の行動を変えること）の項を提案する。本文の導入で短く定義した

## data-vs-instructions/review.md
[メインに判断してほしいこと]
- 「境界がない」の定義は write.md の問いのとおり、原因の正本で確認を（今回は検証していない）

## effort-levels/write.md
[メインに判断してほしいこと]
- 節 defaults-by-surface に、数値ファイルの「モデル × 面」の表がまだ無い（facts に effort の表がない）。`fact-table` の目印はない id で止まるため置けず、本文は値なしの説明にした。facts-proposal.yml の `effort-default-by-model-surface` を反映したら、節の「各モデルの既定の値は、変わりやすいので…」の段落の直前に `<!-- gen:begin fact-table effort-default-by-model-surface --><!-- gen:end fact-table effort-default-by-model-surface -->` を置き、その段落は表を指す文に直してほしい
- data の effort に `enforcement` 属性がない。要点の「強制力」の目印を置けなかった。値を足すか（effort は設定で、お願い・鍵のどちらにも当たらない可能性がある）、型の必ず持つものの扱いを決めてほしい
- 本文の「新しい版」としか書いていない 2 か所（modelSettings、別モデルのサブエージェント）は、facts-proposal.yml の版の 2 件を反映すれば、目印で版を書ける
[提案]
- facts-proposal.yml：既定の effort の表 1 件（research/23 §3.2 の写し。Claude Code の列は 2026-11-05 に Model configuration と照合）、版の fact 2 件
- 用語集：新しい語の提案はなし。front matter の他のキーの直しもなし

## effort-levels/review.md
[メインに判断してほしいこと]
- facts の effort の表（facts-proposal.yml）と enforcement 属性を反映するか

## suspected-degradation/write.md
[メインに判断してほしいこと]
- #postmortem-example の表の日付とモデル名は、ポストモーテム本文（WebFetch の要約）で確かめた過去の固定の記録として本文に直接書いた。facts に置くべきなら、そう指示してほしい
- 「API は含まれない」は WebFetch の要約の記述。報告の原文の該当文で再確認してほしい（要約を通した確認のため）
[提案]
- 用語集：「ポストモーテム」（事後報告）が用語集にあるか未確認。なければ追加を提案する
- 出典：status-claude-com は data/sources.d に置いた。共有の data/sources.yml へ移す必要があればメインが反映

## suspected-degradation/review.md
[メインに判断してほしいこと]
- write.md の 2 点（事後報告の表を本文に直接書いてよいか、「API は含まれない」の原文確認）はそのまま残る。事実の検証はこの担当の範囲外

## give-reasons/write.md
[提案]
- front matter：sources に cc-docs-best-practices を入れていない（本文で使わなかったため）。束の出典一覧にあるので、足すかはメインの判断。
[メインに判断してほしいこと]
- 「なぜ効くか」の内部の仕組みは公式にも無いので（推論・実践例なし）と明記した。この扱いでよいか。
- 判断例の「ですます調」の効果と「本番 DB」の例は、筆者が作った想定の例（公式の例は読み上げのみ）。

## give-reasons/review.md
[メインに判断してほしいこと]
- write.md の提案（sources に cc-docs-best-practices を足すか）は、本文が使っていないので足さなくてよいと考える。

## suggest-or-do/write.md
[メインに判断してほしいこと]
- 本文にモデル名を書かなかった（モデル名は目印で書く決まりのため）。「公式のモデル別の指針」と言い、出典の一覧に頼った。読者に具体名が要るなら、names の目印を使う案を決めてほしい
- 「止まって議論する」書き方は、束の 11 第2節のとおり（推論・実践例なし）の印で書いた。最新のモデル別の指針に同じ記述があるかは未確認と本文にも書いた
[提案]
- 用語集：「system prompt」は prh でエラーになるので、本文は「システムプロンプト」にした。`default_to_action` などのタグ名は用語集に載せなくてよい
- 前提のページ four-specifics の「完了」へ link を張った（four-specifics#done）

## suggest-or-do/review.md
[メインに判断してほしいこと]
なし（モデル名を目印で出すかは write.md の判断事項のまま）

## state-the-scope/write.md
[メインに判断してほしいこと]
- 本文から `give-reasons`（related にない）を link で指した。check は通ったが、related に足すかを判断してほしい（下の提案）
- `#two-layers` の「アプリ」タブに「アプリで依頼の範囲を仕組みで縛る手段は未確認」と書いた。確認できる資料が束になかったため
[提案]
```yaml
frontmatter:
  - {id: state-the-scope, key: related, before: [does-more-than-asked, say-what-you-want, suggest-or-do, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks], after: [does-more-than-asked, say-what-you-want, suggest-or-do, give-reasons, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks], reason: "本文で give-reasons を指したため"}
```

## state-the-scope/review.md
[メインに判断してほしいこと]
- write.md の提案（related に give-reasons を足す）に同意する
- アプリタブの「未確認」と API タブの記述は束に根拠がない。確かめるか、削るかを決めてほしい

## long-context-first/write.md
[メインに判断してほしいこと]
- 図（目次 visual の Before/After）は SVG にせず、本文の Before/After とスニペットで代えた。SVG が要るなら次の波で
- 公式の「最大 30% 向上」は数値の提案にとどめ、本文には数字を書いていない（目印が使えないため）。承認後に fact の目印を足す
[提案]
- facts：facts-proposal.yml
- 用語集：新しい語の提案なし

## allow-i-dont-know/write.md
[メインに判断してほしいこと]
- 「ある報告に〜偽の flag を大量に提出した」（調査 11 の p34#205）は、束に出典 URL がなく、束の出典の一覧にもない。（根拠：弱・単発・版依存）として出典なしで書いた。元の出典を確かめて足すか、削るか
- 競技の実践者の指摘は chokudai の記事（sources に入れた）。個人名は本文に出していない
[提案]
```yaml
frontmatter:
  - {id: allow-i-dont-know, key: pitfalls, before: null, after: [言葉の許可だけを頼りにする, やりすぎて答えられることまで断らせる], reason: "型の必ず持つものに pitfalls があるため。値の形は schema 次第"}
```

## allow-i-dont-know/review.md
[メインに判断してほしいこと]
- 偽 flag の報告（調査 11 p34#205）の出典追加か削除（write.md と同じ）

## when-to-start-fresh/write.md
[メインに判断してほしいこと]
- 「訂正が重ねて失敗したら /clear」の回数は、カード §7 に従い本文に書かず、`facts-proposal.yml` で数値の提案にした。本文は「回数の目安は公式を見る」。fact が入ったら `#signals` を目印に差し替えてよい
- 図は Mermaid（流れ図）。catalog の visual の案どおり
[提案]
- 数値：facts-proposal.yml の `clear-after-failed-corrections`

## when-to-start-fresh/review.md
[メインに判断してほしいこと]
- 回数の fact が入ったら #signals の「回数の目安は公式を見る」を目印に差し替える（write.md と同じ）

## rewind-dont-correct/write.md
[メインに判断してほしいこと]
- 断られたときの巻き戻し（research/26 §3.3 (b)）は `#how` の末尾に 1 段落で入れた。利用ポリシーを避ける頼み方とは分けて書いてある。置き場所が合うか確認してほしい
- アプリでの編集の詳細（編集後に元の枝が見えるか・戻せるか）は、材料になく、確かめていないので、本文に「画面で確かめる」と書いた。確かめられる担当がいれば書き足せる
[提案]
なし（用語集・data・front matter の他キーへの提案はない）。

## rewind-dont-correct/review.md
[メインに判断してほしいこと]
- アプリの編集の挙動は未確認のまま「画面で確かめる」と書かれている。確かめられる担当がいれば足してほしい（write.md と同じ）

## promises-after-compaction/write.md
[メインに判断してほしいこと]
- 図の案（static の対応図）は、SVG にせず #where-to-put の表（置き場所｜向く約束｜例）で代えた。図が要るなら別途
- 「ふつうのファイルは自動では戻らないので、CLAUDE.md に読む 1 行を書く」は「この辞典の推奨」と明記した独自の提案。公式の記述ではない
[提案]
- 変わりやすい値の提案なし（版・上限・トークン数は本文に書かず「上限付き」「数値は版で変わりうる」とした）
- front matter の提案なし
- 用語集：`auto モード`（prh が auto mode を auto モードに直すため、本文はそれに従った）

## promises-after-compaction/review.md
[メインに判断してほしいこと]
- 図の案を表で代えた件は、表で用が足りると見た。図は必須でない

## inspect-context/write.md
[メインに判断してほしいこと]
- 節 limits を足した（落とし穴と比べる相手の置き場所）。不要なら外してよい
- 動く図は作らず、公式の Explore the context window へのリンクにした（目次の備考 M8 の「リンクか自作か」の選択）
[提案]
- 数値の提案はなし
- front matter の提案：なし
- 用語集：なし

## inspect-context/review.md
[メインに判断してほしいこと]
- 執筆の判断（節 limits の追加、動く図は公式へリンク）は妥当と見た。そのままでよい

## always-on-costs/write.md
[メインに判断してほしいこと]
- 図なし：型の目安にある「比喩付きの図」を置かなかった
- #why-small の「2026-11-03 に確かめた現行の Best practices が『コンテキストを最大の制約として管理する』をやめてよい表に挙げる」は、束の research/23 §3.1 の写しに基づく。一次資料は未確認なので、検証の担当に確認してほしい
- #reduce の順（測る→外す→CLI→スキル→paths→CLAUDE.md→フック）は「この辞典の推奨」と明記した（公式の順ではない）
[提案]
- 数値の提案なし（数値を本文に書いていない）。feature の目印で load_timing・context_cost を指した
- front matter の変更提案なし

## always-on-costs/review.md
[メインに判断してほしいこと]
- listing tax の説明を足すなら一次資料が要る。
- #why-small の Best practices の記述（2026-11-03）は一次資料で未確認（事実の検証役へ）。

## choose-what-to-read/write.md
[メインに判断してほしいこと]
- アプリでの扱い（添付など）は束に材料がなく「未確認」と書いた。調べる担当が要るか。
[提案]
- 数値：facts-proposal.yml（@ で全文が入る上限。本文は数字なしで、目印を置く場所は caveats）。
- 前提・related の front matter は変更なし。

## choose-what-to-read/review.md
[メインに判断してほしいこと]
- アプリでの添付の扱いを調べる担当が要るか（write.md と同じ）。

## how-memory-works/write.md
[メインに判断してほしいこと]
- 図（static の案）は描かず、#scope の表で代えた。プロジェクトの外の会話がプロジェクトのメモリを読むか、シークレットチャットがメモリを読むかが材料になく、図に断定を書けないため。図が要るなら材料を足してから
- hc-memory の記事の題名が材料の中で 2 つある（05 は旧 URL）。本文は題名を書かず、出典の一覧に任せた
[提案]
- facts-proposal.yml に 2 件（プランごとの既定、過去チャットの検索の対象プラン）。本文は数値・プラン名を書かないので、目印はまだない
- 用語集：「Topics（メモリの項目）」「Pause」「Reset」の追加を提案する（本文で短く説明した）

## how-memory-works/review.md
[メインに判断してほしいこと]
- 強制力の属性が app-memory にない。data に足すか判断を
- 図の案（static）は未作成のまま。材料不足の判断は write.md のとおり

## how-attachments-are-read/write.md
[メインに判断してほしいこと]
- 数値の目印が 1 つもない。data/facts.yml に PDF の上限などの facts がなく、目印を置けなかった。提案（下）が入ったら、{#pdf-and-others} の「境目のページ数と…公式の記事で確かめる」の文と、{#pitfalls} の上限の食い違いの項に目印を置く
- 判断例の「PDF に書き出すと図が残るか」は公式の資料にない（本文は「書き出しの結果次第」と書いた）
- 「強制力」の項目を要点に置かなかった。型の手引きの要求との差をどう扱うか
[提案]
```yaml
proposals:
  - fact: {id: app-pdf-visual-pages, title: アプリで PDF の図まで読まれるページ数の上限, value: 100 ページまで（文字と視覚要素）, sources: [hc-upload-files], checked: 2026-11-04, status: 確認済み}
    used_in: [how-attachments-are-read#pdf-and-others]
  - fact: {id: app-pdf-text-only-pages, title: アプリで PDF の文字だけが読まれるページ数の上限, value: 101〜1000 ページは文字だけ。1000 ページを超えると拒否, sources: [hc-upload-files], checked: 2026-11-04, status: 確認済み}
    used_in: [how-attachments-are-read#pdf-and-others]
  - fact: {id: app-upload-file-size-count, title: アプリのアップロードの大きさと数の上限, value: 会話は 1 ファイル 500MB・最大 20 ファイル、プロジェクトのファイルは 1 ファイル 30MB, sources: [hc-upload-files, hc-files], checked: 2026-11-04, status: 食い違いあり（ファイルの作成の記事はアップロードとダウンロードを 1 ファイル 30MB までと書く）}
    used_in: [how-attachments-are-read#pitfalls]
```

## how-attachments-are-read/review.md
[メインに判断してほしいこと]
- 境目のページ数の目印を置けていない。facts の提案が入ったら、pdf-and-others と pitfalls に目印を置く
- compare の表は機能名が自ページへのリンクになる（生成の仕様）。読者に不要なら表の見せ方を検討

## search-research-thinking/write.md
[メインに判断してほしいこと]
- 呼び出しの回数と時間の目安は、数値ファイルに該当の項目がなかった。本文は数字なしで書き、提案（facts-proposal.yml）に置いた。反映されたら #comparison の「どれだけ広く調べるか」の項に fact の目印を足す。
- compare の表に、リサーチ（using-research 未公開）が「準備中」と出る。web 検索の行は自分のページへ向く（機能の page が自ページ）。生成の仕様なら問題ない。
- 「web 検索と思考」の組み合わせは公式の記事に記述がなく、（推論・実践例なし）を付けた提案として短く書いた。不要なら削る。
[提案]
- 数値：facts-proposal.yml のとおり（2 件）。

## search-research-thinking/review.md
[メインに判断してほしいこと]
- 上記 4 の表の自己リンク。
- 数値の提案（facts-proposal.yml）が反映されたら、目印を足す。

## input-symbols/write.md
[メインに判断してほしいこと]
- 比べる相手の節を「つながる操作」にしたが、これでよいか（comparison ページがない）
- 強制力のバッジが interactive-mode で出るか（値がなければ「未確認」になる）。出さない選択でよいか
[提案]
- なし（用語集・数値・front matter の他のキーへの提案はなし）

## input-symbols/review.md
[メインに判断してほしいこと]
- #compare は comparison ページがないため link の列挙。型の目安を満たすとみなしてよいか
- 強制力のバッジが出るか（data の interactive-mode に値なし）

## permission-modes-overview/write.md
[メインに判断してほしいこと]
- 既定の開始モード（対話は auto、-p は Manual）の値は、目印がないため本文に手で書かず、台帳の行を指した。facts-proposal.yml の 2 件を採用するなら、#defaults に fact の目印を置く
- 緩める側の雛形（acceptEdits や auto の settings）は、守りを先に置く方針で載せなかった
[提案]
- planning/batches/step8/pages/permission-modes-overview/facts-proposal.yml（既定の開始モード 2 件）

## permission-modes-overview/review.md
[メインに判断してほしいこと]
- facts-proposal.yml を採用して #defaults に既定の fact の目印を置くと、読者の目的「既定で何が進むか」に直接答えられる。

## checkpoints-and-rewind/write.md
[メインに判断してほしいこと]
- 公式は、Claude が先にファイル編集の道具で触ったファイルへの、その後の Bash の変更は戻ると書く。summary の「Bash で変えたファイル…は戻らない」は不正確なので、直す案を facts-proposal.yml に書いた。目次の「Bash での変更は戻らない」も同様
- 「強制力」を目印にせず手書きにした件（data の checkpoints に enforcement を足すか、手書きのままでよいか）
[提案]
- 数値：facts-proposal.yml の 2 件（100 件・約 30 日）。本文は数字なしで読める形にしてあり、used_in の節に目印を置く
- front matter：summary の直し（同ファイル）

## checkpoints-and-rewind/review.md
[メインに判断してほしいこと]
- summary の直し（write.md の提案）の採否と、強制力の手書きの扱い

## working-with-git/write.md
[メインに判断してほしいこと]
- 「慣れた」の目安（赤信号の差分を自分で見つけられる・巻き戻しを一度使った）は、束の「慣れるまでは人が握り、慣れたら draft PR」を具体化した私の案。本文で「辞典の目安で、研究で測った基準ではない」と書いた。承認できなければ削る
- 公式の立場の段に、auto モードが止める git の操作（force push・`git reset --hard`・未承認 PR のマージ）を確認日 2026-10-29 付きで書いた。「既定」の語は避けたが、変わりやすい値に当たると判断するなら外す
- 「1 つの PR に 1 つのアイデア、スコアが下がったら戻す」に（根拠：中。複数の実務家の一致）を付けた。束の材料の表記は「中」だけで、一次の記事は開いていない。違えば「弱」へ
[提案]
- 無し（数値の提案なし。本文に変わりやすい値は書いていない）

## working-with-git/review.md
[メインに判断してほしいこと]
- write.md の 3 点（「慣れた」の目安、確認日付きの auto モードの記述、（根拠：中）の印）は未判断のまま。事実の検証は範囲外

## claude-md-length/write.md
[メインに判断してほしいこと]
- 本文で `claude-md-vs-rules-skills-styles` をページ単位で指した（related にない）。related への追加を提案する
- 「月 1 回の棚卸し」「681 行（Kaggle 3 位の自己申告）」「約 2.5k トークン（二次要約）」は根拠：弱として書いた。載せる程度の可否を見てほしい
[提案]
```yaml
frontmatter:
  - {id: claude-md-length, key: related, before: [init-and-first-claude-md, path-scoped-rules, how-skills-load, when-to-lock, emphasis-words, instructions-ignored, pruning-extensions, measure-changes, felt-vs-measured, after-switching-models, share-team-settings, claude-md-loading-order, inspect-context], after: [init-and-first-claude-md, path-scoped-rules, how-skills-load, when-to-lock, emphasis-words, instructions-ignored, pruning-extensions, measure-changes, felt-vs-measured, after-switching-models, share-team-settings, claude-md-loading-order, inspect-context, claude-md-vs-rules-skills-styles], reason: "比べる相手の節で指している"}
```
- 数値の提案はなし（200 行は claude-md-recommended-lines、版は doctor-prompt-audit-min-version を使った）

## claude-md-length/review.md
[メインに判断してほしいこと]
- write.md の related への claude-md-vs-rules-skills-styles 追加の提案に賛成
- 1 の削除した文は、公式の memory の文書で確かめられれば戻してよい（未確認）

## connecting-mcp/write.md
[メインに判断してほしいこと]
1. 型の手引きは要点に強制力の属性を求めるが、mcp の項目に enforcement がない。値を足すなら「お願い」でも「鍵」でもなく、どう分類するかの決めが要る。足りなければこのままでよい
2. 目次の「図の案（static）」に沿って SVG を 1 枚付けた（スコープ 3 種の表と重なる内容）。不要なら外してよい
[提案]
- 数値の提案：facts-proposal.yml（MCP の出力の警告と上限。調査資料 01 G-1 の値で、一次資料では今回確かめていない。status は要確認とした。本文は数字なしで読める）
- 用語集・prh・front matter の提案はなし

## connecting-mcp/review.md
[メインに判断してほしいこと]
- 強制力の属性が data の mcp にないこと（write.md の 1）。このページでは文で代替している

## verification-ladder/write.md
[メインに判断してほしいこと]
- 目次の図の案は「上るほどお願いから鍵に近づく」だが、段 2（/goal）は判定がモデルで、段 4 は別の目なので、鍵に近づく一本の軸にならない。図は段ごとに「お願い・モデルが判定・鍵・別の目」と書き分けた
- モデルの名前（Opus 5 など）は変わりやすい値なので本文に書かず、台帳 `outdated-advice-ledger#add-double-check` と `model-quirks#official-guidance` を指した
[提案]
- なし（front matter の他のキー、用語集、data への提案はない）。`/goal` の条件の字数上限は束の data にないため書かず、goal-until-done 側に任せた

## verification-ladder/review.md
[メインに判断してほしいこと]
- 指摘 3：雛形の `features` を外すか別の値にするか（外すと tracks の最新版が出る）。雛形が最低の版を要しないなら、版の表示を出さない方法の提案が要る

## protect-tests/write.md
[メインに判断してほしいこと]
- 比喩付きの図は置かず、守りの層の図（catalog の visual 案）だけにした。この型の目安の「比喩付きの図」を満たさない。必要なら足す
- #layers の判断例は「推論・実践例なし」の印を付けた
[提案]
- なし（front matter の他のキー・用語集・data への提案はなし）。数値は本文に手で書いていない。研究の値（79% 超、54%→9%）は固定の記録として、研究名・世代付きで本文に書いた

## protect-tests/review.md
[メインに判断してほしいこと]
- 型の目安の「比喩付きの図」を足すか（write.md と同じ論点）

## independent-review/write.md
[メインに判断してほしいこと]
- 「AI の承認を人の承認に数えない」に、claude.dev ブログの原文 1 文を引用した（出典 id claude-dev-blog-solving-code-review-anthropic）。方針の文ではなく、他者の引用として置いた
- #who の表の「責任を持つか」列は、本ページの整理（出典なし）。必要なら弱めてよい

## independent-review/review.md
[メインに判断してほしいこと]
- #4：safety: true の雛形に道具が出す注記が、レビュー依頼の雛形には合わない。safety の付け方の見直しを提案する

## verifier-defines-problem/write.md
[メインに判断してほしいこと]
- 節を 2 つ足した（`#why`・`#misconceptions`）。構成の目安に合わせたもの。外すなら言ってほしい
- 「評価と実験の地図」`#map` は、related 全 12 ページへの手書きの案内にした。hub 的な役割と重なるなら削ってよい
[提案]
- なし（用語集・prh・data・front matter の他キーへの提案はない）

## verifier-defines-problem/review.md
[メインに判断してほしいこと]
- #map を残すか（write.md と同じ論点）。

## felt-vs-measured/write.md
[メインに判断してほしいこと]
- 節 `what-you-keep` を足した（既存の anchor は変えていない）。足さず `why` か `what-to-record` に畳む案もある
- Bastani（PNAS 2025）は、束の出典が RePEc の書誌ページのみ。本文の 48%・17% は research/24 の写しが「17%下が…」で切れており、「対照群と比べた値」は手元の材料では確かめていない
[提案]
```yaml
sources:
  - note: pnas-bastani-2025-genai-learning の URL を PNAS 本体（doi 10.1073/pnas.2422633122）に差し替えるか追加する案。書誌ページでは数値を直接確かめられない
frontmatter: []
```
- 用語集・prh・data への提案はなし。数値の提案（facts-proposal.yml）もなし（研究の結果は固定の記録として本文に書いた）

## felt-vs-measured/review.md
[メインに判断してほしいこと]
- なし（write.md の判断事項に同じ。Bastani の数値は事実の検証役に委ねる）

## measure-changes/write.md
[メインに判断してほしいこと]
- 「数個〜20 個ほど」の task 数は、目次の備考どおり「推論・実践例なし」と本文に書いた。Anthropic の 20〜50 個は「公式の立場」として併記した
- how-many-runs の 95% 区間の式と、勝率 55% の n=100・400 の値は、research/24 B-53 の検算を使った。成功率の試行への当てはめは、本文に「概算」と書いた
- 判断例と結果の表は架空の数字（本文に「架空」と明記）。検証ノートではない
- by-stratum の「層は先に決める」は、この辞典の助言（根拠の印は「中・類推」）
[提案]
- 数値の提案はなし（変わりやすい値は plugin-eval の成熟度を feature の目印で指しただけ）
- 用語集への提案：task・trial・grader・transcript・outcome・pass@k・pass^k（本文の terms で短く定義した）
- front matter の提案はなし（signs・aliases は変えていない）

## measure-changes/review.md
[メインに判断してほしいこと]
- 148 行の長文は、括弧内の英語と出典リンクで長い。分割は軽微なので直していない
- 71 行の警告は文頭「測る前に整える守りが 2 つある」の段落。直す価値は低い

## verifier-three-conditions/write.md
[メインに判断してほしいこと]
- 「想定の場面」（CSV 変換の判断例）は束に根拠がない業務の例。事実の主張ではなく想定として書いた。実例が要るなら別途探す
- 図は置いていない（図の案なし）
[提案]
- なし（front matter・用語集・数値の提案はなし）

## verifier-three-conditions/review.md
[メインに判断してほしいこと]
- 想定の場面（CSV 変換）は根拠のない想定の例。write.md と同じ

## test-the-verifier/write.md
[メインに判断してほしいこと]
- 研究の数値（CORE-Bench 42% → 95%、96.12 と 96.124991…）は、card §7 の「研究の結果は固定の記録」に従い、モデル名・日付・条件を添えて本文に書いた。目印にしていない
- `tests/proposed/`・`tests/frozen/` は例示のパスとして本文に書いた。A-4 の deny ルール（`Edit(/tests/frozen/**)`）の具体は freeze-eval-assets に任せ、本文では繰り返していない
[提案]
- 用語集：「検証器」「red/green」「凍結」が用語集にあるか未確認。なければ追加を提案する
- front matter の提案：なし

## test-the-verifier/review.md
[メインに判断してほしいこと]
- なし（用語集の「検証器」「red/green」「凍結」の有無は write.md の提案のまま）

## selection-pressure/write.md
[メインに判断してほしいこと]
- Fishtest FAQ の「おおむね 4〜5 回」は変わりうる慣行なので、本文に手で書いた（FAQ の引用として、根拠の印付き）。fact 化するなら下の提案を採り、本文を目印に差し替える
- 53 件中 16 件（約 30%）は二次の報道 1 本で原典未確認。根拠：弱と明記して本文に置いた（summary・signs には不使用）。不要なら削る
[提案]
```yaml
proposals:
  - fact: {id: fishtest-retry-cap, title: Fishtest が同じアイデアの再挑戦に置く上限（回数の目安）, value: "おおむね 4〜5 回", sources: [github-official-stockfish-fishtest], checked: 2026-11-05, status: 束の材料（research/24 B-50）による。FAQ 本文は未再確認}
    used_in: [selection-pressure#retry-cap]
```

## selection-pressure/review.md
[メインに判断してほしいこと]
- 「おおむね 4〜5 回」を fact 化するか（write.md の提案）。

## when-to-lock/write.md
[メインに判断してほしいこと]
- 面ごとのタブは置かなかった。材料に app・api の鍵の手段がなく、`#where-to-move` で `request-lock-table#by-surface` を指すだけにした。
- 判断例「小さな直しにとどめて」は、材料（design §10.5 の判断を含む規則の例）から一般化した例で、公式の事例ではない。不要なら外してよい。
[提案]
なし。

## when-to-lock/review.md
[メインに判断してほしいこと]
- 判断例「小さな直しにとどめて」は一般化した例（write.md と同じ）。

## what-auto-mode-stops/write.md
[メインに判断してほしいこと]
- 数値の置き方：誤検知率 0.4%・見逃し率 17%・5.7% は、card §7 の「研究の結果は固定の記録」に当たると読み、記事の日付・データの種類・n を添えて本文に書いた（根拠：中）。目次の notes は「数値は data に置く」とあるので、data に置くなら facts-proposal.yml の 2 件目を採り、本文を fact の目印に替える。連続 3 回／合計 20 回の上限は本文に書かず、1 件目の提案にした（本文は「一定の回数」）
- 強制力の書き方：data の auto-mode に enforcement がない前提で、要点の「強制力」を手書きの文にした。feature の目印を使える形（enforcement の値か、値なしの表示）にするか決めてほしい
[提案]
- facts：facts-proposal.yml
- 用語集：「分類器（auto モードの）」は本文で「別のモデル（分類器）」と短く定義した。用語集に入れるか決めてほしい
- 台帳：yolo-skip-permissions の `now` と本文の勧めは合っている。変更の提案なし

## what-auto-mode-stops/review.md
[メインに判断してほしいこと]
- 要点の「強制力」を手書きにしたこと（write.md 参照）

## sandboxing/write.md
[メインに判断してほしいこと]
- default-reads・fail-if-unavailable の「既定」を本文で文として書いた。facts の目印にするなら facts-proposal.yml を採用してほしい
- 目次の「検証ノート（制作の WSL2 での実測）」は未実施のため書いていない
[提案]
- front matter は変更提案なし

## sandboxing/review.md
[メインに判断してほしいこと]
- 「検証ノート」は未実施のまま。判断例「コンテナの中で動かすか」の「選んだもの」は条件つきで、どちらも筋が通る形のため残した。

## default-safety-settings/write.md
[メインに判断してほしいこと]
- 面ごとの既定の値（開始モード・アプリの Auto／Manual・サンドボックスの有無・シークレットの保持）は、既定値なので本文に手で書かず、観点ごとに確かめ先の節を指した。下の提案の facts を data に足したら、#defaults-by-surface の観点の箇条に fact の目印を置く（used_in に書いた）
- 節の見出しが「面ごとの既定（生成の表）」で、title が「（生成の表）」を含む。読者に見える見出しとして不自然なので、title の変更を提案する（anchor は変えない）
- #by-stage は教材の推奨で、安全の既定の変更に当たる。決定 2026-11-03 の内容（公式の既定を基準、任せるからサンドボックスと秘密の読み取りの禁止、無人は使い捨ての環境、預かったデータは契約のある面だけ）のとおりに書いた。「手動のモードで始める」は足していない
[提案]
- facts-default-safety-settings.yml：4 件（claude-code-default-start-mode・app-default-permission-mode・sandbox-default-state・incognito-retention-period）。値は束の data と research の写しから起こしたもので、一次資料を開いて確かめていない
- frontmatter（YAML）：
```yaml
frontmatter:
  - {id: default-safety-settings, key: sections, before: [面ごとの既定（生成の表）], after: [面ごとの既定], reason: "見出しに作り方の注記が出るため"}
```

## default-safety-settings/review.md
[メインに判断してほしいこと]
- 見出し title の「（生成の表）」変更（write.md の提案）
- 組み合わせ方を #limits の下ではなく独立の節にするか（anchor の追加は front matter の変更）

## where-your-data-goes/write.md
[メインに判断してほしいこと]
- 数値の目印を置けていない：data/facts.yml に保持期間などの fact がなく、ない id を指すと止まるため、本文は数字なしで書いた。提案の fact を入れた後、#retention・#local-transcripts・#misconceptions に目印を置く
- プラン名（Free・Pro・Max・Ultra・Team・Enterprise）も変わりやすい値なので書かず「個人向け／商用」で書いた。名前の目印の使い方を決めてほしい
- 学校が配るアカウントの扱いは未確認と書いた（11 p34#215）
- 「API キーで使う Claude Code は API の側」は、束の「API は商用」から読んだ。公式で直接は未確認
[提案]
```yaml
proposals:
  - fact: {id: deleted-chat-backend-days, title: 消した会話がバックエンドから消えるまでの期間（日）, value: 30, sources: [privacy-long-store-data], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: training-opt-in-retention-years, title: 学習への利用を許可した会話が学習のパイプラインに残る最長（年）, value: 5, sources: [privacy-long-store-data, anthropic-news-updates-our-consumer-terms], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: violation-retention, title: 違反と判定された会話の入出力・分類スコアの最長（年）, value: 入出力 2・スコア 7, sources: [privacy-long-store-data], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: feedback-retention-years, title: フィードバックと /feedback・/bug・/share の保持（年）, value: 5, sources: [privacy-long-store-data, cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: local-transcript-cleanup-days, title: Claude Code の手元の記録の既定の保持（日。cleanupPeriodDays で変更）, value: 30, sources: [cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#local-transcripts]
```

## where-your-data-goes/review.md
[メインに判断してほしいこと]
- fact 提案の登録後に数値の目印を置くこと（指摘 5）。それまでは冒頭だけで日数が分からない
- 追加した 2 節（what-it-prevents・misconceptions）を目次の sections に反映すること

## prompt-injection-in-practice/write.md
[メインに判断してほしいこと]
- #patterns に Invariant Labs・Check Point の事例を会社名つき・手口の細部なしで載せた。方針 B1 に照らして問題ないか
- WhatsApp の事例の「確認画面に一部しか見えない形」は隠し方に触れる。強すぎれば削る
[提案]
- 空。research/22 #9（v2.1.317 でアカウントのメールアドレスを送る前に確認）は「入った版」に当たるので本文に書かず。要るなら data の facts に項目を足して #what-works から指す

## prompt-injection-in-practice/review.md
[メインに判断してほしいこと]
- write.md の 2 点（事例の書き方の方針 B1、WhatsApp の「確認画面」の記述）は未回答のまま

