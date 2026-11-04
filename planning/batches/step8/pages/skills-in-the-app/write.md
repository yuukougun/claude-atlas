# write.md：skills-in-the-app（feature・app）

## 書いたファイル
- docs/app/skills-in-the-app.md（stubs から mv。stage を draft、updated を 2026-11-05）
- snippets/skills-in-the-app/SKILL.md・SKILL.expect.yaml
- front matter で変えたキー：sections（purpose・limits・compare・old-advice を足した。既存の anchor は変えず、purpose を先頭に置いた）・sources（既に data/sources.yml にある 6 件）・stage・updated

## 必ず持つものの対応
- 強制力のバッジ（要点）：冒頭の要点「強制力」の `feature enforcement` の目印（属性のバッジはテンプレートも出す）
- tracks：front matter の `tracks: [app-skills, styles]`（変更なし）
- level：front matter の `level: 任せる`。upload 節は `仕組みにする`
- 構成の目安：使いどころ→#purpose／最小の使い方→#built-in-and-custom・#upload／雛形→#upload（SKILL）／効かない場面→#limits・#not-triggered／比べる相手→#compare／古くなった助言→#old-advice（台帳 customize-tabs・styles-for-tone を link）。面のタブは surfaces が app だけなので置かない

## メインに判断してほしいこと
- 公式同士の食い違い（Help Center と Platform の文書。組織での配布・Claude Code への同期）を、数値なしで「自分の画面と管理者の設定で確かめる」と書いた。プラン名と版は本文に書いていない
- 「2026 年 6 月に告知」は固定の記録として手書きした（台帳の changed.date に合わせた）

## 提案
- 数値・用語集・prh・data への提案はなし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 4（助詞の重なり）→直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形（週報の SKILL.md）は、アプリにアップロードして動かしていない（動作は未確認）
- Styles の移行が終わったか、画面にメニューが残るか。Web の取得はしていない
- 「+」か「/」から使う操作、トグルの位置は、束の資料の写しに拠り、画面で見ていない
- 組み込みスキルの対象が Excel・Word・PowerPoint・PDF のままか（02 §1-10、確認日 2026-10-29）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
