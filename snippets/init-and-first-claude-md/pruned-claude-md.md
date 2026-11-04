# 開発の約束

## コマンド

- テスト：`npm test`（単体のファイルだけなら `npm test -- path/to/file.test.ts`）
- 型検査：`npm run typecheck`。テストの前に通す

## 落とし穴

- `src/generated/` は `npm run codegen` が作る。手で直さない（次の生成で消える）
- 結合テストは `.env.test` がないと黙って成功扱いになる。新しい環境ではまず `.env.test` の有無を確かめる

## 決まり

- 公開 API の変更は、先に `docs/api-changes.md` へ理由を書く。理由は、後から経緯を追えるようにするため
