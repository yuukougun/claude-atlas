---
id: move-judgment-into-scripts
title: 判断を決定論的なスクリプトに移す
aliases: [LLM にスクリプトを書かせる, 決定論的な道具に置き換える]
type: concept
field: enforce
chapter: 何を縛るか
order: 30
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, api]
principle: [縛る, 確かめる]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 毎回 Claude に判断させている作業を、Claude に書かせたスクリプトに移せる。結果が毎回同じになり、確かめやすくなる。
signs:
  - {type: goal, text: 同じ集計や変換を、毎回 Claude にやらせている}
  - {type: symptom, text: 同じ集計なのに、頼むたびに数字が少しずつ違う}
prerequisites: [request-vs-lock, nondeterminism]
related: [when-to-lock, request-lock-table, mcp-or-cli, shrink-failing-inputs, bisect-regressions, build-observation-tools, hook-recipes, writing-skills, designing-agent-tools]
tracks: [skills, hooks]
sources: [cc-docs-hooks-guide, cc-docs-skills]
volatility: 低
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜそうなるか, anchor: why}
  - {title: 移す作業の見分け方, anchor: what-to-move}
  - {title: 書かせたスクリプトを確かめる, anchor: check-the-script}
  - {title: スクリプトの置き場所, anchor: where-to-put}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：毎回 Claude に判断させている集計や変換を、書かせたスクリプトで動かすと、結果が毎回同じになり、確かめやすくなる。
    - **いつ引くか**：同じ集計や変換を毎回 Claude にやらせているとき。同じ集計なのに頼むたびに数字が少しずつ違うとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->・<!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end -->

<!-- textlint-disable -->
別名：LLM にスクリプトを書かせる・決定論的な道具に置き換える
<!-- textlint-enable -->

判断を決定論的なスクリプトに移すとは、毎回 Claude が読んで答えを出していた作業を、Claude が書いたスクリプトで置き換えることである。置き換えた後は、Claude が毎回答えを出すのではなく、スクリプトが毎回同じ手続きで動く。このページは、どの作業を移すか、移した後に何を確かめるかを扱う。

## 何が起きるか {#what-happens}

毎月のアクセスログから、カテゴリごとの金額の合計を出す作業を、毎回 Claude に頼んでいる場面を考える。頼み方は同じなのに、月をまたぐと、あるいは同じ月でも頼み直すたびに、合計が少しずつ違うことがある。どれが正しいかは、自分で数え直さないと分からない。

Before と After を同じ依頼で並べる。

```text
Before：
logs/ の CSV から、category ごとの amount の合計を出してください。

After：
logs/ の CSV から、category ごとの amount の合計を出すスクリプトを
scripts/aggregate.py に書いてください。合計は、そのスクリプトを流した
結果を使ってください。
```

After では、答えそのものではなく、答えを出す手続きを書かせている。手続きは一度書かれれば、同じ入力に対して同じ出力を返す。次の月からは、Claude に数えさせず、そのスクリプトを流す。Before と After の違いは「合計を出して」と頼むか、「合計を出す手続きを書いて、それで出して」と頼むかだけである。具体的な依頼文の雛形は、次の節で示す。

入力の縮小でも、同じ傾向が報告されている。大きな失敗入力を最小の再現例に縮める作業では、LLM に直接縮めさせるより、縮めるスクリプトを書かせるほうが強いという結果がある。ただし、1 件の研究からの一般化であり、研究の名・年・対象のモデルはここでは示せない。集計や変換への当てはめも類推である（根拠：中・類推）。縮小の手順そのものは <!-- link:begin shrink-failing-inputs -->失敗する入力を縮めるスクリプトを書かせる（準備中）<!-- link:end --> に任せる。

## なぜそうなるか {#why}

Claude の答えは、文章を生成する過程で出る。数や集計も同じ過程で出るので、同じ入力でも毎回同じ結果になるとは限らない。なぜ答えが変わるかは <!-- link:begin nondeterminism#why -->[同じ質問でも答えが変わる（非決定性） › なぜ答えが変わるか](../basics/nondeterminism.md#why)<!-- link:end --> で扱っている。

スクリプトは、書かれた手続きを機械が実行する。入力が同じなら、出力も同じになる。これが「決定論的」の意味である。ただし、これは再現できるということであり、正しいということではない。正しさは、移した後に別に確かめる必要がある。

お願いと鍵の見方でいうと、「毎回こう数えてください」と頼むのはお願いで、スクリプトで数えるのは、数え方を機械の側に固定する鍵にあたる。指示の側の話は <!-- link:begin request-vs-lock#why -->[お願いと鍵（決定論的か、非決定論的か） › なぜそうなるか](../basics/request-vs-lock.md#why)<!-- link:end --> にある。ここでの鍵は、フックや deny ルールのように Claude の動作を止めるものではなく、作業の手続きを固定するものである。

## 移す作業の見分け方 {#what-to-move}

移す作業かどうかは、次の問いで見分ける。

- 入力と出力の形を、先に書けるか。
- 正解を機械で計算できるか、または別の方法で検算できるか。
- 同じ頼みを繰り返しているか。
- 途中の数のずれが、結果に紛れて気付かれにくいか。

これらに「はい」が多いほど、移す候補になる。逆に、文の意味の解釈、あいまいな分類、要約、原因の仮説出しのように、正解が 1 つに決まらない作業は、Claude に残す。

| 作業の性質 | 置き場 |
| --- | --- |
| 数える・合計する・並べ替える・形式を変換する | スクリプト |
| 規則が書き切れる検査（形式・件数・重複） | スクリプト |
| 意味の解釈・あいまいな分類・要約 | Claude |
| 両方が混ざる作業 | 分けて、機械で決まる部分をスクリプトへ |

混ざる作業は分ける。たとえば問い合わせメールの集計なら、各メールの分類は Claude が判断し、分類結果の件数の集計はスクリプトが数える。判断を含む規則を機械に押し込むと、境界の例で破綻する。鍵にしないほうがよい規則の考え方は <!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](when-to-lock.md#what-not-to-lock)<!-- link:end --> と同じである。

!!! example "判断例：アンケートの毎週の集計"
    - **状況**：毎週、アンケートの回答から、選択式の設問の件数集計と、自由記述の要約を Claude に頼んでいる。件数が週ごとに少しずれる。
    - **迷う候補**：全部をこれまでどおり Claude に頼む。全部をスクリプトにする。
    - **選んだもの**：件数集計だけをスクリプトに移し、自由記述の要約は Claude に残す。
    - **理由**：件数集計は、規則が書き切れて検算できるので、移すと毎週同じ結果になる。要約は正解が 1 つに決まらず、規則に書き切れないので、スクリプトにはできない。

依頼の雛形は次のとおり。角括弧の欄を、自分の入力と規則で埋める。

<!-- gen:begin snippet move-judgment-into-scripts/ask-for-script -->
<!-- textlint-disable -->

??? example "雛形：繰り返す集計をスクリプトにさせる依頼"

    ```text
    次の集計を、毎回あなたが数える代わりに、スクリプトにして `scripts/aggregate.py` に書いてください。

    - 入力：<入力ファイルの場所と形式。例：logs/ の CSV。列は date, category, amount>
    - 出力：<出力の形。例：category ごとの amount の合計と件数を、CSV で標準出力へ>
    - 規則：<数え方の決まり。例：amount が空の行は合計に入れず、除外した件数を別に出す>
    - 判断が要る所：<例：category の表記ゆれは、スクリプトで直さず、未知の値として一覧に出す>

    守ること：
    - 同じ入力から、同じ出力が出るようにする（乱数・現在時刻・並びが不定の処理を使わない）。
    - 入力の行数が、集計した行数と除外した行数の合計に合うことを、最後に確かめて表示する。
    - 書いたら、手計算できる小さな入力（5 行ほど）を作り、期待する出力を先に書いてから、スクリプトを流して突き合わせる。

    まだ実際の入力には流さず、スクリプトと、小さな入力での突き合わせの結果だけを見せてください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet move-judgment-into-scripts/ask-for-script -->

## 書かせたスクリプトを確かめる {#check-the-script}

スクリプトは同じ間違いを毎回再現する。決定論的に動くからこそ、間違った手続きがそのまま固定される。流して合計が出た時点では、確かめたことにならない。書かせたスクリプトは、次の順で確かめる。

1. 手計算できる小さな入力を作り、期待する出力を先に自分で書く。流した結果と突き合わせる。小さな例で手計算と合うかを先に確かめる考え方は、<!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end --> と同じである。
2. 同じ入力で 2 回流して、出力が一致することを見る。
3. 入力の行数が、集計した行数と除外した行数の合計に合うことを見る。規則で除外する行は、除外した件数も出力させる。
4. 空のファイル・ヘッダーだけのファイル・欠損の多い入力・想定外の値を含む入力で、黙って違う結果を出さないことを見る。
5. 実際の入力に流して、手元の別の数（概算や前回の値）とだいたい合うかを見る。

Claude に「このスクリプトは正しいか」と聞いても、確かめたことにはならない。コードの説明ではなく、実際に流した入力と出力を見せるよう頼む。そのための依頼の雛形を示す。

<!-- gen:begin snippet move-judgment-into-scripts/review-the-script -->
<!-- textlint-disable -->

??? example "雛形：書かせたスクリプトを流して確かめさせる依頼"

    ```text
    scripts/aggregate.py を、次の点で確かめてください。コードの説明ではなく、実際に流した結果を見せてください。

    1. 同じ入力で 2 回流し、出力が完全に一致するか。
    2. 入力の行数 = 集計した行数 + 除外した行数 になっているか。
    3. 次の入力で壊れないか：空のファイル・ヘッダーだけのファイル・amount が空の行だけのファイル・想定外の category を含むファイル。
    4. 手計算できる小さな入力で、私が書いた期待値と一致するか。期待値：<自分で手計算した値>

    食い違いがあれば、直す前に、どの入力でどの値が食い違ったかを報告してください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet move-judgment-into-scripts/review-the-script -->

!!! example "判断例：流したら、手元の概算と合わない"
    - **状況**：書かせた集計スクリプトを実際のログに流したら、合計が、前回の値から見込める範囲とずれている。
    - **迷う候補**：Claude に同じ集計を直接やり直させて、2 つの結果を比べる。小さな入力に切り出して、手計算と突き合わせる。
    - **選んだもの**：小さな入力に切り出して、手計算と突き合わせる。
    - **理由**：Claude に直接やり直させた結果も、頼むたびに変わりうるので、比べる相手として弱い。手計算は、どこで食い違うかを特定できる。

確かめて直したスクリプトは、リポジトリに置いて、版を管理する。毎回「集計して」と頼んで毎回スクリプトを書かせ直すと、書かれるスクリプトが毎回違いうるので、移した意味が薄れる。

## スクリプトの置き場所 {#where-to-put}

スクリプトを置く場所は、どう呼ぶかで決める。この辞典で扱う機能のうち、スキルとフックの違いを次に示す。

<!-- gen:begin compare 強制力 読み込みの時期 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 |
| --- | --- | --- |
| [スキル（skills）](../extend/writing-skills.md) | お願い | セッション開始と使うとき |
| [フック（hooks）](hooks-basics.md) | 鍵 | イベントが起きたとき |

すべて共通：圧縮で残るか 残る。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 圧縮で残るか -->

面ごとの手段は次のとおり。

=== "Claude Code"
    - 頼まれたときだけ流すなら、リポジトリに置いて、Claude に Bash で実行させる。
    - 繰り返す手順なら、スキルの補助ファイルとしてスクリプトを置く。置き方は、<!-- link:begin writing-skills#supporting-files -->[スキルの作り方 › 補助ファイルとスクリプトに分ける](../extend/writing-skills.md#supporting-files)<!-- link:end --> にある。
    - Claude の判断に任せず、決まった場面で毎回流したいなら、フックのコマンドとしてスクリプトを呼ぶ。フックの組み方は <!-- link:begin hook-recipes#guards -->[代表的なフックのレシピ › 先に整える守り](hook-recipes.md#guards)<!-- link:end --> から始める。
    - 外部の道具としてつなぐか、CLI で済ませるかの選び方は <!-- link:begin mcp-or-cli -->[MCP か CLI か](../extend/mcp-or-cli.md)<!-- link:end --> にある。

=== "API"
    - 処理を自分のプログラムの側に書き、モデルには結果だけを渡す。
    - モデルに呼ばせたいなら、処理を道具として定義し、道具の中でスクリプトと同じ手続きを走らせる。道具の作り方は <!-- link:begin designing-agent-tools -->エージェント用のツールを設計する原則（準備中）<!-- link:end --> にある。
    - 具体的な呼び出しの書き方は、この辞典では扱わない。公式の文書を参照する。

## 何に効くか {#effects}

このページの内容は、原理の「縛る」と「確かめる」、原因の「縛っていない」と「確かめていない」に関わる。

- **縛る**：毎回 Claude の判断に任せていた作業の手続きを、スクリプトとして固定する。同じ入力なら同じ手続きが走るので、結果のぶれがなくなる。これは、お願いを鍵に移す考え方の延長である。お願いと鍵の対応は <!-- link:begin request-lock-table#table -->[お願いと鍵の対応表 › 用途ごとの対応表](request-lock-table.md#table)<!-- link:end --> で選べる。
- **確かめる**：出力が再現でき、検算の手段（小さな入力・行数の突き合わせ）を持てる。結果のぶれに気付けない状態から、ぶれを見つけられる状態に変わる。
- **縛っていない（原因）**：手続きを決めずに毎回判断させている状態を直す。
- **確かめていない（原因）**：結果を検算する手段を持たない状態を直す。ただし、確かめる作業そのものは省けない。

## 誤解 {#misconceptions}

- **スクリプトにすれば正しくなる**：決定論的なのは再現性であり、正しさではない。間違った手続きは、毎回同じ間違いを返す。書かせたら、小さな入力での手計算の突き合わせなど、確かめる手順を踏む。
- **全部の作業を移せる**：判断が要る部分は移せない。無理に規則へ押し込むと、境界の例で破綻する。移す作業の見分け方に従い、混ざる作業は分ける。
- **temperature を下げれば同じ結果になる**：この助言は、今の Claude では使えない。事情は <!-- link:begin nondeterminism#temperature-advice -->[同じ質問でも答えが変わる（非決定性） › temperature を下げる助言は今は使えない](../basics/nondeterminism.md#temperature-advice)<!-- link:end --> にある。
- **毎回スクリプトを書かせ直せばよい**：書かせるたびにスクリプトが変わりうる。確かめた版を置いて、それを流す。
- **移したら Claude は要らなくなる**：スクリプトを書く・直す・結果を読んで次の判断をするのは、Claude の仕事のままである。移すのは、毎回同じ手続きで済む部分だけである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)

**関連**

- [お願いを鍵に移す判断](when-to-lock.md)
- [お願いと鍵の対応表](request-lock-table.md)
- [MCP か CLI か](../extend/mcp-or-cli.md)
- 失敗する入力を縮めるスクリプトを書かせる（準備中）
- 退行の原因を git bisect で探させる（準備中）
- [観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)
- [代表的なフックのレシピ](hook-recipes.md)
- [スキルの作り方](../extend/writing-skills.md)
- エージェント用のツールを設計する原則（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
