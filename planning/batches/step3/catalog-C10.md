# 工程3 C10：judgment（判断と理解を守る）と contest（コンテストで使う）の目次の報告

- 担当：C10（2026-11-04）
- 書いたもの：[planning/catalog/judgment.yaml](../../catalog/judgment.yaml)（11ページ）・[planning/catalog/contest.yaml](../../catalog/contest.yaml)（9ページ・まとめた候補3）・この報告
- ほかのファイルは変えていない。git の操作と Web は使っていない。kyopro-atlas は、方針 A5 のリンク先の見当を付けるために `../kyopro-atlas/docs` を読んだだけ（decisions 2026-11-03「手本の読み方」の範囲）
- 材料：brief-catalog.md の §2・§3 のとおり。根拠の強さは research/24 §2.3（F1）、大会の規則は research/24 §2.4 と decisions 2026-11-03「大会の規則の版」、実在の人物は research/24 A-6・research/25 P1・P12 に従った

## 1. 書いたファイルとページ数

| 分野 | ページ | 優先度 | レベル | 型 |
| --- | --- | --- | --- | --- |
| judgment | 11 | 必須 6・推奨 4・任意 1 | 整える 7・任せる 3・仕組みにする 1 | judgment 11 |
| contest | 9 | 必須 2・推奨 5・任意 2 | 使う 2・整える 1・任せる 3・仕組みにする 2・なし 1 | concept 4・recipe 4・hub 1 |

章（ナビゲーションの小見出し）：

- judgment：総論／落とし穴ごとの対策／理解を手放さない／振り返りと再発防止
- contest：入口と現在地／規則と練習／評価と実験／本番とチーム戦

### judgment

| id | 題名（略） | 優先度 | level | wave | pitfalls |
| --- | --- | --- | --- | --- | --- |
| human-pitfalls | 人の側の五つの落とし穴（総論） | 必須 | 整える | 1 | 五つすべて |
| over-reliance | 判断を預けすぎる（過度依存） | 必須 | 整える | 1 | 預けすぎる |
| agreement-is-not-evidence | 同意は根拠に数えない | 必須 | 整える | 1 | 同意を根拠にする |
| ask-without-sycophancy | 迎合させない聞き方 | 推奨 | 整える | | 同意を根拠にする |
| decide-when-to-quit | やめどきを先に決める | 必須 | 任せる | 1 | やめられない |
| ai-ideas-are-everyones | AI の案は「みんなの案」 | 必須 | 整える | 1 | みんなの案になる |
| think-before-asking | 頼む前に自分で考える | 推奨 | 整える | | みんなの案になる・預けすぎる |
| learning-with-ai | AI で新しい技術を学ぶ | 必須（推奨から上げた） | 整える | 1 | 預けすぎる・体感を信じる |
| how-much-understanding-to-keep | どこまで理解を手放してよいか | 推奨 | 任せる | | 預けすぎる |
| retros-without-ai-verdicts | 振り返りで AI に評価させない | 任意 | 任せる | | 同意を根拠にする・体感を信じる |
| postmortems | 失敗を仕組みに戻す | 推奨 | 仕組みにする | | — |

- 落とし穴エ（体感を信じる）の本体は eval の felt-vs-measured（C8 が judgment 型・必須・wave 1 で作った）。総論から関連で指す
- どの judgment のページも pitfalls を持つ（postmortems は落とし穴を名指ししない再発防止の型なので空。人の側の落とし穴の一覧には総論から入る）

### contest

| id | 題名（略） | 優先度 | level | 型 |
| --- | --- | --- | --- | --- |
| format-cheatsheet | コンテストの形式別の早見表 | 推奨 | なし | hub（comparison から変えた） |
| ai-in-contests-today | AI はコンテストでどこまで来たか（確認日付き） | 推奨 | 使う | concept |
| competition-rules | 大会の規則の早見（禁止・部門分け・許可と開示） | 必須 | 使う | concept |
| practice-vs-contest-day | 練習と本番の使い分け | 必須 | 整える | concept |
| evaluators-by-format | 形式別の評価器 | 推奨 | 任せる（仕組みにするから下げた） | concept |
| running-contest-experiments | 実験の回し方 | 推奨 | 仕組みにする | recipe |
| search-code-checklist | 探索コードと高速化の点検表（AI に書かせたとき） | 任意 | 任せる | recipe |
| competition-day-operations | 本番の運用 | 推奨 | 任せる | recipe |
| long-team-competitions | チーム戦の運用（長期・対戦型） | 任意 | 仕組みにする | recipe |

- 七つの形式は、format-cheatsheet と evaluators-by-format の両方で同じ厚さの節にした（decisions「コンテストの分野」）。requirements §4.3 の七つに短期のヒューリスティック（短期 AHC）がないので、ヒューリスティックの節の中で短期と長期を分ける
- 大会の規則と成績は、類型・版・確認日・出典の種類・リンクだけを数値ファイルに置く前提で書き、確かめられない版（ABC・ARC・AGC の20261014版、短期 AHC の20260818版、長期 AHC の20261026版、Codeforces、「過去問の練習には適用されない」）は「未確認」と notes に書いた
- 対戦型と長期チーム戦は直接の研究がなく類推、と notes に書いた（format-cheatsheet・long-team-competitions）
- 競技の練習法と AtCoder の規則の細部は kyopro-atlas へリンクする（方針 A5）。catalog の id では指せないので、各ページの notes にリンク先の見当（atcoder-system#ai-rules・practice-method・contest-strategy・stress-testing）を書いた

## 2. まとめた候補・採らなかった候補・新しいページ

まとめた（contest.yaml の merged）：

| 候補 | まとめた先 | 理由 |
| --- | --- | --- |
| formats-and-ai-fit | format-cheatsheet（節 why-formats-differ） | 五つの軸の一般の判断は delegate の is-the-task-ai-suited が持つ（11 第1節 分野12 p12#63）。形式ごとの当てはめは早見表の列そのもの。成績のばらつきは ai-in-contests-today の囲みへ。D5 |
| insight-patterns | think-before-asking（節 five-questions） | 11 は考察の五つの問いと「先に自分、その後で AI」を新分野案X に置き、新分野案Y「考察の型」の行は上位者の考察の手順（競技の技術そのもの）。AI への頼み方だけを残し、競技の技術は kyopro-atlas へ（方針 A5） |
| reading-top-solutions | learning-with-ai（節 summaries-of-solutions） | AI に関わる中身（要約で手法の条件が落ちる、AI の使い方を書き残す）は一般化できる。後者は retros-without-ai-verdicts の節 record-ai-usage に置いた。上位解法を読む練習そのものは kyopro-atlas へ。根拠の一つ（With AI 部門の解説の義務）は未確認（research/24 A-3） |

- 採らなかった候補：なし
- 新しいページ：なし
- registry から変えた点：learning-with-ai の優先度（推奨 → 必須）、format-cheatsheet の型（comparison → hub。比べて選ぶものではなく、自分の形式の行から進む題材の入口なので）、evaluators-by-format の level（仕組みにする → 任せる。AI に任せる前の最初の成果物で、competition-day-operations の前提にするため）、題名の小さな直し（competition-rules の「開示」を方針 A4 の類型に合わせて「許可と開示」に、search-code-checklist に「（AI に書かせたとき）」を足した、など）

## 3. wave: 1 を付けたページ（judgment）

human-pitfalls・over-reliance・agreement-is-not-evidence・decide-when-to-quit・ai-ideas-are-everyones・learning-with-ai の6つ。

- registry の wave_core の5つ（総論と、落とし穴ア・イ・ウ・オの本体）に learning-with-ai を足した。D10 の「判断と理解の核」の理解の側が第一波に一つもないのを避けるため。learning-with-ai は根拠に無作為化実験があり（Anthropic の研究は52人・GPT-4o ベース・課題の直後のクイズ、高校生の実験は約1,000人・GPT-4）、how-much-understanding-to-keep と contest の practice-vs-contest-day（必須）の前提になる
- 第一波で前提からたどって入るほかの分野のページは、four-principles（start）と sycophancy（basics。C1 が必須に上げたので agreement-is-not-evidence の前提にした）
- contest には付けていない（decisions 2026-11-03「第一波に足すもの」）

## 4. ほかの分野への提案と new_features

open_issues の要約（詳しくは各ファイルの open_issues）：

1. **eval・verify（C8）**：10 付録A-9 の後半（差分スコアと全再計算の一致の assert）は局所探索に固有なので、eval の differential-testing でなく contest の search-code-checklist の雛形にする案。A-16 の前半は verify の own-generated-code（出荷の基準）と judgment の learning-with-ai（学ぶ手順）で書き分ける。verifier-three-conditions と what-not-to-delegate（C9）は、工程4でも任せるより上の段にしない（上げると段の逆転）
2. **symptoms（C12）**：人の側の診断の振り分けの案。caves-when-pushed → agreement-is-not-evidence・ask-without-sycophancy、wont-rethink-approach → decide-when-to-quit。going-in-circles（整える）からは decide-when-to-quit（任せる）を前提にせず関連にすると段の逆転を避けられる
3. **メイン（数値ファイル）**：data/facts.yml に、大会の規則の項目（大会・部門・類型・版・版の状態〔確認済み・未確認〕・確認日・一次資料の所在・確かめた資料の種類）と、AI の成績の項目（大会・日付・結果・出典の種類〔一次・報道・ベンダーの推定・自己申告〕・確認日）の形を design §9.1 に足す
4. **メイン（kyopro-atlas との食い違い）**：方針 A5 でリンクする kyopro-atlas の atcoder-system#ai-rules は「（20261014 版は）過去問の練習には適用されない」と言い切っている。claude-atlas はこの点と版を「未確認」とする。リンクはよいが、二つの教材の書き方が食い違って見える（kyopro-atlas は変えていない）
5. **ほかの分野からの参照**：まとめた3つの候補を指すと参照のエラーになる。途中で delegate・team・recipes が指していたが各担当が直した。この報告の時点で残るのは prompting の share-targets-and-bounds の related の formats-and-ai-fit（C3。format-cheatsheet に替える）。insight-patterns を指すページは、think-before-asking をすでに前提か関連に持つなら外すだけでよい（#five-questions に替えると前提と関連の重複のエラー）

ほかの担当の提案で取り込んだもの：C1（human-pitfalls-intro を six-causes にまとめた → human-pitfalls は six-causes を関連に。sycophancy を必須に → agreement-is-not-evidence の前提に）、C7（checking-ai-rules を必須に → competition-rules の前提）、C8（felt-vs-measured を落とし穴エの本体に。running-contest-experiments の前提に selection-pressure、層別は measure-changes#by-stratum、agreement-is-not-evidence の関連に model-based-grading、A-15 を experiment-log と decide-when-to-quit で分け合う）、C9（format-cheatsheet の前提に is-the-task-ai-suited、long-team-competitions の前提に separate-roles、関連の追加）、C11（read-specs-yourself・build-test-harness への関連、search-code-checklist はコンテストに固有の点検だけ）。

取り込まなかったもの：C7 の「practice-vs-contest-day の前提にも checking-ai-rules」。competition-rules を通して推移的に届くので、直接の前提だけを書く規則（catalog/README §4.4-1）に従った。

new_features：なし（tracks に使ったのは subagents・output-styles・insights・claude-md・hooks・permissions・usage-limits で、どれも catalog/README §5 にある）。

## 5. 検査の結果

`python3 tools/check_catalog.py --field judgment` と `--field contest` を、ほかの分野のファイルが増えるたびに流し直した。

- 2026-11-04 01:45（分野のファイル21・ページ310。symptoms だけがまだない）：judgment・contest ともにエラー 0・警告 0
- 最後に流した 01:47（分野のファイル23・ページ329）：judgment はエラー 0・警告 5、contest はエラー 0・警告 3。警告はすべて「未処理の候補」で、symptoms.yaml が書きかけ（6ページまで）のため、関連に置いた症状のページ（wont-rethink-approach・going-in-circles・summary-overstates-source・deleted-something-important・instructions-ignored・misses-broken-evaluation・stuck-in-a-check-loop）がまだ入っていない。症状は1症状1ページで残る（design §4.1）ので、C12 が書き終えれば消える見込み。まとめられた場合は、まとめた先に替える
- 全体の検査で私のファイルに関わるエラーは、prompting の share-targets-and-bounds → formats-and-ai-fit の1件（相手のファイルの参照。§4 の5）
- 途中の一時の警告：prompting が書きかけの間、関連に置いた ask-for-options・prompt-patterns・before-after-prompts が「未処理の候補」になったが、prompting が書き終えて消えた

途中で直したもの：eval が stratified-and-worst-case を measure-changes にまとめたので、running-contest-experiments の関連を measure-changes#by-stratum に替えた（参照のエラー1件を0にした）。

検査の道具が見ない規則も手で確かめた：aliases に題名と同じ語を入れない（6か所を直した）、materials と notes に個人の名前を書かない（名前の一覧で検索して0件）、summary に強さを断定しない・変わりやすい値を書かない。

## 6. 確かめていないこと・迷った点

確かめていないこと（各ページの notes に書き、執筆の前に確かめる）：

- 工程2で一次資料を確かめていない研究：先に人が答える設計の研究と、確かめるのが安いほど依存が減る研究（総論・over-reliance）、固執のメタ分析の「リスクや機会費用の情報は固執を弱める」（decide-when-to-quit）、考えてから使う群の研究の1件と創作の実験の「10.7%」、研究アイデアの研究、悪魔の代弁者・「挑発」の研究、押しの説得率「84.5%」（research/24 §5・B-44・B-55）
- 大会の成績のうち、AWTF 2025、ICPC 2025 の OpenAI の12問、IOI 2025 の6位相当、AWTF 2026 Algorithm の5問（報道だけ。research/24 §5）
- 大会の規則の版と各部門の範囲（§1 の未確認の一覧）
- symptoms（この時点でまだファイルがない）からの参照と、そこへの参照（caves-when-pushed・wont-rethink-approach・going-in-circles など）。symptoms ができた後の全体の検査で確かめる

迷った点：

1. **learning-with-ai を必須・wave 1 にしたこと**。brief の「総論と、ほかのページの多くが前提にするページ」だけで読むと総論1つになるが、registry の wave_core（総論と四つの落とし穴の本体）と D10 の「判断と理解の核」に合わせ、理解の側から1つ足した。第一波を小さく保つなら、learning-with-ai を推奨に戻してよい（その場合 practice-vs-contest-day の前提から外す）
2. **contest の3つのまとめ**。D5（固有の論点だけ）と方針 A5（競技の技術と練習法は kyopro-atlas）による。requirements §4.3 の12の候補が9ページになった。ほかの担当が指していたので、まとめる判断は早めに伝わるほうがよかった
3. **ai-in-contests-today を残したこと**。design §4.1-5（事例の紹介だけのページは作らない）に当たらないよう「成績から何を読むか」を本体にした。それでも薄ければ、format-cheatsheet の確認日付きの囲みにまとめる案がある
4. **format-cheatsheet を hub にしたこと**。level を持たないのでロードマップの段には出ない。題材の入口として、逆引きの状況のサインから入る想定
5. **search-code-checklist（任意）**。点検表の多くは補完自身が推論と明記した項目。任意なので残したが、工程4で recipes の performance-tuning の節に寄せる判断もありうる
6. **human-pitfalls の題名の「（総論）」**。registry どおりにした。start の入口（human-pitfalls-intro）は C1 が six-causes にまとめたので、題名が紛れる心配はなくなった。「（総論）」を外すかは工程4で決めてよい
7. **brief の「materials と notes にも、個人の名前を書かない」**は、否定的な文脈に限らず名前を書かない、と強めに読んだ。研究と事例は 11 の元ID と research/24・25 の項目の番号で指した。執筆の段で、肯定的な文脈の出典として名前を出すのは D12 のとおり差し支えない
8. **surfaces**：judgment のページは [app, claude-code] にした（判断はどの面でも同じだが、新しい文脈で批評させる手段などがアプリと Claude Code で違う）。api の面は付けていない
