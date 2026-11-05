# build-GL（用語集に語を足す）

## 足した語（25行）
- 用語の定義：止めすぎ
- 安全と拡張の語：信頼境界、critical paths・protected paths、path traversal
- 評価の語：評価器、referee、CV、愚直解・本解、判定役、ロックボックス・hold-out、アブレーション
- 機能と利用の語：層（設定の）、上位/日常/軽い系統、マーケットプレイス、teleport、ステータスライン、description、legacy artifacts
- 新しい節「API と SDK の語」（api-terms）：settingSources、stateless、ZDR、tool_use・tool_result、Agent・Environment・Session・Events
- 学びと表記の語：伴走・委託（丸投げは別名として言及）、強調語

## 飛ばした語と理由
- すでにある：能力の凸凹、ハルシネーション、システムプロンプト、非決定性、prompt injection、cutoff 2 語、ポストモーテム、Topics、Pause・Reset、task〜pass^k、検証器、red/green、凍結、分類器、tool poisoning 系、表記の正本、漢字を開く、OOF、認知負債、技能形成、利用上限、回り込み、プラグイン（表記の正規形の表）
- 表記の正規形にだけある（定義は足した）：マーケットプレイス
- 持ち主のページに短い定義が見つからない（記憶で書かないため保留）：HIPAA 対応、ミューテーションスコア、変異、カバレッジ、写し（snapshot）、較正、ローカルテスタ（評価器の行で触れた）、ベンチマーカー、Monitor、tool runner、ゲートウェイ、月次のふり返り、lint・推敲、データの区分、定期タスク、RAG（持ち主の too-much-project-knowledge は「公式から確かめられない」と書く。定義にしにくい）
- 別の行で足りる：縛る・握る・見せる／見えていない（「4 つの原理・比例則」の行にある）
- 判断を要する：Project instructions、bypass permissions の平文表記（下記）

## 食い違いの気づき
- 「表記の正規形」は subagent を「サブエージェント」とするが、持ち主の split-models-by-role は「サブエージェントには軽いモデル」と書き、一致する。問題なし。
- 用語集は「ステータスライン」を採るが、usage-context-statusline の表に「ステータスライン（status line）」がある。向きは一致。
- 用語集の「アプリの画面の名前（Project instructions）は確かめていない」とあるが、where-to-put-instructions の別名に `Project instructions` と `プロジェクトの指示` がある。用語集の注記は更新の余地がある（直していない）。
- 持ち主ページは `critical paths` を公式の呼び名とし、protected paths は題名の語。用語集は 1 行にまとめた。
- 持ち主ページの「縛りすぎの害」の題と用語集の「縛りすぎ」の言い方は揃っている。

## 検査
- `uv run python tools/check_page.py glossary`：エラー 0・警告 0
- 手順の注意：表の継ぎ目の空行を sed で 1 行削除した（Bash の書き込み。内容の訂正のみ）。

## 道具の呼び出し
約 12 回（読み取り中心。Edit 6、Write 1、sed 1、check_page 1）
