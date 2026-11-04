---
id: experiment-log
title: 実験台帳（仮説を先に書く・提案者・分母・検証器の版）
nav_title: 実験台帳
aliases: [実験ノート, 実験の記録, 実験のログ]
type: recipe
field: eval
chapter: 実験を回す
order: 110
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [体感を信じる]
scenes: [開発, データ分析, コンテスト, チーム]
summary: 実験ごとに、実行前に書く仮説・提案者・分母・検証器の版・採否と判定者を台帳に残せる。結果を見てからの後付けと、同じ失敗の繰り返しを防ぐ。
signs:
  - {type: goal, text: どの変更がなぜ効いたかを、後から追えるようにしたい}
  - {type: symptom, text: 前に効かなかった改善案を、気づかずにまた試していた}
  - {type: symptom, text: 結果を見てから、効いた理由を後付けしている}
wave: 1
prerequisites: [selection-pressure]
related: [decide-when-to-quit, lockbox-and-holdout, measure-changes, verifier-three-conditions, progress-files, keep-failure-lessons, compare-hypotheses-in-parallel, running-contest-experiments, own-generated-code, record-decisions, postmortems, measure-the-upper-bound]
tracks: []
outdated_advice: []
sources: [github-official-stockfish-fishtest, anthropic-research-infrastructure-noise, zenn-chiman-b233cc80, nvidia-winning-kaggle-competition-generative-ai, zenn-nakakiiro-kagglecl, schulman-opinionated-guide-ml-research]
volatility: 低
sections:
  - {title: 実験 1 件の流れ, anchor: flow}
  - {title: 台帳の項目, anchor: fields}
  - {title: 仮説を先に書く, anchor: hypothesis-first}
  - {title: 検証器の版を残す, anchor: verifier-version}
  - {title: 提案者を記録する, anchor: proposer}
  - {title: 進捗ファイルなどとの違い, anchor: not-progress-file}
  - {title: 台帳が書けているかの確かめ方, anchor: check}
  - {title: 台帳があっても繰り返すとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：実験ごとに、実行前に書く仮説、提案者、分母、検証器の版、採否と判定者を台帳に残せる。結果を見てからの後付けと、同じ失敗の繰り返しを防げる。
    - **いつ引くか**：どの変更がなぜ効いたかを後から追いたいとき。前に効かなかった改善案を気づかずにまた試していたとき。結果を見てから、効いた理由を後付けしているとき。
    - **前提**：<!-- link:begin selection-pressure -->選択圧：良かった版を選び続ける罠（準備中）<!-- link:end -->

<!-- textlint-disable -->
別名：実験ノート・実験の記録・実験のログ
<!-- textlint-enable -->

実験台帳は、改善の試行を 1 件ずつ記録するファイルである。Claude に改善案を出させて回すほど、試行は増え、何を試して何が分かったかは会話から消える。台帳は、その記録を会話の外に置く。

台帳の効き目は、2 つの守りに支えられている。1 つは、仮説と採否の基準を結果の前に書いて固定する守りである。もう 1 つは、同じ検証器で測った結果だけを並べる守りである。検証器が信頼できるかどうかは<!-- link:begin verifier-three-conditions -->検証器の三条件（正しい・書き換えられない・本番を代表する）（準備中）<!-- link:end -->で、良かった版を選び続ける罠は<!-- link:begin selection-pressure#defenses -->選択圧：良かった版を選び続ける罠 › 防ぎ方（準備中）<!-- link:end -->で見る。

## 実験 1 件の流れ {#flow}

台帳は、実験 1 件ごとに次の順で使う。各段の終わりに、その段を終えたと言える状態を置く。

1. **台帳を置く**：リポジトリに台帳のファイルを作る。終わりの状態は、commit されて版を追えること。
2. **実行前の欄を埋める**：仮説・採否の基準・変更・分母・検証器の版を書く。過去の件を読み、見送った案と同じでないかも確かめる。終わりの状態は、実行前の欄が commit され、結果の欄が空であること。
3. **走らせる**：書いたコマンドをそのまま走らせる。終わりの状態は、結果が検証器の版と一緒に出力されていること。
4. **実行後の欄を埋める**：結果、採否と判定者、なぜ効いたかの説明を足す。終わりの状態は、仮説の欄を書き換えずに、採否が決まっていること。

各欄に書くことは次の節、仮説の欄の扱いは「仮説を先に書く」の節で見る。

## 台帳の項目 {#fields}

実験台帳は、1 実験を 1 件として、決まった欄を埋めて残すファイルである。置き場所は、プロジェクトのリポジトリの中（例：`docs/experiments.md`）にして、commit で版を追えるようにする。

欄は、実行前に埋めるものと実行後に埋めるもので分ける。

| 欄 | 埋める時 | 書くこと |
| --- | --- | --- |
| ID・日付・commit | 実行前 | 実験を指す番号、日付、変更前後の commit |
| 提案者 | 実行前 | 案を出したのが人か AI か |
| 仮説 | 実行前 | 何が起きると予想するか。外れたら何を意味するか |
| 採否の基準 | 実行前 | 何が出たら採り、何が出たら見送るか |
| 変更・コマンド | 実行前 | 何を変えたか、どう走らせたか |
| 分母 | 実行前 | 何件のケースを、何回ずつ走らせたか |
| 検証器の版 | 実行前と実行後 | 評価を走らせるコードと入力のハッシュ |
| 結果 | 実行後 | 平均、最悪帯（成績の悪い側の下位 10% の平均）、信頼区間、層別（入力の大きさなどの区分ごと）の値 |
| 採否と判定者 | 実行後 | 採る・見送る・保留と、決めた人 |
| なぜ効いたかの説明 | 実行後 | 結果を見た後の解釈。仮説とは別の欄に置く |

分母は、結果の平均や割合が何件の何回から出たかを示す数である。「平均が上がった」だけでは、100 件の平均か 5 件の平均かが分からず、ぶれの大きさも読めない。測り方と必要な数は<!-- link:begin measure-changes#how-many-runs -->変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ（準備中）<!-- link:end -->と<!-- link:begin running-contest-experiments#games-for-win-rate -->実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › 勝率に要る試合数（準備中）<!-- link:end -->で決め、台帳には決めた数を書く。結果は合計だけでなく、層別と最悪ケースの値も残す（<!-- link:begin measure-changes#by-stratum -->変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る（準備中）<!-- link:end -->）。

1 件分の雛形を次に置く。閾値や回数の値は例であり、自分の課題のぶれに合わせて決め直す。

<!-- gen:begin snippet experiment-log/ledger-entry -->
<!-- textlint-disable -->

??? example "雛形：実験台帳の 1 件分（仮説・提案者・分母・検証器の版・採否）"

    ```markdown
    ## EXP-014 ヒューリスティックの近傍に「2 点交換」を足す

    - 日付：2026-12-01（例）
    - commit：a1b2c3d（変更前）→ e4f5a6b（変更後）
    - 提案者：AI（Claude）。きっかけは人が出した「近傍が狭くて局所解に止まる」という観察
    - 仮説（実行前に人が書く。結果を見る前に確定する）：
      近傍に 2 点交換を足せば、平均スコアが上がる。変更前の局所解で止まっているケースが多いので、
      改善は大きいケースほど出ると予想する。上がらなければ、近傍の広さは原因ではないと判断する
    - 採否の基準（実行前に書く。値は例）：
      - 採る：400 ケースの平均の差の 95% 区間が 0 を含まず、最悪帯（下位 10% の平均）が下がっていない
      - 見送る：区間が 0 を含む
      - 同じ案の再挑戦：変種を含めて 4 回までを目安にする（例）
    - 変更：`solve.py` の `neighbors()` に 2 点交換を追加。ほかは触らない
    - コマンド：`python eval/run.py --cases eval/cases --seeds 400 --out runs/exp-014.json`
    - 分母：ケース 400 件（開発用の入力。seed 0〜399）。試行は各ケース 1 回。層別は入力の大きさで 3 層
    - 検証器の版：`eval/run.py` と `eval/cases/` のハッシュ 7f3a9c21（結果の先頭に出力させて貼る）。
      変更前の記録と同じ値であることを確かめた
    - 結果：平均の差、最悪帯（下位 10% の平均）の差、95% 区間、層別の表（ここに貼る）
    - 採否と判定者：採る／見送る／保留。判定者：人（提案者とは別）。日付
    - なぜ効いたかの説明（結果を見た後に書く。仮説とは別の欄に置く）：
      仮説どおりか、予想外か。説明できない採用は保留にする
    - 次の一手：この結果で消えた案と、新しく出た案
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet experiment-log/ledger-entry -->

## 仮説を先に書く {#hypothesis-first}

仮説は、実験を走らせる前に人が書き、結果を見た後で書き換えない。結果を見てから説明を作ると、どんな結果でも「予想どおり」に見えてしまうからである。

後付けの説明は、結果が出た後の自分に都合のよい筋書きになりやすい。Claude に頼むと、これはさらに起きやすくなる。結果を渡して「なぜ効いたか」を聞けば、Claude はもっともらしい理由を書く。その理由が正しいかどうかは、その実験だけでは確かめられない。

先に書く内容は 3 つである。

- **仮説**：変更によって何がどう変わると予想するか。ケースの種類による差も予想できるなら書く。
- **外れたときの解釈**：予想が外れたら、何が分かったことになるか。ここが書けない実験は、結果の使い道が決まっていない。
- **採否の基準**：何が出たら採り、何が出たら見送るか。基準を後から動かせると、見たい結果に合わせて採否が決まる。基準を動かすときは、先に理由を台帳へ書く。

結果を見た後の解釈は、仮説の欄とは別の「なぜ効いたか」の欄に書く。2 つの欄を比べると、予想どおりだったのか、予想外だったのかが残る。

説明できない採用は保留にする。「改善したが、なぜかは分からない」変更は、別の入力や別の検証器で崩れる危険を抱えたまま本流に入る。説明を Claude に出させて自分で確かめる手順は<!-- link:begin own-generated-code#gate -->生成コードを自分のものにする › 自分の言葉で言い直してから採る（準備中）<!-- link:end -->で見る。

台帳の書き込みは Claude に手伝わせてよいが、仮説の欄と採否の基準の欄は人が書く。実行前の欄だけを埋めさせ、結果の欄を空のまま残させる依頼の雛形を次に置く。

<!-- gen:begin snippet experiment-log/ask-to-log -->
<!-- textlint-disable -->

??? example "雛形：台帳に実行前の欄だけを書かせ、過去の実験との重複を確かめさせる依頼"

    ```markdown
    実験台帳 `docs/experiments.md` に、次の実験の記録を追加する。まだ実験は走らせない。

    1. 末尾に新しい ID の見出しを作り、「仮説」「採否の基準」「変更」「コマンド」「分母」「検証器の版」の欄だけを埋める。
    2. 仮説と採否の基準は、私が下に書いた文をそのまま写す。言い換えたり、補ったりしない。
    3. 「結果」「採否と判定者」「なぜ効いたかの説明」は空欄のまま残す。
    4. 台帳に書いてある過去の実験を読み、今回の案が、見送った案と同じか変種でないかを確かめる。同じなら、その実験の ID と見送った理由を挙げて、走らせる前に私に聞く。
    5. 提案者の欄は「AI」と書き、私の案なら「人」と書く。判断がつかないときは聞く。

    仮説：…
    採否の基準：…
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet experiment-log/ask-to-log -->

仮説と基準を写させるのは、Claude が書き換えて整えるのを防ぐためである。実験の前に決めた基準を、事後に動かしていないかは、commit の履歴で確かめられる。

## 検証器の版を残す {#verifier-version}

検証器の版は、結果と一緒に台帳へ残す。検証器が変わると、前後の数値は同じ物差しで測ったものではなくなるからである。検証器は、評価を走らせるコードと、評価に使う入力やケースの組を合わせたものを指す。

版は、ハッシュで残すのが確実である。評価を走らせるコードと入力をまとめたハッシュを、評価を走らせるスクリプト（ランナー）が結果の先頭に書き出す。台帳にはそのハッシュを貼る。ハッシュが前の実験と同じなら、検証器は変わっていない証拠になる。違うなら、前の数値と並べて比べてはいけない。

次の場面で、版の違いが問題になる。

- **検証器を直した後**：バグ修正や採点の変更で数値の水準が動く。直した後は、直す前の版を、新しい検証器で測り直して基準線にする。
- **ケースを足した後**：入力の組が変わるので、平均は別の物差しになる。
- **実行環境が変わった後**：実行環境の違いだけで、エージェント型のコーディング評価の結果が動くという Anthropic の報告がある（根拠：中）。環境の版（ランナーの設定、マシン、ライブラリ）も、分かる範囲で台帳に書く。細かい差は「ぶれ」として扱い、小さな差を採否の理由にしない。詳細は[Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/research/infrastructure-noise)を読む。

Claude に検証器そのものを書き換えさせない守りは<!-- link:begin verifier-three-conditions#tamper-proof -->検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない（準備中）<!-- link:end -->で見る。人だけが持つ入力の扱いは<!-- link:begin lockbox-and-holdout#scores-only -->ロックボックスと hold-out（人だけが持つ検証用データ） › 点数だけを返す（準備中）<!-- link:end -->で見る。台帳のハッシュは、書き換えを事後に見つける手がかりにもなる。

## 提案者を記録する {#proposer}

台帳の提案者の欄には、案を出したのが人か AI かを書く。実験の入口を記録する欄である。

この欄を付ける理由は 2 つある。

1. **後から振り返る材料になる**：採用した変更のうち、誰の案が多かったかが分かる。AI の案を採用するときに、人が確かめた点を追える。
2. **実験の置き場所を分けられる**：Kaggle の上位勢のリポジトリに、Claude の実験と人の実験を命名で分ける例がある（根拠：弱）。ID の接頭辞（`H-` は人、`A-` は AI）で分けておくと、台帳を絞り込める。

提案者ごとに、当たりの率（採用に至った実験の割合）を比べる案も考えられる。ただし、この比べ方は先行例のない独自の提案である（推論・実践例なし）。案の種類や難しさが人と AI で違えば、率の差は提案者の力量を表さない。傾向を見る程度にとどめ、採否の基準にはしない。

AI の案を採用するときの確認は、台帳の外にも持つ。採る前に、変更の理由を Claude に説明させ、自分の言葉で言い直せるかを確かめる（<!-- link:begin own-generated-code#explain -->生成コードを自分のものにする › 処理の流れと入力の端を説明させる（準備中）<!-- link:end -->）。

## 進捗ファイルなどとの違い {#not-progress-file}

実験台帳は、採否の記録である。作業を続けるための記録とは目的が違う。

- **進捗ファイル**：計画・やること・決めたこと・分かったことを持ち、別のセッションから作業を再開するためのファイルである。内容は更新され続ける。<!-- link:begin progress-files#files -->進捗ファイルで、途中から再開できるようにする › ファイルの分け方（準備中）<!-- link:end -->を見る。
- **実験台帳**：1 件ずつ、実行前に仮説を書き、実行後に結果と採否を足す記録である。件が増えるだけで、過去の件は書き換えない。
- **失敗の教訓**：捨てた試みから「何が駄目だったか」だけを短く残すものである。台帳の「なぜ効かなかったか」の欄を要約して持ってもよい。<!-- link:begin keep-failure-lessons#what-to-keep -->失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか（準備中）<!-- link:end -->を見る。
- **決定の記録**：決めたことと理由を、チームに残す文書である。実験で採った変更の理由は、台帳を指す形でそこに書ける。<!-- link:begin record-decisions -->決定を文書に残す（ADR と週次アップデート）（準備中）<!-- link:end -->を見る。

効かなかった実験も、台帳に残す。Kaggle の事例では、改善しなかった実験の予測も保存して、後で組み合わせた（根拠：弱）。Claude が前の実験の要約ファイルを「記憶」として読み、失敗済みの案の再提案を防いだ事例もある（根拠：弱）。個々の事例は[Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/)と[Claude Code / CodexでKaggle金メダルを取った話](https://zenn.dev/chiman/articles/b233cc808d6af3)にある。

## 台帳が書けているかの確かめ方 {#check}

台帳が機能しているかは、次の 3 つの問いで確かめる。

1. **実行前に書いたと言えるか**：仮説と採否の基準の欄の最後の更新が、結果の記録より前の commit か。同じ commit なら、結果を見た後に書いた可能性が残る。
2. **別の人が追えるか**：台帳だけを渡された人が、検証器の版と分母から、同じ条件で実験をやり直せるか。
3. **同じ案を見つけられるか**：新しい案が出たとき、台帳を検索して、過去の実験と同じか変種かを見つけられるか。台帳の見出しに、案の短い名前（例：「2 点交換」）を付けておくと見つけやすい。

Claude に、台帳の過去の件と今回の案の重複を調べさせるのも、有効な確かめ方になる。ただし、Claude が「重複なし」と答えても、案の名前を変えただけの重複を見落とすことがある。重複と判断された件の ID を挙げさせ、その件を自分で読む。

## 台帳があっても繰り返すとき {#when-it-fails}

台帳を付けても、同じ失敗の繰り返しは起きる。起きたときは、次の順に見直す。

- **台帳を読まずに案を出している**：Claude に案を考えさせる前に、台帳を読ませる。依頼に台帳のパスを書く。台帳が長くなりすぎたら、見送った案の一覧を別に作る（<!-- link:begin keep-failure-lessons#too-much -->失敗の教訓は捨てずに書き残す › 書き残しすぎの副作用（準備中）<!-- link:end -->）。
- **同じ案の変種を延々と試している**：変種ごとに別の案として記録すると、1 つの案への挑戦回数が見えなくなる。同じ案の再挑戦に上限を置く。チェスエンジンの検定基盤 Fishtest の FAQ は、同じアイデアの再挑戦におおむね数回の上限を置くとしている。チェスの慣行なので、他の課題への当てはめは類推である。上限の考え方は<!-- link:begin selection-pressure#retry-cap -->選択圧：良かった版を選び続ける罠 › 同じアイデアの再挑戦に上限を置く（準備中）<!-- link:end -->で見る。出典は[Fishtest FAQ](https://github.com/official-stockfish/fishtest/wiki/Fishtest-faq)にある。
- **やめどきが決まっていない**：頭打ちになった後も実験を重ねている。方針そのものを疑う合図は<!-- link:begin decide-when-to-quit#plateau -->やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図（準備中）<!-- link:end -->で見る。
- **方針を変えすぎている**：逆に、方針を頻繁に変えすぎるのも失敗になる。ML 研究の実践者に、毎日の実験とアイデアをノートに残して定期的に見返すことを勧める例がある（根拠：弱）。変えすぎの扱いは<!-- link:begin decide-when-to-quit#dont-switch-too-often -->やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 変えすぎも失敗（準備中）<!-- link:end -->にある。
- **台帳が形だけになっている**：仮説の欄が「改善する」の一言である。外れたときの解釈と採否の基準が書けないなら、その実験は走らせる前に設計し直す。
- **失敗の原因を仕組みで見たい**：誰が間違えたかではなく、どの隙間が許したかで振り返る。<!-- link:begin postmortems#which-gap -->失敗を仕組みに戻す（ポストモーテム） › 誰がではなく、どの隙間が（準備中）<!-- link:end -->を見る。

開発用の入力で測り続けると、台帳に書いた「採った」変更の集まりが、その入力に合わせ込まれる。節目の確認には、開発では見ない入力を使う（<!-- link:begin lockbox-and-holdout#three-tiers -->ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける（準備中）<!-- link:end -->）。台帳は、合わせ込みを防ぐ代わりに、合わせ込みが起きた経緯を後から追う手段になる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Fishtest FAQ](https://github.com/official-stockfish/fishtest/wiki/Fishtest-faq)：GitHub（official-stockfish）・英語・確認日 2026-11-04
- [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/research/infrastructure-noise)：Anthropic・英語・確認日 2026-11-04
- [Claude Code / CodexでKaggle金メダルを取った話](https://zenn.dev/chiman/articles/b233cc808d6af3)：Zenn（chiman）・確認日 2026-11-04
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/)：NVIDIA Developer Blog・英語・確認日 2026-11-04
- [【Claude Code】Kaggle上位勢が設定するClaude Codeのskillsとagentsをチェックする](https://zenn.dev/nakakiiro/articles/kaggle_claude_code_boilerplate)：Zenn（nakakiiro）・確認日 2026-11-04
- [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html)：John Schulman（個人のブログ）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- 選択圧：良かった版を選び続ける罠（準備中）

**次に読む**

- 仮説ごとに並べて、同じ物差しで比べる（準備中）
- 実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）（準備中）

**関連**

- やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）（準備中）
- ロックボックスと hold-out（人だけが持つ検証用データ）（準備中）
- 変更が効いたかを測る（小さな eval）（準備中）
- 検証器の三条件（正しい・書き換えられない・本番を代表する）（準備中）
- 進捗ファイルで、途中から再開できるようにする（準備中）
- 失敗の教訓は捨てずに書き残す（準備中）
- 生成コードを自分のものにする（準備中）
- 決定を文書に残す（ADR と週次アップデート）（準備中）
- 失敗を仕組みに戻す（ポストモーテム）（準備中）
- 上界を測って「限界です」を反証する（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
