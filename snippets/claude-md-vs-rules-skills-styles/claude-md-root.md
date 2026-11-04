# 開発の前提

## コマンド

- テスト：先に `docker compose up -d db` で DB を起こしてから `npm test` を流す。DB が起きていないと全件が失敗する
- 型検査：`npm run typecheck`

## 落とし穴

- `generated/` は手で直さない。`npm run codegen` で作り直す

## 止めていること

- `.env` は deny ルールで読めなくしてある。値が要る作業は、読もうとせず人に頼む
