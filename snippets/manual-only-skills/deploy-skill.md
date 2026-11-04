---
name: deploy
description: 本番環境へのデプロイ手順。人が /deploy で呼んだときだけ使う
disable-model-invocation: true
argument-hint: [staging|production]
---

# デプロイの手順

対象の環境は $ARGUMENTS である。

1. `git status` で作業ツリーが空であることを確かめる
2. `npm test` を流し、失敗したら止めて人に報告する
3. これから流すコマンドと対象の環境を人に見せ、承認を待つ
4. 人が承認したら `./scripts/deploy.sh $ARGUMENTS` を流す
