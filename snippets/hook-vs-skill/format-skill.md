---
name: format-after-edit
description: ソースファイルを編集するときに使う。編集のあとに prettier で整形する手順を書いている
---

# 編集のあとの整形

1. ソースファイルを編集したら、そのファイルに `npx prettier --write <ファイル>` を流す
2. `.prettierignore` に載っているファイルと、生成物（`generated/` の下）には流さない
3. 整形で差分が増えたときは、増えた差分も含めて、変更の内容を確かめる
