# independent-review 執筆報告

## 書いたファイル
- docs/verify/independent-review.md（stub から移した。stage: draft、updated: 2026-11-05。sections に what-happens・effects・limits を足した。sources に既存の 5 件を入れた）
- snippets/independent-review/reviewer-subagent.md（目次の A-5。kind: subagent）・fresh-session-request.md（prompt）・security-review-request.md（prompt、safety: true）と、それぞれの .expect.yaml
- data/sources.d/independent-review.yml は作らない（出典はすべて data/sources.yml に既存）

## 必ず持つものの対応
- どの原理に関わるか（principle: 確かめる）：#effects で名指し
- どの原因に関わるか（prevents: 確かめていない）：#what-happens と #effects
- 落とし穴（pitfalls: 同意を根拠にする）：#effects（と #ai-approval）
- level（任せる）：front matter。要点の最初は「何が分かるか」
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #who・#hide-reasoning → #effects → #limits → page-links。技法の面は #hide-reasoning の Before/After

## メインに判断してほしいこと
- 「AI の承認を人の承認に数えない」に、claude.dev ブログの原文 1 文を引用した（出典 id claude-dev-blog-solving-code-review-anthropic）。方針の文ではなく、他者の引用として置いた
- #who の表の「責任を持つか」列は、本ページの整理（出典なし）。必要なら弱めてよい

## 提案
- なし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 2（「一つ」→「1 つ」）、直した後 エラー 0・警告 0。直した後、さらに 1 回流した（リンク文の直しの確認。計 3 回）

## 確かめていないこと
- 雛形 3 つの動作（新しいセッションでの試行はしていない）
- アプリでの新しい会話の手順の細部（一般的な内容のみ。公式で確かめていない）
- 「同じ会話では問題なしと返りやすい」「新しいセッションも迎合する」の程度（調査資料の p34#226 は版依存のため、強い断定を避けた）
- Web の取得なし。束の材料のみで書いた

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 0
