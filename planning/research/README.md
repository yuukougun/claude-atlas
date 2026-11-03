# 調査資料（リポジトリを作る前の調査）

リポジトリを作る前に、別のセッションで行った調査の資料。どれも AI が書いたもので、2026-10-29 時点の確認に基づく。使い方と信頼の目安は [../requirements.md](../requirements.md) §0 と §10 にある。

| ファイル | 中身 |
| --- | --- |
| `00-content-report.md` | 内容の考察（主報告）。背骨、20分野・300ページ候補、逆引き73項目、古くなった助言31項目、鮮度の仕組み、見せ方、未決の論点 |
| `01-official-claude-code.md` | Claude Code の公式機能と公式の推奨 |
| `02-official-app-models-prompting.md` | claude.ai アプリ、プランと利用上限、モデル、公式のプロンプト指針、API・SDK の概念 |
| `03-community-english.md` | 英語圏の実践者の知見 |
| `04-community-japanese.md` | 日本語圏の実践者の知見 |
| `05-failures-safety-fundamentals.md` | 失敗の型、基礎概念、セキュリティ、検証の習慣 |
| `06-existing-curricula.md` | 既存の講座・書籍・ガイドの構成と空白 |
| `10-contest-supplement.md` | コンテストを想定した AI エージェントの使いこなし（別のセッションの調査。6部25章と付録） |
| `11-contest-crosscheck.md` | `10` の全論点を `00` と照合した一覧（追加候補・重なる論点・食い違う点・疑わしい主張・雛形の扱い） |
| `11a`〜`11c` | `11` の元の作業ノート（`10` の部ごと） |
| `20-kyopro-atlas-retrospective.md` | 手本の kyopro-atlas のセッションへの質問の回答（2026-11-03。制作セッションが受け取ったもの） |
| `21-step1-findings.md` | 工程1で調査資料を読んで見つけた、作者に聞く点と事実の疑い（2026-11-03。制作セッションのまとめ） |
| `22-changes-since-1029.md` | 工程2：2026-10-29 以降の変更（Claude Code の CHANGELOG・リリースノート・ニュース） |
| `23-errata-official.md` | 工程2：公式の機能についての既知の誤りの確認（requirements §10.1 ほか） |
| `24-errata-contest.md` | 工程2：補完調査（10）の疑わしい主張の確認（大会の規則・成績・研究の強さ） |
| `25-people-orgs-and-primary.md` | 工程2：実在の人物・団体についての記述と、読めていなかった一次資料の確認 |
| `26-gaps-official.md` | 工程2：公式情報の空白（requirements §10.4）と、プラン・データの扱いの前提 |
| `27-japanese.md` | 工程2：「日本語で使う」の核の材料（公式の日本語版の訳語・出力を揃える仕組み・英語への回帰） |
| `28-tech-check.md` | 工程2：制作とサイトの技術（hooks・permissions・`claude -p` の隔離・sandbox・schema・Zensical・出典のドメインの AI の利用の指定） |

## 読むときの注意

- `11` の中の「MAIN」は `00`、「補完」は `10` を指す。元IDの `p12#34` は `11a` の #34、`p34#…` は `11b`、`p56#…` は `11c` の番号
- `00` と `11` の分野番号（分野00〜19）は、`requirements.md` §4 の分野番号とは違う。対応は `requirements.md` §4.2 の表にある
- `00` §7 の「調査の空白」と、`requirements.md` §10 の既知の誤りを先に読むこと
- 2026-11-03 に、工程2の結果（`22`〜`28`）を `00`〜`11` と requirements.md に反映した。誤りの箇所には `【2026-11-03 注記】`、実在の人物・団体についての誤りを直した箇所には `【2026-11-03 訂正】` を付けた（決まりは decisions.md の 2026-11-03「工程2（調査の補完）の結果への回答」）
