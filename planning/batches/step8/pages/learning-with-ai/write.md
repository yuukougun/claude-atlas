# write.md：learning-with-ai（執筆）

## 書いたファイル

- `docs/judgment/learning-with-ai.md`（stub から移した。stage: draft）。front matter で変えたキー：`sections`（`why`・`what-you-keep`・`how-to-check` の 3 節を足した。既存 5 節の anchor は不変）・`sources`（8 件。すべて既存の id）・`stage`・`updated`
- `snippets/learning-with-ai/quiz-after-generate.md`（と `.expect.yaml`）、`summarize-solutions.md`（同）、`hints-only.md`（同。目次の案に足した 3 つめ）
- `data/sources.d/learning-with-ai.yml`：新しい出典がないので作っていない

## 必ず持つものの対応

- 判断例（状況・迷う候補・選んだもの・理由の 4 行）：`learning-steps` の末尾（`!!! example "判断例：明後日の長期コンテストまでに、焼きなましを使えるようにする"`）
- level：front matter の `level: 整える`（変更なし）
- 構成の目安（要点 → 何が起きるか → なぜ → 判断例 → 握るもの → 確かめ方）：`faster-but-shallower`・`patterns`（何が起きるか。根拠の印と n・モデルを付けた）→ `why`（なぜ）→ `learning-steps`（判断例を含む）→ `hints-not-answers`・`summaries-of-solutions` → `what-you-keep`（握るもの）→ `how-to-check`（確かめ方）

## メインに判断してほしいこと

- 競技の上位解法の読み方そのものは kyopro-atlas を指す決め（カード §8）だが、URL・ページ名が束になく、リンクを置いていない。置くなら `summaries-of-solutions` の末尾に 1 文を足す
- 研究の割合・件数は、カード §7 の「研究の結果は固定の記録」に従い、研究名・年・対象を添えて本文に手で書いた（facts への提案はしていない）。この解釈でよいか
- 判断例の「30 分ほど」は、この辞典の根拠のない目安である。残すか、「少しの時間」に弱めるか

## 提案

```yaml
frontmatter:
  - {id: learning-with-ai, key: summary, before: "AI に書かせると速く進む一方で理解が残りにくいことと、…", after: "（直さなくてよい。ただし本文は『速さの得は確かめられていない』と書くので、『速く進む』を『進んでいるように感じる』などに弱める案がある）", reason: "Anthropic の研究で完了時間の差は有意でない（束 6.1・6.6）。題名・summary の『速く進む』と本文の言い方に温度差がある"}
```

用語集への提案：なし（用語集を読んでいない。`認知負債`・`技能形成` が語になっているかは未確認）。

## 検査の結果

- `check_page.py learning-with-ai`：1 回目 エラー 0・警告 6、直した後 エラー 0・警告 1
- 残した警告 1：要点の「いつ引くか」の `no-doubled-joshi`（助詞「と」）。signs の言い回し（AI と一緒だと分かった気になる）を保ったため

## 確かめていないこと

- 数値と研究の記述はすべて束（調査資料の写し）によった。一次資料は開いていない。「中央値 3 対 1」は未確認と束にあるので書かず、「多く遭遇した」だけを書いた
- 「素の GPT-4 の群」「約 1,000 人・48%・17%・自己評価が楽観的」は束の research/24 による。自己評価は本文の節が出典（束 §3 の 8）
- CS1 の 917 人の研究（arxiv-2607-05068）、Kestin、Brender は、題名と束の要約だけに頼った。発表年（Kestin 2025）は出典 id から推した
- 雛形 3 つは動作を確かめていない。expect は観察として書いた
- Learning 出力スタイルの `TODO(human)` の挙動は、束の調査資料（公式の文書を引いたもの）によった。公式の文書は開いていない
- アプリのタブは、会話の最初に頼む一般的な説明にとどめた。アプリ固有の機能（プロジェクトの指示など）は確かめていない
- Claude Code は WSL・Linux の CLI を基準にした。ほかの OS・IDE 拡張は確かめていない

## 使用量

- 道具の呼び出し：Read 2、Bash 5（mv と確認 1、出典 id の確認 1、雛形 1、検査 2 のうち書き換え 1 を含む）、Write 2。Web の取得：0
