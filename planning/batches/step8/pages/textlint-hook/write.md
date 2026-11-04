# write.md：textlint-hook

## 書いたファイル
- docs/japanese/textlint-hook.md（stub から移して draft に。front matter は stage・updated・sources・sections のみ変更。sections に `verify`〔動いたかを確かめる〕を足した。stubs の元のファイルは削除）
- snippets/textlint-hook/ の 3 組：textlint-after-write.py（hook）・register-hook.json（settings）・textlintrc.json（other）と、それぞれの .expect.yaml
- sources は既にある id のみ（cc-docs-hooks・cc-docs-hooks-guide・cc-docs-best-practices・zenn-yuki-a01e472d）。data/sources.d/ は作っていない

## 必ず持つものの対応
- 手順：#post-tool-use（3 段の各段に「確かめ」を付けた）。全体の確かめ方：#verify
- 確かめる・縛るページへの道：front matter の prerequisites（align-japanese-output・block-with-exit-2）と related（hook-recipes・hooks-basics・writing-safe-hooks ほか）。本文では #rules で align-japanese-output#lock-layer、#post-tool-use で block-with-exit-2#exit-2-vs-json、#failure-and-few で writing-safe-hooks#fail-open を指す
- level：front matter の「仕組みにする」（変更なし）
- 構成の目安：要点 → 先に整える守り（#rules）→ 手順（#post-tool-use）→ 確かめ方（#verify）→ 失敗したとき（#gaps・#failure-and-few）→ #share

## メインに判断してほしいこと
- `onFailure: "block"` が入った版（公式の文書では v2.1.295 以降）を本文に書いていない。fact の id が data にないため。fact の追加を提案する（下）。入れば #failure-and-few に目印を置く
- #failure-and-few の「この辞典の制作でも、縛る規則は少なく絞る方針」は制作の方針（decisions 2026-11-03）への言及。公開の方針の文と見なすなら削る

## 提案
```yaml
proposals:
  - fact: {id: hook-on-failure-block-min-version, title: フックの onFailure "block" が使える最低の版, value: "2.1.295", sources: [cc-docs-hooks, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [textlint-hook#failure-and-few]
```
- 用語集・prh・front matter への提案はなし

## 検査の結果
- 1 回目：エラー 1（prh：本文の "hooks" を「フック」に）・警告 3（助詞「で」の重複 1・読点 4 つ以上が 2）。直した
- 2 回目：エラー 0・警告 1（助詞「で」の重複 1）。2 回目の後に、その 1 文を書き換えたが、書き換え後の検査は流していない（brief の「2 回だけ」に従った）

## 確かめていないこと
- 雛形はどれも実行していない。textlintrc.json のルール名・オプション名（`sentence-length`・`max-ten`・`no-mix-dearu-desumasu`・`prh` の `rulePaths`）は記憶と、束の Zenn の記事の要約に基づく。textlint 側の文書では確かめていない
- `--format unix` の出力の形と、`npx --no-install textlint` が各環境で textlint を見つけることは未確認
- `--fix` を先に走らせたときに Claude の次の編集が失敗するか（本文で未確認と書いた）
- FileChanged の入力の項目と、matcher がファイル名の列挙だけで任意の Markdown を拾えないこと（公式の文書の matcher の説明から言えると判断したが、FileChanged の節は読んでいない）
- クラウドのセッションに textlint が入るか。初めて開くリポジトリのフックの信頼の扱い（share-team-settings#after-trust の中身は束の要約のみ）
- 2 回目の検査の後に書き換えた 1 文（#gaps の「終わりに一括検査する」）の警告が消えたこと

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 5、Write 8 を含む）。Web の取得：1 回（code.claude.com の hooks の文書）
