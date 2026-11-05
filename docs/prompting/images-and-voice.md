---
id: images-and-voice
title: 画像・スクリーンショット・音声で渡す
aliases: [スクショを貼る, 画面の画像を渡す, 音声入力, /voice]
type: concept
field: prompting
chapter: 資料と入力の渡し方
order: 140
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない]
scenes: [開発, 文章]
summary: 言葉で説明しにくい画面・図・エラーは画像で、まとまらない考えは音声で渡すと、見せられる文脈が増える。読み取りの誤りは残るので、要点は文字でも確かめる。
signs:
  - {type: symptom, text: 画面の崩れを言葉で説明しきれない}
  - {type: goal, text: 考えを話しながら頼みたい}
  - {type: goal, text: エラー画面をそのまま見せたい}
prerequisites: [brief-a-new-colleague]
related: [visual-checks, how-attachments-are-read, voice-and-mobile, input-symbols, let-claude-ask, keep-replies-in-japanese]
tracks: [voice, voice-dictation]
sources: [cc-docs-common-workflows, cc-docs-voice-dictation, cc-docs-commands, cc-docs-settings-reference, hc-voice-mode]
volatility: 中
sections:
  - {title: 画像で渡すと速いもの, anchor: images}
  - {title: 音声でまとめて話して渡す, anchor: voice}
  - {title: なぜ見せると効くのか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：画像と音声の使い分けが分かる。言葉で説明しにくい画面・図・エラーは画像で、まとまらない考えは音声で渡す
    - **いつ引くか**：画面の崩れを言葉で説明しきれないとき。考えを話しながら頼みたいとき。エラー画面をそのまま見せたいとき
    - **前提**：<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end -->

<!-- textlint-disable -->
別名：スクショを貼る・画面の画像を渡す・音声入力・/voice
<!-- textlint-enable -->

画像・スクリーンショット・音声で渡すとは、文字に直すと手間がかかる文脈を、画像と話し言葉という別の経路で Claude に届ける頼み方の技法である。Claude には渡されたものしか見えないので、画面も頭の中の考えも、渡さなければ存在しない。このページは、何を画像にし、何を音声にし、何を文字に残すかを決める目安を示す。

## 画像で渡すと速いもの {#images}

画像で渡すと速いのは、見た目・図・エラー表示のように、言葉に直すと時間がかかるうえに抜けが出るものである。画面の崩れ、ダッシュボードの数字の並び、設計図、デザインの見本がこれに当たる。

同じ依頼を、言葉だけで頼む場合と、画像を添えて頼む場合で並べる。

**Before**

```text
設定画面のボタンの位置がおかしいので直して
```

**After**（画像を 1 枚添える）

```text
添付は設定画面をスマホ幅で開いたスクリーンショット。
右上の保存ボタンがヘッダーに収まらず、2 行目に落ちている。
期待は、保存ボタンがヘッダーの右端に 1 行で並ぶこと。
直すのは src/components/Header.tsx だけ。直したら同じ幅で見え方を確かめて。
```

After で足したものは 3 つある。画像（言葉では表しにくい「落ちている」様子）、画像の中で見てほしい所（右上の保存ボタン）、期待と直す範囲である。画像は「どう見えているか」を渡すが、「どう見えるべきか」と「どこまで触ってよいか」は渡さない。後者は文字で書く。

次の雛形は、画像に添える文字の骨組みである。空欄のうち、答えで結果が変わるものだけを埋める。

<!-- gen:begin snippet images-and-voice/screenshot-request -->
<!-- textlint-disable -->

???+ example "雛形：スクリーンショットに添える依頼の雛形"

    ```text
    添付のスクリーンショットは、<画面の名前と状態。例：設定画面、スマホ幅>。
    見てほしい所：<画像の中のどこか。例：右上の保存ボタン>
    期待：<本来どうなるべきか>
    実際：<画像で起きていること>
    条件：<再現に要るもの。例：ブラウザ、画面の幅、ログインの有無>
    直す範囲：<触ってよいファイルや範囲>
    完了：<何を確かめたら終わりか>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet images-and-voice/screenshot-request -->

画像の渡し方は面で違う。

=== "アプリ"

    画像は添付として渡す。どこまでが図も含めて読まれるかと、読まれたかの確かめ方は <!-- link:begin how-attachments-are-read#verify -->[添付ファイルはどこまで読まれるか › 読まれたかを確かめる（ページの番号と引用）](../app/how-attachments-are-read.md#verify)<!-- link:end --> にある。

=== "Claude Code"

    公式の手順では、画像をウィンドウへドラッグする、コピーした画像をターミナルへ貼り付ける、画像のファイルのパスを書く、の 3 つで渡す。貼り付けのキーは、Windows と WSL でほかの環境と違う。1 つの会話に複数の画像を渡せる。手順の細部は公式の文書（出典の common-workflows）を見る。macOS と IDE 拡張での挙動は未確認である。

Claude 自身にブラウザを操作させ、画面を見て確かめさせたいときは、渡す側ではなく確かめさせる側の話になる。<!-- link:begin visual-checks#screenshots -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › スクリーンショットで比べる](../verify/visual-checks.md#screenshots)<!-- link:end --> を見る。

!!! example "判断例：エラーの渡し方"
    - **状況**：テストが落ち、ターミナルに長いスタックトレースが出ている。
    - **迷う候補**：スクリーンショットを撮って渡す。文字をコピーして貼る。
    - **選んだもの**：文字をコピーして貼る。画面全体の状態が要るときだけ、スクリーンショットを足す。
    - **理由**：文字はそのままコピーでき、ファイル名や行番号を読み違えない。画像は、文字に直せない配置・色・ずれを見せるときに使う。

## 音声でまとめて話して渡す {#voice}

音声で渡すのは、考えがまとまっていない段階で、背景・迷い・制約をまとめて出したいときである。書くより話すほうが速く、書く手間で省いていた前提が出てくる。ただし、話した量が多いほど要点が埋もれるので、最後に文字で締める。

音声の入口は 2 つある。アプリの音声モードと、Claude Code の音声入力（`/voice`）である。名前が似ていて別の機能なので、表で区別する。

<!-- gen:begin compare 面 成熟度 -->
<!-- textlint-disable -->

| 機能 | 面 | 成熟度 |
| --- | --- | --- |
| 音声モード（voice mode） | アプリ | beta |
| [音声入力（/voice）](images-and-voice.md) | Claude Code | GA |

<!-- textlint-enable -->
<!-- gen:end compare 面 成熟度 -->

=== "アプリ"

    アプリの音声モードは、Claude と声で会話する機能である。始め方と、モバイルでできることは <!-- link:begin voice-and-mobile#voice -->音声モード・Quick entry・モバイル<!-- link:end --> にある。

=== "Claude Code"

    Claude Code の音声入力は、話した言葉を入力欄に書き起こす機能である。`/voice` で有効にする。書き起こしは入力欄に入るので、タイピングと混ぜて 1 つの依頼にできる。

    - 録音には、キーを押している間だけ録るモードと、1 回押して始めてもう 1 回押して送るモードがある。`/voice tap` で後者にし、`/voice hold` で前者に戻す。
    - 後者は、書き起こしが短すぎない限り、そのまま送信される。聞き違いを送る前に読み直したいときは、押している間だけ録るモードを使う。
    - 録音を取り消すには `Esc` か `Ctrl+C` を押す。書き起こしは捨てられ、入力欄は録音の前に戻る。
    - 録音は Anthropic のサーバへ送られて書き起こされる。クラウドのセッションと SSH のセッションでは使えない。マイクがない環境でも使えない。
    - 書き起こしは claude.ai のアカウントで認証したときだけ使える。API キーや Bedrock などで使っている場合は使えない。
    - 音声の言語は、返答の言語を決める `language` の設定と同じものを使う。空のままだと英語として聞き取られる。日本語で話すなら、`/config` か設定ファイルで `language` を日本語にする。

    WSL・Linux 以外の OS と IDE 拡張での挙動は未確認である。キーの割り当てを含む細部は公式の文書（出典の voice-dictation）を見る。

音声で話した後は、短い文字で締める。次の雛形は、要点・完了・範囲・固有名を足す。さらに、実装の前に Claude に言い直させる。

<!-- gen:begin snippet images-and-voice/spoken-brief -->
<!-- textlint-disable -->

??? example "雛形：音声で話した後に文字で足す締めの雛形"

    ```text
    （音声で話した内容の後ろに、文字で足す）

    要点：<話した内容を 1 文で>
    完了：<何ができていれば終わりか>
    範囲：<やらないこと、触らないもの>
    固有名：<音声で崩れやすいファイル名、関数名、製品名>

    実装の前に、聞き取った内容を 3 行で言い直してください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet images-and-voice/spoken-brief -->

**Before**（話したまま送る）

```text
えっと、ログインの画面なんだけど、たまに何か変な感じで、前にも似たことがあって……
```

**After**（話した後に文字で締める）

```text
（上の話の後ろに）
要点：ログイン後の画面遷移が、ときどき止まる。
完了：止まる条件を特定し、再現する失敗テストを 1 つ書く。
範囲：認証の実装は直さない。
固有名：useAuthRedirect
実装の前に、聞き取った内容を 3 行で言い直してください。
```

After で足したものは 4 つある。話の要点、完了の条件、触らない範囲、崩れやすい固有名である。最後の 1 行で、聞き違いを実装の前に見つけられる。

考えが固まっていない段階では、話しっぱなしで頼むより、Claude に質問させて決める手もある。<!-- link:begin let-claude-ask#how -->[質問させる・インタビューさせる › 質問させる頼み方](let-claude-ask.md#how)<!-- link:end --> を見る。

## なぜ見せると効くのか {#why}

画像と音声が効くのは、原理「見せる」にあたるからで、防ぐのは原因「見えていない」である。Claude には会話に入ったものしか見えない。画面の見た目や頭の中の考えは、言葉に直す途中で落ちる。落ちた分は、Claude には最初からなかったことになる。

<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end --> の比喩で言えば、隣の席の新人に頼むとき、画面を指して「ここ」と言えば済む場面がある。画像はその指差しにあたる。音声は、書くより軽い手段で背景を多く渡す方法にあたる。

何に効くかを整理する。

- 画像は、配置・色・ずれ・図の構造のように、言葉にすると不正確になる情報の落ちを防ぐ。
- 音声は、書く手間で省かれていた前提や迷いが依頼に入るのを助ける。
- どちらも、渡した量が増えるだけで、その中のどこが要点かは Claude に決められない。要点は文字で足す。

## 効かない場面とやりすぎ {#limits}

画像と音声には、効かない場面がある。

- **文字で取れるものを画像にする**：スタックトレース、ログ、コードは文字で貼る。画像にすると、読み違いの余地を自分で作る。
- **細部の読み取りを任せきる**：小さな文字、細かい数値、近い色の差は読み違えることがある。重要な値は文字でも書き、読まれたかは <!-- link:begin how-attachments-are-read#verify -->[添付ファイルはどこまで読まれるか › 読まれたかを確かめる（ページの番号と引用）](../app/how-attachments-are-read.md#verify)<!-- link:end --> の方法で確かめる。
- **見てほしい所を書かずに貼る**：画像に情報が多いと、関係のない所を拾う。切り抜くか、見てほしい所を文字で書く。
- **写り込み**：画面には、トークン、個人情報、顧客の情報が写っていることがある。渡す前に隠すか、写さない。
- **話した内容をそのまま送る**：聞き違いや、言い忘れた完了の条件が、実装が進んでから見つかる。聞き違いやすいのはファイル名・関数名・製品名である。
- **長く話せば伝わると考える**：量は要点の代わりにならない。完了と範囲は文字で足す。

この技法は、頼み方の基本を置き換えない。画像や音声を使っても、文脈のない同僚が読んで迷う依頼は、Claude も迷う。

次に読むものは、ページ下部の関連にある。入力の記号を使い分けたいなら <!-- link:begin input-symbols#which -->[入力の記号（/ ! @）と Esc › 入力の記号の使い分け](../cli/input-symbols.md#which)<!-- link:end --> も見る。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [新人の同僚に頼むつもりで](brief-a-new-colleague.md)

**関連**

- [画面で確かめる（ブラウザ・スクリーンショット・/verify）](../verify/visual-checks.md)
- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- [質問させる・インタビューさせる](let-claude-ask.md)
- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04
- [Voice dictation](https://code.claude.com/docs/en/voice-dictation)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Use voice mode](https://support.claude.com/en/articles/11101966-use-voice-mode)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
