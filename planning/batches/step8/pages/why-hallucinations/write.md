# write.md：why-hallucinations（執筆）

## 書いたファイル
- docs/basics/why-hallucinations.md（stub から mv。stage を draft、updated を 2026-11-05、sources に既存の 5 つの id、sections に 5 節を追加）
- docs/img/why-hallucinations/guess-pays.svg、known-name-misfire.svg（目次の図の案の二本立て）
- 雛形・data/sources.d は無し（templates なし。出典は既存の id だけ）

## 必ず持つものの対応
- 用途（なぜそうなるか）：#guess-pays（訓練と評価の傾き）、#known-name（内部の誤作動）
- どの原理・原因に関わるか（principle「見せる」「確かめる」、prevents「見えていない」「確かめていない」を名指し）：#what-helps
- pitfalls：front matter に値がないので、持たない
- level を持つ・要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（例→なぜ→何に効くか→誤解→関連）：#what-happens → #guess-pays・#known-name → #what-helps → #misconceptions → 関連（page-links）

## メインに判断してほしいこと
- 束 6.2 の写しは別の話題（Inferences の別ページ分）で、この主題の材料でなかった。arXiv 2509.04664 の要旨と Anthropic の Tracing thoughts を WebFetch で確かめて書いた（2 回）
- #known-name の CTF の 1 文（根拠：弱・類推）は束 6.4 の要約だけが根拠で、出典（includesecurity-ctfs-ai-era）の原文は開いていない。出典の範囲が混ざる注意（11 第4節 #35）があるので、不安なら削ってよい。削るなら sources の同 id も外す

## 提案
- 用語集：「ハルシネーション」は導入で短く定義した。用語集にないなら追加を提案する
- front matter の提案：なし

## 検査の結果
- check_page.py：エラー 0、警告 4（日本語の助詞「は・も・が」の重なり。意味を保つため残した。うち 1 件は図の代替テキスト「間違いも白紙も」）
- 修正前は警告 8、エラー 0

## 確かめていないこと
- Claude 3.5 Haiku の結果が今の Claude に当てはまるか（本文は「言えない」と書いた）
- 論文の本文（要旨だけ確認）と、Tracing thoughts の細部（WebFetch の要約で確認）
- CTF の報告と chokudai の記事の原文
- 図の見た目（SVG は描画を見ていない）。page-links の中身は道具が生成

## 使用量
- 道具の呼び出し：約 15 回（Bash と Read と Write、check_page は 3 回。1 回は修正スクリプトの誤りで修正が適用されず、同じ結果を再度流した）
- Web の取得：2 回
