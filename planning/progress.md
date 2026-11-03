# 進捗と残り作業

セッションが途切れても続きから再開できるように、工程ごとの状態と次にやることを記録する。作業の区切りごとに更新する。

## 工程（requirements §11「進め方」）

| # | 工程 | 状態 | 成果物 |
| --- | --- | --- | --- |
| 0 | 形式と運用を決める（工程1の前に入れた） | 完了（2026-11-03） | [format-and-operations.md](format-and-operations.md)（v1.1）・[decisions.md](decisions.md)・[questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)・[research/20-kyopro-atlas-retrospective.md](research/20-kyopro-atlas-retrospective.md) |
| 1 | 質問 | 完了（2026-11-03） | [decisions.md](decisions.md)・[research/21-step1-findings.md](research/21-step1-findings.md) |
| 2 | 調査の補完 | 未着手 | |
| 3 | 設計 | 未着手 | |
| 4 | 設計の見直し | 未着手 | |
| 5 | 決定の提示 | 未着手 | |
| 6 | 土台作り | 未着手 | |
| 7 | 試作 | 未着手 | |
| 8 | 本制作 | 未着手 | |
| 9 | 仕組み作り | 未着手 | |
| 10 | 全体の検証 | 未着手 | |
| 11 | 公開と鮮度の運用 | 未着手 | |

## 工程1：質問

- requirements §11 で必ず聞く点（ライセンスと作者名・サイトの URL、初版の範囲と公開の目安、検証ノートを作るときの環境）と、そこから派生した点（作者が目を通す範囲、作者のプランと試せる面、GitHub のリポジトリを作る時期、調査資料の公開）は、2026-11-03 に答えを得た（decisions.md「2026-11-03 工程1（質問）の回答」）
- 調査資料の読み込み：5つの担当（サブエージェント）が全文を読み、作者に聞く点と事実の疑いを挙げた（[research/21-step1-findings.md](research/21-step1-findings.md)）。挙がった点への回答を得た（decisions.md「2026-11-03 工程1（質問）：調査資料を読んで出た点への回答」）

## 次にやること

1. 工程2（調査の補完）は、ユーザーが進めると言ってから始める。始めるときは、research/21-step1-findings.md §2 の事実の疑いと requirements §10 を材料にする
2. 土台作り（工程6）の始めに GitHub のリポジトリを作る。最初の push の前に、調査資料の中の実在の人物・団体についての疑わしい記述を、直すか注記を付ける（decisions 2026-11-03）

## ユーザーにお願いしていること

- 制作に入る前に、/config の Dynamic workflow size を変える（decisions 2026-11-03）
- 雛形の動作確認を始める前に、`sudo apt install bubblewrap socat` で sandbox の道具を入れる（decisions 2026-11-03「危ない雛形を試す場所」）
