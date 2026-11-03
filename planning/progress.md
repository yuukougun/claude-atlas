# 進捗と残り作業

セッションが途切れても続きから再開できるように、工程ごとの状態と次にやることを記録する。作業の区切りごとに更新する。

## 工程（requirements §11「進め方」）

| # | 工程 | 状態 | 成果物 |
| --- | --- | --- | --- |
| 0 | 形式と運用を決める（工程1の前に入れた） | 完了（2026-11-03） | [format-and-operations.md](format-and-operations.md)（v1.1）・[decisions.md](decisions.md)・[questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)・[research/20-kyopro-atlas-retrospective.md](research/20-kyopro-atlas-retrospective.md) |
| 1 | 質問 | 完了（2026-11-03） | [decisions.md](decisions.md)・[research/21-step1-findings.md](research/21-step1-findings.md) |
| 2 | 調査の補完 | 完了（2026-11-04） | [batches/step2/](batches/step2/README.md)・research/22〜28（担当の報告）・調査資料と requirements.md への訂正と注記 |
| 3 | 設計 | 未着手 | |
| 4 | 設計の見直し | 未着手 | |
| 5 | 決定の提示 | 未着手 | |
| 6 | 土台作り | 未着手 | |
| 7 | 試作 | 未着手 | |
| 8 | 本制作 | 未着手 | |
| 9 | 仕組み作り | 未着手 | |
| 10 | 全体の検証 | 未着手 | |
| 11 | 公開と鮮度の運用 | 未着手 | |

## 工程2：調査の補完（完了 2026-11-04）

- 7つの担当（R1〜R7）が一次資料で確かめ、報告を research/22〜28 に書いた。4つの担当（W-A〜W-D）がファイルで分けて調査資料と requirements.md に訂正と注記を付け、W-E が報告と作業の記録から否定的な文脈の実名を外した。別の2つの担当（V1・V2）が確かめ、直しの後に確かめ直した（batches/step2/）
- ユーザーに確かめたこと：作者のプラン（Ultra）、資料の直し方、否定的な文脈の実名（planning/ の全部から外す）、断られたときの頼み直しの方針の拡張、大会の規則の版（確かめられないものは未確認。作者には頼まない）、git の履歴（作り直さずに公開）。decisions.md の 2026-11-03 の工程2の節
- 使用量の目安：担当は14（R1〜R7・W-A〜W-E・V1・V2）、合わせて約680万トークン（各担当の完了の通知の値の合計。直しで再開した担当は最後の通知の値）。工程1の5つの担当は約126万トークン

## 工程1：質問

- requirements §11 で必ず聞く点（ライセンスと作者名・サイトの URL、初版の範囲と公開の目安、検証ノートを作るときの環境）と、そこから派生した点（作者が目を通す範囲、作者のプランと試せる面、GitHub のリポジトリを作る時期、調査資料の公開）は、2026-11-03 に答えを得た（decisions.md「2026-11-03 工程1（質問）の回答」）
- 調査資料の読み込み：5つの担当（サブエージェント）が全文を読み、作者に聞く点と事実の疑いを挙げた（[research/21-step1-findings.md](research/21-step1-findings.md)）。挙がった点への回答を得た（decisions.md「2026-11-03 工程1（質問）：調査資料を読んで出た点への回答」）

## 次にやること

1. 工程3（設計）は、ユーザーが進めると言ってから始める。材料は format-and-operations.md（v1.1）・decisions.md（特に「工程2で確かめた事実（設計の前提）」）・research/22〜28
2. 土台作り（工程6）の始めに GitHub のリポジトリを作る。最初の push の前に、調査資料の中の実在の人物・団体についての疑わしい記述を、直すか注記を付ける（decisions 2026-11-03）

## ユーザーにお願いしていること

- ~~制作に入る前に、/config の Dynamic workflow size を変える（decisions 2026-11-03）~~ 済み（2026-11-04。large にした）
- ~~雛形の動作確認を始める前に、`sudo apt install bubblewrap socat` で sandbox の道具を入れる（decisions 2026-11-03「危ない雛形を試す場所」）~~ 済み（2026-11-04。bubblewrap 0.6.1・socat 1.7.4.1 が入ったことを確かめた。Claude Code の `!` ではパスワードを入力できないので、普段の WSL の端末で入れてもらった）
