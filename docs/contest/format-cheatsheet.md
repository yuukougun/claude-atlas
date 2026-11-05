---
id: format-cheatsheet
title: コンテストの形式別の早見表（AI の効き方と人が握るところ）
nav_title: 形式別の早見表
aliases: [形式と AI の効き方, 大会の形式ごとの AI の使いどころ]
type: hub
field: contest
chapter: 入口と現在地
order: 10
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる, 握る]
prevents: []
pitfalls: []
scenes: [コンテスト]
summary: 七つの形式ごとに、AI が効くところ・人が握るところ・評価器・規則の類型・当日の注意を一つの表で引ける。形式で効き方が違う理由も五つの軸で分かる。
signs:
  - {type: situation, text: AHC や Kaggle、ISUCON、CTF に AI を使って出たい}
  - {type: goal, text: 出る大会で、AI がどこまで役に立つか見当を付けたい}
  - {type: situation, text: 初めての形式の大会に出るので、AI の使いどころが分からない}
prerequisites: [is-the-task-ai-suited]
related: [ai-in-contests-today, competition-rules, practice-vs-contest-day, evaluators-by-format, competition-day-operations, running-contest-experiments, search-code-checklist, long-team-competitions, verifier-defines-problem, checking-ai-rules, read-specs-yourself, build-observation-tools, think-before-asking, ai-ideas-are-everyones, entrusted-data, instructions-hidden-in-materials, disclosure-and-provenance, performance-tuning]
tracks: []
outdated_advice: []
volatility: 高
sections:
  - {title: 七つの形式の早見表, anchor: overview}
  - {title: 形式で効き方が違う理由（五つの軸）, anchor: why-formats-differ}
  - {title: 短時間のアルゴリズム, anchor: algorithm}
  - {title: ヒューリスティック（短期・長期）, anchor: heuristic}
  - {title: 性能改善, anchor: performance-tuning}
  - {title: CTF, anchor: ctf}
  - {title: データ分析, anchor: data-analysis}
  - {title: ハッカソン・作品, anchor: hackathon}
  - {title: 対戦型・長期チーム戦, anchor: battle-and-team}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：7 つの形式ごとに、AI が効くところ・人が握るところ・評価器を早見表で引ける。効き方の違う理由も読める。
    - **いつ引くか**：AHC や Kaggle、ISUCON、CTF に AI を使って出るとき。初めての形式の大会で、AI の使いどころの見当を付けたいとき。
    - **前提**：<!-- link:begin is-the-task-ai-suited -->[そのタスクは AI に向いているか（五つの軸）](../delegate/is-the-task-ai-suited.md)<!-- link:end -->

<!-- textlint-disable -->
別名：形式と AI の効き方・大会の形式ごとの AI の使いどころ
<!-- textlint-enable -->

コンテストの形式別の早見表は、大会の形式から、AI が効くところと人が握るところ、評価器、規則で確かめること、当日の注意を引く入口である。中身の説明は各ページが持ち、ここは自分の形式の行から進む先を示す。表は 2026-11-05 時点の整理で、形式を比べた定量の研究はなく、個別の事例からの推論である（根拠：中）。

## 七つの形式の早見表 {#overview}

先に規則を確かめ、規則が許す範囲で AI の使いどころを決める。規則が割れる理由と確認表は <!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](../safety/checking-ai-rules.md#checklist)<!-- link:end --> にあり、主な大会の類型と版は <!-- link:begin competition-rules#rules-by-type -->[大会の規則の早見（禁止・部門分け・許可と開示） › 類型ごとの大会（確認日付き）](competition-rules.md#rules-by-type)<!-- link:end --> の表で引ける。大会と回で規則は変わる。そのため、以下の 2 つの表には条文も類型も書かず、類型と版は確認日つきの表で引く。

最初の表は、形式ごとの AI の使いどころと人の受け持ち、検証に使う評価器である。形式の名前から各節へ進める。

| 形式 | AI が効くところ | 人が握るところ | 評価器 |
| --- | --- | --- | --- |
| [短時間のアルゴリズム](#algorithm) | 練習での解説、別解の比較、テストケースの生成、弱点の分析 | 本番の考察と実装。オンサイトでは分担と時間配分 | 愚直解との比較 |
| [ヒューリスティック](#heuristic) | テスタや可視化の作成。長期では並列の実験、実装、高速化、パラメータ探索 | 問題の本質の考察、評価関数、新しい方針、時間配分、ループから抜ける判断 | 公式とスコアが一致するテスタ |
| [性能改善](#performance-tuning) | 定番の初手（インデックス、N+1、キャッシュ）、計装、コードの全体把握 | 中盤以降の計測の解釈、ボトルネックの見極め、仕様上のトレードオフ | ベンチマーカー |
| [CTF](#ctf) | 易〜中難度の問題、序盤の速さ、並列化 | 新規性の高い問題、OSINT、推測型、実行時の状態、長時間の一貫性 | flag の検証 |
| [データ分析](#data-analysis) | パイプライン、EDA、実験の量産、先行解の調査、アンサンブル | CV の設計、リークの検出、データの目視、最終提出の選択 | 分布の差を確かめた CV |
| [ハッカソン・作品](#hackathon) | 試作の速さ、実装の幅 | 課題設定、ユーザーにとっての価値、説明と発表 | 機械の評価器がない |
| [対戦型・長期チーム戦](#battle-and-team) | 補助関数の初版、ローカルの対戦場、基準ボット、周辺作業と集計 | 戦略とメタの読み、評価の定義、撤退の判断、チームの合意 | 対戦場と基準のボット |

次の表は、形式ごとに規則で確かめることと、当日の注意である。

| 形式 | 規則で確かめること | 当日の注意 |
| --- | --- | --- |
| [短時間のアルゴリズム](#algorithm) | 補完や AI 概要の扱い、翻訳の可否。オンサイトの機器と通信の制限 | 補完と AI 概要を確実に切る。事前ライブラリの出所を書けるようにする |
| [ヒューリスティック](#heuristic) | 部門の有無と、部門ごとの許可の範囲。補完ツールの指定 | 初回提出の前に部門を選ぶ。ログを残す。費用の上限を決める |
| [性能改善](#performance-tuning) | レギュレーションの AI の項目。当日のマニュアルの優先 | 再起動試験、データの永続化、最終計測前の計装の除去、終盤の変更の凍結 |
| [CTF](#ctf) | AI の扱いと、部門・区分 | flag は提出前に検証する。誤答のペナルティと、問題に仕込まれた指示に注意する |
| [データ分析](#data-analysis) | データを外部の AI に送ってよいか。コードコンペの実行環境 | 最終提出は CV と公開順位のずれを見て人が選ぶ |
| [ハッカソン・作品](#hackathon) | AI を使った箇所の説明や開示の求め | 使った箇所を記録して開示する。デッドコードと保守性での減点に注意する |
| [対戦型・長期チーム戦](#battle-and-team) | 要項と行動規範。運営への確認の記録 | 直前の大きな変更を避け、戻せるようにする。リハーサルを複数回行う |

## 形式で効き方が違う理由（五つの軸） {#why-formats-differ}

形式で AI の効き方が違うのは、作業を AI に任せて効くかを決める 5 つの軸が、形式ごとに違う値を取るからである。軸の一般の判断は <!-- link:begin is-the-task-ai-suited#five-axes -->[そのタスクは AI に向いているか（五つの軸） › 五つの軸](../delegate/is-the-task-ai-suited.md#five-axes)<!-- link:end --> が持ち、ここは大会の形式への当てはめだけを置く。

5 つの軸は、検証器の速さと信頼性、問題の典型度、入出力がテキストで完結するか、環境の制約、期間である。AI が最も効くのは、次の条件がそろう形式である。検証器が機械的で速い。問題が典型的である。入出力がテキストで完結する。手元で回せる。期間が中程度以上ある。人の価値が残るのは、検証器がないかノイズが大きい場面、新規の問題、外部環境とのやりとり、長時間の一貫性である（根拠：中、個別事例からの推論）。

次の表は、7 つの形式を 5 つの軸で並べた効きやすさの見当である。同じ形式の中でも、問題ごとにばらつく。

| 形式 | 検証器の速さと信頼性 | 問題の典型度 | テキストで完結 | 環境の制約 | 期間 |
| --- | --- | --- | --- | --- | --- |
| 短時間のアルゴリズム | 愚直解との比較を手元で組める | 過去問に近いものが多い | 完結する | 軽い（手元で回る） | 短い |
| ヒューリスティック | 公式と一致するテスタが手元にある | 中（方針は問題ごとに違う） | ほぼ完結する（可視化は別） | 軽い（長期は計算の費用がかかる） | 短期は短く、長期は日単位 |
| 性能改善 | ベンチマーカーで速いが、計測のぶれがある | 定番の初手は典型 | 完結しない（サーバ環境） | 重い（再起動・永続化） | 短い。頭打ちが来る |
| CTF | flag の正否は明確だが、提出に制限がある | 易〜中は典型、難問は新規 | 問題による | 重い（外部サーバ・実行環境） | 短い。AI の優位が序盤に寄る |
| データ分析 | CV は遅くノイズがあり、公開順位とずれる | 中 | 表データは完結、それ以外は別 | 中（計算資源） | 長い（週単位から） |
| ハッカソン・作品 | 機械の検証器がない | 低い（課題設定から新規） | 完結しない（ユーザー・発表） | 中 | 短い〜中 |
| 対戦型・長期チーム戦 | 対戦場はノイズが大きく、メタで動く | 低い | 完結する（対戦場は手元） | 本番マップや相手に依存 | 長い（数か月に及ぶものがある） |

読み方は 3 通りある。検証器が速い形式（短時間のアルゴリズム、ヒューリスティック）では、評価器を先に立てると、AI の試行が選別され、効きが大きく出る。検証器が遅いか、ない形式（データ分析、ハッカソン）では、AI の出力を選ぶ基準を人が持つ。環境の制約が重い形式（性能改善、CTF）では、AI が見えない環境の状態を人が確かめる。検証器が目標を決める仕組みは、<!-- link:begin verifier-defines-problem#why -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 検証器に映ったものだけが目標になる](../eval/verifier-defines-problem.md#why)<!-- link:end --> で読める。

計算や API の費用は形式によって大きく違い、費用をかけた側が有利になる形式もある。参加の前に費用の上限を決めておくことを、戦略の一部として扱う。

## 短時間のアルゴリズム {#algorithm}

短時間のアルゴリズムは、オンライン（ABC・ARC・AGC、Codeforces）とオンサイト（ICPC、IOI、JOI）で規則が大きく違う形式である。例は調査の厚い AtCoder から多く取る。AtCoder の規則の細部と競技の練習法は、手本の kyopro-atlas の atcoder-system の ai-rules と practice-method を見る。

- **AI が効く**：練習での解説、別解の比較、テストケースの生成、弱点の分析。オンサイトでは、事前のライブラリの整備と検証、練習相手にも使う（根拠：中、版依存）。
- **人が握る**：本番の考察と実装のすべて。オンサイトでは、チーム内の分担と時間配分も人が決める。
- **評価器**：愚直解との比較で見る。作り方は <!-- link:begin evaluators-by-format#stress-test -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › 短時間のアルゴリズム：愚直解との比較](evaluators-by-format.md#stress-test)<!-- link:end --> にある。
- **規則と当日**：補完と AI 概要を確実に切る。事前に作ったライブラリを使うなら、出所を書けるようにする（<!-- link:begin disclosure-and-provenance#provenance -->[AI 利用の開示と出所の記録 › 出所を記録する](../safety/disclosure-and-provenance.md#provenance)<!-- link:end -->）。オンサイトは印刷物が最後の頼りで、AI 頼みの練習だけでは崩れる。

関連するページを 3 つ挙げる。

- 本番で AI を使えない大会に向けた練習の組み方：<!-- link:begin practice-vs-contest-day#what-to-ask-in-practice -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 練習で AI に頼むこと](practice-vs-contest-day.md#what-to-ask-in-practice)<!-- link:end -->
- 本番の条件で自力を確かめる方法：<!-- link:begin practice-vs-contest-day#test-under-contest-conditions -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 本番の条件で自力を確かめる](practice-vs-contest-day.md#test-under-contest-conditions)<!-- link:end -->
- 問題文の読み方：<!-- link:begin read-specs-yourself#read-first -->[仕様を自分で読み、AI に誤読を指摘させる › 先に自分で読んで要約する](../recipes/read-specs-yourself.md#read-first)<!-- link:end -->

## ヒューリスティック（短期・長期） {#heuristic}

ヒューリスティックは、スコアを競う最適化の形式で、短期（数時間）と長期（日単位）を分けて考える。AtCoder の AHC（Heuristic Contest）が例である。

- **AI が効く（短期）**：練習でのテスタや可視化の作成。本番は補完程度にとどまる大会がある（根拠：中、版依存）。
- **AI が効く（長期）**：ローカル評価での並列実験、実装、高速化、パラメータ探索。大量の試行を局所評価で選別する勝ち方の構造は <!-- link:begin ai-in-contests-today#how-ai-wins -->[AI はコンテストでどこまで来たか（確認日付き） › 勝ち方の構造（大量の試行と局所評価による選別）](ai-in-contests-today.md#how-ai-wins)<!-- link:end --> にある。
- **人が握る**：問題の本質の考察、評価関数、新しい方針、時間配分、ループから抜ける判断。先に自分の案を書き、AI には問い・反論・観察の道具を頼む順序は <!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end --> にある。
- **評価器**：公式とスコアが一致するテスタ。作り方は <!-- link:begin evaluators-by-format#tester -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › ヒューリスティック：公式とスコアが一致するテスタ](evaluators-by-format.md#tester)<!-- link:end --> にある。
- **規則と当日**：長期には、AI を使う部門と使わない部門を分ける回がある。部門の有無と版は <!-- link:begin competition-rules#rules-by-type -->[大会の規則の早見（禁止・部門分け・許可と開示） › 類型ごとの大会（確認日付き）](competition-rules.md#rules-by-type)<!-- link:end --> の表で確かめ、初回提出の前に部門を選ぶ。ログを残し、費用の上限を決める。短期は補完ツールが指定のリストにあるか確かめる。

AI に書かせた探索コードの点検は <!-- link:begin search-code-checklist#search-code -->探索コードと高速化の点検表（AI に書かせたとき） › 探索コードの点検の観点（準備中）<!-- link:end --> にある。ケース数・集計・勝率に要る試合数は <!-- link:begin running-contest-experiments#more-cases -->[実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › ぶれるならケースを増やす](running-contest-experiments.md#more-cases)<!-- link:end --> にある。観察の道具を作らせる使い方は <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end --> にある。

## 性能改善 {#performance-tuning}

性能改善は、ISUCON のように、動くアプリケーションを当日の計測で速くする形式である。環境が重く、AI の効きは序盤で大きく、中盤以降は頭打ちになる傾向がある（根拠：中、個別事例）。

- **AI が効く**：定番の初手（インデックス、N+1、キャッシュ）、計装、コードの全体把握。
- **人が握る**：中盤以降の計測の解釈、ボトルネックの見極め、仕様上のトレードオフ。
- **評価器**：ベンチマーカー。計装の入れ方は <!-- link:begin evaluators-by-format#benchmarker -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › 性能改善：ベンチマーカーと計装](evaluators-by-format.md#benchmarker)<!-- link:end --> にある。
- **規則と当日**：レギュレーションの AI の項目と、当日のマニュアルの優先を確かめる。再起動試験、データの永続化、最終計測前の計装の除去、終盤の変更の凍結に注意する。

頼み方は、プロファイルを先に取り、出力の一致と複数回の実測を証拠に求める。手順は <!-- link:begin performance-tuning#profile-first -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › プロファイルを先に取る](../recipes/performance-tuning.md#profile-first)<!-- link:end --> と <!-- link:begin performance-tuning#too-good-speedups -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › 良すぎる速度向上を疑う](../recipes/performance-tuning.md#too-good-speedups)<!-- link:end --> にある。当日の運用は <!-- link:begin competition-day-operations#endgame -->[本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › 終盤：凍結と最終確認](competition-day-operations.md#endgame)<!-- link:end --> にある。

## CTF {#ctf}

CTF は、セキュリティの問題を解いて flag を提出する形式である。ここでは攻撃の手口は扱わず、AI の効き方と人の受け持ちだけを書く。

- **AI が効く**：易〜中難度の暗号・Web・pwn の問題、序盤の速さ、並列化（根拠：中、版依存）。
- **人が握る**：新規性の高い問題、OSINT、推測型の問題、実行時の状態、長時間の一貫性。外部サーバとのやりとりが多い問題と、特定の環境が要る問題は、AI が落としやすい。
- **評価器**：flag の検証。提出の前に、flag が正しい形で出ているかを確かめる。方法は <!-- link:begin evaluators-by-format#flag -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › CTF：提出の前の flag の検証](evaluators-by-format.md#flag)<!-- link:end --> にある。
- **規則と当日**：誤答のペナルティと、AI の扱い、区分の選択を確かめる。問題に仕込まれた指示への扱いは <!-- link:begin instructions-hidden-in-materials#two-kinds -->[課題資料・問題文に仕込まれた指示 › 仕込まれる指示の二つの型（攻撃と、利用の規則の合図）](../safety/instructions-hidden-in-materials.md#two-kinds)<!-- link:end --> にある。

提出の段の運用は <!-- link:begin competition-day-operations#submission -->[本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › 提出：人が確かめる](competition-day-operations.md#submission)<!-- link:end --> が持つ。

## データ分析 {#data-analysis}

データ分析は、Kaggle や SIGNATE のように、データから予測や分析の精度を競う形式である。評価の手元の指標と、本番の順位のずれが主な難所である。

- **AI が効く**：パイプラインの作成、EDA、実験の量産、先行解の調査、アンサンブル（根拠：中、版依存）。
- **人が握る**：CV の設計、リークの検出、データの目視からの洞察、最終提出の選択。
- **評価器**：分布の差を確かめた CV。作り方は <!-- link:begin evaluators-by-format#cv -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › データ分析：分布の差を確かめた CV](evaluators-by-format.md#cv)<!-- link:end --> にある。
- **規則と当日**：データを外部の AI に送ってよいかを確かめる。判断は <!-- link:begin entrusted-data#whose-data -->[預かったデータ・規約付きのデータを AI に渡してよいか › 誰のデータで、何が決まっているか](../safety/entrusted-data.md#whose-data)<!-- link:end --> にある。コードコンペは推論の実行がオフラインになる。

実験の集計と勝率の判定は <!-- link:begin running-contest-experiments#aggregation -->[実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › 集計の方法を選ぶ（相対スコア）](running-contest-experiments.md#aggregation)<!-- link:end --> にある。

## ハッカソン・作品 {#hackathon}

ハッカソン・作品コンテストは、期間内に作品を作り、説明と発表で評価される形式である。機械の評価器がなく、人の評価が結果を決める。

- **AI が効く**：試作の速さと、実装の幅（根拠：中、版依存）。
- **人が握る**：課題設定、ユーザーにとっての価値、説明と発表。
- **評価器**：機械の評価器がない。代わりに何を基準にするかは <!-- link:begin evaluators-by-format#no-mechanical-evaluator -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › ハッカソン：機械の評価器がないとき](evaluators-by-format.md#no-mechanical-evaluator)<!-- link:end --> にある。
- **規則と当日**：AI を使った箇所の説明や開示の求めを、募集要項で確かめる。使った箇所を記録して開示し、デッドコードや保守性での減点に注意する。記録は <!-- link:begin disclosure-and-provenance#four-points -->[AI 利用の開示と出所の記録 › 開示・相談・出所・意図の四つの観点](../safety/disclosure-and-provenance.md#four-points)<!-- link:end --> にある。

AI の案が他の参加者と似通う点は <!-- link:begin ai-ideas-are-everyones#outputs-converge -->[AI の案は「みんなの案」（均質化） › AI を使った成果どうしは似る](../judgment/ai-ideas-are-everyones.md#outputs-converge)<!-- link:end --> にある。差が要る場面では、AI の案を「ほかの人も得ている案」として扱い、上積みを自分で考える。

## 対戦型・長期チーム戦 {#battle-and-team}

対戦型は、ボットや AI を作って他のチームのものと戦わせる形式で、長期チーム戦は、数か月にわたるチームの大会である。この 2 つは直接の研究がなく、隣接する形式からの類推で書いている（類推）。

- **AI が効く**：経路探索・通信・補助関数の初版、ローカルの対戦場、基準ボット。長期チーム戦では、評価環境の周辺作業、実装、集計、文書化（類推）。
- **人が握る**：戦略とメタの読み、直接対決での強さ、本番マップへの頑健性。長期チーム戦では、評価の定義、撤退の判断、チームの合意、本番環境への対応。
- **評価器**：対戦場と基準のボット。作り方は <!-- link:begin evaluators-by-format#arena -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › 対戦型：対戦場と基準のボット](evaluators-by-format.md#arena)<!-- link:end --> にある。
- **規則と当日**：要項と行動規範を読み、不明点は運営に確かめて記録する。直前の大きな変更を避け、戻せるようにする。

採否は旧版と他のチームの両方を相手に決める。この進め方と役割の分け方は <!-- link:begin long-team-competitions#adoption -->チーム戦の運用（長期・対戦型） › 採否は旧版とほかのチームの両方で決める（準備中）<!-- link:end --> と <!-- link:begin long-team-competitions#roles -->チーム戦の運用（長期・対戦型） › 役割を分ける（準備中）<!-- link:end --> にある。凍結とリハーサルは <!-- link:begin long-team-competitions#freeze-and-rehearse -->チーム戦の運用（長期・対戦型） › 凍結とリハーサル（準備中）<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [そのタスクは AI に向いているか（五つの軸）](../delegate/is-the-task-ai-suited.md)

**関連**

- [AI はコンテストでどこまで来たか（確認日付き）](ai-in-contests-today.md)
- [大会の規則の早見（禁止・部門分け・許可と開示）](competition-rules.md)
- [練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）](practice-vs-contest-day.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](evaluators-by-format.md)
- [本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）](competition-day-operations.md)
- [実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）](running-contest-experiments.md)
- 探索コードと高速化の点検表（AI に書かせたとき）（準備中）
- チーム戦の運用（長期・対戦型）（準備中）
- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [学校・組織・コンテストの規則（類型と確認表）](../safety/checking-ai-rules.md)
- [仕様を自分で読み、AI に誤読を指摘させる](../recipes/read-specs-yourself.md)
- [観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)
- [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [課題資料・問題文に仕込まれた指示](../safety/instructions-hidden-in-materials.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)
- [性能改善を頼む（プロファイルが先・出力の一致と実測）](../recipes/performance-tuning.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
