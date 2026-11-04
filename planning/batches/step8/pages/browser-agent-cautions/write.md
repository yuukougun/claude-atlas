# write.md：browser-agent-cautions

## 書いたファイル
- docs/safety/browser-agent-cautions.md（stubs から mv。stage draft、updated 2026-11-05）
- data/sources.d/browser-agent-cautions.yml（新規 1 件：claude-for-chrome-blog）
- front matter で変えたキー：sections（what-happens・what-it-prevents・misconceptions を足した。reach・what-not-to-do はそのまま）、sources（cc-docs-chrome・hc-claude-in-chrome・hc-computer-use・hc-cowork-safety・claude-for-chrome-blog）、stage、updated。雛形・図はなし（目次の templates・visual とも「なし」）

## 必ず持つものの対応
- 原理（principle＝縛る）に関わる：#what-it-prevents（見出しと本文で「縛る」を名指し）
- 原因（prevents＝境界がない）に関わる：#what-it-prevents（「境界がない」を名指し）、#reach（境界のない事実）
- pitfalls：front matter が空のため、持たない
- level（整える）・要点の最初は「何が分かるか」：冒頭の要点の囲み

## メインに判断してほしいこと
- 束の材料 6.3 は The Register を出典にしていたが、theregister.com は AI の利用を断るドメイン（check_noai.py で noai）。資料にせず、同じ内容の Anthropic の公式ブログ（claude.com/blog/claude-for-chrome）を 1 回取得して数値（29 シナリオ・123 件・23.6%・11.2%・35.7%→0%）を確かめ、出典に足した。材料の写しの出典を差し替える必要がある
- 新しい出典 claude-for-chrome-blog を data/sources.d に置いた（check_noai は通過）。ほかのページが同じ URL を足していないか、反映時に確認してほしい

## 提案
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし。変わりやすい値（成熟度・版・プラン）は本文に書かず、数値の提案もなし。ブログの試験結果は研究の時点の記録として、時点・対象つきで本文に書いた

## 検査の結果
- 1 回目：エラー 0・警告 2（「三つ」の表記、助詞「に」の重なり）→ 直した後の 2 回目：エラー 0・警告 0

## 確かめていないこと
- Claude in Chrome が「自分のログイン済みのサイトに届く」点は、公式の文書では明記を確かめておらず、本文に「推論」と書いた。作業用プロファイルの案も「推論・実践例なし」と書いた
- 試験結果の対象のモデルは、ブログに名指しがなく不明。現行版の数値は未確認
- 公式の文書の「機微な情報に強く非推奨」の原文は束の写し（調査資料 02）によった。原文は開いていない
- 面ごとの違い（Desktop の Cowork と Claude Code の CLI、OS）は書いていない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：1 回（claude.com/blog/claude-for-chrome。初回の anthropic.com は転送のみ）
