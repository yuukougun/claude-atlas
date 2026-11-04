---
id: pruning-extensions
title: 拡張の棚卸しと剪定
aliases: [/skill-doctor, 拡張が多すぎる, skillOverrides, 使っていないスキル]
type: recipe
field: extend
chapter: 見直し
order: 240
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: [体感を信じる]
scenes: [開発, チーム]
summary: 入れた CLAUDE.md・スキル・MCP・プラグインを定期的に見直し、使っていないものを外せる。常駐のコストを測ってから切り、共有するものは複数の人が使うものに絞る。
signs:
  - {type: symptom, text: 使っていないはずの設定が、毎回トークンを使っている}
  - {type: situation, text: 設定を作り込んで、しばらくたった}
prerequisites: [extensions-at-a-glance, always-on-costs]
related: [inspect-context, claude-md-length, skill-descriptions, plugins-and-marketplaces, vetting-extensions, insights-and-usage-review, felt-vs-measured, what-uses-up-limits#find-what-uses-it, hits-limits-quickly, share-team-settings, when-to-add-what]
tracks: [claude-md, skills, mcp, plugins]
sources: [cc-docs-skills, cc-docs-plugins-measure, cc-docs-features-overview, cc-docs-context-window, cc-docs-mcp, cc-docs-commands, cc-docs-costs]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 測る, anchor: measure}
  - {title: 切る基準, anchor: criteria}
  - {title: 切る手順, anchor: cut}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：入れた拡張を、使われた記録と常駐のコストで見直し、戻せる形で外せる。
    - **いつ引くか**：使っていないはずの設定が毎回トークンを使っているとき。設定を作り込んで、しばらくたったとき。
    - **前提**：<!-- link:begin extensions-at-a-glance -->[拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)<!-- link:end -->・<!-- link:begin always-on-costs -->[常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)<!-- link:end -->

<!-- textlint-disable -->
別名：/skill-doctor・拡張が多すぎる・skillOverrides・使っていないスキル
<!-- textlint-enable -->

拡張の棚卸しと剪定は、入れた CLAUDE.md・スキル・MCP・プラグインを定期的に見直し、使われていないものを外す手順である。拡張は足すときに考えるが、外すときには考えない。放っておくと、使わないものの名前と説明が毎回の依頼に載り続ける。

## 先に整える守り {#guards}

外す前に整えるのは、戻せることと、体感で決めないことの 2 つである。

- **戻せる形で切る**：CLAUDE.md とプロジェクトの設定を、切る前に git へ入れる。スキルは SKILL.md を消さず、設定の `skillOverrides` で隠す（設定のしかたは「切る手順」の節）。プラグインは削除せず、まず無効にする。外して困ったら、設定を 1 行戻せば元の状態へ返る形を保つ。
- **記録で決める**：「たぶん使っていない」「重い気がする」では決めない。体感は実測とずれる。何を記録で測るかは <!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end --> にある。この手順では、使われた回数の記録と、常駐の大きさの記録で決める。
- **新しく入れ直すときの確認**：外したものを後で入れ直すときは、出所と中身を <!-- link:begin vetting-extensions#guards -->[MCP・プラグイン・スキルを入れる前の確認 › 先に整える守り](../safety/vetting-extensions.md#guards)<!-- link:end --> の手順で確かめる。外すだけの棚卸しでは、この確認は要らない。

## 測る {#measure}

測るのは、拡張ごとの「常駐の大きさ」と「使われた記録」の 2 つである。手順は 3 段で、各段の終わりに確かめを付ける。

**手順 1：基準値を控える。** 新しいセッションの起動直後に `/context` を開き、内訳を控える。見方と控え方は <!-- link:begin inspect-context#baseline -->[/context で中身を見る › 起動直後の基準値](../context/inspect-context.md#baseline)<!-- link:end --> にある。確かめ：切った後に見比べられる値が、メモに残っている。

**手順 2：常駐の大きさを見る。** 拡張の種類ごとに、常駐のしかたが違う。下の表は、このページが扱う 4 つの違いである。

<!-- gen:begin compare 読み込みの時期 コンテキストのコスト -->
<!-- textlint-disable -->

| 機能 | 読み込みの時期 | コンテキストのコスト |
| --- | --- | --- |
| [CLAUDE.md](what-to-put-in-claude-md.md) | セッション開始 | 常駐 |
| [スキル（skills）](writing-skills.md) | セッション開始と使うとき | 使うまで小さい |
| [MCP](connecting-mcp.md) | セッション開始 | 使うまで小さい |
| プラグイン（plugins）（準備中） | セッション開始と使うとき | 使うまで小さい |

<!-- textlint-enable -->
<!-- gen:end compare 読み込みの時期 コンテキストのコスト -->

大きさを見る場所は種類ごとに違う。

| 種類 | 常駐の大きさを見る所 | 補足 |
| --- | --- | --- |
| CLAUDE.md | `/context` のメモリのファイルの欄 | 全文が毎回入る。行の削り方は <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end --> |
| スキル | `/skill-doctor` の報告 | 名前と説明の分が毎回入る。本文は呼ばれたときに入る |
| プラグイン | シェルで `claude plugin details <名前>` | 常駐の分の推定が出る。推定と実際はずれうる |
| MCP | `/context` の MCP ツールの欄 | プラグインの詳細には MCP の分が数えられない |

確かめ：主な拡張のうち、常駐が大きい順の上位が分かる。

**手順 3：使われた記録を見る。** 記録は 4 か所にある。

- `/skill-doctor`：スキルごとの費用と使われ方を出す。一度も呼ばれていないスキルに印を付け、どこで切るかも示す。対象は組み込みと企業管理のスキルを除いたもので、使うには <!-- fact:begin skill-doctor-min-version -->Claude Code 2.1.252 以降（2026-11-04 時点）<!-- fact:end --> が要る。対話のセッションでは `/plugin` の Stats タブが開く。
- `/plugin` の Installed タブ：使われなかった期間と回数が <!-- fact:begin plugin-not-used-recently-threshold -->14 日かつ 10 セッション（2026-11-05 時点）<!-- fact:end --> に達したプラグインが「Not used recently」の見出しに移る。`--plugin-dir` で読んだものや、組織の設定で有効にしたものには出ない。
- `/doctor`：入れたスキル・MCP サーバー・プラグインを並べ、使われなかったものの無効化を勧める。
- `/usage`：対応するプランでは、最近の使用量をスキル・サブエージェント・プラグイン・MCP サーバーの割合で出す。読み方は <!-- link:begin insights-and-usage-review#usage-breakdown -->/insights と /usage で振り返る › /usage の内訳から削るものを選ぶ（準備中）<!-- link:end --> と <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> にある。

確かめ：一覧の各行に「最後に使われた時期」か「使われた記録なし」が書けている。記録がない拡張は、記録がないと書いたまま次へ進む。

棚卸しの一覧は、下の雛形をそのまま使える。

<!-- gen:begin snippet pruning-extensions/inventory-checklist -->
<!-- textlint-disable -->

??? example "雛形：棚卸しの手順のチェックリスト"

    ```markdown
    ## 拡張の棚卸し（記録日：YYYY-MM-DD）

    ### 0. 基準値

    - [ ] 新しいセッションの起動直後に /context を開き、常駐の内訳（システムのプロンプト・ツール・MCP・メモリのファイル・スキル）を控えた
    - [ ] 控えた値：＿＿＿＿（切った後に同じ場所で見比べる）

    ### 1. 一覧（1 行に 1 つ）

    | 種類 | 名前 | 置き場所（個人／プロジェクト／プラグイン） | 常駐の大きさ | 最後に使われた時期 | 判断 |
    | --- | --- | --- | --- | --- | --- |
    | スキル |  |  |  |  | 残す／縮める／外す／保留 |
    | MCP |  |  |  |  |  |
    | プラグイン |  |  |  |  |  |
    | CLAUDE.md の節 |  |  |  |  |  |

    ### 2. 外す前の確認

    - [ ] 使われた記録は、体感ではなく /skill-doctor・/plugin・/doctor・/usage で見た
    - [ ] 呼ぶまで何も載らない設定のスキル（自動起動を禁じたもの）を、「使われていない」だけで外していない
    - [ ] 共有のリポジトリにあるものは、SKILL.md や共有の設定を直さず、自分の設定側で切った
    - [ ] 戻し方を 1 行で書いた（例：skillOverrides のエントリを消す／プラグインを有効に戻す）

    ### 3. 切った後

    - [ ] 同じ場所で /context を見て、基準値より減った
    - [ ] 数回の作業のあいだ、切ったものを呼ぼうとして困った場面がなかった
    - [ ] 判断と日付を残した（次の棚卸しで同じ議論を繰り返さない）
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet pruning-extensions/inventory-checklist -->

## 切る基準 {#criteria}

切るかどうかは、「役に立っている気がする」ではなく、使われた記録と常駐のコストの 2 つで決める。気がするだけで残した拡張は、残した理由が誰にも説明できない。

| 見えたこと | 判断 | 理由 |
| --- | --- | --- |
| 一度も呼ばれず、常駐が大きい | 先に外す | 毎回の費用だけが出ている。`/skill-doctor` も、費用の大きいものから見るよう勧める |
| 一度も呼ばれないが、`disable-model-invocation: true` で自動起動を禁じていて、呼ぶまで何も載らない | 残す | 常駐のコストがない。まれに使う手順なら、外す理由は記録からは出ない |
| 呼ばれているが、説明が長い | 縮める | 外すと使う機会を失う。説明の直し方は <!-- link:begin skill-descriptions -->[スキルの description の書き方](skill-descriptions.md)<!-- link:end --> |
| 呼ばれているが、他の人が作ったもので、説明だけ載れば足りる | 名前だけにする | `skillOverrides` の `name-only` で、SKILL.md を直さずに常駐を減らせる |
| 同じ役目の拡張が 2 つある | 一方に寄せる | 説明が重なると、常駐も増え、どちらが呼ばれるかも揺れる |
| CLAUDE.md の行で、消しても誤りが出ない | 削る | 判断は <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end --> の問いに従う |

共有するものには別の基準を足す。リポジトリに入れて全員に配るスキルやコマンドは、複数の人が使うものに絞る。使うのが 1 人なら、その人の個人の設定に置く。公式が、別のリポジトリでも使うならプラグインにする、と勧める型と同じである（根拠：中）。共有と個人の分け方は <!-- link:begin share-team-settings#shared-vs-personal -->チームで設定を共有する › 共有するものと個人に残すもの（準備中）<!-- link:end --> にある。

!!! example "判断例：共有のデプロイ用スキルが一度も呼ばれていない"
    - **状況**：リポジトリに入れたデプロイ用のスキルが、`/skill-doctor` で一度も呼ばれていない。チームで見直している。
    - **迷う候補**：使われていないので外す。まれに使う手順なので残す。
    - **選んだもの**：残す。ただし、自動起動を禁じてあるかを先に確かめる。
    - **理由**：自動起動を禁じたスキルは、呼ぶまで何も載らないので、残しても費用が増えない。禁じていないなら、説明が毎回載るので、禁じるか個人の設定へ移すかを選ぶ。

!!! example "判断例：誰か 1 人しか使わないスキルが共有に入っている"
    - **状況**：共有のリポジトリにあるスキルの使用記録を、チームの全員が自分の `/skill-doctor` で見た。呼んでいたのは 1 人だけだった。
    - **迷う候補**：共有に残す。その人の個人の設定へ移す。
    - **選んだもの**：個人の設定へ移す。
    - **理由**：共有のものは、全員のセッションで説明が載る。載る相手が増えるのに使う人が 1 人なら、費用が見合わない。複数の人が使うようになったら、共有に戻す。

## 切る手順 {#cut}

切るのは、拡張の種類ごとに戻せる手段で行う。

**手順 4：種類ごとに戻せる形で外す。**

- **スキル**：SKILL.md を直さず、`skillOverrides` で状態を変える。`/skills` の画面で、スキルを選んでスペースキーで状態を切り替え、Esc で保存する。保存先は `.claude/settings.local.json` である。状態は 4 つある。`on` は名前と説明を載せる。`name-only` は名前だけを載せる。`user-invocable-only` は Claude には隠し、`/` のメニューには残す。`off` は両方から隠す。設定にないスキルは `on` と同じに扱われる。
- **プラグイン**：削除せず、まず無効にする。プラグインの中のスキルは `skillOverrides` の対象外で、`/plugin` で管理する。
- **MCP**：使われていないサーバーは接続の設定から外す。操作は <!-- link:begin connecting-mcp -->[MCP をつなぐ](connecting-mcp.md)<!-- link:end --> にある。
- **CLAUDE.md**：削るか、条件付きの rules やスキルへ移す。やり方は <!-- link:begin claude-md-length -->[CLAUDE.md の長さと剪定](claude-md-length.md)<!-- link:end --> にある。

スキルの設定の例を下に置く。名前は例なので、自分の環境のスキルに置き換える。

<!-- gen:begin snippet pruning-extensions/skill-overrides -->
<!-- textlint-disable -->

??? example "雛形：他の人が作ったスキルを名前だけ、または非表示にする skillOverrides の設定"

    ```json
    {
      "skillOverrides": {
        "legacy-context": "name-only",
        "deploy": "off"
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet pruning-extensions/skill-overrides -->

`skillOverrides` は、スキルの名前だけに当たる。別名で呼べる組み込みのスキルには、その別名の名前では当たらない。

確かめ：切ったものと戻し方が、一覧の「判断」の列に 1 行ずつ書けている。

**手順 5：基準値と見比べる。** 新しいセッションの起動直後に `/context` を開き、手順 1 の値と比べる。確かめ：常駐の内訳が減っている。減っていなければ、切ったものが常駐の大半ではなかった。残りは <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> の順で見直す。

## 確かめ方 {#verify}

棚卸し全体が効いたかは、減ったかと、困らなかったかの 2 つで見る。

- **減った**：手順 5 の見比べで、常駐の内訳が基準値より減っている。
- **困らなかった**：切った後の数回の作業のあいだに、切ったものを呼ぼうとして失敗した場面がなかった。スキルを `off` にした場合、フルネームで呼ぶと `skillOverrides` のエラーが返るので、困った場面は気づきやすい。
- **記録が残った**：切ったもの・理由・日付・戻し方を残す。次の棚卸しで、同じ議論をやり直さずに済む。

次の棚卸しは、拡張を足した後の区切りで行う。上限に早く当たり始めたときも行う。足す段階で <!-- link:begin when-to-add-what -->[拡張を足すタイミング](when-to-add-what.md)<!-- link:end --> の基準で絞ると、棚卸しが小さく済む。

## 失敗したとき {#failure}

- **`/skill-doctor` が使えない、または報告が出ない**：必要な版を満たしているかを確かめる。機能フラグの取得を省くセッションでは使えない。リモート操作の接続からは使えず、「Skill usage reports are not available on this connection.」と返る。セッションが動いているマシンの端末で実行する。
- **外したスキルが必要になった**：`skillOverrides` のエントリを消すか `on` に戻す。プラグインなら有効に戻す。記録は残して、次の棚卸しで基準を見直す。
- **切ったのにプラグインのスキルが残っている**：プラグインのスキルは `skillOverrides` の対象ではない。`/plugin` から管理する。
- **切っても重いままで、上限に早く当たる**：常駐が主因ではない可能性がある。原因の切り分けは <!-- link:begin hits-limits-quickly#diagnosis -->[すぐ上限に当たる › 原因を安く確かめる順](../symptoms/hits-limits-quickly.md#diagnosis)<!-- link:end --> にある。
- **スキルが使われない、または余計に使われる**：外すのではなく説明を直す。直し方は <!-- link:begin skill-descriptions -->[スキルの description の書き方](skill-descriptions.md)<!-- link:end --> にある。
- **外す前に、入れる側の確認が足りなかった**：次に入れるときは <!-- link:begin plugins-and-marketplaces#before-install -->プラグインとマーケットプレイス › 入れる前の確認（準備中）<!-- link:end --> と <!-- link:begin vetting-extensions#checklist -->[MCP・プラグイン・スキルを入れる前の確認 › 全体の確かめ方](../safety/vetting-extensions.md#checklist)<!-- link:end --> を先に見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Measure plugin cost and usage](https://code.claude.com/docs/en/plugins/measure)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)

**関連**

- [/context で中身を見る](../context/inspect-context.md)
- [CLAUDE.md の長さと剪定](claude-md-length.md)
- [スキルの description の書き方](skill-descriptions.md)
- プラグインとマーケットプレイス（準備中）
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- /insights と /usage で振り返る（準備中）
- [体感と実測](../eval/felt-vs-measured.md)
- [上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)
- [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- チームで設定を共有する（準備中）
- [拡張を足すタイミング](when-to-add-what.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
