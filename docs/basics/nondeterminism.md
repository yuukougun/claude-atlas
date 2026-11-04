---
id: nondeterminism
title: 同じ質問でも答えが変わる（非決定性）
nav_title: 同じ質問でも答えが変わる
aliases: [非決定性, ばらつき, 再現性, 毎回答えが違う]
type: concept
field: basics
chapter: 答えの確かさ
order: 130
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
summary: 同じ頼み方でも答えが毎回少し変わるので、一回の結果で良し悪しを決められないことが分かる。答えのばらつきは不確かさの合図になり、何回か試して比べる理由になる。
signs:
  - {type: goal, text: 同じ頼み方でも答えが毎回変わる理由を知りたい}
  - {type: goal, text: 一回うまくいった頼み方を信じてよいか判断したい}
prerequisites: []
related: [fact-checking, measure-changes, felt-vs-measured, why-hallucinations, refine-in-conversation]
outdated_advice: [lower-temperature]
sections:
  - {anchor: what-happens, title: 何が起きるか}
  - {anchor: why, title: なぜ答えが変わるか}
  - {anchor: what-helps, title: 何に効くか}
  - {anchor: temperature-advice, title: temperature を下げる助言は今は使えない}
  - {anchor: misconceptions, title: よくある誤解}
sources: [anthropic-research-infrastructure-noise]
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：同じ頼み方でも答えは毎回少し変わるので、1 回の結果では良し悪しを決められない。ばらつきは不確かさの合図になる。
    - **いつ引くか**：同じ頼み方でも答えが毎回変わる理由を知りたいとき。1 回うまくいった頼み方を信じてよいか判断したいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：非決定性・ばらつき・再現性・毎回答えが違う
<!-- textlint-enable -->

同じ質問でも答えが変わる現象を、非決定性と呼ぶ。Claude に同じ依頼を出し直すと、言い回しだけでなく、結論や手順が変わることがある。このページは、その変わり方を前提にして、1 回の結果をどこまで信じるかを決める考え方を示す。

## 何が起きるか {#what-happens}

同じ依頼を、同じ条件で 3 回出すと、3 回とも少しずつ違う答えが返る。違いは言い回しの揺れで済むこともあれば、結論そのものが入れ替わることもある。たとえば「この関数のバグを指摘して」と 3 回頼むと、毎回同じ箇所を挙げる回もあれば、1 回だけ別の箇所を挙げる回もある。この例は起きることのイメージであり、実際の出力の記録ではない。

次の判断例は、この性質を前提に、1 回の結果をどう扱うかを示す。

!!! example "判断例：1 回うまくいった頼み方を採用してよいか"
    - **状況**：コードレビューの依頼文を直して 1 回試したところ、狙いどおりの指摘が返ってきた。
    - **迷う候補**：その依頼文をすぐチームの標準にする。同じ依頼文をあと数回出して、指摘が安定するかを見てから決める。
    - **選んだもの**：あと数回出して、指摘が安定するかを見てから決める。
    - **理由**：1 回の成功は、依頼文が良かった場合と、たまたま良い答えが出た場合を区別できない。数回出して毎回狙いに近ければ依頼文のおかげと考えやすく、毎回ばらつくならまだ決められない。

ばらつきの大きさ自体も情報になる。毎回同じ結論が返る問いは、迷いが小さい問いと見る目安になる（推論・実践例なし）。毎回結論が割れる問いは、情報が足りないか、問いが曖昧か、答えが元から割れる問いである。割れ方を見ることが、不確かさの合図を読むことになる。

## なぜ答えが変わるか {#why}

Claude は答えを一度に確定させて取り出すのではなく、語のかけら（トークン）を順に選んで文章を作る。選び方に幅があるので、同じ依頼でも途中の選択が分かれ、分かれた先は別の文章になる。たとえるなら、同じレシピを渡しても毎回少し味が違う料理人である。1 回の皿で腕を判断せず、何度か作らせて比べる。

この仕組みの細部には、公開された資料で確かめられていないものがある。たとえば、出力の揺れを抑える設定をしても結果が完全には揃わない理由は、このページでは確かめていない。このページは、その理由には頼らない。確かなのは、起きる現象のほうである。同じ依頼で答えが変わることを、使う側の前提にしておけばよい。

答えが変わる原因には、Claude の側の揺れのほかに、こちらの条件の違いもある。会話の履歴、読み込まれるファイル、実行環境の違いは、依頼文が同じでも結果を動かす。実行環境の資源の設定だけで、コーディングのベンチマーク（Terminal-Bench 2.0）の結果が 6 ポイント動いた、という Anthropic の研究がある（根拠：中。2026 年の報告、1 つのベンチマークでの結果）。手元の比べ方でも、条件を揃えないと、差が頼み方の差なのか環境の差なのか分からなくなる。

## 何に効くか {#what-helps}

このページの考え方が効く原理は「確かめる」で、防ぐ原因は「確かめていない」である。1 回の結果を、確かめないまま信じる状態を避ける。

- **1 回で決めない**：頼み方の良し悪しや、変更が効いたかどうかは、複数回の結果を並べて決める。回数と差の大きさの目安は <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> で扱う。小さく比べる手順は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。
- **ばらつきを合図にする**：答えが毎回割れるなら、事実や前提の不足を疑う。割れる所を、根拠を確かめる場所の目印にする。重要な事実の確かめ方は <!-- link:begin fact-checking#best-of-n -->[事実を確かめる（引用・照合・best-of-N） › 何度か聞いて比べる（best-of-N）](../verify/fact-checking.md#best-of-n)<!-- link:end --> から始める。
- **体感で決めない**：「最近よくなった」「悪くなった」という感覚は、ばらつきを取り違えて生まれることがある。同じ物差しの記録で見る理由は <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end --> で扱う。
- **ずれたら頼み方を直す**：ばらつきを理由に、会話の中で訂正を積むと、前の答えが文脈に残る。依頼を直して出し直す考え方は <!-- link:begin refine-in-conversation#edit-the-request -->[頼み方は一回で決めない（会話で詰める） › 訂正を重ねるより依頼を直す](../prompting/refine-in-conversation.md#edit-the-request)<!-- link:end --> にある。

比べるときの出し直し方は、面で少し違う。

=== "アプリ"
    新しい会話を開いて、同じ依頼を出し直す。同じ会話の中で聞き直すと、前の答えが文脈に残り、独立した試行にならない。

=== "Claude Code"
    新しいセッションで、同じ依頼を出し直す。読み込まれるファイルや CLAUDE.md の内容を揃えてから比べる。IDE 拡張や WSL・Linux 以外の OS での動作は未確認。

=== "API"
    同じ要求を、条件を揃えて複数回送る。モデルの指定、system プロンプト、メッセージを揃える。結果は 1 件ずつ記録して並べる。

## temperature を下げる助言は今は使えない {#temperature-advice}

以前は、出力を安定させる手として temperature を下げる助言があった。この助言は撤回されており、今のモデルではそもそも指定できない。何を使い、どの版からどうなったかは <!-- link:begin outdated-advice-ledger#lower-temperature -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#lower-temperature)<!-- link:end --> の行を見る。

使えない前提で、ばらつきには別の手で付き合う。出力の形を指示で絞る。重要な部分は複数回の結果で確かめる。ばらつきを消すことよりも、ばらつきがあっても判断を誤らない仕組みを作る。

## よくある誤解 {#misconceptions}

- **誤解：「答えが変わるのは、Claude が壊れているからだ」**。変わること自体は、このページの前提どおりの通常の動作である。変わった結果の中身が誤りなのかどうかは、別に確かめる。
- **誤解：「毎回同じ答えが返れば、その答えは正しい」**。毎回同じ答えは、安定を示すだけで、正しさを示さない。同じ誤りを毎回返すこともある。誤りが繰り返される背景は <!-- link:begin why-hallucinations#guess-pays -->[ハルシネーションはなぜ起きるか › 分からなくても答えるほうが得になる訓練](why-hallucinations.md#guess-pays)<!-- link:end --> で扱う。
- **誤解：「1 回うまくいった頼み方は、いつも通用する」**。1 回の成功は、頼み方の力と偶然を区別できない。複数回で確かめてから使う。
- **誤解：「1 回失敗した頼み方は、役に立たない」**。同じ理由で、1 回の失敗も頼み方の欠陥の証拠にならない。複数回で見て、毎回外れるなら直す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/research/infrastructure-noise)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [判断を決定論的なスクリプトに移す](../enforce/move-judgment-into-scripts.md)
- [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)

**関連**

- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [ハルシネーションはなぜ起きるか](why-hallucinations.md)
- [頼み方は一回で決めない（会話で詰める）](../prompting/refine-in-conversation.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
