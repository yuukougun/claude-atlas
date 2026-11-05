---
id: claude-md-loading-order
title: CLAUDE.md の階層と読み込み順
aliases: [CLAUDE.local.md, '@import', claudeMdExcludes, ユーザーの CLAUDE.md, サブフォルダの CLAUDE.md]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 50
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム]
summary: どの CLAUDE.md がいつ読まれ、どう重なるかを確かめられる。上書きではなく連結され、サブフォルダの分は後から読まれ、取り込みではコンテキストが減らないことが分かる。
signs:
  - {type: symptom, text: 個人の指示とプロジェクトの指示の、どちらが効いているか分からない}
  - {type: situation, text: モノレポで、フォルダごとに違う規約がある}
  - {type: symptom, text: ほかのチームのフォルダの指示まで読み込まれている}
prerequisites: [what-to-put-in-claude-md]
related: [path-scoped-rules, what-survives-compaction, agents-md, settings-layers, using-auto-memory, managed-settings-enforcement, share-team-settings, inspect-context, claude-md-length, forgot-after-compaction]
tracks: [claude-md, rules]
sources: [cc-docs-memory, cc-docs-context-window]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 読み込まれる場所と順番, anchor: order}
  - {title: 取り込みでは減らない, anchor: import}
  - {title: 最小の使い方, anchor: usage}
  - {title: モノレポとほかのチームの指示, anchor: monorepo}
  - {title: 圧縮の後と、クラウドのセッション, anchor: after-compaction}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：どの CLAUDE.md がいつ読まれ、どう重なるかを確かめ、モノレポで余計な指示を外せる。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。どの階層の CLAUDE.md も、Claude が読んで従うだけの文脈で、何も止められない。例外を許さない禁止は、読み込み順で守らせようとせず、鍵に移す。
    - **いつ引くか**：個人の指示とプロジェクトの指示のどちらが効いているか分からないとき、モノレポでフォルダごとに規約が違うとき、ほかのチームの指示まで読み込まれているとき。
    - **前提**：<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->

<!-- textlint-disable -->
別名：CLAUDE.local.md・@import・claudeMdExcludes・ユーザーの CLAUDE.md・サブフォルダの CLAUDE.md
<!-- textlint-enable -->

CLAUDE.md の階層と読み込み順は、複数の場所に置いた CLAUDE.md が、どの時点でどの順に Claude の文脈へ入るかの決まりである。結論は 3 つある。ファイルは上書きされず連結される。サブフォルダの分は、起動時より後に読まれる。`@import` で取り込んでも文脈は減らない。

## 使いどころ {#when}

CLAUDE.md を複数の場所に置き始めると、「いま Claude には何が見えているのか」が分からなくなる。このページが防ぐ原因は「見えていない」と「散らかっている」である。効かせる原理は「見せる」で、読み込まれているものを一覧で確かめ、余計なものは外す。

引くのは、次のような場面だ。

- 個人の `~/.claude/CLAUDE.md` とプロジェクトの CLAUDE.md の両方に書いてあり、どちらが効いているのか分からない。
- モノレポで、フォルダごとに違う規約を CLAUDE.md に書き分けたい。
- 自分のチームと関係のないフォルダの指示が、文脈に入ってしまっている。
- 書く内容の判断は<!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](what-to-put-in-claude-md.md#what-to-write)<!-- link:end -->に任せる。このページは、書いたものが読まれる仕組みを扱う。

## 読み込まれる場所と順番 {#order}

Claude Code は、作業ディレクトリ（`claude` を起動したフォルダ）とその上のすべての階層から、`CLAUDE.md` と `CLAUDE.local.md` を起動時に読む。見つかったファイルは、上書きではなく連結されて文脈に入る。並びは、ファイルシステムの根に近いほうが先で、作業ディレクトリに近いほうが後になる。同じ階層では、`CLAUDE.local.md` が `CLAUDE.md` の後に付く（[How Claude remembers your project](https://code.claude.com/docs/en/memory)）。

作業ディレクトリより下のサブフォルダにある `CLAUDE.md` と `CLAUDE.local.md` は、起動時には読まれない。Claude がそのサブフォルダのファイルを読むか、書くか、編集したときに、1 回だけ読み込まれる。単一のファイルに `cat` や `head` をかける Bash も、読んだことに数えられる（同じ文書）。

```text
monorepo/
├── CLAUDE.md             起動時（作業ディレクトリより上の階層）
├── CLAUDE.local.md       起動時（同じ階層では CLAUDE.md の後）
├── other-team/
│   └── CLAUDE.md         起動時には読まれない（上の階層でも下の階層でもない）
└── team-a/               ここで claude を起動する（作業ディレクトリ）
    ├── CLAUDE.md         起動時
    └── api/
        └── CLAUDE.md     Claude が api/ のファイルを読み書きしたとき
```

この木から読み取れることは 4 つある。

- 個人の指示（`~/.claude/CLAUDE.md`）とプロジェクトの指示は、どちらも文脈に入り、片方がもう片方を消すことはない。矛盾する指示があると、Claude はどちらかを選んでしまうことがある。順番は「後ろが勝つ」という保証ではない。公式の文書は、矛盾を見つけて消すことを勧めている。
- 作業ディレクトリの上にある CLAUDE.md は、起動した場所を下げても読まれ続ける。読み込みを減らしたいなら、起動する場所を変えるのではなく、読み込みから外す（外し方は「モノレポとほかのチームの指示」の節にある）。
- 同じ階層の兄弟フォルダ（上の図の `other-team/`）は、起動時には読まれない。ただし Claude がそのフォルダのファイルを読めば、後から入る。
- `--add-dir` で足したフォルダの CLAUDE.md は、既定では読まれない。環境変数 `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` を `1` にすると読まれる。

なお、AGENTS.md は、作業ディレクトリかその上に CLAUDE.md か `CLAUDE.local.md` があると、既定では読まれない。その扱いは<!-- link:begin agents-md -->[AGENTS.md とほかのツールとの共有](agents-md.md)<!-- link:end -->にまとめてある。

## 取り込みでは減らない {#import}

`@path/to/file` と書くと、別のファイルを CLAUDE.md の中に取り込める。相対パスは、取り込む側のファイルを基準に解決される。取り込みは入れ子にでき、段数は<!-- fact:begin claude-md-import-max-hops -->4 段（ホップ）まで（2026-11-05 時点）<!-- fact:end -->。

取り込みは整理のための仕組みで、文脈の節約にはならない。取り込まれたファイルも起動時に一緒に展開されるので、読み込まれる量は変わらない。サブフォルダの CLAUDE.md が取り込むファイルも、その CLAUDE.md と一緒に後から読まれる。

読み込む量を減らしたいときは、取り込みではなく、パスで条件を付けた rules を使う。仕組みは<!-- link:begin path-scoped-rules#when -->[.claude/rules と paths で必要なときだけ読ませる › 使いどころ](path-scoped-rules.md#when)<!-- link:end -->にある。

プロジェクトの CLAUDE.md が、作業ディレクトリの外のファイル（たとえばホームの下）を取り込むと、最初の 1 回だけ承認のダイアログが出る。断ると、その取り込みは無効のままになる。

## 最小の使い方 {#usage}

このページの機能は Claude Code に固有で、面ごとの手段の違いはない。確かめと外し方は、次の順で行う。

1. セッションの中で `/context all` を実行し、**Memory files** の一覧を見る。ここにないファイルは、Claude には見えていない。一覧の読み方の全体は<!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end -->にある。
2. `/memory` を実行する。CLAUDE.md、`CLAUDE.local.md` と、そのほかの記憶ファイルの場所が一覧で出る。まだ存在しない個人用・プロジェクト用のファイルも出るので、そこから開いて編集できる。
3. サブフォルダの CLAUDE.md は、起動時の一覧には出ない。読み込まれたときに、端末に `Loaded` の行とパスが出る。新しく置いたサブフォルダの CLAUDE.md を試すなら、Claude に書かせず、シェルで作ってから、そのサブフォルダのファイルを読ませる。
4. いつ・なぜ読み込まれたかを記録に残したいときは、`InstructionsLoaded` フックを使う（[Hooks reference](https://code.claude.com/docs/en/hooks)）。パス付き rules や、後から読まれるサブフォルダの分を調べるのに向く。
5. 余計なファイルは、設定の `claudeMdExcludes` で外す（書き方は「モノレポとほかのチームの指示」の節にある）。

個人だけの指示は、プロジェクトの根に `CLAUDE.local.md` を置く。CLAUDE.md と同じ扱いで読まれ、同じ階層では CLAUDE.md の後ろに付く。`.gitignore` に足して、コミットされないようにする。

## モノレポとほかのチームの指示 {#monorepo}

モノレポでは、規約を置く場所で、読まれる範囲が決まる。共通の方針を根の CLAUDE.md に置くと、全員の起動時に入る。チーム固有の規約をチームのフォルダの CLAUDE.md に置くと、そのフォルダの中で起動したときと、そのフォルダのファイルを読んだときだけ入る。

ほかのチームの指示が入ってくるのは、主に次の 3 つの場合である。

- ほかのチームの規約が、作業ディレクトリより上の階層の CLAUDE.md に書いてある。起動時に必ず連結される。
- モノレポの根で起動し、ほかのチームのフォルダのファイルを Claude が読んだ。そのフォルダの CLAUDE.md が、後から入る。
- 追加のフォルダを `--add-dir` で足し、環境変数 `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` を `1` にしている。

外すには、設定の `claudeMdExcludes` に、パスか glob のパターンを並べる。パターンは絶対パスに対して照合され、ユーザー・プロジェクト・手元・管理のどの層に書いてもよい。配列は層をまたいで合わさる。自分の手元だけで外すなら、`.claude/settings.local.json` に書く。組織の管理の CLAUDE.md は、この設定では外せない。層と優先順位は<!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end -->を見る。具体的な設定は、雛形の節にある。

!!! example "判断例：ほかのチームの規約が根の CLAUDE.md に混ざっている"
    - **状況**：モノレポの根の CLAUDE.md に、チーム A 向けの規約まで書いてある。チーム B の自分が `team-b/` で起動すると、チーム A の規約も起動時に入る。
    - **迷う候補**：ア：自分の `.claude/settings.local.json` の `claudeMdExcludes` で、根の CLAUDE.md を外す。イ：根の CLAUDE.md を直して、チーム A の規約を `team-a/CLAUDE.md` に移す。
    - **選んだもの**：まずアで手元の混ざりを止め、並行してイをチームに提案する。
    - **理由**：アは自分の手元だけで今すぐ効くが、根の CLAUDE.md には共通の方針も書いてあるので、外すと共通の方針も失う。イなら、根には共通の方針だけが残り、全員の手元が同時に直る。チームで共有する設定の入れ方は<!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end -->を見る。

## 圧縮の後と、クラウドのセッション {#after-compaction}

圧縮（compaction）で会話が要約に置き換わるとき、CLAUDE.md は読み込まれ方で扱いが分かれる。プロジェクト直下の CLAUDE.md は、ディスクから読み直されて文脈に入れ直される。サブフォルダの CLAUDE.md は要約に溶け、そのサブフォルダのファイルを再び読むか書くまで戻らない（[Explore the context window](https://code.claude.com/docs/en/context-window)）。

だから、サブフォルダの CLAUDE.md にだけ書いた規則は、長い作業の途中で圧縮が起きると、見えなくなることがある。圧縮を越えて効かせたい規則は、プロジェクト直下の CLAUDE.md に移す。圧縮全体の表は<!-- link:begin what-survives-compaction#kept -->[圧縮（compaction）で何が残り、何が消えるか › そのまま効くもの](../basics/what-survives-compaction.md#kept)<!-- link:end -->、約束を忘れたときの切り分けは<!-- link:begin forgot-after-compaction#diagnosis -->[圧縮の後に約束を忘れた › 原因を安く確かめる順](../symptoms/forgot-after-compaction.md#diagnosis)<!-- link:end -->にある。作業ディレクトリより上の階層の CLAUDE.md が圧縮の後にどうなるかは、公式の表がプロジェクト直下の分しか書いておらず、このページでは確かめていない。

クラウドのセッションでは、読まれるものが手元と違う。個人の `~/.claude/CLAUDE.md` と `.claude/settings.local.json` は、クラウドのセッションに届かない。リポジトリに入っている CLAUDE.md は届く。個人の指示をクラウドに届けたいときは、環境の setup script で `~/.claude/CLAUDE.md` を書く方法がある。リポジトリの CLAUDE.md に入れると、チーム全員に効く。

## 雛形 {#templates}

1 つ目は、個人だけの指示を置く `CLAUDE.local.md` である。最後の行は、ホームに置いた別のファイルを取り込む例で、worktree をまたいで同じ個人の指示を使いたいときに使う。`CLAUDE.local.md` はそれを作った worktree にしか存在しないためである。

<!-- gen:begin snippet claude-md-loading-order/claude-local -->
<!-- textlint-disable -->

??? example "雛形：個人だけの指示を置く CLAUDE.local.md"

    ```markdown
    # 個人の設定（このリポジトリの手元だけ）

    - 手元の動作確認は、ローカルの開発サーバー（http://localhost:3000）に向ける
    - テストを流すときは、まず変えたファイルの分だけ流し、全体は最後に 1 回流す
    - 自分用のメモは ~/.claude/my-project-instructions.md にも置いてある
    - @~/.claude/my-project-instructions.md
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-loading-order/claude-local -->

2 つ目は、ほかのチームのフォルダの CLAUDE.md と rules を読み込みから外す設定である。`other-team` の部分は、自分のモノレポのフォルダ名に変える。

<!-- gen:begin snippet claude-md-loading-order/exclude-other-teams -->
<!-- textlint-disable -->

??? example "雛形：ほかのチームのフォルダの CLAUDE.md と rules を読み込みから外す設定"

    ```json
    {
      "claudeMdExcludes": [
        "**/other-team/CLAUDE.md",
        "**/other-team/.claude/CLAUDE.md",
        "**/other-team/.claude/rules/**"
      ]
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-loading-order/exclude-other-teams -->

## 効かない場面と落とし穴 {#limits}

- **階層は強制ではない**：どの階層の CLAUDE.md も、Claude には文脈として渡るだけである。深いフォルダの CLAUDE.md に書いても、守らせる力は強くならない。例外を許さない禁止は、置き場所をどう工夫しても守られる保証にならない。鍵に移し、CLAUDE.md には理由を書く。移し先は<!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end -->にある。
- **「取り込めば短くなる」は誤解**：取り込みは、読む側のファイルを短く見せるだけで、文脈に入る量は同じである。長さが問題なら、<!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end -->の問いで行を減らす。
- **サブフォルダの分は、必要な時点で入るとは限らない**：Claude がそのフォルダのファイルを読むまで入らない。作業の最初の指示にそのフォルダの規約が要るなら、サブフォルダの CLAUDE.md では間に合わないことがある。
- **後から読まれる分には大きさの上限がある**：サブフォルダの CLAUDE.md や、後から読まれる rules が上限を超えると、先頭だけが渡る。後半は Claude がファイルを読みに行くまで文脈に入らない。上限は、下の表のとおりである。

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

- **矛盾は選び方が保証されない**：個人・プロジェクト・サブフォルダの間で矛盾すると、Claude はどちらかを選ぶ。読まれる順の最後が勝つとは言えないので、矛盾は定期的に探して消す。
- **管理の CLAUDE.md は外せない**：`claudeMdExcludes` は、組織が配る管理の CLAUDE.md には効かない。強制の仕組みは、<!-- link:begin managed-settings-enforcement#cannot-override -->管理設定と組織の強制 › 利用者の側から外せない範囲（準備中）<!-- link:end -->にある。
- **手元の確認は WSL・Linux の CLI を基準にしている**：ほかの OS と IDE 拡張で、読み込まれる場所や順番が同じかは、未確認である。

## 比べる相手 {#compare}

CLAUDE.md と rules は、どちらも指示をファイルで置く機能だが、読み込む時期が違う。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 読み込みの時期 | コンテキストのコスト | 圧縮で残るか |
| --- | --- | --- | --- |
| [CLAUDE.md](what-to-put-in-claude-md.md) | セッション開始 | 常駐 | 残る |
| [rules（.claude/rules/）](path-scoped-rules.md) | セッション開始か、一致するファイルを扱うとき | 常駐か、一致するファイルのときだけ | 条件による |

すべて共通：強制力 お願い。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

- **rules**：パスで条件を付けると、一致するファイルを扱うときだけ読み込める。階層に置くだけの CLAUDE.md より、読み込む時期を細かく決められる。使い方は<!-- link:begin path-scoped-rules#minimal -->[.claude/rules と paths で必要なときだけ読ませる › 最小の使い方](path-scoped-rules.md#minimal)<!-- link:end -->にある。
- **設定ファイル**：設定は、同じキーなら優先順位の高い層が勝つ。CLAUDE.md は、層が違っても連結される。この違いは<!-- link:begin settings-layers#merge -->[設定ファイルの階層と優先順位 › 合わさる設定、上書きされる設定](../cli/settings-layers.md#merge)<!-- link:end -->にある。
- **自動メモリ**：Claude が自分で書き溜める記録で、人が書く CLAUDE.md と役割が違う。分担は<!-- link:begin using-auto-memory#when -->[自動メモリ › 使いどころ](using-auto-memory.md#when)<!-- link:end -->にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)

**次に読む**

- [AGENTS.md とほかのツールとの共有](agents-md.md)

**関連**

- [.claude/rules と paths で必要なときだけ読ませる](path-scoped-rules.md)
- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [自動メモリ](using-auto-memory.md)
- 管理設定と組織の強制（準備中）
- [チームで設定を共有する](../team/share-team-settings.md)
- [/context で中身を見る](../context/inspect-context.md)
- [CLAUDE.md の長さと剪定](claude-md-length.md)
- [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
