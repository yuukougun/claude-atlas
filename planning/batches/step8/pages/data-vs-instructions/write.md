# write.md：data-vs-instructions（concept・basics）

## 書いたファイル
- docs/basics/data-vs-instructions.md（stubs から mv。stage を draft に、updated を 2026-11-05 に）
- docs/img/data-vs-instructions/one-context.svg（目次の図の案「頼んだ指示と読ませた文書の中の文が同じ一本の文脈に並ぶ図」）
- front matter で変えたキー：sections（5 節を追加）・sources（既存の 4 id：invicti-web-security-owasp-top-risks・simonwillison-lethal-trifecta・simonwillison-newsletter-new-prompt-injection-papers-agents・hc-cowork-safety）・stage・updated
- 雛形なし（目次の templates は「なし」）。data/sources.d は新しい出典がないので書いていない

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle: 縛る`・`prevents: 境界がない` を本文で名指す）：#effects（原理の「縛る」と原因の「境界がない」を段落で名指し）
- level 整える・要点の最初が「何が分かるか」：冒頭の要点の囲み
- `pitfalls`：front matter に pitfalls のキーがないので名指す対象なし
- 型の構成（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens → #why → #entries（面のタブ）→ #effects → #misconceptions。関連はテンプレートの page-links

## メインに判断してほしいこと
- 「境界がない」の意味を、本文では「信頼できる指示と信頼できない資料の間に、文脈の中で仕切りがない状態」と書いた。原因の定義が別にあれば直してほしい
- 「バグではなく文脈に並ぶ仕組みから来る性質として扱うのが安全」は（推論）を付けた。強すぎれば弱めてよい

## 提案
```yaml
frontmatter:
  - {id: data-vs-instructions, key: related, before: [prompt-injection-in-practice, lethal-trifecta, instructions-hidden-in-materials, before-opening-unknown-repos, vetting-extensions, browser-agent-cautions, sandboxing], after: [request-vs-lock, prompt-injection-in-practice, lethal-trifecta, instructions-hidden-in-materials, before-opening-unknown-repos, vetting-extensions, browser-agent-cautions, sandboxing], reason: "本文で request-vs-lock を指した（お願いと鍵の比喩）。request-vs-lock 側の related には既に本ページがある"}
```
- 用語集：「prompt injection」（読ませた資料に紛れた文が Claude の行動を変えること）の項を提案する。本文の導入で短く定義した

## 検査の結果
- 1 回目：エラー 0・警告 7 → 直して 2 回目：エラー 0・警告 2
- 残した警告：53 行の助詞「が」の連続（読みは自然）、69 行の文の長さ 130（論文の紹介文。割ると対象の記述が離れる）

## 確かめていないこと
- 「The Attacker Moves Second」は原論文を開かず、紹介記事（束の抜き出し）だけに基づく。対象のモデル名は未確認
- OWASP LLM01 は Invicti の解説（二次）に基づく。OWASP 本体は未確認
- 本文の「面ごとの経路」のタブは、束の記述（ファイル・Web・MCP の道具の説明・issue）と一般的な構成からの整理で、公式の面ごとの文書では確かめていない
- 判断例「受信メールの要約」は説明用の想定で、実測ではない。コネクタごとの権限の分け方は書いていない
- 描画（図の見え方）は未確認

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0 回
