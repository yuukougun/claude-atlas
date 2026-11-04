# write.md：what-to-put-in-claude-md（feature・extend）

## 書いたファイル

- `docs/extend/what-to-put-in-claude-md.md`（stubs から移して stage: draft。stubs 側は削除）
- front matter で変えたキー：`sections`（節を 4 つ足した：scenes・limits・compare・outdated。既存 3 つの anchor は変えず）、`stage`（draft）、`updated`（2026-11-05）、`sources`（空から 8 件。すべて既存の id）
- 雛形（`snippets/what-to-put-in-claude-md/`）：`short-claude-md`・`team-three-zones`・`contest-claude-md`（各 `.md` と `.expect.yaml`。kind は claude-md）
- `data/sources.d/` は作っていない（使った出典はすべて data/sources.yml にある）

## 必ず持つものの対応

- 機能の属性のバッジ（強制力・読み込みの時期など）：テンプレートが出す。本文は要点の「強制力」と `limits` の圧縮の項で `feature` の目印を使った
- `tracks`（claude-md）：front matter に既にある。本文の各所の `feature` の目印がこれを読む
- 要点（強制力・確認日と版のバッジ）：冒頭の要点の囲み
- 使いどころ（どの原因を防ぐか）：`#what-to-write`（見えていない・散らかっている・原理「見せる」を名指し）
- 最小の使い方（面のタブ）：`#what-to-write` の「最小の使い方」。面は claude-code だけなのでタブは置かない
- 雛形：`#what-to-write`（short-claude-md）、`#scenes`（team-three-zones・contest-claude-md）
- 効かない場面・落とし穴：`#limits`
- 比べる相手：`#compare`（comparison は claude-md-vs-rules-skills-styles#how-to-choose へ）
- 古くなった助言：`#outdated`（architecture-in-claude-md・hash-to-memorize を台帳へ link）
- level：front matter に「任せる」

## メインに判断してほしいこと

- 公開の約束・方針の文は入れていない。`#scenes` の「大会の規則は写さず、確認先だけを書く」は、このページの書き方の説明で、約束ではない。気になるなら見てほしい
- 雛形 `team-three-zones` の「止まって相談する」はモデルの癖に依存する（材料 A-3）。本文に「現行のモデルでの挙動は確かめていない」と書いた

## 提案

- 用語集・prh・data・front matter への提案はなし
- 数値の提案（`facts-proposal.yml`）もなし。行数の目安や回数の目安は本文に書かず、claude-md-length と when-to-add-what へ渡した

## 検査の結果

- 1 回目：エラー 2（全角と半角の間の空白）・警告 5。直した
- 2 回目：エラー 0・警告 2
  - 170 行の「にも」の重なり：直せていない（軽微。次の整理で直してよい）
  - 253 行の「に」の重なり：link の目印の間に道具が入れた題名（準備中の表示）による。本文の誤検出

## 確かめていないこと

- 公式の Best practices を 2026-11-05 に 1 回取得し、「Keep CLAUDE.md short」の 4 種類・強調（IMPORTANT）の扱い・構成の説明の扱い・`/init`・`/doctor`・`CLAUDE.local.md` を確かめた。memory のページ自体は取得していない（束の写しと data による）
- 材料 A-1 の旧い「含める／除外」の表は、現行の版にそのままの形では無いので、4 種類と移し先の表に組み直した。「除外」のうち、フォルダ別の規約・linter・コードの写しは実務家の記事の助言（根拠：中）として書いた
- 雛形は動作を確かめていない。`/context all` の流し方は公式の文書による
- 禁止を deny ルールで止める例の「効かない場面」は、permission-rules#child-processes へ渡しただけで、中身は確かめていない
- Windows・macOS・IDE 拡張での動作は未確認と書いた
- link の先の節は、束の「指せる節」にあるものだけを使った

## 使用量

- 道具の呼び出し：約 14 回（読み 5・確認 3・Web 取得 1・書き込み 8・検査 2 など）
- Web の取得：1 回（code.claude.com の best-practices）
