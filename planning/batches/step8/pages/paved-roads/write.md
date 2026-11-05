# write.md：paved-roads（concept・team）

## 書いたファイル

- `docs/team/paved-roads.md`：stub から移し済み（中断前に mv 済み）。front matter は `sections`（6 節に増やした。既存の 3 つの anchor は変えず、what-happens・principles-and-causes・misconceptions を足した）・`stage`（draft）・`updated`（2026-11-05）・`sources`（4 件）だけ変えた
- `data/sources.d/paved-roads.yml`：新しい出典 `dora-2025-report` と、ドメイン `dora.dev`（check_noai.py で断る指定なしを確認）
- 雛形・図は置かない（目次の templates・visual が「なし」）

## 必ず持つものの対応

- どの原理・どの原因に関わるか（`principle`＝縛る・握る、`prevents`＝境界がない・縛っていない を名指す）：`#principles-and-causes`（補足で `#defaults-over-attention` と `#start-low-risk`）
- level（整える）を持つ・要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-happens` → `#defaults-over-attention`・`#start-low-risk`・`#amplifier` → `#principles-and-causes` → `#misconceptions` → 関連（テンプレート）。比喩付きの図は置いていない（理由：図にして要点が増える内容がなく、お願いと鍵の比喩は前提ページに任せた）

## メインに判断してほしいこと

- 出典 `dora-2025-report`（新規）の `dora.dev` を `data/sources.yml` のドメイン一覧へ載せるか。sources.d に `domains` を書いたが、スキーマが sources.d で受けるかは check_page が通ったので足りているはず。メインの生成で確認してほしい
- メルカリの実例（`#defaults-over-attention`）は @IT の報道に基づく肯定的な文脈。束の「補足」にある `--dangerously-skip-permissions` の禁止と作業時間の減少は、一次で確かめられないとあるので書いていない

## 提案

```yaml
frontmatter: []
```

数値の提案はなし（本文に変わりやすい値を書いていない。DORA は割合・標本の大きさを書いていない）。用語集の追加提案もなし。

## 検査の結果

- 1 回目：エラー 0・警告 9（no-doubled-joshi）。直した後の 2 回目：エラー 0・警告 1（`#principles-and-causes` の「が」の重複）。その 1 文は、その後に「利用者の手では外せない範囲は」へ直したが、再実行していない（2 回までの決まりのため）

## 確かめていないこと

- DORA 2025 の「スループットと正の関係」「不安定さが増え続けた」は、dora.dev のページでは確かめられず（ページに記述なし）、束の材料と InfoQ の記事の題名に頼った。標本の大きさと相関の設計も未確認なので、本文は数値を書かず、相関で因果は書かないとした
- メルカリの記述は束が写した @IT の要約に基づく。@IT の原文は開いていない
- 導入事例一覧の「課題を公開した企業」の記述は束の写しに基づく（企業名と数値は出していない）
- 「日本語圏の実務の記事で勧められている」（根拠：弱）は束の材料（書籍・記事）に基づき、出典 id がない
- 末尾の `#principles-and-causes` の最後の修正後の textlint

## 使用量

- 道具の呼び出し：約 17 回（Read 4・Bash 7・Write 3・Edit 7 など）。Web の取得：1 回（dora.dev）
