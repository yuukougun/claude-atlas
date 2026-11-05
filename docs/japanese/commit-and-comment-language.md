---
id: commit-and-comment-language
title: コミットメッセージ・コメントの言語
aliases: [コミットを日本語で書かせる, コードのコメントの言語, CLAUDE.local.md に置く]
type: concept
field: japanese
chapter: 返答とコミットの言語
order: 40
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
scenes: [開発, チーム]
summary: コミットメッセージとコメントの言語はチームの決まりとして共有の指示に書き、個人の好みは個人の設定に分けて置く。返答の言語の設定がそこまで効くかは公式に書かれていない。
signs:
  - {type: goal, text: コミットメッセージは日本語、コードのコメントは英語にしたい}
  - {type: situation, text: OSS で、自分だけ日本語で返事をもらいたい}
  - {type: symptom, text: 返事は日本語なのに、コミットメッセージだけ英語になる}
prerequisites: [keep-replies-in-japanese]
related: [settings-layers, claude-md-loading-order, what-to-put-in-claude-md, working-with-git, share-team-settings, cloud-sessions-and-teleport, hook-recipes]
tracks: [language-setting, claude-md, settings]
sources: [cc-docs-settings-reference, cc-docs-settings, cc-docs-memory, cc-docs-cloud-environments, cc-docs-claude-code-on-the-web]
volatility: 中
sections:
  - {title: チームの決まりと個人の好みを分ける, anchor: team-vs-personal}
  - {title: 共有の設定の言語は個人の設定を上書きする, anchor: override}
  - {title: クラウドのセッションに届く指示, anchor: cloud}
  - {title: 何に効くか, anchor: effects}
  - {title: 設定がどこまで効くかは確かめる（検証ノート）, anchor: verify-note}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：コミットとコメントの言語はチームの決まりとして共有の指示に書き、個人の好みは個人の層に分けると、ぶつからない。
    - **いつ引くか**：コミットを日本語、コメントを英語にしたいとき。OSS で自分だけ日本語の返事がほしいとき。返事は日本語なのにコミットだけ英語になるとき。
    - **前提**：<!-- link:begin keep-replies-in-japanese -->[日本語で返し続けさせる](keep-replies-in-japanese.md)<!-- link:end -->
    - **注意**：返答の言語の設定がコミットとコメントにまで効くかは、公式の文書に書かれていない。

<!-- textlint-disable -->
別名：コミットを日本語で書かせる・コードのコメントの言語・CLAUDE.local.md に置く
<!-- textlint-enable -->

コミットメッセージとコメントの言語は、Claude にコミットやコードの編集を任せたときに決める必要が出る。返答の言語とは別の決まりとして扱うと、チームの設定と個人の好みが衝突しにくい。

## チームの決まりと個人の好みを分ける {#team-vs-personal}

コミットメッセージとコメントの言語は、チームの決まりと個人の好みを別の場所に書き分けるのが基本である。

起きがちなのは、返答は日本語なのにコミットメッセージだけ英語になる、という食い違いである。原因は 2 つ考えられる。コミットの言語をどこにも書いていないか、書いてあっても Claude に届いていないか、である。返答の言語を決める `language` の設定は、公式の文書では「いつもその言語で答える」指示として渡されるものである。コミットやコメントに効くとは書かれていない。詳しい扱いは <!-- link:begin keep-replies-in-japanese#language-setting -->[日本語で返し続けさせる › 言語の設定と、効かないときに確かめること](keep-replies-in-japanese.md#language-setting)<!-- link:end --> を見る。

決めたいことごとに、置き場所と効く人は次のように分かれる。

| 置き場所 | 決めること | 効く人 |
| --- | --- | --- |
| リポジトリの `CLAUDE.md` | コミットメッセージとコメントの言語（チームの決まり） | 全員。クラウドのセッションにも届く |
| `.claude/settings.local.json` の `language` | 自分への返答の言語（このプロジェクトだけ） | 自分だけ。クラウドには届かない |
| `~/.claude/settings.json` の `language` | 自分への返答の言語（全プロジェクト） | 自分だけ。クラウドには届かない |
| `CLAUDE.local.md` | このプロジェクトでの自分だけの書き方の好み | 自分だけ。クラウドには届かない（推論・実践例なし） |

チームの決まりは、共有の `CLAUDE.md` に短く書く。決まりの本文のほかに、理由を 1 行添える。理由があると、決まりの外の場面でも Claude が判断しやすい。何を `CLAUDE.md` に書き、何を外すかは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> を見る。

<!-- gen:begin snippet commit-and-comment-language/team-claude-md -->
<!-- textlint-disable -->

??? example "雛形：チームの言語の決まり（リポジトリの CLAUDE.md）"

    ```markdown
    ## 言語の決まり

    - コミットメッセージは日本語で書く。件名も本文も日本語にする
    - コードのコメントは英語で書く
    - 変数名・関数名・コマンド・パスは原文のままにする
    - 理由：コミットの履歴はチーム全員が日本語で読む。コードは外部の貢献者も読むので、コメントは英語にそろえる
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet commit-and-comment-language/team-claude-md -->

個人の好みは、コミットされない `CLAUDE.local.md` に置く。公式の文書では、プロジェクトの根に置いて `.gitignore` に足すものとして書かれている。`CLAUDE.md` の後に読み込まれ、同じ扱いになる。読み込みの順は <!-- link:begin claude-md-loading-order#order -->[CLAUDE.md の階層と読み込み順 › 読み込まれる場所と順番](../extend/claude-md-loading-order.md#order)<!-- link:end --> を見る。

OSS で自分だけ日本語の返事がほしいときは、返答の言語だけを個人の層に置く。コミットとコメントは、そのリポジトリの決まりに従わせる。次のように、範囲を言葉で区切っておく。

<!-- gen:begin snippet commit-and-comment-language/personal-local -->
<!-- textlint-disable -->

??? example "雛形：自分だけの返答の言語（CLAUDE.local.md）"

    ```markdown
    ## 私への返答の言語

    - 私への返答（会話）は日本語で行う
    - コミットメッセージ・コードのコメント・PR の文面は、このリポジトリの決まりと既存の履歴に従う。日本語にしない
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet commit-and-comment-language/personal-local -->

`AGENTS.md` を使うリポジトリでは注意がいる。公式の文書（2026-11-05 に確認）では、`AGENTS.md` があって `CLAUDE.md` がないとき、Claude は既定で `AGENTS.md` を読む。

そこへ `CLAUDE.local.md` を足すと、既定では `AGENTS.md` を読まなくなる。両方を読ませる選び方が設定にある。名前と手順は、公式の文書「How Claude remembers your project」を見る。

線引きの考え方は次にまとめてある。

- <!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end -->

## 共有の設定の言語は個人の設定を上書きする {#override}

共有のプロジェクト設定に `language` を入れると、各人が `~/.claude/settings.json` に書いた `language` より優先される。つまり、共有に入れた時点で、全員の返答の言語を決めたことになる。

公式の文書にある設定の優先順は、強い順に次のとおりである。

1. 管理設定
2. `--settings` で渡したもの
3. `.claude/settings.local.json`
4. `.claude/settings.json`
5. `~/.claude/settings.json`

`language` のように値が 1 つのキーは、上の層が下の層を上書きする。リストのキーのように合わさることはない。層の考え方は <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end -->、合わさる設定と上書きされる設定の違いは <!-- link:begin settings-layers#merge -->[設定ファイルの階層と優先順位 › 合わさる設定、上書きされる設定](../cli/settings-layers.md#merge)<!-- link:end --> を見る。

この順から、置き場所の判断が出る。

- チーム全員の返答の言語をそろえたいなら、共有の `.claude/settings.json` に入れてよい
- 自分だけ違う言語にしたいなら、共有には入れない。共有に入っていても、`.claude/settings.local.json` なら上書きできる
- OSS のように、ほかの人の言語を決める立場にないなら、`language` は個人の層に置く

自分のプロジェクトだけ上書きするなら、次の設定を `.claude/settings.local.json` に置く。

<!-- gen:begin snippet commit-and-comment-language/settings-local-language -->
<!-- textlint-disable -->

??? example "雛形：自分だけの返答の言語（.claude/settings.local.json）"

    ```json
    {
      "language": "japanese"
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.0。

<!-- textlint-enable -->
<!-- gen:end snippet commit-and-comment-language/settings-local-language -->

!!! example "判断例：OSS で自分だけ日本語の返事がほしい"
    - **状況**：英語で運営している OSS のリポジトリで、自分への返事は日本語にしたい。コミットとコメントは、これまでどおり英語にしたい。
    - **迷う候補**：`~/.claude/settings.json` に `language` を置くだけにする。または、`CLAUDE.local.md` に「返答は日本語、コミットとコメントは英語」と書く。どちらも筋が通る。
    - **選んだもの**：`language` は個人の層に置き、`CLAUDE.local.md` にも「コミットとコメントは英語」と 1 行足す。
    - **理由**：`language` がコミットやコメントに効くかは公式に書かれていない。効く範囲を言葉で区切っておけば、効いたかどうかによらず英語のままになる。

## クラウドのセッションに届く指示 {#cloud}

クラウドのセッションには、個人の層に置いた言語の指示は届かない。公式の文書では、クラウドのセッションは次のものを読まない。

- `~/.claude/settings.json`
- `.claude/settings.local.json`
- `~/.claude/CLAUDE.md`

一方、リポジトリの `.claude/settings.json` は、1 つのリポジトリのセッションでは読まれる。リポジトリの `CLAUDE.md` に書いたチームの決まりは、手元とクラウドのどちらにも同じように届く。

`CLAUDE.local.md` は `.gitignore` に入れるので、リポジトリを取得するクラウドのセッションには入らないと考えられる（推論・実践例なし）。クラウドでも自分の好みを効かせたいなら、環境の setup script で `~/.claude/CLAUDE.md` を書く方法が公式にある。公式の例は、コミットメッセージの好みである。

クラウドへ送る前に、コミットの言語の決まりがリポジトリの `CLAUDE.md` にあるかを確かめる。送り方と手元の設定との違いは <!-- link:begin cloud-sessions-and-teleport#settings -->[クラウドセッションと teleport › 手元の設定との違い](../cli/cloud-sessions-and-teleport.md#settings)<!-- link:end -->、読み込みの全体は <!-- link:begin claude-md-loading-order#after-compaction -->[CLAUDE.md の階層と読み込み順 › 圧縮の後と、クラウドのセッション](../extend/claude-md-loading-order.md#after-compaction)<!-- link:end --> を見る。サブエージェントや圧縮の後など、ほかの届かない所は <!-- link:begin keep-replies-in-japanese#reach -->[日本語で返し続けさせる › 届かない所（サブエージェント・圧縮の要約・クラウドのセッション）](keep-replies-in-japanese.md#reach)<!-- link:end --> にある。

## 何に効くか {#effects}

コミットとコメントの言語を、チームの決まりと個人の好みに分けて書く方法は、原理の「見せる」には強く効き、「縛る」には弱くしか効かない。防ぐ原因は「見えていない」と「縛っていない」の 2 つである。

- **見せる**：決まりを、Claude が読む場所に書く。リポジトリの `CLAUDE.md` に書けば、コミットの言語の決まりは手元とクラウドの両方で見える。個人の層に置いた指示がクラウドで見えないのは、見えていない原因の典型である
- **縛る**：守られなかったら止める仕組みを置く。`CLAUDE.md` は文脈であり、強制ではない。公式の文書も、必ず止めたいなら PreToolUse フックを使うと書く。コミットの言語を「縛る」なら、コミットを実行するコマンドの前でメッセージを調べ、日本語でなければ止めて理由を返す形になる。ただし、言語の判定のしかたに公式の例はない

Claude にコミットまで任せる段階では、まず見せる。そのうえで、守られているかを履歴で確かめる。確かめて揺れるなら、フックを足す。フックの組み方と常設する前の確かめ方は、<!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end --> と <!-- link:begin hook-recipes#verify -->[代表的なフックのレシピ › 常設する前に確かめる](../enforce/hook-recipes.md#verify)<!-- link:end --> を見る。コミットを人が握るか任せるかの段階は <!-- link:begin working-with-git#who-commits -->[git との付き合い方 › 誰がコミットするか](../cli/working-with-git.md#who-commits)<!-- link:end --> にある。

## 設定がどこまで効くかは確かめる（検証ノート） {#verify-note}

`language` の設定がコミットメッセージとコメントに効くかは、公式の文書に書かれていない。2026-11-03 に、公式の文書の全文から `language` の記述を探した。コミットメッセージ・コードのコメント・圧縮の要約・思考の要約に効くかどうかを述べた箇所は、見つからなかった。

ある解説記事は、`language` はコメントやコミットメッセージには効かないと書く。しかし、この辞典はその記事を読めず、公式の文書でも確かめられなかった。そのため、効くか効かないかの結論は出せない。この辞典では、実際に試した記録は持っていない（2026-11-05 時点）。

自分の環境で確かめるなら、使い捨てのリポジトリで次のように試す。偽のファイルだけを使い、壊れて困る操作はしない。

1. 新しいセッションで、`claude --version` を控える
2. `language` を `japanese` にし、`CLAUDE.md` にコミットの言語の指示を書かない
3. 小さなファイルの変更を頼み、コミットさせる。`git log` で件名と本文の言語を見る
4. コメントを足す変更を頼み、足されたコメントの言語を見る
5. `CLAUDE.md` にコミットの言語の決まりを足して、3 と 4 をもう一度試す

結果は、日付・Claude Code の版・モデル・試した場所（手元の CLI またはクラウド）と一緒に控える。1 回の結果は揺れるので、同じ依頼を数回試す。2 つの条件の差が出たかを、数えて比べる。

## 誤解されやすいこと {#misconceptions}

- **「`language` はコメントやコミットに効かない」**：公式の文書に記述がないだけで、効かないと確かめられたわけではない。確かめるまでは、決まりを `CLAUDE.md` に書いて補う
- **「共有の設定に `language` を入れても、各人が上書きできる」**：個人の `~/.claude/settings.json` では上書きできない。上書きできるのは、優先順が上の `.claude/settings.local.json` などである
- **「`CLAUDE.md` に書けば必ず守られる」**：`CLAUDE.md` は文脈として渡されるお願いで、強制ではない。守らせたいなら、フックで確かめる
- **「クラウドでも手元と同じ設定が効く」**：個人の層の設定と `~/.claude/CLAUDE.md` は届かない。チームの決まりはリポジトリに置く

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [日本語で返し続けさせる](keep-replies-in-japanese.md)

**関連**

- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [CLAUDE.md の階層と読み込み順](../extend/claude-md-loading-order.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [git との付き合い方](../cli/working-with-git.md)
- [チームで設定を共有する](../team/share-team-settings.md)
- [クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
