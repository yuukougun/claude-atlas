---
name: release
description: リリースの手順を実行する。バージョンを上げ、タグを付け、公開前の確認をするときに使う
disable-model-invocation: true
---

# リリースの手順

1. `git status` で作業ツリーが空であることを確かめる
2. `npm version patch` でバージョンを上げ、タグを付ける
3. 公開前の確認として、`npm pack --dry-run` の出力を人に見せる
4. 人が承認したら `npm publish` を流す
