# write.md：share-team-settings（recipe・team）

## 書いたファイル
- docs/team/share-team-settings.md（stubs から移し、stage を draft に。front matter の変更：sections を 2 から 6 に〔既存の shared-vs-personal・after-trust はそのまま。guards・steps・verify・when-it-fails を足し、本文の順に並べ替え〕、sources に既存の 5 件〔cc-docs-settings・cc-docs-memory・cc-docs-mcp・cc-docs-permissions・cc-docs-plugins-overview〕、updated 2026-11-05）
- snippets/share-team-settings/shared-settings.json・.expect.yaml（kind settings・place project・safety true）
- snippets/share-team-settings/local-settings.json・.expect.yaml（kind settings・place local・safety true）
- stubs/team/share-team-settings.md を削除（docs へ移した扱い）。data/sources.d は新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点：冒頭の囲み（abstract）
- 手順：#steps（各段に「確かめ」を付けた）
- 確かめる・縛るのページへの道（比例則）：#guards（permission-rules・protecting-secrets・protected-paths・vetting-extensions・before-opening-unknown-repos）。front matter の prerequisites に permission-rules、related に同じ守りのページ
- level：front matter（仕組みにする）
- 構成の目安（先に整える守り → 手順 → 確かめ方 → 失敗したとき）：#guards → #steps → #verify → #when-it-fails。間に #shared-vs-personal と #after-trust を置いた

## メインに判断してほしいこと
- front matter の sections に 4 節を足し、順を本文に合わせた。既存 2 つの anchor は変えていない
- compare の表（強制力・読み込みの時期）は、data の settings・mcp の強制力が null のため「未確認」が出る行がある。見栄えが悪ければ列を変える

## 提案
- front matter・用語集・prh・data への提案：なし
- 数値の提案：なし（本文に変わりやすい値を書いていない）

## 検査の結果
- 書き終えた後：エラー 0・警告 3。直した後：エラー 0・警告 1
- 残した警告：share-team-settings.md:54:512 no-doubled-joshi（助詞「に」）。原因は、link の目印の間に道具が入れる題名「知らないリポジトリを開く前に › 開く前に見るファイル」の中の「前に」で、道具が書く部分なので直せない（誤検出）

## 確かめていないこと
- 雛形の動作（信頼の前後の allow の効き方、deny の効き方）。expect は観察として扱うと書いた
- 共有の設定のクラウドセッションでの扱いは、束の B-1（クラウドセッションは user/local を読まない）だけに基づく
- `.claude/settings.local.json` が自動で git に入らないかは確かめていない。本文は「git status で確かめ、出るなら .gitignore に足す」と書いた
- Windows ネイティブ・macOS・IDE 拡張の動作
- 二度目の直しの Edit は、Write ではなく Bash の置換で行った（指示は Write。小さな 2 か所の文言のため）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
