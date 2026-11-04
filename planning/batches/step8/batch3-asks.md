## lethal-trifecta/write.md
[メインに判断してほしいこと]
- 目次の備考「アプリの二条件との対応を by-surface に書く」は、条件 1＝A、条件 2＝C と置き、B を数えない点を「この辞典の読み方（推論・実践例なし）」と書いた。この読みでよいか
- 材料 5（research/22 #27：クラウドの予定のタスクに頼んでいないコネクタが付いたときの警告）は、入った版（v2.1.317）が要る事実で、fact の id がまだないため本文に書かなかった。facts への追加と、tasks-and-schedules-in-the-app 側での扱いを検討してほしい
[提案]
- 数値の提案なし。用語集・prh・front matter への提案なし

## lethal-trifecta/review.md
[メインに判断してほしいこと]
- write.md の 2 件（アプリの二条件の読み。材料 5 の v2.1.317 の扱い）はそのまま引き継ぐ
- 警告 12 件を直すか残すか

## vetting-extensions/write.md
[メインに判断してほしいこと]
- 判断例を 1 つ置いた（provenance）。「選んだもの」が実質、個人の好みの標準に見えないか確認を
- dependencies の「入れる前に確かめる観点」は一般的な観点にとどめ、具体のコマンドや registry の機能は書いていない（brief どおり、一次資料は開いていない）。必要なら後の波で補う
- mods と plugin の「確認を重くする」の線引き（checklist の「重くする」の列挙）は、このページの推奨であって公式の立場ではない。根拠の印は付けていない（推論・実践例なし）
[提案]
```yaml
frontmatter:
  - {id: vetting-extensions, key: sections, before: "4 節", after: "guards・checklist・after-install の 3 節を足した 7 節", reason: "recipe の構成の目安（守り・確かめ方・失敗したとき）を満たすため。ページ側はすでに反映済み"}
```

用語集への提案：「サンドボックス」は prh の指定どおり使った。「tool poisoning」「rug pull」「slopsquatting」は本文で短く定義した（用語集に無ければ追加を提案する）。

## vetting-extensions/review.md
[メインに判断してほしいこと]
- Claude Code タブの「全部の一覧を作る」に具体の手段（`/mcp` など）を足すかは、一次資料で確かめてから
- 雛形の `features: [mcp]` は版の注記を消すための指定。別の指定がよければ決めてほしい

## protecting-secrets/write.md
[メインに判断してほしいこと]
- 面「app」のタブを置いていない。アプリの権限ルール・サンドボックスの有無を束で確かめられなかったので、アプリは default-safety-settings#defaults-by-surface を指すだけにした。タブが要るなら、アプリ側の根拠の追加が要る
- 雛形の `sandbox.credentials.envVars`（deny）は、公式の sandboxing 文書の例から取った。書き方・動作の確認は動作確認の担当へ
- when-it-fails に、リポジトリの設定ファイル経由で API キーが外へ出た脆弱性（修正済み）への言及を 1 行置いた。手口は書いていない。名指しの出典（Check Point）は sources に入れていない
[提案]
- なし（数値・用語集・prh への提案はない）

## protecting-secrets/review.md
[メインに判断してほしいこと]
- アプリ面のタブを置くか（指摘 3）

## destructive-commands/write.md
[メインに判断してほしいこと]
- 見逃しの割合（auto モード、公式記事の 17%、n=52）は facts にないので、本文に書かず、`what-auto-mode-stops#limits` へ指した。facts へ足すなら下の提案
- アプリの面（surfaces に app）は材料がなく、タブを作らず「未確認」と一文で書いた。app の調査が要るか
- 本文に Opus 4.6 の名がある（prompting ガイドの記述の時点の名として）。ルール上は変わりやすい名前なので、扱いを見てほしい
[提案]
```yaml
proposals:
  - fact: {id: auto-mode-overeager-miss-rate, title: "auto モードの分類器が実トラフィックの過剰に積極的な行動を見逃した割合", value: "17%（n=52）", sources: [anthropic-eng-code-auto-mode], checked: 2026-11-05, status: 要確認}
    used_in: [destructive-commands#misconceptions]
```

## destructive-commands/review.md
[メインに判断してほしいこと]
- 警告 2 件を許すか。許さないなら 44 行は「ファイル・履歴・データ」に、91 行は箇条を分ける
- 作者の判断：Opus 4.6 を外した扱い（write.md の判断事項）でよいか

## what-not-to-delegate/write.md
[メインに判断してほしいこと]
- `who-adopted` の AtCoder World Tour Finals 2026 の記述は、束の報道 2 件の題名と材料の要約だけに基づく（根拠：弱）。研究資料 25 P1 を読んでいないので、記述が材料と合うか確認してほしい。合わなければ該当の箇条を削る
- 事例の人名（Kaggle 1 位の参加者・Unagi 等）は出していない（第三者の扱い）。書き方の方針（第三者）1 に照らして問題ないか
[提案]
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし

## what-not-to-delegate/review.md
[メインに判断してほしいこと]
- who-adopted の AtCoder World Tour Finals 2026 の箇条は報道の題名ベース（write.md のとおり）。research/25 P1 との照合が要る
- 「考察の出どころが AI であることは、すでに起こりうる」は報道からの推論として強め。照合の結果で弱めるか削る

## five-questions-before-delegating/write.md
[メインに判断してほしいこと]
- 材料の 6.3 p34#141 の「三条件」（機械的な合否・隔離・外部記憶）を #back-to-dialogue に（根拠：弱）で入れた。「外部記憶」は束に定義がなく、「会話が圧縮されても残る記録」と読み替えた。出典の個別 id が束にないため sources には足していない。読み替えが正しいか確認がほしい
- 4 段の分け方（p34#151）も出典 id が束にないため（根拠：弱）の実践者の整理として書き、sources に足していない。出典の id を特定できるなら足してほしい
- 「2026-11-05 に Best practices の改稿後の版にも 5 つの問いがある」と本文に書いた（WebFetch 1 回で確認。節「Let Claude run without you」）
[提案]
- 変わりやすい値の提案はなし（`--max-turns` などの数値は本文・雛形とも置いていない）
- 古くなった助言の台帳へ `outdated-advice-ledger#yolo-skip-permissions` を link した（#proportional-guards）

## five-questions-before-delegating/review.md
[メインに判断してほしいこと]
- 指摘 2 の表の幅（列を絞るか）
- write.md の 2 件（「外部記憶」の読み替え、4 段の出典 id）は未解決のまま

## goal-until-done/write.md
[メインに判断してほしいこと]
- 雛形 run-unattended は `--max-turns`・`--max-budget-usd` の効き方を手元で確かめていない（台帳の記述に基づく）。載せてよいか
- 「比べる相手」は comparison ページが束になかったので、箇条で書いた
[提案]
```yaml
frontmatter:
  - {id: goal-until-done, key: related, before: [...], after: [..., how-usage-limits-work], reason: "利用上限の節から、上限の主のページ（auto-continue・wrap-up-allowance の page）を指したい。束の指せる節にないので本文ではリンクしていない"}
proposals:
  - fact: {id: goal-condition-max-chars, title: /goal の条件の長さの上限, value: 4000, unit: 文字, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#writing-conditions]
  - fact: {id: goal-idle-checkins-max, title: /goal の席が空いている間の確認の呼びかけの回数の上限（v2.1.246 以降）, value: 3, unit: 回, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#evaluator-reads-conversation]
  - fact: {id: goal-auto-retry-max, title: /goal の自動の再試行の回数（過負荷・切断。超えると一時停止。v2.1.269 以降）, value: 3, unit: 回, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#at-usage-limits]
  - fact: {id: goal-checkin-minutes, title: 背景の作業を待つときの最初の確認の間隔（CLAUDE_CODE_GOAL_CHECKIN_MINUTES で変更）, value: 30, unit: 分, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#evaluator-reads-conversation]
  - fact: {id: auto-continue-max, title: 利用上限での自動の継続の回数の上限（/goal も同じ）, value: 3, unit: 回, sources: [cc-docs-interactive-mode, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#at-usage-limits]
```
本文は上の数値を書かない形にしてあり、目印を置く場所は used_in のとおり（目印は提案が通ってから足す）。

## goal-until-done/review.md
[メインに判断してほしいこと]
- 要点の「強制力」を手書きの文にしている。カードは `feature` の目印で指す形。data の note が強制力を書かないとするため、目印にできるかの確認が要る

## humans-set-the-parallel-limit/write.md
[メインに判断してほしいこと]
- 「この辞典の推奨」として「まず 1〜3 本から」と書いた（目次の notes と research/03 W9 に従い、（推論・実践例なし）の印を付け、実践者の幅と三段で並べた）。数値の目印にはしていない
- 実践者の本数（1 本・最大 2 本・3〜4 本・5 本以上）を、個人名なしで自己申告として本文に書いた。標準として示してはいない。方針に反するなら削る
- 制作で多数の担当を同時に動かすこと（research/21 §2.4）は、本文で触れなかった。レビューの要らない調査・偵察かどうかの区別で説明する案は目次の notes にあるが、制作の運用に関わる自己言及なので入れていない
[提案]
- 数値・front matter・用語集・prh の提案はなし

## humans-set-the-parallel-limit/review.md
[メインに判断してほしいこと]
- 「まず 1〜3 本から」の推奨と、実践者の本数を自己申告として載せた点は、write.md の判断待ちのまま。
- 「疲れの兆し」5 項目は出典のない整理（根拠：弱と明記済み）。

## choosing-parallel-modes/write.md
[メインに判断してほしいこと]
- 「1〜2 割は捨てる」を自己申告・根拠：弱で #expect-to-discard に置いた。個人の構成として標準にはしていない。実在の人物の名は出していない。この扱いでよいか
- 「3〜4 本ほど」の上限の声も経験則として置いた。数値の目印にすべきか
[提案]
```yaml
frontmatter: []
facts: []
```
- 用語集・prh への提案はなし。prh は subagents → サブエージェント、agent teams → エージェントチームを要求するので本文はそれに従った。agent view と workflows は原文のまま

## choosing-parallel-modes/review.md
[メインに判断してほしいこと]
- 指摘 3：表の Projects 行が自ページを指す。データ側の page を変えるか、このままか
- write.md の「3〜4 本」を数値の目印にするかは未判断

## human-pitfalls/write.md
[メインに判断してほしいこと]
- 「先に人が答える」（Buçinca ほか 2021）を本文に使った。brief の notes は「一次資料を確かめていない」とするため、PDF を 1 回取得したが読み取れず（本文が取れない）確かめられなかった。束の 6.4 の写しの内容（誤った AI への依存を減らす／成績のよい設計ほど好まれない）を（根拠：中・類推）で書いた。確かめるまで強めない、または削る判断がほしい
- 「確かめる手間を下げる」（Vasconcelos ほか 2023）は、既存の over-reliance の記述（著者らの見立て・模擬の AI）に合わせ、（根拠：中・類推）で書いた
[提案]
- 数値の提案（facts）はなし。研究の結果は固定の記録として本文に書いた（card §7）
- 用語集・prh・front matter の提案はなし

## human-pitfalls/review.md
[メインに判断してほしいこと]
- 執筆の報告にある Buçinca ほか（2021）の一次資料の未確認。確かめるまで削るか弱めるか

## decide-when-to-quit/write.md
[メインに判断してほしいこと]
- 判断例のうち 2 つ目の 0.57・±0.05 の話は、400 試合の 95% 区間（±0.049）の計算から作った例。数値を例と明記済み
- 方針・約束の文は足していない（カード §13）
[提案]
- なし（用語集・prh・data・front matter の直しは出さない）
- 数値の提案もなし。0.60・4 回・400 試合・3 回連続は、雛形と判断例の中で「例」と明記した。研究の数値（ρ など）は、研究の名・年・対象を添えて本文に書いた

## decide-when-to-quit/review.md
[メインに判断してほしいこと]
- 判断例 1 の理由は、誤差の扱いを事前に決める話に落ち着くため、やや込み入る。読者に硬ければ簡素化を検討してほしい（今回は直さず）

## ai-ideas-are-everyones/write.md
[メインに判断してほしいこと]
- 10.7% は工程2で確かめていないため本文に書かなかった（原論文の science.org は check_noai で断る指定あり）。代わりに「作品どうしが似通った」とだけ書いた。原論文を出典にできない件（11 第4節 #55 の指示）をどうするか
- 「なぜ（人の側の仕組み）」は独立の節にせず、既存 sections の中に短く入れた。分けたほうがよければ節の追加を判断してほしい
[提案]
- front matter の直しの提案はなし
- 用語集・prh への提案：なし

## ai-ideas-are-everyones/review.md
[メインに判断してほしいこと]
- 特になし（write.md の 10.7% の扱いは作者判断のまま）

## learning-with-ai/write.md
[メインに判断してほしいこと]
- 競技の上位解法の読み方そのものは kyopro-atlas を指す決め（カード §8）だが、URL・ページ名が束になく、リンクを置いていない。置くなら `summaries-of-solutions` の末尾に 1 文を足す
- 研究の割合・件数は、カード §7 の「研究の結果は固定の記録」に従い、研究名・年・対象を添えて本文に手で書いた（facts への提案はしていない）。この解釈でよいか
- 判断例の「30 分ほど」は、この辞典の根拠のない目安である。残すか、「少しの時間」に弱めるか
[提案]
```yaml
frontmatter:
  - {id: learning-with-ai, key: summary, before: "AI に書かせると速く進む一方で理解が残りにくいことと、…", after: "（直さなくてよい。ただし本文は『速さの得は確かめられていない』と書くので、『速く進む』を『進んでいるように感じる』などに弱める案がある）", reason: "Anthropic の研究で完了時間の差は有意でない（束 6.1・6.6）。題名・summary の『速く進む』と本文の言い方に温度差がある"}
```

用語集への提案：なし（用語集を読んでいない。`認知負債`・`技能形成` が語になっているかは未確認）。

## learning-with-ai/review.md
[メインに判断してほしいこと]
- 節 faster-but-shallower の題と summary の「速く進む」を、本文（速さの得は未確認）に合わせて弱めるか。題の変更は front matter の sections の title とあわせて要る
- ほかの write.md の判断事項（kyopro-atlas へのリンク）は未対応のまま

## how-usage-limits-work/write.md
[メインに判断してほしいこと]
- 節 limit-types の題は「（プランごとの表）」だが、表にする数値が facts にないため表の目印を置いていない（置くと検査が止まる）。facts-proposal.yml の usage-limit-types-by-plan を採るなら、節に `<!-- gen:begin fact-table usage-limit-types-by-plan -->` の組を足す。採らないなら題から「（プランごとの表）」を外すか、choosing-a-plan の表への link のままにする（今はそうしている）。Team の席ごとの値は束に材料がなく null にした
- auto-continue-max-times・wrap-up-allowance-frequency・wrap-up-allowance-min-version を採ったら、#when-you-hit-the-limit の「続ける回数には上限がある」「回数はプランで違う」「新しい版が要る」の所に fact の目印を足す（今は数字なしで読める形）
- 用語集に「利用上限」の項があるか確かめていない。本文は題名どおり「利用上限」、別名の行に「利用制限」「使用制限」
[提案]
- 数値：facts-proposal.yml（used_in つき）
- front matter：なし

## how-usage-limits-work/review.md
[メインに判断してほしいこと]
- #limit-types の題の「（プランごとの表）」と中身の不一致（write.md の判断と同じ）

## what-uses-up-limits/write.md
[メインに判断してほしいこと]
- 節 effects・misconceptions を足した。目次の sections が 3 つだったので、catalog 側の同期が要るなら反映を頼む
[提案]
```yaml
frontmatter:
  - {id: what-uses-up-limits, key: sections, before: [causes, long-sessions, find-what-uses-it], after: [causes, long-sessions, find-what-uses-it, effects, misconceptions], reason: "concept の必ず持つもの（何に効くか・誤解）を節にした"}
```

## what-uses-up-limits/review.md
[メインに判断してほしいこと]
- 節 effects・misconceptions を足した sections の同期（write.md の提案どおり）

## saving-priorities/write.md
[メインに判断してほしいこと]
- 図は置かなかった。目次の visual が「なし」のため。置くなら、順位の 5 段の図を提案できる
- 「API」のタブは束に材料が少なく、effort の評価と「履歴は呼び出す側が持つ」という一般的な説明だけにした。後者は束の材料に出典がない（API の文書で確かめるなら出典の追加が要る）
[提案]
- 用語集・prh・data への提案はない
- 数値の提案もない（本文に変わりやすい値を書いていない）

## saving-priorities/review.md
[メインに判断してほしいこと]
- API タブの「履歴を持つのは呼び出す側」に出典を足すか（上の 3）

## align-japanese-output/write.md
[メインに判断してほしいこと]
- 「確認日と版を付けて」書く挙動（強制できる場所・アプリに機械の仕組みがないこと）に、確認日 2026-11-03 は付けたが、Claude Code の版は付けていない（束に版がなく、版は入った版に当たるため手で書かない）。版を付けるなら数値の提案が要る
- 判断例を 2 つ置いた（`#app`、`#keep-few`）
[提案]
- なし（用語集・prh・data・front matter の直しの提案はない）

## consistent-politeness/write.md
[メインに判断してほしいこと]
- なし（公開の約束・方針の文は入れていない）
[提案]
- 用語集・prh・data への提案はなし
- 数値の提案はなし（変わりやすい値は本文に書いていない）

## consistent-notation/write.md
[メインに判断してほしいこと]
- 本文の方針の文（「plan mode・effort・allow ルール…の 3 語だけを英語のまま書く」）は design §6.2 とカード §4 の写しで、約束の文ではないと判断した
- scripts の置き場所：雛形は Python（PyYAML）。リポジトリの tools には置かず、読者向けの例にした
[提案]
- 用語集への提案：「表記の正本」「漢字を開く」を用語に入れるか（本文で短く定義した）
- prh.yml への提案：なし（例の語〔サーバ・ユーザ・出来る など〕は雛形の中だけ）

## consistent-notation/review.md
[メインに判断してほしいこと]
- #5 の prh specs の挙動を、事実の検証役に確かめてほしい。

## textlint-hook/write.md
[メインに判断してほしいこと]
- `onFailure: "block"` が入った版（公式の文書では v2.1.295 以降）を本文に書いていない。fact の id が data にないため。fact の追加を提案する（下）。入れば #failure-and-few に目印を置く
- #failure-and-few の「この辞典の制作でも、縛る規則は少なく絞る方針」は制作の方針（decisions 2026-11-03）への言及。公開の方針の文と見なすなら削る
[提案]
```yaml
proposals:
  - fact: {id: hook-on-failure-block-min-version, title: フックの onFailure "block" が使える最低の版, value: "2.1.295", sources: [cc-docs-hooks, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [textlint-hook#failure-and-few]
```
- 用語集・prh・front matter への提案はなし

## textlint-hook/review.md
[メインに判断してほしいこと]
- `onFailure` の版の fact 提案（write.md）の反映。入ったら #failure-and-few に目印を置く

## fix-a-bug/write.md
[メインに判断してほしいこと]
- 「checkpoints-and-rewind」を related にない状態で本文から link した（when-stuck と guards-first）。related への追加が要るか
- when-stuck の症状への表は手書き（このページの routes が空のため）。routes に入れるなら front matter の提案が要る
[提案]
- 特になし（数値の提案はなし。研究の割合は書かず、変わりやすい値は本文に書いていない）

## fix-a-bug/review.md
[メインに判断してほしいこと]
- write.md の 2 件（checkpoints-and-rewind を related に足すか、when-stuck の表を routes にするか）は未判断のまま

## review-bottlenecks/write.md
[メインに判断してほしいこと]
- 本文は、事例の社名（READYFOR・Rehab for JAPAN）を、各社が自社の数値を報告した形で出した。否定的な文脈ではないが、名指しの扱いが気になるなら社名を外してよい
- 「一次資料で確かめたこと」：asoview の記事を 1 回取得し、「1 件 10〜15 分が 2〜3 分」「承認の自動化はやりすぎ」の記述と、測定条件の記載がないことを確かめた。READYFOR・Rehab for JAPAN の数値は束の research/25 P7 の写しによる（元記事は取得していない）
[提案]
- なし（用語集・prh・data・front matter の他のキーの提案はない）

## review-bottlenecks/review.md
[メインに判断してほしいこと]
- 79・97 行の助詞の警告を残した（流す回数の上限のため）。必要なら直してほしい

## does-more-than-asked/write.md
[メインに判断してほしいこと]
- 古くなった助言の台帳は `outdated-advice-ledger#keep-going-dont-be-lazy` で指した。related にも prerequisites にも入っていないので、リンクの検査の結果を見てほしい
- 診断 2 の洗い出しは、研究（過剰な不適合判定）を理由に「判定・修正案を求めない」雛形にした。根拠は旧世代のモデルを含む研究で、（根拠：中・類推）と書いた
[提案]
- facts の提案なし（本文に変わりやすい値は書いていない。モデル名は公式文書の題名にだけ出る）
- 他の提案なし

## does-more-than-asked/review.md
[メインに判断してほしいこと]
- 診断 2 の「同じ会話の Claude は、自分の変更を甘く見やすい」は出典がない一般論に見える。事実の検証役に回してほしい（私は事実を見ていない）

## keeps-stopping/write.md
[メインに判断してほしいこと]
- 手順 1 に「古い版の不具合」を数値なしで書いた（版は facts-proposal.yml に提案）。本文に版を出さない形でよいか。
- 手順 6 で Sonnet の low・medium の癖を、公式の指針へのリンクと確認日（2026-11-05）つきで書いた。モデルの名前はリンクの題名にだけ出た（本文の地の文には出さない）。
- 手順 4 の権限モードは「Claude Code の機能」と書いた（data の surfaces が claude-code のみ）。アプリ側の確認の出方は書いていない。
[提案]
- facts-proposal.yml：auto-mode-no-verdict-display-fixed（used_in：keeps-stopping#diagnosis。本文に目印はまだ置いていない。採用されたら、手順 1 の「現在は修正されている」の前後に目印を足せる）

## keeps-stopping/review.md
[メインに判断してほしいこと]
- 手順 1 の不具合の修正は束の写しに基づき未確認。CHANGELOG での確認を事実の検証に回す

## refused-or-blocked/write.md
[メインに判断してほしいこと]
- 「人の側の落とし穴」は pitfalls が空のため、言い換えて通そうとする癖を 1 段落だけ本文に書いた。pitfalls への追加が要るかは判断を仰ぐ
- 「合っていない」の枝に、フックの停止の見分け方（理由の文面が自分の書いたものと一致する）を書いた。記憶に頼らず束の材料だけで書いたが、面ごとの表示は未確認
[提案]
- 数値・用語集・prh・front matter への提案はなし

## refused-or-blocked/review.md
[メインに判断してほしいこと]
- 指摘 3 のため、面ごとの停止の表示は when-requests-are-refused 側で持たせる必要がある

## insists-on-mistakes/write.md
[メインに判断してほしいこと]
- 事例（存在しないバグを擁護し、履歴の検索で撤回）は、他社のモデルの単独の経験談なので、モデル名を出さず「根拠：弱」にした。lukyanenko-kaggle-antigravity-s6e7 の「The bug that never existed」の節を WebFetch で確かめた（書き手が実際の行を見せ、エージェントが履歴を検索して誤記がなかったと確認）。出典は sources に入れたが、本文に書き手の名は出していない。
- 「人の側の落とし穴」は、束に五つの中身がなく、six-causes#human-side を指すだけにして、本文に「違うとだけ返すと手がかりがない」を（推論・実践例なし）で 1 つ置いた。多すぎれば削ってよい。
[提案]
- 数値の提案、front matter の提案、用語集・prh への提案は、なし。

## insists-on-mistakes/review.md
[メインに判断してほしいこと]
- 警告の修正後は未検査。メインの一括検査で確かめてほしい。

## plausible-falsehoods/write.md
[メインに判断してほしいこと]
- sections に 4 節を足した（forms・to-fixes・examples・prevent）。routes の目印は、stub では diagnosis の中だったが、to-fixes に分けた
- 「Claude Code」タブは、束に claude-code の根拠がないため、手元のファイルを読ませて引用させるという一般的な書き方にとどめた。確かめが要れば指示がほしい
- 判断例 2 つ目の「揃った場合も原文で確かめるまで採用しない」は、固有の出典がなく筆者の推論。fact-checking#best-of-n の持ち主ページと食い違わないか確かめてほしい
[提案]
- なし（数値は本文に書いていない）

## plausible-falsehoods/review.md
[メインに判断してほしいこと]
- write.md の 3 点（Claude Code タブが一般論、判断例 2 の推論、routes の節の分割）は変更せず残した

## uses-nonexistent-apis/write.md
[メインに判断してほしいこと]
- 「知識の古さ」は六つの原因の名前が束にない（prevents は 3 つ）ため、診断の 2 番目に「版が合っているか」として置いた。六つの原因の並びと名前が site.yml と合うか見てほしい。
- 診断の 2 番目は routes に行き先がなく、前提と doesnt-know-latest#diagnosis を本文で指した。routes に knowledge-cutoff 等を足す案は出していない。
[提案]
- 用語集・prh・data への提案なし。front matter の提案なし。

## uses-nonexistent-apis/review.md
[メインに判断してほしいこと]
- write.md の指摘どおり、診断の「版が合っているか」を 2 番目に置いたことが site.yml の六つの原因の並びと合うか。確かめていない。

## doesnt-know-latest/write.md
[メインに判断してほしいこと]
- 知識の締め切りの日付が data/facts.yml にない（grep で該当なし）。本文は日付なしで書き、fact の目印は置いていない。下の提案を入れたら、#diagnosis の 1 番に目印を足したい
- 型の手引きの「六つの原因を安く確かめる順」に対し、このページの prevents は「見えていない」の 1 つだけなので、1 つの原因の中を 6 つの確かめ（日付・版・検索・資料・検索結果の古さ・資料の薄い領域）に分けた。この解釈でよいか
- 項目 6 の「資料の薄い領域」は、材料 6.5（CTF の観察）を（根拠：弱・類推）で 1 文だけ使った。材料は 2 次の一般化なので、削ってもよい
[提案]
```yaml
proposals:
  - fact: {id: current-models-reliable-knowledge-cutoff, title: 現行モデルの reliable knowledge cutoff, value: "2026-06（モデルごと。Opus 4.6 は 2025-05）", sources: [api-docs-models-overview, api-docs-opus-4-6-overview], checked: 2026-11-04, status: 確認済み}
    used_in: [doesnt-know-latest#diagnosis]
  - fact: {id: current-models-training-data-cutoff, title: 現行モデルの training data cutoff, value: "2026-06（モデルごと。Opus 4.6 は 2025-08）", sources: [api-docs-models-overview, hc-up-date-training-data], checked: 2026-11-04, status: 確認済み}
    used_in: [doesnt-know-latest#diagnosis]
```
- 値は research/26 #12 の写しによる（束の 6.3・6.4）。モデルごとの表にするかは、メインが data の形に合わせて決める
- 用語集への提案：「reliable knowledge cutoff（確かな知識の日付）」と「training data cutoff（学習データの日付）」の区別が、knowledge-cutoff 側にあるか確かめたい（本文は「確かな知識の日付」「学習データの日付」と書いた）

## doesnt-know-latest/review.md
[メインに判断してほしいこと]
- write.md の提案どおり、締め切りの日付が data にない。入ったら #diagnosis の 1 番に目印を足す
- 事実の正しさ（Claude Code と API の検索の説明）は検証の対象外で、write.md の「確かめていないこと」のまま

## old-advice-doesnt-work/write.md
[メインに判断してほしいこと]
- 台帳の行ごとの節（`outdated-advice-ledger#<行の id>`）は束の「指せる節」にないため指さず、台帳の入口と `#find-in-your-setup` を指した。カード §11 は行の id で指すとあるので、指せる節が増えたら差し替えるか判断してほしい
- 判断例は `/agents` を使った。台帳の行の内容（作成の画面が撤回）に基づく。版の数値は本文に書いていない
[提案]
なし（front matter・用語集・数値への提案は無い）

## old-advice-doesnt-work/review.md
[メインに判断してほしいこと]
- 台帳の行ごとの節を指せない件は write.md のとおり。指せる節が増えたら差し替え

## skipped-later-pages/write.md
[メインに判断してほしいこと]
- 「安く確かめられる順」は prevents の並び（見えていない → 散らかっている）に従った。site.yml の並びとの照合はしていない（束にない）。
[提案]
読み込みの範囲の数値（PDF の図まで読まれるページの上限・文字だけが読まれるページの上限・拒否される上限）は data/facts.yml の facts に id がなく、本文には書かなかった（文で「一定のページ」と言い、値は how-attachments-are-read#pdf-and-others を指す）。how-attachments-are-read 側で fact を作るなら、このページは本文を直さずに目印へ差し替えられる。

```yaml
proposals:
  - fact: {id: pdf-visual-page-limit, title: PDF で図表まで読まれるページ数の上限（アプリ）, value: 未確定（束の材料 05 §2-5 では「100ページまで」）, sources: [hc-upload-files], checked: 2026-11-05, status: 要確認}
    used_in: [skipped-later-pages#diagnosis]
  - fact: {id: pdf-text-only-page-limit, title: PDF が文字だけで読まれるページ数の上限（これを超えると拒否）, value: 未確定（同「1000ページ」）, sources: [hc-upload-files], checked: 2026-11-05, status: 要確認}
    used_in: [skipped-later-pages#diagnosis]
```

## summary-overstates-source/write.md
（ファイルがない）

## summary-overstates-source/review.md
[メインに判断してほしいこと]
- 執筆の終了後に、この検証を回し直す。
- 雛形が先にできていて、本文が未書きなので、執筆が途中で止まった可能性がある。

## forgets-in-long-chats/write.md
[メインに判断してほしいこと]
- 診断の人の側の項目は、five の落とし穴の中身を束で見ていないため、特定の落とし穴の名を挙げず「前提が文面にない・後の指示と食い違う」と書いた。six-causes の内容と合うか確認してほしい
- `outdated-advice-ledger` ページは準備中のため、台帳の 2 行を link の目印で指した
[提案]
なし（数値・front matter・用語集への提案はない）。

## forgets-in-long-chats/review.md
[メインに判断してほしいこと]
- 雛形の「要る最低の版」の注記が、面を問わない依頼にも出る。features を空にする指定が可能か、メインが判断してほしい

## going-in-circles/write.md
[メインに判断してほしいこと]
- 訂正の回数の目安（公式は 2 回）を、数値の提案にした。採用なら `#choose` の「さらに訂正を足さないよう勧める」の後に fact の目印を置く文へ直す（本文には数字を書いていない）
- 確認日付きの記述として「公式の Best practices（2026-11-05 に確認）」と書いた。確認は WebFetch 1 回（best-practices の /clear の節）
[提案]
- data/facts.yml：facts-proposal.yml のとおり（best-practices-clear-after-failed-corrections）

## going-in-circles/review.md
[メインに判断してほしいこと]
- 研究段落の削除で sources を 1 件にした。研究の根拠を戻すなら、前提の context-rot 側に置くのが筋
- 162 行の警告は、リンクの題名が文に入るための誤検出に近い

## forgot-after-compaction/write.md
[メインに判断してほしいこと]
- 診断の 6 項目目（版）は、圧縮まわりの不具合が更新履歴で直った旨だけを書き、版の数値は本文に出していない。入った版（v2.1.317 など）を目印で示すなら、数値ファイルへの追加が要る（下の提案）
- アプリと API は「未確認」と 1 文で書いた（束に材料がないため）。タブにしていない
- 「人の側の落とし穴」は、診断の節末で six-causes を指すだけにした
[提案]
```yaml
proposals:
  - fact: {id: compaction-bugfix-min-version, title: 圧縮の後の "Prompt is too long" と要約の取りこぼしを直した版, value: v2.1.317, sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [forgot-after-compaction#diagnosis]
```
（根拠は束 6.5。本文には目印をまだ置いていない。採用するなら診断の 6 項目目に目印を足す）

## forgot-after-compaction/review.md
[メインに判断してほしいこと]
- 項目6の版の目印は、write.md の提案（compaction-bugfix-min-version）を採るかの判断待ち

## unexpected-memories/write.md
[メインに判断してほしいこと]
- 「メモリの項目（Topics）を設定で開く」は台帳 memory-daily-summary の now の文に基づく。設定画面の項目名の詳細は how-memory-works に任せ、本文では書いていない
- 「ほかのプロジェクトの記憶が混ざる」の項目 3 は、「プロジェクトはそれぞれのメモリを持つ」（data の note）の範囲に留めた。05 §2-4 の「プロジェクト内ではアカウント全体のメモリも併用される」は、data の note と書き方が違うため本文に入れていない（how-memory-works#scope の側で確定してほしい）
[提案]
- なし（用語集・prh・data への提案なし）

## unexpected-memories/review.md
[メインに判断してほしいこと]
- 症状「会話を消したのに覚えている」の人向けに、項目 5 を先頭近くへ動かすか（順は front matter の方針次第）

## repeating-the-same-explanation/write.md
[メインに判断してほしいこと]
- 診断の 1 項目目と末尾の段落に「書いてあるのに守られない」「毎回変わる部分」の確認を置いた（原因 2 つ以外の切り分け）。症状の言い換えと重なる所なので、不要なら削る
- 「回数を目安にした足し方」は when-to-add-what に任せ、公式の表の回数（2 回・3 回）は本文に書かなかった（数値の id がないため）
[提案]
- 数値の提案：なし
- 雛形の `control` は私の推測の書き方（「返りやすい」）。動作確認の担当が試すまで記録として扱う

## repeating-the-same-explanation/review.md
[メインに判断してほしいこと]
- 雛形の置き場所を診断側に移すか。現状のままでも可

## inconsistent-japanese-style/write.md
[メインに判断してほしいこと]
- 「いつ引くか」と「よくある形」で、sign の「サーバー」と「サーバ」を、prh の誤検出を避けるため「同じ語の表記が混在する」と言い換えた（`#forms` にだけ例を出し、`textlint-disable prh` で囲んだ）。sign の文字そのものを要点に出したいなら、検査の結果を見て判断してほしい
- アプリと API の「機械で確かめて差し戻す仕組み」は、他の症状ページ（replies-in-english）に合わせて「未確認」と書いた
[提案]
用語集・prh・data・手引きへの提案はない。

## inconsistent-japanese-style/review.md
[メインに判断してほしいこと]
- write.md にある、sign の「サーバー」と「サーバ」の言い換え（#forms にだけ例を出す）は、そのままでよいと見る。sign の文字を要点に出したければ、メインが判断する

## rewrote-tests-to-pass/write.md
[メインに判断してほしいこと]
- 診断の「縛っていない」で、「Edit の deny ルールだけでは子プロセスの書き込みを止められないことがある」と書いた。束の freeze-eval-assets と permission-rules の要約に基づく。持ち主のページ側と食い違わないか、メインの確認を頼む。
- 「確かめていない」の項に、ImpossibleBench の「止まる権利」の効果（Claude Opus 4.1 では小さい）を入れた。束の research/24 A-10 の写しに基づき、数値は Claude 以外のモデルのものを書いていない。
- 初動に `git restore --source=<時点> -- <テストのパス>` を書いた。保存した差分を先に取る手順を前に置いた。
[提案]
- 用語集・prh・data への提案はなし。
- front matter の直しの提案はなし。

## rewrote-tests-to-pass/review.md
[メインに判断してほしいこと]
- write.md の項目のとおり、「Edit の deny ルールだけでは子プロセスを止められないことがある」の記述が持ち主のページと合うかの確認が要る（事実は見ていない）

## misses-broken-evaluation/write.md
[メインに判断してほしいこと]
- 「よくある形」の最初の 2 件の出典は束の材料メモ（10 第8章。ANDPAD の 10 実験目の話と、Pebblous の要約が伝える研究）にだけ頼り、元の記事は開いていない。ANDPAD の例の対象モデルは「未確認」と書いた。公開の前に原文での確認を勧める
- 診断の項目 5 の「エージェントが自分の作業を高く評価しやすい」は、anthropic-eng-harness-design-long-running（束の 10 第18章の写し）に基づく。同じ流れで評価を確かめる役を持たせない、という書き方にした
[提案]
- 用語集：OOF（学習に使わなかった分の予測）を本文で短く定義した。用語集に項目があるか、なければ追加を提案する
- 数値の提案：なし（研究の固定の結果だけを、名前・年・対象のモデルを添えて書いた）

## misses-broken-evaluation/review.md
[メインに判断してほしいこと]
- 指摘 6：#forms の 2 件目の出典の原文確認

## stuck-in-a-check-loop/write.md
[メインに判断してほしいこと]
- routes の節を diagnosis の外（#routes）に分けた。stub では diagnosis の中だった。anchor の `diagnosis` は変えていない。他の symptom ページと並びを揃えるなら、戻してよい
- 実例の ISUCON13 の記事（zenn-microsoft-78e01f59）を取得して確かめた。記事に「対処として手法の知識や検索を与えた」記述はなく、今後の改善案として Agent Skills や検索用 MCP を挙げるだけだった。調査資料（11 の行）は「対処は…新しい仮説を入れること」と書く。本文は記事に合わせた。調査資料の表現の見直しを提案する
- 実例の対象は Azure SRE エージェントで、Claude とは限らない。本文は「類推」を付けた
[提案]
- 数値の提案はなし（本文に変わりやすい値を書いていない。時間の「約 1 時間」「3〜4 時間」は報告の時点の記録として、報告の名を添えて書いた）
- front matter の提案はなし

## wont-rethink-approach/write.md
[メインに判断してほしいこと]
- 診断の並び（散らかっている → 確かめていない）は front matter の `prevents` の順に従った。site.yml の並びは見ていない
- 「疑いすぎにも注意する」の段落を診断の末尾に置いた（decide-when-to-quit#dont-switch-too-often への案内。出典は Schulman、根拠：弱）
- 研究名のない言及（2012 年のメタ分析・166 標本・根拠：強）は Sleesman らの出典に基づく。ρ の値は書いていない
[提案]
なし（front matter・用語集・数値への提案はない）。

## wont-rethink-approach/review.md
[メインに判断してほしいこと]
- 診断の並び（散らかっている → 確かめていない）が site.yml の並びかは未確認

## blames-the-tools/write.md
[メインに判断してほしいこと]
- 六つの原因の「安く確かめる順」を site.yml で確かめていない。prevents の並び（見えていない → 散らかっている → 確かめていない）のまま並べ、先頭に「人が同じ操作を自分で実行する」を足した。順が違えば直してほしい。
[提案]
- なし（数値の提案・front matter の変更の提案ともになし）

## blames-the-tools/review.md
[メインに判断してほしいこと]
- 診断の先頭に足した「人が自分で実行する」と、原因の並びが site.yml と合うか（write.md の件を引き継ぐ）。

## parallel-fatigue/write.md
[メインに判断してほしいこと]
- 診断の並びは front matter の prevents → pitfalls の順にした。site.yml の六つの原因の並びとの突き合わせはしていない
- 並列の疲労の数値は、目次の notes（research/21 P7）に従い使わなかった。研究・事例の数値も入れず、持ち主のページ（review-bottlenecks など）に任せた

## deleted-something-important/write.md
[メインに判断してほしいこと]
- 「止める」の項の「復旧のつもりのコマンドが戻せる状態を変えることがある」は、束に出典がない一般的な助言で、「この辞典の推奨」と付けた。不要なら削る
- git の復旧手順（`git restore`・`git reflog`）は束にない一般の知識で、一次資料で確かめていない
[提案]
- front matter の直しの提案はなし

## deleted-something-important/review.md
[メインに判断してほしいこと]
- 「止める」の項の一般的な助言（この辞典の推奨）と git の復旧手順は一次資料未確認。write.md の指摘のまま

## secrets-exposed/write.md
[メインに判断してほしいこと]
- `#diagnosis` の項目 2 に、`git add` を許す規則と `.gitignore` の有無を見る、と書いた。束に出典がなく、一般の実務の知識である。要出典の扱いにするか、削るかを決めてほしい
- `#first-response` の「履歴から消す書き換えはキーの無効化の代わりにならない」も同じく一般の実務の知識で、束に出典はない
- `#prevention` のアプリのタブは「アプリでの同等の設定は未確認」と書いた。アプリ側の材料が束になかったため
[提案]
- なし（数値・用語集・data への提案はない。本文に変わりやすい値は書いていない）

## secrets-exposed/review.md
[メインに判断してほしいこと]
- 項目 3 の出典なしの記述（write.md の指摘と同じ）を要出典にするか削るか

## followed-injected-instructions/write.md
[メインに判断してほしいこと]
- 診断の順を、2 縛っていない → 3 境界がない とした（six-causes の並びの ④ → ⑥）。site.yml の並びを確認していない
- 「実例」の GitHub MCP の事例を（根拠：中）で本文に置いた。企業の一次の報告で、事例を名指しせず「研究者が報告した」と書いた。重すぎるなら削る
[提案]
- 用語集・prh・data・front matter への提案はなし

## followed-injected-instructions/review.md
[メインに判断してほしいこと]
- 指摘 3 の `features: [auto-mode]` は版の表示を消すための回避。雛形の版の既定を、prompt 種では出さない扱いにするか検討してほしい
- write.md の判断（診断の順、GitHub MCP の事例の重さ）は事実の検証の担当に任せる

## wrong-amount-of-approvals/write.md
[メインに判断してほしいこと]
- なし（約束・方針の文は書いていない）
[提案]
- なし（数値は本文に書いていない。承認率などは approval-fatigue に任せた）

## hits-limits-quickly/write.md
[メインに判断してほしいこと]
- 診断の並びは、cause の名前（散らかっている・合っていない）の下に 5 項目を置いた（長さ・常駐・手戻り・モデルと effort）。「六つの原因を site.yml の並びで」は、このページの prevents が 2 つだけなので、手戻り→モデルと effort の順（saving-priorities の優先順位）に合わせた。site.yml の並びとの整合を見てほしい
- 診断の先頭に「長さの上限との取り違え」と、末尾に「枠の側（上限の種類・課金の経路）」を原因の外の項目として足した
- 面のタブ（アプリ・Claude Code・API）は診断の冒頭の「残りと内訳を見る場所」に置いた。API のタブは、束の check-billing-path の要約（従量課金・経路）だけに基づく
[提案]
- なし（用語集・prh・data・front matter への提案はない）。数値の提案もなし（数値は本文に書いていない）

## hits-limits-quickly/review.md
[メインに判断してほしいこと]
- 診断の先頭と末尾に原因の外の項目を足した件（write.md と同じ）。site.yml の並びとの整合を見てほしい
- 項目 3 のアプリ側の「コネクタや拡張を数える」と、API の面の記述は束に根拠が薄い。事実の検証役に回してほしい

## too-slow/write.md
[メインに判断してほしいこと]
- 診断の項目 1（障害・混雑）は六つの原因の外だが、最も安い確認として置いた。要らなければ外す
- 項目 6 は research/22 #21（CHANGELOG）に基づく。docs の sub-agents に記述がないため「2026-11 時点の CHANGELOG」と日付付きで書いた。古くなりやすい
- #prevention の seems-less-capable は節を指さずページを指した
[提案]
- 数値の提案はなし（本文に変わりやすい数値は書いていない。既定の effort は effort-levels#defaults-by-surface へ任せた）
- front matter のほかのキーの直しはなし

## too-slow/review.md
[メインに判断してほしいこと]
- 診断 6（サブエージェントの effort）は CHANGELOG のみが根拠で古くなりやすい。事実の検証役の確認を勧める。

## seems-less-capable/write.md
[メインに判断してほしいこと]
- 診断で「版」を原因の名前に当てはめていない（版・effort・モデルは「合っていない」、会話の量は「散らかっている」と書いた）。catalog の想定と違うなら指示がほしい
- アプリの版の見方は束にないため「未確認」と書いた
[提案]
- 数値の提案なし。既定の effort の値は本文に書かず、`effort-levels#defaults-by-surface` を指した
- front matter の提案なし

## seems-less-capable/review.md
[メインに判断してほしいこと]
- 診断で「版」を原因の名前に当てはめていない点（write.md のとおり）。catalog の想定と違うなら指示がほしい
- 雛形のファイルを直したので、メインの生成で目印の間が更新されるか確かめてほしい（check_page は流して反映済み）

