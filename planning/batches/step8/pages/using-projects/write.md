# write.md：using-projects

## 書いたファイル
- docs/app/using-projects.md（stubs から移動して新規に書いた。stub の元ファイルは削除）。front matter の変更：stage を draft、updated を 2026-11-05、sources を 5 件、sections に pitfalls・compare の 2 節を追加（既存 3 節は変更なし）
- snippets/using-projects/project-instructions.md と .expect.yaml（目次の templates の案）
- data/sources.d/using-projects.yml（jinrai-claude-projects-guide を 1 件。noai は sources.yml の domain 表で false を確認済み）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・成熟度）：冒頭の要点の「強制力」と導入に feature の目印（`project-instructions/enforcement`・`projects/maturity`）。節 instructions にも強制力を置いた。バッジの列はテンプレートが出す
- tracks（projects・project-instructions）：front matter に既存どおり
- 1 機能 1 ページ・節に分ける：scope・knowledge・instructions（anchor）。公式の網羅はしていない
- level（整える）：front matter に既存どおり
- 構成の目安：要点 → 使いどころ（scope・knowledge、防ぐ原因は attention-budget#effects への link）→ 雛形（instructions）→ 効かない場面（pitfalls）→ 比べる相手（compare）。最小の使い方のタブは surfaces が app だけなので置かない。古くなった助言は台帳の行がないので置かない

## メインに判断してほしいこと
- 「1 プロジェクト 1 目的」は企業の解説記事 1 件（根拠：弱）としか確かめられていない。本文は公式の規則ではないと明記した
- Free で project instructions が使えるかの食い違いは、pitfalls に書いた（プラン中立・数値なし・確認日 2026-11-03 の表現）。packet の features には「5 件まで」があるが、数値なので本文に書かず、目印もない

## 提案
```yaml
proposals:
  - fact: {id: projects-free-limit, title: Free で作れるプロジェクトの数, value: 5, sources: [hc-projects-manage], checked: 2026-11-04, status: 確認済み}
    used_in: [using-projects#pitfalls]
```
（本文は数字なしで読める。置くかどうかは任せる）

## 検査の結果
- check_page.py：エラー 0・警告 1。warning は 78 行目の textlint no-doubled-joshi で、link の目印の間に道具が書いた題名（「容量に近づくと何が変わるか」など）に由来する。誤検出として残した。再実行はしていない

## 確かめていないこと
- Web の取得なし。事実は束の材料（公式 3 記事の写しと 04 Q4）だけに基づく。画面の操作は確かめていない
- 雛形の動作は未確認。expect の「目的から外れた依頼を聞き返す」は観察として記録する形にした
- 用語集の語の初出のリンクは付けていない（用語集を読んでいない）
- キャッシュが切れるまでの時間は束にないので書いていない

## 使用量
- 道具の呼び出し 12 回前後・Web の取得 0 回
