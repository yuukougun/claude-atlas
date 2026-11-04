---
id: claude-md-length
title: CLAUDE.md の長さと剪定
aliases: [CLAUDE.md が長い, CLAUDE.md の行数, /doctor prompt-audit, CLAUDE.md の育て方]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 40
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: [体感を信じる]
scenes: [開発, チーム]
summary: CLAUDE.md や /init の叩き台を、行ごとに残すか削るかを判断して短く保てる。消したら誤りが出るかで選び、強調しても守られない行はファイルを短くするか鍵に移す。
signs:
  - {type: situation, text: CLAUDE.md が長くなってきた}
  - {type: goal, text: CLAUDE.md から何を削ればよいか知りたい}
prerequisites: [what-to-put-in-claude-md, always-on-costs]
related: [init-and-first-claude-md, path-scoped-rules, how-skills-load, when-to-lock, emphasis-words, instructions-ignored, pruning-extensions, measure-changes, felt-vs-measured, after-switching-models, share-team-settings, claude-md-loading-order, inspect-context, claude-md-vs-rules-skills-styles]
tracks: [claude-md]
outdated_advice: [important-caps, architecture-in-claude-md]
sources: [cc-docs-memory, cc-docs-best-practices, cc-changelog, humanlayer-writing-good, tembo-write-great, darragh-stopped-coding-weeks-still-placed, qiita-hikariclaude01-e54c70, serverworks-claude-md-guide, wb-cc-best-practices-2026-10-26, wb-cc-best-practices-2026-10-27]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 削るときの問い, anchor: deletion-test}
  - {title: /init の叩き台を削る, anchor: init-draft}
  - {title: 剪定のプロンプト, anchor: prune-prompt}
  - {title: チームで育てる, anchor: team}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：CLAUDE.md や `/init` の叩き台を、行ごとに「消したら誤りが出るか」で選び、短く保てる。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。長さを整えても、Claude が読んで従うだけで何も止められない。強調しても守られない行は、ファイルを短くするか、例外を許さない規則なら鍵（フックや deny ルール）に移す。
    - **いつ引くか**：CLAUDE.md が長くなってきたとき、CLAUDE.md から何を削ればよいか知りたいとき。
    - **前提**：<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->・<!-- link:begin always-on-costs -->[常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)<!-- link:end -->

<!-- textlint-disable -->
別名：CLAUDE.md が長い・CLAUDE.md の行数・/doctor prompt-audit・CLAUDE.md の育て方
<!-- textlint-enable -->

CLAUDE.md の長さと剪定は、書き足して長くなったファイルを、行ごとに残すか削るかを決めて短く保つ作業である。決め手は行数ではなく、その行を消したら Claude が作業を間違えるかどうかだ。このページは、その問い方、`/init` の叩き台の削り方、チームでの育て方をまとめる。

## 使いどころ {#when}

CLAUDE.md の全文は、セッションを始めるたびに文脈へ入り、毎回のリクエストに乗り続ける。長いファイルには 2 つの害がある。毎回の費用が増えることと、必要な行が周りの行に埋もれて守られにくくなることだ。常駐の費用の全体像は<!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end -->に任せる。

このページが防ぐ原因は「散らかっている」である。文脈の中に関係のない行が混ざり、効かせたい行が目立たなくなる。効かせる原理は「見せる」で、Claude に見せるものを、リポジトリを読んでも分からないことだけに絞る。

引くのは、次のような場面だ。

- 書き足すうちにファイルが長くなり、全体が見通せなくなってきた。
- 規則を書いたのに守られず、強調を足したくなっている。
- `/init` が作った叩き台を、そのまま使ってよいか迷っている。

公式の文書は、<!-- fact:begin claude-md-recommended-lines -->目安は 1 ファイル 200 行以内（2026-11-04 時点）<!-- fact:end -->と書く。

## 削るときの問い {#deletion-test}

削るときの問いは 1 つである。**この行を消したら、Claude は間違えるか**。間違えないなら削る。リポジトリのコード・設定・README を読めば分かることは、消しても間違えない。

行の種類ごとの判定は、次のようになる。

| 行の種類 | 判定と行き先 |
| --- | --- |
| 推測できないコマンド・理由・落とし穴・確かめ方 | 残す。書き方は<!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> |
| ディレクトリの木・ファイルの一覧・フレームワークの説明 | 削る。Claude がリポジトリを自分で読む |
| 標準的な言語の規約・linter で検査できる規約 | 削る。検査は linter やフォーマッタに任せる |
| 詳しい API 文書 | 削り、リンクにする |
| 特定のフォルダだけに関わる規約 | rules に移す。<!-- link:begin path-scoped-rules#after-compaction -->.claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期（準備中）<!-- link:end --> |
| たまにしか使わない長い手順 | スキルに移す。<!-- link:begin how-skills-load#after-compaction -->スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの（準備中）<!-- link:end --> |
| 例外を許さない禁止 | 鍵に移し、CLAUDE.md には理由だけを残す。<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> |

最小の手順は次の 5 つだ。

1. 今の行数と、見出しごとの行数を控える。`/context` で起動直後の内訳も控えておく（<!-- link:begin inspect-context#baseline -->[/context で中身を見る › 起動直後の基準値](../context/inspect-context.md#baseline)<!-- link:end -->）。
2. 上の問いを 1 行ずつ当て、「残す」「削る」「移す」「判断できない」に分ける。「判断できない」は、理由が見えない行で、書いた人に聞く。
3. 「削る」を消し、「移す」を移し先に写す。1 回で全部やらず、まとまりごとに分けると、効いた変更と効かなかった変更を区別しやすい。
4. 削った後に、`/doctor` を実行する。コードから導き出せる内容の削減案が出る。さらに `/doctor prompt-audit` は、古いモデル向けに書いた指示・存在しないファイルへの参照・矛盾する指示を洗い出す。後者には、<!-- fact:begin doctor-prompt-audit-min-version -->Claude Code 2.1.283 以上が要る（2026-11-04 時点）<!-- fact:end -->。
5. 削って良くなったかは、体感で決めない。前に失敗したタスクを新しいセッションで前後に何度か走らせて比べる（<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end -->、<!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end -->）。

!!! example "判断例：強調を足したくなる行"
    - **状況**：「テストの前に必ずマイグレーションを流す」と CLAUDE.md に書いたが、たまに飛ばされる。
    - **迷う候補**：行を IMPORTANT で強調する。ファイル全体を先に短くする。フックでマイグレーションを強制する。
    - **選んだもの**：まずファイルを短くし、それでも飛ばされるなら、例外のない規則なのでフックにする。
    - **理由**：強調を足しても直らず、むしろ規則を当てはめすぎる原因になる。飛ばされる原因が、長すぎて埋もれているのか、お願いでは足りない規則なのかを分けて見るほうが、早く直る。

**行数の目安の幅。** 割れる論点なので、三段に分けて書く。

- 公式の立場：目安は <!-- fact:begin claude-md-recommended-lines -->目安は 1 ファイル 200 行以内（2026-11-04 時点）<!-- fact:end -->で、長いと文脈を使い、守られにくくなると書く。
- 実践者の幅：記事によって、100 行ほどから数百行まで割れる（根拠：弱）。Kaggle で 3 位に入った参加者は、最終的に 681 行になったと自己申告している（根拠：弱）。Claude Code 開発者のチームの約 2.5k トークンという値は二次要約の数字で、一次資料では確かめていない。
- この辞典の推奨：行数は目安にとどめ、各行に「消したら誤りが出るか」を当てる。長くても毎回必要な行なら残してよい。公式の目安を大きく超えるなら、移せる行がないかを先に探す。

「従える指示は 150〜200 個ほど」という数字もよく引かれるが、出どころの記事が厳密な調査ではないと断っている値なので、この辞典は根拠にしない。

## /init の叩き台を削る {#init-draft}

`/init` は、リポジトリを調べて CLAUDE.md の叩き台を作る。叩き台は膨らみやすく、重要な「なぜ」が抜けやすい（根拠：弱。実践者の主張）。叩き台に入りがちなのは、構成の説明、ファイルごとの説明、フレームワークの紹介で、どれも Claude がリポジトリから自分で読み取れる。

実践者の間では、叩き台を使う派（公式を含む）と、1 行ずつ手で書く派に割れている。この辞典は、**叩き台に使うなら、必ず削って手で直してから使い始める**とする。手で書く場合も、書いた後に同じ問いで削る。操作の流れは<!-- link:begin init-and-first-claude-md#run-init -->/init と最初の CLAUDE.md › /init で叩き台を作る（準備中）<!-- link:end -->、手で書く流儀との違いは<!-- link:begin init-and-first-claude-md#by-hand -->/init と最初の CLAUDE.md › 手で書く流儀との違い（準備中）<!-- link:end -->にある。

削る順番は、次のようにする。

1. 叩き台を最後まで読み、リポジトリを見れば分かる節をまとめて消す。
2. 残った行に、削るときの問いを当てる。
3. 抜けている「なぜ」と落とし穴を、手で足す。踏んだ地雷、触ってはいけないファイル、コマンドの癖がその対象である。

!!! example "判断例：叩き台の「プロジェクト構成」の節"
    - **状況**：`/init` の叩き台に、ディレクトリの木と各フォルダの説明が 40 行ある。
    - **迷う候補**：新しい人が読むときに便利なので残す。Claude が読み取れるので削る。
    - **選んだもの**：木と説明は削り、「なぜ API とワーカーを分けたか」のような設計の判断だけを数行で残す。
    - **理由**：構成は Claude が自分で読むが、判断の理由はコードから読み取れない。人に便利な地図は README に置けばよい。

## 剪定のプロンプト {#prune-prompt}

下のプロンプトは、各行に「消したら誤りが出るか」を問わせ、書き換える前に判定の表を出させる。承認するまでファイルを書き換えさせないのが要点で、何を消したかが見えなくなるのを防ぐ。

<!-- gen:begin snippet claude-md-length/prune-prompt -->
<!-- textlint-disable -->

??? example "雛形：各行に「消したら誤りが出るか」を問わせる剪定のプロンプト"

    ```markdown
    CLAUDE.md を、行ごとに残すか削るかを判断して短くしたい。まだ何も書き換えず、先に案だけを出してほしい。

    手順は次のとおり。

    1. CLAUDE.md を最後まで読む。行数を数え、見出しごとの行数も出す。
    2. 各行について「この行を消したら、Claude は作業を間違えるか」を調べる。リポジトリのコード・設定・README を読めば分かることは、消しても間違えない側に入れる。
    3. 次の 4 つに分けて表にする。列は「行（または範囲）」「判定」「理由」「移し先」。
       - 残す：コードから推測できないコマンド、理由、落とし穴、確かめ方
       - 削る：構成の説明、ファイルごとの説明、標準的な規約、コードの写し
       - 移す：特定のフォルダだけに関わる規約、たまにしか使わない手順、例外を許さない禁止
       - 判断できない：理由がこの場から分からない行（私に聞く）
    4. 「移す」の行は、移し先を選ぶ。フォルダ別の規約は rules、たまに使う手順は skill、例外を許さない禁止は deny ルールかフックにする。
    5. 強調（IMPORTANT・必ず・大文字）が付いた行は、別に一覧にする。強調を足したくなる行は、ファイルが長すぎて埋もれていないか、鍵にすべき規則かを、理由と一緒に書く。

    私が表を見て承認するまで、ファイルを書き換えないこと。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-length/prune-prompt -->

試すときは、CLAUDE.md を git に入れてからにする。表の判定は Claude の推測なので、「削る」の行は自分の目でも確かめる。

## チームで育てる {#team}

CLAUDE.md はチームの合意文書として、リポジトリに入れて育てる。個人の好みは共有のファイルに入れず、`CLAUDE.local.md` か `~/.claude/CLAUDE.md` に分ける。共有する設定全体の分け方は<!-- link:begin share-team-settings#shared-vs-personal -->チームで設定を共有する › 共有するものと個人に残すもの（準備中）<!-- link:end -->にある。

育てる運用の案は、次のとおりだ。

- 変更は PR にして、別のメンバーが承認する。古い・矛盾した指示は、自信のある誤ったコードを生むので、足すより直すほうを重く見る（根拠：弱）。
- 足す基準は、同じ誤りを 2 回訂正したときにする。書く行の選び方は<!-- link:begin what-to-put-in-claude-md#adding-lines -->[CLAUDE.md に書くこと・書かないこと › 足すときの手順](what-to-put-in-claude-md.md#adding-lines)<!-- link:end -->にある。
- 定期的に棚卸しする。月に 1 回という頻度は実践者の経験則で（根拠：弱）、公式の決まりではない。棚卸しのたびに、上の問いを全行に当てる。
- モデルを替えたときも見直す。古いモデル向けに入れた強調や検証の指示が残っていないかを見る（<!-- link:begin after-switching-models#checklist -->新しいモデルに替えたら見直すこと › 見直す順（準備中）<!-- link:end -->）。
- モノレポで、ほかのチームの CLAUDE.md が混ざって読まれるときは、除外の設定がある（<!-- link:begin claude-md-loading-order#monorepo -->CLAUDE.md の階層と読み込み順 › モノレポとほかのチームの指示（準備中）<!-- link:end -->）。

拡張の全体（skills・MCP・プラグイン）の棚卸しは、<!-- link:begin pruning-extensions#criteria -->拡張の棚卸しと剪定 › 切る基準（準備中）<!-- link:end -->が持つ。

## 効かない場面と落とし穴 {#limits}

- **削っても守られない規則がある。** お願いの形のまま短くしても、例外を許さない規則は破られる。原因の切り分けは<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end -->、鍵に移す判断は<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->に任せる。
- **体感で決めると外れる。** 「短くしたら速く・賢くなった」は体感で、削る前後の記録とずれることがある。落とし穴は「体感を信じる」ことで、判断は同じ物差しで取った記録に頼る（<!-- link:begin felt-vs-measured#evidence -->[体感と実測 › 何が起きるか（研究と根拠の強さ）](../eval/felt-vs-measured.md#evidence)<!-- link:end -->）。
- **行を別のファイルに分けただけでは減らない。** `@path` の取り込みは整理に役立つが、取り込み先も一緒に読み込まれ、常駐の量は減らない（<!-- link:begin claude-md-loading-order -->CLAUDE.md の階層と読み込み順（準備中）<!-- link:end -->）。減らしたいなら、rules に移して条件付きで読ませるか、スキルに移す。
- **「なぜ」まで削らない。** 行数を詰めるあまり、理由を消すと、Claude が例外の場面で判断できなくなる。コマンドだけ残して理由を消した行は、削る前より弱い。
- **対象の範囲。** 手順は Claude Code を WSL・Linux の CLI で使う場合を基準にした。ほかの OS と IDE 拡張で `/doctor` の出力が同じかは未確認である。

## 比べる相手 {#compare}

- CLAUDE.md のほかに rules・スキル・スタイルのどれへ移すかは、<!-- link:begin claude-md-vs-rules-skills-styles -->[CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)<!-- link:end -->で比べている。
- CLAUDE.md に何を書くかの方針は<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->、このページは「書いた後に短く保つ」側を持つ。
- 強調語で守らせる話は<!-- link:begin emphasis-words#why-not -->強調語（IMPORTANT・必ず）の現在 › 強調で直らない二つの理由（長すぎる・例外がない）（準備中）<!-- link:end -->が持つ。

## 古くなった助言 {#outdated}

- **IMPORTANT や YOU MUST で強調すれば守られる。** 今は強調せず、ふつうの言葉で書く。それでも守られないなら、ファイルが長すぎないかを見て短くし、例外を許さない規則ならフックか deny ルールにする。改稿前の公式の文書は、守られない 1 行にだけ強調を付けるよう勧めていた。扱いは<!-- link:begin outdated-advice-ledger#important-caps -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#important-caps)<!-- link:end -->にある。
- **アーキテクチャやファイル構成を CLAUDE.md に書く。** 今は、書かない。Claude がリポジトリを自分で読むので、書くのは、読んでも分からない理由・決まり・落とし穴だけにする。扱いは<!-- link:begin outdated-advice-ledger#architecture-in-claude-md -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#architecture-in-claude-md)<!-- link:end -->にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)

**関連**

- /init と最初の CLAUDE.md（準備中）
- .claude/rules と paths で必要なときだけ読ませる（準備中）
- スキルの考え方（手順を必要なときだけ読む）（準備中）
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- 強調語（IMPORTANT・必ず）の現在（準備中）
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- 拡張の棚卸しと剪定（準備中）
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [体感と実測](../eval/felt-vs-measured.md)
- 新しいモデルに替えたら見直すこと（準備中）
- チームで設定を共有する（準備中）
- CLAUDE.md の階層と読み込み順（準備中）
- [/context で中身を見る](../context/inspect-context.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)：HumanLayer・英語・確認日 2026-11-04
- [How to Write a Great CLAUDE.md: Best Practices and Tips](https://www.tembo.io/blog/how-to-write-a-great-claude-md)：Tembo・英語・確認日 2026-11-04
- [I Stopped Coding for 11 Weeks — and Still Placed 3rd on Kaggle](https://darragh.bearblog.dev/i-stopped-coding-for-11-weeks-and-still-placed-3rd-on-kaggle/)：Darragh・英語・確認日 2026-11-04
- [CLAUDE.md 設計パターン集──プロジェクト規模別に使い分ける7つのテンプレート](https://qiita.com/hikariclaude01/items/e54c70c90c6aa84d0f66)：Qiita（hikariclaude01）・確認日 2026-11-04
- [CLAUDE.md の書き方ガイド － Claude Code にプロジェクトのルールを教える方法](https://blog.serverworks.co.jp/claude-code-claudemd-guide)：サーバーワークス・確認日 2026-11-04
- [Best practices for Claude Code（改稿前。Internet Archive の写し、2026-10-26 19:44 UTC）](https://web.archive.org/web/20261026194435/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04
- [Best practices for Claude Code（改稿後。Internet Archive の写し、2026-10-27 08:15 UTC）](https://web.archive.org/web/20261027081520/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
