# XC1 整合の確認：フックの組（6ページ）

対象：hooks-basics・block-with-exit-2・writing-safe-hooks・hook-recipes・hook-vs-skill・keep-replies-in-japanese

結論：はっきり直せる食い違いはなかった。ページは1つも書き換えていない。強制力（フック＝鍵）の言い方、終了コードの意味（0／2／その他は通る）、失敗すると通す既定、matcher と `if` の説明、置き場所の一覧、deny＞ask＞allow の順番は、6ページで合っていた。

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | hook-recipes #register と各レシピの設定（block-dangerous-bash など）／block-with-exit-2 #templates の設定 | hook-recipes の #guards は「止める用途ではフックの失敗を止めに倒す」と書き、writing-safe-hooks は `onFailure: "block"` と `args` を勧める。だが hook-recipes の登録例は `onFailure` も `args` もない shell 形で、止めるレシピ（block-dangerous-bash）もそのまま。block-with-exit-2 の登録例も同じ（雛形の目的が違うため軽め） | 直さず。推奨の食い違いなので、メインが決める（下） |
| 軽い | hooks-basics #locations の末尾 と keep-replies #reach／#stop-hook | クラウドのセッション：hooks-basics は「リポジトリの `.claude/settings.json` は読まれる」と条件なしで書く。keep-replies は「フックが届くのはリポジトリを1つだけ選んだセッション。複数選択とプロジェクトのスレッドでは届かない」と条件つき | 直さず。どちらが正しいか、この教材では決められない（事実の確認は範囲外）。持ち主の hooks-basics に条件が足りない可能性が高い |
| 軽い | block-with-exit-2 #limits ／ writing-safe-hooks #fail-open | 失敗の扱い：block-with-exit-2 は「止めない種類のエラー**になりうる**」、writing-safe-hooks は表で「通る」と言い切る（Stop 系など `onFailure` が効かない種類の注記も block-with-exit-2 にはない） | 直さず。矛盾ではなく粒度の差。参照先 link があるので許容 |

## メインに決めてほしいこと

1. 止めるレシピの登録例（hook-recipes #register・block-with-exit-2 の設定・writing-safe-hooks 以外）に `onFailure: "block"` と `args` を入れるか。入れないなら、各例の近くに「止める用途は writing-safe-hooks の設定に直す」と一言置くか。現状は、#guards の推奨と登録例が合わない。
2. hooks-basics #locations のクラウドの記述に、keep-replies と同じ条件（リポジトリを1つだけ選んだセッション）を足すか。

## check_page.py の結果

ページを直していないので実行せず（0回）。

## 道具の呼び出し

Bash 7回、Write 1回（この報告）。
