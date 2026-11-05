---
id: checking-for-updates
title: 最新を自分で確かめる方法
aliases: [変更の追い方, 変更履歴の読み方, リリースノート, 手元の版を確かめる]
type: recipe
field: changes
chapter: 古い情報を見分ける
order: 40
level: 整える
priority: 推奨
surfaces: [claude-code, app, api]
principle: [確かめる]
summary: 手元の版と、Claude Code の変更履歴・Help Center と API のリリースノート・公式の文書の改稿を自分で確かめられる。自分の設定や指示に古い書き方が残っていないかも点検できる。
signs:
  - {type: goal, text: 新しい版で何が変わったかを自分で追いたい}
  - {type: goal, text: 記事の手順が手元の版でも通じるか、自分で確かめたい}
  - {type: symptom, text: 公式の文書にある機能やコマンドが、手元では見つからない}
prerequisites: []
related: [dating-information, outdated-advice-ledger, change-timeline-2026, ask-claude-code, suspected-degradation, after-switching-models]
sources: [cc-docs-commands, cc-docs-skills, cc-docs-setup, cc-changelog, cc-docs-changelog, hc-release-notes, api-release-notes, npm-claude-code, wb-cc-best-practices-2026-10-26]
volatility: 中
sections:
  - {title: 先に整える守り（確かめる）, anchor: before-you-start}
  - {title: 変更の記録の在り処, anchor: where-records-live}
  - {title: 手順, anchor: steps}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手元の版と、変更履歴・リリースノート・公式の文書の改稿を自分で確かめ、設定に古い書き方が残っていないかも点検できる。
    - **いつ引くか**：新しい版で何が変わったかを追いたいとき。記事の手順が手元の版で通じるか確かめたいとき。公式の文書にある機能が手元で見つからないとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：変更の追い方・変更履歴の読み方・リリースノート・手元の版を確かめる
<!-- textlint-enable -->

最新を自分で確かめるとは、記事や Claude の答えに頼らず、手元の版と公式の変更の記録を自分で突き合わせることである。変更の記録は 1 か所に集まっていないので、どこに何が載るかを知っていると速い。このページは、その在り処と、記録から自分の設定への影響を洗い出す手順を示す。

## 先に整える守り（確かめる） {#before-you-start}

記録を読む前に、次の 3 つを決めておく。比べる相手が動くと、何と何を比べたのか分からなくなるためである。

- **比べる基準を控える**：手元の版、更新の通り道（latest と stable のどちらか）、前回確かめた日を、1 行のメモにする。メモがないと、「前回より後」の範囲が決まらない。
- **点検は読むだけで頼む**：Claude に点検させるときは、「ファイルは書き換えず、読むだけにする」と頼む。これはお願いであり、鍵ではない。直しは作業ツリーをきれいにしてから受け、差分で確かめる。
- **記事や Claude の答えは、版と日付を付けて扱う**：記事の日付と版の見方は <!-- link:begin dating-information#check-date-and-version -->[いつの情報かを見分ける › 日付と版の確かめ方](dating-information.md#check-date-and-version)<!-- link:end --> にある。Claude Code に機能を聞いた答えは、手元の版より新しい機能を含みうる。確かめ方は <!-- link:begin ask-claude-code#check-version -->[Claude Code 自身に聞く › 答えの版を確かめる](../cli/ask-claude-code.md#check-version)<!-- link:end --> にある。

## 変更の記録の在り処 {#where-records-live}

変更の記録は面ごとに在り処が違い、どれも他の記録の代わりにならない。1 つの記録で見つからないことは、変わっていない証拠にならない。

=== "アプリ"

    - 変更は Help Center の[リリースノート](https://support.claude.com/en/articles/12138966-release-notes)に載る。
    - リリースノートに載らず、個別の Help Center の記事や料金のページにだけ出る変更もある。プランの名前のような変更は、そちらで確かめる。

=== "Claude Code"

    - 対話の中では `/release-notes` を使う。版を選ぶ画面が開き、選んだ版の項目か、全版の項目が出る。項目は画面に出るだけで、Claude が見る会話には入らない。
    - 公式リポジトリの [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) は、版ごとの項目の一次の記録だが、日付がない。日付は文書の [changelog](https://code.claude.com/docs/en/changelog) にある。文書の日付は、npm の公開日（UTC）と 1 日ずれることがある。
    - 版の番号は連番ではない。たとえば 2.1.313 は npm に公開されていない欠番で、2.1.315 は CHANGELOG にも文書にも項目がない。項目が見つからない版を見つけても、取りこぼしとは限らない。
    - CHANGELOG に入った変更が、各機能の文書に反映されるのは遅れることがある。機能の文書に書かれていない変更は、CHANGELOG で探す。
    - 動作は WSL・Linux の CLI を基準に書いた。ほかの OS と IDE 拡張での `/release-notes` の動きは未確認である。

=== "API"

    - 変更は Claude Platform の[リリースノート](https://platform.claude.com/docs/en/release-notes/overview)に載る。モデルの追加や退役、引数の変更はここで見る。
    - 手元の Claude Code の版とは別の軸である。モデルを替えたときの見直しは <!-- link:begin after-switching-models#retirements-and-default-changes -->[新しいモデルに替えたら見直すこと › 退役と既定の変化に気づく](../models/after-switching-models.md#retirements-and-default-changes)<!-- link:end --> にある。

### 公式の文書の改稿は別の記録で探す

公式の文書そのものも、あとから書き直される。書き直しは変更履歴に載らないことがある。文書の以前の姿は、Internet Archive の保存（`https://web.archive.org/web/<日時>/<文書の URL>`）で読める。

例として、Claude Code の Best practices は 2026-10-26 から 27 にかけて大きく書き直された。2026-10-26 の保存には「コンテキストの窓が埋まるのが最大の制約」という前提の文があり、2026-10-27 以降の保存と現行の版にはない。改稿前の姿は [2026-10-26 の写し](https://web.archive.org/web/20261026194435/https://code.claude.com/docs/en/best-practices)で読める。文書を引いた記事は、記事の日付に近い保存と今の文書を見比べる。改稿の前後のどちらを読んだ記事か、見比べれば分かる。

## 手順 {#steps}

次の 6 段で進める。各段の末尾に「確かめ」を付けた。この確かめが取れてから次へ進む。

1. **手元の版と更新の通り道を控える**。`claude --version` が版を出す。`/status` の Status タブにも版が出る。`claude doctor` は、セッションを始めずにインストールの状態を読むだけで診断し、自動更新が有効かと、最後の更新の結果を見られる。通り道は `autoUpdatesChannel` で決まる。既定は latest で、新しい版をすぐ受け取る。stable が受け取る版は、latest より遅れる（<!-- fact:begin claude-code-stable-channel-delay -->ふつう 1 週間ほど前の版（大きな退行のある版を飛ばす）（2026-11-05 時点）<!-- fact:end -->）。Homebrew は cask の名前で、apt・dnf・apk はリポジトリで通り道を選ぶ。**確かめ**：版・通り道・前回確かめた日が、メモに 1 行で書けている。
2. **前回より後の記録を読む**。「変更の記録の在り処」の節に挙げた記録を、メモの版より後から読む。Claude Code は `/release-notes` か CHANGELOG、アプリは Help Center、API は Platform のリリースノートを使う。手元が stable なら、latest にだけ入った項目はまだ手元にない。**確かめ**：読む記録ごとに、読み終えた最後の版か日付が書き留めてある。
3. **自分の設定に当たる語を探す**。コマンド名・設定のキー・環境変数・モデル名・機能名を、`CLAUDE.md`、`settings.json`、スキル、フックから拾い、記録の項目に出る語と突き合わせる。手で突き合わせる代わりに、次の依頼を使える。**確かめ**：当たった項目が、「版・項目・自分の設定の場所」の一覧になっている。
4. **手元の版に入っているかを確かめ、1 つずつ試す**。項目の版が手元の版以下なら試せる。新しいセッションで 1 つずつ試し、効果が出たかを版付きで書き留める。まとめて直すと、どれが効いたか分からなくなる。外すものを 1 つずつ外して測る手順は <!-- link:begin after-switching-models#remove-one-at-a-time -->[新しいモデルに替えたら見直すこと › ハーネスの部品を一つずつ外して測る](../models/after-switching-models.md#remove-one-at-a-time)<!-- link:end --> にある。推奨や安全の既定に関わる項目は、自分の判断で採否を決める。**確かめ**：試した項目ごとに、「版・試した日・結果」の 1 行がある。
5. **設定や指示の古い書き方を点検する**。Claude Code では `/doctor prompt-audit` が、`CLAUDE.md`、スキル、そのほかの設定から、古い指示や食い違う指示を洗い出す。使うには <!-- fact:begin doctor-prompt-audit-min-version -->Claude Code 2.1.283 以上が要る（2026-11-04 時点）<!-- fact:end -->。`/doctor` 本体は、結果を先に報告し、確認を取ってから直す。公式の文書は `prompt-audit` の確認の有無を書いていないので、作業ツリーをきれいにしてから使い、差分で確かめる。API のコードに書いた指示には、別に `/claude-api prompt-audit` がある。手元の版がこの下限に満たないときや、確かめた先の文書を指定したいときは、後述の点検の依頼を使う。台帳に載った助言は <!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> の手順で探せる。**確かめ**：見つかった古い書き方が、「ファイル・行・直し方」の一覧になっている。
6. **点検した版と日付を残す**。次回の「前回」になる。**確かめ**：メモの版と日付が、今日のものに更新されている。

### 手元の版と通り道を一度に控える

段 1 の記録は、次のスクリプトで 1 回にまとめられる。

<!-- gen:begin snippet checking-for-updates/show-version -->
<!-- textlint-disable -->

??? example "雛形：手元の版と更新の通り道を控えるスクリプト"

    ```bash
    #!/usr/bin/env bash
    # 手元の Claude Code の版と、更新の通り道の設定を一度に控える。読むだけで、何も書き換えない。
    set -u

    echo "== 手元の版 =="
    claude --version

    echo
    echo "== 更新の通り道と下限の設定（user・project・local） =="
    grep -n -E '"(autoUpdatesChannel|minimumVersion)"' \
      ~/.claude/settings.json \
      .claude/settings.json \
      .claude/settings.local.json 2>/dev/null \
      || echo "設定に autoUpdatesChannel も minimumVersion もない（通り道は既定の latest）"

    echo
    echo "== 公開されている版の目印（npm が使える環境だけ） =="
    # latest と stable が今どの版を指すかを見る。Homebrew や apt で入れた人も、版の比べ方は同じ。
    npm view @anthropic-ai/claude-code dist-tags --json 2>/dev/null \
      || echo "npm が使えないので省略（公式の変更履歴で版を確かめる）"
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet checking-for-updates/show-version -->

### 記録から、自分の設定に関わる変更を洗い出させる

段 3 は、変更履歴を Claude に読ませて表にさせると速い。表の「関わる設定」は推測を含むので、出た行は自分の目で確かめる。

<!-- gen:begin snippet checking-for-updates/read-changes-since -->
<!-- textlint-disable -->

??? example "雛形：変更履歴から、自分の設定に関わる変更を洗い出させる依頼"

    ```markdown
    Claude Code の変更履歴を読んで、自分の設定に関わる変更だけを洗い出してほしい。ファイルは書き換えず、読むだけにする。

    前回確かめたときの版は【前回の版】、今の手元の版は【手元の版】だ。この範囲の項目を、公式の変更履歴（https://code.claude.com/docs/en/changelog）で読んでほしい。

    照らす相手は、このプロジェクトと私のユーザー設定にある次の 4 つだ。

    1. `CLAUDE.md` と `.claude/rules/` に書いたコマンド名・機能名
    2. `settings.json` のキーと環境変数
    3. `.claude/skills/`・サブエージェント・フックの定義
    4. 使っているモデル名と effort の指定

    結果は表で返す。列は「版」「変更の項目（原文の要約）」「関わる自分の設定（ファイル・行）」「手元の版に入っているか」「試す前に確かめること」とする。関わるかどうかは推測を含むので、確信の度合いも添える。変更履歴に項目がない版は、飛ばさず「項目なし」と書く。終わりに、1 つずつ試す順番の案を出す。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet checking-for-updates/read-changes-since -->

### 古い書き方の点検を頼む

段 5 の `/doctor prompt-audit` が使えないときや、確かめる先を指定したいときは、次の依頼を使う。名前が今もあるかを公式の文書で確かめさせ、確かめた先の列が空の行は信用しない。

<!-- gen:begin snippet checking-for-updates/audit-outdated-writing -->
<!-- textlint-disable -->

??? example "雛形：設定や指示に残った古い書き方を点検させる依頼"

    ```markdown
    自分の設定や指示に、古くなった書き方が残っていないか点検してほしい。ファイルは書き換えず、読むだけにする。

    調べるのは、このプロジェクトと私のユーザー設定にある `CLAUDE.md`、`.claude/rules/`、`.claude/skills/`、サブエージェントの定義、`settings.json` だ。見つけたいものは次の 4 つである。

    1. 今の公式の文書にない名前（コマンド・設定のキー・環境変数・機能名）
    2. 名前が変わった、または別の仕組みに置き換わったと公式の文書が書くもの
    3. 古いモデル向けの補助の記述（強調の語、細かすぎる手順の刻み方）
    4. 互いに食い違う指示

    名前が今もあるかは、公式の文書（https://code.claude.com/docs/en/commands や設定の文書）を開いて確かめてほしい。記憶で答えず、確かめられなかった名前は「未確認」と書く。

    結果は表で返す。列は「ファイル・行」「引用」「種類（1〜4）」「確かめた先（文書の題名）」「直すとしたらどうなるか」とする。直す提案は書いてよいが、実行はしない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet checking-for-updates/audit-outdated-writing -->

## 確かめ方 {#verify}

手順の全体が通ったかは、次の 3 つに答えられるかで確かめる。

1. 手元の版と通り道は何で、前回から何日あいたか。
2. 前回より後の項目のうち、自分の設定に当たったものはどれか。それぞれの版は、手元の版以下か。
3. 試した項目は、新しいセッションで効果が出たか。

変更が品質に出るかは、設定を直した前後で同じ課題を流して比べる。体感で決めない。測り方は <!-- link:begin suspected-degradation#measure -->[劣化を疑ったら測って確かめる › 版と effort を記録して、同じ課題で比べる](../models/suspected-degradation.md#measure)<!-- link:end --> にある。

## 失敗したとき {#when-it-fails}

公式の文書にある機能やコマンドが手元で見つからないときは、まず版を疑う。文書は新しい版の機能も載せるためである。原因の候補は 3 つある。

- **手元の版が、機能の入った版より古い**。stable の通り道にいると、latest にだけ入った機能はまだ届かない。新しく出たモデルが、stable の版より新しい Claude Code を要することもある。そのモデルをすぐ使うなら、latest へ移る。
- **コマンドがメニューに出ていないだけ**。`/` の候補から隠れ、全名を打つと出るコマンドがある。
- **自動更新が止まっている**。`claude doctor` で最後の更新の結果を見て、手で更新するなら `claude update` を使う。`minimumVersion` で下限を決めてあると、自動更新と `claude update` のどちらでも、下限を下回る版は入れられない。

???+ example "判断例：文書にあるコマンドが手元の候補にない"
    - **状況**：公式の Commands の文書に載るコマンドを使いたいが、`/` の候補に出ない。
    - **迷う候補**：文書が間違っていると見て探すのをやめる。または、手元の版が古いと見て更新する。
    - **選んだもの**：先に、手元の版と、そのコマンドが入った版を突き合わせる。
    - **理由**：文書は新しい版の機能も載せるので、間違いより版の差のほうが起きやすい。stable にいるなら、更新ではなく通り道の差かもしれない。版が足りているなら、全名を打ってみて、それでも出ないときに初めて文書の誤りを疑う。

見つかった差が、品質の低下に見える形で出たときは <!-- link:begin suspected-degradation -->[劣化を疑ったら測って確かめる](../models/suspected-degradation.md)<!-- link:end --> へ進む。モデルを替えた後の見直しは、<!-- link:begin after-switching-models -->[新しいモデルに替えたら見直すこと](../models/after-switching-models.md)<!-- link:end --> が受け持つ。見つけた古い助言の今の扱いは <!-- link:begin outdated-advice-ledger -->[古くなった助言の台帳](outdated-advice-ledger.md)<!-- link:end --> で引く。2026 年の変更の流れは <!-- link:begin change-timeline-2026 -->[2026 年の主な変更の年表](change-timeline-2026.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Advanced setup](https://code.claude.com/docs/en/setup)：Anthropic・英語・確認日 2026-11-05
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)：Anthropic・英語・確認日 2026-11-04
- [@anthropic-ai/claude-code (npm registry)](https://registry.npmjs.org/@anthropic-ai/claude-code)：Anthropic（npm の公開記録）・英語・確認日 2026-11-04
- [Best practices for Claude Code（改稿前。Internet Archive の写し、2026-10-26 19:44 UTC）](https://web.archive.org/web/20261026194435/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [いつの情報かを見分ける](dating-information.md)
- [古くなった助言の台帳](outdated-advice-ledger.md)
- [2026 年の主な変更の年表](change-timeline-2026.md)
- [Claude Code 自身に聞く](../cli/ask-claude-code.md)
- [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- [新しいモデルに替えたら見直すこと](../models/after-switching-models.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
