# write.md：documents-in-japanese（執筆）

## 書いたファイル

- `docs/japanese/documents-in-japanese.md`（stub から移した。front matter の変更：`sections` に guard・verify・failure を足した〔既存の pdf・keigo・glossary は変えず〕／`stage` を draft に／`updated` を 2026-11-05 に）
- `snippets/documents-in-japanese/` に 3 雛形（`pdf-read-check`・`keigo-request`・`internal-terms`、各 `.md` と `.expect.yaml`）。目次の templates は「なし」だったが、手順に要るので足した
- `data/sources.d/documents-in-japanese.yml` は作っていない（下の「メインに判断してほしいこと」）

## 必ず持つものの対応

- 手順：`#pdf`（渡す前に見るもの・渡した後にさせること）・`#keigo`（渡す 4 つの情報）・`#glossary`（一覧の 3 欄）
- 確かめる・縛るのページへの道：front matter の `prerequisites`（long-context-first）と `related`（consistent-politeness・consistent-notation・skipped-later-pages・how-attachments-are-read ほか）。本文では `#guard`（long-context-first#quote-first など）・`#verify`・`#failure` から link
- level：`整える`（front matter）
- 構成の目安：要点 → 先に整える守り `#guard` → 手順 `#pdf`・`#keigo`・`#glossary` → 確かめ方 `#verify` → 失敗したとき `#failure`

## メインに判断してほしいこと

- sources が空のまま。束に出典の一覧がなく、ページの事実は束の research 材料（PDF の読み込みの範囲など）を数値なしで指すだけにした。縦書き・スキャンの PDF の読まれ方は推論で書かず、手元で確かめる手順にした。出典を足すなら、support.claude.com の Upload files to Claude を `sources` に足すか判断してほしい
- 書き出しの「敬語の段階」の説明（尊敬語・謙譲語、社外に自社の人を高めない）は一般の日本語の作法で、一次資料の出典はない

## 提案

```yaml
frontmatter: []
```

用語集・data・prh への提案はない。

## 検査の結果

- `check_page.py` を 2 回流した。エラー 0。警告 2（`no-doubled-joshi`、144 行と 182 行）。どちらも link の目印の間に道具が書いた題名（例：「…一緒に指定する」「…置き場所…」）に「に」が含まれる文で、文を短く直した後も残った。誤検出の可能性が高い。再度は流していない

## 確かめていないこと

- 縦書き・スキャンの PDF がアプリ・Claude Code・API でどう読まれるか（試していない。expect の記録は未実施）
- 3 つの雛形の動作（実際には依頼を出していない）
- アプリと Claude Code の差。本文は面のタブを使わず、面に共通の手順にした
- 警告 2 件が本当に誤検出か（上記）

## 使用量

- 道具の呼び出し：約 14 回（Read 3、Write 7、Edit 4、Bash 4 のうち移動 1・検査 2・行確認 1）。Web の取得：0
