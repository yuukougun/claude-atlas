# write.md：humans-set-the-parallel-limit

## 書いたファイル
- docs/delegate/humans-set-the-parallel-limit.md（stubs から mv。stage を draft、updated を 2026-11-05、sections を 2 から 8 に増やし〔既存 2 つの anchor は維持〕、sources を既存の id 8 件で埋めた）
- docs/img/humans-set-the-parallel-limit/review-bandwidth.svg（図：本流と偵察の本数と、人のレビューの帯域）
- 雛形・data/sources.d は置かない（目次の templates はなし。出典は data/sources.yml に既にある id だけを使った）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle・prevents・pitfalls を本文で名指す）：#what-it-prevents（握る・確かめていない・預けすぎる・体感を信じる）
- level（仕組みにする）と、要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #why-human-side → #mainline-vs-scouting・#guards-before-widening・#signs-of-fatigue・#practitioner-range → #what-it-prevents → #misconceptions →（関連はテンプレート）

## メインに判断してほしいこと
- 「この辞典の推奨」として「まず 1〜3 本から」と書いた（目次の notes と research/03 W9 に従い、（推論・実践例なし）の印を付け、実践者の幅と三段で並べた）。数値の目印にはしていない
- 実践者の本数（1 本・最大 2 本・3〜4 本・5 本以上）を、個人名なしで自己申告として本文に書いた。標準として示してはいない。方針に反するなら削る
- 制作で多数の担当を同時に動かすこと（research/21 §2.4）は、本文で触れなかった。レビューの要らない調査・偵察かどうかの区別で説明する案は目次の notes にあるが、制作の運用に関わる自己言及なので入れていない

## 提案
- 数値・front matter・用語集・prh の提案はなし

## 検査の結果
- 1 回目：エラー 0・警告 6（textlint の no-doubled-joshi 5、max-ten 1）。5 件を直して 2 回目：エラー 0・警告 3
- 残した警告：行 97（link の間に道具が入れる題名を含む文）、行 124（link の中身を含む文）、行 144（誤解の箇条）の「に」「は」の重複。文意を保つため、検査の回数の上限（2 回）に達したので直していない

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0）。事実は束の抜き出しだけに基づく
- 公式の Best practices に並べる本数の目安があるかは、確かめていない。本文は「確かめた範囲では示されていない」と書いたので、確かめるまで言い切りにしないこと
- 実践者の本数（Mitchell Hashimoto の 1 本、Kaggle 3 位の最大 2 本、3〜4 本、5 本以上）は束の写しからの二次で、元の記事の文面は見ていない
- 疲れの兆しの 5 項目は推論による整理で、出典はない（本文に（根拠：弱）と整理の旨を付けた）
- 「重要な変更は一度に 1 つしかレビューしてマージできない」は 11 の写し（simonwillison-parallel-coding-agents に当たる）からで、元の記事を見ていない
- アンケートの標本・日付・設問は research/25 P7a の写しからで、zenn-resqnet-a1cfd81a がその記事に当たることは束の題名から判断した
- SVG をブラウザで描画して見ていない
- 判断例は筆者の作例で、実際の事例ではない

## 使用量
- 道具の呼び出し 9 回ほど（Read 3、Bash 4、Write 3 を含む）、Web の取得 0
