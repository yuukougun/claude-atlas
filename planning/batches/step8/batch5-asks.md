## path-scoped-rules/write.md
[メインに判断してほしいこと]
- 古くなった助言：この機能の台帳の行がないので、台帳は指さず、`#outdated` に束の注記にある「CLAUDE.md は再注入される」の言い切りと、`@import` でコンテキストが減るという説明の 2 つを短く書いた。後者は束の調査資料（Serverworks の記事）が根拠で、公式の文書では確かめていない。台帳に行を足すか、`#outdated` の 2 点目を外すかを決めてほしい
- 面のタブは claude-code の 1 つだけ（surfaces がその 1 面のため）。1 面だけのタブを残すか、外すかを決めてほしい
[提案]
- 数値：facts-proposal.yml に、必要なときに読み込まれるファイルの文字数の上限を 1 件（used_in は path-scoped-rules#limits）。本文はこの数字なしで読めるので、目印は置いていない。承認後に目印を足す
- 用語集：新しい語の提案なし

## path-scoped-rules/review.md
[メインに判断してほしいこと]
- 指摘 2 件を直したので stage は draft のまま
- write.md の 2 点（#outdated の 2 点目と面のタブ 1 つ）は、そのまま判断を仰ぐ。直した導入の文に残る警告がないか、最後の check_all で確認してほしい

## how-skills-load/write.md
[メインに判断してほしいこと]
- 説明文が圧縮の後に作り直される挙動は、入った版を本文に書かず「公式の変更履歴で確かめる」とした。facts に版の項目を足せば目印にできる（下の提案）。
[提案]
- facts-proposal.yml を参照（`skill-description-rebuild-min-version`）。本文の足し先は `how-skills-load#after-compaction` の「説明文」の項目。
- front matter の変更の提案：なし。

## how-skills-load/review.md
[メインに判断してほしいこと]
- 指摘 3 件を直したので stage は draft のまま（別の担当が直しの差分を確かめるまで reviewed にしない）。
- 指摘 4 は事実側の確認に任せる。

## skill-descriptions/write.md
[メインに判断してほしいこと]
- 台帳の行はなく、古くなった助言は薄い（`#old-advice` は「記事によって上限の字数が違う」の読み替えだけ）。節ごと削るなら、sections からも外す
- 「実践者の間では成否は説明文でほぼ決まるとよく言われる」を（根拠：弱）で 1 文だけ残した。数（9割）は書いていない。要らなければ `#purpose` の最後の 1 文を削る
[提案]
```yaml
frontmatter:
  - {id: skill-descriptions, key: related, before: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents], after: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents, skills-in-the-app, hook-vs-skill, instructions-ignored], reason: "本文で指している。本文が指すページは related に入れたい"}
glossary:
  - {term: description（スキルの説明文）, definition: "スキルの SKILL.md のフロントマターにあり、Claude がそのスキルを読み込むかを決める手がかりになる文。名前とともに毎回の会話に載る", reason: "ほかのページ（writing-skills・writing-subagents）でも使う語"}
```

数値の提案はない（既存の `skill-listing-entry-max-chars`・`skill-description-max-chars`・`skill-listing-budget-fraction` を目印で指した）。

## skill-descriptions/review.md
[メインに判断してほしいこと]
- write.md の提案（related に skills-in-the-app・hook-vs-skill・instructions-ignored を足す、glossary に description）は未判断のまま残る
- #old-advice は薄い。write.md のとおり、節ごと削るか判断が要る

## hook-vs-skill/write.md
[メインに判断してほしいこと]
- 「ほかの OS と IDE 拡張は未確認」の一文を #table の補足に入れた。位置はここでよいか
[提案]
- なし（数値の提案も、front matter の提案もない）

## hook-vs-skill/review.md
[メインに判断してほしいこと]
- 「ほかの OS と IDE 拡張は未確認」の位置（#table の末尾）は許容範囲と見た
- 直したので stage は draft のまま

## writing-subagents/write.md
[メインに判断してほしいこと]
- 台帳への link `outdated-advice-ledger#<行の id>` が、4 行とも check_page で通った。ページの id と anchor はこの形で合っていた（確認のみ）
[提案]
- 数値の提案：なし。同時実行数・ネストの深さ・skills の上限・入った版は本文に書いていない（環境変数の名前だけ書いた）
- 用語集・prh：「フロントマター」の表記が prh で要求された（front matter は不可）。用語集にあるので、変更の提案はない

```yaml
frontmatter: []
```

## writing-subagents/review.md
[メインに判断してほしいこと]
- 事実は確かめていない。write.md が挙げた束にない 2 点（tools を省くと道具を引き継ぐ・Bash で書き込める）は、事実の検証役へ

## skill-vs-subagent/write.md
[メインに判断してほしいこと]
- 表の列から「強制力」「圧縮で残るか」を外した。subagents の強制力が data で空（注に「書かない」）、圧縮で残るかも null で、表が「未確認」だらけになるため。圧縮は表の下の箇条で書いた。subagents に `survives_compaction`（記録は圧縮の影響を受けない）を入れるなら、列を足せる
[提案]
```yaml
facts-note: 数値の提案はない。
frontmatter: []
```
- 用語集への提案：なし

## skill-vs-subagent/review.md
[メインに判断してほしいこと]
- write.md の提案（表に強制力と圧縮の列を足すために、subagents の `survives_compaction` を data に入れるか）は、そのまま残す
- stage は draft のまま（直しを入れたため）

## mcp-or-cli/write.md
[メインに判断してほしいこと]
- 比較の表は、tracks が `mcp` 1 つだけなので 1 行になる。CLI は data の機能にないため行にできない。表を比べる形にするには、tracks に `skills` を足す案がある（スキル側が常駐する説明文のコストを持つ）。CLI 自体の行は data に機能として足すか、足さないかの判断が要る。
- `stances` の「この辞典の推奨」に（根拠：中）を付けた。公式の案内と実務家の一致の重なりを根拠にした判断で、割れる論点なので、強さの印が妥当かを見てほしい。
- Simon Willison を肯定的な文脈で名指しした（出典付き）。Composio はベンダー記事と明記した。
[提案]
```yaml
facts:
  proposals:
    - fact: {id: mcp-output-warning-tokens, title: MCP のツール出力で警告が出る大きさ, value: "10,000 トークン", sources: [cc-docs-mcp], checked: 2026-10-29, status: 要確認（調査資料 01 G-1 の写し。一次は未確認）}
      used_in: [mcp-or-cli#table, mcp-or-cli#verify]
    - fact: {id: mcp-output-default-limit-tokens, title: MCP のツール出力の既定の上限（MAX_MCP_OUTPUT_TOKENS）, value: "25,000 トークン", sources: [cc-docs-mcp], checked: 2026-10-29, status: 要確認（調査資料 01 G-1 の写し。一次は未確認）}
      used_in: [mcp-or-cli#table, mcp-or-cli#verify]
frontmatter:
  - {id: mcp-or-cli, key: tracks, before: [mcp], after: [mcp, skills], reason: "比較の表を MCP とスキルの 2 行にして、常駐の説明文の差を示すため（判断はメイン）"}
```

本文は数字なしで読める形にしてある。目印を置く場所は、`table`（出力の警告と上限の文）と `verify`（出力が大きいときの項目）。

## mcp-or-cli/review.md
[メインに判断してほしいこと]
- 指摘 4（tracks に skills を足すか。CLI の行を data に足すか）。
- 直したので stage は draft のまま。再検査で警告 0 を確かめてほしい。

## pruning-extensions/write.md
[メインに判断してほしいこと]
- 目次の備考「40 個を超えたら見直す」は、出どころを確かめる指示のため本文に書かなかった。数値ファイルに置く案が出たら、used_in は `pruning-extensions#criteria`
- 公開の約束や方針の文は書いていない
[提案]
- 数値：`facts-proposal.yml` の 2 件。本文には数を書いていないので、置く場所は measure の「/plugin の Installed タブ」の項目。置くなら「一定の期間と回数のあいだ」を目印に替える。2 件目は本文に使っていない（任意）
- 用語集・prh・front matter への提案はなし

## pruning-extensions/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま（別の担当が差分を確かめるまで）

## checking-citations/write.md
[メインに判断してほしいこと]
- 事例の扱い：材料 6.2 の訴訟の事例の出典は techcrunch.com で、check_noai.py が「noai あり」と判定した（deny にある）。そのため事例は本文に書かず、誤りの形を一般形で書いた。目次の「Anthropic の訴訟の事例」の位置づけは、noai でない別の一次の出典（裁判所の記録など）が見つかれば足せる。足すか、事例なしのままにするかを判断してほしい
- 「よくある誤りの形」の 4 形のうち、「引用が原文にない」「出典が主張を支えていない」は材料 6.2 にはなく、目次の確認表の列（引用の文言・主張を支えているか）から立てた。出典を付けていない
[提案]
なし（用語集・data・front matter の提案なし）

## checking-citations/review.md
[メインに判断してほしいこと]
- write.md のとおり、訴訟の事例が techcrunch.com が noai のため入っていない。別の一次資料の有無の判断
- stage は draft のまま（直したため）

## request-lock-table/write.md
[メインに判断してほしいこと]
- `#table` の手書きの表の「文体・表記」「返答の言語」の行は、research/27 §3.2 と textlint-hook・keep-replies-in-japanese の要約に基づく。Stop フックで言語を確かめる行を鍵として載せたが、言語の判定のしかたは公式の例がない（keep-replies-in-japanese 側の扱いと揃うか確認してほしい）
- `#combine` の「止めるのは壊れにくい手段に任せる」は research/28 の推論（試していない）で、本文に（推論・実践例なし）と付けた。残すか削るか
[提案]
- front matter・用語集・prh・data への提案はない

## request-lock-table/review.md
[メインに判断してほしいこと]
- write.md の 2 点（Stop フックで言語を確かめる行の扱い、#combine の推論の段落を残すか）は未判断のまま。stage は直したので draft のまま

## writing-safe-hooks/write.md
[メインに判断してほしいこと]
- 節の追加：`when`・`templates`・`limits` を sections に足した。カードの型の構成に合わせたもの
- `${CLAUDE_PROJECT_DIR}` を `args` の要素に書く形は、research/28 #23 の「置き換えを使うフックには args を付ける」から組んだ。args の中での置き換えの実際の動きは、動作確認の担当に確かめてほしい
- 本文は permission-rules を、束の「つながるページ」にないが、既存の公開ページなので page 単位で link した。related に足すかは判断を仰ぐ
[提案]
```yaml
frontmatter:
  - {id: writing-safe-hooks, key: related, before: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing], after: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing, permission-rules], reason: "比べる相手の表で permission-rules を指したため（任意）"}
```
- 数値の提案はなし（onFailure の版は既存の fact `hook-on-failure-block-min-version` を使った。タイムアウトの既定値は本文に書いていない）
- 用語集・prh への提案：managed settings は prh で「管理設定」に直された。本文は「管理設定」にした

## writing-safe-hooks/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。write.md の提案（related に permission-rules を足すか）は未判断のまま

## hook-recipes/write.md
[メインに判断してほしいこと]
- 雛形 filter-test-output は `updatedInput` と `permissionDecision: allow` を一緒に返す。公式の文書の抜粋に allow と並べた例があるが、allow が必須かは全文で確かめていない。確かめる担当に見てほしい
- 通知のコマンドは `notify-send`（Linux のデスクトップ）。WSL などは本文で「未確認」と書いた
- 目次の備考にある「制作の .claude/settings.json の H3 の動作確認を雛形の動作確認に使う」は、確認の結果を見ていないため使っていない。制作の H2・H3 は注釈付きの文章で示した
- 「PATH の差し替えで止めた実践者の例」は、第三者を名指ししないため名前を出さず、（根拠：弱）で書いた
[提案]
```yaml
sources:
  - note: "担当にだけ禁じる節の「disallowedTools は指定子を付けても Bash 全体が外れる」は research/28 #14 の S3（サブエージェントの文書）による。このページの sources に載せる id が無い（cc-docs-subagents など）。足すなら data/sources.d への追加が要る"
facts:
  - note: "agent_id が入力に付く最低の版（research/28 #1：v2.1.69、2026-03-04）を数値の id にすると、deny-subagent-commit の min_version_fact に使える。本文には版を書いていない"
```
front matter の他キーの直しの提案はなし。

## hook-recipes/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。filter-test-output の allow と updatedInput の関係（write.md の疑問）は事実の検証で、ここでは見ていない

## where-bypass-is-ok/write.md
[メインに判断してほしいこと]
- 目次の templates の案は「使い捨てのコンテナで無人の実行を動かす手順の例」。カード §10 は、使い捨てのコンテナは試せず、回避された仕組みを守りとして勧める雛形は載せない、とする。そこで Dockerfile や起動コマンドではなく、条件だけの確認の一覧を雛形にした。コンテナの具体の手順を載せるかは判断を仰ぐ
- 本文の「この辞典の推奨」（秘密を入れない・届く範囲を限る・通信の宛先を絞る・差分で取り出す）は、束の材料にない推論で、（推論・実践例なし）と明記した。必須ページの中心にしない形（公式の条件を先に置いた）だが、確認を頼む
- #not-a-substitute と誤解の節で台帳 outdated-advice-ledger#yolo-skip-permissions を指した。束の「指せる節」の一覧にないが、カード §11 の指定どおり。anchor が存在しない場合は check の結果で止まるはず（検査は通った）
[提案]
- 用語集・data・prh への提案はなし
- 数値の提案なし（本文に変わりやすい値を書いていない。permissions.blockWritesOutsideWorkingDirectories の入った版、auto の既定、-p の既定は本文に書かず、持ち主のページと台帳へ回した）

## where-bypass-is-ok/review.md
[メインに判断してほしいこと]
- write.md の 3 点（コンテナの具体手順の雛形を載せるか、推奨条件の確認、台帳 anchor）を引き継ぐ
- 指摘は直したので stage は draft のまま（直しの差分を別の担当が未確認）

## entrusted-data/write.md
[メインに判断してほしいこと]
- `#misconceptions` の「オプトアウトしても、すでに学習に使われたデータは残る」は research/05 4-7 と research/26 §3.12 の写しに基づく。本文に日数・年数は書いていない
- コンペのデータの記述は、束の材料（research/11、類推・版依存）だけが根拠。印は（根拠：中・類推）にした。大会の規約は読んでいない
[提案]
- front matter・用語集・data への提案はなし

## entrusted-data/review.md
[メインに判断してほしいこと]
- 指摘 1 は事実の言い方に関わる。本文は直し済みだが、別の担当による確認が要る。直したので stage は draft のまま
- 指摘 6 の Claude Code の認証方式と契約の側の対応を、公式の文書で照合してほしい

## before-opening-unknown-repos/write.md
[メインに判断してほしいこと]
- 先に整える守りの 2 は、「プロジェクトの deny と ask は信頼と関係なく効く」（research/28 #19）から、自分の側の deny を先に置く、と読んだ。自分の（ユーザーの）deny が信頼の前から効くかは束に明記がないので、本文では書き分けていない
- `#isolate` の「手元の認証情報を持ち込まない」は、where-bypass-is-ok#requirements の中身を見ずに一般論として書いた。そのページの条件と食い違うなら直す
- `#files-to-check` の表の `.vscode/` は、Check Point の推奨に名前があるだけで、動作は未確認と本文に書いた
[提案]
- front matter の直しの提案はなし
- 数値の提案（facts-proposal.yml）はなし。年月は研究の記録として書いた（修正の月は 2025-08・09・12。Check Point の記事の日付）

## before-opening-unknown-repos/review.md
[メインに判断してほしいこと]
- 指摘 4：手順 4 の確かめに、起動後に動いているフックと MCP を見る画面やコマンドの名前を足すか。公式の文書で確かめてから足す必要がある

## checking-ai-rules/write.md
[メインに判断してほしいこと]
- 注意書き（法的な助言ではない）：decisions 2026-11-03 の方針 7 はサイト全体の注意書きだが、card §13 によりページには足していない。「このページは法令の解釈を書かない」という範囲の文だけ rights-and-licenses に置いた。サイトの注意書きの場所は作者の承認を得てメインが決める
- `#when-unclear` の判断例は、高専プロコンの例（公式ページに生成 AI の記述がなく、行動規範の熟読を求める）の一般化として、大会名を出さずに書いた。大会名と版を出すかはメインが判断する
[提案]
```yaml
frontmatter:
  - {id: checking-ai-rules, key: prevents, before: [], after: [境界がない], reason: "本文は、規則の境界を決める側と確かめる側を分ける話で、where-your-data-goes と同じ原因（境界がない）に結べる。付けるなら本文の when-unclear に原因名の名指しを足す"}
```

- 用語集・prh・data への提案はなし。数値の提案（facts-proposal.yml）もなし（本文に変わりやすい値を書いていない）

## checking-ai-rules/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しがあったため）
- write.md の prevents 提案（境界がない）の採否

## parallel-with-worktrees/write.md
[メインに判断してほしいこと]
- 要点の「強制力」：data の worktrees に enforcement の属性がなく、`feature` の目印を使えなかった。手書きで「鍵ではない」と書いた。facts に enforcement を足すか（下の提案）、手書きのままでよいか
- 比例則の守りは使いどころに link で置いた（humans-set-the-parallel-limit#guards-before-widening・protecting-secrets#keep-out・sandboxing#when）。secrets の `.worktreeinclude` 雛形が safety の確認を通ってから載せる、という目次の備考に沿い、雛形は safety: true にして載せた。確認の担当に回すか
[提案]
```yaml
frontmatter: []
facts_to_check:
  - 「分岐元の既定（worktree.baseRef の fresh/head のどちらが既定か）」は本文に書かず省いた。fact 化するなら下記
proposals:
  - fact: {id: worktree-base-ref-default, title: worktree.baseRef の既定値, value: "fresh（リモートの既定ブランチから切る）", sources: [cc-docs-worktrees], checked: 2026-10-29, status: 要確認}
    used_in: [parallel-with-worktrees#minimal]
  - fact: {id: worktree-sandbox-resume-fix-version, title: "claude -p --resume / --continue で入った worktree に sandbox の保護がかかるようになった版", value: "2.1.314（調査 research/22 #7 による）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [parallel-with-worktrees#pitfalls]
  - fact: {id: worktree-block-writes-setting-version, title: permissions.blockWritesOutsideWorkingDirectories が入った版, value: "2.1.314（research/22 #4 による）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [parallel-with-worktrees#pitfalls]
  - features_attribute: {id: worktrees, enforcement: なし, reason: "作業場所を分けるだけで、ほかのセッションの書き込みを禁じる鍵でもお願いでもない。値の選び方は main が判断"}
glossary: []
```

## parallel-with-worktrees/review.md
[メインに判断してほしいこと]
- 強制力の属性を data に足すか（write.md の提案）
- 指摘 4 の版の fact 化

## headless-basics/write.md
[メインに判断してほしいこと]
- 数値の提案 3 件（facts-proposal.yml）。取り込めば、`#permissions` の既定の変遷と `--permission-prompts none` の版、`#output-and-exit-codes` の「直った版」に fact の目印を置ける。いまは版を書かず「公式で確かめる」と書いた
- 要点の「強制力」は、headless に強制力の属性がないため permission-modes の値（鍵）を指した。属性の持たせ方に別の決まりがあれば直す
[提案]
- 用語集：特になし

## headless-basics/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しを別の担当が確かめていないため）

## feature-to-api-mapping/write.md
[メインに判断してほしいこと]
- 比例則の警告が残った。目次の備考のとおり、守りのページは足さなかった。本文では `#combine` の末尾で、定期の作業の線引きとして `tasks-and-schedules-in-the-app#what-not-to-schedule` を指した
- 図の線の実線・破線：破線は web 検索・コードの実行 ↔ server tools と、定期・長時間の作業 ↔ Managed Agents（役割の近さ）。この分け方でよいか
[提案]
```yaml
frontmatter: []

## feature-to-api-mapping/review.md
[メインに判断してほしいこと]
- compare 表で MCP connector の行が、このページ自身へのリンクになる（data の `mcp-connector` の page がこのページ）。表示上は問題ないが、自己リンクを避けたいなら道具側の対応を検討する
- 比例則の警告は、目次の備考どおり残す判断でよいかを確認する

## sdk-comparison/write.md
[メインに判断してほしいこと]
- 「第三者の製品が claude.ai のログインやプランの上限を提供することは承認がない限り認められていない」を 2 か所に書いた（出典は Agent SDK overview。束の data の note と 02 §5-9）。公開の方針の文には当たらない（Anthropic の規則の紹介）と判断したが、気になるなら削る
- Managed Agents の単価は本文に書かず、facts-proposal.yml に提案した。承認されたら `#managed-agents` の「費用の面では」の文に fact の目印を足す
[提案]
- data：`facts-proposal.yml`（managed-agents-session-hour-price）
- 用語集：Agent／Environment／Session／Events（Managed Agents の構成要素）は本文で短く定義した。用語集への追加を検討してほしい

## sdk-comparison/review.md
[メインに判断してほしいこと]
- 指摘 1 の ZDR の説明は、一次資料で確かめていない。気になれば文言を直す
- write.md の「推論」の組み合わせ方 2 件は、断定が強くない書き方なので問題とは見なさなかった

## parallel-and-loop-costs/write.md
[メインに判断してほしいこと]
- 倍率「約7倍」は本文に書かず、条件つきと書いた（facts-proposal.yml）。Manage costs の原文は未確認（束の research/23 #7 に頼る）
- 「約 15 倍」（2025 年の Research 機能）は、研究の固定の記録として本文に書いた（根拠：中）。目印にするなら提案を足す
- `--max-turns`・`--max-budget-usd` は台帳 ralph-loops の本文を根拠に書いた。headless-basics#limits は束の指せる節にないので指さなかった
- `--max-turns` などを「確かに止める」仕組みと書いた。原文での確認はしていない
[提案]
- 雛形の「要る最低の版」が、features で subagents（1.0.60）になっている。tracks 全体だと 2.1.154（workflows）になるため `features: [subagents]` を expect に書いた
- 用語集：prh が「agent teams」を「エージェントチーム」に直す。表記の揺れは出なかったが、別名の行以外は日本語で統一した

## parallel-and-loop-costs/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま（直しの差分を別の担当が確かめていないため）。

## can-i-prompt-in-japanese/write.md
[メインに判断してほしいこと]
- 公式の多言語の表（Multilingual support）は、束の材料（旧世代の Sonnet 4.5 と Haiku 4.5 の旧い値）から更新され、Global-MMLU で Fable 5.1・Opus 5.5・Sonnet 5.5・Haiku 5.5 の日本語の値が載っている（Web を 1 回取得して確認）。本文は、モデル名と数値を手で書かず、「現行のどのモデルでも英語に近い。小さいモデルほど差がやや開く」と定性で書いた。下の提案の fact を採用するなら、`#evaluation` に表の目印を置ける
- research/27 #12 の「Sonnet 4.5 が 96.8%、Haiku 4.5 が 93.5%」は、公式の表に載らなくなったので本文に使っていない。目次の notes と summary（「比べたデータはない」は作業の指示に限る）は、このままで食い違わない
- `thinking-words` 節は、版の数字を書かず、「以前は CHANGELOG に記録があり効く時期があった」と書いた（台帳の行に版があるため）。台帳の行へは link で指した
[提案]
```yaml
proposals:
  - fact: {id: multilingual-global-mmlu-japanese, title: "公式の多言語の評価（Global-MMLU）で、英語を 100% とした日本語の成績（モデルごと）", value: "Fable 5.1 98.7%・Opus 5.5 99.2%・Sonnet 5.5 98.4%・Haiku 5.5 97.4%", sources: [api-docs-multilingual-support], checked: 2026-11-05, status: 確認済み}
    used_in: [can-i-prompt-in-japanese#evaluation]
    note: 最大の effort・adaptive thinking・zero-shot。1 ポイント未満の差は測定の揺れ、と公式が注記。表は 1 つの値に丸めず、モデルごとの表（fact-table）にしてほしい
```

## can-i-prompt-in-japanese/review.md
[メインに判断してほしいこと]
- 指摘を直したので stage は draft のまま（直しの差分を別の担当が確かめていない）
- write.md の提案（Global-MMLU の fact）を採るなら、#evaluation に fact-table の目印を置ける。本文は今、モデル名と数値なしで通じる

## explore-a-codebase/write.md
[メインに判断してほしいこと]
- `#guards-first` で plan mode を「編集を止めたまま調べさせる手」と一言だけ書いた（束に plan mode の説明の節がなく、suggest-or-do ページの言い回しに合わせた）。plan mode の使いどころの節は束の「指せる節」にないため link していない。確かめる担当に、この一言の正確さを見てほしい
- `#when-it-fails` の「繰り返し合わないときは、新しいセッションで範囲を狭めてやり直す」は、束の材料に根拠がない実務上の助言（推論）。残すか削るか判断してほしい
[提案]
- なし（数値の提案なし、front matter の提案なし、用語集の提案なし）

## explore-a-codebase/review.md
[メインに判断してほしいこと]
- 指摘 6 の助言を残すか。plan mode の一言（#guards-first）の正確さは公式で未確認（事実の検証は範囲外）
- 直したため stage は draft のまま

## spec-first/write.md
[メインに判断してほしいこと]
- mock-first は、束にモックの根拠の資料がない。「この辞典の推奨（推論・実践例なし）」と書いた。必須ページの題名に入る節なので、根拠の資料を足すか、節を軽くするかの判断がほしい
- 他ページの雛形（let-claude-ask/interview-feature、goal-until-done/stop-condition）を `gen:begin snippet` で取り込んだ。生成は通ったが、別ページの snippet を使う形がよいかの確認がほしい
[提案]
- 数値の提案なし。AskUserQuestion の 1 回の質問数は、本文に書かず、目印も使っていない
- 用語集・prh への提案なし

## spec-first/review.md
[メインに判断してほしいこと]
- mock-first の根拠の弱さ（write.md と同じ）
- 他ページの snippet を gen:begin で取り込む形でよいか（write.md と同じ）
- 直したので stage は draft のまま。別の担当による直しの差分の確認が要る

## research-and-reports/write.md
[メインに判断してほしいこと]
- Claude Code の面：web 検索・取得の動作は束の材料になく、記憶で書かなかったため「未確認」と書いた。必要なら Claude Code の担当ページ（または一次資料）での確認後に書き足す
- `compare` の表は tracks の 4 機能から生成される。表の列が読み手に合うかは生成後に見てほしい
- 台帳 `outdated-advice-ledger#cowork-separate-app` の link は、app-or-claude-code の節の末尾に置いた
[提案]
- front matter・用語集・data への提案はない。数値の提案もない（数値を本文に書いていない）

## research-and-reports/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま（直しの差分を別の担当が確かめていない）

## ai-usage-guidelines/write.md
[メインに判断してほしいこと]
- 「止まって相談する」の一行は、モデルの既定の癖に依存する旨の注記（11 第5節 A-3）。本文では「お願いで、観察として扱う」と expect に書くに留め、モデル名と確認日は書いていない。確認日を付けるなら、検証担当か作者の確認が要る
- 目次の notes にある「`data/holdout/` を禁止に挙げているのに A-4 で守っていない」は、claude-atlas 自身の雛形の話で、この辞典のページの雛形には関係しないと読んだ。雛形では .env・secrets/ を例にした
[提案]
- 用語集：「データの区分」を本文で短く定義した。必要なら用語集への追加を検討（強い提案ではない）
- front matter の提案：なし

## ai-usage-guidelines/review.md
[メインに判断してほしいこと]
- write.md にある「止まって相談する」の一行がモデルの癖に依存する旨の確認日の付け方（未確認のまま）

## practice-vs-contest-day/write.md
[メインに判断してほしいこと]
- kyopro-atlas の practice-method への指し方：本文は URL なしで名前だけ書いた（導入の段落）。公開 URL か相対リンクの決まりがあれば反映してほしい
- 「AtCoder の規則は過去問の練習には適用されない」は書いていない（未確認のため）。「練習と本番で規則の扱いが違うことがある」の一般の注意にとどめた
- 根拠の弱い主張に印を付けた：「丸投げ OK／要確認／禁止」の線引きと、解説役・採点役の使い分けは（根拠：弱）、部門の使い分けも（根拠：弱）、本番条件の確かめ方の手順は（推論・実践例なし）。必須ページの中心が推論になっていないか、見てほしい
- 部門の類型や AHC の日付・「今後数回」の範囲は、変わりやすいので本文に書かず competition-rules を指した
[提案]
- front matter、用語集、data への提案なし

## practice-vs-contest-day/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま。kyopro-atlas の practice-method の指し方は write.md の判断待ち

