---
id: forgot-after-compaction
title: 圧縮の後に約束を忘れた
aliases: [compaction の後に忘れる, 自動圧縮で指示が消えた, /compact の後に忘れる]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 150
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 圧縮の後に、会話で決めた約束や禁止を忘れる原因を切り分け、圧縮で残る場所に移すか、仕組みで縛るかを決める。
signs:
  - {type: symptom, text: 圧縮されたら前に決めたことを忘れた}
  - {type: symptom, text: 会話で禁止したことを圧縮の後にやられた}
  - {type: symptom, text: 自動圧縮の後から作業の進め方が変わった}
wave: 1
prerequisites: [what-survives-compaction]
related: [progress-files, what-to-put-in-claude-md, path-scoped-rules#after-compaction, block-with-exit-2, instructions-ignored, replies-in-english, forgets-in-long-chats, six-causes]
routes:
  - {cause: 散らかっている, to: [promises-after-compaction, compact-and-auto-compact, handoff-documents]}
  - {cause: 縛っていない, to: [when-to-lock#spoken-rules-fade, permission-rules, hook-recipes]}
tracks: [compaction, claude-md, permissions, hooks]
outdated_advice: []
sources: [cc-docs-context-window, cc-docs-memory, cc-docs-best-practices, cc-docs-costs, cc-docs-permissions, cc-docs-hooks-guide, cc-changelog, cc-issue-4017, cc-issue-6354, cc-issue-24460, zenn-hkdeveloper-claudeco]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：約束を圧縮の外に置く, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：圧縮の後に約束を忘れる原因を、置き場所の問題か縛っていない問題かに切り分け、移し先を決められる。
    - **いつ引くか**：圧縮されたら前に決めたことを忘れた、会話で禁止したことを圧縮の後にやられた、自動圧縮の後から作業の進め方が変わった、というとき。
    - **前提**：<!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end -->

<!-- textlint-disable -->
別名：compaction の後に忘れる・自動圧縮で指示が消えた・/compact の後に忘れる
<!-- textlint-enable -->

圧縮の後に約束を忘れた、とは、会話で決めた規則や禁止が、圧縮の後に守られなくなることである。多くは Claude の記憶違いではなく、約束が圧縮で戻らない場所にあったか、頼んだだけで縛っていなかったかのどちらかになる。このページは原因の切り分けと行き先の振り分けを受け持ち、置き場所の仕組みと対処の本体は行き先のページに任せる。Claude Code の挙動を基準に書いており、アプリと API の圧縮で何が残るかは確かめていない（未確認）。

## よくある形 {#forms}

圧縮の後に約束が破られる場面は、次の 4 つの形で現れる。どれも「圧縮より前は守られていた」ことが共通する。

- 長いセッションの途中で自動圧縮が走った後、会話で伝えた「push はレビューの後」を破って push された。
- 手順書を読み込んでいる最中に圧縮が走り、手順の一部が飛んだ。日本語の参加レポートには、これで開発ブランチへの直接 push まで起きた例がある（根拠：弱。二次の参加レポート）。
- 席を外して戻ったら、口調や作業の進め方が変わっていた。放置の間にも圧縮は起きうる。
- 「CLAUDE.md に書いたのに圧縮の後に無視された」という報告が GitHub に複数ある（根拠：弱。題名を確認しただけで、本文と修正状況は未確認）。

圧縮の前から守られていなかったなら、この症状ではない。その場合は <!-- link:begin instructions-ignored -->[CLAUDE.md や指示が守られない](instructions-ignored.md)<!-- link:end --> から切り分ける。

## 原因を安く確かめる順 {#diagnosis}

原因は 2 つに絞れる。約束が圧縮で戻らない場所にあった（散らかっている）か、戻る場所にあっても縛っていなかった（縛っていない）かである。確かめる手間の小さい順に並べる。

1. **約束の置き場所（散らかっている）**：約束が会話の発言にしかなかったかを見る。圧縮の前に、どこで約束したかをたどる。CLAUDE.md・rules・スキル・計画やメモのファイルに書いた覚えがなく、会話で口頭のように伝えただけなら、要約に溶けて消えたと考えるのが自然である。確かめるには、圧縮の直後に、この節の末に置いた雛形の依頼で、Claude に見えている約束とその置き場所を挙げさせる。返答は観察として読み、原因の証明にはしない。仕組みは <!-- link:begin what-survives-compaction#dissolved -->[圧縮（compaction）で何が残り、何が消えるか › 要約に溶けて消えるもの](../basics/what-survives-compaction.md#dissolved)<!-- link:end --> にある。
2. **書いた場所の種類（散らかっている）**：約束が CLAUDE.md や rules にあっても戻らなかったときは、置いた場所を見る。プロジェクトの根の CLAUDE.md は入れ直される。サブフォルダの CLAUDE.md と `paths` 付きの rules は、引き金になるファイルを読むまで戻らない。確かめるには、ファイルの置き場所と `paths` の有無を見る。仕組みの説明は <!-- link:begin what-survives-compaction#reread-on-demand -->[圧縮（compaction）で何が残り、何が消えるか › 必要になったら読み直されるもの](../basics/what-survives-compaction.md#reread-on-demand)<!-- link:end --> と <!-- link:begin path-scoped-rules#after-compaction -->.claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期（準備中）<!-- link:end --> にある。
3. **作業の途中の状態（散らかっている）**：禁止ではなく「手順のどの段まで終えたか」が飛んだときは、状態が会話にしかなかった。読み込んだファイルも、一部しか戻らず、大きいものは中身なしの参照になる。呼び出したスキルの本文も上限付きである。確かめるには、状態を書いたファイルがあるかを見る。置き場所の整理は <!-- link:begin promises-after-compaction#caveats -->[圧縮で消えない場所に約束を置く › paths 付きの rules とスキルの本文の注意](../context/promises-after-compaction.md#caveats)<!-- link:end --> にある。
4. **圧縮が起きたとき（散らかっている）**：自動圧縮は打たなくても走る。席を外した間にも起きる。確かめるには、いつ圧縮が走ったかと、その前に長く放置していなかったかを思い出す。放置で起きる圧縮は <!-- link:begin compact-and-auto-compact#idle-compaction -->/compact と自動圧縮 › 席を外すとき（idle compaction と cache 切れ）（準備中）<!-- link:end --> にある。
5. **例外を許さない禁止か（縛っていない）**：破られたのが「push してはいけない」のような禁止で、置き場所が CLAUDE.md や会話だけなら、縛っていない。公式は、CLAUDE.md や会話の指示は Claude が試みることを変えても、許すことは変えないと書く。会話で言った境界は圧縮で消えうるので、確かな保証には deny ルールを足すよう勧めている。確かめるには、その禁止が設定の権限ルールやフックにあるかを見る。設定にあるルールは圧縮の影響を受けない。判断は <!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end --> にある。
6. **版（どちらにも関わる）**：圧縮まわりの不具合は、版を上げて直ったものがある。大きな CLAUDE.md が変わった後の自動圧縮で失敗する不具合などが、更新履歴に出ている。確かめるには、使っている版と更新履歴の圧縮の項を見る。該当する不具合があって版が古いなら、版を上げてから同じ症状が出るかを見る。

人の側の落とし穴（頼めば伝わると思い込む、規則を詰め込みすぎる）も、置き場所の見直しの前に疑う。診断の全体の入口は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

原因が決まったら、次の表の行き先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 散らかっている | [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)<br>/compact と自動圧縮（準備中）<br>[handoff 文書と document-and-clear](../context/handoff-documents.md) |
| 縛っていない | [お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<br>代表的なフックのレシピ（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

雛形は、圧縮の直後に出す確認の依頼である。作業を進めさせず、見えている約束とその置き場所だけを答えさせる。

<!-- gen:begin snippet forgot-after-compaction/list-known-promises -->
<!-- textlint-disable -->

??? example "雛形：圧縮の後に、いま見えている約束とその置き場所を挙げさせる依頼"

    ```text
    圧縮の後の確認です。作業は進めず、答えるだけにしてください。

    1. いまの文脈で、守ることになっている約束・禁止・手順を、1 つずつ番号を付けて挙げてください。
    2. それぞれについて、どこに書いてあるかを答えてください。CLAUDE.md、rules、スキル、計画やメモのファイル、この会話の中の発言のどれかを、ファイル名つきで。
    3. 会話の発言にしか根拠がない約束があれば、その旨を印を付けて分けてください。
    4. 私が圧縮の前に伝えたはずで、いまの文脈に見当たらないものがあれば、「見当たらない」と書いてください。推測で補わないでください。

    確認したい約束：
    <ここに、圧縮の前に決めた約束を書く>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet forgot-after-compaction/list-known-promises -->

## 判断例 {#examples}

!!! example "判断例：会話で言った「レビューまで push しない」が破られた"
    - **状況**：レビューを待つ作業の最初に、会話で「レビューが済むまで push しないで」と伝えた。長い作業の途中で自動圧縮が走り、その後に push された。
    - **迷う候補**：CLAUDE.md に同じ一文を足して再発を防ぐ。push を deny ルールで止める。
    - **選んだもの**：push を deny ルールで止め、CLAUDE.md には理由だけを残す。push はレビューの後に人が行う。
    - **理由**：例外を許さない禁止だから、お願いのままにしない。CLAUDE.md の一文は入れ直されても、守らせる強制力にはならない。会話の一文は圧縮で失われうる。

!!! example "判断例：長い手順書の途中で圧縮が走り、手順が飛んだ"
    - **状況**：長い手順書を順に実行させている途中で圧縮が走り、終えた段と次の段が曖昧になった。
    - **迷う候補**：手順書の全文を CLAUDE.md に移して常駐させる。手順書は元のファイルのまま置き、終えた段を進捗ファイルに書かせる。
    - **選んだもの**：進捗ファイルに、終えた段と次の段を書かせる。圧縮の後は、手順書と進捗ファイルを読み直させる。
    - **理由**：飛んだのは手順書の内容より「いまどの段か」であり、それは会話にしかなかった。全文の常駐は、毎回の文脈を重くする。

## 予防：約束を圧縮の外に置く {#prevention}

予防の中心は、約束の種類ごとに置き場所を決めることである。置き場所の整理は <!-- link:begin promises-after-compaction#where-to-put -->[圧縮で消えない場所に約束を置く › 約束の種類ごとの置き場所](../context/promises-after-compaction.md#where-to-put)<!-- link:end --> が受け持つ。ここでは入口だけを示す。

- **守ってほしい方針と規則**：プロジェクトの根の CLAUDE.md に置く。圧縮の後も入れ直される。書く内容と外す内容の見分け方は <!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)<!-- link:end --> にある。
- **例外を許さない禁止**：権限ルールかフックに移す。CLAUDE.md には理由と相談の基準だけを残す。フックは会話の外で動くので、圧縮の後も働く。止めた理由を返す書き方は <!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)<!-- link:end --> にある。
- **作業の進み具合と決めたこと**：ファイルに書かせる。置き方は <!-- link:begin progress-files -->進捗ファイルで、途中から再開できるようにする（準備中）<!-- link:end --> にある。
- **長く放置する前、または区切りの前**：書き出してから会話を新しくするか、残す焦点を指示して圧縮する。使い分けは <!-- link:begin handoff-documents#vs-compact -->[handoff 文書と document-and-clear › /compact との使い分け](../context/handoff-documents.md#vs-compact)<!-- link:end --> にある。要約の方針を CLAUDE.md の節に書く方法もある（公式の Manage costs のページが案内する）。

どれも、頼んだだけで終わらせず、圧縮の後に確認の依頼で見えているかを確かめるところまで含める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] /compact causes Claude Code to ignore CLAUDE.md（Issue #4017）](https://github.com/anthropics/claude-code/issues/4017)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[BUG\] Claude forgets everything in CLAUDE.md after compaction（Issue #6354）](https://github.com/anthropics/claude-code/issues/6354)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [CLAUDE.md context lost after /compact — re-inject project instructions（Issue #24460）](https://github.com/anthropics/claude-code/issues/24460)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Claude Code Meetup Japan #3 参加レポート（前編）- 開発手法・実践編](https://zenn.dev/hkdeveloper/articles/claude-code-meetup-japan-3)：Zenn（hkdeveloper）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)

**次に読む**

- [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- /compact と自動圧縮（準備中）
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 代表的なフックのレシピ（準備中）

**関連**

- 進捗ファイルで、途中から再開できるようにする（準備中）
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- .claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期（準備中）
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [CLAUDE.md や指示が守られない](instructions-ignored.md)
- [英語で返ってくる](replies-in-english.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
