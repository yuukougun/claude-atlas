# 進捗と残り作業

セッションが途切れても続きから再開できるように、工程ごとの状態と次にやることを記録する。作業の区切りごとに更新する。

## 工程（requirements §11「進め方」）

| # | 工程 | 状態 | 成果物 |
| --- | --- | --- | --- |
| 0 | 形式と運用を決める（工程1の前に入れた） | 完了（2026-11-03） | [format-and-operations.md](format-and-operations.md)（v1.1）・[decisions.md](decisions.md)・[questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)・[research/20-kyopro-atlas-retrospective.md](research/20-kyopro-atlas-retrospective.md) |
| 1 | 質問 | 完了（2026-11-03） | [decisions.md](decisions.md)・[research/21-step1-findings.md](research/21-step1-findings.md) |
| 2 | 調査の補完 | 完了（2026-11-04） | [batches/step2/](batches/step2/README.md)・research/22〜28（担当の報告）・調査資料と requirements.md への訂正と注記 |
| 3 | 設計 | 完了（2026-11-04） | [design.md](design.md)・[catalog/](catalog/README.md)・schema/site.yml・[batches/step3/](batches/step3/README.md) |
| 4 | 設計の見直し | 完了（2026-11-04） | [design-review.md](design-review.md)・設計書の第2版・[batches/step4/](batches/step4/README.md) |
| 5 | 決定の提示 | 完了（2026-11-04） | design.md §12・decisions.md「2026-11-04 工程5（決定の提示）の回答」 |
| 6 | 土台作り | 進行中（2026-11-04〜） | |
| 7 | 試作 | 未着手 | |
| 8 | 本制作 | 未着手 | |
| 9 | 仕組み作り | 未着手 | |
| 10 | 全体の検証 | 未着手 | |
| 11 | 公開と鮮度の運用 | 未着手 | |

## 工程3・4：設計と見直し（完了 2026-11-04）

- 工程3：メインが設計書の第1版を書き、担当 C0 が全候補の一覧（registry）、T1 が目次の検査の道具、C1〜C12 が23分野の目次、I1〜I7 が担当どうしの提案の統合、T2 が検査の追加を受け持った（batches/step3/）
- 工程4：4人の担当（R1 読者の立場・R2 要件と決定との照合・R3 目次の質・R4 技術と進め方）が見直し、113件（重大9件）を挙げた。メインが対応を design-review.md に決め（DR-01〜DR-20）、D1 が設計書を第2版にし、T3 が検査の道具を症状のページの振り分け先（routes）に合わせ、F1〜F7 が目次を直し、V1〜V3 が反映を確かめた（batches/step4/）
- いまの目次：357ページ（必須177・推奨144・任意36）。症状のページ34すべてに routes。検査はエラー0・警告3（比例則。理由は notes）。第一波は推奨の数え方で135ページ
- 使用量の目安（担当の完了の通知の値の合計）：工程3の統合の担当7人と T2 で約265万トークン（C0・T1・C1〜C12 の値はこの記録に残していない）。工程4の見直し4人で約167万、反映の9人（D1・T3・F1〜F7）で約404万、確かめる V1〜V3 で約107万

## 工程2：調査の補完（完了 2026-11-04）

- 7つの担当（R1〜R7）が一次資料で確かめ、報告を research/22〜28 に書いた。4つの担当（W-A〜W-D）がファイルで分けて調査資料と requirements.md に訂正と注記を付け、W-E が報告と作業の記録から否定的な文脈の実名を外した。別の2つの担当（V1・V2）が確かめ、直しの後に確かめ直した（batches/step2/）
- ユーザーに確かめたこと：作者のプラン（Ultra）、資料の直し方、否定的な文脈の実名（planning/ の全部から外す）、断られたときの頼み直しの方針の拡張、大会の規則の版（確かめられないものは未確認。作者には頼まない）、git の履歴（作り直さずに公開）。decisions.md の 2026-11-03 の工程2の節
- 使用量の目安：担当は14（R1〜R7・W-A〜W-E・V1・V2）、合わせて約680万トークン（各担当の完了の通知の値の合計。直しで再開した担当は最後の通知の値）。工程1の5つの担当は約126万トークン

## 工程1：質問

- requirements §11 で必ず聞く点（ライセンスと作者名・サイトの URL、初版の範囲と公開の目安、検証ノートを作るときの環境）と、そこから派生した点（作者が目を通す範囲、作者のプランと試せる面、GitHub のリポジトリを作る時期、調査資料の公開）は、2026-11-03 に答えを得た（decisions.md「2026-11-03 工程1（質問）の回答」）
- 調査資料の読み込み：5つの担当（サブエージェント）が全文を読み、作者に聞く点と事実の疑いを挙げた（[research/21-step1-findings.md](research/21-step1-findings.md)）。挙がった点への回答を得た（decisions.md「2026-11-03 工程1（質問）：調査資料を読んで出た点への回答」）

## 次にやること

1. 工程6a（土台作り）：1段目の担当5人（B1 サイトと CI・B2 読む層と data・B3 書き方の検査・B4 縛り・B5 手引きとチェックリスト）が並列に作る（batches/step6/README.md）。終わったら2段目（作る層・検査の層・見た目）、3段目（つなぐ：空のサイトのデプロイ、hooks の確かめ）
2. 6b data の初版、6c 骨格

済んだこと（2026-11-04）：planning/ の実名の検索（0件。batches/step6/names-N1.md）、GitHub の公開のリポジトリ yuukougun/claude-atlas の作成と push

## ユーザーにお願いしていること

- ~~制作に入る前に、/config の Dynamic workflow size を変える（decisions 2026-11-03）~~ 済み（2026-11-04。large にした）
- ~~雛形の動作確認を始める前に、`sudo apt install bubblewrap socat` で sandbox の道具を入れる（decisions 2026-11-03「危ない雛形を試す場所」）~~ 済み（2026-11-04。bubblewrap 0.6.1・socat 1.7.4.1 が入ったことを確かめた。Claude Code の `!` ではパスワードを入力できないので、普段の WSL の端末で入れてもらった）
