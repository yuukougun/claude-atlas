## lock-side-effects/write.md
[メインに判断してほしいこと]
- `prevents`・`pitfalls` が空。縛りすぎで起きやすい原因の名前を割り当てるかは、メインの判断
- 注釈付きのセッション記録（目次の見せ方 DR-17）は未作成。束に `state/blocks.log` の中身がないため、仮の記録を作らず、判断例（想定の例と明記）と記録 1 行の雛形で代えた。実際の記録から選んだ例を足すなら、メインが材料を渡す
[提案]
```yaml
glossary:
  - {term: 縛る, note: "規則を鍵（フックと権限ルール）に移すこと。本文 #effects で短く定義した。用語集にあるか未確認"}
  - {term: 握る, note: "何を任せ、何を人が決めるかを人が持つこと。同上"}
```
- 用語「回り込み」「止めすぎ」を用語集に足す案（本文で短く定義済み）

## lock-side-effects/review.md
[メインに判断してほしいこと]
- 「直したほうがよい」を直したので stage は draft のまま。注釈付きのセッション記録（DR-17）が未作成なのは write.md のとおり
- `prevents`・`pitfalls` が空のままでよいか

## skills-in-the-app/write.md
[メインに判断してほしいこと]
- 公式同士の食い違い（Help Center と Platform の文書。組織での配布・Claude Code への同期）を、数値なしで「自分の画面と管理者の設定で確かめる」と書いた。プラン名と版は本文に書いていない
- 「2026 年 6 月に告知」は固定の記録として手書きした（台帳の changed.date に合わせた）
[提案]
- 数値・用語集・prh・data への提案はなし

## skills-in-the-app/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま。

## using-research/write.md
[メインに判断してほしいこと]
- 強制力：data の research に enforcement がないため、要点に「リサーチは調べる機能で、条件は依頼に書くお願い」と手で書いた。バッジが要るなら、data の research に enforcement（お願い）の追加を検討してほしい
- 要点の「前提」の link が、生成後に search-research-thinking の題名で出ることだけ確認してほしい
[提案]
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし。使うモデルの名前を本文に出していない（束の data の note が「モデルは facts の値」とするが、research のモデルを指す fact がない）。出すなら次の fact の追加が要る
```yaml
proposals:
  - fact: {id: research-model, title: リサーチが使うモデル, value: 未記入（hc-research で確かめる）, sources: [hc-research], checked: 2026-11-05, status: 未確認}
    used_in: [using-research#when-to-use]
```

## using-research/review.md
[メインに判断してほしいこと]
- 強制力のバッジ：data の research に enforcement を足すか（write.md と同じ）
- fact `research-call-guide` の目印の間に、日付「（2026-10-29 時点）」を手で書いてある。生成で消えるなら、日付を目印の外に出す扱いを確認してほしい（検査は通っている）

## output-style-modes/write.md
[メインに判断してほしいこと]
- 単独のページとして、組み込みの版の数値（Concise の v2.1.237、/output-style の v2.1.269）を本文に書かず「新しい版が要る」とした。数値の提案は下
[提案]
```yaml
proposals:
  - fact: {id: output-style-concise-min-version, title: Concise スタイルが要る Claude Code の版, value: "2.1.237", sources: [cc-docs-output-styles, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#built-in]
  - fact: {id: output-style-command-min-version, title: /output-style コマンドが要る Claude Code の版, value: "2.1.269", sources: [cc-docs-output-styles, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#switch]
  - fact: {id: output-style-setting-case-sensitive, title: outputStyle の値は大文字小文字を区別し、合わない値は Default になる（/output-style コマンドは区別しない）, value: 区別する, sources: [cc-docs-output-styles], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#switch]
frontmatter:
  - {id: output-style-modes, key: related, before: [...], after: [... , permission-modes-overview], reason: "本文で Proactive と権限モードの関係から link した（未宣言のまま指している）"}
```
- 用語集：「出力スタイル（claude.ai の Styles とは別）」の区別は既存。フック（hook）の訳は prh どおりにした

## output-style-modes/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 上の警告 1 件の扱い
- 事実の検証はしていない。Proactive・Concise の挙動の記述は束の外の公式文書に基づくため、事実の担当が確かめる必要がある

## approval-fatigue/write.md
[メインに判断してほしいこと]
- 93%・97%・13.6% は「研究の結果は固定の記録」（カード §7 の最後）として、研究名・日付・出所を添えて本文に書いた。目次の notes は「数値は数値ファイルに出典の日付付きで置く」とあるので、data/facts.yml に置いて目印にする道を選ぶなら、本文の該当 3 か所（why）を直す
- 「サンドボックスで自動許可を有効にすると、囲いの中の Bash は Manual でも確認なしに実行される（例外あり）」は 05 1-10 の写し（cc-docs-sandboxing を引く）に基づく。今日の一次資料では確かめていない
[提案]
- 数値の提案はなし。
- front matter の変更の提案はなし。

## approval-fatigue/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。
- 事実と出典は確かめていない（本検証の対象外）。write.md の判断事項（93%・97%・13.6% を本文に置く件）は未解決。

## settings-layers/write.md
[メインに判断してほしいこと]
- 要点の「強制力」は、tracks の最初の settings に enforcement の値がないため、管理の機能の値を使った。feature 型の「強制力」の行が settings に要るなら、data の settings に enforcement を足すか、置き方の決めが要る
[提案]
- 用語集：「層」（scope）を設定の文脈で定義するか確認。本文は「層」で統一した（公式は scope）
- front matter の変更はなし

## settings-layers/review.md
[メインに判断してほしいこと]
- 指摘を直したため stage は draft のまま（別の担当が直しの差分を未確認）
- 執筆の報告のとおり、feature の「強制力」を settings 自身が持たない点は data 側の判断が要る

## protected-paths/write.md
[メインに判断してほしいこと]
- 外を閉じるキーの版の下限（v2.1.314）を本文に書けないので、数値の提案にした。採用されたら本文の「版の下限は数値ファイルに置く（提案済み）」を目印に置き換える
- 「提案済み」という文が、採用後は古くなる
[提案]
- data/facts.yml：facts-proposal.yml（used_in：protected-paths#outside-working-directory）
- 用語集：critical paths（重要な場所への rm/rmdir の保護）・protected paths の追加を提案

## protected-paths/review.md
[メインに判断してほしいこと]
- facts.yml に block-writes-outside-min-version がまだない。採用後に、タブの版の文を fact の目印に置き換えたい（write.md の提案どおり）

## stop-hooks/write.md
[メインに判断してほしいこと]
- 目次の templates は 1 つだけだが、登録の設定を足して 2 つにした
- 「Stop フックと `/goal` の併用の挙動」は確かめておらず、本文に「確かめていない」と書いた
[提案]
- 数値の提案はなし（上限は既存の fact `stop-hook-block-cap` を使った）
- front matter の提案（YAML）：なし
- 検証ノート（目次 notes の見せ方）は、制作の環境での記録が要るため作っていない

## stop-hooks/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま（別の担当が直しの差分を確かめるまで reviewed にしない）

## open-ended-loop-trap/write.md
[メインに判断してほしいこと]
- 研究の事例（頭打ち・CTF・ISUCON・DrivenData）は、束の写しだけに基づく。出典が sources にないので、本文では実験名・数値（CTF の問数や順位など）を省き、DrivenData の「9 日間・12 位から 7 位」だけ載せた。一次資料を足して sources に載せるか、載せずに残すかを決めてほしい
- 根拠の印：調査資料では頭打ちの実験が「強（単独の実験）」だが、カード §6 の定義（RCT・大規模）に合わせて（根拠：中）にした
- 図：対比の表で代えた。SVG の図が要るなら別の担当で
[提案]
```yaml
frontmatter:
  - {id: open-ended-loop-trap, key: sources, before: [], after: [（頭打ちの実験・DrivenData・ISUCON の一次資料）], reason: "事例の根拠を sources に載せるため。出典の id は一次資料を確かめてから"}
```

## open-ended-loop-trap/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。事例の出典（sources 空）は write.md の判断事項のとおり

## model-quirks/write.md
[メインに判断してほしいこと]
- 本文の表に、モデルの系統名（Opus・Sonnet・Fable・Haiku）を 2026-10-29 の確認の時点つきで手書きした。版の数字は書いていない。系統名も「変わりやすい名称」と見るなら、names への追加か、数値の提案（facts-proposal.yml）の fact-table への置き換えが要る
- 表の「合わせ方の向き」の列は、調査資料 02 §4-13 を要約した私の言い換えで、公式の文は写していない
[提案]
- facts-proposal.yml を参照（used_in は #official-guidance。fact 化されたら、表を fact-table か fact の目印に替える）
- related に outdated-advice-ledger を足す提案はしない（台帳の行への link は本文にある）

## model-quirks/review.md
[メインに判断してほしいこと]
- write.md の、系統名の手書き（表の Opus・Sonnet・Fable・Haiku）の扱いは、メインの判断のまま

## cloud-sessions-and-teleport/write.md
[メインに判断してほしいこと]
1. `cloud-sessions` の features に「強制力」の属性がない（束の data は maturity のみ）。feature 型は要点に強制力を足す決まりだが、手で書くと決まりに反するので、成熟度だけにした。属性の追加を data で判断してほしい
2. 本文の、クラウドが読むもの・読まないものの表は、公式の文書（settings・cloud-environments。確認日 2026-11-05）の写しの要約で、手書きである。変わりやすいので、data の機能の項目に載せるか、現状のまま確認日付きの本文にするかを判断してほしい
3. 使えるプラン（Pro・Max・Ultra・Team・Enterprise の席）は変わりやすい値として本文に書かず、公式へのリンクにした。数値ファイルにプランの項目があれば、目印に替えられる
[提案]
```yaml
frontmatter: []
facts: []
```
- 用語集：「teleport」の項目を足すなら「クラウドのセッションを手元の端末に取り込む操作」の定義が要る（本文は導入で短く定義した）
- 入れ子の `claude -p` の不具合（CHANGELOG v2.1.317）は、版を手で書かない決まりで、版なしで書いた。入った版を data に置くなら、`used_in: [cloud-sessions-and-teleport#limits]`

## cloud-sessions-and-teleport/review.md
[メインに判断してほしいこと]
- write.md の 1（強制力の属性が data にない）に同意。属性の追加を data で判断してほしい

## checking-unattended-runs/write.md
[メインに判断してほしいこと]
- 目次の備考にある「注釈付きのセッション記録」（制作のワークフローの無人の実行を、報告・記録・始めと終わりの HEAD の比較で確かめた例。DR-08 の H3）は、制作の環境の記録を渡されていないため載せていない。載せるなら、記録の材料を別に渡してほしい
- `fact` の目印に使った 2 件（claude-code-p-startup-failure-exit-code-fix-version・auto-mode-no-verdict-display-fixed）は data/facts.yml で status が未確認（CHANGELOG の原文を開いていない）。確認済みになるまで、本文の版の記述も未確認のまま
[提案]
- front matter・用語集・data への提案はなし

## checking-unattended-runs/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しの差分を別の担当が確かめていないため）
- fact の 2 件が未確認のため、本文の版の記述は未確認の表示になる（write.md と同じ）

## freeze-eval-assets/write.md
[メインに判断してほしいこと]
- 雛形の `sandbox.filesystem` のパスを `./eval` の形で書いた。公式（sandboxing）は「`.` は project settings では根に解決」と書くが、`./eval` のような相対パスの細部は、参照先の settings-reference の節を未確認。動作確認の担当に確かめてほしい。外れたら `/` 始まりの絶対パスを使う案に変える
- 第三者の実践例（評価指標のファイルを凍結し、編集してよいファイルを 1 つに限った自律研究の例）を、名指しせず（根拠：弱）で 1 文だけ書いた。束の材料（11 p34#12）に基づく。名前や出典の URL は調べていない。要らなければ削ってよい
[提案]
- 数値の提案はなし（版・既定値・上限は本文に書かず、目印も使っていない）
- front matter の提案：なし

## freeze-eval-assets/review.md
[メインに判断してほしいこと]
- 指摘 1〜5 を直したため stage は draft のまま（別の担当の確認が要る）
- 雛形の `./eval` 形のパスの確認は write.md のとおり未了

## split-models-by-role/write.md
[メインに判断してほしいこと]
- 図を置かなかった。必要なら「分ける形」の表を図にする案を別の担当へ
[提案]
- facts-proposal.yml：opusplan の割り当て（plan mode は上位の系統、実行は日常の系統）。本文は系統の名前だけで書き、数値・版は書いていない。承認後に目印へ差し替える
- front matter（YAML）：
```yaml
frontmatter:
  - {id: split-models-by-role, key: related, before: [...], after: [..., choosing-a-model#verify], reason: "本文が choosing-a-model#verify を指している（前提に含まれるので不要なら無視してよい）"}
```
- 用語集：「上位の系統・日常の系統・軽い系統」を本文で使った。current-models の表と言い方を合わせてよいか確認してほしい
- 台帳：既存の avoid-opus-as-expensive の行を本文で指した。変更の提案なし

## split-models-by-role/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま。「上位の系統・日常の系統・軽い系統」の用語集への追加を検討してほしい。

## ask-without-sycophancy/write.md
[メインに判断してほしいこと]
- Truth Decay（arxiv-2503-11656、7 回目の追撃で 76.74% → 30.23%）を（根拠：弱）で #what-happens に載せた。research/24 B-44 の確認の範囲に入っていないので、載せるか判断してほしい
- Jin & Chen（arxiv-2603-00539、26.2% → 73.2%）は 10 第19章の数値のまま載せた。B-40 のような訂正はないが、一次資料では確かめていない
[提案]
- front matter・用語集・data への提案はなし

## ask-without-sycophancy/review.md
[メインに判断してほしいこと]
- write.md の Truth Decay と Jin & Chen の扱い（一次資料未確認）は、事実の検証の対象外なので判断を引き継ぐ

## how-much-understanding-to-keep/write.md
[メインに判断してほしいこと]
- 「ある実務家」の認知負債の紹介は、個人を名指ししない決めに合わせて名を出さず、出典は `sources` の speakerdeck-twada-agentic-software-engineering で示した。Simon Willison の記事は sources.yml にないので載せていない
- U-22・RITSEC・With AI 部門の大会の例は、束の注記で一部が未確認のため載せなかった（大会の話は practice-vs-contest-day へ link）
- 週1回など、ここで言う習慣の頻度は本文に書かなかった（根拠が中で数値の出典がないため）
[提案]
なし（数値の提案・front matter の提案・用語集への提案は不要。認知負債は用語集にある）

## how-much-understanding-to-keep/review.md
[メインに判断してほしいこと]
- 残る警告は、link の題名を含む文の誤検出に近い。許容するか、link の前後を短くするかの判断

## less-ai-sounding-japanese/write.md
[メインに判断してほしいこと]
- 第三者の推敲スキルは、名前を出さず「方針が 2 つに分かれる」とだけ書いた（目次の notes の、考え方の例として名前を出す案より控えめ）。名前と成熟度・確認日を付けて出すなら、材料の再確認が要る
- 「AI 臭さ」は読みやすさの品質と書き、AI の利用を隠さない旨を #guards の 1 項目に書いた。公開の方針に当たる文なら承認を（カード §13）。約束の文ではなく、手順の目的の説明のつもり
[提案]
なし（front matter・用語集・data への提案なし）。用語集に「lint」「推敲」があるかは未確認。

## less-ai-sounding-japanese/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま（別の担当の確認待ち）
- write.md の判断事項（#guards の「隠す目的にしない」が方針の文に当たるか）はそのまま残る

## what-subagents-dont-inherit/write.md
[メインに判断してほしいこと]
- 目次の visual（親から担当へ届くもの・届かないものの図）は、図を作らず `#what-arrives` の表で代えた。図が要るなら別途
- 強制力の属性が data の features にない。他の feature ページも文で書いているが、道具で出す形にするか
[提案]
- なし（数値の提案も、front matter の提案もなし）

## what-subagents-dont-inherit/review.md
[メインに判断してほしいこと]
- 指摘 1・3 を直したので stage は draft のまま（別の担当による差分の確認待ち）
- 図の案（visual）を表で代えた件は write.md のとおり

## diffs-humans-must-read/write.md
[メインに判断してほしいこと]
- 材料の p56#61（AI が生成した PR は約 1.7 倍の指摘、分析元は AI レビュー製品の販売元）は、出典を立てていないため本文に使わなかった。使うなら sources 追加と利害の併記が要る
- 「要の処理は厳しく、周辺は緩く」の出どころ（実践者の講演）は、個人を名指さず、（根拠：弱）の経験則として書いた。出典を立てて名指すかは判断を求める
- 赤信号の一覧は（根拠：中）とした（材料では「強〜中」）。強さの扱いを確認してほしい
[提案]
なし（用語集・prh・data への提案はない。数値の提案もない）

## diffs-humans-must-read/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま（brief §4.2-5）。
- p56#61（AI 生成 PR の指摘が約 1.7 倍）は出典未設定で未使用。write.md の判断事項のとおり。

## share-team-settings/write.md
[メインに判断してほしいこと]
- front matter の sections に 4 節を足し、順を本文に合わせた。既存 2 つの anchor は変えていない
- compare の表（強制力・読み込みの時期）は、data の settings・mcp の強制力が null のため「未確認」が出る行がある。見栄えが悪ければ列を変える
[提案]
- front matter・用語集・prh・data への提案：なし
- 数値の提案：なし（本文に変わりやすい値を書いていない）

## share-team-settings/review.md
[メインに判断してほしいこと]
- compare の表の「—」（settings・permissions の欠けた属性）の見え方

## separate-roles/write.md
[メインに判断してほしいこと]
- sources が空のまま。研究（過度依存のメタ分析、迎合、固執のエスカレーション）の印は、研究名を本文に書かず、持ち主のページ（over-reliance・agreement-is-not-evidence）を指して付けた。出典を足すなら sources の提案が要る
[提案]
- なし（front matter・用語集・data への提案はない）

## large-context-window/write.md
[メインに判断してほしいこと]
- 窓の大きさ・長い入力の単価・トークナイザーの差は数値の目印を使わず、current-models へ link して本文から外した（束に facts の id がなかったため）。目印にしたければ facts への追加が要る
- outdated-advice-ledger#save-context-for-200k と #subagents-to-save-context の link を置いた（束の指せる節の一覧にない。check_page は通った）
- 図は置かなかった（比喩は文章で広い机と送り直す受験者を使った）

## large-context-window/review.md
[メインに判断してほしいこと]
- 窓の大きさや長い入力の単価の facts の id を足すなら、費用の節に目印を置ける

## permission-to-stop/write.md
[メインに判断してほしいこと]
- 判断例の題「止まる条件を書いた後に、tests/ を守るか」を末尾に置いた（#with-structure）。不要なら外してよい
- 「やりすぎ」の1文は (推論・実践例なし) の印を付けた。根拠の資料がない
[提案]
- なし（数値の提案もなし。54%→9% などは研究の固定の記録として、研究名・年・対象を添えて本文に書いた）

## keep-failure-lessons/write.md
[メインに判断してほしいこと]
- 「見えていない」「見せる」を four-principles・six-causes の whole-page link で指した（節の anchor は束にない）。check は通った
- 目次 notes の指示（「大量に読ませると消極的」は単独の経験談として本文で書く）に従い、#too-much に（根拠：弱・類推）で置いた。仕組みの説明は（推論・実践例なし）と明示
[提案]
- なし（用語集・data への提案なし。数値の fact なし）

## keep-failure-lessons/review.md
[メインに判断してほしいこと]
- なし。直したので stage は draft のまま

## own-generated-code/write.md
[メインに判断してほしいこと]
- #gate の Rust コンパイラ開発ガイドの規約の文は、束の材料（11 の p56#43）に基づく。Web は取得していない。本文は「ガイドの版で変わりうる」と付けた
- #when-it-fails の Anthropic の研究の数値（50%・67%・52 人・各 4 人ほど）は束の research/24 A-13 の写し。本文に手で書いた（研究の固定の記録として、common §9 の扱い）
[提案]
- なし（facts・用語集・prh・front matter の他のキーの提案はない）

## think-before-asking/write.md
[メインに判断してほしいこと]
- Psyho の投稿（threadreaderapp.com、sources.yml で noai: true）は資料にしなかった。そのため「直感を育てる単純な解で実験する」の根拠は、terry_u16 の講義資料と AHC001 の解説で代えた
- Shun_PI の資料・a1k0n の事例・p56 の項目は、競技の技術そのものなので kyopro-atlas に任せ、本文に入れていない（sources.yml にも id はあるので、足したければ言ってほしい）
- 判断例で「15〜30 分」を「決めた時間」と言い換えた箇所と、本文の「15〜30 分は目安（根拠：弱）」の扱いでよいか
- decide-when-to-quit（related にない）と competition-rules を、ページ単位で link した。related に足すかは任せる
[提案]
```yaml
frontmatter:
  - {id: think-before-asking, key: related, before: [], after: [decide-when-to-quit, competition-rules], reason: "本文から指している。related に足すなら追記"}
```
（上は任意。足さなくても check_page は通っている）

## think-before-asking/review.md
[メインに判断してほしいこと]
write.md の提案（related に decide-when-to-quit・competition-rules を足すか）は未判断のまま。

## resume-and-branch/write.md
[メインに判断してほしいこと]
- 要点に「強制力」を置いていない。sessions の機能に enforcement の値がない（操作であり、お願い・鍵のどれにも当てはめにくい）。属性を足すか、このページでは省くかを決めてほしい
- 「ブランチ名・セッション名を揃える」（11 の p34#195）には（根拠：弱）を付けた。強さの判定が違えば直してほしい
- #pitfalls の「分岐が分けるのは会話であって、ファイルではない」は、公式が会話の複製と書いていることからの読み（この辞典の読み、と本文に明記）。公式にファイルの扱いの明記はなく、確かめる担当がいれば試してほしい
[提案]
```yaml
frontmatter:
  - {id: resume-and-branch, key: sections, before: [resume, branch, naming], after: [use-cases, resume, branch, naming, pitfalls, compare, outdated], reason: "型の構成の目安（使いどころ・落とし穴・比べる相手・古くなった助言）に合わせて節を足した。既存の anchor は変えていない"}
```
- 数値の提案はなし（保持期間は既存の local-transcript-cleanup-days を目印で指した）
- 用語集：「ピッカー（セッションの一覧）」は本文で「セッションの一覧（ピッカー）」と 1 回だけ書いた。追加は要らないと考える

## resume-and-branch/review.md
[メインに判断してほしいこと]
- sessions に enforcement の属性を足すか、feature 型でも省くかを決めてほしい（要点の「強制力」）
- stage は draft のまま（直したため）

## lockbox-and-holdout/write.md
[メインに判断してほしいこと]
- 三層の定義：材料は「入力を開発用・検証用・ロックボックスの三層」「hold-out は人が持ち点数だけ返す」「ロックボックスは節目にだけ見る」まで。「検証用＝点数だけ返す、ロックボックス＝点数も返さず選ぶために使わない」の線引きは、材料と選択圧の考え方から書いた設計である。本文では「実践者の運用に機械学習の考え方を当てはめた（根拠：中・類推）」と書いた。要否の確認を願う
- 「点数だけでも問い合わせを重ねると合わせ込める（類推）」は材料にない。選択圧のページの考え方からの類推として書いた
- 「月単位の定期確認にとどめる（根拠：弱）」は、材料の「月 1 回程度」を数字なしで書いた。数値の提案にするかは任せる
[提案]
```yaml
frontmatter: []
```
- 用語集：「ロックボックス」「hold-out」の追加を提案。hold-out＝作る途中の調整では使わず取り置く検証用データ、ロックボックス＝その中で人だけが持ち節目にだけ開ける最後の層
- freeze-eval-assets のページで、設定の雛形（`data/holdout/` の Read deny と sandbox `denyRead`）を持つ。このページは置き場所と考え方だけを書き、そこを指した

## lockbox-and-holdout/review.md
[メインに判断してほしいこと]
- write.md の 3 点（三層の線引きは設計、類推の記述、月単位の経験則の数値化）は、そのまま引き継ぐ

## documents-in-japanese/write.md
[メインに判断してほしいこと]
- sources が空のまま。束に出典の一覧がなく、ページの事実は束の research 材料（PDF の読み込みの範囲など）を数値なしで指すだけにした。縦書き・スキャンの PDF の読まれ方は推論で書かず、手元で確かめる手順にした。出典を足すなら、support.claude.com の Upload files to Claude を `sources` に足すか判断してほしい
- 書き出しの「敬語の段階」の説明（尊敬語・謙譲語、社外に自社の人を高めない）は一般の日本語の作法で、一次資料の出典はない
[提案]
```yaml
frontmatter: []
```

用語集・data・prh への提案はない。

## documents-in-japanese/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しを入れたため）。sources が空なので、出典を足すかは write.md の判断を参照

## change-timeline-2026/write.md
[メインに判断してほしいこと]
- 流れの説明（`#trends`）に日付・版・数・モデル名を書かず、台帳の行への link で時期を示した（変わりやすい値を手で書かない規則のため）。足りなければ指示がほしい
- 目次 visual の「四つの列の年表」は図にしていない。`timeline` の生成物の形に依存するため
- 「2027 年の変更は次の年のページ」という約束に当たる文は書いていない（公開の約束の扱い）
[提案]
- front matter：related に `default-safety-settings` を足す案（本文で `default-safety-settings#by-stage` を指したため）

```yaml
frontmatter:
  - {id: change-timeline-2026, key: related, before: [outdated-advice-ledger, term-index, checking-for-updates, dating-information], after: [outdated-advice-ledger, term-index, checking-for-updates, dating-information, default-safety-settings], reason: "自律の既定化の流れで守りの正本を指したため"}
```
- 用語集・prh：「skills」は prh で「スキル」に直される（本文は「スキル」に直した）。「auto mode」「effort」の扱いは用語集のとおり

## change-timeline-2026/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 警告 1 件（#trends 末尾の段落）は直していない。直すなら「年表で「入った」と読める変更は…」の文を分ける

## init-and-first-claude-md/write.md
[メインに判断してほしいこと]
- 「実践者の幅」に個人・記事の名前を出さず、「ある実践者の記事」と書いた。出典（redreamality・Tembo など）を sources に足すかは未判断
- 要点に「強制力」の項を足した（feature 型の要件）。形が合わなければ直してほしい

## init-and-first-claude-md/review.md
[メインに判断してほしいこと]
- 指摘 1・2 を直したため stage は draft のまま
- 実践者の出典（redreamality・Tembo 等）を sources に足すか（write.md と同じ）

## using-auto-memory/write.md
[メインに判断してほしいこと]
- 面のタブは surfaces が claude-code だけなので、タブは「Claude Code」1 つだけにした。1 つだけのタブが不自然なら、通常の番号付き手順にしてよい
- 雛形（#review）は節 #review の中に置いた。#usage に移すかは任せる
[提案]
- data/facts.yml：ローカルのセッションでの既定の状態を数値ファイルに置く案（facts-proposal.yml）。本文は既定を書かず、「環境ごとに /memory のトグルで確かめる」にした。置かれたら #usage に目印を足す
- 用語集：特になし

## using-auto-memory/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。雛形を #usage に移すかは任せる（write.md の指摘どおり）

## read-specs-yourself/write.md
[メインに判断してほしいこと]
- 研究（要約の一般化・LLM のコードの誤りの類型など）と競技の事例は、出典を sources.d に作らず本文に載せなかった。載せるなら出典の登録（arXiv 2種・競技者の記事）と check_noai の確認が要る。研究の数値は前提の summary-overgeneralization が持つため、重複を避けて link に任せた
- 競技の部分は人名・個人の事例を出さず、kyopro-atlas は平文の名前で触れただけ（リンクは付けていない）。リンク形式の指定があれば直してほしい
[提案]
- なし（用語集・data・front matter への提案はない）

## read-specs-yourself/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。別の担当が差分を確かめたら reviewed にする
- 研究・競技事例の出典が本文にない（write.md のとおり）。追加するか判断してほしい

## harness-over-model/write.md
[メインに判断してほしいこと]
- 手元の 2 件の一次資料（DrivenData、Anthropic の記事）を Web で確かめた。調査資料 11・10 の要約は「差の多くはハーネスに帰せられた」だが、DrivenData の記事は Claude Code と Codex の差をモデルとハーネスに切り分けておらず、ハーネスの根拠は別のツールの成績が大きく下がったことだった。本文は記事に合わせて「切り分けていない」と書いた。目次の備考・調査資料の要約を直すか、判断してほしい
- 本文に Claude Code（Opus 4.5）と Codex（GPT 5.2 Codex）の名前を、研究の時点の固定の記録として書いた（card §7 の末尾の扱い）。第三者のツール名の扱いとして問題ないか確認してほしい
- 目印を使わない固定の記録（モデル名・費用や時間は数値を書かず）にした。フルハーネスの費用と時間は本文に書いていない
[提案]
```yaml
frontmatter: []
```

- 用語集 `harness` の行は「モデルのまわりでツールを動かし、モデルが見る文脈を管理する層」。本文の定義はこれに合わせた。変更の提案はない
- prh：「system prompt」は システムプロンプト、「harness engineering」は ハーネスエンジニアリングに直した（prh の指摘どおり）

## harness-over-model/review.md
[メインに判断してほしいこと]
- write.md の「調査資料 11 の要約と DrivenData の記事が食い違う」件（目次の備考・調査資料の直し）
- stage は draft のまま（直したため）

## long-chat-limits/write.md
[メインに判断してほしいこと]
- 窓の大きさの数値は本文に書かず、facts-proposal.yml で提案（採用なら auto-management に fact の目印を置く）
- 公式の 2 記事で「有料のプランに限る」の書き方が食い違う（data の note と同じ）。pitfalls で「画面と公式で確かめる」と書いて留めた
[提案]
- facts-proposal.yml（上記）
- 用語集：「拡張思考」が prh の正。extended thinking を本文に出さないよう直した

## long-chat-limits/review.md
[メインに判断してほしいこと]
- feature の要点は強制力を持つ決まりだが、data の機能に enforcement がない。値を足すなら data 側の提案が要る
- 窓の大きさの数値は facts-proposal.yml の採否待ち

## plugins-and-marketplaces/write.md
[メインに判断してほしいこと]
- 強制力の目印：data の plugins には enforcement がない。「なし」を足すなら提案のとおり。足したら要点に `feature plugins/enforcement` を入れたい
- 逆に、クラウドのセッションでプラグインが動くかは、束（research/01・27）が「ローカルの設定のプラグインは読まない」「プラグインは読み込まれない」と書くのに対し、公式の org ページ（2026-11-05 に取得）は、クラウドでのリポジトリの設定の扱いを面ごとの別の節に任せている。本文は「ローカルで入れたものは届かない。リポジトリの設定の場合は未確認」と書いた。data に確認済みの値を足せるなら足したい
[提案]
```yaml
frontmatter: []
proposals:
  - feature_patch: {id: plugins, add: {enforcement: なし}}
    reason: プラグインは束ねて配るだけで、止める力を持たない。要点の「止めるもの」と合わせる
    sources: [cc-docs-plugins-overview]
glossary:
  - {term: マーケットプレイス, note: プラグインの一覧（marketplace.json）を持つカタログ。ストアではない。用語集になければ追加}
```

## plugins-and-marketplaces/review.md
[メインに判断してほしいこと]
- 強制力の目印（data の plugins に enforcement: なしを足すか）と、クラウドでのリポジトリ設定のプラグインの扱い（write.md のとおり）
- 直したので stage は draft のまま

## risk-tiered-approval/write.md
[メインに判断してほしいこと]
- 人の承認の数（0・1・2 人）と段の中身を、数値の目印にせず、記事（2026-10-15）の固定の記録として本文に書いた。「回数」に当たるなら facts に置く案が要る。当たらないなら今のまま。
- 本文の「承認のコメントに読んだ箇所を 1 行書く」「迷う変更は上の段に倒す」は独自の提案で、（推論・実践例なし）を付けた。
- 「承認の数を実際に強制できるかは、ホスティングの機能で確かめる（未確認）」とした。GitHub 等の設定の手順は束になく、書いていない。
[提案]
```yaml
frontmatter: []
```

用語集・prh・data への提案はない。

## risk-tiered-approval/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。
- write.md が挙げた、人数（0・1・2 人）を固定の記録として本文に書いた件は、このまま問題ないと見る。

## dating-information/write.md
[メインに判断してほしいこと]
- 「公式の Best practices が書き直された」の記述に日付・版を書いていない（変わりやすい値を避けるため）。日付入りで書くなら facts への登録が要る
- `claude --version` は束にない。記憶による記述（広く使われる確認手段）なので、別の担当が確かめてほしい
[提案]
- 無し（用語集は既存の語のみ。prh に従い フック・スキル・auto モード・サンドボックス と書いた）

## dating-information/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- `claude --version` と、アプリ・API の変更の記録の在り処は束になく記憶による。事実の確認が要る

## why-prompt-caching/write.md
[メインに判断してほしいこと]
- 本文に数値を書いていない。既定の寿命・読み取りの倍率・最小の長さは facts にないため、数字なしで書いた。下の提案を入れるなら、#what-happens と #why の「数字は公式で確かめる」の所に目印を置ける
- #effects のタブ「Claude Code」から、cost の分野のページを名指しせず文章で指した（id の指定がなかったため）
[提案]
```yaml
proposals:
  - fact: {id: prompt-cache-default-ttl, title: プロンプトキャッシングの既定の寿命, value: "5 分（使うたびに延びる。1 時間の寿命も選べる）", sources: [api-docs-prompt-caching], checked: 2026-11-05, status: 確認済み}
    used_in: [why-prompt-caching#why]
  - fact: {id: prompt-cache-read-multiplier, title: キャッシュの読み取りの料金の倍率（基本の入力単価に対して）, value: "多くのモデルで 0.1 倍。モデルにより 0.05 倍・0.025 倍の例外がある。書き込みは 5 分の寿命で 1.25 倍、1 時間で 2 倍", sources: [api-docs-prompt-caching], checked: 2026-11-05, status: 確認済み}
    used_in: [why-prompt-caching#what-happens]
```
- 公式の文書（2026-11-05 に取得。後半 65,992 字は未読）で、順序（tools→system→messages）、無効にする変更の表、effort が既定以外のとき messages が外れること、既定の寿命、倍率を確かめた

## why-prompt-caching/review.md
[メインに判断してほしいこと]
- write.md の数値の提案（寿命・読み取りの倍率）を facts に入れるか。入れれば #what-happens と #why に目印を置ける

## ask-for-outcomes/write.md
[メインに判断してほしいこと]
- sections に 4 つ足した（before-after・why・limits・templates）。技法の構成に合わせるため
- 題名「細かく指図するか、成果で頼むか」の「か」が 2 つ続く問いの形は、catalog の決定どおりで変えていない
[提案]
- 出典の一覧が束になく、data/sources.yml の既存 id（cc-docs-best-practices・api-docs-prompting-best-practices・prussianblue-ahc054-claude-code・jitendrazaa-tips-code-tips-creator-boris）を sources に入れた。新しい出典の追加はない
- 数値の提案なし。用語集・prh・front matter の提案なし

## ask-for-outcomes/review.md
[メインに判断してほしいこと]
- 指摘 0 件のため stage を reviewed にした

## refine-in-conversation/write.md
[メインに判断してほしいこと]
- 「Claude Code の作者のチームの習慣として紹介」（#why、根拠：弱）は二次の記事の紹介。個人名は出していない。弱すぎるなら削ってよい
- 節 edit-the-request は目次の備考どおり短く、rewind-dont-correct#why に譲った
[提案]
- なし（新しい用語・数値・出典はない）

## refine-in-conversation/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま
- #why の「Claude Code の作者のチームの習慣」（根拠：弱）は write.md のとおり、弱ければ削除でよい

## progress-files/write.md
[メインに判断してほしいこと]
- handoff-documents が `progress-files#decided-vs-open` を「聞くべきことの分け方」として指しているため、その節に聞くべきことの欄の書き方（問い・聞く相手・暫定の仮定・進めてよい範囲）を置いた
- 題名から特定の実践者のファイル名を外す方針（notes）に従い、4 ファイルの名前は aliases と雛形の例だけに置いた。本文では実践者を名指ししていない。ただし本文の表と雛形が `PLAN.md`・`TODO.md`・`KNOWLEDGE.md` を使うので、「特定の個人の構成を標準として示す」に当たらないか確認してほしい（`SPEC.md` を外し `DECISIONS.md` を足した形にした）
[提案]
- 数値・用語集・prh.yml・data への提案はなし
- 出典 qiita-minorun365-114f53 は sources に入れたが、本文では名指しせず、参考の節に出る。否定的な文脈ではない

## progress-files/review.md
[メインに判断してほしいこと]
- write.md の判断事項（4 ファイル構成が「特定の個人の構成を標準」に当たらないか）は未解決のまま。stage は draft のまま（直しを別の担当が確かめていないため）

