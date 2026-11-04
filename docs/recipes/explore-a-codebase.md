---
id: explore-a-codebase
title: 知らないコードベースを読む
aliases: [コードベースの理解, オンボーディング, 既存のコードを把握する, コードの地図を作る]
type: recipe
field: recipes
chapter: 読んで理解する
order: 10
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, 学習]
summary: 知らないコードベースの全体像を、広い質問から始めて具体的な箇所へ絞りながらつかむ。説明は該当のファイルと行で確かめ、分かったことは地図や用語集にして残す。
signs:
  - {type: situation, text: 引き継いだリポジトリで、どこに何があるか分からない}
  - {type: goal, text: ある処理が入口からどこを通って動くのかを追いたい}
  - {type: symptom, text: コードの説明がもっともらしいが、本当にそう動くのか分からない}
prerequisites: [choose-what-to-read, fact-checking]
related: [read-specs-yourself, research-in-subagents, code-intelligence-plugins, own-generated-code, how-much-understanding-to-keep, learning-with-ai, before-opening-unknown-repos, vetting-extensions#dependencies, what-to-put-in-claude-md, init-and-first-claude-md, uses-nonexistent-apis, fix-a-bug]
tracks: [subagents, plugins]
outdated_advice: [architecture-in-claude-md]
sources: [cc-docs-common-workflows, cc-docs-best-practices]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards-first}
  - {title: 広い質問から絞る, anchor: broad-to-narrow}
  - {title: 説明をコードで確かめる, anchor: check-against-code}
  - {title: 地図と用語集を残す, anchor: keep-a-map}
  - {title: 他人のリポジトリを開くとき, anchor: unknown-repos}
  - {title: 理解できたかの確かめ方, anchor: overall-check}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：広い質問から具体的な処理へ絞って全体像をつかみ、説明はコードで確かめ、分かったことを地図と用語集に残す。
    - **いつ引くか**：引き継いだリポジトリでどこに何があるか分からないとき。ある処理が入口からどこを通るのか追いたいとき。コードの説明がもっともらしいのに、本当にそう動くのか分からないとき。
    - **前提**：<!-- link:begin choose-what-to-read -->[@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)<!-- link:end -->・<!-- link:begin fact-checking -->[事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：コードベースの理解・オンボーディング・既存のコードを把握する・コードの地図を作る
<!-- textlint-enable -->

知らないコードベースを Claude に読ませると、説明はすぐ返ってくる。しかし、その説明がコードの実際の動きと合っているとは限らない。このページは、広い質問から始めて絞り、答えにファイルと行を添えさせて自分で確かめ、分かったことを別のファイルに残す進め方を示す。

## 先に整える守り {#guards-first}

読み始める前に、説明を確かめる守りと、読む量を絞る守りを整える。守りがないと、もっともらしい説明を信じたまま理解が進む。

- 確かめる守り：最初の依頼から、主張にファイルのパスと行番号を添えさせる。読んでいない所は「未読」、名前からの推測は「推測」と分けて書かせる。引用させる頼み方は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> が扱う。
- 縛る守り：探索の間はコードを変えさせない。依頼に「読んで答えるだけ」と書くのはお願いにとどまる。編集を止めたまま調べさせたいときは、Claude Code の plan mode を使う。
- 戻れる状態：読み始める前に、作業ツリーに未コミットの変更がないことを `git status` で確かめる。読むだけの作業で差分が出たら、止めて原因を見る。
- 読む量の守り：入口にしたいファイルは `@` で直接指す。長い出力は要点に絞ってから会話に入れる。使い分けは <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> と <!-- link:begin choose-what-to-read#trim-output -->[@参照と、何を読ませるかの絞り込み › 出力を絞る](../context/choose-what-to-read.md#trim-output)<!-- link:end --> が扱う。

## 広い質問から絞る {#broad-to-narrow}

知らないコードベースは、広い質問から始め、答えを見ながら具体的な処理へ絞る。いきなり細部を聞くと、全体の中での位置が分からないまま、説明の正しさも判断できない。Claude Code では、リポジトリのルートで起動して進める（根拠は公式の Common workflows）。

1. **概観をつかむ**：リポジトリ全体の概観を聞く。主なディレクトリの役割を答えさせる。終わりの印：主なディレクトリの役割を、自分の言葉で言える。
2. **構成と規約を聞く**：主なアーキテクチャのパターン、主なデータモデル、認証のような横断の仕組みの扱いを聞く。終わりの印：次に追う処理を 1 つ決められる。
3. **関連するコードを探させる**：追う処理に関わるファイルを探させ、そのファイル同士がどう連携するかを聞く。探すときは、プロジェクトのドメイン用語で頼む。終わりの印：ファイルの一覧が出て、そのうち数個を自分で開いて、確かに関係があると分かる。
4. **入口から追わせる**：処理を入口から末端まで、通る順に追わせる。答えには、各段のファイルのパスと行番号を付けさせる。終わりの印：すべての段に、開けるパスと行番号が付いている。

手順 4 の頼み方の雛形を次に置く。

<!-- gen:begin snippet explore-a-codebase/trace-flow -->
<!-- textlint-disable -->

??? example "雛形：全体像から特定の処理の流れへ絞る質問（答えにファイルと行を添えさせる）"

    ```markdown
    このリポジトリで、<処理の名前。例：ログイン、注文の確定>が、入口からどこを通って動くのかを知りたい。
    コードは変えずに、読んで答えるだけにする。

    進め方：
    1. まず、その処理の入口になるファイルと関数を挙げる。入口は、このリポジトリで使われている用語で探す
    2. 入口から、呼ばれる順に、通るファイルと関数を並べる。各段に「ファイルのパス:行番号」を付ける
    3. データを保存・読み出す所と、外部に出ていく所（ネットワーク・ファイル・別のサービス）があれば、段の中に印を付ける

    守ること：
    - 実際に読んだファイルだけを根拠にする。読んでいない所は「未読」と書く
    - 名前から推測した所は、「推測」と書いて分ける
    - 行番号を付けられない主張は、書かずに最後の「確かめられなかったこと」に並べる

    最後に、私が次に読むとよいファイルを 3 つまで挙げる。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.12。

<!-- textlint-enable -->
<!-- gen:end snippet explore-a-codebase/trace-flow -->

読む量が多いときは、次の 2 つの手で本筋の会話を軽くする。

- 型のあるコードベースでは、言語サーバーを使わせると、ファイルを総当たりで読む代わりに定義へ飛べる。入れ方と効き方は <!-- link:begin code-intelligence-plugins -->[code intelligence プラグイン（LSP）](../extend/code-intelligence-plugins.md)<!-- link:end --> が扱う。
- 出力が多く、本筋から独立した調査は、別室の部下であるサブエージェントに任せ、結論と根拠の場所だけを戻させる。トークンは余分にかかる。任せてよい調査と頼み方は <!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](../context/research-in-subagents.md#when)<!-- link:end --> と <!-- link:begin research-in-subagents#how -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 頼み方と戻させる形](../context/research-in-subagents.md#how)<!-- link:end --> が扱う。

!!! example "判断例：認証まわりの調べを、本筋で読むか、サブエージェントに任せるか"
    - **状況**：引き継いだ Web アプリで、ログインの流れを追いたい。認証に関わりそうなファイルが多数あり、全部を読むと会話が長くなる。
    - **迷う候補**：本筋の会話で順に読む。または、「認証に関わるファイルを洗い出して、役割を 1 行ずつ、パスと行番号付きで戻す」調査をサブエージェントに任せる。
    - **選んだもの**：洗い出しはサブエージェントに任せ、ログインの流れを追う作業は本筋で行う。
    - **理由**：洗い出しは出力が多く、本筋から独立している。流れを追う作業は、自分が理解するための作業で、途中の読みを見ながら質問を絞りたい。ただし、戻ってきた一覧のパスは、本筋でいくつか開いて確かめる。

## 説明をコードで確かめる {#check-against-code}

Claude のコードの説明は、該当のファイルと行を自分で開いて確かめる。説明が流暢でも、読んでいない所を名前から推測して書いていることがある。知らないコードベースでは、自分に判断の材料がないので、説明のもっともらしさが正しさの代わりになりやすい。これが、Claude 側の原因「確かめていない」（読んでいない所を確かめないまま答える）に当たる。

確かめる手は、費用の小さい順に 3 つある。

1. **引用を自分で照らす**：説明に付いた行番号の数か所を、自分でファイルを開いて照らす。引用が実際の行と一致するかを見る。
2. **主張ごとに、引用付きで確かめ直させる**：説明を主張に分けさせ、各主張の根拠のコードを読み直して、そのまま引用させる。合わないものは「合わない」と書かせる。説明を原文と照らす頼み方は <!-- link:begin fact-checking#summaries -->[事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<!-- link:end --> が扱う。
3. **実行して確かめる**：説明が「この関数が呼ばれる」と言うなら、テストを 1 つ流す、または使い捨てのブランチでログを足して実行し、実際に通るかを見る。

手の 2 つ目の頼み方の雛形を次に置く。

<!-- gen:begin snippet explore-a-codebase/recheck-claims -->
<!-- textlint-disable -->

??? example "雛形：説明の主張を、コードの引用で確かめ直させる依頼"

    ```markdown
    いまの説明の中の、コードについての主張を 1 つずつ確かめ直してほしい。コードは変えない。

    やること：
    1. 説明を主張ごとに分けて、番号を振る
    2. 各主張について、根拠のコードを今そのファイルから読み直し、該当の行をそのまま引用する（要約や言い換えにしない）
    3. 引用がコードと合っていれば「合う」、合わなければ「合わない」と書き、実際のコードが何をしているかを添える
    4. 読み直せなかった主張は「確かめられなかった」と書く

    表の形で、列は「番号｜主張｜ファイルのパス:行番号｜引用｜判定」にする。
    最後に、説明全体のうち、どの部分が名前や構成からの推測だったかを挙げる。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.12。

<!-- textlint-enable -->
<!-- gen:end snippet explore-a-codebase/recheck-claims -->

「本当にそう？」と聞くだけでは、根拠を示さずに前の説明を言い直すことがある。引用を求めると、その場でコードを読み直す手間が入るので、合わない主張が見つかりやすい。処理の流れと入力の端を説明させ、実際の動きと照らす手順は、生成コードを採る前の確かめと同じである。詳しくは <!-- link:begin own-generated-code#check-explanation -->[生成コードを自分のものにする › 説明を実際の動きと照らす](../verify/own-generated-code.md#check-explanation)<!-- link:end --> が扱う。

重要な主張は、同じ質問を新しい会話でもう一度して、答えが一致するかを見る手もある。やり方は <!-- link:begin fact-checking#best-of-n -->[事実を確かめる（引用・照合・best-of-N） › 何度か聞いて比べる（best-of-N）](../verify/fact-checking.md#best-of-n)<!-- link:end --> が扱う。一致しても正しいとは限らない。一致しない主張は、読み直す箇所の目印になる。

## 地図と用語集を残す {#keep-a-map}

読んで分かったことは、地図と用語集として、リポジトリの中の別のファイルへ残す。会話の中だけに置くと、新しいセッションでまた同じ所を読み直すことになる。残しておけば、次に読むときの出発点になる。

- 地図：ディレクトリごとの役割と、読んだ処理ごとの通り道を、ファイルのパスと関数名で書く。行番号は、コードが変わるとすぐずれるので、地図には書かない。どの時点のコードを読んだかを、日付と commit で末尾に書き、古くなったと分かるようにする。
- 用語集：このプロジェクト固有の語（コード内の名前・略語・ドメイン用語）を、1 語 1〜2 行で書く。ドメイン用語で頼むと関連コードが探しやすくなるので、用語集は次の質問の道具にもなる。

頼み方の雛形を次に置く。

<!-- gen:begin snippet explore-a-codebase/write-map -->
<!-- textlint-disable -->

??? example "雛形：読んで分かったことを、地図と用語集に残させる依頼"

    ```markdown
    ここまでに読んで分かったことを、リポジトリの中の、CLAUDE.md とは別の 2 つのファイルにまとめてほしい。
    ファイルを作る前に、置き場所と名前の案を私に見せ、承認を待つ。CLAUDE.md には書かない。

    1. 地図（`docs/codebase-map.md` の案）
       - 主な構成：ディレクトリごとに、役割を 1 行で書く
       - 主な流れ：読んだ処理ごとに、入口から通る順にファイルのパスと関数名を並べる
       - 末尾に「どの時点のコードを読んだか」として、日付と `git rev-parse --short HEAD` の結果を書く

    2. 用語集（`docs/glossary.md` の案）
       - このプロジェクト固有の語（コード内の名前、略語、ドメイン用語）を、1 語 1〜2 行で書く
       - 各語に、使われている代表的なファイルのパスを 1 つ添える

    守ること：
    - 実際に読んだ所だけを書く。読んでいない所は「未読」と書く
    - 行番号は、すぐずれるので地図には書かない。ファイルのパスと関数名で指す
    - 分からなかったことは、最後に「未解決」として並べる
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.12。

<!-- textlint-enable -->
<!-- gen:end snippet explore-a-codebase/write-map -->

地図と用語集は CLAUDE.md には書かず、別のファイルに置く。Claude はリポジトリを自分で読めるので、構成やファイルの並びを CLAUDE.md に書く助言は、今は勧められていない。CLAUDE.md に残すのは、リポジトリを読んでも分からないことに絞る。この助言の変化は <!-- link:begin outdated-advice-ledger#architecture-in-claude-md -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#architecture-in-claude-md)<!-- link:end --> にあり、残す行と外す行の見分け方は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> が扱う。`/init` で CLAUDE.md の叩き台を作る手は <!-- link:begin init-and-first-claude-md#run-init -->[/init と最初の CLAUDE.md › /init で叩き台を作る](../cli/init-and-first-claude-md.md#run-init)<!-- link:end --> が扱う。

地図は、Claude が書いた文章を人が確かめないまま残すと、誤りを固定してしまう。残す前に、地図の中のパスと関数名の数か所を、自分で開いて確かめる。

## 他人のリポジトリを開くとき {#unknown-repos}

他人のリポジトリは、読み始める前に、開くだけで動きうるものがないかを確かめる。設定・フック・MCP の定義が入っていると、中身を読ませる前に動くことがある。開く前に見るファイルと、信頼の確認が出る前後で効くものは <!-- link:begin before-opening-unknown-repos#files-to-check -->[知らないリポジトリを開く前に › 開く前に見るファイル](../safety/before-opening-unknown-repos.md#files-to-check)<!-- link:end --> と <!-- link:begin before-opening-unknown-repos#trust -->[知らないリポジトリを開く前に › 信頼の前と後で効くもの](../safety/before-opening-unknown-repos.md#trust)<!-- link:end --> が扱う。

読み進める途中で、依存のパッケージを入れる場面もある。存在しない名前や後から登録された名前に注意し、入れる前に確かめる。その手順は <!-- link:begin vetting-extensions#dependencies -->[MCP・プラグイン・スキルを入れる前の確認 › 依存のパッケージを入れる前に（存在しない名前・後から登録された名前）](../safety/vetting-extensions.md#dependencies)<!-- link:end --> が扱う。

## 理解できたかの確かめ方 {#overall-check}

読み終えたら、自分の理解を全体で確かめる。Claude の説明が正しいことと、自分が分かったことは別だからである。

- 追った処理を、自分の言葉で、ファイルを見ずに言い直す。言い直せない所が、読み直す箇所になる。手順は <!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end --> が扱う。
- 「この処理に項目を 1 つ足すなら、どのファイルのどこを変えるか」を Claude に聞き、答えの箇所を自分で開く。変える箇所が見当違いなら、まだ全体をつかめていない。
- 地図の通りにコードをたどり、実在しないパスや関数名がないかを数か所で確かめる。

中核になる部分は、説明できるまで理解を確かめる。周辺の部分は、地図に任せてよい。線の引き方は <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](../judgment/how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end --> が扱う。AI を介した学びで理解が残りにくいことは <!-- link:begin learning-with-ai#faster-but-shallower -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 速さの得は確かめられず、理解は残りにくい](../judgment/learning-with-ai.md#faster-but-shallower)<!-- link:end --> が扱う。仕様書や規約が別にあるときは、原文を先に自分で読む手が <!-- link:begin read-specs-yourself#read-first -->[仕様を自分で読み、AI に誤読を指摘させる › 先に自分で読んで要約する](read-specs-yourself.md#read-first)<!-- link:end --> にある。

## うまくいかないとき {#when-it-fails}

症状ごとに、見るページが違う。

- 説明に存在しないファイル・関数・パッケージが出てくる：<!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](../symptoms/uses-nonexistent-apis.md#diagnosis)<!-- link:end --> で原因を切り分ける。読ませた範囲が足りない場合は、入口を `@` で直接指して、読ませ直す。
- 説明の行番号が実際のコードと合わない：該当の主張を捨て、「説明をコードで確かめる」の 2 つ目の手の雛形で、主張ごとに引用を取り直す。繰り返し合わないときは、新しいセッションで範囲を狭めてやり直す（推論・実践例なし）。
- 流れを追っている途中で、バグらしい挙動が見つかった：読む作業をいったん止め、<!-- link:begin fix-a-bug -->[バグを直す](fix-a-bug.md)<!-- link:end --> の手順に移る。読む作業の中で、そのままコードを直させない。
- 読んだ内容を、自分では説明できない：<!-- link:begin how-much-understanding-to-keep -->[どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)<!-- link:end --> で、どこまで理解を手放すかを決める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)

**関連**

- [仕様を自分で読み、AI に誤読を指摘させる](read-specs-yourself.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [code intelligence プラグイン（LSP）](../extend/code-intelligence-plugins.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- [MCP・プラグイン・スキルを入れる前の確認 › 依存のパッケージを入れる前に（存在しない名前・後から登録された名前）](../safety/vetting-extensions.md#dependencies)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [/init と最初の CLAUDE.md](../cli/init-and-first-claude-md.md)
- [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- [バグを直す](fix-a-bug.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
