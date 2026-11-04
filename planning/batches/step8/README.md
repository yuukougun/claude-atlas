# 工程8（第一波）のバッチ

第一波（136ページ。tools/check_catalog.py --stats）のうち、まだ骨格（stub）のページ（124）を書く。流し方は v3.1（[brief-page.md](brief-page.md)、ワークフロー .claude/workflows/step8-wave.js）。作者の決め（decisions 2026-11-05「工程7の終わりの頼みへの回答」）：最初に20ページほどで使用量と質を確かめてから残りを流す。口座に5時間の上限があるので、枠の終わりを見て区切る。

- 束は `uv run python tools/make_packet.py <id> …` で作り直してから流す（型の必ず持つものの節 1b を含む）
- バッチの終わりにメインがすること：数値の提案（pages/<id>/facts-proposal.yml）と共有のファイルへの提案をまとめて反映、生成、check_all（描画を含む）、使用量の集計、commit と push
- 公開：書いたページは draft のまま、下書きの印付きで公開する。工程7の試作と測定のページ（tools/gen/config.yml の held_back）は、最初のバッチの終わりに held_back から外して一緒に公開する（作者の承認は 2026-11-05 に出た）

## バッチ1（20ページ。2026-11-05）

| ページ | 型 | 分野 |
| --- | --- | --- |
| four-principles | guide | start |
| six-causes | guide | start |
| reverse-index | hub | start |
| tokens | concept | basics |
| context-rot | concept | basics |
| sycophancy | concept | basics |
| why-hallucinations | concept | basics |
| brief-a-new-colleague | concept | prompting |
| define-done | concept | verify |
| evidence-not-reports | concept | verify |
| hooks-basics | feature | enforce |
| permission-rules | feature | enforce |
| what-to-put-in-claude-md | feature | extend |
| fact-checking | recipe | verify |
| handoff-documents | recipe | context |
| where-to-put-instructions | comparison | app |
| over-reliance | judgment | judgment |
| claims-done-but-isnt | symptom | symptoms |
| replies-in-english | symptom | symptoms |
| not-what-i-meant | symptom | symptoms |

結果（2026-11-05）：40人・エラー0・約6.5分（同時に16人）。1ページあたり、読み直し約106万・書き込み約12万・出力約2.0万トークン、道具の呼び出し約24回（v3 の測りの約1.2倍）。全体で読み直し約2,130万トークン。ページの検査はエラー0（警告は残るページあり。下書きでは止めない）、写しの描画の検査は56ページでエラー0・警告0。バッチの終わりの扱いは [rules.md](rules.md)、後でまとめるものは [backlog.md](backlog.md)。直しは BF1、束の道具の直し（生成の目印を束に載せる）は PK3

## 残りの段取り

- 残り104ページを、52ページずつ2つのバッチに分ける（5時間の枠の終わりを見て区切る）。束は PK3 の後に作り直す
- バッチの終わりは、報告の「メインに判断してほしいこと」と「提案」を道具で1つのファイルに抜き出し、担当が rules.md の先例で当てる。先例に合わないものだけをメインが決める
- 第一波の終わりまでに：数値の提案を data に入れて目印を置く（backlog.md）、鮮度の点検の skill（design §9.4 の手順の1・2・5）を仕上げる（design §10.1 の8a）
