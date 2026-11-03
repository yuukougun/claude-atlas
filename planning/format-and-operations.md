# 形式と運用の論点（洗い出しと最初の見立て）

- 版：2026-11-03 v0。requirements.md と、手本の kyopro-atlas（`../kyopro-atlas`）のファイルから洗い出した
- kyopro-atlas の制作セッションへの質問は [questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)。回答（`research/20-kyopro-atlas-retrospective.md`）を読んだあとに、この文書を案（v1）に直す
- 決まったことは [decisions.md](decisions.md) に日付付きで記録する（この文書は案で、決定ではない）

見立ての言葉：

- **そのまま**：kyopro-atlas の形をほぼそのまま使う
- **手直し**：形は使い、claude-atlas に合わせて項目や規則を直す
- **変える**：別の形にする案がある
- **新設**：kyopro-atlas にないもの

決め方：**K** は kyopro-atlas のセッションに経緯を聞いてから決める。**U** はユーザーに決めてもらう。**設計** は設計の工程（requirements §11「進め方」の3）で決める。

---

## 1. kyopro-atlas と違う前提

形式と運用の違いは、主に次の前提の違いから来る。

| | kyopro-atlas | claude-atlas |
| --- | --- | --- |
| 内容が古くなる速さ | 年単位（アルゴリズム・定理） | 週〜月単位（機能・既定値・料金・名称）。Claude Code は2026年に約235版 |
| 事実の確かめ方 | 第三者の解説記事、コード片のコンパイルと実行 | 公式文書・CHANGELOG・リリースノート、設定や雛形を実際に動かす |
| 裏付けを集める場所 | 問題の台帳 `data/problems.yaml` | 数値ファイル・出典・古くなった助言の台帳（新設） |
| 本文に載る技術的な部品 | KaTeX の数式、C++ のコード片、動く図 | settings.json・hook・skill・subagent の定義・CLAUDE.md の例。数式はほぼない。動く図は少数 |
| 読者 | AtCoder の学習者（作者本人が中心） | 公開を前提に、いろいろな人 |
| 制作との関係 | 制作の道具は教材の題材ではない | 制作そのものが教材の教える「確かめる・縛る・握る」の実例で、後で素材にする（requirements §7） |
| claude.ai での使い方 | 解けなかった問題の解説 | 困りごとの相談（Claude についての相談を Claude にする） |
| 規模と公開 | 353ページ（のち357）を一度に作り、骨格から公開 | 約370の候補。初版は「必須」のページ（D10） |
| 進捗の仕組み | 解いた・理解した・勉強したいリスト（localStorage） | 入れない（D17） |

---

## 2. 論点の一覧

| # | 論点 | 見立て | 決め方 |
| --- | --- | --- | --- |
| F1 | フォルダ構成 | 手直し | 設計 |
| F2 | front matter と schema | 手直し | K → 設計 |
| F3 | 段階（stage）と正本（catalog の凍結） | そのまま | K → 設計 |
| F4 | 冒頭の要点と、準備中のページの公開 | 要点はそのまま、準備中の出し方は変える可能性 | K → U |
| F5 | 数値ファイルと、本文からの参照 | 新設 | K → 設計 |
| F6 | 確認日・変わりやすさ・期限切れの注意書き | 新設 | 設計 |
| F7 | 出典の記録と、AI の利用を断るサイトの確認 | 手直し | K → 設計 |
| F8 | 図 | 手直し | 設計 |
| F9 | 技術基盤（Material for MkDocs と Zensical） | 見直す | K → U |
| F10 | 生成スクリプト | 手直し（写して直す） | K → U |
| F11 | 検査スクリプト | 手直し＋新設 | 設計 |
| F12 | 設定・雛形の動作確認 | 新設（形はまねる） | U・K → 設計 |
| F13 | textlint と prh | そのまま（prh の規則は作り直す） | 設計 |
| F14 | サブエージェントへの分担 | そのまま（検証の観点を足す） | K → 設計 |
| F15 | バッチの回し方（並列の数・止め方・再開） | 変える（規模を決め直す） | U・K |
| F16 | 執筆の手引きとチェックリスト | 変える（組み方） | K → 設計 |
| F17 | 決定と進捗の記録（decisions.md・progress.md） | そのまま＋制作の記録の置き場を足す | K → U |
| F18 | CLAUDE.md | 手直し | K → 設計 |
| F19 | 制作に hooks・permissions を使うか | 新設を検討 | K → U |
| F20 | commit と push | 変える（今は push しない） | U |
| F21 | 使用量と期間の見込み | そのまま（試作で測る） | 設計 |
| F22 | claude.ai 連携 | 手直し | U・K |
| F23 | 制作者用 skill（事例の記録・鮮度の点検） | 手直し＋新設 | 設計 |
| F24 | Issue のテンプレート | 手直し | 設計 |
| F25 | 進捗チェック | 入れない | 決定済み（D17） |
| F26 | ライセンスの表記 | そのまま | U（次の工程の最初の質問） |

### 2.1 リポジトリと形式

#### F1 フォルダ構成（手直し）

- **kyopro-atlas**：`docs/<field>/<id>.md`・`docs/img/<id>/`・`overrides/assets/`（JS・CSS・同梱ライブラリ・graph.json）・`data/`（台帳）・`snippets/<id>/`・`schema/`・`tools/`・`tests/`・`claude/`・`.claude/skills/`・`planning/`（catalog・checklists・batches・research・review）・`notes/`（追跡外）（design §8.2）
- **見立て**：骨組みはそのまま使える。`data/` は台帳の代わりに数値ファイル・出典・古くなった助言の台帳を置き、`snippets/` は設定の雛形の置き場にする。静的ファイルを `overrides/assets/` に集める理由（claude.ai で `docs/` を丸ごと読ませる）は claude-atlas でも同じに当てはまる

#### F2 front matter と schema（手直し）

- **kyopro-atlas**：JSON Schema（`schema/page.schema.json`）を、`check_pages.py` の中の小さな検査器で当てる。必須は10キー。`type`・`field`・`level`・`kind` は列挙。型ごとの条件は `allOf` の if/then（interfaces §2）
- **見立て**：仕組みはそのまま使う。足すキーが十数個ある（requirements §5.2）。すべてを全ページの必須にすると、骨格づくりと検査と執筆者の負担が重くなるので、全ページ必須・型ごと（feature だけの `enforcement` など）・任意に分ける。`kind` の固定の語彙は、`principle`・`prevents`・`surfaces` などの軸に分かれる

#### F3 段階と正本（そのまま）

- **kyopro-atlas**：目次（catalog。初版 → 見直しで第2版）→ 骨格（8a）で front matter と台帳が正になり、catalog は凍結して執筆の指示にだけ使う。`stage` は stub → draft → reviewed → done。done は「一通りの作業を終え、作者が公開してよいとしたもの」で、作者がすべての記述を確かめた意味ではない（decisions 2026-10-29）
- **見立て**：二重管理を避ける理由は claude-atlas にも当てはまる。調査資料 00 §6 の「catalog を唯一の正本にする」案は採らない方向（§3 の1）。鮮度の点検で `verified` が何度も書き換わるので、正本は front matter のほうが合う。done と鮮度（確認日の期限）は別の軸として持つ

#### F4 冒頭の要点と、準備中のページの公開（要点はそのまま、準備中の出し方は変える可能性）

- **kyopro-atlas**：全ページの本文の最初に要点の囲み（何ができるか・いつ使うか・計算量・前提）。骨格の段階から stub（要点だけのページ）を「準備中」の印付きで公開し、ナビゲーションにも出した
- **見立て**：要点の囲みはそのまま使い、項目は requirements §5.3 のとおり変える。準備中のページの出し方は再検討する。初版は必須のページだけなので（D10）、約370の候補を準備中で全部出すと、逆引きの行き先の多くが準備中になる。一方で、全体の地図が早く見える利点もある

#### F5 数値ファイルと、本文からの参照（新設）

- **kyopro-atlas**：数値ファイルはない。近いのは問題の台帳 `data/problems.yaml` と、台帳から本文の問題の行を作り直す `tools/fix_problems.py`
- **見立て**：料金・上限・既定値・大会の規則と成績を1つのファイル（例：`data/facts.yml`）に集め、項目ごとに出典と確認日を持たせる（D11）。本文からの参照は、道具が本文に値を書き込む形（`gen:begin`〜`gen:end` の目印や、置き換えの目印）を勧める。調査資料が勧める mkdocs-macros は、Zensical に移りにくいうえ、claude.ai のスレッドが読むリポジトリの Markdown には値が入らない（§3 の2）

#### F6 確認日・変わりやすさ・期限切れの注意書き（新設）

- **kyopro-atlas**：`updated`（読者に見える中身を変えた日）だけ
- **見立て**：`verified`・`verified_with`・`volatility`・`tracks` を持つ（requirements §5.2・§7）。期限切れの注意書きは、ビルドのときではなく、ページに出した確認日からブラウザで日数を計算して出す案にする（§3 の5）

#### F7 出典の記録と、AI の利用を断るサイトの確認（手直し）

- **kyopro-atlas**：各ページの末尾の「参考」、手引きの付録 B（確かめたドメイン）、`tools/check_noai.py`、台帳の evidence
- **見立て**：claude-atlas の出典は公式文書が中心で、同じ URL を多くのページが使い、移転も多い（docs.anthropic.com → code.claude.com など）。出典を1か所（例：`data/sources.yml`）に持ってページからは id で参照すると、リンクの検査と確認日の更新が1か所で済む。付録 B の記録もデータにする

#### F8 図（手直し）

- **kyopro-atlas**：Mermaid（CDN から読む）・SVG（`docs/img/<id>/`）・動く図（自作の部品。priority 1 を25前後）。`render_svg.py`・`render_pages.py`・`check_svg.py` で確かめる
- **見立て**：動く図は、動かすことで分かりやすくなる数個に絞る（requirements §2）。数式（KaTeX）はほぼ要らない。描いて崩れを数える検査（`render_pages.py`）は最初から用意する（kyopro-atlas では工程11で足した）

#### F9 技術基盤（見直す）

- **kyopro-atlas**：Material for MkDocs 9.7.7＋MkDocs 1.6.1 を `uv.lock` で固定。MkDocs の hooks・macros・自作プラグインを使わず、生成は独立スクリプト。Zensical の試験ビルドを CI で並走させ、評価は 0.1.0 が出てから（design §8.1）
- **見立て**：Material の保守は 2027-05-05 まで（kyopro-atlas の調査）。Zensical 0.1.0 は kyopro-atlas の記録では 2026-11-05 の予定で、今日（2026-11-03）の2日後である。新しく始めるので、最初からどちらにするかを決め直す価値がある。requirements §2 は Material を引き継ぐとしている

### 2.2 道具

#### F10 生成スクリプト（手直し。写して直す）

- **kyopro-atlas**：`gen_site.py`（nav.yml・分野の入口・一覧・`llms.txt`・分野ごとの詳細索引・graph.json・手書きのページの生成部分）。生成物はコミットし、`--check` で鮮度を確かめる。骨格は `make_skeleton.py`
- **見立て**：AtCoder に固有の部分（問題・台帳・出題頻度・ACL）を外せば、多くが使える（§3 の3）。逆引きは `signs` の type（symptom・goal・situation）から、比較表は `enforcement` などの属性から、知識マップとロードマップは level（委任の段階）と `prerequisites` から作る。写して直すか作り直すかは、どこが絡み合っているかを聞いてから決める

#### F11 検査スクリプト（手直し＋新設）

- **kyopro-atlas**：`check_pages.py`（schema・参照・循環・レベルの逆転・リンク・書き方）・`check_svg.py`・`render_pages.py`（CI の外で手元）・`check_noai.py`・textlint・lychee（週1回）
- **見立て**：足す検査は、数値が数値ファイルを経由しているか、版に依存する記述に確認日があるか、根拠の強さの表記、出典の型と確認日、期限切れ。外す検査は、問題の行・台帳・KaTeX まわり

#### F12 設定・雛形の動作確認（新設。形はまねる）

- **kyopro-atlas**：`snippets/<id>/<name>.cpp` と `<name>.yaml`（コンパイラ・フラグ・期待・入出力）。`check_snippets.py`。CI は gcc:15.2.0 のコンテナで変わったものだけ、週1回すべて
- **見立て**：雛形のファイルと期待（例：この hook はこの操作を止める）を置き、二段で確かめる。静的な検査（JSON の形、settings の schema、skill と subagent の front matter）は CI で毎回行う。実機の確認（使い捨てのフォルダで `claude -p` を動かす）は手元だけで行い、確かめた版を記録する。実機の確認は使用量を使い、Claude Code の版で結果が変わる。作者の環境で試すかは、requirements §11 の最初の質問にもある

#### F13 textlint と prh（そのまま。prh の規則は作り直す）

- **kyopro-atlas**：preset-ja-technical-writing・prh・全角と半角の間の空白。警告は残してよい。用語の正規形の表は用語集が正で、prh.yml はそこから作る
- **見立て**：設定はそのまま使える。prh の規則は、製品名・機能名・英語とカタカナの書き分け（subagent とサブエージェントなど）を新しく決める。機能名・コマンド・ファイル名は原文のまま書き、公式の日本語訳での言い方を併記する方針（00 §6）

### 2.3 制作の運用

#### F14 サブエージェントへの分担（そのまま。検証の観点を足す）

- **kyopro-atlas**：執筆 → 検証（別の担当。事実・コード・分かりやすさ・図の4観点）→ 直し。執筆者が書いてよいのは担当のページ・snippets・図だけで、共有ファイル（用語集・prh・台帳・catalog・手引き）への変更は報告に「提案」として書き、メインがバッチの終わりに反映する。生成と commit・push はメインだけ（CLAUDE.md、design §10.2）
- **見立て**：requirements §7・§11 の「書いた本人に採点させない」と一致する。検証の観点に「出典と鮮度（数値ファイル経由・確認日・根拠の強さ・版依存の記述）」と「雛形の動作」を足す

#### F15 バッチの回し方（変える。規模を決め直す）

- **kyopro-atlas**：ワークフローの pipeline で1ページずつ「執筆 → 検証 → 直し」を回し、同時に最大20（1本16まで）。利用上限で途中で止め、ページごとの段階を `batches/b1/STATE.md` に残して再開した。ページの一覧はファイルから機械的に渡す（手で打ち直した一覧が食い違った反省）
- **見立て**：この制作環境では、ワークフロー（多数のサブエージェントをまとめて動かす仕組み）はユーザーが明示したときだけ使い、規模の目安は既定で10未満（設定で変えられる）。並列の数・止める基準・再開の手順は、試作で測ってから決める

#### F16 執筆の手引きとチェックリスト（変える。組み方）

- **kyopro-atlas**：`style-guide.md` 1本（約4.9万字）。§13〜§17 にバッチごとの決定を足し、「後の節が優先」とした。チェックリスト4本（fact・code・clarity・figure）。見本2枚に「構成をまねない」と添える
- **見立て**：決定を後ろに足す形だと、執筆者は全部を読み、食い違いを自分で解く必要がある。共通の手引きと型ごとの短い手引きに分け、決定は元の節に溶かし込み、変更の記録は別にする案。チェックリストには「出典と鮮度」「雛形」を足す

#### F17 決定と進捗の記録（そのまま＋制作の記録の置き場を足す）

- **kyopro-atlas**：`decisions.md`（ユーザーの決定と確かめた事実。新しい日付の記録が優先）、`design.md` の変更履歴、`progress.md`（工程の表・次にやること・ユーザーへのお願い）、`batches/<バッチ>/`（状態・報告・バッチの決定）
- **見立て**：分け方はそのまま使う。requirements §7 は、制作で使った CLAUDE.md・skills・hooks・分担とその結果を、後で用途別レシピや注釈付きのセッション記録の素材にするとしている。decisions と progress に混ぜると探しにくいので、素材になる出来事（うまくいかなかった指示とその直し、検証の指摘の実例など）を書き留める場所を分ける案

#### F18 CLAUDE.md（手直し）

- **kyopro-atlas**：約3KB。冒頭に claude.ai の解説役への注意、要件・決定・進捗への案内、守ること、並列で書くときの規則
- **見立て**：同じ構成でよい。教材が教える原則（推測できないことだけを書く、例外を許さない規則は hooks と deny に任せる）の実例になるように書く

#### F19 制作に hooks・permissions を使うか（新設を検討）

- **kyopro-atlas**：使っていない（`.claude/` は記録用の skill だけ）
- **見立て**：「縛る」の実例になる（例：執筆者が担当外のファイルや生成物を書けない、AI の利用を断るサイトを開けない）。ただし公開のリポジトリの `.claude/settings.json` は、読者が手元でリポジトリを開いたときや、claude.ai のスレッドがリポジトリを clone したときにも読まれる。制作のときだけ効く形（`settings.local.json` や環境変数での切り替え）にするか、例として置くだけにするかを決める

#### F20 commit と push（変える。今は push しない）

- **kyopro-atlas**：工程1〜10 は main に直接 commit・push（まとまった単位）。工程11 は Issue のグループごとのブランチ・pull request・作業ツリー（git worktree）
- **見立て**：今はユーザーの指示で、ファイルを変えたらその都度 commit し、push はしない。GitHub にリポジトリを作った後の運用（main に直接か、pull request か、作業ツリーで並行するか）と、requirements §11 の「まとまった単位で意図を持ってコミットする」との関係を決める

#### F21 使用量と期間の見込み（そのまま。試作で測る）

- **kyopro-atlas**：試作の9ページで測り、1ページあたり約35〜45万トークン、残り約340ページで約1.2〜1.5億トークン・作業時間は合計約20時間と見込んだ（batches/pilot.md）
- **見立て**：claude-atlas は一次資料の確認と雛形の実機の確認が加わるので、1ページあたりは重くなる見込み。試作で型ごとに測る

### 2.4 使い続けるための仕組み

#### F22 claude.ai 連携（手直し）

- **kyopro-atlas**：新しい Projects（claude.ai/code。スレッドがリポジトリを clone した Claude Code として動く）。プロジェクトの指示（v1）、手順 `claude/explain.md`、記録用まとめの形式 `claude/record-format.md`、CLAUDE.md の冒頭に解説役への注意。9b で実機確認した
- **見立て**：相談役の手順（逆引き → 症状ページ → 対処）、根拠のページ・節の URL と確認日、確認日の古い項目には「公式で確かめること」と添える（requirements §8）。スレッドがリポジトリの CLAUDE.md と `.claude/` を読むので、制作用の規則や hooks と干渉しないようにする。作者の claude.ai の Projects の種類を確かめる（§3 の6）

#### F23 制作者用 skill（手直し＋新設）

- **kyopro-atlas**：`/record-problem`（`disable-model-invocation: true`。`notes/<問題ID>.md` に1問1ファイル。`notes/` は git の追跡外）
- **見立て**：事例の記録（作者が出会った困りごとを1件1ファイルで `notes/` に）は同じ形にする。鮮度の点検の skill は新設する（前回確認した版以降の CHANGELOG とリリースノートの差分 → `tracks`・`aliases` と照らす → 影響のあるページの一覧。更新は人が承認する）

#### F24 Issue のテンプレート（手直し）

- **kyopro-atlas**：`page-error.yml`（各ページの「誤りを報告する」から、題名・URL・更新日を入れて開く）
- **見立て**：種類に「情報が古い」を足し、確認日と版の欄を足す（requirements §7）

#### F25 進捗チェック（入れない）

- **kyopro-atlas**：解いた・理解した・勉強したいリスト（localStorage）
- **見立て**：D17 のとおり入れない。kyopro-atlas のテンプレートと JS を写すときに、進捗の部品を外す

#### F26 ライセンスの表記（そのまま）

- **kyopro-atlas**：本文と図は CC BY 4.0（`LICENSE-docs`）、コードとそのほかは MIT（`LICENSE`）
- **見立て**：D19 の案と同じ。作者名・サイトの URL の表記とあわせて、requirements §11 の最初の質問で確かめる

---

## 3. 調査資料と要件の中で気づいた点

調査資料は AI が書いたもので、根拠が弱いのに断定している箇所や、要件・手本と食い違う箇所がある。形式と運用に関わるものを挙げる。

1. **catalog を唯一の正本にする案**（00 §6「planning/catalog は、ページの一覧と front matter の唯一の正本にし、雛形はそこから生成する」）：kyopro-atlas は骨格の後に catalog を凍結し、front matter を正にした（二重管理を避けるため。design-review T10）。手本と食い違う
2. **数値を mkdocs-macros で参照する案**（00 §6「本文からは mkdocs-macros などで参照する」）：requirements §2 の「MkDocs を import しない独立スクリプト」と、kyopro-atlas の「Zensical に移りやすくするため macros を使わない」（design §8.1）と食い違う。また claude.ai のスレッドはリポジトリの Markdown をそのまま読むので、マクロのままでは値が見えない
3. **「スクリプトの多くは AtCoder 固有なので作り直す前提」**（00 §7）：言い過ぎである。AtCoder に固有の道具（`ap.py`・`build_ledger.py`・`fix_problems.py`・`frequency.py`・`check_snippets.py`）はあるが、大きな2本で AtCoder・問題・台帳・ACL・出題頻度・コード片・KaTeX に触れる行は、`gen_site.py` が1536行中134行、`check_pages.py` が2477行中136行で、どちらも1割に満たない。`render_pages.py`・`check_svg.py`・`check_noai.py`・`textlint_targets.py`・`make_skeleton.py` はほぼ汎用である（分野の一覧などの決め打ちは直す必要がある）。写して直す選択肢がある
4. **「用語集は、MkDocs Material の略語ツールチップで本文中の語に自動で付ける」**（00 §6）：日本語の語には効かない。Python-Markdown 3.11.2 の abbr で確かめると、前後が英数字でない語にだけ当たり、「subagent を」には付くが、「subagentを」「サブエージェントを」「お願いと鍵を」には付かなかった（2026-11-03、kyopro-atlas の .venv の Python-Markdown で確認）
5. **期限切れの注意書きを「ビルド時に」出す**（requirements §7）：kyopro-atlas は生成物を決定的にして `--check` で鮮度を確かめる（生成日時を書かない。design-review T5）。ビルドした日で結果が変わる注意書きは、この方式と合わない。また、push がない間は日数が古いままになる。ページに確認日を出し、日数はブラウザで計算する案を F6 に書いた
6. **claude.ai の Projects の種類**（requirements §8「claude.ai の Projects にこのリポジトリをつなぎ」）：従来の Projects（知識に GitHub のファイルを入れる）か、新しい Projects（claude.ai/code。スレッドがリポジトリを clone する）かが書かれていない。kyopro-atlas の記録（decisions 2026-10-21）では、作者の claude.ai は新しい Projects で、従来の方式は使えなかった。調査資料 02 §1-2 は従来の Projects だけを説明している
7. **front matter の例の食い違い**（00 §6 の例）：`level: L3`・`priority: 必須`・`summary: {can, when, prereq}` の形で、requirements §3.3（level は「使う」〜「回す」の名前）・§5.2（kyopro-atlas のキーを引き継ぐ。summary は1文）と、00 自身の §7（summary は1文のまま）とも違う。requirements の形を正とする

---

## 4. このあと

1. K の論点を中心に、kyopro-atlas のセッションに経緯・理由・反省を聞く（[questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)）
2. 回答を `research/20-kyopro-atlas-retrospective.md` に保存し、この文書を案（v1）に直す
3. U の論点を、選択肢と推奨を付けてユーザーに質問する。決まったことは decisions.md に記録する
