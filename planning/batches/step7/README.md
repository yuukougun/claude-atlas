# 工程7（試作）のバッチ

型ごとに1ページ以上を書き、確かめて直す（design §10.1 の7）。終わりの条件：試作のページで描画と書き方の検査が0件、型ごとの手引き・チェックリスト・見本を確定し、試作で分かった設計の直しを反映した。作者への頼みを1回にまとめる（progress.md「工程7の終わりに、作者にまとめてお願いすること」）。

- 共通の指示は [brief-page.md](brief-page.md)。見せ方の一覧は [../../shows.md](../../shows.md)
- 試作のページは、波が来るまで公開から外す（tools/gen/config.yml の held_back）

## 試作のページ（10）

| ページ | 型 | 分野 | 雛形 |
| --- | --- | --- | --- |
| instructions-ignored | symptom | symptoms | |
| request-vs-lock | concept | basics | |
| four-specifics | concept（頼み方の技法） | prompting | |
| writing-skills | feature | extend | skill・prompt |
| claude-md-vs-rules-skills-styles | comparison | extend | |
| keep-replies-in-japanese | recipe | japanese | hook・settings |
| agreement-is-not-evidence | judgment | judgment | |
| competition-rules | concept（コンテスト） | contest | |
| outdated-advice-ledger | ledger | changes | |
| how-to-use | guide | start | |

## 役割とモデル（decisions 2026-11-04「役割ごとのモデル」）

| 役割 | モデル |
| --- | --- |
| 執筆・直し・分かりやすさの検証・描画の検証 | Sonnet 5.5（max effort） |
| 事実と出典の検証・確かめ直し・メイン | Opus（このセッションのモデル） |

## 段取り

1. ワークフロー：はじめに hooks がワークフローの担当に効くかを確かめ、10ページを「執筆 → 検証（事実・分かりやすさ・描画）→ 直し → 確かめ直し」で回す
2. 並行して、雛形の実機の確認の道具（`check_templates.py --live`。design §8.7・DR-07）を担当が作る。できたら、雛形のある2ページの雛形を確かめる
3. メインが、数値の提案を data にまとめ、生成物を作り直し、検査を流す。手引き・チェックリスト・設計への提案をまとめて直す。使用量を集める
4. 作者への頼みを1回にまとめる
