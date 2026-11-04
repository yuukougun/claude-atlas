# 報告：執筆（four-specifics）

- 手引きの版：共通 2026-11-04 第1版・型（concept）2026-11-04 第1版
- 書くことのない見出し（範囲を越えたこと・止められた操作）は置かない（brief-page §5）

## 1. 書いたファイル

- `docs/prompting/four-specifics.md`：stubs から mv。front matter で変えたのは sections（5 → 10 節。既存 5 節の title・anchor は不変）・stage（stub → draft）・sources（`[]` → cc-docs-best-practices・api-docs-prompting-best-practices・arxiv-2403-08937）。updated は stub と同じ 2026-11-04 のまま
- `docs/img/four-specifics/four-points.svg`：静的な図 1 枚（4 点と、書かないと推測で埋まる所。catalog の visual の案どおり）
- `snippets/four-specifics/dev.txt`・`writing.txt`・`data-analysis.txt` と各 `.expect.yaml`：prompt の雛形 3 つ（catalog の templates は「なし」。front matter の scenes の 3 場面に合わせて足した）
- 作らなかったもの：`data/sources.d/four-specifics.yml`（3 出典とも data/sources.yml にある）、`facts-proposal.yml`（数値の提案なし）

## 5. メインに判断してほしいこと

1. Before/After の元：catalog の notes は「Best practices の Instead of / Try から取る」、共通 §11 は「例をそのまま使わない」。公式の例（login bug・calendar widget）は使わず、同じ形（曖昧な 1 行 → 4 点）の別の例（カートの合計）を作った。この扱いでよいか
2. 研究の数値（333 件・20.77%・15.27%）を本文に手で書いた。固定の研究結果で変わりやすい値ではないと判断したが、§9 の「割合」に当たるなら facts に足して目印にする。根拠の印は（根拠：中・類推）、モデル名（CodeGen・PanGu-Coder・Codex）と公表年（2024）と「Claude の結果ではない」を添えた
3. 「4 点」の数え方：公式の 3 点（ファイル・症状・直った状態）に、表の例にある倣うパターンの指定を足して、この教材が 4 点にまとめた、と本文に書いた。Analytics Vidhya の整理も Anthropic の 40 万セッションの研究も引いていない（notes の注意どおり。長さとの対比も書いていない）
4. 文章・データ分析への当てはめは（類推）、「ずれ方 → 欠けた点」の表は（推論・実践例なし）と書いた。必須ページの中心にはしていないが、強さの書き方でよいか
5. 用語集の初出リンクは付けていない。用語集の本文と anchor がまだなく、フック・deny ルール・プロンプトを指せない

## 6. 提案

```yaml
frontmatter:
  - {id: four-specifics, key: title, before: 具体性の4点（対象・状況・完了・手本）, after: 具体性の 4 点（対象・状況・完了・手本）, reason: "共通 §5：半角数字と全角文字の間に空白を入れる。本文は「4 点」と書いた。任意（題名はナビゲーションと他ページの link の表示に出る）"}
  - {id: four-specifics, key: summary, before: 依頼に対象・状況・完了の形・倣う手本の4点を書くと、Claude が推測で埋める所が減り、意図とのずれが減る。欠けている点が、次に書き足すものになる。, after: 依頼に対象・状況・完了の形・倣う手本の 4 点を書くと、Claude が推測で埋める所が減り、意図とのずれが減る。欠けている点が、次に書き足すものになる。, reason: "同上"}
```

- 用語集：語「具体性の 4 点」。定義「依頼に書く対象・状況・完了の形・倣う手本の 4 点。公式の Best practices の助言（ファイルの名指し・症状・直った状態の先出し・倣うパターンの指定）を、この教材が 4 つにまとめた呼び名」。anchor 案は本ページ（four-specifics）
- 道具（gen の link の目印）：道具が差し込む相手の題名が、書き方の検査の警告を出す。six-causes「失敗の二つの軸と診断の入口」・four-principles「四つの原理と比例則…」は漢数字（arabic-kanji-numbers）、show-examples#overfit「例にだけ合う出力に気をつける」は助詞の重複（no-doubled-joshi）。リンクを外す・別の節へ向ける・文を作り替える形で避けた。目印の間を検査から外すか、題名を直すかを決めたい
- 手引き（common §12 か型の手引き）：prompt の雛形の expect.yaml の形。道具が読むのは `title`・`features`・`safety` だけで、`title` は折りたたみの題「雛形：{title}」になるので「雛形」を含めない。この試作では `title`・`kind: prompt`・`place`・`expect`（観察する行の一覧）を書いた。形を決めるなら手引きに書く
- 手引き（brief-page §2）：読むのは 3 ファイルとあるが、書式（目印の見え方・expect.yaml・タブ・SVG の寸法・textlint の閾値）を確かめるのに約 20 回の追加の呼び出しが要った。束か手引きに「書き方の早見」があると、1 ページの使用量が減る

## 7. 検査の結果

- `gen_site.py --page four-specifics`：目印を埋めた（最後の実行は変更 0）
- `check_pages.py --page four-specifics`：エラー 0・警告 0
- `check_templates.py --page four-specifics`：エラー 0・警告 0
- `check_svg.py --page four-specifics`：エラー 0・警告 0（図 1 枚）
- `npx textlint docs/prompting/four-specifics.md` と `npm run lint:text` の自分のページ分：指摘 0。途中に出た警告（算用数字・助詞の重複・読点の数）と prh の hook → フックは直した。残した警告はない
- 図は headless Chrome で幅 400（ライト）と幅 328（暗い背景）に描いて目視した。`render_pages.py` は流していない

## 8. 確かめていないこと

- Prompting best practices（API 文書）は開いていない。束 6.1 の記述（基本原則に「文脈のない新人として扱う」「例を示す」がある）に基づく 1 文だけを書いた
- Tambon ほかの論文は、arXiv の HTML の前 10 万字（全体は約 16 万字）で、333 件・類型の割合・モデル名を確かめた。妥当性への脅威の節は読んでいない。モデルの世代は本文から確かめられず、「旧世代」とは書いていない
- アプリと API のタブ（添付・貼り付け・`messages` に入れる）は公式文書で確かめていない。Claude Code のタブ（`@`・スクリーンショット・パイプ）は Best practices で確かめた
- 雛形 3 つは動かしていない（道具が「動作を確かめていない雛形」と書く）。expect.yaml の `expect` は未検証の期待
- WSL・Linux 以外の OS と IDE の拡張は未確認。幅 390 のページ全体の描画・ダーク・mkdocs のビルドはメインが流す
- Best practices は 2026-10-27 ごろに改稿されている。本文は 2026-11-04 に読んだ版に基づく

## 9. 使用量

- 道具の呼び出し：約 75 回（Bash 約 50・Read 9・Edit 10・Write 4・WebFetch 2・ToolSearch 1）。Web の取得は 2 回（Best practices・Tambon ほか）。所要は約 35 分。トークンは不明
