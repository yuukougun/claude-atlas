# write.md：skipped-later-pages（執筆）

## 書いたファイル
- docs/symptoms/skipped-later-pages.md（stubs から mv。stage: draft、updated: 2026-11-05）
- snippets/skipped-later-pages/quote-with-pages.txt と quote-with-pages.expect.yaml
- front matter で変えたキー：`sections`（forms・routes-to-fixes・lookalikes・example・prevention を足した。diagnosis の anchor は維持）、`sources`（[hc-upload-files, arxiv-2307-03172, api-docs-reduce-hallucinations]。すべて既存の id）、`stage`、`updated`。data/sources.d/skipped-later-pages.yml は、新しい出典がないので書いていない

## 必ず持つものの対応
- 冒頭の要点：冒頭の囲み（abstract）
- 診断のチェックリスト（六つの原因を安く確かめられる順）：`diagnosis`（見えていない 2 項目 → 散らかっている 2 項目。prevents の並びに合わせた）
- 人の側の落とし穴：持たない。front matter の `pitfalls` が空で、この症状に当たる落とし穴が束の材料にないため
- 原因ごとの振り分け先（routes）：`routes-to-fixes`（`gen:begin routes` の目印）
- よくある形（読者の言葉）：`forms`
- 判断例：`example`
- 予防（仕組みに移す）：`prevention`

## メインに判断してほしいこと
- 「安く確かめられる順」は prevents の並び（見えていない → 散らかっている）に従った。site.yml の並びとの照合はしていない（束にない）。

## 提案
読み込みの範囲の数値（PDF の図まで読まれるページの上限・文字だけが読まれるページの上限・拒否される上限）は data/facts.yml の facts に id がなく、本文には書かなかった（文で「一定のページ」と言い、値は how-attachments-are-read#pdf-and-others を指す）。how-attachments-are-read 側で fact を作るなら、このページは本文を直さずに目印へ差し替えられる。

```yaml
proposals:
  - fact: {id: pdf-visual-page-limit, title: PDF で図表まで読まれるページ数の上限（アプリ）, value: 未確定（束の材料 05 §2-5 では「100ページまで」）, sources: [hc-upload-files], checked: 2026-11-05, status: 要確認}
    used_in: [skipped-later-pages#diagnosis]
  - fact: {id: pdf-text-only-page-limit, title: PDF が文字だけで読まれるページ数の上限（これを超えると拒否）, value: 未確定（同「1000ページ」）, sources: [hc-upload-files], checked: 2026-11-05, status: 要確認}
    used_in: [skipped-later-pages#diagnosis]
```

## 検査の結果
- 1 回目：エラー 2・警告 3。エラーは related の summary-overstates-source がまだ存在しない id（並行の担当が stubs から docs へ移す途中で、2 回目の時点で解消）。警告は「一つ」の表記・長い 1 文・助詞「に」の重複
- 2 回目（直した後）：エラー 0・警告 1。残した警告は line 77 の「に」の重複で、生成された link の題名（「資料を先、質問を最後に置く」）が原因とみられ、本文では直せない

## 確かめていないこと
- 読み込みの範囲の具体的な値、API で渡すときの違い、スキャン PDF の扱いは、束の材料にある範囲を超えて確かめていない（本文は値を書かず、持ち主のページを指す）
- 雛形の動作（実際に後半の図に対して「読めていない」と返るか）は未確認
- site.yml の原因の並びとの照合、Web の取得はしていない

## 使用量
- 道具の呼び出し：約 14 回（Read 2・Bash 7・Write 4 ほか）。Web の取得：0
