---
id: path-scoped-rules
title: .claude/rules と paths で必要なときだけ読ませる
nav_title: .claude/rules と paths
aliases: [rules, パス別のルール, paths のフロントマター, ディレクトリごとの規約]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: 特定のフォルダやファイル向けの規約を、そのファイルに触れたときだけ読み込ませられる。常駐を減らせるが、圧縮の後は引き金のファイルを読むまで戻らない。
signs:
  - {type: goal, text: 特定のディレクトリだけのルールを書きたい}
  - {type: symptom, text: 一部のフォルダ用の規約が、関係のない作業にも毎回読み込まれている}
  - {type: symptom, text: 圧縮の後、フォルダごとの規約が効かなくなった}
  - {type: situation, text: CLAUDE.md が長くなってきた}
prerequisites: [what-to-put-in-claude-md]
related: [claude-md-loading-order, claude-md-length, what-survives-compaction, promises-after-compaction, claude-md-vs-rules-skills-styles, how-skills-load, when-to-lock, always-on-costs, forgot-after-compaction]
tracks: [rules]
sources: [cc-docs-memory, cc-docs-features-overview-ja, cc-docs-context-window, claude-blog-steering-code-skills-hooks]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 雛形, anchor: templates}
  - {title: 圧縮の後に戻る時期, anchor: after-compaction}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：特定のフォルダやファイル向けの規約を `.claude/rules/` に分け、`paths` で一致するファイルに触れたときだけ読み込ませられる。
    - **いつ引くか**：特定のディレクトリだけのルールを書きたいとき。CLAUDE.md が長くなってきたとき。圧縮の後にフォルダごとの規約が効かなくなったとき。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。読み込まれた規約は CLAUDE.md と同じ扱いの指示で、Claude が読んで従うだけである。特定の操作を止める力はない。
    - **前提**：<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->

<!-- textlint-disable -->
別名：rules・パス別のルール・paths のフロントマター・ディレクトリごとの規約
<!-- textlint-enable -->

`.claude/rules/` と `paths` は、フォルダやファイルの種類ごとの規約を、CLAUDE.md から切り出して置く仕組みである。切り出した規約は、一致するファイルに Claude が触れたときだけ会話に入る。常駐する量を減らせる代わりに、圧縮の後の規約は、一致するファイルを再び読むまで戻らない。

## 使いどころ {#when}

`paths` 付きの rules は、一部の場所だけの規約を、全セッションで常駐させないための仕組みである。防ぐ相手は、指示が散らかって焦点がぼやける原因である。`api/` の規約が、ドキュメントを直すだけの作業でも毎回読み込まれる状態が、その例である。

選ぶ基準は、その規約が全作業に要るかどうかである。

- 全作業で要る事実（ビルドの手順、守るべき地雷）は、CLAUDE.md に残す。何を残すかは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> が説明する。
- 言語別・ディレクトリ別の規約は、rules に出す。公式も、CLAUDE.md は全セッションで要るものに絞り、場所ごとの指針は rules に置くよう勧める。
- 複数の手順にまたがる作業の流れは、rules ではなくスキルに置く。考え方は <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end --> にある。

CLAUDE.md を短くする判断そのものは <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end --> が持つ。常駐するものの費用は <!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end --> で確かめる。ここで扱うのは、外へ出した規約の読み込まれ方である。

## 最小の使い方 {#minimal}

使い方は 3 手で足りる。1 つのトピックを 1 つのファイルにして、先頭に `paths` を書く。

=== "Claude Code"

    1. プロジェクトの `.claude/rules/` に、トピックごとの `.md` ファイルを置く。`testing.md` や `api-design.md` のように、中身が分かる名前にする。サブフォルダに分けてもよく、`.md` は再帰的に見つかる。
    2. ファイルの先頭に YAML の フロントマター を書き、`paths` に対象のグロブを並べる。書き方の例は[雛形](#templates)にある。
    3. 本文には、その場所でだけ要る規約を書く。

    `paths` を書かないファイルは、セッションの開始時に読み込まれる。`.claude/CLAUDE.md` と同じ優先度で、CLAUDE.md を分割しただけの扱いである。

    ユーザー単位の規約は `~/.claude/rules/` に置ける。この場合の `paths` は、セッションの主な作業ディレクトリから見た相対になる。

グロブの基準は、プロジェクトの規約なら `.claude` フォルダを含むディレクトリである。よく使う形は次のとおり。

| パターン | 一致するもの |
| --- | --- |
| `**/*.ts` | 基準のディレクトリの下にあるすべての `.ts` |
| `src/**/*` | `src/` の下のすべてのファイル |
| `/*.md` | 基準のディレクトリ直下の `.md`。サブフォルダは含まない |
| `src/components/*.tsx` | `src/components/` 直下の `.tsx`。サブフォルダは含まない |
| `src/**/*.{ts,tsx}` | ブレース展開で、複数の拡張子をまとめて指定する |

読み込みの引き金は、Claude が一致するファイルを Read・Write・Edit で扱うときである。`cat` や `head` で 1 つのファイルを読む Bash の操作も、読みと数えられるものは引き金になる。フォルダ全体を対象にするときは、`src/api/**/*` のようにグロブで書く。

## 雛形 {#templates}

`paths` 付きの規約の例と、読み込まれる時期を確かめる依頼を載せる。どちらも、自分のリポジトリの構成に合わせて置き換える。

<!-- gen:begin snippet path-scoped-rules/api-rule -->
<!-- textlint-disable -->

??? example "雛形：paths を付けた rules のファイル（.claude/rules/api.md）"

    ```markdown
    ---
    paths:
      - "src/api/**/*.ts"
      - "tests/api/**/*.test.ts"
    ---

    # API の規約

    - 入力は、ハンドラの先頭でスキーマを通して検証する
    - エラーは `src/api/errors.ts` の `ApiError` を投げる。ハンドラの中で応答を直接組み立てない
    - 公開する関数には JSDoc を付ける。理由：ドキュメントの生成が JSDoc を読むため
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.64。

<!-- textlint-enable -->
<!-- gen:end snippet path-scoped-rules/api-rule -->

<!-- gen:begin snippet path-scoped-rules/check-loaded -->
<!-- textlint-disable -->

??? example "雛形：条件付きの規約が読み込まれる時期を確かめる依頼"

    ```markdown
    いま会話に入っている、フォルダやファイル向けの規約（.claude/rules の規則）を、ファイル名つきで一覧にして。
    次に `<引き金にしたいファイルのパス>` を読んで、もう一度同じ一覧を出して。
    1 回目と 2 回目で増えた規約があれば、そのファイル名と、規約の先頭の 1 行を書いて。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.64。

<!-- textlint-enable -->
<!-- gen:end snippet path-scoped-rules/check-loaded -->

確かめる依頼の答えは Claude の自己申告である。規約が読み込まれた証拠とは見なさず、効いているかは実際の作業の出力で見る。

## 圧縮の後に戻る時期 {#after-compaction}

`paths` 付きの rules は、圧縮の後、`paths` に一致するファイル（読み込みの引き金になるファイル）を読むか書くまで戻らない。圧縮では会話が要約に置き換わり、一度読み込まれた規約も要約に溶ける。一致するファイルに再び触れると、規約は読み直される。

`paths` のない rules は扱いが違う。直下の CLAUDE.md と同じく、圧縮の後にディスクから入れ直される。同じ rules でも `paths` の有無で答えが分かれるため、機能の属性の表では、圧縮で残るかが「条件による」と出る。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 | コンテキストのコスト | 圧縮で残るか |
| --- | --- | --- | --- | --- |
| [rules（.claude/rules/）](path-scoped-rules.md) | お願い | セッション開始か、一致するファイルを扱うとき | 常駐か、一致するファイルのときだけ | 条件による |

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

圧縮を越えて効かせたい規則は、`paths` を外すか、直下の CLAUDE.md に移す。公式もこの 2 つを勧める。

!!! example "判断例：テストの規約を圧縮の後も効かせる"
    - **状況**：`tests/**` に一致する `paths` 付きの rules に、テストの書き方を置いている。長い作業の途中で圧縮が走り、その後のテストが規約を外れ始めた。
    - **迷う候補**：`paths` を外して常駐させる。規約を直下の CLAUDE.md に移す。`paths` はそのままにして、圧縮の後にテストのファイルを読ませる。
    - **選んだもの**：テストのファイルを読ませて規約を戻し、その規約が全作業で要るなら `paths` を外す。
    - **理由**：外せば常駐の費用が戻る代わりに、圧縮の後も確実に残る。テスト以外の作業が多いなら、読ませて戻す運用のほうが軽い。

圧縮の仕組みの全体は <!-- link:begin what-survives-compaction#reread-on-demand -->[圧縮（compaction）で何が残り、何が消えるか › 必要になったら読み直されるもの](../basics/what-survives-compaction.md#reread-on-demand)<!-- link:end --> が説明する。

約束の置き場所は <!-- link:begin promises-after-compaction#caveats -->[圧縮で消えない場所に約束を置く › paths 付きの rules とスキルの本文の注意](../context/promises-after-compaction.md#caveats)<!-- link:end --> が説明する。

圧縮の後に約束を忘れたときの切り分けは <!-- link:begin forgot-after-compaction#diagnosis -->[圧縮の後に約束を忘れた › 原因を安く確かめる順](../symptoms/forgot-after-compaction.md#diagnosis)<!-- link:end --> を使う。

## 効かない場面と落とし穴 {#limits}

**お願いであって、鍵ではない。** 読み込まれた規約は、Claude が従う指示であり、操作を止めない。例外を許さない禁止は、権限ルールやフックに移す。判断の合図は <!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> が持つ。

**引き金より前の作業には入っていない。** 規約は、一致するファイルに触れた時点で入る。そのため、そのファイルを読む前の計画や判断には、規約が入っていないことがある（推論・実践例なし）。計画の段階から守らせたい規約は、`paths` を外すほうが安全である。

**フロントマター が壊れると、常駐に変わる。** `paths` を含む YAML が解釈できないと、Claude Code は フロントマター を無視し、`paths` のない rules として読み込む。つまり、関係のない作業にも毎回読み込まれる。この症状に当たったら、まず YAML の書き方を疑う。解釈の失敗は `claude --debug` で見られる。

**読む項目は `paths` だけである。** rules の フロントマター のうち、Claude Code が読むのは `paths` だけで、ほかのキーはエラーなしで無視される。説明用のキーを足しても何も起きない。

**グロブの書き間違いは、静かに何も一致しない。** `[` を含む、括弧の式として読めないパターンは、無効として何にも一致しない。同じ rules のほかのパターンは働き続けるので、一部だけ効かない形になる。基準のディレクトリを取り違えた相対パスも、何にも一致しない。

**大きすぎるファイルは、先頭しか入らない。** 引き金で読み込まれる rules には、ファイル 1 つごとのサイズの上限がある。超えると先頭だけが入り、残りは Claude が読みに行くまで会話に入らない。大きいときは、複数のファイルに分ける。上限は、コンテキストの窓とモデルで次のとおり違う。

<!-- gen:begin fact-table claude-md-on-demand-char-limit -->
<!-- textlint-disable -->

| コンテキストの窓とモデル | 上限（文字数） |
| --- | --- |
| 200K の窓 | 40000 |
| 1M の窓（Claude Opus 4.6・Claude Sonnet 4.6） | 200000 |
| 1M の窓（それより後のモデル） | 150000 |

確認日 2026-11-04。出典：[How Claude remembers your project](https://code.claude.com/docs/en/memory)。

<!-- textlint-enable -->
<!-- gen:end fact-table claude-md-on-demand-char-limit -->

**シンボリックリンクには承認がいる。** 作業ディレクトリの外へ向かうリンクは、外部の取り込みと同じ扱いになる。承認の後も、読み込まれるのは `paths` のない rules だけである。共有する規約を `paths` 付きで使いたいなら、`~/.claude/rules/` に置く。

**読み込まれたかを確かめるのは、自分である。** 読み込まれたかは、実際の作業の出力で見るのが確実である。CLAUDE.md の読み込みの確認に使う `/context all` が、条件付きの rules の一覧にも使えるかは未確認である。

## 比べる相手 {#compare}

置き場所の選び方は <!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end --> に表と基準がある。ここでは近い 2 つとの違いだけを書く。

- **サブフォルダの CLAUDE.md**：どちらも必要なときに読み込まれる。ディレクトリに結びつく規約はサブフォルダの CLAUDE.md、`*.test.ts` のように、フォルダをまたぐファイルの種類に結びつく規約は rules が向く。読み込み順と重なりは <!-- link:begin claude-md-loading-order#monorepo -->CLAUDE.md の階層と読み込み順 › モノレポとほかのチームの指示（準備中）<!-- link:end --> で確かめる。
- **スキル**：スキルは作業の手順を、呼ぶ場面で読む。rules はファイルへの触れ方で自動的に入る規約で、手順書には向かない。

## 古くなった助言 {#outdated}

この機能に当たる古い助言の行は、台帳にまだない。気をつけたいのは、次の言い方である。

- 「CLAUDE.md は圧縮の後に再注入される」だけで済ませる説明。直下の CLAUDE.md と `paths` のない rules には当たるが、`paths` 付きの rules には当たらない。
- 「`@import` でコンテキストが減る」という説明。取り込みは起動時に展開されるため、減らしたいなら rules に分けて `paths` で条件付きにする（根拠：弱。実践者の記事による。公式の文書では未確認）。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)

**次に読む**

- [CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)

**関連**

- CLAUDE.md の階層と読み込み順（準備中）
- [CLAUDE.md の長さと剪定](claude-md-length.md)
- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Claude Code を拡張する](https://code.claude.com/docs/ja/features-overview)：Anthropic・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
