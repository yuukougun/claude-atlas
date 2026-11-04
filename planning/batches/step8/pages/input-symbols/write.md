# input-symbols 執筆の報告

## 書いたファイル
- docs/cli/input-symbols.md（stubs から移し、stage を draft に）。front matter の変更：sections を 4 から 9 に（既存の anchor slash・bang・at・esc は維持。which・templates・pitfalls・compare・outdated を足した）、sources を [cc-docs-interactive-mode, cc-docs-commands, cc-docs-how-claude-code-works, cc-changelog] に、stage、updated
- snippets/input-symbols/point-with-at.{txt,expect.yaml}、redirect-after-esc.{txt,expect.yaml}
- data/sources.d は不要（出典の id は既存のものだけ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文には置かず、要点の「止められること」で止められる範囲を一言（冒頭の要点）。強制力の目印は、interactive-mode に強制力の値があるか不明なので置かなかった
- tracks：front matter の tracks: [interactive-mode]（本文は #which〜#esc が扱う）
- level：front matter の level: 使う
- 使いどころ（どの原因を防ぐか）：#which（見えていない）
- 最小の使い方：#slash #bang #at #esc。面は claude-code だけなのでタブは置かない
- 雛形：#templates
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compare（比べる comparison ページがないので、つながる操作を link で並べた）
- 古くなった助言：#outdated（hash-to-memorize を台帳へ link）

## メインに判断してほしいこと
- 比べる相手の節を「つながる操作」にしたが、これでよいか（comparison ページがない）
- 強制力のバッジが interactive-mode で出るか（値がなければ「未確認」になる）。出さない選択でよいか

## 提案
- なし（用語集・数値・front matter の他のキーへの提案はなし）

## 検査の結果
- 1 回目：エラー 1（前提の書き方）・警告 6。2 回目：エラー 0・警告 1
- 残した警告：81 行目の「が」の重複（no-doubled-joshi）。「Claude の解釈や許可を挟まず、あなたが打ったコマンドがそのまま走る」で、誤検出に近いと見た

## 確かめていないこと
- 一次資料は Interactive mode の英語版 1 回の取得のみ。`!` の出力と応答、`@` の候補表示、Esc・Esc、待ち行列、サンドボックスの外で走る点はこれで確認。ほかの面（IDE・アプリ）と OS の動作は未確認
- `@` で指したファイルの内容が会話にどう入るか（全文か一部か）は確かめず、書かなかった
- 雛形の動作は試していない
- 「`?` で手元の表を確かめる」は、ショートカット一覧の `?` を研究資料の記述から書いた（本文の取得では確かめていない）
- サンドボックスの例外の条件（公式の strict sandbox mode の節）は本文に書かず公式を指すだけにした

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 1 回（code.claude.com の interactive-mode）。check_page は 2 回
