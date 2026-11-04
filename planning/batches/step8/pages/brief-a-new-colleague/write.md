# write.md：brief-a-new-colleague（執筆）

## 書いたファイル
- docs/prompting/brief-a-new-colleague.md（stub から移し、stage を draft、updated を 2026-11-05）
- front matter で変えたキー：sections（why・limits を追加）、sources（既存 id 5 件）、stage、updated
- snippets/brief-a-new-colleague/brief-template.{txt,expect.yaml}、role-line.{txt,expect.yaml}
- docs/img/brief-a-new-colleague/colleague-and-claude.svg（static の図）
- data/sources.d/ は作っていない（使った出典は data/sources.yml に既にある）

## 必ず持つものの対応
- どの原理に関わるか（principle＝見せる）：#why（「見せる」と明記、four-principles#show へ link）
- どの原因に関わるか（prevents＝見えていない）：#why（「見えていない」と明記、six-causes#claude-side へ link）
- pitfalls：front matter に値がないため持たない
- level（使う）：front matter。要点の最初は「何が分かるか」
- 技法の構成：Before/After は #colleague-test・#ask-for-more、何が変わるかは各節の「足したもの」、なぜ効くかは #why、効かない場面・やりすぎは #limits

## メインに判断してほしいこと
- 手元の束の notes にある「アプリの where-to-put-instructions」と「extend の CLAUDE.md のページ」は、related にも指せる節にもないので link していない。#role のタブは一般的な記述だけにした

## 提案
```yaml
frontmatter:
  - {id: brief-a-new-colleague, key: related, before: [four-specifics, give-reasons, show-examples, images-and-voice, refine-in-conversation, before-after-prompts, not-what-i-meant, six-causes, four-principles], after: [..., where-to-put-instructions], reason: "#role のタブからアプリの指示の置き場所のページへ指すため（page id は要確認）。Claude Code 側は extend の CLAUDE.md のページ"}
```
- 用語集：「システムプロンプト」は prh が「system prompt」を誤りにするので、本文の表記はそれに合わせた。用語集に定義があるなら #role の初出の link 追加を提案

## 検査の結果
- 1 回目：エラー 3（system prompt の表記）・警告 6。2 回目：エラー 0・警告 4（助詞の重複 3、算用数字 1 は直した）
- 2 回目の後、警告の残り 2 文（導入と #why の図の次の文）を書き直したが、再検査は回数の決まりで流していない

## 確かめていないこと
- 3 つの Before/After の返答が実際に改善するか（雛形・例は動作未確認）
- 公式文書の原文の再確認（束の 02 §4-1・4-5、確認日 2026-10-29 に基づく）
- アプリ・Claude Code のタブの記述は、束の材料にない一般的な説明
- SVG の描画の見え方（目視していない）
- 「実務家の一致（根拠：中）」は束の 03 Q5 P1 の要約に基づき、原文は開いていない

## 使用量
- 道具の呼び出し 約 9、Web の取得 0
