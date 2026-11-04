# write.md：where-to-put-instructions

## 書いたファイル
- docs/app/where-to-put-instructions.md（stub から mv。front matter の変更：stage を draft、updated を 2026-11-05、sources に既存の 6 件、sections に how-to-choose・combine を足した。既存 4 節の anchor は変えず）
- snippets/where-to-put-instructions/personal-instruction-example.md と .expect.yaml
- data/sources.d は新しい出典がないので作っていない

## 必ず持つものの対応
- 比較の表：comparison（compare の目印。効く範囲と読まれる時期の手書きの表も同じ節）
- 判断例：how-to-choose（4 つ）
- 構成の目安（要点→表→選び方→組み合わせ方）：comparison → how-to-choose → combine
- level：front matter の 整える を維持

## メインに判断してほしいこと
- 「Claude Code の置き場所との対応」の表（Claude への指示＝ユーザー単位の CLAUDE.md など）は、束にない知識で書いた。公式で確かめていない
- 優先の順（個人とプロジェクトの指示が矛盾したとき）は公式資料で確かめられず、本文に「確かめていない」と書いた

## 提案
```yaml
proposals:
  - fact: {id: app-instruction-scope-and-timing, title: アプリの指示の置き場所ごとの効く範囲と読まれる時期, value: 本文の表のとおり, sources: [hc-personalization, hc-skills-what, hc-memory], checked: 2026-11-05, status: 確認済み}
    used_in: [where-to-put-instructions#comparison]
```
- 比較の表の「読み込みの時期」の列が data にない。上の表を手書きしたので、feature に読み込みの時期を足すなら、手書きの表と置き換えられる

## 検査の結果
- 書き終えた後：エラー 0・警告 3。直した後：エラー 0・警告 2（no-doubled-joshi の 2 件）。その後に 2 件を言い換えたが、再検査は回数の決まりで流していない

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0 回）。束の写しだけに基づく
- 言い換えの後の警告の数（流していない）
- 画面に Styles のメニューが残るか、Claude への指示の画面での名前

## 使用量
- 道具の呼び出し 約 10 回、Web の取得 0 回
