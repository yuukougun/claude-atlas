# 工程2（調査の補完）のバッチ

requirements §11「進め方」の2。既存の調査を読み、§10 の誤りを直し、空白を一次資料で埋め、2026-10-29 以降の変更を確かめる。全部を調べ直す必要はない（requirements）。第一波（D10 と、2026-11-03 に足した「日本語で使う」の核）に関わるものを優先する。

- 共通の指示：[brief.md](brief.md)
- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す
- 担当が書くのは報告のファイルだけ。調査資料への注記（実在の人物・団体についての記述を含む）と decisions.md への反映は、メインが報告を読んでから行う

## 担当と割り当て

| 担当 | 報告のファイル | 割り当て | 状態 |
| --- | --- | --- | --- |
| R1 | `research/22-changes-since-1029.md` | 2026-10-29 以降の変更：Claude Code の CHANGELOG（v2.1.312 より後。手元は 2.1.317）、Help Center のリリースノート、Claude Platform のリリースノート、Anthropic のニュース（モデル・料金・プラン）。教材の分野と古くなった助言の台帳への影響。ISUCON2026（10-31）など、コンテストの分野に関わる出来事 | 実行中 |
| R2 | `research/23-errata-official.md` | 公式の機能についての既知の誤り：requirements §10.1 の10件と、21 §2.2 の F2（auto mode の数値と時期）・F3（モデルの既定の effort）・F6（01 の「埋まるほど性能が落ちる」の3か所） | 実行中 |
| R3 | `research/24-errata-contest.md` | 補完調査（10）の疑わしい主張：requirements §10.2 の項目、11 第4節の67件のうち読者が行動の根拠にしそうなもの（大会の規則・成績・AI の性能の主張）、21 §2.2 の F1（人の側の五つの現象の根拠の強さ）・F4（AtCoder の規則の版） | 実行中 |
| R4 | `research/25-people-orgs-and-primary.md` | 実在の人物・団体についての記述（21 §2.1 の P1〜P7）を確かめ、調査資料への注記の文を提案する。requirements §10.4 の「一次資料を読めていないもの」（Anthropic の約40万セッションの分析、HumanLayer の CLAUDE.md の記事、Claude Code チームのレビュー運用の原文）を読み、調査資料の書き方と照らす | 実行中 |
| R5 | `research/26-gaps-official.md` | 公式情報の空白（requirements §10.4）：Styles の現行の仕様、チャット共有の仕様、断られたときの頼み直し方（公式の案内）、IDE 拡張の固有の機能、Desktop のローカル MCP、Office アドインの機能、knowledge cutoff の Help Center の記事、`ANTHROPIC_API_KEY` と課金の経路の関係、AskUserQuestion の質問数の上限。21 §2.3 の前提：個人向けプランの年齢の条件、Max プランの API credits の有無と使い道、個人プランで会話が学習に使われるかの設定と保持の期間 | 実行中 |
| R6 | `research/27-japanese.md` | 第一波に足した「日本語で使う」の核：公式の日本語訳（Claude Code の文書など）の有無と、主な用語の訳語（subagent・hooks・skills・permissions・sandbox・compaction・effort など）。日本語の出力を揃える公式の仕組み（Claude Code の言語の設定、output style、CLAUDE.md、claude.ai の言語の設定や Styles など）と、その効く範囲。英語への回帰についての一次の記録（公式の文書・GitHub の issue など）と、その根拠の強さ | 実行中 |
| R7 | `research/28-tech-check.md` | 制作とサイトの技術の確認：hooks の入力の項目（サブエージェントかを見分けられるか）、matcher と permissions のルールの書き方（WebFetch のドメイン、Edit・Read のパス）、hooks と permissions がサブエージェントとワークフローの担当にも効くか。雛形を確かめるときに作者の設定が混ざらない方法（`claude -p` で読み込む設定を絞るオプション、`--bare` の条件など）。Linux・WSL2 の sandbox の条件（bubblewrap・socat）と設定のキー。settings.json の JSON Schema（公式か、どこにあるか）と、skill・subagent の front matter の仕様。Zensical の 11-05 の予告の中身と、Material for MkDocs からの移行の互換性（テンプレートの上書き・独自の JS）。主な出典のドメイン（公式の各サイト・github.com・zenn.dev・qiita.com・note.com など）の AI の利用を断る指定 | 実行中 |
