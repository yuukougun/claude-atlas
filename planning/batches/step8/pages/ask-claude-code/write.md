# write.md：ask-claude-code（執筆）

## 書いたファイル

- `docs/cli/ask-claude-code.md`（stubs から移した。stubs の元ファイルは削除）。front matter で変えたキー：`sections`（why-newer・what-it-helps・misconceptions を足し、節の並びをページの順にした。既存の 2 つの anchor は変えていない）、`sources`（cc-docs-common-workflows・cc-docs-how-claude-code-works・cc-docs-settings-reference。どれも data/sources.yml に既にある）、`stage`（draft）、`updated`（2026-11-05）
- 雛形・図・`data/sources.d/ask-claude-code.yml` は置いていない（目次の templates・visual が「なし」。出典は既存の id だけで足りた）

## 必ず持つものの対応

- 用途「なぜそうなるか（原理・仕組み）」：`#why-newer`（答えが手元の版より新しくなる理由）
- 用途「頼み方の技法（どう頼むと何が変わり、なぜか）」：`#what-to-ask`（Before/After と、足した 3 点の理由）
- 必ず持つもの「principle（見せる）・prevents（見えていない）を本文で名指しで結び付ける」：`#what-it-helps`。`pitfalls` は空なので結び付ける項目はない
- level（使う）・要点の最初が「何が分かるか」：冒頭の囲み
- 構成の目安（要点 → 例 → なぜ → 何に効くか → 誤解 → 関連）：`#what-to-ask` → `#why-newer` → `#check-version` → `#what-it-helps` → `#misconceptions` →（関連は page-links）。確かめる節を「なぜ」の後に置いた

## メインに判断してほしいこと

- 章立て：目次の sections は 2 つだけだったが、概念型の必ず持つものを満たすため 3 節を足した。多すぎるなら `#misconceptions` を落とせる
- `/powerup` の記述は 01 の調査資料（「実演は `/powerup`」）の範囲に留めた。動作の中身は書いていない

## 提案

```yaml
frontmatter: []
```

- 用語集：「見せる」「見えていない」を本文で短く定義した（`#what-it-helps`）。用語集に定義があれば、そちらに合わせて本文を直してよい
- 本文は hooks を「フック」と書いた（prh の指摘）。signs の goal は「hooks の書き方などを」のままで、これは front matter なので直していない（`{id: ask-claude-code, key: signs, ...}` を直すなら「フック」への統一をメインが判断）

## 検査の結果

- `check_page.py` 1 回目：エラー 3（prh：hooks → フック）・警告 1（助詞「に」の連続）。直した後の 2 回目：エラー 0・警告 0

## 確かめていないこと

- 実機での動作（`!claude --version` が会話に入ること、Claude Code に聞いたときに文書の URL と必要な版を添えるか）は試していない。公式の文書の読みと束の材料による
- `autoUpdatesChannel` の stable が「少し前の版を指す」ことは research/22 #3 の写しによる。settings-reference を直接は開いていない
- 「文書を調べさせると古い書き方が混じりにくい」は推論で、本文に（推論・実践例なし）を付けた
- 「記憶に頼った答えと文書を調べた答えを URL で見分けられる」点は、運用上の勧めであって、Claude Code の仕様の確認ではない
- 他 OS・IDE 拡張の動作は扱っていない（WSL・Linux の CLI を基準）

## 使用量

- 道具の呼び出し：約 9 回。Web の取得：0 回
