---
id: side-questions-btw
title: 本筋を汚さずに聞く（/btw）
aliases: [/btw, 横道の質問, サイドクエスチョン]
type: feature
field: context
chapter: 脇道を分ける
order: 150
level: 整える
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発, 学習]
summary: 作業の途中のちょっとした質問を /btw で聞き、答えを会話の履歴に残さない。本筋の文脈を汚さずに、用語の確認や寄り道ができる。
signs:
  - {type: goal, text: ちょっとした質問で本筋を汚したくない}
  - {type: situation, text: 作業の途中で、関係のない疑問がわいた}
prerequisites: [tidy-the-desk]
related: [research-in-subagents, when-to-start-fresh, must-know-operations, learning-with-ai]
tracks: [btw]
outdated_advice: []
sources: [cc-docs-interactive-mode, cc-docs-commands]
volatility: 中
sections:
  - {title: 何を防ぐか, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 効かない場面と落とし穴, anchor: pitfalls}
  - {title: /btw・新しい会話・サブエージェントの使い分け, anchor: which}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`/btw` を使うと、作業の途中の質問を、会話の履歴に足さず聞ける。答えは、会話にすでにあることだけから返る。
    - **いつ引くか**：ちょっとした質問で本筋を汚したくないとき。作業の途中で、関係のない疑問がわいたとき。
    - **強制力**：<!-- gen:begin feature btw/enforcement -->なし<!-- gen:end feature btw/enforcement -->。質問の道を別に用意するだけで、Claude のふるまいを縛る機能ではない。履歴に入らず、道具を使わないのは、お願いではなく機能の作りである。
    - **前提**：<!-- link:begin tidy-the-desk -->[机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)<!-- link:end -->

<!-- textlint-disable -->
別名：/btw・横道の質問・サイドクエスチョン
<!-- textlint-enable -->

`/btw` は、Claude Code の対話の途中で、今の会話について横から質問する組み込みのコマンドである。質問と答えは会話の履歴に入らず、Claude は道具を使わずに、文脈にあるものだけから答える。本筋の文脈を増やさずに、直前の判断や用語を確かめたいときの手である。

## 何を防ぐか {#when}

`/btw` が防ぐのは、本筋と関係のない往復で、文脈が散らかることである。作業中に「さっきの関数の名前は何だった」と普通の依頼で聞くと、質問と答えが履歴に残る。履歴は以後の応答でも読まれるので、広い机の上で、本筋と関係のない紙が増えていく。`/btw` は、その紙を机へ置かず、答えだけを見て閉じる手である。

文脈の整頓の全体と、整頓が何に効くかは、<!-- link:begin tidy-the-desk#effect -->[机を整える：新鮮さ・巻き戻し・書き出し・委任 › 何に効くか（見せる・散らかっている）](tidy-the-desk.md#effect)<!-- link:end --> にある。`/btw` は、履歴を新しくしたり巻き戻したりする手ではなく、そもそも履歴に足さない手である。

向く質問は、今の会話にすでに出ていることを聞き返すものである。

- Claude がすでに読んだコードや、出力の中身を確かめる
- 少し前に Claude が決めた理由を思い出す
- 説明に出てきた用語の意味を聞く

学習の場面では、会話に出た用語をその場で聞き返せる。ただし、答えを読んで分かった気になることと、理解が残ることは別である。理解が残ったかの確かめ方は <!-- link:begin learning-with-ai#how-to-check -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 理解が残ったかの確かめ方](../judgment/learning-with-ai.md#how-to-check)<!-- link:end --> にある。

## 最小の使い方 {#minimal}

使い方は、`/btw` の後に質問を書いて送るだけである。ここでは、Claude Code の端末での動きを示す。

=== "Claude Code"

    1. `/btw` に続けて質問を書き、送る。例は `/btw さっき読んだ設定ファイルの名前は何だった？` である。
    2. 答えが、重ねて出る表示（オーバーレイ）に出る。Space・Enter・Escape のどれかで閉じて、入力欄に戻る。
    3. 閉じた後に見返すには、質問を付けずに `/btw` を送る。直近のやり取りが開き直る。
    4. 答えの表示中は、`c` で答えを Markdown のままコピーできる。`f` を押すと、この質問と答えを引き継いだサブエージェントが別に動く（ローカルのセッションのみ）。

    `/btw` は、Claude が応答を作っている最中にも使える。本筋の作業は止まらない。ただし、Claude がいま書いている途中の返答は、`/btw` からは見えない。

    続けて聞きたいときは、もう一度 `/btw` を送る。前の `/btw` のやり取りは、次の `/btw` から見える。一覧を空にするには、答えの表示中に `x` を押す。これらは端末を閉じると消える。

VS Code 拡張では、`/btw` はオーバーレイではなくパネルで開くと公式が書いている。ほかの IDE 拡張と、WSL・Linux 以外の OS での動きは、この辞典では未確認である。

質問の例を、次の雛形に示す。

<!-- gen:begin snippet side-questions-btw/btw-questions -->
<!-- textlint-disable -->

??? example "雛形：本筋の途中で、文脈にあることを聞き返す /btw の質問"

    ```markdown
    /btw さっき読んだ設定ファイルの名前は何だった？
    /btw 先ほどの修正で、リトライを足した理由を一言で思い出させて
    /btw 説明に出てきた「冪等」は、ここでは何を指している？
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet side-questions-btw/btw-questions -->

## 効かない場面と落とし穴 {#pitfalls}

`/btw` の弱点は、道具を使えないことと、答えが本筋に伝わらないことである。

- **道具を使えない**：`/btw` は、ファイルの読み込み・コマンドの実行・検索をしない。「このファイルを開いて確かめて」は頼めない。文脈にないことを聞くと、確かめずに推測で答える恐れがある（推論）。新しく調べる質問は、本筋で頼むか、サブエージェントに任せる。
- **答えは本筋の Claude に伝わらない**：答えが履歴に入らないので、本筋の Claude は、その答えを知らない。答えを受けて方針を変えるときは、結論を本筋の依頼に書く。
- **答えは残らない**：閉じた答えを見返せるのは、端末のセッションが続いている間だけである。残したい答えは、ファイルに書き出す。書き出しの考え方は <!-- link:begin tidy-the-desk#four-actions -->[机を整える：新鮮さ・巻き戻し・書き出し・委任 › 四つの動作](tidy-the-desk.md#four-actions)<!-- link:end --> にある。
- **使用量には数える**：履歴に足されないのは、本筋の文脈が増えない、という意味である。答えのトークンは使用量に数える。会話のプロンプトキャッシュが温かいうちは、答え以外の費用はわずかだと公式は書いている。
- **掘り下げには向かない**：1 つの `/btw` は、1 つの質問と 1 つの答えで終わる。続けて聞くことはできるが、そのたびに道具なしの短い確認になる。掘り下げるなら、`f` で引き継ぐか、本筋で聞く。

実行中の処理を待つ間に聞く場面は <!-- link:begin must-know-operations#watch-and-background -->[知らないと損をする操作 › 様子を見る・背景に回す](../cli/must-know-operations.md#watch-and-background)<!-- link:end --> を見る。

## /btw・新しい会話・サブエージェントの使い分け {#which}

本筋を離れて聞く手は 3 つある。違いは、本筋の履歴に何が残るかと、道具を使えるかである。

| 手 | 向く場面 | 本筋の履歴 | 道具 |
| --- | --- | --- | --- |
| `/btw` | 今の会話にあることを確かめる | 質問も答えも足されない | 使えない |
| 新しい会話 | 話題が変わった。訂正を重ねても直らない | 本筋を離れ、空の文脈から始める | 使える |
| サブエージェント | 新しく読んで調べる | 結論と根拠の場所だけを戻させる | 使える |

使い分けの基準は、新しい情報が要るかどうかである。`/btw` は、会話ですでに分かっていることを聞く手で、新しく見つけに行く手ではない。見つけに行くならサブエージェントで、本筋の話が終わったなら新しい会話である。新しい会話の合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](when-to-start-fresh.md#signals)<!-- link:end --> に、サブエージェントに任せてよい調査は <!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](research-in-subagents.md#when)<!-- link:end --> にある。

`/btw` の属性を、次の表に示す。コンテキストのコストの「ゼロ」は、本筋の会話の文脈に足さない、という意味である。答えのトークンまでゼロにはならない。

<!-- gen:begin compare 成熟度 コンテキストのコスト -->
<!-- textlint-disable -->

| 機能 | 成熟度 | コンテキストのコスト |
| --- | --- | --- |
| [/btw](side-questions-btw.md) | GA | ゼロ |

<!-- textlint-enable -->
<!-- gen:end compare 成熟度 コンテキストのコスト -->

!!! example "判断例：実装の途中で、関数の名前を忘れた"
    - **状況**：長い修正の途中で、Claude が少し前に読んだ関数の名前を思い出せない。
    - **迷う候補**：本筋でそのまま聞く。`/btw` で聞く。
    - **選んだもの**：`/btw` で聞く。
    - **理由**：答えは会話にすでにあり、道具は要らない。本筋で聞くと、その往復が履歴に残る。名前が分かれば、本筋の依頼にそのまま書ける。

!!! example "判断例：聞いたら、別のファイルを調べたくなった"
    - **状況**：`/btw` で設計の理由を聞いたら、答えが「別のモジュールに関係する」と指した。そのモジュールの中身は、まだ読んでいない。
    - **迷う候補**：`/btw` で重ねて聞く。`f` で引き継ぐ。本筋の依頼として頼む。
    - **選んだもの**：読む量が少なければ本筋で頼む。多ければ `f` で引き継ぐ。
    - **理由**：`/btw` は道具を使えず、文脈にないモジュールは読めない。引き継いだサブエージェントは道具を使え、結果を本筋と分けて受け取れる。

!!! example "判断例：本筋が終わり、次の話題に移る"
    - **状況**：ひとつの機能の実装が済み、別の機能の相談を始めたい。
    - **迷う候補**：同じ会話のまま、`/btw` で次の話題の下調べを少しずつ聞く。新しい会話を始める。
    - **選んだもの**：新しい会話を始める。
    - **理由**：次の話題の作業には道具が要り、`/btw` は道具を使えない。前の機能の履歴を持ち込むと、文脈も散らかる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)

**関連**

- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](research-in-subagents.md)
- [新しい会話を始めるタイミング](when-to-start-fresh.md)
- [知らないと損をする操作](../cli/must-know-operations.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
