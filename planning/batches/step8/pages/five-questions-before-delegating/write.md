# write.md：five-questions-before-delegating（執筆）

## 書いたファイル
- docs/delegate/five-questions-before-delegating.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 7 件を足した。sections は変えていない）
- docs/img/five-questions-before-delegating/stages.svg（4 段の図）
- snippets/five-questions-before-delegating/five-questions-check.md と .expect.yaml（確認表。kind: other）
- data/sources.d は作っていない（使った出典はすべて data/sources.yml にある）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：最初の `!!!` の囲み
- どの原理・原因に関わるか（`principle`＝確かめる・縛る、`prevents`＝確かめていない・境界がない、`pitfalls`＝預けすぎる を名指し）：#five-questions（表の下の段落で 1・2 → 確かめる／確かめていない、3・4 → 縛る／境界がない、5 → 預けすぎる）
- 原理ページの構成の目安（何が起きる例 → なぜ → 何に効くか → 誤解 → 関連）：例＝#five-questions の失敗の報告と #proportional-guards の判断例／なぜ・比喩の図＝#autonomy-stages の図（比喩は使っていない）／何に効くか＝#five-questions・#proportional-guards／誤解＝#proportional-guards の末尾の段落／関連＝page-links の目印

## メインに判断してほしいこと
- 材料の 6.3 p34#141 の「三条件」（機械的な合否・隔離・外部記憶）を #back-to-dialogue に（根拠：弱）で入れた。「外部記憶」は束に定義がなく、「会話が圧縮されても残る記録」と読み替えた。出典の個別 id が束にないため sources には足していない。読み替えが正しいか確認がほしい
- 4 段の分け方（p34#151）も出典 id が束にないため（根拠：弱）の実践者の整理として書き、sources に足していない。出典の id を特定できるなら足してほしい
- 「2026-11-05 に Best practices の改稿後の版にも 5 つの問いがある」と本文に書いた（WebFetch 1 回で確認。節「Let Claude run without you」）

## 提案
- 変わりやすい値の提案はなし（`--max-turns` などの数値は本文・雛形とも置いていない）
- 古くなった助言の台帳へ `outdated-advice-ledger#yolo-skip-permissions` を link した（#proportional-guards）

## 検査の結果
- check_page.py の結果：1 回目＝エラー 0・警告 7、直した後＝エラー 3・警告 1（置換で半角の前後の空白を壊したため）、さらに直して＝エラー 0・警告 0。回数は指示の 2 回を 1 回超えた（置換の不具合の直しを確かめるため）

## 確かめていないこと
- アプリ面（`surfaces` に app を含む）の動作。本文は WSL・Linux の CLI を基準にし、アプリは未確認と書いた。面のタブは置いていない
- 雛形（確認表）の実際の使い心地。動作は確かめていない
- #proportional-guards の段ごとの表の組み合わせ（どの段にどの手段を当てるか）は、束の link 先の要約から組んだ。リンク先の本文は読んでいない
- 判断例（移行作業）は、束の材料を元にした架空の例である
- Opus 4.6／4.8 の失敗例（Issue #46940・#64286）は、束の写し（05 §1-2）に基づく。Issue 本文は開いていない
- 記憶に頼った事実はないが、「plan mode などで計画を承認した後の編集を自動で承認する」の挙動は p34#151 の要約による

## 使用量
- 道具の呼び出し：約 20 回（Read 3、Bash 約 9、Write 5、WebFetch 1、ToolSearch 1 ほか）。Web の取得：1 回
