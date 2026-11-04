---
id: request-lock-table
title: お願いと鍵の対応表
aliases: [お願いと鍵の早見表, 非決定論的な指示と決定論的な制御の対応表, 指示と強制の対応表]
type: comparison
field: enforce
chapter: 何を縛るか
order: 20
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, 文章, チーム]
summary: 完了の判定・禁止・出力の形式・文体などの用途ごとに、お願いの書き方と鍵の手段を並べて選べる。同じ用途でも、面によって使える鍵が違う。
signs:
  - {type: goal, text: この規則をどの仕組みで強制すればよいか知りたい}
  - {type: goal, text: 出力の形式や文体を毎回そろえたい}
prerequisites: [when-to-lock]
related: [request-vs-lock, permission-rules, hooks-basics, stop-hooks, sandboxing, hook-vs-skill, claude-md-vs-rules-skills-styles, structured-outputs-basics, textlint-hook, keep-replies-in-japanese, protect-tests, move-judgment-into-scripts]
tracks: [hooks, permissions, sandbox, claude-md, output-styles, structured-outputs]
outdated_advice: [important-caps, prefill-for-json, styles-for-tone]
sources: [cc-docs-features-overview, cc-docs-best-practices, cc-docs-hooks-guide, cc-docs-permissions, cc-docs-sandboxing, cc-docs-memory, cc-docs-output-styles, api-docs-structured-outputs]
volatility: 中
sections:
  - {title: 用途ごとの対応表, anchor: table}
  - {title: 鍵にできるのはどこか（ターンの終わりと道具の前後）, anchor: where-locks-act}
  - {title: 面ごとの鍵の手段, anchor: by-surface}
  - {title: 選び方（判断例）, anchor: choose}
  - {title: 組み合わせ方と確かめ方, anchor: combine}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：機械で判定できて例外のない規則は鍵（deny ルール・フック・structured outputs）に、判断が要る規則はお願い（CLAUDE.md・出力スタイル）に置くと選べる。
    - **いつ引くか**：この規則をどの仕組みで強制すればよいか知りたいとき。出力の形式や文体を毎回そろえたいとき。
    - **前提**：<!-- link:begin when-to-lock -->[お願いを鍵に移す判断](when-to-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：お願いと鍵の早見表・非決定論的な指示と決定論的な制御の対応表・指示と強制の対応表
<!-- textlint-enable -->

お願いと鍵の対応表は、完了の判定・禁止・出力の形式・文体といった用途ごとに、お願いの書き方と鍵の手段を並べて選ぶための表である。お願いと鍵の違いそのものは <!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end --> にある。この表は、鍵に移すと決めた後に手段を選ぶときに引く。

## 用途ごとの対応表 {#table}

最初に、手段ごとの属性を比べる。お願いに当たる手段と鍵に当たる手段が、強制力の列で分かれる。

<!-- gen:begin compare 面 強制力 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 面 | 強制力 | 圧縮で残るか |
| --- | --- | --- | --- |
| [フック（hooks）](hooks-basics.md) | Claude Code | 鍵 | 残る |
| [権限（permissions）](permission-rules.md) | Claude Code | 鍵 | 残る |
| [サンドボックス](sandboxing.md) | Claude Code | 鍵 | 残る |
| [CLAUDE.md](../extend/what-to-put-in-claude-md.md) | Claude Code | お願い | 残る |
| 出力スタイル（output styles）（準備中） | Claude Code | お願い | 残る |
| structured outputs（準備中） | API | 鍵 | 未確認 |

<!-- textlint-enable -->
<!-- gen:end compare 面 強制力 圧縮で残るか -->

次に、用途ごとに、お願いの書き方と鍵の手段を並べる。鍵の列は、強制できる手段だけを書く。

| 用途 | お願い（書き方） | 鍵（手段） |
| --- | --- | --- |
| 完了の判定（テストが通るまで終えない） | 依頼に完了の条件を成果で書く。テストの実行コマンドを CLAUDE.md に置く | Stop フック。確かめる処理が通るまでターンを終えさせない |
| 禁止（`.env` を編集しない・push しない） | CLAUDE.md に、禁止の理由と、迷ったときに相談する基準を書く | deny ルール。コマンドの中身まで見るなら PreToolUse フック |
| 読み書きと通信の境界（秘密の置き場を読ませない） | CLAUDE.md に、触れない場所を書く | Claude のファイルの道具には deny ルール。Bash から起きるプロセスにはサンドボックス |
| 出力の形式（JSON・決まった見出し） | 形を指示に書き、例を添える | structured outputs（API）。API 以外の面では、鍵はなく、指示と検査の組み合わせになる |
| 文体・表記（機械で見つけられる範囲） | CLAUDE.md・出力スタイルに書く | PostToolUse フックで textlint などを走らせ、残った違反を Claude に返す |
| 返答の言語 | 言語の設定・CLAUDE.md・出力スタイル | Stop フックで最後の返事を確かめて続けさせる |
| 調子・口調 | いつも同じなら指示、場面で切り替えるならスキル | なし（判断を含み、機械で判定できない） |

読み方は 3 つある。

- 鍵の列が「なし」の用途は、お願いだけで運ぶ。鍵にしない規則の見分け方は <!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](when-to-lock.md#what-not-to-lock)<!-- link:end --> にある。
- 禁止と境界の行は、手段が 1 つでは足りない。deny ルールは Bash から起きた子プロセスに効かず、サンドボックスは Claude のファイルの道具に効かない。詳しくは <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](permission-rules.md#child-processes)<!-- link:end --> と <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](sandboxing.md#scope)<!-- link:end --> を読む。
- 完了の判定の行は、Stop フックが続けて止められる回数に上限がある。止め続けるループを避ける書き方は <!-- link:begin stop-hooks#avoid-loops -->Stop フックで「終わらせない」 › 止め続けるループを避ける（準備中）<!-- link:end --> にある。

## 鍵にできるのはどこか（ターンの終わりと道具の前後） {#where-locks-act}

Claude Code で強制できるのは、ターンの終わりと、道具の呼び出しの前後だけである。Stop フックで最後の返事を、PreToolUse フックで次の道具の呼び出しを、PostToolUse フックで道具の結果を扱える。これ以外の場面に、鍵はない。

次の 4 つは、鍵に見えて鍵にならない。

- **道具の合間の一言**：画面へ出る前に止める仕組みはない。MessageDisplay のフックは表示を差し替えるだけで、止められない。そのため、文体と言語の行では鍵に数えない。
- **prompt 型と agent 型のフック**：別のモデルが判断するので、毎回同じ結果になるとは限らない。鍵にするのは、スクリプトが判定する command 型などのフックである。
- **Bash で書き換えたファイル**：`Edit|Write` に絞った PostToolUse フックは、Bash でファイルが変わったときに動かない。どこから書き換えても拾うなら、ファイルの変更を見る別のきっかけ（FileChanged）を使う。
- **サンドボックスの外の道具**：Claude のファイルの道具・MCP サーバー・フックは、サンドボックスの外で動く。

!!! example "判断例：返答を毎回日本語にしたい"
    - **状況**：Claude Code で作業していて、英語のツール出力を読んだ後に、返答が英語へ戻ることがある。
    - **迷う候補**：言語の設定と CLAUDE.md に書くだけで足りるとする。Stop フックで最後の返事を確かめる。
    - **選んだもの**：お願いの層（言語の設定・CLAUDE.md・出力スタイル）を土台にして、最後の返事だけ Stop フックで確かめる。
    - **理由**：強制できるのはターンの終わりだけで、道具の合間の一言は画面に出るのを止められない。お願いの層は届く範囲もそれぞれ違う。この限界の中で減らす組み合わせは <!-- link:begin keep-replies-in-japanese#stop-hook -->[日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)<!-- link:end --> にある。

## 面ごとの鍵の手段 {#by-surface}

同じ用途でも、面によって使える鍵が違う。

=== "アプリ"

    フック・権限ルール・サンドボックスは Claude Code の機能で、アプリには鍵の手段がない。返答の言語や文体を機械的に確かめる仕組みも、公式の文書に見当たらない。手段はどれも指示である。

    いつも同じ調子や形式にするなら、全会話に効く指示に書く。場面ごとに切り替えるなら、スキルにする。例外を許さない規則をアプリだけで強制する手段はない。強制が要るなら、規則を Claude Code か API の側へ移す。

=== "Claude Code"

    表の手段のうち、API の機能である structured outputs 以外の 5 つが使える。止める規則は deny ルールとフック、境界はサンドボックス、常に効かせる指示は CLAUDE.md と出力スタイルに置く。

    鍵の手段は、会話の外で動くものと、設定にあるものである。会話で言った禁止は圧縮で消えうるが、設定のルールは圧縮の影響を受けない。理由は <!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](when-to-lock.md#spoken-rules-fade)<!-- link:end --> にある。

    クラウドのセッションには、ユーザーの設定・CLAUDE.md・フック・プラグインが届かない。届けたい規則は、リポジトリの CLAUDE.md と `.claude/settings.json` に入れる。ただし、そうするとチーム全員に効く。

=== "API"

    使える鍵は structured outputs で、応答を与えた JSON スキーマに合う形にする。道具の名前と入力をスキーマに合わせる strict tool use も同じ仕組みである。形が保証されない場合と、形が正しくても中身は別に確かめる理由は <!-- link:begin structured-outputs-basics#not-guaranteed -->structured outputs（形式を保証する） › 形が保証されない場合（準備中）<!-- link:end --> にある。

    返答の言語や文体には鍵がない。公式の多言語の文書は、本番では言語を明示し、最も確実な場所はシステムプロンプトだとする。文体は、呼び出し側のコードで検査して、再試行するかを決める。

## 選び方（判断例） {#choose}

選ぶ順は、規則を機械で判定できるかを先に見る。判定できて例外がなければ鍵、判定に判断が入るならお願いである。

!!! example "判断例：「main に push しない」と頼んだ"
    - **状況**：長い作業の途中で、会話で「main に push しないで」と頼んだ。作業の途中で圧縮が入っても守らせたい。
    - **迷う候補**：CLAUDE.md に禁止を書く。会話で何度も言い直す。deny ルールにする。
    - **選んだもの**：push を含むコマンドへの deny ルールを置く。CLAUDE.md には、禁止の理由と、どうしても必要なときに相談する基準だけを書く。
    - **理由**：例外を許さず、コマンドの文字で判定できる。会話の禁止は圧縮で消えうるが、設定のルールは残る。コマンドの別の書き方まで拾い、理由を返したいなら、同じ判定の PreToolUse フックを足す。

!!! example "判断例：受け取る JSON をそのままプログラムに渡す"
    - **状況**：Claude の出力を、人が読まずに、後続のプログラムへ渡す。
    - **迷う候補**：形を指示に書いて、検査して再試行する。structured outputs で形を指定する。
    - **選んだもの**：API を自分のコードから呼べるなら structured outputs にする。形が崩れる場合に備えて、検査も残す。
    - **理由**：形は指示ではなく、デコードの制約で守られる。ただし、保証されない場合があり、形が正しくても中身の正しさは別に確かめる。Claude Code の `-p` で形を指定する方法は <!-- link:begin structured-outputs-basics#claude-code -->structured outputs（形式を保証する） › Claude Code の -p で形を指定する（準備中）<!-- link:end --> にある。

## 組み合わせ方と確かめ方 {#combine}

実際の規則は、1 つの手段で済むことが少ない。組み合わせ方の基本は 3 つある。

- **二層で書く**：例外を許さない部分は鍵で止め、CLAUDE.md には理由と相談の基準だけを書く。鍵は Claude の振る舞いを変えず、止めるだけなので、理由を読ませる層が別に要る。書き分けは <!-- link:begin request-vs-lock#two-layers -->[お願いと鍵（決定論的か、非決定論的か） › 二層で書く](../basics/request-vs-lock.md#two-layers)<!-- link:end --> にある。
- **止めるのは壊れにくい手段に任せる**：依存のない deny ルールに強制を任せ、フックには理由の文と記録を受け持たせる（推論・実践例なし）。フックだけが強制を担う規則では、フックが動かない場合に何が起きるかを先に確かめる。確かめ方は <!-- link:begin hooks-basics#not-running -->[フックの考え方とイベント › 動いていないように見えるとき](hooks-basics.md#not-running)<!-- link:end --> にある。
- **判断を含む規則は鍵にしない**：判断を鍵に押し込むと止めすぎる。判断は <!-- link:begin hook-vs-skill -->[フックとスキルの違い](../extend/hook-vs-skill.md)<!-- link:end --> や <!-- link:begin claude-md-vs-rules-skills-styles -->[CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)<!-- link:end --> で置き場所を選び、毎回 Claude に判断させている作業は <!-- link:begin move-judgment-into-scripts -->判断を決定論的なスクリプトに移す（準備中）<!-- link:end --> でスクリプトに移す。

鍵を置いたら、効く範囲を確かめる。

1. 新しいセッションで、鍵が止めるはずの依頼をわざと出す。止まる、または理由が返ることを見る。
2. 子プロセスや別の書き方など、鍵が当たらない経路を 1 つ試す。当たらないなら、サンドボックスやフックで別に塞ぐ。
3. 圧縮の後でも同じ依頼で止まることを見る。

テストや採点を書き換えて通す行為は、ファイルの鍵とレビューを重ねて防ぐ。層の分け方は <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> にある。

## 古くなった助言 {#outdated}

お願いと鍵の選び方に関わる古い助言が 3 つある。今どうするかだけを書く。

- 強調して守らせる助言：<!-- link:begin outdated-advice-ledger#important-caps -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#important-caps)<!-- link:end -->。強調せず、ふつうの言葉で書く。それでも守られないなら、規則を鍵に移す。
- prefill で JSON の形を強制する助言：<!-- link:begin outdated-advice-ledger#prefill-for-json -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#prefill-for-json)<!-- link:end -->。形の保証は structured outputs で行う。
- アプリのスタイルで調子を切り替える助言：<!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->。調子と形式をいつもそろえるなら指示を使い、場面で切り替えるならスキルを使う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いを鍵に移す判断](when-to-lock.md)

**関連**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- [権限ルール（allow・ask・deny）](permission-rules.md)
- [フックの考え方とイベント](hooks-basics.md)
- Stop フックで「終わらせない」（準備中）
- [サンドボックスで封じ込める](sandboxing.md)
- [フックとスキルの違い](../extend/hook-vs-skill.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- structured outputs（形式を保証する）（準備中）
- [textlint をフックで回す](../japanese/textlint-hook.md)
- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- 判断を決定論的なスクリプトに移す（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
