# agent-loop 執筆の報告

## 書いたファイル
- `docs/basics/agent-loop.md`（stubs から移した。front matter の変更：sections を 7 節足した・stage を draft・updated を 2026-11-05・sources を 8 件。ほかのキーは変えていない）
- `snippets/agent-loop/request-with-check.md` と `.expect.yaml`（prompt。依頼の本文。合否を返すコマンド・変えないもの・止まる条件を足した After）
- `data/sources.d/agent-loop.yml` は作っていない。sources は data/sources.yml に既にある id だけを使った

## メインに判断してほしいこと
- 目次の visual 案（mermaid の輪）は、本文の mermaid のコードブロックで置いた。docs/ の既存ページに mermaid の実例がなく、描画は未確認。検証（描画）で見てほしい
- 目次の templates は「なし」だったが、Before/After の After として雛形を 1 つ足した

## 提案
- 束の指せる節に、定義済みの `harness-over-model`・`subagent-isolation` の sections がない。subagent-isolation はページ単位で指した
- 数値の提案（facts-proposal.yml）は作っていない。ツール応答の上限（束 6.3 の 25,000 tokens）は変わりやすい値なので本文に使わなかった。使うなら facts に追加が要る
- 用語集：「エージェントループ」「interleaved thinking」を本文で短く説明したが、用語集への追加は未提案（用語集を読んでいない）

## 検査の結果
- 1 回目：エラー 0・警告 11（ja-technical-writing の max-ten・arabic-kanji-numbers・no-doubled-joshi）。言い回しを直して 2 回目へ
- 2 回目：エラー 0・警告 3。80 行の読点 4 つ、129 行と 151 行の助詞の重なり。直し損ねた。検査はもう流していない

## 確かめていないこと
- mermaid 図の描画、snippet の gen 出力の見え方
- 雛形の動作（実際に Claude へ渡していない）
- ALE-Bench の数値は束の写し（論文本文は開いていない）。「約 4 時間」は束の「4 時間」に沿った
- 面ごとのタブは置かなかった（アプリでのループの見え方は材料がない）。Claude Code は WSL・Linux の CLI 基準で、他 OS は未確認
- 「根拠：中」の印の強さの妥当性。reward hacking の一文は Anthropic の研究の報告に沿うが、研究本文は読んでいない
- 「interleaved thinking」の挙動は束 6.3 の一行だけに基づく

## 使用量
- 道具の呼び出し：13 回前後。Web の取得：0 回
