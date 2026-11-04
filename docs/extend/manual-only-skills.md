---
id: manual-only-skills
title: 副作用のあるスキルを勝手に動かさない
aliases: [disable-model-invocation, 手動専用のスキル, user-invocable]
type: feature
field: extend
chapter: スキル
order: 130
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: デプロイのような副作用のある手順を、Claude が自分の判断で動かさないようにできる。人だけが呼べる設定と、それでも鍵が要る場面を見分ける。
signs:
  - {type: goal, text: デプロイ用の手順を、勝手に動かされたくない}
  - {type: symptom, text: デプロイのような手順を、頼んでいないのに始められた}
prerequisites: [writing-skills]
related: [skill-descriptions, permission-rules, destructive-commands, hook-vs-skill, when-to-lock, does-more-than-asked]
tracks: [skills]
sources: [cc-docs-skills, cc-docs-features-overview, cc-docs-permissions, cc-docs-best-practices]
volatility: 中
sections:
  - {title: 勝手に動くのは、説明文が合ったから, anchor: use}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 人だけが呼べる設定と、Claude だけが呼べる設定, anchor: variants}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 鍵が要る場面の判断, anchor: need-lock}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`disable-model-invocation: true` を付けると、デプロイのような手順のスキルを、Claude が自分の判断で動かさず、人が呼んだときだけ動かせる。
    - **いつ引くか**：デプロイ用の手順を、勝手に動かされたくないとき。デプロイのような手順を、頼んでいないのに始められたとき。
    - **強制力**：スキル全般の値は「<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->」である。ただしこの設定は、Claude が自分でスキルを呼ぶ道を Claude Code がふさぐ。止まるのはその道だけで、同じコマンドを Claude が直接打つ道と、人が呼んだ後の手順の中身は止まらない。
    - **前提**：<!-- link:begin writing-skills -->[スキルの作り方](writing-skills.md)<!-- link:end -->

<!-- textlint-disable -->
別名：disable-model-invocation・手動専用のスキル・user-invocable
<!-- textlint-enable -->

副作用のあるスキルを勝手に動かさないとは、デプロイや送信のような手順のスキルに `disable-model-invocation: true` を付け、Claude が自分の判断でそのスキルを呼ぶ道をふさぐことである。呼べるのは、人が `/deploy` のように打ったときだけになる。ただし、止まるのはスキルの呼び出しだけで、手順に含まれるコマンドそのものを縛る設定ではない。

## 勝手に動くのは、説明文が合ったから {#use}

スキルが頼んでいないのに動くのは、Claude が説明文を読み、今の依頼に合うと判断してスキルを呼ぶからである。既定のスキルは、人と Claude のどちらでも呼べる。名前と説明がセッションの最初から Claude に見えており、依頼が説明文に合えば、Claude が自分で本体を読み込む。この仕組みは、手順書を何度も貼らなくて済むようにするためのものだ。

しかし、デプロイや送信のように、動かすと外の世界が変わる手順では、同じ仕組みが危うくなる。「リリースの準備をして」と頼んだだけで、説明文に合った `deploy` のスキルが読み込まれ、本番への手順が始まるかもしれない。防ぐ原因は、起動の判断を Claude に任せたまま、縛っていないことである。

使いどころは、次のような手順のスキルである。

- 動かすと外に出るもの。デプロイ、公開、メッセージの送信、課金のある操作
- 動かす時機を、人が決めたいもの。リリースの直前の確認や、コミットのような区切りの手順
- 説明文を工夫しても、誤った起動が減らないもの。起動の合図の言葉が、普段の依頼とも重なる場合

説明文の側で起動を合わせたいだけなら、この設定ではなく「<!-- link:begin skill-descriptions#overlap -->[スキルの description の書き方 › ほかのスキルと重ならないようにする](skill-descriptions.md#overlap)<!-- link:end -->」を使う。この設定は、合わせるのではなく、呼び出しそのものを人に限る。

## 最小の使い方 {#minimal}

スキルの先頭のフロントマターに、`disable-model-invocation: true` を 1 行足す。スキルの置き場所と作り方は「<!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](writing-skills.md#minimal)<!-- link:end -->」にある。

```markdown
---
name: deploy
description: 本番環境へのデプロイ手順。人が /deploy で呼んだときだけ使う
disable-model-invocation: true
---
```

これだけで、Claude Code は次のように動く。

- 人が `/deploy` と打つと、スキルの本体が会話に入り、手順が動く。
- Claude が自分の判断で `deploy` を呼ぼうとしても、Claude Code が呼び出しを止める。止められた Claude は、人に `/deploy` を打つよう案内することが多い。ただし、この挙動は実機では未確認である。
- 説明文は Claude の文脈に入らない。呼ぶまで、このスキルは何も場所を取らない。

この設定は Claude Code のスキルの設定である。claude.ai へアップロードするスキルでは、このキーが取り込みを止めることがある。注意点は「<!-- link:begin writing-skills#limits -->[スキルの作り方 › 効かない場面と落とし穴](writing-skills.md#limits)<!-- link:end -->」にある。

確かめ方は 2 つある。新しいセッションで `/deploy` を打って、手順が動くことを見る。次に、`/deploy` を打たずに「デプロイして」と頼み、Claude がスキルを読み込まずに案内で返すことを見る。後者は、依頼の言い方や説明文の合い方で変わりうるので、観察として扱い、1 回の結果で安心しない。

## 人だけが呼べる設定と、Claude だけが呼べる設定 {#variants}

呼べる側を変える設定は、名前が似ていて向きが逆なので、取り違えやすい。スキルの呼び出しの向きは、フロントマターの 2 つのキーで決まる。

| 設定 | 人が呼べるか | Claude が自分で呼べるか | 説明文が文脈に入るか |
| --- | --- | --- | --- |
| 既定 | 呼べる | 呼べる | 入る |
| `disable-model-invocation: true` | 呼べる | 呼べない | 入らない |
| `user-invocable: false` | 呼べない | 呼べる | 入る |

副作用のある手順に使うのは、真ん中の行である。`user-invocable: false` は、人の `/` のメニューから隠して Claude だけが使う背景知識のスキルに使うもので、勝手な起動を止める効果はない。

他人が作ったスキルを編集せずに、見え方だけを変えたいときは、設定の `skillOverrides` が使える。値の `user-invocable-only` は、Claude からは隠れ、人の `/` のメニューには残る。意味はフロントマターの `disable-model-invocation: true` に近く、`user-invocable: false` とは逆である。名前から逆の意味に読みやすいので、使う前に公式の文書で値の意味を確かめる。

## 雛形 {#templates}

デプロイのスキルを、人が呼んだときだけ動くようにした例である。手順の中に、人の承認を待つ段を入れてある。

<!-- gen:begin snippet manual-only-skills/deploy-skill -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/deploy/SKILL.md（人が呼んだときだけ動くデプロイのスキル）"

    ```markdown
    ---
    name: deploy
    description: 本番環境へのデプロイ手順。人が /deploy で呼んだときだけ使う
    disable-model-invocation: true
    argument-hint: [staging|production]
    ---

    # デプロイの手順

    対象の環境は $ARGUMENTS である。

    1. `git status` で作業ツリーが空であることを確かめる
    2. `npm test` を流し、失敗したら止めて人に報告する
    3. これから流すコマンドと対象の環境を人に見せ、承認を待つ
    4. 人が承認したら `./scripts/deploy.sh $ARGUMENTS` を流す
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet manual-only-skills/deploy-skill -->

手順の中の承認の段は、お願いである。Claude がそれを飛ばさないと保証する鍵ではない。最後のコマンドの前に必ず確認を挟みたいときは、次のように、コマンドの側に ask ルールを置く。ルールの評価の仕組みは「<!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->」にある。

<!-- gen:begin snippet manual-only-skills/deploy-ask -->
<!-- textlint-disable -->

??? example "雛形：.claude/settings.json（デプロイのスクリプトを流す前に確認を求める ask ルール）"

    ```json
    {
      "permissions": {
        "ask": ["Bash(./scripts/deploy.sh *)"]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet manual-only-skills/deploy-ask -->

## 効かない場面と落とし穴 {#limits}

この設定が止めるのは、Claude がスキルを自分で呼ぶ道だけである。次の場面は止めない。

- **同じコマンドを直接打つ道**：スキルを呼べなくても、Claude が `./scripts/deploy.sh production` のようなコマンドを、Bash から直接流すことはできる。スキルの呼び出しが止められたとき、Claude が同じことをやり直さないかは、Claude の振る舞いしだいで、鍵ではない。コマンドそのものを止めるには、権限ルールかフックが要る。権限ルールの書き方は「<!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end -->」にある。
- **人が呼んだ後の手順の中身**：人が `/deploy` を呼んだ後は、手順の各段をセッションの権限で動かす。手順に書いた「承認を待つ」「失敗したら止める」は、お願いである。守らせたい段は、コマンドの側の ask ルールかフックで縛る。
- **Claude はスキルの存在を知らない**：この設定を付けたスキルは、説明文が Claude の文脈に入らない。「本番に出したい」と頼んでも、Claude はこのスキルを見つけられない。人が名前を覚えて呼ぶ運用になる。
- **ほかの呼び出しの道も止まる**：公式の文書によると、この設定は 2 つの道も止める。1 つはサブエージェントへの事前の読み込み、もう 1 つは定期実行のタスクによるスキルの起動である。デプロイの手順をサブエージェントに持たせたいときは、別の方法を考える。
- **誤解されやすい取り違え**：`user-invocable: false` を付けても、Claude の勝手な起動は止まらない。向きが逆になる。付けたキーが意図どおりかは、上の表で見直す。

消されたくないものや、取り返しのつかない操作を守る考え方は、「<!-- link:begin destructive-commands#guard -->[消されたくないもの（破壊的コマンド） › 確認を求めさせる頼み方と、鍵](../safety/destructive-commands.md#guard)<!-- link:end -->」にある。スキルの設定は、その手前の、起動の入口を絞る一手にすぎない。

## 鍵が要る場面の判断 {#need-lock}

`disable-model-invocation: true` は、お願いと鍵の中間にある。Claude Code がスキルの呼び出しを止めるので、説明文の工夫よりは強い。しかし、コマンドそのものを止める鍵ではない。どこまでをこの設定に任せ、どこから鍵に移すかは、動かす手順の取り返しのつかなさで決める。移す合図の見分け方は「<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->」にある。

!!! example "判断例：ステージングへの公開の手順"
    - **状況**：ステージングに公開する手順をスキルにした。失敗しても、環境を作り直せば戻る。
    - **迷う候補**：説明文に「人が頼んだときだけ使う」と書くだけにする。`disable-model-invocation: true` も付ける。
    - **選んだもの**：`disable-model-invocation: true` を付ける。
    - **理由**：説明文の一文はお願いなので、依頼の言い方しだいで破られる。1 行足せば、起動の入口は確実に人だけになる。戻せる環境なので、コマンド側の鍵までは置かない。

!!! example "判断例：本番へのデプロイの手順"
    - **状況**：本番へのデプロイをスキルにした。実行すると利用者に影響が出て、巻き戻しも簡単ではない。
    - **迷う候補**：スキルの設定だけにする。スキルの設定に加えて、コマンドを流す前の確認も権限ルールで強制する。
    - **選んだもの**：両方を置く。スキルには `disable-model-invocation: true` を付け、デプロイのコマンドには ask ルールを置く。
    - **理由**：スキルの設定は、スキルを呼ぶ道しか止めない。Claude が同じコマンドを直接流す道は残る。本番に触れる操作は、権限ルールとフックでも縛る。

頼んでいないことまでやられる症状が、デプロイ以外にも出ているなら、原因を安く切り分ける順は「<!-- link:begin does-more-than-asked#diagnosis -->[頼んでいないことまでやる（過剰設計） › 原因を安く確かめる順](../symptoms/does-more-than-asked.md#diagnosis)<!-- link:end -->」にある。このページが直接の答えになるのは、デプロイのような手順のスキルを勝手に呼ばれる場面に限る。

## 比べる相手 {#compare}

- **フック**：決まったときに必ず動く鍵である。スキルは Claude が判断して使うお願いで、フックは外から止める。手順を必ず走らせたい、または特定の操作を必ず止めたいなら、フックを選ぶ。選び方は「<!-- link:begin hook-vs-skill#how-to-choose -->[フックとスキルの違い › フックとスキルの選び方](hook-vs-skill.md#how-to-choose)<!-- link:end -->」にある。
- **権限ルール**：許可・確認・拒否で、Claude が使える道具とファイルを決める。コマンドそのものを止めたいなら、こちらを使う。この設定と組み合わせる。
- **説明文の書き直し**：起動の合図を合わせる手段である。呼び出しの道は残る。方法は「<!-- link:begin skill-descriptions#front-load -->[スキルの description の書き方 › いつ使うかを先頭に具体的に書く](skill-descriptions.md#front-load)<!-- link:end -->」にある。
- **お願いを鍵に移す判断**：同じ注意を繰り返したときに、どの規則を鍵に移すかを決める。全体の考え方は「<!-- link:begin when-to-lock -->[お願いを鍵に移す判断](../enforce/when-to-lock.md)<!-- link:end -->」にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [スキルの作り方](writing-skills.md)

**関連**

- [スキルの description の書き方](skill-descriptions.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [フックとスキルの違い](hook-vs-skill.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
