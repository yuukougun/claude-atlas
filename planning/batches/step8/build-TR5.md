# TR5：バッチ5の終わりの扱い

## 直したページ（6ページ・7件）
- checking-citations：「引用が原文にない」「出典が主張を支えていない」の2形に（推論・実践例なし）を付けた（2件）
- path-scoped-rules：#outdated の `@import` の説明に（根拠：弱。公式の文書では未確認）
- explore-a-codebase：「新しいセッションで範囲を狭めてやり直す」に（推論・実践例なし）
- skill-descriptions：related に skills-in-the-app・hook-vs-skill・instructions-ignored を追加
- writing-safe-hooks：related に permission-rules を追加
- check_page：エラー0（checking-citations は既存の警告3、ほかは警告0）。各ページ1回

## backlog に足した件数
約 35 件（数値の提案 10 ページ分、用語集 3 語、道具・data の形 7、出典 2、調べる担当 10、本文の足し先 2）。

## batch5-decisions.md
13 行。

## 4（spec-first の雛形の重なり）
重なりなし。spec-first は let-claude-ask/interview-feature を `gen:begin snippet` で取り込んでいるだけで、同じ雛形を自分では置いていない（snippets/spec-first/ の3つは spec-outline・mock-request・fresh-session-start で別物）。外すものはなく、変更なし。

## 5（メインの直しの確かめ）結論：(a)(b) は問題なし。(c) に取り残しあり
| 重さ | 場所 | 問題 | 直し方 |
| --- | --- | --- | --- |
| 直す | planning/checklists/common.md:51-52 | 「reviewed にした検証役が stage を reviewed にし、同時に verified と verified_with を書く」「verified は事実・出典・鮮度の検証役が…」のまま。keys.yml（verified は reviewed でも任意）と decisions 2026-11-05「段階 reviewed の付け方」に食い違う | 「reviewed にするのは書いた担当とは別の担当。verified は出典を読み直したときだけ書く」に置き換える |
| 直したほうがよい | planning/checklists/clarity.md:8、planning/guides/README.md:15-18、planning/guides/common.md:250、planning/checklists/common.md:49 | 「検証役」の言い回しが残る。事実の検証の担当は置かない方針（decisions 2026-11-04）と合わない。guides/README の表の検証役は役割の名として残してよいかも要判断 | 方針上なくなった役（事実の検証役）の言い回しだけ置き換える |
| 軽い | planning/design-review.md:95,111・format-and-operations.md:122-123 | 旧い決定前の文書（凍結の可能性） | 凍結なら直さない |
| 確認済み | (a) schema/keys.yml・tests/tools/test_lib_schema.py | verified・verified_with の required を外し、forbidden（stub・draft）は残した。テストは DELETE で空の集合に。tools/lib/model.py の expiry は verified が None でも動く。design §3.3 の218行・§10.2 とも合う | なし |
| 確認済み | (b) tools/checks/template_keys.yml | statusLine は settings の最上位のキー。docs/cli/usage-context-statusline.md が使っている。公式の確認はメインの記録（再確認はしていない） | なし |

## 量
Web の取得 0 回。道具の呼び出し 約 16 回。

## 備考
- 書き込みを止められたものはなし。
- batch5-decisions.md の「推す案」は先頭に書いた。
