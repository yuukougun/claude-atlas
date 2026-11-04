---
paths:
  - "src/api/**/*.ts"
  - "tests/api/**/*.test.ts"
---

# API の規約

- 入力は、ハンドラの先頭でスキーマを通して検証する
- エラーは `src/api/errors.ts` の `ApiError` を投げる。ハンドラの中で応答を直接組み立てない
- 公開する関数には JSDoc を付ける。理由：ドキュメントの生成が JSDoc を読むため
