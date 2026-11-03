# 工程3 C3 の報告：prompting（頼み方）・japanese（日本語で使う）

- 日付：2026-11-04
- 共通の指示：[brief-catalog.md](brief-catalog.md)

## 1. 書いたファイルとページ数

| ファイル | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| `planning/catalog/prompting.yaml` | 24 | 必須 13・推奨 11 | 使う 4・整える 17・任せる 3 | concept 21・recipe 3 | 24（全部採る） |
| `planning/catalog/japanese.yaml` | 11 | 必須 6・推奨 4・任意 1 | 使う 1・整える 8・任せる 1・仕組みにする 1 | concept 3・recipe 8 | 12（採る 10・まとめた 2）＋新規 1 |

章：prompting は「頼み方の原則・何をどこまで頼むか・資料と入力の渡し方・詰め方と頼み直し・正直さと確かめ方・型と例文」、japanese は「考え方・返答とコミットの言語・文体と表記・資料と環境」。

registry から変えた点（理由は各ページの notes と level_evidence）：

- 題名：show-examples の「（3〜5個）」を外した（題名に数値を書かない）。ask-for-outcomes は requirements §6.7 の統合方針に合わせ「細かく指図するか、成果で頼むか」に。requesting-prose は検出を逃れる話と読まれないよう「文章を頼むとき（読み手・目的・手本を渡す）」に（方針 B4）。textlint-hook は公式の日本語版の多数派に合わせ「textlint をフックで回す」に（ほかの担当と同じく design §6.2）
- レベル：does-double-check-work・asking-for-reasoning を任せる→整える、keep-replies-in-japanese を任せる→整える（英語のツール出力を読む普段の作業で出会う。症状 replies-in-english（整える）の前提に置けるようにした。フックの節は sections の level で仕組みにする）
- 優先度：asking-for-reasoning を任意→推奨（推論の全文を求める指示は拒否の引き金で、断られたときの振り分け先になる）。consistent-notation・textlint-hook を推奨→必須（日本語の核として第一波に入れるため）
- 型：keep-replies-in-japanese を concept→recipe（設定→指示→フック→測る、の手順が本体）

requirements §6.7 の4つの統合方針は、ask-for-outcomes（成果か狙いか）・ask-for-options（選択肢か、自分の案が先か）・long-context-first（原文か要約か）・say-what-you-want と state-the-scope の two-layers の節（禁止を CLAUDE.md に書くか）に置いた。

## 2. merged・dropped と新しいページ

merged（japanese）：

- more-tokens-in-japanese → can-i-prompt-in-japanese（tokens の節）。倍率は非公表で tokenizer で変わり、自分で数える、という論点は独立のページには薄い。basics の tokens（単位の考え方）を前提にし、日本語の量・上限への効き方・数え方の本体はこの節が持つ（C1 の提案と一致）
- proofreading-skills-for-japanese → less-ai-sounding-japanese（proofreading-skill の節）。第三者の skill を比べて選ぶページは推薦の一覧になりやすく（D13、requirements §6.4）、比べた記事は1回の出力だけ。選ぶ軸と、文体の手引きを自分でスキルにする公式の形を節にした

dropped：なし。

新規：

- japanese の **align-japanese-output**（日本語の出力を揃える：お願いで足りること、仕組みが要ること。必須・整える・wave 1）。核の分野の総論（catalog/README §4.6）が registry になかった。どの手段（language の設定・CLAUDE.md・出力スタイル・アプリの指示・フック・lint）がどこまで届き、どれが強制かを集める。材料は research/27 §3.2・§3.4
- prompting の when-refused（正当な依頼を断られたとき）を一度足したが、safety の **when-requests-are-refused**（C7 の新規）と題も中身も同じなので取り下げた。症状の入口は symptoms の refused-or-blocked、対処の本体は safety のページとみなし、give-reasons・asking-for-reasoning から指した

## 3. wave: 1 を付けたページ（japanese）

align-japanese-output・keep-replies-in-japanese・consistent-politeness・consistent-notation・textlint-hook の5ページ（decisions 2026-11-03「第一波に足すもの」の、英語への回帰と文体・表記を仕組みで揃えるページ）。can-i-prompt-in-japanese は symptoms の replies-in-english の前提として第一波に入る。less-ai-sounding-japanese（読みやすさ）と commit-and-comment-language は核に入れていない。全体の第一波は、検査の時点で 122 ページ（wave: 1 が 59、前提でたどれるもの 63。ほかの担当の更新で変わる）。

## 4. ほかの分野への提案（open_issues の要約）と new_features

急ぎ（今、検査のエラーになっている）：

- **basics・extend**：まとめた候補を指す参照が3件残る。basics の tokens の related の more-tokens-in-japanese は `can-i-prompt-in-japanese#tokens` に、extend の writing-skills と hook-vs-skill の related の proofreading-skills-for-japanese は `less-ai-sounding-japanese#proofreading-skill`（hook-vs-skill には `#lint-vs-judgment` も合う）に直す。どちらの担当も報告を書き終えているので、メインが直す必要がありそう

そのほか：

- symptoms：replies-in-english の診断は research/27 P13 の順にし、対処の本体を keep-replies-in-japanese と align-japanese-output に（keep-replies は整えるにしたので前提にも置ける）。refused-or-blocked の related に safety の when-requests-are-refused を入れる。refused-or-blocked の notes の「モデルを変える」は、decisions 2026-11-03「断られたときの頼み直し」の手段の一覧になく、自動の切り替えは仕組みとして説明する方針（research/26 §4.3 も同じ）なので揃える
- context：long-context-first（依頼の中の並べ方・引用を先に抜かせる・原文か要約か）と handing-long-documents（資料の形と量）、refine-in-conversation（考え方）と rewind-dont-correct（操作）の境界
- models：モデル別の癖は model-quirks に置き、prompting は一般論にする。after-switching-models に強い言い方を和らげることと確認の一文を外すことを
- verify・judgment・recipes・eval：evidence-not-reports・think-before-asking・spec-first・write-docs・measure-changes からの相互リンク（多くは取り込み済み）
- changes：important-caps の「今どうするか」と時期を現行の Best practices に合わせる（research/23 §4.2）。Styles から skills への移行を台帳にするなら consistent-politeness・align-japanese-output から指す。think-hard-keywords の日本語の「熟考」に CHANGELOG 1.0.8 の一次資料を足せる（research/27 #18）
- enforce・safety・cli・app：stop-hooks から keep-replies-in-japanese#stop-hook、hook-recipes から textlint-hook、disclosure-and-provenance から less-ai-sounding-japanese（B4 の線を揃える）
- basics・api：台帳の lower-temperature は basics の nondeterminism か api に付ける（api の担当も同じ意見）

new_features（features.yaml への提案）：

- `language-setting`：Claude Code の language 設定（返答の言語。値は検証されない。research/27 #2・#3）。japanese の3ページが指す
- `voice-dictation`：Claude Code の音声入力（/voice）。アプリの voice とは別。images-and-voice が指す

## 5. 検査の結果

`python3 tools/check_catalog.py --field prompting`・`--field japanese`：どちらもエラー 0・警告 0（分野のファイル 23・ページ 361 を読んだ時点）。途中で出たものは直した：ほかの分野でまとめられた候補への参照3件（stratified-and-worst-case・formats-and-ai-fit・files-pdfs-and-images）、symptoms の書きかけによる未処理の候補の警告（symptoms の更新で解決）。全体の検査では、§4 の「急ぎ」の3件が basics・extend のファイルにエラーとして出る。

## 6. 確かめていないこと・迷った点

- keep-replies-in-japanese の summary の「ツールの合間の短い一言が画面に出る前に止める仕組みはない」は公式の仕様（research/27 §3.3 で強）だが、版に依る。新しいフックが入れば summary も直す
- align-japanese-output を新しい総論にしたが、basics の request-vs-lock と enforce の request-lock-table と重なりうる。日本語の届く範囲（サブエージェント・圧縮・クラウドのセッション）と、アプリに機械の仕組みがないことに絞って書く想定
- proofreading-skills-for-japanese をまとめたことで、ほかの分野の参照が3件壊れた。独立のページを望む声とみることもできる。推薦の一覧にしない形なら戻す余地はある
- 断られたときの対処の本体を safety と prompting のどちらに置くか。safety の担当は「prompting が本体を持つなら merged にしてよい」と書いている。重複を避けて safety に寄せたが、頼み直しは頼み方でもあるので、工程4で見直してよい
- documents-in-japanese は材料が薄い（00 の根拠は独自の整理）。縦書きやスキャンの PDF の読まれ方は検証ノートで書く
- 「言語より構造が効く」は実践者の経験則。share-targets-and-bounds の根拠は中〜弱（性能最適化の例は未確認、目標スコアの実験は類推）
- claude.ai の日本語の画面の項目名は確かめていない（research/27 §5）。題名の訳語の割れ（plan モード／プランモード など）は用語集で決める
- Web は開いていない。材料は調査資料と工程2の報告だけ
