## isolate-with-safe-mode/write.md
[メインに判断してほしいこと]
1. 強制力：data の safe-mode の機能に `enforcement` の値がない。本文の要点では手書きを避け、「止められるもの」の 1 行にした。data に値が入れば `feature safe-mode/enforcement` の目印に替えられる
2. 公式の挙動の記述（外れるもの・管理の方針）は debug-your-config 1 回の取得と束の research による。`--bare` との違いは束の data の note にある範囲（認証が通常どおり）だけを書いた
[提案]
```yaml
proposals:
  - fact: {id: safe-mode-enforcement, title: "--safe-mode の強制力", value: "なし（読み込みを止めるだけ）", sources: [cc-docs-cli-reference], checked: 2026-11-05, status: 要確認}
    used_in: [isolate-with-safe-mode#what-is-disabled]
```

## isolate-with-safe-mode/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- summary の提案：
```yaml
frontmatter:
  - {id: isolate-with-safe-mode, key: summary, before: "権限と管理の設定は効いたままで、安全の設定を外す道具ではない。", after: "認証・権限の仕組み・管理の設定は効いたままだが、自分の deny ルールやフックは外れるので、安全の設定を外す道具ではない。", reason: "本文の権限の段落と食い違わせない"}
```
- 事実と出典は確かめていない（キー割り当てが外れる点などは束にない記述。debug-your-config の取得に基づくと write.md にある）

## tests-first/write.md
[メインに判断してほしいこと]
- when-it-fails の末尾の段落（実践者の報告を（根拠：弱）で一文）は、一次資料を開かず、束の 03 W7 の写しだけに基づく。残すか削るか
- 5 節の追加（guards-first・verify・when-it-fails）はカード §3 の「型の構成は目安」に従った

## tests-first/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。write.md の末尾の段落（根拠：弱）の扱いは作者側の判断のままにした

## shared-artifacts-and-files/write.md
[メインに判断してほしいこと]
- プラン名（Free・Pro・Max・Ultra・Team・Enterprise）と、招待の期限・1 日の上限の数は、本文に手で書かず「個人向けのプラン」「組織向けのプラン」「一定の期間」と書いた。数値の目印は、提案の id が data にまだないため置いていない。facts に入れたら `#who-can-see` に目印を置く
- 競技中の守り（private のリポジトリ・共有リンクの無効化・公開ページへの出力の禁止）を `#revoke` の末尾に（類推）の印で短く書いた。材料は research/11 の表の 1 行のみで、強さの印が弱い。残すかの判断を頼む
[提案]
```yaml
proposals:
  - fact: {id: chat-sharing-plans, title: 会話の共有のしかたとプランの対応（招待は全プラン、公開リンクは個人向けのプラン、組織向けのプランは組織の中だけ）, value: "招待：Free・Pro・Max・Ultra・Team・Enterprise／公開リンク：Free・Pro・Max・Ultra／組織の中だけ：Team・Enterprise", sources: [hc-share-chats, hc-share-people, hc-share-public], checked: 2026-11-04, status: 確認済み}
    used_in: [shared-artifacts-and-files#who-can-see]
  - fact: {id: chat-sharing-invite-expiry, title: 開かれない招待が切れるまでの期間と、1 日に招待できる人数の上限, value: "期間：30 日（上限の人数は材料にない）", sources: [hc-share-people], checked: 2026-11-04, status: 要確認}
    used_in: [shared-artifacts-and-files#who-can-see]
  - fact: {id: chat-sharing-file-limit, title: コード実行で作ったファイルを含む会話を公開リンクで共有できないプラン, value: "Free・Pro・Max・Ultra", sources: [hc-share-chats, hc-files], checked: 2026-11-04, status: 確認済み}
    used_in: [shared-artifacts-and-files#who-can-see]
```
- data の提案：features の `chat-sharing` の `since` が未確認。tracks の `chat-sharing` はすでにある。`artifacts-overview` への `used_in` は不要
- 用語集：「写し（snapshot）」を、共有した時点の内容の複製の意味で入れる案

## shared-artifacts-and-files/review.md
[メインに判断してほしいこと]
- write.md の 2 点（数値の目印の追加、競技中の守りの段落を残すか）を引き続き判断してほしい

## claude-md-loading-order/write.md
[メインに判断してほしいこと]
- 一次資料として code.claude.com/docs/en/memory を 1 回開いた（Web の取得 1 回）。/context all の Memory files、/memory、Loaded の行、InstructionsLoaded フック、claudeMdExcludes の例、CLAUDE.local.md の worktree の注意、サブフォルダの CLAUDE.md の大きさの上限は、束になくこの文書から書いた
- 木の図は SVG ではなく code ブロックの文字の木にした（visual 案は static の図）。SVG が要るなら別の担当へ
[提案]
```yaml
proposals:
  - fact: {id: claude-md-import-max-hops, title: "@import の入れ子の段数の上限", value: "4 段（ホップ）", sources: [cc-docs-memory], checked: 2026-11-05, status: 確認済み}
    used_in: [claude-md-loading-order#import]
  - fact: {id: claude-md-on-demand-size-limit, title: "後から読まれるサブフォルダの CLAUDE.md・rules のファイル単位の大きさの上限（コンテキストの大きさごと）", value: "200K のコンテキストで 40,000 字（ほかは公式の文書の表）", sources: [cc-docs-memory], checked: 2026-11-05, status: 要確認}
    used_in: [claude-md-loading-order#limits]
```
- 上の 2 つは本文では数字を書かず、used_in の場所に目印を足せる。段数は調査資料 01 A-1 から、大きさの上限は公式の文書から
- front matter・用語集・prh の提案はなし

## claude-md-loading-order/review.md
[メインに判断してほしいこと]
- なし（write.md の SVG 図の件と数値の提案は、そちらのとおり）

## suspect-too-good-results/write.md
[メインに判断してほしいこと]
- 束の 6.3 のとおり、「漏洩変数で QWK≈1.0、LB 0.44」の例は原典未確認なので、本文に使っていない
- 「2倍を超える向上」の目安は規則として書かず、「桁違い」「改善の幅が不自然に大きい」とした
[提案]
- 用語集・prh・data・front matter への提案はない

## suspect-too-good-results/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 事実と出典は確かめていない。write.md のとおり、雛形の動作と PERFOPT-Bench・SpecBench の原典は未確認

## insights-and-usage-review/write.md
[メインに判断してほしいこと]
- data の features（insights・usage）に強制力がない。「なし」を足せば、要点の文を `feature enforcement` の目印にできる。足すかの判断をお願いしたい
- 要点の強制力の行は手書きの「なし」。`/usage` の推奨を自動で適用する操作がある版もあり（01 M）、見るだけの間は「なし」と書いた。適用の操作は版の数値を書かず「用意されている版もある」とだけ書いた
[提案]
```yaml
frontmatter: []
```

- 用語集・prh・data の提案はなし

## insights-and-usage-review/review.md
[メインに判断してほしいこと]
- data の features（insights・usage）に強制力を足すか。足せば、要点の強制力の行を `feature enforcement` の目印にできる（write.md と同じ提案）

## browser-agent-cautions/write.md
[メインに判断してほしいこと]
- 束の材料 6.3 は The Register を出典にしていたが、theregister.com は AI の利用を断るドメイン（check_noai.py で noai）。資料にせず、同じ内容の Anthropic の公式ブログ（claude.com/blog/claude-for-chrome）を 1 回取得して数値（29 シナリオ・123 件・23.6%・11.2%・35.7%→0%）を確かめ、出典に足した。材料の写しの出典を差し替える必要がある
- 新しい出典 claude-for-chrome-blog を data/sources.d に置いた（check_noai は通過）。ほかのページが同じ URL を足していないか、反映時に確認してほしい
[提案]
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし。変わりやすい値（成熟度・版・プラン）は本文に書かず、数値の提案もなし。ブログの試験結果は研究の時点の記録として、時点・対象つきで本文に書いた

## browser-agent-cautions/review.md
[メインに判断してほしいこと]
- 警告 1 件は browser-control の題名「…選ぶ」を含む生成テキスト由来。放置してよいかの判断

## check-billing-path/write.md
[メインに判断してほしいこと]
- 節「経路が決まる順」の 2（`ANTHROPIC_AUTH_TOKEN`）と 4（`apiKeyHelper`）の課金先は、束の材料にないので「確かめていない」と書いた。一次資料で確かめるなら追記する
- 対象のプランと月の額は本文に書かず、公式の記事への link にした。数値の提案（下）が data に入ったら fact-table か fact の目印に替える
[提案]
```yaml
proposals:
  - fact: {id: api-credits-eligible-plans-and-amounts, title: プランに付く月の API credits の対象と額, value: "Max・Ultra・Team が対象（額は Max 100 ドル、Ultra 200 ドル、Team は席ごとの額の合算で月 500 ドルまで）。Free・Pro・Enterprise は対象外", sources: [hc-api-credits], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#monthly-api-credits]
  - fact: {id: api-key-env-p-mode-uses-key-without-confirmation, title: ANTHROPIC_API_KEY があるとき claude -p は確認なしにその鍵を使う, value: "変数があれば必ずその鍵を使い、Console の組織に API の従量の料金がかかる。対話では最初に一度確認が出る", sources: [cc-docs-authentication, hc-claude-code-plan], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#api-key-in-env]
  - fact: {id: auth-precedence-order, title: Claude Code の認証の優先順位, value: "クラウドの提供元 > ANTHROPIC_AUTH_TOKEN > ANTHROPIC_API_KEY > apiKeyHelper > CLAUDE_CODE_OAUTH_TOKEN > profile と federation > /login", sources: [cc-docs-authentication], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#how-the-path-is-chosen]
```
本文の該当箇所は今は地の文（確認日は 2026-11-04 と手書き）。上の fact が入ったら目印に替える。

## check-billing-path/review.md
[メインに判断してほしいこと]
- 雛形の直し（指摘 2）：手順 3 で見つけたときも found=1 にするか、最後の文言を分けるか。snippet の持ち主が直す
- stage は draft のまま（直しの差分を別の担当が確かめていないため）

## model-based-grading/write.md
[メインに判断してほしいこと]
- 手順の「人が先に採点した例を集める」の件数は書いていない。公式の評価の記事の「20〜50 個のタスク」は、数値の提案にせず、measure-changes#small-eval を指すにとどめた。必要なら数値の提案を別に起こしてほしい
- 「人の点を見せる前に採点役の点を人に見せない」「一致の線は結果を見る前に決める」「測る例は依頼の例と分ける」は、束の材料（hold-out は人が持つ、聞き方で迎合が増える）からの運用上の整理であり、出典付きの主張ではない。本文は断定の形にしたが、根拠の印は付けていない。弱いと判断するなら（推論・実践例なし）の印を足してほしい
- 失敗したときの節は、症状ページ（misses-broken-evaluation など）を束の指せる節に含まないので指していない。振り分けたければ、related への追加の提案が要る
[提案]
```yaml
frontmatter: []
```
- 用語集：「較正（calibrate）」「判定役／採点役」を、このページでは「採点役の点を人の点に近づけるために採点の依頼を直す作業」と短く定義して使った。用語集に無ければ追加の提案
- 数値の提案：なし（本文に変わりやすい値を書いていない）

## model-based-grading/review.md
[メインに判断してほしいこと]
- 上の 5 の運用上の整理に（推論・実践例なし）の印を付けるか
- 症状ページへの振り分けのため、related への追加の要否

## what-feedback-sends/write.md
[メインに判断してほしいこと]
1. feedback の機能に `enforcement` がない。/feedback は強制の仕組みではないので、要点に「強制力」を置かなかった。必要なら data 側で値（なし）を足すか、feature 型でこの項目を外すかを決める
2. 目次の templates は「なし」。分かりやすさのために、テレメトリを止める env の雛形を 1 つ足した（safety: true）
[提案]
```yaml
proposals:
  - fact: {id: feedback-transcript-share-retention-months, title: セッション評価の後の記録の共有（Yes を選んだとき）の最長の保持期間, value: 6, unit: か月, sources: [cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [what-feedback-sends#what-is-sent]
```
- 束の research/05 4-6 の写し（Data usage より）に「最大6か月」とある。数値の目印が置けないので、本文は数字なしにしてある。fact が入ったら what-is-sent の該当文（「別の上限が付く」）に目印を置く
- 用語集・prh・front matter の提案はなし

## what-feedback-sends/review.md
[メインに判断してほしいこと]
- write.md の提案（記録の共有の最長保持期間の fact）を入れたら、#what-is-sent の該当文に目印を置く
- feedback の機能に enforcement がない件（write.md 1）はそのまま

## compare-hypotheses-in-parallel/write.md
[メインに判断してほしいこと]
- 要点の項目名を、型の既定の形から変えた（「決めるのは人」を足した）。仮説・物差し・採否は人が決める、という catalog の notes（requirements §6.3）を要点に出すため
- 「失敗したとき」に症状ページへの振り分けはない（routes が空で、束に症状ページがない）。当たった形ごとに、指せる節へ送った
[提案]
- front matter、用語集、data への提案はなし
- 根拠の印は付けていない。「負けた案は取り込まないので衝突の解決が要らない」は仕組みから言えることとして書いた（catalog の根拠は「実践（章:中）」）。印が要るなら、メインが付ける

## compare-hypotheses-in-parallel/review.md
[メインに判断してほしいこと]
- 44 行目の再検査をバッチの検査で確かめてほしい

## agent-view-and-background/write.md
[メインに判断してほしいこと]
- 要点の「強制力」：features の agent-view・cross-session-messaging に `enforcement` の値を足すか、この型でも強制力の行を省いてよいかを決めてほしい。いまは文章で代えた
- 本文の「確認 2026-11-05」は、公式の agent-view と cross-session-messaging の文書を今日取得して確かめたことによる。data の checked は 2026-11-04 のまま
[提案]
```yaml
frontmatter: []
proposals:
  - fact: {id: agent-view-worktree-delete, title: "agent view で消すと worktree も消える（未コミットの変更があっても。未 push のコミットがあると消せない）", value: "挙動の記述", sources: [cc-docs-agent-view], checked: 2026-11-05, status: 確認済み}
    used_in: [agent-view-and-background#pitfalls]
```
上の提案は任意。本文は目印なしで挙動を文章で書き、「確認 2026-11-05」を付けた。`features` の note に入れる案でもよい。用語集への追加の提案はなし。

## agent-view-and-background/review.md
[メインに判断してほしいこと]
- 上の警告が消えたかを、メインの検査で確かめてほしい
- 強制力の値を features に足すか（write.md の件）

## when-ai-is-unavailable/write.md
[メインに判断してほしいこと]
- 障害の事例（2026-08-16 の報道）は、備考の指示どおり使っていない。日付を一次資料で確かめれば足せる
- 「公式の稼働状況の情報」へのリンクは、URL を確かめていないので手書きのリンクにしていない。status 系の出典を data に足すかどうか
- {#fallbacks} の「API は、プランの枠とは別の経路」は、link 先の usage-credits-basics#vs-api-credits と facts の note（API キーでは Wrap-Up Allowance・自動の継続が効かない）に基づく書き方で、API の上限の中身は書いていない
[提案]
- front matter・用語集・data への提案は、なし

## when-ai-is-unavailable/review.md
[メインに判断してほしいこと]
- 指摘 3：雛形の「要る最低の版」の表示を消すために、expect.yaml の features を空にするか
- stage は draft のまま（直しを別の担当が確かめていないため）

## evaluators-by-format/write.md
[メインに判断してほしいこと]
- 出典：このページの sources は空のまま。本文の研究・事例（ISUCON14 の再挑戦の事後報告、Battlecode の事後報告、Kaggle 風の CV 実験のブログ）に付ける出典を、新しいドメインの確認のうえで足すか。この担当は Web を取得していない
- 第三者のツール（pahcer・psyleague など）は、成熟度と確認日を添える決め（DR-17）の材料が束にないので、名前を出していない。必要なら確認日付きで足す
- 誤答で提出が止まる大会の例は、目次の備考に従い、数字を書かず規則の確認に回した
[提案]
- 数値の提案はなし（変わりやすい値は書いていない）
- 用語集：ローカルテスタ、ベンチマーカー、CV、referee（対戦の審判）が用語集にあるかを未確認。なければ追加を提案する

## evaluators-by-format/review.md
[メインに判断してほしいこと]
- 出典が空（write.md のとおり）。事例（ISUCON14・Battlecode・CV 実験）の sources 追加は未了

## ask-for-options/write.md
[メインに判断してほしいこと]
- `sources` が空：束に出典の一覧がなく、材料は調査資料と、実務家の tip（（根拠：弱）で本文に付けた）。公式の文書で裏付けられるなら、出典の追加を頼みたい
- 本文の（類推）は束の C-14（実践・類推）に基づく。強さの付け方に異論があれば直してほしい
[提案]
- 用語集・prh・data への提案なし。front matter の他のキーの変更もなし

## ask-for-options/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま
- write.md の提案どおり、sources が空（公式の文書での裏付けの追加）
- 残りの警告 2 件を直すかどうか

## too-much-project-knowledge/write.md
[メインに判断してほしいこと]
- 強制力の属性：projects の項目に enforcement がない。ナレッジは「使える状態にするだけ」と本文に書いたが、バッジの値は data 側の判断
- 本文は RAG mode の細部（切り替えの時点・表示・読まれる部分）を「確かめていない」と明示した。注記（materials の notes）に従った。公式の説明を追加で確かめるなら、hc-projects-manage の RAG の節の再確認が要る
[提案]
- 用語集：「RAG（mode）」を追加する案。本文では「資料の全体を毎回渡さず、質問に関係する部分を検索で取り出して渡す方式」の一般の意味を短く書き、Claude の実装は確かめていないと添えた
- front matter・数値の提案はなし

## too-much-project-knowledge/review.md
[メインに判断してほしいこと]
- 強制力の属性：data の projects に enforcement を足すか。足すなら要点に一言（お願いか鍵か）を入れる。足さないなら、この型の必須を満たさない理由を決める
- 指摘 5 が残るため、stage は draft のまま
- 用語集への「RAG（mode）」の追加案は write.md のとおり

## incognito-chats/write.md
[メインに判断してほしいこと]
- 強制力：data の incognito 機能に enforcement の値がない。要点には「アプリの仕組みで、お願いではない。保持と管理者への見え方は止められない」と文で書いた。data に enforcement を足すなら、値の提案が要る（鍵のように見えるが、Help Center の記述からの読み取りで、値の語彙に当てはまるかは未確認）
- 「組織向けのプラン」「さらに上位のプラン」と、プラン名を伏せて書いた（プラン名は変わりやすい値のため）。名前を出すなら data に fact が要る
[提案]
```yaml
frontmatter: []
```

- data：incognito-retention-period（status: 未確認）を使った。Help Center（hc-incognito）を 1 回開いて、30 日の既定・Enterprise の扱いが記述と合うことは見たので、status を確認済みにする提案
- 用語集：monthly recap の訳を「月次のふり返り」とした。用語集にあれば合わせる

## incognito-chats/review.md
[メインに判断してほしいこと]
- 指摘 3・4（上記）。
- 指摘を 2 件直したので stage は draft のまま。

## pitfalls-of-ai-written-tests/write.md
[メインに判断してほしいこと]
- 図（比喩付き）は置かなかった。このページは落とし穴と確かめる手が中心で、既存の比喩に合うものがなかったため。必要なら図の案を別途
- 数値の扱い：束の 59.6〜68.1%（p34#61）と、PBT-Bench の約 31%（p34#63）は、arXiv の要旨を取得して確かめた結果、要旨に見つからなかった（特に 31.4% は「素のプロンプトでの最低の再現率」で、失敗の割合ではない）。そのため本文に書いていない。MutGen の 100% と 4% は要旨で確認でき、「単一の例」と明記して書いた。調査資料側の p34#61・p34#63 の記述は誤読の疑いがある（確認の提案）
[提案]
```yaml
frontmatter:
  - {id: pitfalls-of-ai-written-tests, key: sections, before: [pinning-bugs, weak-tests, test-strength, add-to-untested], after: [pinning-bugs, weak-tests, test-strength, add-to-untested, what-it-helps, misconceptions], reason: "concept の構成（何に効くか・誤解）に合わせて 2 節を追加した（既に反映済み）"}
```

- 用語集：「ミューテーションスコア」「変異」「カバレッジ」を追加してよい（本文で短く定義した）
- 台帳（catalog/verify.yaml）の notes：p34#61・p34#63 は要旨で確認できなかった旨を追記してよい

## pitfalls-of-ai-written-tests/review.md
[メインに判断してほしいこと]
- 指摘 1〜3 を直したため stage は draft のまま（直しの差分を別の担当が未確認）
- 図なしでよいか

## instructing-reviewers/write.md
[メインに判断してほしいこと]
- 「保守的に」「重大なものだけ」で報告が減る話は、公式の Opus 5 向けの文書を出典（api-docs-prompting-opus-5）にしたが、文書は開いていない（束の写しによる）。モデル名・世代は本文に書かず「新しい世代のモデル」とした。モデル別の傾向の数値ファイルがあれば、目印で書き足したい
[提案]
- 該当なし（front matter の sources だけ自分で書いた）

## instructing-reviewers/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。要点を直した後の警告が消えたか、メインの検査で確認してほしい

## instructions-hidden-in-materials/write.md
[メインに判断してほしいこと]
- 方針 B1（decisions 2026-11-03）の写しが束に見つからなかったため、「AI を禁じる課題の隠し指示を外す方法は書かない」は目次の備考だけを根拠に守った。本文に「この辞典では扱わない」の宣言は入れていない（方針の文になるため）
- CTF 大会の例は大会名を出さず「ある CTF 大会」にした。名指しするなら一次資料での確認が要る

## instructions-hidden-in-materials/review.md
[メインに判断してほしいこと]
- 方針 B1 の写しが束にない点（write.md と同じ）。本文は隠し指示を外す方法に触れていない
- stage は draft のまま（直したため）

## when-requests-are-refused/write.md
[メインに判断してほしいこと]
- 変わりやすい値は本文に手で書かず、言い方を避けて数値の提案にした（既定の有効・版・表示の文・分類の名前・課金・対象のモデル・検証の制度の段階）。本文に目印を置く場合の場所は used_in に書いた
- Settings > Capabilities と /config の項目名は、日付（2026-11-04 時点）付きで本文に書いた。名称の扱いとして不要なら外す
- Life Sciences Verification Program は束の材料（research/26）が出典。data/sources.yml に該当の id がなく、本文は出典の id で指していない。出典の追加を提案する
[提案]
- sources：Life Sciences Verification Program の公式の記事を data/sources.yml に足す（URL は未取得）
- 数値：facts-proposal.yml のとおり

## when-requests-are-refused/review.md
[メインに判断してほしいこと]
- 段階は draft のまま（直したため）。別の担当の確認で reviewed にする
- 上の 76 行の警告の文を「1・3・4 は重ねてよい」に縮めると消えるはず（メインが流す検査で）

## before-using-top-model/write.md
[メインに判断してほしいこと]
1. 公式の食い違い（research/26 #22 の続き）：Fable の記事は「別の週の上限はなく、通常の週の上限の内側」と書く（2026-11-05 に WebFetch で確認）。Max・Ultra の記事と facts の `usage-limit-types-by-plan`・features の `usage-limits` の note は「別の週の上限」と書く。本文は Fable の記事に合わせ、警告の囲みで 3 通りの書き方を並べた。how-usage-limits-work#limit-types の最後の箇条（「Max と Ultra には最上位のモデル向けに別の週の上限がある」）と表の列名の見直しを提案する
2. #which-limit のプラン別の分け方（含まれる／usage credits／API 料金／使えない）を、数値ファイルがないため文の箇条で手書きした。下の提案の表の fact を足したら、箇条を `fact-table` に置き換える
3. 名前の扱い：本文は最上位のモデルの名前（Fable）を aliases の行にしか書かない。用語集に「最上位のモデル」の定義を置くかは任せる
[提案]
```yaml
proposals:
  - fact: {id: top-model-by-plan, title: 最上位のモデルの引かれ先（プランごと）, value: "Max・Ultra・Team と席ごとの Enterprise の premium seat は通常の週の上限の内側（一部まで）。Pro・Team と席ごとの Enterprise の standard seat は usage credits（席ごとの Enterprise は組織が有効にした場合）。使用量に基づく Enterprise と API は標準の API 料金。Free は使えない", sources: [hc-fable-models-plan, claude-pricing, hc-max-plan, hc-ultra-plan], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit, choosing-a-model#plans, choosing-a-plan#plan-table]
  - fact: {id: top-model-weekly-share, title: プランに含まれる最上位のモデルの割合（通常の週の上限のうち）, value: "50%（料金のページは「半分まで」）", sources: [hc-fable-models-plan, claude-pricing], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit]
  - fact: {id: top-model-claude-code-min-version, title: 最上位のモデルを Claude Code で使う最低の版, value: "モデル 5 は 2.1.170、モデル 5.1 は 2.1.255（モデルの世代ごと）", sources: [hc-fable-models-plan], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit]
frontmatter: []
```
- `used_in` の 3 件目の版・割合は、本文に数字を書かず、目印の置き場所だけ #which-limit に想定した。fact が入ったら、割合と版の文に目印を足す
- 正本の更新の提案：facts `usage-limits` の note と `usage-limit-types-by-plan` の「最上位のモデルの別の週の上限」列を、上の食い違いに合わせて見直す

## before-using-top-model/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。write.md の提案（公式の食い違い、fact 3 件）は未反映。
- #which-limit 冒頭の「2026-11-05 に確かめた」は手書きの日付。fact 化したら目印に置き換える。

## data-analysis/write.md
[メインに判断してほしいこと]
- A-8 の雛形は、目次では prompting の prompt-patterns と「snippets の1か所から取り込む」とある。prompt-patterns のページはまだ snippets にないので、この `snippets/data-analysis/observe-and-hypothesize` を正本にした。prompt-patterns の担当に、同じ id を gen の目印で取り込むよう伝えてほしい
- 目次の材料 6.3（ML のリーク、パイプラインの 50%）は、二次要約で原典未確認のため本文に書かず、audit-ml-pipelines と suspect-too-good-results へ link するだけにした
[提案]
```yaml
frontmatter: []
```
用語集・prh・data への提案はなし。変わりやすい値は本文に書いていないので facts-proposal.yml も作らない。

## data-analysis/review.md
[メインに判断してほしいこと]
- write.md の判断事項（A-8 雛形の正本を本ページにしたこと）はそのまま引き継ぐ

## checking-for-updates/write.md
[メインに判断してほしいこと]
- stable の遅れの日数は、目次の備考どおり数値ファイルへ置く案を facts-proposal.yml に書いた。承認までは本文に日数を書かず、目印も置いていない
- 面のタブにある「`/release-notes` の動きは WSL・Linux の CLI 基準、ほかは未確認」の文は、基準の決まりに沿った書き方にした
[提案]
- facts-proposal.yml（上記）
- 用語集：prh が `skills` を `スキル` へ直すと指摘した。本文は「スキル」に直した。`/doctor` と `/release-notes` などのコマンド名は原文のまま

## checking-for-updates/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま（直しの差分は別の担当の確認前）。

## unfaithful-reasoning/write.md
[メインに判断してほしいこと]
- 「なぜそうなるか」の比喩付きの図は置いていない。比喩の一覧に合うものがなく、図の案も無かったため。必要なら別の担当に図の案を頼む
[提案]
- front matter・用語集・data への提案はない。なお signs の goal「なぜその答えになったのか、過程を全部見せてほしい」に、このページは「見せても一致するとは限らない」を答えている（変更の提案ではない）

## unfaithful-reasoning/review.md
[メインに判断してほしいこと]
- 平方根の問いで思考が合っていた例（#what-happens、#misconceptions）と、表の各例のモデルは、事実の確認の対象外とした。出典（tracing-thoughts）で突き合わせてほしい
- 要点の直し後の textlint を、メインの一括検査で確認してほしい

## what-each-surface-cannot-do/write.md
[メインに判断してほしいこと]
- `#gaps-within-a-surface` は、data にない制約（シークレットチャット以外のアプリ内の差・Claude Code のクラウドの設定）を、調査資料（確認日 2026-10-29）から手で書いている。data の features へ入れるか判断してほしい
- 台帳の行 `cowork-separate-app` を link で指した。ページの `outdated_advice` は空のまま（直す提案はしていない）
[提案]
```yaml
frontmatter: []
```
- data の提案：アプリ内の面（Web・Desktop・モバイル）ごとの対応を持つ属性が data にない。表が「アプリ」1 行になる。`features` に面の細分か「統合の後の制約」の項目を足すと、表で出せる

## what-each-surface-cannot-do/review.md
[メインに判断してほしいこと]
- 表がほぼ「アプリ」1 面だけで、題名の「できないこと」を表で引けない。data に面の細分か制約の項目を足すかの判断（write.md と同じ）
- stage は draft のまま（直したため）

## browser-control/write.md
[メインに判断してほしいこと]
- 強制力のバッジ：data の 2 機能に `enforcement` がない。拡張のサイト許可（鍵に近い）と computer use のアプリごとの許可を、どの値にするか決めてほしい。本文は値を書いていない
- 成熟度が面と出典で割れる（data の note どおり）。`computer-use` の節で表記の違いを一文で述べ、表は Help Center の beta に合わせたと書いた。id を面で分けるなら、その一文を直す
- `which-to-use` の表の「届く範囲」の列（コネクタは狭く、画面は広い）は、公式の優先順の理由「速く確実」に私が足した整理である。公式が範囲の広さで順を決めているとは書いていない
[提案]
```yaml
proposals:
  - fact: {id: chrome-extension-requirements, title: Claude in Chrome を Claude Code から使う要件（拡張の版・対応ブラウザ・プラン・認証の方法・WSL）, value: "拡張 1.0.36 以降。Chrome・Edge と、検出される Chromium 系。直接の Anthropic のプラン（Pro・Max・Ultra・Team・Enterprise）。/login での認証が要る（API キーと setup-token では無効）。WSL は非対応。第三者のプロバイダー経由は不可", sources: [cc-docs-chrome], checked: 2026-11-05, status: 確認済み}
    used_in: [browser-control#claude-in-chrome]
  - fact: {id: computer-use-requirements, title: computer use（Cowork・Desktop）の対象のプランと OS, value: "macOS・Windows の Desktop。Pro・Max・Ultra。Team と Enterprise は対象外（beta）。投資・取引・暗号資産のアプリは既定でブロック", sources: [hc-computer-use], checked: 2026-11-05, status: 確認済み}
    used_in: [browser-control#computer-use]
```
- 本文はどちらも数字なしで、公式を指す書き方にした。ids が承認されたら、`claude-in-chrome` の節のタブと `computer-use` の節のタブに fact の目印を置く
- Help Center の入門（hc-claude-in-chrome）は、Chrome のみ・有料プランと書く（調査資料 02 §1-12、確認日 2026-10-29）。Claude Code の文書（cc-docs-chrome）は Chrome・Edge と Chromium 系を挙げる。公式同士の食い違いなので、上の提案は両方の出典を持たせるのがよい
- 用語集：「サンドボックス」は prh が sandbox を直したので問題なし。追加の提案はなし

## browser-control/review.md
[メインに判断してほしいこと]
- 強制力のバッジ：data の 2 機能に enforcement がなく、要点に出ない（write.md と同じ）
- 指摘 2〜3 を直したため、stage は draft のまま

## output-shape/write.md
[メインに判断してほしいこと]
- 節の順は mirror → length → where → guaranteed → effects → limits。技法の目安（なぜ効くか）が終盤に来るので、入れ替えたほうがよいなら指示がほしい
[提案]
なし（データ・用語集への提案はない）。

## output-shape/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。#where の面別の書き分けは箇条（タブでない）にしてある。タブにするかは判断してほしい

## manual-only-skills/write.md
[メインに判断してほしいこと]
- 面のタブは、surfaces が claude-code だけなので置かず、本文で「Claude Code のスキルの設定」と書いた
- 束の備考どおり、「sign の言い換えにも読める does-more-than-asked」へは need-lock の末尾で 1 回だけ指し、このページが直接の答えになる場面を狭く書いた
[提案]
- 用語集：特になし
- 数値の提案：なし（本文に数値・版・既定値を手で書いていない）

## manual-only-skills/review.md
[メインに判断してほしいこと]
- ask ルールの `Bash(./scripts/deploy.sh *)` の書式は、permission-rules のページと突き合わせていない（事実の検証は置かない）。動作確認の担当に任せたい

## check-the-metric/write.md
[メインに判断してほしいこと]
- OpenAI の出典（openai-expanding-on-sycophancy）：取得が 403 で本文を開けなかった。題名「Expanding on what we missed with sycophancy」と公開日 2025-05-02 は記憶による仮のもの。本文の記述は調査資料（10-contest-supplement.md）の要約に拠る。メインが開いて、題名・日付・内容（オフライン評価と A/B テストが良かった、専門テスターの懸念、ロールバック）を確かめてほしい
- CVPR の出典：published の `2023-06-01` は仮の値（大会の年から）。題名と要旨はポスターのページで確かめた
- 既存の出典の lukyanenko-kaggle-antigravity-s6e7 は開いていない（束と調査資料に拠る）。「accuracy と balanced accuracy」「CV 0.967・LB 0.874」を、ブログで確かめてほしい。本文の根拠の印は（根拠：弱）にした（材料は弱〜中）
- カード §1 は sources を「既にある id だけ」としているが、新しい出典 2 件を sources.d に足して sources に入れた（カード §8 の「新しい出典は sources.d」に従った）
[提案]
- 数値の提案なし。本文の数値（0.967・0.874・80 件・2025 年 4 月）は研究の時点の固定の記録として扱った（カード §7）
- front matter の提案なし。用語集・prh への提案なし

## check-the-metric/review.md
[メインに判断してほしいこと]
- 指摘が 1 件（直したほうがよい）あったので stage は draft のまま。直しの差分は別の担当の確認待ち
- write.md の出典の未確認（OpenAI の題名・日付、Kaggle のブログの数値）は未解決のまま

## differential-testing/write.md
[メインに判断してほしいこと]
- USACO Guide の出典は、実際に開くと、ストレステストの詳しい手順ではなく「生成器を書き、遅い単純解と比べる」の 1 文だけだった（詳細は別の節への案内）。本文は 1 文の範囲に抑え、根拠は弱とした
- 「deny ルールやフックで止める」は、リンクなしの一言にした（enforce 分野の対応ページの id が束にないため）。必要なら link を足してほしい
[提案]
- front matter：なし
- 用語集：「愚直解」「本解」を本文で短く定義した（用語集にあるかは未確認）。なければ追加の提案
- data：数値の提案なし。研究の割合（59.6〜68.1%）は研究名と年付きで本文に置いた

## differential-testing/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 「deny ルールやフック」にリンクがない件は write.md のとおり、enforce 分野の id が束にないため据え置き

## move-judgment-into-scripts/write.md
[メインに判断してほしいこと]
- 「なぜそうなるか」の図は置かなかった（比喩が「お願いと鍵」だけで、文章で足りると判断した）。図が要るなら別の担当に頼む
- 1 件の研究の根拠（入力の縮小）は、束に研究の名・年・対象モデルがないため、「調査資料が拾った 1 件の研究」と書き、（根拠：中・類推）を付けた。名・年・対象は入れていない
[提案]
- 数値の提案・front matter の提案・用語集などへの提案：なし

## move-judgment-into-scripts/review.md
[メインに判断してほしいこと]
- 研究の名・年・対象モデルが束にない。出せるなら 1 次資料の確認を別途

## loop-and-scheduling/write.md
[メインに判断してほしいこと]
- 目次の notes は、アプリのタスクと定期実行を「タブではなくリンクで送る」とあるので、面のタブは置かず、`tasks-and-schedules-in-the-app#where-it-runs` へのリンクにした。front matter の surfaces に app があるのと、Desktop scheduled tasks がアプリ（Claude Code Desktop）で動くことの整理は、メインの判断に任せる
- `compare` の目印は、tracks の 2 機能の属性をそのまま出す。scheduled-tasks はクラウドとDesktop の両方を指す項目なので、表の読み方に誤解が出ないか、生成後に見てほしい
[提案]
数値の提案（本文には数字を書かず、公式の文書で確かめるよう促した。used_in の節に目印を置ける）。出典は cc-docs-scheduled-tasks（確認 2026-11-05、WebFetch 1 回）。

```yaml
proposals:
  - fact: {id: loop-recurring-expiry-days, title: セッション内の繰り返しの失効までの日数, value: 7, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: loop-max-tasks-per-session, title: 1 セッションに置ける予定のタスク数の上限, value: 50, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: loop-min-interval, title: /loop の最小の間隔, value: 1 分, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
  - fact: {id: loop-self-paced-interval-range, title: 間隔を省いた /loop で Claude が選ぶ間隔の範囲, value: 1 分から 1 時間, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: desktop-scheduled-task-min-interval, title: Desktop の予定のタスクの最小の間隔, value: Claude が設定すると 1 分、フォームでは 1 時間, sources: [cc-docs-scheduled-tasks, cc-docs-desktop-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
  - fact: {id: cloud-scheduled-task-min-interval, title: クラウドの予定のタスクの最小の間隔, value: 1 時間, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
```

用語集の提案：なし。front matter の提案：なし。

## loop-and-scheduling/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- surfaces に app があるが、面のタブは置かず、アプリの定期実行はリンクで送っている（目次の notes どおり）。整理はメインの判断に任せる
- 追加した Desktop の説明（新しいセッションが立ち上がる、手元のファイルを読める）は、事実の確認を別の担当に頼む

## usage-credits-basics/write.md
[メインに判断してほしいこと]
- usage-credits の機能の属性（強制力・読み込みの時期など）が data にない。feature 型の「強制力」の項を置けていない。属性を足すか、このページは項を省くかを決めてほしい
[提案]
```yaml
proposals:
  - fact: {id: usage-credits-expiry-japan, title: usage credits の失効の期間（日本など）, value: "購入から 6 か月（2026-09-10 以降の購入分）", sources: [hc-usage-credits], checked: 2026-11-04, status: 確認済み}
    used_in: [usage-credits-basics#how-it-works]
```

本文は今、期間を書かずに「公式の記事で確かめる」としている。fact が入れば、#how-it-works の失効の段落に目印を置く。

## usage-credits-basics/review.md
[メインに判断してほしいこと]
- 強制力の属性を data に足すか（write.md と同じ）。足したら、要点に `feature` の目印を入れる
- stage は draft のまま（直しの差分を別の担当が確かめていないため）

## build-test-harness/write.md
[メインに判断してほしいこと]
- 図の案（解・評価・記録を分けた構成図）は描かず、同じ内容を雛形 `repo-layout` で出した。図が要るなら別途
- `separate-eval-assets` は「縛る」の置き場所の話で、実際の止め方（deny・サンドボックス）は freeze-eval-assets へ送った。節の順は目安から少し外し、守りの節を先頭に足した
[提案]
- 用語集・数値・front matter の提案はなし

## build-test-harness/review.md
[メインに判断してほしいこと]
- 図の案（構成図）は描かれていない。repo-layout の雛形で足りるとみなした。図が要るなら別途

## office-paperwork/write.md
[メインに判断してほしいこと]
- 節の並び：手順の節（human-ai-human）が、守りの節（work-folder・private-data）より先にある。目次の sections の順を変えないために保った。守りを先にするなら、並べ替えの許可がほしい
- `#work-folder` に「確認が出る既定のまま始める」と書いた（モードの具体名は書かず、段階の判断は default-safety-settings#by-stage に任せた）。decisions 2026-11-03「安全の既定の勧め方」と矛盾しないかの確認がほしい
- アプリのスキル（page: skills-in-the-app）は、束の「指せる節」にないので link していない。本文は「アプリ側の設定は面ごとに違うので公式の文書で確かめる」とした
[提案]
- 数値の提案：なし（本文に変わりやすい値を書いていない）
- front matter の提案：なし
- 用語集・prh：なし

## office-paperwork/review.md
[メインに判断してほしいこと]
- 節の並び（手順が守りより先）は write.md の判断事項のまま。目安どおりにするなら sections の並べ替えの許可が要る

## requesting-prose/write.md
[メインに判断してほしいこと]
- 本文の「公式のモデル別の手引きにも…装飾的な文体を外すよう一文で頼む例がある」は、モデル名を書かず（今のモデル名は目印で書く決めのため）、束 6.3 の Fable 5.1 の手引きの一文に基づく。出典 id は sources に入れた。モデル名を出す要不要の判断をお願いする
- 「AI っぽい」は読みやすさの品質として扱い、AI が書いたと分からなくする方法は書いていない（方針 B4）
[提案]
- なし（front matter・用語集・data への提案はない）

## requesting-prose/review.md
[メインに判断してほしいこと]
- 本文でモデル名を出さずに Fable 5.1 の手引きに触れる件（write.md の判断依頼）は、分かりやすさの上では問題なし。モデル名を出す要不要は事実の側の判断

## build-on-results/write.md
[メインに判断してほしいこと]
- 11 の注記にある「分野04（prompting）に置く案」は採らず context のまま書いた（目次の決定どおり）。refine-in-conversation とは `#effect` の「依頼の言い方がずれている」で結んだ
- 目次の「訂正が 2 回失敗したら /clear」という数字は、変わりやすい規則の値になりうるので本文に書かず、「訂正を重ねても直らないとき」と言い換えた
[提案]
- 用語集・prh・data への提案はなし。front matter の他キーの直しもなし

## code-intelligence-plugins/write.md
[メインに判断してほしいこと]
- data の features の `code-intelligence` に `enforcement` の値がない。冒頭の「強制力」は、目印を使わず文で「止める働きはない」と書いた。`enforcement: なし` を足せば `<!-- gen:begin feature enforcement -->` に差し替えられる（下の提案）
- 公式の文書にある言語ごとのプラグイン名・実行ファイルの対応表は載せず、公式へのリンクにした（カード §12 の網羅を避ける方針）。`/plugin install typescript-lsp@claude-plugins-official` の 1 行だけ例に載せた。マーケットプレイス名は変わりうる値なので、気になれば数値の目印に直す
[提案]
```yaml
data:
  - {feature: code-intelligence, key: enforcement, after: なし, reason: "診断は自動で返り、LSP の道具は読み取り専用で、Claude の動きを止めない（公式 code-intelligence の文書）。冒頭の強制力を目印に差し替えるため", used_in: [code-intelligence-plugins#top]}
```
front matter の提案、用語集・prh への提案はない。

## code-intelligence-plugins/review.md
[メインに判断してほしいこと]
- 「直す」「直したほうがよい」を 2 件直したため、stage は draft のまま。直しの差分の確認は別の担当に
- write.md の提案（data の code-intelligence に enforcement を足し、強制力を目印にする）を反映するか

## visual-checks/write.md
[メインに判断してほしいこと]
- 要点の「強制力」の目印が「—」（data の verify-skill の enforcement が null）になる。本文は「値は数値ファイルの登録待ち」と書いた。data への追記後に、この括弧を外してほしい
[提案]
```yaml
proposals:
  - feature_attribute: {id: verify-skill, key: enforcement, value: お願い}   # 値の案。出典 cc-docs-skills で確かめてから
    used_in: [visual-checks#top]
```

## visual-checks/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しを別の担当が確かめていないため）
- 強制力の値（verify-skill の enforcement）を data に入れたら、本文の括弧を外す

## looks-are-not-quality/write.md
[メインに判断してほしいこと]
- `#why` の「比喩付きの図」は置かなかった（一覧に合う比喩がない。表で代えた）。必要なら図の案を頼む
- SpecBench の注記（記憶したコンパイラは Claude の結果ではない）に従い、その例は本文に使っていない
- 修正中に、Write ではなく Bash（python3 で文字列置換）でページを 1 回直してしまった。内容は同じ趣旨の文の短縮だけ
[提案]
- front matter：なし（related の frontend-design・make-slides は本文で指した）

## looks-are-not-quality/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま（別の担当の確認待ち）
- 比喩付きの図の有無（型の目安）は write.md の判断のとおり。必要なら図の案を依頼
- 本文の Anthropic ブログの URL は /research/ 形、束の材料は /engineering/ 形。転送先は未確認（事実の検証は対象外）

## dynamic-workflows/write.md
[メインに判断してほしいこと]
- 強制力：data の features の `workflows` に `enforcement` がないので、`feature workflows/enforcement` の目印を使えなかった。ワークフロー自体は何も強制しない機能なので、要点に「止められるもの」を手書きで足した（「担当の道具には権限ルールと サンドボックス が効く」）。型の「強制力」の項目をどう扱うか（`enforcement: なし` を足すか、この形でよいか）を決めてほしい
- 本文の数値：担当の数・同時の上限・警告のしきい値・規模の目安の段は、数値ファイルに項目がないので本文に書いていない。facts-proposal.yml の 4 件を data/facts.yml に入れてもらえば、`fact-table` や `fact` の目印で足せる
[提案]
- data/facts.yml：facts-proposal.yml の 4 件（workflow-concurrent-agents・workflow-agent-caps・workflow-large-warning・workflow-size-guideline）。出典は cc-docs-workflows、確認日 2026-11-05
- 用語集・prh：なし（check_page で prh が hook・sandbox を指摘したので、本文は「フック」「サンドボックス」に統一した）

## dynamic-workflows/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 強制力：`enforcement: なし` を features の workflows に足すか（write.md と同じ）
- 184 行の警告の直し（任意）

## structured-outputs-basics/write.md
[メインに判断してほしいこと]
- 台帳の link `outdated-advice-ledger#prefill-for-json` を使った。check は通った
[提案]
- なし（数値・用語集・data への提案はなし）。スキーマの複雑さの上限などは数値を書かず、公式への案内にとどめた

## structured-outputs-basics/review.md
[メインに判断してほしいこと]
- 指摘 1 を直したので stage は draft のまま（直しの差分を別の担当が確かめていないため）

