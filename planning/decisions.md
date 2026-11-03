# 決定事項の記録

要件定義書（[requirements.md](requirements.md)）で決めていなかった点と、要件を変えた点を、ユーザーへの質問と回答で決めた記録。新しい決定は日付を付けて追記する。設計書と食い違う場合は、新しい日付の記録を優先する。

## 2026-11-03 制作の始め方

| 項目 | 決定 | 補足 |
| --- | --- | --- |
| リポジトリ | このフォルダで git init し、引き継ぎの zip を展開した planning/ を最初のコミットにした。ブランチ名は main | ユーザーの指示。ブランチ名は kyopro-atlas に合わせた（メインの判断） |
| GitHub と push | GitHub へのリポジトリ作成と push は、まだしない | ユーザーの指示。いつ作るかは未定 |
| commit | ファイルを書き換えたら、その都度 commit する | ユーザーの指示（今の作業の約束） |
| 手本の読み方 | kyopro-atlas は clone せず、同じ親ディレクトリの `../kyopro-atlas` を読む。中は読むだけにし、変更・commit・書き込みをしない | ユーザーの指示。requirements §2 の「clone する」の代わり |
| 今回の範囲 | 形式と運用を決めるところまで。requirements §11「進め方」の調査の補完・設計・ページ作りには、ユーザーが進めると言うまで入らない | ユーザーの指示 |

## 2026-11-03 kyopro-atlas のセッションへの質問の後

kyopro-atlas のセッションに質問し（[questions-for-kyopro-atlas.md](questions-for-kyopro-atlas.md)）、回答を [research/20-kyopro-atlas-retrospective.md](research/20-kyopro-atlas-retrospective.md) に保存した。

| 項目 | 決定 | 補足 |
| --- | --- | --- |
| 工程1〜10 の経緯 | 回答したセッションは工程11（Issue の対応）だけを経験していて、形式を決めた工程1〜10 を覚えていなかった。工程1〜10 についての問いは「分からない」のまま進める。工程1〜10 のセッション（手元に transcript が残っている）の再開や読み込みはしない | ユーザーの選択。形式を決めた理由の多くは kyopro-atlas の design.md・design-review.md・decisions.md に書かれている |
| claude.ai での相談の仕組み | 作らない。requirements §8 の「claude.ai で困りごとを相談する」（Projects にリポジトリをつなぐ手順ファイルとプロジェクトの指示を `claude/` に置く）を取り下げる | ユーザーの判断：「kyopro-atlas は問題を解く形式だから claude.ai での質問が必要なだけで、claude-atlas では必要ない」。Claude 用の索引（`llms.txt`）などの扱いは別に確かめる |
