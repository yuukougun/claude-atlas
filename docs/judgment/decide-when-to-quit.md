---
id: decide-when-to-quit
title: やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）
nav_title: やめどきを先に決める
aliases: [サンクコスト, 損切りの判断, 撤退の判断]
type: judgment
field: judgment
chapter: 落とし穴ごとの対策
order: 50
level: 任せる
priority: 必須
surfaces: [app, claude-code]
principle: [握る]
prevents: []
pitfalls: [やめられない]
scenes: [開発, コンテスト, チーム]
summary: 費やした分だけ方針を捨てにくくなる傾向に対し、やめる基準を着手前に書き、作った本人以外が判定して守る方法が分かる。
signs:
  - {type: symptom, text: ここまで作ったので、今さら方針を変えられない}
  - {type: goal, text: 頭打ちになった方針を、続けるかやめるか決めたい}
  - {type: goal, text: Claude の「もう打ち手がない」を、やめる根拠にしてよいか判断したい}
wave: 1
prerequisites: [human-pitfalls]
related: [experiment-log, lockbox-and-holdout, when-to-start-fresh, wont-rethink-approach, going-in-circles, what-not-to-delegate, open-ended-loop-trap, selection-pressure, keep-failure-lessons, separate-roles, agreement-is-not-evidence, running-contest-experiments, competition-day-operations, long-team-competitions]
tracks: []
outdated_advice: []
sources: [sleesman-2012-escalation-commitment, github-official-stockfish-fishtest, kiri8128-ahc-without-annealing, speakerdeck-shun-duan-qi-ahcdesheng, schulman-opinionated-guide-ml-research, qiita-ktdatascience-cad6d1, speakerdeck-chihironakayama-agentshi-dai-nokagglede, lukyanenko-rogii-geosteering-kaggle]
volatility: 低
sections:
  - {title: なぜやめられなくなるか, anchor: why-escalation}
  - {title: 基準を着手前に書く, anchor: write-criteria-first}
  - {title: 判定を作った本人から離す, anchor: separate-the-judge}
  - {title: 頭打ちは方針を疑う合図, anchor: plateau}
  - {title: 変えすぎも失敗, anchor: dont-switch-too-often}
  - {title: AI の「やめよう」「続けよう」を再検証する, anchor: ai-advice-on-quitting}
  - {title: 判断例, anchor: decision-examples}
  - {title: 人が握るもの, anchor: what-you-hold}
  - {title: 確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：費やした分だけ方針を捨てにくくなる傾向に対し、やめる基準を着手前に書き、作った本人以外が判定して守る方法が分かる。
    - **いつ引くか**：ここまで作ったので今さら方針を変えられないとき。頭打ちの方針を続けるか迷うとき。Claude の「もう打ち手がない」を根拠にやめてよいか判断したいとき。
    - **前提**：<!-- link:begin human-pitfalls -->[人の側の五つの落とし穴（総論）](human-pitfalls.md)<!-- link:end -->
    - **根拠の強さ**：人が失敗しかけた方針に固執する要因は、メタ分析で確かめられている（根拠：強）。AI の速さと迎合が固執を強める筋は推論で、研究も実践例もない。

<!-- textlint-disable -->
別名：サンクコスト・損切りの判断・撤退の判断
<!-- textlint-enable -->

やめどきを先に決めるとは、着手する前にやめる基準・期日・判定者を書いておくことである。期日には、作った本人以外が基準と照らして、続けるかやめるかを決める。結果を見てからでは、費やした分に判断が引かれる。この決まりは、方針の単位の判断が後回しになるのを防ぐ守りになる。

## なぜやめられなくなるか {#why-escalation}

失敗しかけた方針に固執する傾向は、人の側の仕組みとして確かめられている。2012 年のメタ分析（Academy of Management Journal）は、166 の独立な標本をまとめ、固執を強める要因を示した。時間の投資（ρ=.432）、エゴへの脅威（.473）、完成への近さ（.393）、初期の決定への個人の責任（.258）である。実験室と実地、学生と管理職の研究を含む（根拠：強。組織の意思決定の領域）。

この 4 つは、AI と作るときの場面に重ねて読める。

- **時間の投資**：すでに作った量が、続ける理由に化ける。
- **エゴへの脅威**：自分が選んだ方針をやめると、判断の誤りを認めることになる。
- **完成への近さ**：「あと少しで動く」という感覚が、やめる決断を遅らせる。
- **個人の責任**：最初に方針を決めた人ほど、その方針をやめにくい。

ここまでの重ね読みは、組織の研究を AI 作業の場面に当てはめたもので、類推である。

さらに、AI の速さは「もうすぐ完成する」という感覚を早め、AI の迎合が方針への疑いを弱める、という筋が考えられる。一人で長期に開発すると、4 つの要因が一人に集まるという筋もある。どちらも直接調べた研究はなく、実践例もない（推論・実践例なし）。このページの中心は、この推論ではなく、着手前の基準と、判定を作った本人から離すことである。

会話の単位の撤退（訂正を 2 回重ねても直らなければ新しい会話にする）は、<!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end -->が扱う。このページが扱うのは、数日から数か月かけて育てる方針の単位の撤退である。

## 基準を着手前に書く {#write-criteria-first}

方針ごとに、着手する前に、撤退の基準を数値と日付で書き、登録日付きで台帳に残す。結果が出たあとに基準を決めると、費やした分に基準のほうが引き寄せられるからである。この理由は筋の通った推論であり、仮説を先に書く台帳の考え方と同じ向きにある（推論・実践例なし）。実験 1 件の台帳は<!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](../eval/experiment-log.md#hypothesis-first)<!-- link:end -->が扱い、このページは方針の単位の台帳を扱う。

書く項目は 5 つである。

- **方針と期日**：何をいつまでに試すか。
- **撤退の基準**：期日の時点で何が出なければやめるか。数値と日付で書く。
- **判定者**：誰が期日に判定するか。実装者以外にする（次の節）。
- **同じアイデアの再試行の上限**：変種を含めて何回までか。
- **見直しの合図**：改善幅が誤差以内の変更が何回続いたら、調整をやめて方針を見直すか。

例を挙げる。「期日までに、基準ボット群に対するロックボックスでの勝率が 0.60 未満なら撤退する」「同じアイデアの再試行は 4 回まで」。0.60 や 4 回に根拠はなく、例である。ロックボックスは、人だけが持つ検証用データで、<!-- link:begin lockbox-and-holdout#keep-out-of-reach -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 読めない所に置く](../eval/lockbox-and-holdout.md#keep-out-of-reach)<!-- link:end -->が置き方を扱う。

4 回は、Stockfish の検定基盤 Fishtest の FAQ にある目安を借りた例である。FAQ は同じアイデアの再挑戦を「おおむね 4〜5 回が上限」とし、変更を試すことと、運のよい試行を通しすぎないことの釣り合いを理由にする。チェスエンジンの検定の慣行で、一般の規則ではない（根拠：弱。経験則）。再挑戦に上限を置く理由は、<!-- link:begin selection-pressure#retry-cap -->[選択圧：良かった版を選び続ける罠 › 同じアイデアの再挑戦に上限を置く](../eval/selection-pressure.md#retry-cap)<!-- link:end -->が扱う。

基準を書く前の見積もりも、同じ向きの手になる。実装の前に概算でスコアを見積もり、届かない見込みの方針には着手しない。「期待改善量 ÷ 実装時間」で優先順位を付ける実践者もいる（根拠：弱。コンテストの個人の記事）。業務では「期待効果 ÷ 工数」と読み替えられる。

撤退したときは、「何が分かったか」を台帳に残し、次の方針の禁止事項にする。何を残し、何を捨てるかは<!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](../context/keep-failure-lessons.md#what-to-keep)<!-- link:end -->が扱う。

雛形は次のとおりである。動作は確かめていない。

<!-- gen:begin snippet decide-when-to-quit/exit-criteria -->
<!-- textlint-disable -->

??? example "雛形：撤退基準の登録（方針・期日・基準・判定者・再試行の上限を、着手前に登録日付きで書く）"

    ```markdown
    ## POL-003 評価関数を学習済みの重みに置き換える方針

    - 登録日：2026-12-01（例）。この日のあとは、基準・期日・判定者を書き換えない
    - 方針：評価関数の手書きの重みをやめ、自己対戦の記録から学習した重みに置き換える
    - 着手する理由（着手前の見積もり）：実装の前に概算した。手書きの重みの頭打ちが勝率 0.55 前後で、学習で 0.60 を超える見込みがある（見積もりの根拠は別紙に書く）
    - 期日：2026-12-15（例）
    - 撤退の基準（数値と日付で書く。値は例）：期日の時点で、基準ボット群に対するロックボックスでの勝率（400 試合）が 0.60 未満なら撤退する
    - 判定者：評価担当（実装者以外）。個人で進めるときは、この欄の基準に機械的に従う。期日に基準を読み直して解釈を変えない
    - 同じアイデアの再試行の上限：変種を含めて 4 回まで（例。Fishtest の目安 4〜5 回を借りた）
    - 見直しの合図：改善幅が誤差以内の変更が続いたら、重みの調整をやめて、人が方針を見直す。続く回数はここに決めて書く（例：3 回連続）
    - AI に頼んでよいこと：測定の実行、結果の表の作成。続ける・やめる・作り直すの決定は頼まない

    ### 期日の判定（判定者が、期日に書く）

    - 判定日：
    - 測定の記録（実験の ID）：
    - 結果：基準を満たした／満たさなかった
    - 決定：続ける／やめる／作り直す（作り直すなら、新しい方針として新しい登録を起こす）
    - 何が分かったか（やめたときも書く。次の方針の禁止事項にする）：
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet decide-when-to-quit/exit-criteria -->

## 判定を作った本人から離す {#separate-the-judge}

撤退の判定は、実装者以外が下す。チームでは、評価担当が判定する。個人で進めるときは、事前に書いた基準へ機械的に従うことで代える。

作った本人が判定すると、固執の要因が判定に入り込む。メタ分析では、初期の決定への個人の責任（最初に方針を決めた人ほどやめにくい）が固執を強めていた。判定者を分ければ、その要因を判定から外せる。ただし、判定者を分けて固執が減るかを直接調べた資料は、この辞典の材料にはない（推論・実践例なし）。

判定者の置き方は、次のとおりである。

- **判定の測定は、実装者が触れない所に置く**：開発用の入力で測ると、実装者が合わせ込める。人だけが持つ検証用データ（ロックボックス）で測る。
- **続ける・やめる・作り直すの決定は、人が持つ**：AI に測定の実行や表の作成は任せてよい。決定は任せない。撤退は、どの段階でも人が握るものである。分け方は<!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end -->が扱う。
- **AI の賛成を判定の根拠に数えない**：AI が「この方針は有望です」と答えても、基準を満たした証拠にはならない。何を証拠に数えるかは<!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](agreement-is-not-evidence.md#what-counts)<!-- link:end -->が扱う。
- **戦略の改善を AI に回し続けさせて、やめどきも AI に決めさせる運用はしない**：開いたループが過適合を進める理由は<!-- link:begin open-ended-loop-trap#closed-vs-open -->[AI に改善を回させ続ける罠（開いたループ） › 閉じた反復と開いたループ](../delegate/open-ended-loop-trap.md#closed-vs-open)<!-- link:end -->が扱う。

チームの役割の分け方は<!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)<!-- link:end -->が、長期のチーム戦での置き方は<!-- link:begin long-team-competitions#roles -->チーム戦の運用（長期・対戦型） › 役割を分ける（準備中）<!-- link:end -->が扱う。

## 頭打ちは方針を疑う合図 {#plateau}

小さな改善が頭打ちになったら、パラメータの調整をやめて、方針そのものを見直す合図と読む。業務でも、同じ方向の微修正が効かなくなったら方針を疑う、と一般化できる。コンテストの実践者の経験則が出どころで、一部はコンテスト固有である（根拠：弱）。

見直しの合図は、「改善幅が誤差以内の変更が N 回続く」という基準で動かす。着手前に書く項目の 1 つである。N の値に決まりはないので、自分の場面で決めて書く。誤差以内かどうかは、ぶれの幅を測らないと言えない。ぶれを見込んだケース数と試合数の決め方は<!-- link:begin running-contest-experiments#games-for-win-rate -->実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › 勝率に要る試合数（準備中）<!-- link:end -->が扱う。

見直しの場では、次の 3 つを選ぶ。

- 続ける：基準を満たしていて、伸びが続いている。
- やめる：基準を満たさず、伸びる見込みの根拠がない。
- 作り直す：方針の核は残し、別の手法や別の分解に替える。新しい方針として、基準・期日・判定者を登録し直す。

外の測りで方針の当たり外れを早く読む手もある。開始の早い段階で単純な版を提出して順位表を見る、という実践者がいる。順位が悪ければ方針を変え、焼きなましから貪欲法、ビームサーチへと切り替えて好成績につなげた例がある（根拠：弱。単独の経験談）。本番の中盤での頭打ちの見方は<!-- link:begin competition-day-operations#midgame -->本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › 中盤：頭打ちとループを見る（準備中）<!-- link:end -->が扱う。

Claude がエラーを直し続けて方針を疑わないときの診断は、<!-- link:begin wont-rethink-approach#diagnosis -->[直し続けて方針を疑わない（またはすぐ撤退を勧める） › 原因を安く確かめる順](../symptoms/wont-rethink-approach.md#diagnosis)<!-- link:end -->が扱う。

## 変えすぎも失敗 {#dont-switch-too-often}

撤退基準は、早くやめるためだけでなく、むやみに変えないためにも使う。研究者の一人は、粘りすぎるより、問題を頻繁に変えすぎる（有望な案を捨てる）失敗のほうが多い、と助言している。一人の研究者の経験による助言で、実験的な研究の領域の話である（根拠：弱）。

変えすぎを防ぐには、基準の使い方を 2 つ守る。

- **基準を満たしている間は、方針を乗り換えない**：別の案が魅力的に見えても、いまの方針の期日までは、基準で判定する。乗り換えたくなったら、新しい案を新しい方針として登録し、基準・期日・判定者を決める。
- **記録を定期的に見返す**：アイデアと実験の記録を付け、決まった間隔で見返す習慣も、同じ研究者が勧めている。乗り換えの理由が、基準でなく気分になっていないかを、見返すときに確かめる。

固執と変えすぎは、逆向きの失敗に見える。しかし、どちらも「その時点の感覚で決める」ことが原因なので、同じ道具（先に書いた基準と、別の判定者）で防げる。これは推論である（推論・実践例なし）。

## AI の「やめよう」「続けよう」を再検証する {#ai-advice-on-quitting}

Claude の撤退の勧めにも、続行の勧めにも、そのまま従わない。どちらも、本番の条件で再検証するまでは根拠に採用しない。

実践者から、次の報告がある。いずれも単独の報告で、モデルと世代は確かめられていない。版によって変わる可能性がある（根拠：弱）。

- **直し続けて方針を疑わない**：Claude がエラーを直し続けたが、方針そのものの妥当性は疑わなかったという報告がある。
- **会話が長くなると撤退を勧める**：会話が長くなると、Claude が撤退を勧めがちだったという報告がある。
- **安い試行で棄却し、早々に頭打ちを宣言する**：本番と似ていない安い試行でアイデアを棄却し、スコアが頭打ちだと早く宣言したという報告がある。

再検証は、次の順に行う。

1. Claude が撤退を勧める根拠の試行を確かめる。本番と似た入力・似た規模・似た評価で測ったものか。
2. 似ていなければ、本番に近い条件で、同じ試行をやり直す。
3. 結果を、着手前に書いた基準と期日に照らす。決めるのは判定者である。

続行の勧めも同様に扱う。「もう少し直せば通ります」という勧めは、完成への近さの感覚を強める。期日が来ていれば、勧めの強さを問わず、基準で判定する。

会話が長くなったあとの撤退の勧めは、会話そのものが原因のこともある。新しい会話で同じ問いを聞き直す手は、<!-- link:begin when-to-start-fresh#what-it-prevents -->[新しい会話を始めるタイミング › 何に効くか（見せる・散らかっている・やめられない）](../context/when-to-start-fresh.md#what-it-prevents)<!-- link:end -->が扱う。

## 判断例 {#decision-examples}

!!! example "判断例：期日に基準を 0.03 下回り、実装者は「あと少し」と言う"
    - **状況**：対戦型の大会で、評価関数の方針を「期日までにロックボックスでの勝率が 0.60 未満なら撤退」と着手前に登録した。期日の測定は 0.57 だった。実装者は「直近の変更で 0.50 から 0.57 まで伸びている。あと少しだ」と言う。
    - **迷う候補**：期日を延長して続ける。または、基準どおり撤退する。
    - **選んだもの**：判定者が基準どおり撤退と決める。延長したい案は、新しい方針として、新しい基準・期日・判定者を登録して別に起こす。
    - **理由**：伸びが続いているので、延長にも筋が通る。しかし「あと少し」は完成への近さであり、固執を強める要因の 1 つである。延長を実装者が言い出す形では、基準が期日の後で動く。400 試合の勝率は誤差が ±0.05 ほどあり、0.57 と 0.60 の差は誤差の範囲に入る。その扱いは基準を書く時点で決めておくことで、期日の後に動かさない。次の登録には、誤差の扱いを書く。

!!! example "判断例：Claude が「もう打ち手がありません」と言う"
    - **状況**：長い会話の末に、Claude が「この方針は頭打ちで、もう打ち手がありません。撤退を勧めます」と答えた。根拠は、開発用の小さな入力での数回の試行である。期日の判定はまだ先にある。
    - **迷う候補**：Claude の勧めに従い、方針をやめる。または、勧めを無視して期日まで続ける。
    - **選んだもの**：どちらもまだ決めない。本番に近い入力と評価で同じ試行をやり直す。結果は先に書いた基準と照らし、判定者が決める。
    - **理由**：Claude が見た試行は、本番と似ていない安い試行だった。報告では、こうした試行で棄却されることがある。勧めに従えば、拾える方針を捨てる。無視して続ければ、固執になる。測り直しは、どちらの失敗も避ける。

## 人が握るもの {#what-you-hold}

AI にどれだけ任せても、方針の単位では次の 3 つを人が握る。

- **基準を書くこと**：着手前に、基準・期日・判定者・再試行の上限・見直しの合図を決める。
- **続ける・やめる・作り直すの決定**：判定者の人が下す。決めたら、根拠を一文で書く。その一文に AI の賛成が入っていれば、実行や計測の結果に置き換える。
- **撤退の記録**：何が分かったかを残し、次の方針の禁止事項にする。

任せてよいのは、測定の実行、結果の表の作成、台帳の整形である。任せてよいものの分け方は<!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](../delegate/what-not-to-delegate.md#verifiable-axis)<!-- link:end -->が扱う。

この決まりが効かない場面もある。数時間で終わる作業では、台帳を作る手間のほうが大きい。基準を書けないほど探索の初期なら、方針ではなく探索である。期日だけを先に決め、基準は期日までに書く手もある。この扱いは推論である（推論・実践例なし）。

## 確かめ方 {#how-to-check}

この決まりが守れているかは、記録を付けて測る。次を確かめる。

- 着手前に、方針・期日・基準・判定者・再試行の上限が、登録日付きで書かれているか。
- 期日の判定が、書いた基準のとおりか。基準が期日の後に書き換わっていないか。台帳の履歴で見る。
- 判定者が実装者以外か。個人なら、判定が基準への機械的な適用になっているか。
- 撤退・延長・乗り換えの件数と理由を記録し、決まった間隔で見返しているか。撤退が多すぎれば基準が厳しすぎ、延長ばかりなら基準が守られていない。
- Claude の撤退・続行の勧めを、本番に近い条件で再検証してから使ったか。

数値の例は、自分の場面の誤差と規模で置き換える。件数が少ないうちは、傾向として読む。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Cleaning Up the Big Muddy: A Meta-Analytic Review of the Determinants of Escalation of Commitment](https://gwern.net/doc/psychology/cognitive-bias/sunk-cost/2012-sleesman.pdf)：gwern.net（論文の写し）・英語・確認日 2026-11-04
- [Fishtest FAQ](https://github.com/official-stockfish/fishtest/wiki/Fishtest-faq)：GitHub（official-stockfish）・英語・確認日 2026-11-04
- [焼きなまし法が使えなくても AHC 橙になれたよ](https://kiri8128.hatenablog.com/entry/2023/11/29/024335)：Kiri8128・確認日 2026-11-04
- [短期AHCで勝つためのテクニック](https://speakerdeck.com/shun_pi/duan-qi-ahcdesheng-tutamenotekunituku)：Speaker Deck（shun\_pi）・確認日 2026-11-04
- [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html)：John Schulman（個人のブログ）・英語・確認日 2026-11-04
- [【kaggle】Claude CodeだけでKaggleコンペに挑んで惨敗した話](https://qiita.com/ktdatascience/items/cad6d18c080aa6ca812c)：Qiita（ktdatascience）・確認日 2026-11-04
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22)：Speaker Deck（chihironakayama）・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [人の側の五つの落とし穴（総論）](human-pitfalls.md)

**次に読む**

- [役割を分ける（書く人・承認する人・疑う人）](../team/separate-roles.md)

**関連**

- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [AI に改善を回させ続ける罠（開いたループ）](../delegate/open-ended-loop-trap.md)
- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- [失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](agreement-is-not-evidence.md)
- 実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）（準備中）
- 本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）（準備中）
- チーム戦の運用（長期・対戦型）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
