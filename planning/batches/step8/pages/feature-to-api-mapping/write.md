# write.md：feature-to-api-mapping（執筆）

## 書いたファイル
- `docs/api/feature-to-api-mapping.md`（stubs から mv。`docs/api/` は新規に作った）。front matter で変えたキー：`sections`（choose・combine を足した）、`sources`（既存の 13 件）、`stage`（draft）、`updated`（2026-11-05）
- `docs/img/feature-to-api-mapping/mapping.svg`（二列の対応図。実線と破線。幅 400）
- 雛形と `data/sources.d/feature-to-api-mapping.yml` は置かない（目次の templates は「なし」。新しい出典もない）

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`（「何ができるか」に「〜なら…、〜なら…」の基準を 1 文）
- 比較の表（属性は数値ファイルから道具が作る）：`#table` の `compare 面 成熟度 確認日`（手書きの対応表もこの節）
- 判断例：`#choose`（判断例 2 つ）
- 組み合わせ方（構成の目安）：`#combine`
- level を持つ：front matter `level: 任せる`（変更なし）
- 比べるのは混同されやすい組だけ：`#table`（アプリの機能と API の概念の 9 組）

## メインに判断してほしいこと
- 比例則の警告が残った。目次の備考のとおり、守りのページは足さなかった。本文では `#combine` の末尾で、定期の作業の線引きとして `tasks-and-schedules-in-the-app#what-not-to-schedule` を指した
- 図の線の実線・破線：破線は web 検索・コードの実行 ↔ server tools と、定期・長時間の作業 ↔ Managed Agents（役割の近さ）。この分け方でよいか

## 提案
```yaml
frontmatter: []
# 用語集：ZDR（ゼロデータ保持）を本文で短く定義した。用語集に ZDR がなければ追加を提案する
```

## 検査の結果
- 1 回目：エラー 0・警告 5。直した後の 2 回目：エラー 0・警告 3
- 残した警告：比例則（上記の判断）／textlint の助詞の重複（`が`、`に`）2 件。見出しの言い換えで減らせるが、意味を変えずに直せる自然な形を探すには呼び出しが要るため残した

## 確かめていないこと
- web 検索・コードの実行（アプリ）が server tools と同じ実装かは束の材料にない。表で「確かめていない」と書いた
- Claude Code の `-p` が Agent SDK に当たるという対応は目次の備考による。Agent SDK の文書が `-p` を名指すかは開いていない
- Claude Code の自動メモリが memory tool に当たる点は、役割の近さ（記録を書き溜める）としてだけ書いた。形式は確かめていない
- 「アプリがナレッジをキャッシュする」は調査資料 02 §5-2 の写し（hc-usage-limit-best-practices）による。原文は開いていない
- 一次資料は開いていない。リンク先（準備中のページ）は生成のとおり

## 使用量
- 道具の呼び出し：約 17（Read 2、Bash 7、Write 3、Edit 6）。Web の取得：0
