# progress-files 執筆報告

## 書いたファイル
- docs/context/progress-files.md（stubs から移して執筆。front matter の変更：`sections` に guards・cycle・check・troubleshoot を足して並べ替え、`sources` に既存の 5 件、`stage: draft`、`updated: 2026-11-05`）
- snippets/progress-files/：progress-layout.md、claude-md-resume.md、update-progress.md、todo-state.json（各 .expect.yaml 付き）
- data/sources.d/progress-files.yml は書いていない（出典は data/sources.yml の既存の id だけで足りた）

## 必ず持つものの対応
- 手順：`#cycle`（各段に確かめを付けた 4 段）、雛形は `#files`・`#cycle`・`#protect-state`
- 確かめる・縛るのページへの道：`#guards`（handoff-documents#guard、promises-after-compaction#where-to-put）、`#protect-state`（promises-after-compaction#effects）。front matter の前提は handoff-documents、関連は promises-after-compaction
- level：任せる（front matter）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：冒頭 → `#guards` → `#files`・`#cycle` → `#check` → `#troubleshoot`。`#decided-vs-open`・`#protect-state` は手順と確かめ方の間に置いた

## メインに判断してほしいこと
- handoff-documents が `progress-files#decided-vs-open` を「聞くべきことの分け方」として指しているため、その節に聞くべきことの欄の書き方（問い・聞く相手・暫定の仮定・進めてよい範囲）を置いた
- 題名から特定の実践者のファイル名を外す方針（notes）に従い、4 ファイルの名前は aliases と雛形の例だけに置いた。本文では実践者を名指ししていない。ただし本文の表と雛形が `PLAN.md`・`TODO.md`・`KNOWLEDGE.md` を使うので、「特定の個人の構成を標準として示す」に当たらないか確認してほしい（`SPEC.md` を外し `DECISIONS.md` を足した形にした）

## 提案
- 数値・用語集・prh.yml・data への提案はなし
- 出典 qiita-minorun365-114f53 は sources に入れたが、本文では名指しせず、参考の節に出る。否定的な文脈ではない

## 検査の結果
- 書いた後：エラー 0・警告 6（助詞「に」「が」の重複）→ 6 箇所を直した後：エラー 0・警告 3
- 残した警告 3：70 行の警告は、道具が埋める link の題名（長い題名の中の「に」）を含む文で、本文側では直しきれない。179 行は出典の英題リンクを含む長文のため。250 行は link の題名が入る文の中の「が」。いずれも誤検出に近いと判断した

## 確かめていないこと
- 雛形（4 つ）の動作は実機で試していない。expect は書き手の想定
- 「JSON のほうが書き換えられにくい」「`passes` の欄だけを変えさせる」は、Anthropic の記事（2025-11-26 公開）を 1 回取得して確かめた。記事の中に `tests.json` と `feature_list.json` の食い違いがあった（本文では使っていない）。モデルの世代での再現は未確認
- 「コンテストで決定事項と質問すべき事項に分ける実践」は、調査資料（p12#118）の記述のみで、一次の実例を開いていない（根拠：弱で書いた）
- 4 ファイルで分ける実務家の運用（根拠：中）は、束の写しに基づく。個々の記事を再読していない
- `PLAN.md` の書き換えを deny ルールで止める具体的な設定の書き方は載せていない（設定の構文を確かめていないため）
- 他の OS・IDE 拡張での動作は未確認

## 使用量
- 道具の呼び出し：約 14 回（Read 3、Bash 6、Write 10 のうち報告を含む、Edit 7、WebFetch 1）。Web の取得 1 回
