`src/auth/session.ts` の `refreshToken()` が、期限切れの直前に呼ぶと `401 Unauthorized` を返す。直してほしい。

- 症状：`npm test -- session.test.ts` の「refresh before expiry」が落ちる。エラーは次のとおり。
  `Error: Request failed with status code 401 (at refreshToken, src/auth/session.ts:58)`
- 完了：そのテストが通り、`npm run lint` にも指摘が出ない。
- 手本：`src/auth/login.ts` の `retryWithBackoff()` の書き方に合わせる。
