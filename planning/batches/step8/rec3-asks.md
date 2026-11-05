## agent-sdk-basics/write.md
[メインに判断してほしいこと]
- Web の取得 1 回（claude-code-features）：settingSources の既定は「省くと user・project・local をすべて読む」と文書にある。本文では既定を断定せず「毎回書く」にし、現在の記述は提案の fact にした
- 権限モードの既定と承認の扱いは本文に書かず、headless-basics#permissions を指した。持ち主の側で数値・版なしに現在の挙動を書いてあるかの確認が要る
[提案]
```yaml
frontmatter: []
data:
  - {feature: agent-sdk, key: enforcement, after: "なし（または適切な値）", reason: "feature 型の強制力のバッジのため。Agent SDK は機能全体としては強制力の値が決めにくく、メインが判断する"}
```
- 数値・既定値の提案は facts-proposal.yml
- 用語集：`settingSources` は用語集になく、本文で短く説明した。追加の要否はメインの判断

## agent-sdk-basics/review.md
[メインに判断してほしいこと]
- 強制力のバッジ（指摘 4）：data の agent-sdk に enforcement を入れるか決める
- stage は draft のまま（直したため）

## choosing-a-plan/write.md
[メインに判断してほしいこと]
1. 料金（月額・年払い）の表がない。facts にプランの料金の項目がなく、目印はない id を指すと止まるため置けなかった。他ページ（how-usage-limits-work・before-using-top-model）は「料金を含む表は choosing-a-plan にある」と指す。`facts-proposal.yml` の `plan-prices-individual` を facts に入れたら、#plan-table の fact-table の直後に `fact-table plan-prices-individual` の目印を足す。それまで、本文は料金のページへのリンクで代える
2. 表の Team の行の「—」は、facts 側で null のまま（束の材料に席ごとの値がない）。本文は「—は未確認で『ない』ではない」と書いた。Team の席ごとの上限を facts に足すかは任せる
3. 公式同士の食い違い（Fable の別の週の上限か、通常の週の上限の内側か）は before-using-top-model が持つ。このページは引かれ方を before-using-top-model#which-limit に任せ、表の「最上位のモデルの別の週の上限」列はそのまま出る。列の見直しが入れば、このページの表も変わる
4. Ultra の量が旧 Max 20x と同じかは断定していない（research/22 #44）。「ネットに同じだという説明がある」と匿名で書いた。この書き方でよいか
[提案]
`facts-proposal.yml` を参照。要点：`plan-prices-individual`（個人向けの月額・払い方。Pro と Free は料金のページ 2026-10-29 の記録のみ）、任意で `claude-code-in-free-plan`。front matter は related に saving-priorities を足す提案（本文からは指していない）。用語集・prh への提案はなし。

## choosing-a-plan/review.md
[メインに判断してほしいこと]
- 段階は draft のまま（直したため）
- 表の Team 行のセルの文言（data の `usage-limit-types-by-plan`）を、読者向けの「未確認」などに直す提案。料金の facts（`plan-prices-individual`）を入れたら fact-table の目印を足す

## claude-code-surfaces/write.md
[メインに判断してほしいこと]
- 表の「Desktop アプリの Claude Code」の行が、このページ自身へのリンクになる（data の page がこのページのため）。自己リンクのままでよいか
- 表の行は 4 機能で、ターミナルの行がない。ターミナルの CLI は基準として本文で触れた
[提案]
- なし（数値・front matter の提案はない）

## claude-code-surfaces/review.md
[メインに判断してほしいこと]
- 表が比べる表として弱い（成熟度などが全行共通で省かれ、入った版も 1 件だけ）。data の features に属性（例：動く場所・読む設定）を足すか、表を出さない代わりに本文の表にするかを決めてほしい
- 表の「Desktop アプリの Claude Code」が自己リンクになる点（write.md と同じ）
- stage は draft のまま（指摘 1 を直したため）

## xml-tags/write.md
[メインに判断してほしいこと]
- 外から貼った文章を包む節は、公式の案内（Opus 5.5 向け）の「ランダム ID のタグで包み、中の指示に従わないよう書く」に沿った。ID を使う理由は公式の文面にないので、本文で（推論・実践例なし）と断った
- 本文の「最新世代のモデル向けの公式の案内」は、モデル名を書かず出典のリンクの題名に任せた（名前は変わりやすいため）
[提案]
- 数値・用語集・prh・front matter の提案はなし

## xml-tags/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。直しの差分の確認は別の担当が要る
- write.md が「未実行」と書いた textlint の指摘は、今回の検査で 0 になっていた

## ask-claude-code/write.md
[メインに判断してほしいこと]
- 章立て：目次の sections は 2 つだけだったが、概念型の必ず持つものを満たすため 3 節を足した。多すぎるなら `#misconceptions` を落とせる
- `/powerup` の記述は 01 の調査資料（「実演は `/powerup`」）の範囲に留めた。動作の中身は書いていない
[提案]
```yaml
frontmatter: []
```

- 用語集：「見せる」「見えていない」を本文で短く定義した（`#what-it-helps`）。用語集に定義があれば、そちらに合わせて本文を直してよい
- 本文は hooks を「フック」と書いた（prh の指摘）。signs の goal は「hooks の書き方などを」のままで、これは front matter なので直していない（`{id: ask-claude-code, key: signs, ...}` を直すなら「フック」への統一をメインが判断）

## ask-claude-code/review.md
[メインに判断してほしいこと]
- signs の goal「hooks の書き方などを」は本文の「フック」表記と揺れる（write.md の提案どおり）。判断はメイン

## command-cheatsheet/write.md
[メインに判断してほしいこと]
1. コマンド→判断のページの表は、材料の束の方針「生成のページ」に反して手書きになった。gen に、コマンドと行き先のページを持つ表の目印がないため。案：data/facts.yml の features か新しい項目にコマンドの行（コマンド・一言・page・anchor）を持たせ、`command-table` の目印を足す。足すまでは、手書きの表を暫定として残す
2. 手書きの表の「何ができるか」の一言は、束の材料（公式の表の抜粋・行き先のページの要約）の範囲で書いた。`/skills`・`/hooks`・`/mcp`・`/plugin` の一言は名前と行き先の題名から書いたもので、公式の表で一言ずつは確かめていない
3. 台帳の行にない旧名 `/review`・`/allowed-tools` を names の目印で載せた。台帳に行を足すかは任せる（足すなら ledger の提案）
[提案]
- 目印 `command-table` の新設（上の 1）
- `/review`・`/allowed-tools` の台帳の行の追加（任意。上の 3）

## command-cheatsheet/review.md
[メインに判断してほしいこと]
- write.md の判断事項 1（`command-table` 目印の新設）は未解決のまま。

## choosing-mcp-servers/write.md
[メインに判断してほしいこと]
- 第三者サーバーの名前の表（`#examples`）：成熟度は「未確認」、確認日は出典の記事の日付（2026-06-29）と本文に書いた。DR-17 は「成熟度と確認日を添える」とあるが、各サーバーを確かめていないため。名前の表を残すか、確かめる担当を付けるかを決めてほしい
- ページの題材が第三者の名前を出す（推薦ではない旨を本文に明記）。公開の約束や方針の文は置いていない
[提案]
- front matter、用語集、data への提案はない

## choosing-mcp-servers/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 例の表の成熟度の扱い（write.md のとおり）

## disclosure-and-provenance/write.md
[メインに判断してほしいこと]
- 節の題名「開示・相談・出所・意図の四つの観点」は textlint の「四つ」の対象になりうる。今回の検査では出なかった。出る場合は題名を「4 つの観点」にする提案（anchor は変えない）
- 文部科学省の通知の記述は、束の材料（11 第2節 p56#108）に基づく。通知の本文は開いていない。「今の版を確かめる」と書いた。版（年）は本文に書いていない
[提案]
数値の提案はなし。front matter の提案もなし（prevents・pitfalls が空であることは目次側の判断に任せる）。

## disclosure-and-provenance/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しを別の担当が確かめていないため）

## progress-logs-for-long-jobs/write.md
[メインに判断してほしいこと]
- 「ログが大きすぎて監視できなかった例」の（根拠：中）は、目次の materials（11 の p34#168）の評価に拠る。公開の出典がなく、sources に載せていない。出典を足すか、印を（根拠：弱）にするか
- hook-monitor-min-version（facts、status 未確認）を目印で使った。確認済みにするか、本文を直すか
[提案]
- 数値の提案：facts-proposal.yml（Monitor の見張りの期限 3 件と、制限環境での最低の版）。本文は数字を書かず、目印も置いていない。取り込んだら #steps の「見張りには期限があり」の所に目印を置く
- 用語集：Monitor（道具）の定義が本文に短くあるだけ。用語の追加はしていない

## progress-logs-for-long-jobs/review.md
[メインに判断してほしいこと]
- 雛形 watch-request の「errors が前の行より増えた行」を、絞り方が分かる書き方にするか（5）
- hook-monitor-min-version は status 未確認（write.md の件）

## choosing-automation/write.md
[メインに判断してほしいこと]
- 軸の表の「Desktop の予定のタスク」の課金の経路を「未確認」にした。束と data にサブスクリプションの要否の記述が曖昧だったため
- 軸の表は、動く場所・触れられるもの・課金の経路を手書きにした（data の属性ではなく、プランの名前も数値も書いていない）。道具で作れる属性に直せるなら、data への属性の追加を検討してほしい
[提案]
- 数値の提案なし
- front matter の追加なし（sections は載せた 5 節のみ）

## choosing-automation/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しを入れたため）
- 指摘 3 のバッククォートを一括で直すか

## postmortems/write.md
[メインに判断してほしいこと]
- 出典 collins-premortem は本文を取得せず、調査資料の要約に拠る（sources.d の note に明記）。「30% は理由の数」の主張は、メインが原典か本文で確かめてほしい
- SRE Workbook は 1 回取得して確かめた（誰がでなく何が許したか、単一のオーナーと測れる完了状態、レビュー）。「別のメンバーが記録を確かめる」はチェックリストとレビューの記述を根拠にしたやや広い読み
- 目次の備考にある SSW Rules の insights 機能（過去のセッション分析）は、一次資料を開いていないので書かなかった
- 方針・約束の文は足していない（カード §13）
[提案]
- なし（用語集・prh・data・front matter の直しは出さない）
- 数値の提案もなし。ELEPHANT の 72% 対 22%・50 ポイントは、研究の名・年・対象を添えて本文に書いた。「本番の 1 か月前」は出典のない例と明記した

## postmortems/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。最後の直しの検査結果は一括検査で確かめてほしい
- 関連の record-decisions と decide-when-to-quit は本文から指していない。必要なら追加を検討

## tool-use-loop/write.md
[メインに判断してほしいこと]
- 表示の確認：#client-and-server の compare 表（成熟度 入った版）は、2 機能が同じページを指すため、表の機能名のリンクが自分のページへの自己リンクになる。許容か、表を外すかを判断してほしい
[提案]
- 数値・既定値（facts-proposal.yml）：tool_choice の既定値（auto）と、強制が使えないモデルの表。本文は両方とも値を書かず、「auto のとき」「モデルによっては」の形にした。目印を置く場所は used_in に書いた
- 用語集：「システムプロンプト」を prh が要求する（system prompt は書けない）ので本文ではそれに従った。tool_use・tool_result・tool runner を用語として足すかは判断してほしい（本文では原文のままバッククォートか平文）

## tool-use-loop/review.md
[メインに判断してほしいこと]
- compare 表の自己リンクを許容するか、表を外すか（write.md と同じ）
- 直したので stage は draft のまま

## long-running-agent-context/write.md
[メインに判断してほしいこと]
- 図は SVG 1 枚（代替テキストあり）。目次の visual の案（static）に沿った
- 「迷う候補」の判断例は、公式の説明（memory tool と compaction の併用の推奨）に沿った筆者の例。研究や実践例の根拠ではない
[提案]
- 用語集：path traversal（保存先のパスが許す範囲の外へ出る攻撃）を短く定義して追加する案。本文では説明なしで使った
- front matter の提案：なし

## long-running-agent-context/review.md
[メインに判断してほしいこと]
- 用語集に path traversal を足すか（執筆の提案のまま。本文には短い定義を入れた）
- 直したので stage は draft のまま

## commit-and-comment-language/write.md
[メインに判断してほしいこと]
- 特になし。公開の約束・方針の文は書いていない
[提案]
- 用語集・prh・data への提案：なし
- front matter の提案：なし

## commit-and-comment-language/review.md
[メインに判断してほしいこと]
- 特になし。直したため stage は draft のまま（別の担当が直しの差分を確かめるまで）

## write-docs/write.md
[メインに判断してほしいこと]
- なし（公開の約束・方針に関わる文は入れていない）
[提案]
- なし（front matter・用語集・数値の提案はない）

## paved-roads/write.md
[メインに判断してほしいこと]
- 出典 `dora-2025-report`（新規）の `dora.dev` を `data/sources.yml` のドメイン一覧へ載せるか。sources.d に `domains` を書いたが、スキーマが sources.d で受けるかは check_page が通ったので足りているはず。メインの生成で確認してほしい
- メルカリの実例（`#defaults-over-attention`）は @IT の報道に基づく肯定的な文脈。束の「補足」にある `--dangerously-skip-permissions` の禁止と作業時間の減少は、一次で確かめられないとあるので書いていない
[提案]
```yaml
frontmatter: []
```

数値の提案はなし（本文に変わりやすい値を書いていない。DORA は割合・標本の大きさを書いていない）。用語集の追加提案もなし。

## paved-roads/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。write.md にあった `dora.dev` の domains の件は check_page が通っている

## record-decisions/write.md
[メインに判断してほしいこと]
- sources が空。束に出典がなく、材料は調査資料 11 の「根拠：中」の 2 行だけ。ADR の由来や公式の説明には触れず、手順は「この辞典の推奨」の形で書いた。確認の節の基準には（根拠：弱）を付けた。出典を足すなら別途一次資料が要る
- 内容が approx 「新メンバー役が CLAUDE.md と ADR だけで作業できるか」を確かめの基準にした（材料 6.2 に沿う）。調査資料側の「根拠：中」を弱にしたのは、出典が束になく確認できないため
- 面のタブ（アプリ／Claude Code）は置かなかった。手段が面で分かれる所がなく、アプリ側の動作は確認できないため
[提案]
- なし（用語集・prh・data への提案なし）

## record-decisions/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。sources が空（write.md の判断事項のとおり）

## format-cheatsheet/write.md
[メインに判断してほしいこと]
- 規則の列：方針 A4（類型だけを数値ファイルから出す）に対し、`contest-ai-rules` の表の個別セルを目印で埋め込む仕組みがない。そのため類型は書かず、「規則で確かめること」の列と、competition-rules#rules-by-type へのリンクにした。セル単位の目印（例：`fact-cell`）が欲しいか
- 「一つの表」は、読みやすさ（スマホ）のため、早見表を 2 枚（AI・人・評価器／規則・当日の注意）に分けた
- `overview` 節を足した。不要なら外してよい
- 費用の上限の一文（`#why-formats-differ`）は、費用の数値を書かず一般論にした。数値は ai-in-contests-today が持つ想定
[提案]
```yaml
frontmatter:
  - {id: format-cheatsheet, key: sections, before: [7 節], after: [overview を先頭に追加した 9 節], reason: "早見表を 1 節で先に引けるようにした"}
```

## format-cheatsheet/review.md
[メインに判断してほしいこと]
- 手本 kyopro-atlas の節（atcoder-system の ai-rules・practice-method）への実際のリンクの形。

## running-contest-experiments/write.md
[メインに判断してほしいこと]
- 資料にした 2 つのドメインが noai（threadreaderapp.com・chessprogramming.org）なので、Psyho の「2,000〜5,000 ケース」と SPRT の出典は引かなかった。前者は名指しせず「上位者の経験則」（根拠：弱）とし、出典の id は付けていない。後者は「境界を事前に決めた逐次の検定」と一言だけ書いた
- Halite III で 3 位の参加者の事例は、recursive.cc を `check_noai.py` で 2 回確かめたが「取得できない: timed out」で、確かめ済みにできなかったので、事例は載せず、対戦型への当てはめは（類推）の一般論にした。確かめが通れば、事例と出典を足せる
[提案]
```yaml
frontmatter: []
```

数値の提案はなし（本文の数値は、研究・解説の時点の記録と、二項分布の計算値。facts に置く変わりやすい値は書いていない）。

## running-contest-experiments/review.md
[メインに判断してほしいこと]
- 直しの差分を別の担当が確かめていないため、stage は draft のまま
- 追加した式（(1.96 × s / d)²）は自分で導いたもので、他の担当は未確認

## competition-day-operations/write.md
[メインに判断してほしいこと]
- 書かなかったもの：長期 AHC の部門選択の期限の話（未確認 A-3）、Universal Cup のプロンプトインジェクション禁止（工程2で未確認）、2026-08-16 の障害の日付と長さ（未確認。出典の bleepingcomputer.com は noai の記録）、「最も安い保険」（「保険として有効」にとどめた）、本番 1 か月前などの数値（「出典のない例」と文で触れただけ）、模擬本番の演習
- ISUCON13 の初参加チームの準備（3.5 時間）と DEF CON 33 の講演は、sources.yml に id がないため引かなかった。使うなら出典 id の追加が要る
- 「終了の 1〜2 時間前」の数値は本文に書かず、凍結の時刻は前日に決める形にした
[提案]
```yaml
frontmatter: []
```
- 用語集：「評価器」（点や正しさを提出の前に自分で測る道具）を本文で短く定義した。用語集に既にあるか確認を
- facts の提案はなし（変わりやすい値は本文に書いていない。CTF の順位は研究の時点の記録として、名・年・対象を添えて書いた）

## competition-day-operations/review.md
[メインに判断してほしいこと]
- 指摘 2 の文は、出典を足すか削るかを判断してほしい
- stage は直したので draft のまま

## recover-lost-work/write.md
[メインに判断してほしいこと]
- 方針の文は足していない。保持期間を延ばす助言は、秘密が長く残る点と並べて書いた（判断例 retention）。承認が要る文には当たらないと考えた
[提案]
- facts は新規なし。使った既存の id：local-transcript-cleanup-days・checkpoint-retention-days・key-transcript-and-background（status 未確認のまま）
- data/facts.yml の sessions 機能の note に、「JSONL の記録に圧縮の前のやり取りがどこまで残るか」は未確認と足す案（本文では確かめていないと書いた）

## recover-lost-work/review.md
[メインに判断してほしいこと]
- fact key-transcript-and-background の status が未確認で、本文に「未確認」だけが出る。確認済みにするか、本文を「キーは公式の対話モードの文書で見る」に変えるかの判断
- 直したので stage は draft のまま

## is-the-task-ai-suited/write.md
[メインに判断してほしいこと]
- 判断例の「ログの集計と障害の原因調査」は、束の材料にない仮想の場面（材料は大会の事例）。業務の作業にも使える旨（p12#63）に沿って作った。不要なら差し替えてよい
[提案]
- なし（変わりやすい値は本文に書いていない。事例の数値〔AHC058 の局所評価、ISUCON の約 1 時間・3〜4 時間、Airbnb CTF の 60 分・30 問中 13 問・最終 15 問 39 位、Battlecode 2026 のローカル勝率 85% 超〕は研究・報告の時点の固定の記録として、出典 id を添えて書いた）

## is-the-task-ai-suited/review.md
[メインに判断してほしいこと]
- 判断例の仮想の場面を残すか（write.md と同じ）

## pairing-and-delegating/write.md
[メインに判断してほしいこと]
- 伴走と委託の 2 分類の出どころは、調査資料 11（p34#143、根拠：中）の実務家の整理だけ。出典の id が束にないので sources は空にし、本文では（根拠：弱）の印を付けて個人名は出していない。出典を足す場合は、元の投稿の登録（check_noai.py での確認を含む）をお願いしたい
- 表の「この辞典の level」の行（伴走＝任せる、委託＝回す）は requirements §3.3 と目次の level_evidence から書いた対応づけ
[提案]
- 用語集：「伴走」「委託」を追加（伴走＝人が途中を見て舵を取る進め方、委託＝完了条件を渡して任せ後で確かめる進め方）。aliases の「丸投げ」は、本文では「完了条件も確かめ方も渡さない任せ方」として別に定義した

```yaml
glossary:
  - {term: 伴走, definition: "人が途中を見ながら、一歩ずつ方向を直して進める協業の形", page: pairing-and-delegating}
  - {term: 委託, definition: "完了条件を渡して任せ、戻ってきた結果を後で確かめる協業の形", page: pairing-and-delegating}
```

## pairing-and-delegating/review.md
[メインに判断してほしいこと]
- write.md のとおり、sources が空（本文の根拠は（根拠：弱）の印）。出典の登録は作者側の判断
- write.md によると、執筆の直しの一部が Bash で行われた（手順からのずれ）。内容への影響は見つからなかった

## github-actions-with-claude/write.md
[メインに判断してほしいこと]
- 雛形の扱い：カード §10 は「GitHub Actions は試せない雛形なので載せず、条件と概念だけ」、brief §3 と目次は「雛形は載せる・最小権限の workflow を載せる」。目次と brief を優先して 2 つ載せた（折りたたみ・未確認の旨は道具が書く）。載せない方針なら、#templates の節を外し、expect を消す
- minimal-workflow の `permissions` は公式の例のとおり（contents は write）。目次の題は「最小権限」だが、Action が既定で GitHub App として認証するため、`permissions` を read に絞った効果は確かめていない。雛形の題は「最小権限の workflow（@claude に応える）」のまま。題を直すかどうか
- 要点の「強制力」の行は、`permission-modes/enforcement` のような目印を使わず文で書いた。github-actions の機能に強制力の属性を足す提案をするかどうか
[提案]
```yaml
frontmatter: []
```

- 用語集：なし。数値の提案：なし（本文に変わりやすい値の手書きはない。例の値は雛形のコメントに「例」と明記）
- 機能 github-actions の enforcement を data に足す案（値は鍵・お願いの混在のため、メインの判断）

## github-actions-with-claude/review.md
[メインに判断してほしいこと]
- write.md の 3 点（雛形を載せる方針、題の「最小権限」、強制力の属性）は未判断のまま

## stateless-messages-api/write.md
[メインに判断してほしいこと]
- message threads のスレッドの寿命（最後の要求から切れるまで、最後に使ってから消えるまで）は、data の facts に該当の id がない。本文は数字を書かず「公式の文書で確かめる」とした。下の提案で fact を足してもらえれば、#message-threads の 1 つ目の項目に目印を置ける
- 判断例の「選んだもの」（要約で履歴を短くする）は、このページの推奨ではなく状況を限った例である。違和感があれば直す
- ZDR と HIPAA の対象外という記述は、research/22 #40（Platform のリリースノート 11-02）と facts の note による。HIPAA は facts の note にはなく、research/22 だけが根拠。公式の message threads の文書で再確認していない
[提案]
```yaml
proposals:
  - fact: {id: message-threads-lifetime, title: message threads のスレッドの寿命（最後の要求から切れるまでと、最後に使ってから消えるまで）, value: "最後の要求から 5 分で切れ、最後に使ってから 1 時間以内に消える", sources: [api-docs-message-threads, api-docs-messages], checked: 2026-11-05, status: 確認済み}
    used_in: [stateless-messages-api#message-threads]
```
- 根拠：working-with-messages の文書の「A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use」（2026-11-05 に取得）と research/22 #40
- 用語集：「stateless（状態を持たない）」は本文で短く定義した。用語集にないなら追加を検討してほしい

## stateless-messages-api/review.md
[メインに判断してほしいこと]
- write.md の提案（message-threads-lifetime の fact）の反映。反映後、#message-threads の 1 つ目の項目に目印を置ける
- ZDR の言い換え「ゼロデータ保持の契約」と「HIPAA 対応の利用」は事実の検証をしていない。用語集に ZDR を足すか検討してほしい

## refactor-and-migrate/write.md
[メインに判断してほしいこと]
- 雛形 `goal-stop-conditions` の末尾 `or stop after <上限のターン数> turns` は束の 11 §4 #23 の構文を写した。構文と判定の仕様は版依存なので、確認日と版は本文の compare 表（goal の入った版・確認日）と goal-until-done への誘導で担保した。構文自体の fact を数値ファイルに置くか、判断を願う
- compare 表は成熟度が全行共通で表から外れ、「すべて共通」の行に出る。recipe に compare の目印を置くのが型の方針に合うかを確認してほしい（tracks の3機能の版と確認日を出すために使った）
[提案]
```yaml
frontmatter: []
```

- 用語集・prh・data への提案はなし
- 補足：`#goal-stop-conditions` は「止まる条件と上限を先に決める」「`-p` で回すときはターン数と費用の上限を指定する」と書いた。値は書いていない（束の ralph-loops の how_to_find が根拠）

## refactor-and-migrate/review.md
[メインに判断してほしいこと]
- write.md の 2 件（/goal 構文の fact 化、recipe に compare を置く是非）は未解決のまま引き継ぐ

## create-and-review-prs/write.md
[メインに判断してほしいこと]
- 公開の約束や方針の文は入れていない。pr-template の「AI の使用」の欄は、開示の求め方がチームや場で違うため、disclosure-and-provenance#four-points を指すだけにした
- 目次の visual は「なし」なので図は置いていない
[提案]
- 提案はなし（front matter・用語集・data への変更案なし）。数値の提案も、変わりやすい値を本文に書いていないため、なし

## create-and-review-prs/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため、直しの差分を別の担当が確かめていない）
- catalog の備考にある draft PR は束の材料に根拠がなく、本文にない。必要なら材料を足して執筆し直す

## prompt-patterns/write.md
[メインに判断してほしいこと]
- analysis-request.md の Write が止められた。メインが最後の返答の中身から作る必要がある
- 型の骨の「別のセッションに下書きを貼る」「基準を Claude 任せにすると下書きに合わせやすい」は束の材料にない実践上の助言。根拠の印は付けていない。必要なら弱める

## prompt-patterns/review.md
[メインに判断してほしいこと]
- analysis-request.md を作る（案は最後の返答）。作ったら gen_site --page で埋める
- stage は draft のまま（直しあり）

## side-questions-btw/write.md
[メインに判断してほしいこと]
- 数値ファイルの btw に `enforcement` がない。要点の「強制力」は「なし」と手で書いた（insights-and-usage-review と同じ流儀）。データに足すなら下の提案を参照
[提案]
```yaml
proposals:
  - fact: {id: btw/enforcement, title: /btw の強制力, value: なし, sources: [cc-docs-interactive-mode], checked: 2026-11-05, status: 確認済み}
    used_in: [side-questions-btw#when]
```
（data/facts.yml の features の btw に `enforcement: なし` を足す案。道具の形に合わせて直してください）

## side-questions-btw/review.md
[メインに判断してほしいこと]
- write.md の提案（data の btw に enforcement を足す）の判断。それまで要点の強制力は手書き
- 直したため stage は draft のまま

## cloud-schedules/write.md
[メインに判断してほしいこと]
1. 強制力：data の features の scheduled-tasks に enforcement 属性がない。冒頭は手書きで「起動を担うだけ。依頼文の指示はお願い、止められるのは権限の側（保護ルール・ネットワーク・連携先）」とした。属性を足すなら値は「お願い」（依頼文）と「鍵」（保護ルール・環境）の混在で、1 つに決めにくい
2. 3 節以外（success-and-results・templates・pitfalls・compare・outdated）を sections に足した。anchor は既存の 2 つを変えていない
3. `#compare` の `compare` の目印は、scheduled-tasks と cloud-sessions の属性の表になる。比較として弱ければ外してよい
[提案]
```yaml
proposals:
  - fact: {id: scheduled-tasks-min-interval, title: クラウドの定期タスクの最小の間隔（cron の 1 時間より短い間隔は拒否）, value: 1 時間, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#triggers]
  - fact: {id: scheduled-tasks-hourly-cap, title: 定期タスクの実行・GitHub イベントの 1 時間あたりの上限（タスクごと・アカウントごと）, value: 公式の usage and limits の節で確認が要る（値は未取得）, sources: [cc-docs-routines], checked: 2026-11-05, status: 要確認}
    used_in: [cloud-schedules#triggers, cloud-schedules#pitfalls]
  - fact: {id: scheduled-tasks-github-lapse, title: GitHub の接続が切れたとき実行を飛ばす期間と、その後に止まるまでの期間, value: 72 時間, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#pitfalls]
  - fact: {id: scheduled-tasks-schedule-warning-version, title: /schedule が頼んでいない連携先に警告を出すようになった版, value: 2.1.317, sources: [cc-changelog], checked: 2026-11-04, status: 確認済み（research/22 #27）}
    used_in: [cloud-schedules#least-privilege]
  - fact: {id: scheduled-tasks-run-history-question-version, title: /schedule で実行の履歴を尋ねられる版（GitHub の起動を CLI から足せる版は 2.1.225）, value: 2.1.227, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#success-and-results]
  - fact: {id: scheduled-tasks-plans, title: クラウドの定期タスクが使えるプラン, value: Pro・Max・Ultra・Team・Enterprise, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#triggers]
frontmatter: []
```

数値は本文に書いていない（すべて「公式で確かめる」の形）。上の提案が通れば、目印に置き換えられる。

## cloud-schedules/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。強制力の手書きの扱いは write.md 1 のとおり
- 警告 4 件が残る。必要なら文を分ける

## make-slides/write.md
[メインに判断してほしいこと]
- 手順 6 で「2 割」を数にせず、目安の言い方で割合ではないと書いた（目次の notes に従った）。
- Marp は Claude Code タブで例として名前を出すだけにした。第三者ツールの成熟度と確認日は付けておらず、本文に「確かめていない」と書いた。
[提案]
- 用語集・prh・data・front matter の提案はなし。

## make-slides/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直しの差分を別の担当が確かめていないため）。
- 周辺製品とフロントエンドのデザインのページは未公開で「準備中」表示。公開後に表示が変わる。

## artifacts-as-apps/write.md
[メインに判断してほしいこと]
- 面のタブを置いていない（surfaces が app のみ。Claude Code と API は「未確認」と `#pitfalls` に書いた）
- 「Claude を呼ぶ処理は答えが 1 通りに決まらない部分だけに使う」は設計上の推論として `（推論・実践例なし）` を付けた
[提案]
facts-proposal.yml に数値の提案（保存の上限・使えるプラン）を書いた。本文には数値もプラン名も書いていない。目印を置く場所は `artifacts-as-apps#runtime`。

## artifacts-as-apps/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。57 行目の警告を直すなら、括弧の説明を 2 文に分けるとよい。

## bare-mode/write.md
[メインに判断してほしいこと]
- 要点の「強制力」：data に enforcement がないため値の目印を使えなかった。起動時に読み込みを止めるので「鍵」に近いが、道具の許可は絞らない。data への追加の可否を決めてほしい（提案参照）
- 雛形：カード §10 の「API キーが要る --bare は載せない」に従い、catalog の案「自分の設定を混ぜない claude -p の起動例」を、API キー不要の組み合わせ（`CLAUDE_CONFIG_DIR`・`--setting-sources project,local`・`--strict-mcp-config`、research/28 §3.4）にした。この組み合わせは文書から組んだ案で、動かしていない
- ページ内で、related にない `isolate-with-safe-mode` と `checking-unattended-runs` を link で指した（check_page は通った）。related への追加を提案する
[提案]
```yaml
frontmatter:
  - {id: bare-mode, key: related, before: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, github-actions-with-claude, batch-and-p-loops, choosing-automation], after: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, isolate-with-safe-mode, checking-unattended-runs, github-actions-with-claude, batch-and-p-loops, choosing-automation], reason: "本文で比べる相手・確かめ方として指している"}
proposals:
  - fact: {id: bare-mode-default-plan, title: "-p の既定を --bare にする予定の有無", value: "公式の headless の文書は、--bare を将来 -p の既定にすると書く（予定。入る版は未定）", sources: [cc-docs-headless], checked: 2026-11-05, status: 確認済み}
    used_in: [bare-mode#pitfalls]
  - fact: {id: setting-sources-leak-fix-version, title: "--setting-sources で外した設定が漏れる不具合の修正の版", value: "v2.1.314（research/22 #6。CHANGELOG の再確認が要る）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [bare-mode#pitfalls]
  - fact: {id: bare-mode-partial-limits-before, title: "--bare の MCP・システムリマインダー・バックグラウンドの制限が完全になった版", value: "v2.1.286 より前は一部だけ（headless の文書）", sources: [cc-docs-headless], checked: 2026-11-05, status: 確認済み}
    used_in: [bare-mode#what-is-skipped]
features:
  - 提案：data/facts.yml の bare-mode の項目に enforcement（候補：鍵。読み込みの時期は「起動時」）を足す
```
本文は、これらの数字・予定がなくても読める形にした。目印は置いていない（承認後に置く）。

## bare-mode/review.md
[メインに判断してほしいこと]
- write.md の提案（強制力の data 追加、related への 2 ページ追加、数値の提案）の反映。強制力の要点の説明は、data 追加後に目印へ置き換える
- 直したので stage は draft のまま（別の担当による直しの確認が要る）

## prompt-caching-in-practice/write.md
[メインに判断してほしいこと]
- 変わりやすい値（寿命・倍率・最小の長さ・区切りの数の上限）は本文に書かず、数字なしで読める形にした。facts に置いて目印で指すなら、facts-proposal.yml を取り込み、`#pitfalls` `#breakpoints` に目印を足してもらいたい。
- 比例則の警告（level が仕組みにする）が 1 件残る。目次の備考にあるとおり、任せる幅を広げる内容ではないので誤検出と考える。
[提案]
- facts：`facts-proposal.yml` の 4 件（status は要確認。確認日は調査資料 02 §5-2 の 2026-10-29 のまま）。
- front matter の提案：なし。

## prompt-caching-in-practice/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）。facts-proposal.yml の取り込みは write.md のとおり。

## ai-in-contests-today/write.md
[メインに判断してほしいこと]
- 成績の数値（804 人・約 1,300 ドル・呼び出し回数・PicoCTF の順位など）は、目次の notes に従い本文に書かず facts-proposal.yml に提案した。本文は ALE-Bench の論文の結果（Gemini 2.5 Pro、o4-mini-high）と、Anthropic の CTF の 0 問・上位 3% を「固定の記録」として手で書いた（card §7）。fact の目印へ寄せるかを判断してほしい
- 出典のない成績は載せなかった：AWTF 2025（Psyho 対 OpenAI）、ICPC 2025 の OpenAI の 12 問、IOI 2025 の 6 位相当、AWTF 2026 Algorithm の 5 問、MLE-bench の約 64%、BSidesSF 2026・SECCON CTF 14・DARPA AIxCC・CSAW・Kaggle 5 位の事例、HTB の 22 位の推定。束に出典の url がなく、一次資料を確かめていない。載せるなら出典の追加が要る
- AWTF 2026 Heuristic の出典は Understanding AI と OfficeChai（二次の報道）だが、本文の表では出典を直接リンクにしておらず、sources 一覧（参考）で示す。順位表（CPHOF）や ALGO ARTIS の X は sources に未登録のため使っていない
[提案]
- front matter の直しの提案はなし
- data への提案は facts-proposal.yml（4 件）
- 用語集・prh への提案：「アブレーション」を本文で短く定義して使った（用語集にあれば合わせる）

## ai-in-contests-today/review.md
[メインに判断してほしいこと]
- 直しがあったので stage は draft のまま（別の担当の再確認が要る）

## asking-for-reasoning/write.md
[メインに判断してほしいこと]
- 課金の扱い（出力の前に止まっても課金される分類）と、reasoning_extraction が足された日・対象モデルは、本文に手で書かず facts-proposal.yml に提案した。承認後に fact の目印へ差し替えたい（今の本文は課金の中身に触れず「Refusals の文書で確かめる」）
- アプリでの思考の要約の表示方法は束に材料がなく、「未確認」と書いた
[提案]
- facts-proposal.yml（2 件）：reasoning-extraction-billing、reasoning-extraction-since。used_in は asking-for-reasoning#refusal

## asking-for-reasoning/review.md
[メインに判断してほしいこと]
- 直したため stage は draft のまま。課金の扱いと追加日は facts-proposal.yml の承認後に fact の目印へ

## agents-md/write.md
[メインに判断してほしいこと]
- 台帳（outdated-advice）に AGENTS.md の回避策（CLAUDE.md に「読め」と書く・SessionStart フックで出す等）の行がない。#outdated は台帳を指さず本文で書いた。台帳への行の追加を検討してほしい
- 初期の動き（CLAUDE.md があると AGENTS.md を読まない）は既定の動作なので、提案の fact（agents-md-instruction-files-default）を足した後に目印へ置き換えるか決めてほしい。今は目印なしの文で、設定値の名前は本文に出していない（雛形の JSON と判断例だけ）
- 比例則の警告（level 任せる で verify 等のページが前提・関連にない）は、目次の notes どおり対象外。残した
[提案]
- data/facts.yml：facts-proposal.yml を参照（agents-md-direct-read-min-version・agents-md-instruction-files-default・agents-md-plugin-id-rename）
- 用語集：Project instructions（画面の名前）は prh が「プロジェクトの指示」を求める（same-names-across-surfaces）。本文は「読み込みの設定」と言い換えた。画面の名前を確かめたうえで prh か用語集に例外を足すか決めてほしい
- 台帳：上のとおり

## agents-md/review.md
[メインに判断してほしいこと]
- write.md の項目（台帳に AGENTS.md の回避策の行を足すか、初期の動きを fact にするか、Project instructions の表記の例外）を引き継ぐ

## rate-limits-and-errors/write.md
[メインに判断してほしいこと]
- 追加した節 `cause`・`misconceptions` を sections に入れたのでよいか。prevents が空のため、原因は名指さなかった
- 再試行の「間隔にばらつきを足す」は公式にない定石で、「この辞典の推奨」と明記した。残してよいか
- 「再試行の層を重ねない（回数が掛け合わさる）」は（推論・実践例なし）の印を付けた
[提案]
- 数値の提案は `facts-proposal.yml`（SDK の自動の再試行の既定、Claude Code の自動の再試行の既定）。本文は数字なしで読める形にしてあり、承認後に目印を `#retry`・`#in-claude-code` へ置ける
- front matter の提案：なし

## rate-limits-and-errors/review.md
[メインに判断してほしいこと]
- stage は draft のまま（直したため）
- 指摘 3 の「ゲートウェイ」の説明が要るか

## character-encodings/write.md
[メインに判断してほしいこと]
- 版ごとの挙動（Edit・Write が非 UTF-8 を拒むようになった版）は本文に版を書かず、「2026-11-03 に変更の記録で確かめた」と日付で書いた。下の提案の fact が通れば、`#claude-code` の第 1 段落に目印を置いてほしい
[提案]
```yaml
proposals:
  - fact: {id: edit-refuses-non-utf8-since, title: Edit が UTF-8 でないファイルの編集を拒むようになった版, value: "2.1.296", sources: [cc-changelog], checked: 2026-11-03, status: confirmed}
    used_in: [character-encodings#claude-code]
  - fact: {id: write-refuses-non-utf8-since, title: Write が Shift-JIS などを黙って UTF-8 に変えず拒むようになった版, value: "2.1.299", sources: [cc-changelog], checked: 2026-11-03, status: confirmed}
    used_in: [character-encodings#claude-code]
```
- 値は束の research/27 #19 の写し。CHANGELOG 本体は読み直していない

## character-encodings/review.md
[メインに判断してほしいこと]
- 直したので stage は draft のまま。生成時に警告 2 の解消を確かめてほしい
- write.md の提案の fact（2.1.296・2.1.299）は未反映。本文に目印は置いていない

## build-observation-tools/write.md
[メインに判断してほしいこと]
- 出典がない：束の出典の一覧が空で、材料（調査 10 第6章・11）の根拠は threadreaderapp・speakerdeck など check_noai.py 未確認のドメイン。本文の「上位者の考察の手順は共通（根拠：中）」は出典 id なしで置いた。出典を足すなら、ドメインの確認と sources.d の追加が要る
- 失敗のときの振り分け先に症状のページを置いていない（束に routes がなく、指せる症状の節がなかった）
[提案]
- 用語集・prh・data・front matter の提案はない

## build-observation-tools/review.md
[メインに判断してほしいこと]
- 指摘は直したので stage は draft のまま
- write.md の指摘どおり、出典（sources）が空。根拠：中の主張に出典 id がない

## grow-review-checklists/write.md
[メインに判断してほしいこと]
- 材料が目次の 1 行（企業ブログ、根拠：中）だけで、ブログの URL・題名が束にない。本文は「企業ブログで紹介された考え方に基づく（根拠：中）」とだけ書き、出典（sources）は空のまま。出典の URL が分かれば sources に足す
- 失敗したときの節は、束に症状ページの id がなく、症状への振り分けではなく関連ページへの link にした
[提案]
- front matter・用語集・data への提案なし。数値の提案なし

## grow-review-checklists/review.md
[メインに判断してほしいこと]
- 指摘 1・2 は直したが、直しの差分は別の担当が確かめていないので stage は draft のまま
- 出典（企業ブログの URL）が束にない。sources は空のまま

## share-targets-and-bounds/write.md
[メインに判断してほしいこと]
- Anthropic の記事（2026-01-21）を WebFetch 1 回で確かめた。公開前の Claude Opus 4.5 を Claude Code で動かした採用課題 v2 で、合格の基準に届いた後に止まり、達成できるサイクル数を伝えると回避策を見つけた。束の「未確認」は本文では原文で確認済みとして扱った。ただし材料の表の「未確認」の印を data 側で外すかは、メンが判断する
- 要点の「根拠の強さ」の項目は、カードの標準の形にない追加。不要なら外してよい
[提案]
なし（数値の提案も用語集への提案もなし）。

## share-targets-and-bounds/review.md
[メインに判断してほしいこと]
- 要点の「根拠の強さ」項目（write.md 指摘のとおりカードの標準外）は残した。外すかは判断を
- 上の警告の直しが効いたか、メインの検査で確認を

## performance-tuning/write.md
[メインに判断してほしいこと]
- sections を 3 つ足した。守り・手順・確かめ方と失敗したときを、recipe の構成の目安どおり独立の節にするため。不要なら統合してよい
[提案]
- なし（変わりやすい値は本文に置いていない。研究の数値はモデル・対象・年を添えた固定の記録として書いた）

## performance-tuning/review.md
[メインに判断してほしいこと]
- 126 行の読点の警告は、メインの検査で出たら「帯（ばらつきの幅）」の括弧を外すか文を分けてよい
- stage は draft のまま（直したため）

