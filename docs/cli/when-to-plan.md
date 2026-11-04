---
id: when-to-plan
title: plan mode の使いどころ
aliases: [plan モード, plan mode, プランモード, 計画モード, /plan, 計画させてから実装する]
type: feature
field: cli
chapter: 権限モードと計画
order: 50
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [握る, 見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: plan mode で編集を止めたまま調べさせ、出てきた計画を読んで直してから実装に入る。誤解は計画の段階で見つけるほど安く直せるので、方針や範囲に迷いがある作業で使う。
signs:
  - {type: goal, text: いきなり実装させず、先に方針を確かめたい}
  - {type: symptom, text: 大きな変更を、実装が済んでから方針ごと作り直すことが多い}
prerequisites: [permission-modes-overview]
related: [spec-first, let-claude-ask, define-done, split-models-by-role, not-what-i-meant, does-more-than-asked, handoff-documents, using-ides, cloud-sessions-and-teleport]
tracks: [plan-mode]
outdated_advice: []
sources: [cc-docs-permission-modes, cc-docs-context-window]
volatility: 中
sections:
  - {title: 計画が効く作業、省いてよい作業, anchor: when}
  - {title: 最小の使い方, anchor: how-to}
  - {title: 計画の読み方と直し方, anchor: review}
  - {title: 計画を承認した後, anchor: after-approval}
  - {title: 効かない場面・落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：編集を止めたまま Claude に調べさせ、出てきた計画を読んで直してから実装に入れる。
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。計画を承認するまで、Claude Code がソースの編集を止める。ただし `bypassPermissions` が使える対話の端末では、この止めが効かない。
    - **いつ引くか**：いきなり実装させず、先に方針を確かめたいとき。大きな変更を、実装が済んでから方針ごと作り直すことが多いとき。
    - **前提**：<!-- link:begin permission-modes-overview -->[権限モードの選び方](permission-modes-overview.md)<!-- link:end -->

<!-- textlint-disable -->
別名：plan モード・plan mode・プランモード・計画モード・/plan・計画させてから実装する
<!-- textlint-enable -->

plan mode は、Claude Code が編集を止めたまま、ファイルを読み、調べ、実装の計画を書く権限モードである。計画を人が読み、直し、承認してから実装に入る。この辞典では、Claude 側に見えていない前提や範囲の取り違えを、実装の前に見つけるための道具として扱う。

## 計画が効く作業、省いてよい作業 {#when}

計画が効くのは、方針か範囲に迷いがあり、取り違えが実装の後で見つかると高くつく作業である。計画は数十行の文章で、実装の差分は複数のファイルにまたがる。同じ取り違えでも、計画で見つけるほうが読む量と直す量が少ない。

次のような作業では、計画を先に出させる価値が高い。

- 複数のファイルにまたがる変更で、どこを触るかが自分でも固まっていない
- 不慣れなコードで、Claude がどこまで調べて何を前提にするかを確かめたい
- 実現の手段が複数あり、どれを選ぶかで後の作業が変わる
- 頼んだ内容と別のものが出てきて、やり直した経験がある（原因の切り分けは <!-- link:begin not-what-i-meant#diagnosis -->[意図と違うものが出てくる › 原因を安く確かめる順](../symptoms/not-what-i-meant.md#diagnosis)<!-- link:end --> にある）

防ぐ原因は、Claude 側に前提や範囲が見えていないことである。計画は Claude の理解を文章にして外に出すので、人が読んで食い違いを見つけられる。人が握るのは、計画を承認するかどうかという一点である。

省いてよいのは、直す場所と中身を自分で言い切れる小さな変更である。誤字の修正、1 つの関数の戻り値の修正、文言の差し替えなどがそれに当たる。計画にも読む手間と使用量がかかるので、計画が実装より重くなるなら省く。目安として「差分を一文で説明できるなら計画を省く」と言われるが、現行の公式の文書では該当する文を確かめられていない。この辞典の経験則として扱い、公式の推奨とは書かない。

!!! example "判断例：同じ変更を 3 か所に入れる"
    - **状況**：設定の読み込み関数の名前を変え、呼び出し元の 3 ファイルを直したい。
    - **迷う候補**：すぐ実装させる。plan mode で影響の範囲を先に出させる。
    - **選んだもの**：呼び出し元がその 3 つで全部だと確かめられているなら、すぐ実装させる。
    - **理由**：直す場所と中身を一文で言えるので、計画を読む手間のほうが重い。呼び出し元の数が分からない、動的に呼ばれている恐れがある、といった迷いがあれば plan mode にする。

!!! example "判断例：認証の方式を差し替える"
    - **状況**：セッションの Cookie による認証を、トークンによる認証へ差し替えたい。触る範囲もテストの扱いも固まっていない。
    - **迷う候補**：まず小さく実装させて、差分を見て直す。plan mode で計画を出させ、読んでから実装する。
    - **選んだもの**：plan mode で計画を出させる。
    - **理由**：範囲が広く、方式の選び方で後の作業が変わる。実装の後に方針の違いが分かると、差分ごと捨てることになる。計画なら、触るファイルと移行の順序の食い違いを先に見つけられる。

仕様そのものを固めたいなら、計画の前に <!-- link:begin spec-first#interview -->[仕様を先に固める（spec・インタビュー・モック先行） › インタビューで仕様を詰める](../recipes/spec-first.md#interview)<!-- link:end --> へ進む。要件が固まっていないときは、<!-- link:begin let-claude-ask#how -->[質問させる・インタビューさせる › 質問させる頼み方](../prompting/let-claude-ask.md#how)<!-- link:end --> で先に質問させるほうが早い。

## 最小の使い方 {#how-to}

plan mode には 3 通りで入る。対話の端末で `Shift+Tab` を押して権限モードを切り替える。1 回の依頼だけなら、依頼の先頭に `/plan` を付ける。最初から入るなら `claude --permission-mode plan` で起動する。もう一度 `Shift+Tab` を押すと、計画を承認せずに plan mode を出る。切り替えの一覧は <!-- link:begin permission-modes-overview#switch -->[権限モードの選び方 › 切り替え方](permission-modes-overview.md#switch)<!-- link:end --> にある。

plan mode の Claude は、ファイルを読み、調べるためのシェルのコマンドを動かし、計画を書く。ソースの編集はしない。調べのシェルのコマンドが確認なしで動くかは、auto モードが使えるかなどで変わる。確認の出方は <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](permission-modes-overview.md#modes)<!-- link:end --> で確かめる。

計画を頼むときは、範囲外と確かめ方、迷った点を書かせると読みやすい。次の雛形は、計画だけを頼む依頼の一例である。

<!-- gen:begin snippet when-to-plan/ask-for-plan -->
<!-- textlint-disable -->

??? example "雛形：計画だけを頼む依頼"

    ```markdown
    次の変更を、まだ実装せずに、計画だけ立ててほしい。

    - 変更：<やりたいこと>
    - 範囲外：<今回は触らないもの>
    - 守るもの：<変えてはいけない動作・ファイル>
    - 計画には、変えるファイルとその順序、各段で何を見れば済んだと分かるか、選択肢があって迷った点（推奨案つき）を書く
    - 前提が足りないと感じた所は、推測で埋めず、計画の先頭に質問として並べる
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet when-to-plan/ask-for-plan -->

「確かめ方」の書かせ方の詳細は <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> にある。この辞典は WSL・Linux の CLI を基準としている。ほかの OS での動作は未確認である。

## 計画の読み方と直し方 {#review}

計画を読むときは、細部より先に、Claude の理解が合っているかを見る。次の順に読むと、高くつく取り違えから見つかる。

1. **前提**：Claude が何を目的と捉え、何を前提にしているか。自分の意図とずれていれば、以降の項目を読む前に直す
2. **範囲**：触るファイルが想定の内か。頼んでいないファイルや抽象化が入っていないか。入っているなら、<!-- link:begin does-more-than-asked#prevention -->[頼んでいないことまでやる（過剰設計） › 予防：範囲を先に決め、差分を毎回見る](../symptoms/does-more-than-asked.md#prevention)<!-- link:end --> の形で範囲を絞る
3. **順序と確かめ方**：各段で何を見れば済んだと言えるか。見ようのない段は、完了の定義が曖昧な段である
4. **迷った点と質問**：Claude が選んだ理由を書いているか。推測で埋めた所は、答えを返して決める

直し方は 2 通りある。方向の違いは、計画の選択画面で `No, keep planning` を選び、何を変えるかを言葉で返す。計画の中の小さな直しは、`Ctrl+G` で計画を既定のテキストエディタに開き、直接書き換える。方向の違いは言葉で、数か所の差し替えは直接の編集で直すと、やり取りが短く済む（推論・実践例なし）。直接編集した内容が Claude にどう伝わるかは、この辞典では確かめていない。

VS Code の拡張では、plan mode の計画が Markdown の文書として開き、行ごとにコメントを付けて返せる。使い方は <!-- link:begin using-ides#what-you-get -->IDE（VS Code・JetBrains）で使う › IDE で得られるもの（準備中）<!-- link:end --> にある。この辞典では動作を試していない。

計画を読んでも判断がつかないときは、実装に入らず、迷った点を質問として返す。計画の段階で「分からない」と言えることが、plan mode のいちばんの利点である。

## 計画を承認した後 {#after-approval}

計画が出来上がると、Claude Code が進め方を選ばせる。公式の文書（確認日 2026-11-04）にある選択肢は次のとおりである。文言は版や設定で変わる。

- **`Yes, and use auto mode`**：承認して auto モードで実装に入る。auto モードが使えないときは `Yes, auto-accept edits` と出る
- **`Yes, manually approve edits`**：承認して、編集を 1 つずつ確かめながら進める
- **`No, keep planning`**：plan mode のまま、直す点を伝える

任せる幅が広がるのは、最初の選択肢である。承認の前に、計画に完了の定義と、止まって報告する条件を入れておく。書かせ方は <!-- link:begin define-done#stop-and-report -->[「完了」を定義して渡す › 止まって報告する条件](../verify/define-done.md#stop-and-report)<!-- link:end --> にある。計画に自信が持てないとき、危うい作業のときは、2 番目の選択肢で編集を 1 つずつ見る。

設定 `showClearContextOnPlanAccept` を有効にすると、計画の承認と同時に調べの文脈を消す選択肢が、先頭に加わる。調べで文脈が大きくなったときに使える。承認した計画が実装側にどう渡るかは、この辞典では確かめていない。実装に入った後は、計画の内容を Claude が踏まえているかを確かめる。

実装が長くなって会話が圧縮されても、plan mode で書いた計画は、圧縮の後にディスクから入れ直される。圧縮との使い分けは <!-- link:begin handoff-documents#vs-compact -->[handoff 文書と document-and-clear › /compact との使い分け](../context/handoff-documents.md#vs-compact)<!-- link:end --> にある。

会話そのものを新しくして実装するなら、計画を文書に書き出してから渡す。置き場所は <!-- link:begin handoff-documents#where -->[handoff 文書と document-and-clear › 置き場所（圧縮で消えない所）](../context/handoff-documents.md#where)<!-- link:end --> にある。仕様を渡して新しいセッションで作る流れは <!-- link:begin spec-first#implement-fresh -->[仕様を先に固める（spec・インタビュー・モック先行） › 新しいセッションで実装する](../recipes/spec-first.md#implement-fresh)<!-- link:end --> にある。

実装が計画から外れていないかは、実装の後に、差分を承認した計画と照らして確かめる。これは人の役目である。

## 効かない場面・落とし穴 {#limits}

- **`bypassPermissions` が使える対話の端末では、止めが効かない**：Claude は計画だけを立てるよう指示されるが、試みた編集やシェルのコマンドが確認なしで動く。plan mode を安全装置として頼らない。`-p` の実行、Agent SDK、VS Code の拡張のチャット欄では、止めが保たれる
- **何も実行しない仕組みではない**：調べのためにシェルのコマンドが動く。確認の出方は権限モードと設定で変わる
- **計画は正しいと限らない**：Claude は見えていない所を推測で埋める。取り違えを見つけるのは、読んだ人である
- **読まずに承認すると無意味になる**：計画が長すぎるなら、粒度を粗くさせるか、作業を分ける
- **止まるのは計画の間だけ**：鍵がかかるのは、承認までの編集である。承認した後の実装が計画に従うかは、お願いにすぎない。実装後の差分の確かめは省かない

## 比べる相手 {#compare}

| 手段 | 向く場面 | 詳しい説明 |
| --- | --- | --- |
| plan mode | 方針や範囲を、Claude の調べを見て決めたい | このページ |
| 仕様を先に固める | 要件そのものが固まっていない大きな機能 | <!-- link:begin spec-first -->[仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)<!-- link:end --> |
| 質問させる | 自分でも決めていない点を洗い出したい | <!-- link:begin let-claude-ask -->[質問させる・インタビューさせる](../prompting/let-claude-ask.md)<!-- link:end --> |
| 計画と実装でモデルを分ける | 計画に重いモデル、実装に軽いモデルを使いたい | <!-- link:begin split-models-by-role -->計画・実装・サブエージェントでモデルを分ける（準備中）<!-- link:end --> |

手元を離れて長く走らせる作業は、計画と縛りをリポジトリに置いてから送る。その進め方は <!-- link:begin cloud-sessions-and-teleport#what-to-send -->クラウドセッションと teleport › クラウドに送ってよい作業（準備中）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [権限モードの選び方](permission-modes-overview.md)

**次に読む**

- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)
- クラウドセッションと teleport（準備中）

**関連**

- [質問させる・インタビューさせる](../prompting/let-claude-ask.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- 計画・実装・サブエージェントでモデルを分ける（準備中）
- [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- IDE（VS Code・JetBrains）で使う（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
