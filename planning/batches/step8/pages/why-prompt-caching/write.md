# write.md：why-prompt-caching

## 書いたファイル
- docs/basics/why-prompt-caching.md（stubs から移した。stage draft。front matter は sections 4 節の追加、sources に api-docs-prompt-caching・api-release-notes、updated 2026-11-05。stub は削除）
- docs/img/why-prompt-caching/stack.svg（積み木の図。tools・system・messages の 3 段）
- 雛形・data/sources.d は作っていない（目次の templates なし。sources は data/facts.yml が挙げる既存の id）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 見せる／prevents 合っていない）：#effects の冒頭で名指し
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解）：#what-happens／#why／#effects／#misconceptions
- 比喩付きの図（積み木）：#why
- pitfalls：front matter に値がないため持たない

## メインに判断してほしいこと
- 本文に数値を書いていない。既定の寿命・読み取りの倍率・最小の長さは facts にないため、数字なしで書いた。下の提案を入れるなら、#what-happens と #why の「数字は公式で確かめる」の所に目印を置ける
- #effects のタブ「Claude Code」から、cost の分野のページを名指しせず文章で指した（id の指定がなかったため）

## 提案
```yaml
proposals:
  - fact: {id: prompt-cache-default-ttl, title: プロンプトキャッシングの既定の寿命, value: "5 分（使うたびに延びる。1 時間の寿命も選べる）", sources: [api-docs-prompt-caching], checked: 2026-11-05, status: 確認済み}
    used_in: [why-prompt-caching#why]
  - fact: {id: prompt-cache-read-multiplier, title: キャッシュの読み取りの料金の倍率（基本の入力単価に対して）, value: "多くのモデルで 0.1 倍。モデルにより 0.05 倍・0.025 倍の例外がある。書き込みは 5 分の寿命で 1.25 倍、1 時間で 2 倍", sources: [api-docs-prompt-caching], checked: 2026-11-05, status: 確認済み}
    used_in: [why-prompt-caching#what-happens]
```
- 公式の文書（2026-11-05 に取得。後半 65,992 字は未読）で、順序（tools→system→messages）、無効にする変更の表、effort が既定以外のとき messages が外れること、既定の寿命、倍率を確かめた

## 検査の結果
- check_page.py 1 回目：エラー 0・警告 1（「十回」の表記）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- モデルを替えたときのキャッシュの扱い（モデルごとに別か）は公式で確かめていない。本文は「公式で確かめる」と書くにとどめた
- Claude Code での effort・モデルの切り替えがキャッシュに与える影響の実測はしていない（束の 05 §3-8 の記述に基づく）
- アプリのプロジェクトのキャッシュの寿命と挙動は束の 02 の写し（Help Center）のみで、原文は開いていない
- 図の見え方（SVG の描画）は目で確かめていない

## 使用量
- 道具の呼び出し 14 回ほど、Web の取得 1 回
