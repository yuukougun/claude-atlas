# write.md：character-encodings（recipe・japanese）

## 書いたファイル
- `docs/japanese/character-encodings.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-changelog] に。sections に verify・failure を足した）
- `snippets/character-encodings/convert-prompt.md`・`.expect.yaml`（prompt）
- `snippets/character-encodings/to-utf8.sh`・`.expect.yaml`（other）
- 出典のファイルは作っていない（cc-changelog は data/sources.yml にある）

## 必ず持つものの対応
- 手順：`#convert`（複製の作り方と面のタブ）と `#claude-code`（拒まれたときの手順 1〜4）
- 確かめる・縛るページへの道：`#check` 末尾で data-analysis#check-raw-data、`#verify` で data-analysis#check-raw-data と office-paperwork#check（front matter の related にもある）
- level：整える（front matter）
- 構成の目安：要点 → `#check`（先に整える守り）→ `#convert`・`#claude-code`（手順）→ `#verify` → `#failure`

## メインに判断してほしいこと
- 版ごとの挙動（Edit・Write が非 UTF-8 を拒むようになった版）は本文に版を書かず、「2026-11-03 に変更の記録で確かめた」と日付で書いた。下の提案の fact が通れば、`#claude-code` の第 1 段落に目印を置いてほしい

## 提案
```yaml
proposals:
  - fact: {id: edit-refuses-non-utf8-since, title: Edit が UTF-8 でないファイルの編集を拒むようになった版, value: "2.1.296", sources: [cc-changelog], checked: 2026-11-03, status: confirmed}
    used_in: [character-encodings#claude-code]
  - fact: {id: write-refuses-non-utf8-since, title: Write が Shift-JIS などを黙って UTF-8 に変えず拒むようになった版, value: "2.1.299", sources: [cc-changelog], checked: 2026-11-03, status: confirmed}
    used_in: [character-encodings#claude-code]
```
- 値は束の research/27 #19 の写し。CHANGELOG 本体は読み直していない

## 検査の結果
- 1 回目：エラー 0・警告 6（no-doubled-joshi）。直した後の 2 回目：エラー 0・警告 2
- 残った警告：69 行目「に」、142 行目「が」（no-doubled-joshi）。検証の担当が直すか、誤検出として扱う

## 確かめていないこと
- Excel の「CSV（コンマ区切り）」が既定でどの文字コードか（Microsoft の該当ページに記述がなかった。本文は「書き出した側の設定で変わる」「CP932 が多い」と控えめに書いた）
- アプリが添付 CSV の文字コードを自動判定するか（本文で未確認と書いた）
- `iconv`・`nkf`・`uchardet`・`xxd` の挙動と to-utf8.sh の動作（実行していない）。`file` コマンドの判定には触れていない
- 変更の記録の版と内容（束の写しのまま）。Windows・macOS・IDE 拡張での動作

## 使用量
- 道具の呼び出し約 17 回、Web の取得 1 回（Microsoft サポート。有用な記述なし）
