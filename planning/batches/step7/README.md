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

## 役割とモデル（decisions 2026-11-04「役割ごとのモデル」「事実と出典の検証」「ページの確かめ方」）

| 役割 | モデル |
| --- | --- |
| 執筆・分かりやすさの検証（書いた本人とは別）・直し | Sonnet 5.5（max effort） |
| 描画・書き方・参照の検査 | メインが道具でまとめて流す |
| メイン（判断・まとめ・commit） | Opus |

事実と出典の検証と、確かめ直しの担当は置かない。雛形の実機の確認はしない（動作を確かめていない雛形にも注記を付けて載せる）。

## 段取り

1. 道具 `tools/make_packet.py` で、ページごとの材料の束（state/packets/<id>.md）を作る（担当 PK）
2. ワークフロー（.claude/workflows/step7-prototype.js）：10ページを「執筆 → 分かりやすさの検証 → 直し」で回す。hooks がワークフローの担当に効くことは、最初の流し（2026-11-04、上限で止まった）で確かめた
3. メインが、数値の提案を data にまとめ、生成物を作り直し、検査を流す。手引き・チェックリスト・設計への提案をまとめて直す。使用量を集める
4. 作者への頼みを1回にまとめる
