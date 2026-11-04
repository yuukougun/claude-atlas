# write.md：protecting-secrets（recipe・safety）

## 書いたファイル
- docs/safety/protecting-secrets.md（stubs から mv。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：sections（verify・when-it-fails を足した）、sources（既存の 5 件）、stage、updated
- snippets/protecting-secrets/deny-secrets-project.json・.expect.yaml（プロジェクトの deny ルール + サンドボックス）
- snippets/protecting-secrets/deny-secrets-user.json・.expect.yaml（ホームの秘密 + 環境変数の deny）
- data/sources.d/protecting-secrets.yml は書いていない（出典は既存の id だけで足りた）

## 必ず持つものの対応
- 手順：two-layers（4 段。各段に終わりの確認）
- 確かめる・縛るのページへの道：front matter の prerequisites（sandboxing）と related。本文は keep-out・two-layers・when-it-fails で permission-rules・sandboxing・what-auto-mode-stops・hook-recipes・lethal-trifecta・secrets-exposed を link で指す
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：冒頭 → keep-out → two-layers → verify → when-it-fails
- level：任せる（front matter のまま）

## メインに判断してほしいこと
- 面「app」のタブを置いていない。アプリの権限ルール・サンドボックスの有無を束で確かめられなかったので、アプリは default-safety-settings#defaults-by-surface を指すだけにした。タブが要るなら、アプリ側の根拠の追加が要る
- 雛形の `sandbox.credentials.envVars`（deny）は、公式の sandboxing 文書の例から取った。書き方・動作の確認は動作確認の担当へ
- when-it-fails に、リポジトリの設定ファイル経由で API キーが外へ出た脆弱性（修正済み）への言及を 1 行置いた。手口は書いていない。名指しの出典（Check Point）は sources に入れていない

## 提案
- なし（数値・用語集・prh への提案はない）

## 検査の結果
- 1 回目：エラー 0・警告 4（no-doubled-joshi）。直した後の 2 回目：エラー 0・警告 1（line 54 の「では…は」）。最後に 1 文を直したが、再実行はしていない（検査は 2 回までの決まりのため）

## 確かめていないこと
- 雛形の動作（Read の deny ルールがサンドボックスに合わさって grep -r などの子プロセスを止めること、`./.env.*` やサブディレクトリの .env への当たり方、`failIfUnavailable` の挙動）を実機で試していない
- 公式のサンドボックス文書（code.claude.com/docs/en/sandboxing）の先頭 10 万字までで、denyRead・credentials の書き方、パスの規則、Read の deny の合わさり、既定の読み取りを確認した。残りの約 1 万字は読んでいない
- IDE 拡張と、WSL・Linux 以外の OS は未確認と本文に書いた
- 検証の節の頼み方と期待は、観察として書いた推測であり、実際に回していない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：1 回（sandboxing 文書）
