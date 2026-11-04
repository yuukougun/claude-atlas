# write.md：subagent-isolation（執筆）

## 書いたファイル
- docs/basics/subagent-isolation.md（stubs から mv。stage を draft、updated を 2026-11-05、sections 5 節と sources 4 件を追加。ほかのキーは変更なし）
- docs/img/subagent-isolation/rooms.svg（別室の部下の模式図。400x290）
- 雛形（snippets）なし：目次の templates が「なし」。頼み方の雛形は research-in-subagents、定義の雛形は writing-subagents の持ち物のため足さなかった
- data/sources.d/subagent-isolation.yml なし：sources は既存の id だけ（cc-docs-sub-agents・cc-docs-features-overview・cc-docs-best-practices・wb-cc-best-practices-2026-10-27）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle「見せる」・prevents「散らかっている」を名指し）：#what-it-helps。pitfalls は front matter にないので持たない
- level（任せる）：front matter に既存。要点の最初は「何が分かるか」
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens → #why → #cost → #what-it-helps → #misconceptions。関連はテンプレートが出す
- 比例則（任せる幅を広げる内容は見合う守りを同じ流れで先に）：#what-it-helps に、報告書は自己申告なので根拠の場所を戻させ、合否を返すもので確かめる旨と independent-review・agent-loop#close-the-loop への link
- 台帳の行（outdated_advice 3 件）：#what-it-helps（subagents-to-save-context）・#misconceptions（tell-it-to-use-subagents・subagent-per-step）
- 図（目次の visual）：#why

## メインに判断してほしいこと
- 面タブは置かなかった。surfaces に api があるが、束に API の手段の根拠がない（research/22 §3.7 は題と要約だけ）。本文に「API の分け方は扱わない」と一言書いた。API の節を足すなら別途の調査が要る。
- pitfalls が front matter にない。必要なら、どの人間側の落とし穴に結ぶかの提案を求む。

## 提案
- なし（用語集・prh・data への提案なし）

## 検査の結果
- 1 回目：エラー 1（prh：「Create custom subagents」の subagents）・警告 1（助詞「も」の連続）。出典の括弧書きを削除し、「どちらも」の言い回しに直した。2 回目：エラー 0・警告 0

## 確かめていないこと
- Web の取得はしていない。機能の挙動（新しいコンテキストが持つもの、Explore と Plan の例外、fork、圧縮の影響）は束の data の note と research/27 §3.2 の写しによる。公式文書の現行の記述との突き合わせはしていない
- 「報告書は要約だけ戻る」「同じ作業を回しても質は上がらない」は台帳の now と summary による
- 図の見え方（描画）は確かめていない。textlint の対象外の囲み内の段落（判断例）は目で読んだ
- 判断例の「数ファイルで済みそうなら本筋で探す」は書き手の判断の目安で、出典のある数値ではない

## 使用量
- 道具の呼び出し：約 14 回（Read 3、Bash 8、Write 3 など）。Web の取得：0
