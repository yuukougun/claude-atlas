---
id: what-feedback-sends
title: /feedback・トランスクリプトの共有で送られるもの
aliases: [/feedback, /bug, /share, transcript の共有, フィードバックで送られるもの, テレメトリ]
type: feature
field: safety
chapter: データの扱い
order: 50
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: /feedback やトランスクリプトの共有に応じると、会話とコードが送られて長く残ることを知り、送る前に中身を選べる。/share は共有のリンクを作る機能ではない。
signs:
  - {type: situation, text: 不具合を /feedback で報告しようとしている}
  - {type: situation, text: セッションの評価の後に、トランスクリプトを共有するか聞かれた}
prerequisites: [where-your-data-goes]
related: [protecting-secrets, shared-artifacts-and-files, entrusted-data, default-safety-settings, audit-logs-and-telemetry]
tracks: [feedback]
sources: [cc-docs-data-usage, cc-docs-commands, privacy-long-store-data]
volatility: 中
sections:
  - {title: 送られるものと残る期間, anchor: what-is-sent}
  - {title: 送る前に決める, anchor: before-sending}
  - {title: /share は共有のリンクではない, anchor: share-is-bug}
  - {title: テレメトリと報告の機能を止める, anchor: telemetry}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：/feedback は、コードを含む会話の履歴の写しを Anthropic に送り、長く残る。送る前に履歴の範囲と中身を選べる。
    - **いつ引くか**：不具合を /feedback で報告しようとしているとき。セッションの評価の後に、トランスクリプトを共有するか聞かれたとき。
    - **前提**：<!-- link:begin where-your-data-goes -->[送ったデータの行方（学習・保持期間）](where-your-data-goes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：/feedback・/bug・/share・transcript の共有・フィードバックで送られるもの・テレメトリ
<!-- textlint-enable -->

/feedback・トランスクリプトの共有で送られるものを確かめるページである。不具合の報告と、セッションの評価の後の共有は、どちらも会話の中身を Anthropic に渡す操作である。手元に残る記録とは別の経路であり、送る前に中身を決める。

## 送られるものと残る期間 {#what-is-sent}

/feedback と、同じ経路の /bug・/share は、コードを含む会話の履歴の写しを Anthropic に送る（[Data usage](https://code.claude.com/docs/en/data-usage)、[Commands](https://code.claude.com/docs/en/commands)）。送る前に、履歴の範囲を選び、同意の画面で内容を確かめる。この画面で止まれば、何も送られない。

送られたものが残る期間は <!-- fact:begin feedback-retention-years -->5 年（2026-11-05 時点）<!-- fact:end --> である。評価の 👍👎 とバグの報告も、同じ期間で残る。この期間は、会話を消したときの扱いや、学習への利用の設定とは別の項目に書かれている。個人のプランと商用のプランの違い、学習への利用の設定は <!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](where-your-data-goes.md#consumer-vs-commercial)<!-- link:end --> と <!-- link:begin where-your-data-goes#training-setting -->[送ったデータの行方（学習・保持期間） › 学習への利用の設定](where-your-data-goes.md#training-setting)<!-- link:end --> が持つ。

セッションの評価のアンケートは、2 段になっている。

- **評価の記録**：アンケートに答えると、評価だけが記録される。会話の中身は付かない。
- **記録の共有**：評価の後に、記録を見てよいかを聞かれる。ここで Yes を選んだときだけ、記録が送られる。

Yes を選ぶと、ソースコードやファイルの内容がそのままアップロードされる。既知の API キーやトークンの形式は伏せ字になるが、伏せ字にされるのは既知の形式だけである。会話に貼ったパスワードや、形式の決まっていない秘密は、そのまま送られると考える。この記録の共有で残る期間には、/feedback の保持とは別の上限が付く（<!-- fact:begin feedback-transcript-share-retention-months -->最長 6 か月（2026-11-06 時点）<!-- fact:end -->）。送る前に公式の [Data usage](https://code.claude.com/docs/en/data-usage) で確かめる。

=== "アプリ"

    - アプリの 👍👎 の評価とバグの報告は、Claude Code の /feedback と同じ期間で残る。
    - アプリで会話を送る画面の細部と、選べる範囲は、このページでは確かめていない。

=== "Claude Code"

    - `/feedback` で報告を始める。`/bug` と `/share` も同じ経路に入る。
    - 履歴の範囲を選び、同意の画面で送る中身を確かめてから、送る。
    - セッションの評価の後の「記録を見てよいか」は、聞かれたときだけ出る。答えないか No なら、評価だけが残る。

## 送る前に決める {#before-sending}

送る前に決めるのは、会話に何が入っているかと、送る範囲である。送った後に手元から取り消す手順は公式の文書に見当たらないので、送った内容は、保持の期間（<!-- fact:begin feedback-retention-years -->5 年（2026-11-05 時点）<!-- fact:end -->）が過ぎるまで残るものとして扱う。

- **秘密が入っているか**：会話に API キーやパスワードを貼っていたら、伏せ字の対象外の形式で残っているかもしれない。秘密の守り方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](protecting-secrets.md#keep-out)<!-- link:end --> を引く。
- **預かったデータが入っているか**：顧客のデータや、規約の付いたデータが会話やコードに入っているなら、送る前に <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](entrusted-data.md#contracted-surfaces)<!-- link:end --> で、その面に渡してよいかを確かめる。
- **範囲が広すぎないか**：不具合の再現に要る部分だけに範囲を絞る。履歴の全部を送る必要はない。

!!! example "判断例：.env の中身を貼った会話で不具合を報告する"
    - **状況**：デバッグ中に .env の中身を会話へ貼った。その後、Claude Code が途中で止まる不具合に気づき、報告したい。
    - **迷う候補**：その会話の履歴を、そのまま /feedback で送る。または、送らずに、再現の手順を自分の言葉で書いて報告する。
    - **選んだもの**：履歴を送らず、再現の手順を自分で書いて報告する。
    - **理由**：伏せ字になるのは既知の形式だけで、貼った秘密が残るかを送る前に確かめきれない。報告に要るのは、不具合が起きる条件のほうである。秘密を貼っていない新しい会話で再現できるなら、その会話を送る手もある。

## /share は共有のリンクではない {#share-is-bug}

`/share` は、Claude Code では `/bug` の別名で、会話を Anthropic に送るコマンドである（[Commands](https://code.claude.com/docs/en/commands)）。共有のリンクは作らない。名前から、友人や同僚に会話を見せるコマンドだと思って実行しても、会話は Anthropic へ送られる。

「共有」と呼ばれる機能は 2 つあり、送り先が違う。

- **Claude Code の `/share`**：会話を Anthropic に送る。/feedback と同じ保持の期間（<!-- fact:begin feedback-retention-years -->5 年（2026-11-05 時点）<!-- fact:end -->）で残る。他人が開けるリンクは出ない。
- **claude.ai のチャットの共有**：招待や公開リンクで、他人に会話を見せる。何が誰に見え、どれを取り消せるかは <!-- link:begin shared-artifacts-and-files#how-to-share -->[共有リンクと公開アーティファクトの扱い › 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有）](shared-artifacts-and-files.md#how-to-share)<!-- link:end --> と <!-- link:begin shared-artifacts-and-files#revoke -->[共有リンクと公開アーティファクトの扱い › 取り消せるもの・取り消せないもの](shared-artifacts-and-files.md#revoke)<!-- link:end --> が持つ。

会話を人に見せたいときは、後者の機能か、会話の内容を自分で貼る形にする。`/share` を試しに実行して挙動を見る使い方はしない。

## テレメトリと報告の機能を止める {#telemetry}

Claude Code は、/feedback のほかにも、環境変数で止められる通信を持つ（[Data usage](https://code.claude.com/docs/en/data-usage)）。止めるかは、報告に使うかと、通信を絞る必要があるかで決める。

| 環境変数 | 止めるもの |
| --- | --- |
| `DISABLE_TELEMETRY=1` | テレメトリ |
| `DISABLE_ERROR_REPORTING=1` | エラーの報告 |
| `DISABLE_FEEDBACK_COMMAND=1` | /feedback のコマンド |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | テレメトリなど、必須でない通信をまとめて止める |

公式は、テレメトリの metrics にコードも、プロンプトも、ファイルパスも含まれないと説明している。止めるのは、通信の量や種類を絞りたいときである。止めても、手元のセッション記録は変わらない。手元の記録は <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](where-your-data-goes.md#local-transcripts)<!-- link:end --> が持つ。

WebFetch は、取得の前に、ホスト名だけを api.anthropic.com に送って安全リストと照合する。この照合を止める設定は `skipWebFetchPreflight` である。

3 つの変数を置く雛形は次のとおり。`DISABLE_FEEDBACK_COMMAND` を置くと、不具合を /feedback で報告できなくなる。報告に使う人は、この行を外す。

<!-- gen:begin snippet what-feedback-sends/disable-reporting -->
<!-- textlint-disable -->

??? example "雛形：テレメトリ・エラー報告・/feedback を止める環境変数"

    ```json
    {
      "env": {
        "DISABLE_TELEMETRY": "1",
        "DISABLE_ERROR_REPORTING": "1",
        "DISABLE_FEEDBACK_COMMAND": "1"
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet what-feedback-sends/disable-reporting -->

組織で記録を集める側の話、つまり OpenTelemetry や監査ログで何が記録され、何が記録されないかは <!-- link:begin audit-logs-and-telemetry#what-is-recorded -->監査ログと可視化（OpenTelemetry など）<!-- link:end --> が持つ。面ごとの既定の記録の扱いは <!-- link:begin default-safety-settings#defaults-by-surface -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 面ごとの既定（生成の表）](default-safety-settings.md#defaults-by-surface)<!-- link:end --> の表で比べられる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [送ったデータの行方（学習・保持期間）](where-your-data-goes.md)

**関連**

- [秘密情報（.env・API キー）を守る](protecting-secrets.md)
- [共有リンクと公開アーティファクトの扱い](shared-artifacts-and-files.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](entrusted-data.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Data usage](https://code.claude.com/docs/en/data-usage)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)：Anthropic（Privacy Center）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
