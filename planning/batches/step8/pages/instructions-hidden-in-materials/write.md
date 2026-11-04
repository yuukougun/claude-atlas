# write.md：instructions-hidden-in-materials

## 書いたファイル
- docs/safety/instructions-hidden-in-materials.md（stubs から mv。front matter は sections に effects・misconceptions を足し、stage を draft、updated を 2026-11-05 に変えた）
- snippets/instructions-hidden-in-materials/material-as-data.md と .expect.yaml（kind: prompt、safety: true）

## 必ず持つものの対応
- 要点の最初は「何が分かるか」：冒頭の囲み（level 整える）
- どの原理・どの原因に関わるか（principle 握る・縛る、prevents 境界がない）：#effects（3 つを名指し）
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：何が起きるか＝#two-kinds、なぜ＝#two-kinds 内で data-vs-instructions#why へ、対処＝#check-rules・#treat-as-data、何に効くか＝#effects、誤解＝#misconceptions、関連＝テンプレートが出す
- pitfalls：front matter が空のため、名指す対象なし
- 比喩付きの図：置いていない（図の案が目次になく、仕組みは data-vs-instructions が持つため）

## メインに判断してほしいこと
- 方針 B1（decisions 2026-11-03）の写しが束に見つからなかったため、「AI を禁じる課題の隠し指示を外す方法は書かない」は目次の備考だけを根拠に守った。本文に「この辞典では扱わない」の宣言は入れていない（方針の文になるため）
- CTF 大会の例は大会名を出さず「ある CTF 大会」にした。名指しするなら一次資料での確認が要る

## 検査の結果
- 1 回目：エラー 0・警告 4（助詞「に」「ても」の重複）。文を直して 2 回目：エラー 0・警告 1
- 残した警告：本文 129 行の「に」の重複。リンクの題名（道具が入れる）の中の語を数えた誤検出に近く、文は短くしてある

## 確かめていないこと
- 雛形の動作（雛形の expect はまだ試していない）
- 「ある CTF 大会」の報告の一次資料（束の調査資料の写しのみ。根拠の印は中・類推）
- Claude が資料中の AI 向けの文を報告する挙動の実際（雛形の expect は観察として書いた）
- アプリのコネクタと Claude Code の許可の絞り方の詳細な手順（概念だけ書き、面の分野のページに任せた）

## 使用量
- 道具の呼び出し 約 10 回、Web の取得 0 回
