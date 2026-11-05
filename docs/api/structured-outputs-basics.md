---
id: structured-outputs-basics
title: structured outputs（形式を保証する）
aliases: [構造化出力, JSON outputs, strict tool use, --json-schema]
type: feature
field: api
chapter: API の主な機能
order: 40
level: 仕組みにする
priority: 推奨
surfaces: [api, claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない]
scenes: [開発, データ分析]
summary: 出力やツールの呼び出しを、指定したスキーマどおりの形で受け取れる。それでも形が崩れる場合と、形が正しくても中身は別に確かめる理由が分かる。
signs:
  - {type: symptom, text: JSON で返すよう頼んでも形が崩れる}
  - {type: goal, text: 出力を必ず決まった形で受け取りたい}
prerequisites: [request-vs-lock]
related: [output-shape, looks-are-not-quality, tool-use-loop, citations-basics, headless-basics]
tracks: [structured-outputs]
outdated_advice: [prefill-for-json]
sources: [api-docs-structured-outputs, api-release-notes, api-docs-prompting-best-practices, cc-docs-headless]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: JSON outputs と strict tool use, anchor: two-modes}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 形が保証されない場合, anchor: not-guaranteed}
  - {title: prefill からの移行, anchor: from-prefill}
  - {title: Claude Code の -p で形を指定する, anchor: claude-code}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude の応答やツールの呼び出しを、指定した JSON スキーマどおりの形で受け取れる。
    - **いつ引くか**：JSON で返すよう頼んでも形が崩れるとき。出力を必ず決まった形で受け取りたいとき。
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。形の崩れは止められるが、中身の正しさは止められない。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：構造化出力・JSON outputs・strict tool use・--json-schema
<!-- textlint-enable -->

structured outputs は、渡した JSON スキーマに合う形へ Claude の出力を制約する API の機能である。応答そのものの形を決める JSON outputs と、ツールの呼び出しの形を決める strict tool use の 2 つがある。

## 使いどころ {#when}

structured outputs が防ぐ原因は、形を「縛っていない」ことである。「JSON で返して」と書くのは、Claude が読んで判断するお願いにとどまる。前置きの一文、閉じ忘れの括弧、キー名の揺れが混じると、受け取る側のパースが落ちる。お願いと鍵の分け方は <!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end --> にある。スキーマでの指定は、生成の段階で形を縛る鍵の側に当たる。

向く場面は、Claude の出力を別のプログラムに渡す仕組みである。分類のラベル、文書からの項目の抽出、道具に渡す引数がそうだ。人が読む文章の書式や長さを整えたいだけなら、スキーマは要らない。その場合は <!-- link:begin output-shape -->[出力の形と分量を指定する](../prompting/output-shape.md)<!-- link:end --> の書き方で足りる。機械が読む出力で形を必ず守らせたいときが、この機能の出番である。

## JSON outputs と strict tool use {#two-modes}

structured outputs は、縛る対象の違う 2 つの方式からなる。

| 方式 | 指定する場所 | 縛られるもの |
| --- | --- | --- |
| JSON outputs | `output_config.format` に `json_schema` を渡す | 最終の応答の text ブロックの形 |
| strict tool use | ツールの定義に `strict: true` を付ける | ツールの名前と入力の形 |

- JSON outputs は、Claude が「何を答えるか」の形を決める。応答は、スキーマに合う JSON として text ブロックに入る。
- strict tool use は、Claude が「どう道具を呼ぶか」の形を決める。入力の型やキー名が、定義のスキーマからずれない。
- 2 つは同じ依頼で併用できる。併用すると、応答が `tool_use` ブロックの場合と JSON の text ブロックの場合がある。`stop_reason` とブロックの種類を見て分岐する。

どちらも、制約つきのデコード（constrained decoding）で、生成する語をスキーマに合う範囲へ絞る仕組みである。後から検査して直すのではなく、外れた形をそもそも出させない。道具を呼ばせるループの全体は <!-- link:begin tool-use-loop -->[tool use のループ](tool-use-loop.md)<!-- link:end --> にある。

## 最小の使い方 {#minimal}

面によって、形を指定する手段が違う。

=== "Claude Code"

    `claude -p` に `--json-schema` でスキーマを渡す。詳しくは「Claude Code の -p で形を指定する」の節にある。

=== "API"

    JSON outputs は `output_config.format` にスキーマを入れる。strict tool use はツールの定義に `strict: true` を付ける。どちらも、スキーマの最上位の `additionalProperties` は `false` にする。

次の雛形は、API に送る依頼の本文である。モデルの id は、自分の環境で使えるものに替える。

<!-- gen:begin snippet structured-outputs-basics/json-output -->
<!-- textlint-disable -->

??? example "雛形：JSON outputs の依頼の本文（応答を分類のスキーマに合わせる）"

    ```json
    {
      "model": "<モデルの id>",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": "次の問い合わせを分類してください。\n\n「先月の請求書が届いていません」"
        }
      ],
      "output_config": {
        "format": {
          "type": "json_schema",
          "schema": {
            "type": "object",
            "properties": {
              "category": {
                "type": "string",
                "enum": ["billing", "bug", "other"]
              },
              "summary": { "type": "string" }
            },
            "required": ["category", "summary"],
            "additionalProperties": false
          }
        }
      }
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet structured-outputs-basics/json-output -->

<!-- gen:begin snippet structured-outputs-basics/strict-tool -->
<!-- textlint-disable -->

??? example "雛形：strict tool use の依頼の本文（道具の入力をスキーマに合わせる）"

    ```json
    {
      "model": "<モデルの id>",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": "東京の明日の天気を調べて。単位は摂氏で。"
        }
      ],
      "tools": [
        {
          "name": "get_weather",
          "description": "指定した都市の天気を返す",
          "strict": true,
          "input_schema": {
            "type": "object",
            "properties": {
              "city": { "type": "string" },
              "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
            },
            "required": ["city", "unit"],
            "additionalProperties": false
          }
        }
      ]
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet structured-outputs-basics/strict-tool -->

Python と TypeScript などの SDK には、クラスや型からスキーマを作り、応答を読み込んだ形で返す補助がある。使い方は公式の Structured outputs の文書にある。

## 形が保証されない場合 {#not-guaranteed}

structured outputs でも、形が崩れる場合はある。また、形が合っていても、中身の正しさは別の話である。

- **拒否で止まったとき**：`stop_reason` が `refusal` の応答は、スキーマに合わないことがある。応答は成功として返り、料金もかかる。
- **途中で切れたとき**：`stop_reason` が `max_tokens` の応答は、JSON が途中で終わる。`max_tokens` を上げて再試行する。
- **enum の大文字小文字**：enum の値が、大文字小文字だけ違う形で返ることがある。比較は大文字小文字を区別しない形にする。
- **未対応のスキーマ**：再帰するスキーマや数値の範囲（最小・最大）などは使えず、400 エラーになる。スキーマの複雑さにも上限がある。細部は公式の文書で確かめる。
- **併用できない機能**：citations とは併用できず、400 エラーになる。<!-- link:begin citations-basics#limits -->citations（根拠の箇所を返させる） › 一緒に使えない機能（準備中）<!-- link:end --> にまとまっている。

形の保証は、中身の正しさの保証ではない。スキーマは「金額は数値」とは言えても、「その金額が請求書と合う」とは言えない。数値の範囲を縛れないので、範囲の検査はコードの側で行う。見た目が整っていることを品質の証拠にしない理由は <!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)<!-- link:end --> にある。

!!! example "判断例：請求書から金額を抜き出す"
    - **状況**：請求書の文章から、合計金額を JSON で抜き出して会計の仕組みに渡す。
    - **迷う候補**：スキーマで形を保証したので、そのまま会計に渡す。または、形を保証したうえで、明細の合計との一致を別に検査する。
    - **選んだもの**：形は structured outputs に任せ、明細の合計との一致はコードで検査する。
    - **理由**：スキーマが守るのは形だけで、値が正しいかは見ないからだ。形が崩れない分、検査のコードは単純になる。

## prefill からの移行 {#from-prefill}

prefill は、会話の最後に assistant の役のメッセージを置き、応答の書き出しを指定して続きを書かせる手である。以前は、JSON の形を守らせるために使われた。

新しいモデルでは、最後のターンの prefill が 400 エラーになる。どのモデルからかは、台帳の行に日付つきである。モデルを替えて 400 が出たら、まず messages の最後が assistant の役になっていないかを疑う。

移行先は、目的によって分かれる。

- **形を守らせたい**：structured outputs を使う。
- **前置きを省きたい**：省くよう直接指示する。
- **続きを書かせたい、文脈を補いたい**：user のターンに入れる。
- **分類したい**：ラベルを enum にしたスキーマか道具を使う。

structured outputs が使えない場面では、形を指示に書き、検査して再試行する手が残る。

## Claude Code の -p で形を指定する {#claude-code}

Claude Code を非対話で動かす `claude -p` には、`--json-schema` でスキーマを渡す方法がある。スクリプトや CI が、結果を決まった形で受け取るときに使う。

<!-- gen:begin snippet structured-outputs-basics/claude-p-json-schema -->
<!-- textlint-disable -->

??? example "雛形：claude -p で出力の形を指定する"

    ```bash
    claude -p "このリポジトリの README を読み、題名と対象読者を答えて" \
      --output-format json \
      --json-schema '{
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "audience": { "type": "string" }
        },
        "required": ["title", "audience"],
        "additionalProperties": false
      }'
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet structured-outputs-basics/claude-p-json-schema -->

形に合う結果は、出力の JSON の `structured_output` に入る。出力の形式や終了コードの扱いは <!-- link:begin headless-basics#output-and-exit-codes -->[非対話モード（claude -p）の基本 › 出力の形式と終了コード](../delegate/headless-basics.md#output-and-exit-codes)<!-- link:end --> にある。無人で動かすときの許可と止まる上限は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> と <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end --> で先に決める。形が合っても、中身の正しさは、形の保証とは別に確かめる（「形が保証されない場合」の節に判断例がある）。

## 比べる相手 {#compare}

| 欲しいもの | 使うもの |
| --- | --- |
| 機械が読む出力の形を必ず守らせる | structured outputs |
| 書式や長さをそろえる | <!-- link:begin output-shape#guaranteed -->[出力の形と分量を指定する › 必ず守らせたい形式は仕組みで](../prompting/output-shape.md#guaranteed)<!-- link:end --> |
| 特定の道具を必ず呼ばせる | <!-- link:begin tool-use-loop#forcing -->[tool use のループ › 呼ばせ方を縛る（tool\_choice・strict）](tool-use-loop.md#forcing)<!-- link:end --> |
| 根拠の箇所を返させる | <!-- link:begin citations-basics -->citations（根拠の箇所を返させる）（準備中）<!-- link:end --> |

道具の呼び出しを強制する設定は、モデルによって使えないことがある。その場合、公式は strict tool use や JSON outputs を勧める。citations とは併用できないので、どちらが要るかを先に決める。

## 古くなった助言 {#outdated}

「prefill で JSON の形を強制する」は古い助言である。台帳の行は <!-- link:begin outdated-advice-ledger#prefill-for-json -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#prefill-for-json)<!-- link:end --> にある。今は、structured outputs で形を保証する。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)：Anthropic・英語・確認日 2026-11-04
- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [出力の形と分量を指定する](../prompting/output-shape.md)
- [見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)
- [tool use のループ](tool-use-loop.md)
- citations（根拠の箇所を返させる）（準備中）
- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
