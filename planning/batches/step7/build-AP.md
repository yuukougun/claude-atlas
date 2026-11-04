# 報告：工程7 判断事項の担当 AP

対象は `decisions-needed.md` の48件。当てたのは13件（うち一部だけのもの 4 件）。当てなかったのは35件。

## 検査の結果

- `check_page.py`：keep-replies-in-japanese・how-to-use・four-specifics・request-vs-lock・instructions-ignored・claude-md-vs-rules-skills-styles・writing-skills・glossary はエラー0・警告0
- outdated-advice-ledger は警告1（48 行目、link の目印の間の「四つの原理と比例則」。この回の直しの前からある。textlint の対象外にする側の処理が、この行では効いていないらしい。道具の件）
- `npm run lint:text`：エラー0（足した prh 規則で誤った指摘は出ない。writing-skills の「supporting files」だけ正しく指摘され、「「supporting files」」に直した）
- `check_pages.py`：エラー0。`check_catalog.py`：エラー0
- `check_all.py`：gen_site・tests-tools・tests-site が落ちる。原因は `tools/gen/config.yml` が YAML として読めない（別の担当の作業中と見る）ことと、`nav.yml` が古いこと。この回の直しによるものは、nav.yml の古さのうち four-specifics の節の題の変更分だけ（`gen_site.py` で作り直す）

## 番号ごとの扱い

1. 当てない（種類 A。作者の承認）
2. 当てない（種類 A）
3. 当てない（種類 A）
4. 当てない（種類 A）
5. 当てない（種類 D。design・common §8 の呼び名の変更）
6. 当てた：how-to-use の summary から報告の文を外し、signs の4つ目（誤りを見つけた）を外した。承認（#1）の後に戻す。要点・本文の節 report は「準備中」のまま
7. 当てない（`volatility` は直してよいキーでない。一覧に残す）
8. 当てた：claude-md-vs-rules-skills-styles の related に4件を足した
9. 当てた：instructions-ignored の related に not-what-i-meant・forgets-in-long-chats を足した
10. 当てた：instructions-ignored の signs を「作ったスキルが使われない」に直した（prh は変えない）
11. 当てた：keep-replies-in-japanese の related に request-vs-lock を足した
12. 一部：four-specifics の summary の「4点」→「4 点」、sections と本文見出しの「境界の条件」→「境界の入力」を直した。title の「4点」は直してよいキーでないので残す。catalog（`planning/catalog/prompting.yaml:88`）の節の題は合わせていない
13. 当てた：outdated-advice-ledger の summary と要点の「何ができるか」を「撤回・置換・条件付きになった助言」に直した
14. 当てた：request-vs-lock の summary を要点に合わせて直した（117字）
15. 当てた：writing-skills の aliases（.claude/skills）・related 2件・signs 1件を足した。本文の別名の行も合わせた
16. 当てない（catalog は書いてよい範囲の外）
17. 一部：用語集の骨格（`stubs/start/glossary.md`）に語を足した。own-terms にお願い・鍵、具体性の 4 点、回避策、台帳の状態、面、根拠の印、題名（準備中）、ページの段階、レベル、症状のページ、分野、章。definitions にハーネス、出力スタイル、fork、管理設定、圧縮、常駐、回り込み、ターン、ツールの合間の一言、差し戻し、補助ファイル。same-names-across-surfaces に出力スタイルと Styles。prh.yml に「ハーネス」「補助ファイル」の規則を足した。stage は stub のまま。回り込み・症状のページ・分野・章の定義は担当の案がなく、本文から私が書いたので、用語集を書くときに確かめてほしい。「公式の文書」を正規形にするかは決まりの判断なので残す。「条件つき→条件付き」の規則は、block-with-exit-2（別の担当のページ）に警告が出るので足していない
18. 当てない（`tools/checks/`。作る層）
19. 当てない（書き手の担当の仕事）
20. 当てない（種類 D）
21. 当てない（種類 D。common §9 に一言足す案は決まりの変更に当たる）
22. 当てない（`tools/gen`。作る層）
23. 当てない（`tools/gen`・data。作る層）
24. 当てない（data の文面と names の変更）
25. 当てない（種類 D）
26. 当てない（検査の変更。作る層）
27. 当てない（書き手の担当の仕事。本文のリンク）
28. 当てない（`tools/`。作る層）
29. 当てない（種類 D）
30. 当てない（種類 D）
31. 一部：(a) common §13 に「代替テキストは120字以内」を足した。(b) X の投稿を出典にする書き方は、robots.txt の `*` の Disallow との兼ね合いがあり、決まりの追加になるので足していない
32. 当てた：Hooks reference（code.claude.com/docs/en/hooks）を2回取得し、SubagentStop の節を確かめた。3か所を直した（#stop-hook の箇条、SubagentStop の段落の後ろに新しい段落、#reach の3つ目の対処）。公式は、SubagentStop フックの `last_assistant_message` は子の最後の返答の文だと書く。v2.1.271 以降で `SubagentHandback` で報告を渡すときは、報告そのものは `SubagentHandback` に当てた PreToolUse か PostToolUse の `tool_input.message` にあり、`last_assistant_message` には結びの文しか入らないと書く。版の数字は手引き §9 のとおり本文に手で書かず、「新しい版」とした。decisions に「auto モード」とあったが、公式の節には auto モードの記述がなく、本文にも書いていない。**提案（facts）**：`subagent-handback-min-version`、値 2.1.271 以降、出典 Hooks reference の SubagentStop input、used_in は keep-replies-in-japanese の `#stop-hook` と `#reach`。入れば目印で版を書ける
33. 当てない（種類 D。結果を載せるかの判断）
34. 当てない（道具と型の手引きの形の決め。(d) は決まりの判断）
35. 当てない（種類 D）
36. 当てない（雛形 `claude-md-root` は snippets で、書いてよい範囲の外。「deny ルールで止めてある」への弱めは、書く担当に渡す）
37. 当てない（種類 D）
38. 当てない（種類 D。出典の追加は data）
39. 当てない（種類 D）
40. 当てない（種類 D）
41. 当てない（種類 D。サイトの CSS）
42. 当てない（種類 D。design・guides・catalog・decisions の名前の直しを含む）
43. 当てない（種類 D・catalog・道具）
44. 当てない（種類 D・surfaces は直してよいキーでない）
45. 当てない（種類 D。routes は直してよいキーでない）
46. 当てない（catalog の `templates`。書いてよい範囲の外）
47. 一部：common §3（要点の1文目は90字ほど）・§5（「4 つ」と書く、`!!!` 内と判断例の行は「。」で終える）・§9（数字なしで読める形と used_in）・§13（120字）、card.md の同じ箇所、comparison.md（確かめ方の節を足してよい）、ledger.md（目次の sections の並びに従ってよい）に足した。決まりを変える文は入れていない
48. 当てない（`planning/batches/step7/brief-page.md` と `tools/make_packet.py` は書いてよい範囲の外）

## 一覧に残る、メインの判断が要るもの

- 作者の承認（1〜4）
- id・level・priority・routes・wave 以外で、直してよいキーでないもの：#7（volatility）、#12 の title「4点」、#44（surfaces）
- 用語集：「公式の文書」を正規形にするか（#17）、定義を骨格に置いたままにするか、用語集の本文を書く波で表に整えるか。prh の「条件つき」の規則は block-with-exit-2 の手書きの表（135 行）が先に直る必要がある
- 設計・決まり：#5、#21、#29、#30、#33、#37〜#45
- 作る層（別の担当）：#18、#22、#23、#24、#26、#28、#34、#48。いま `tools/gen/config.yml` が読めない。`nav.yml` が古い（gen_site の作り直し）
- catalog：#12 の節の題、#16、#46
- 事実：#32 の facts への提案（上）。decisions の「auto モードの 2.1.271 以降」は、公式の節に auto モードの記述がない（版だけを確かめた）
