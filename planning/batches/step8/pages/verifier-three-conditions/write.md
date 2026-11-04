# write.md：verifier-three-conditions

## 書いたファイル
- `docs/eval/verifier-three-conditions.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections に why・audit・what-it-prevents・misconceptions を足し、sources に既存の 11 件の id を入れた。ほかのキーは変えていない）
- `snippets/verifier-three-conditions/audit-request.md` と `.expect.yaml`（目次の templates は無いが、点検の依頼の雛形を足した）
- `data/sources.d/` は新規なし（使った出典はすべて data/sources.yml にある）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 確かめる・縛る／prevents 確かめていない・縛っていない）：`#what-it-prevents`（pitfalls は空なので名指しなし）
- level（任せる）・要点の最初は「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#why`・`#correct`・`#tamper-proof`・`#representative`（例と理由）→`#audit`→`#what-it-prevents`→`#misconceptions`→関連はテンプレート

## メインに判断してほしいこと
- 「想定の場面」（CSV 変換の判断例）は束に根拠がない業務の例。事実の主張ではなく想定として書いた。実例が要るなら別途探す
- 図は置いていない（図の案なし）

## 提案
- なし（front matter・用語集・数値の提案はなし）

## 検査の結果
- 1 回目：エラー 1（`hooks` の表記。フックに直した）・警告 11
- 2 回目：エラー 0・警告 5（no-doubled-joshi 4・sentence-length 1。link の間に入る相手の題名が長いことによる分が多く、文の中身は短くした）

## 確かめていないこと
- 本文の事実は束の写しだけに基づき、一次資料は開いていない（Web の取得 0 回）。数値（42% から 95%・79% 超・約 50%・70% 超・85% 超・約 20 チーム）は束の写しと調査資料の注記の訂正に従った
- Battlecode 2025 の 2 件の「準優勝」「優勝」の対応、2026 の事例は束の行の要約のみ。p34#16（初期の 3 マップへの値のハードコード）は出典の id が束にないため載せず、rewrote-tests-to-pass へのリンクで足りるとした
- 雛形の動作は確かめていない。リンク先のうち「準備中」の節は公開前
- 「節目ごとに取り直す」は推論として（推論・実践例なし）を付けた

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0
