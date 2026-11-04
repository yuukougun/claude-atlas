# write.md：shared-artifacts-and-files

## 書いたファイル
- `docs/safety/shared-artifacts-and-files.md`（stubs から mv。stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：`sections`（`what-it-prevents` を末尾に足した）、`sources`（hc-share-chats・hc-share-people・hc-share-public・hc-files・hc-connectors・hc-artifacts。いずれも data/sources.yml にある）、`stage`、`updated`
- 雛形・図・sources.d は置かない（目次の templates と visual が「なし」。新しい出典もなし）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle` 握る・`prevents` 境界がない）：`#what-it-prevents`
- 要点の最初の項目が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか → 仕組み → 何に効くか → 誤解 → 関連）：何が起きるか・仕組み＝`#how-to-share`・`#snapshot`・`#who-can-see`・`#revoke`、他人の公開物＝`#opening-others`、何に効くか＝`#what-it-prevents`。誤解の節は置かず、`/share` の取り違えを `#how-to-share` の Claude Code タブに書いた（薄い節を作らないため）。比喩付きの図は、図の案がなく省いた
- `pitfalls` は空のため、名指す対象なし

## メインに判断してほしいこと
- プラン名（Free・Pro・Max・Ultra・Team・Enterprise）と、招待の期限・1 日の上限の数は、本文に手で書かず「個人向けのプラン」「組織向けのプラン」「一定の期間」と書いた。数値の目印は、提案の id が data にまだないため置いていない。facts に入れたら `#who-can-see` に目印を置く
- 競技中の守り（private のリポジトリ・共有リンクの無効化・公開ページへの出力の禁止）を `#revoke` の末尾に（類推）の印で短く書いた。材料は research/11 の表の 1 行のみで、強さの印が弱い。残すかの判断を頼む

## 提案
```yaml
proposals:
  - fact: {id: chat-sharing-plans, title: 会話の共有のしかたとプランの対応（招待は全プラン、公開リンクは個人向けのプラン、組織向けのプランは組織の中だけ）, value: "招待：Free・Pro・Max・Ultra・Team・Enterprise／公開リンク：Free・Pro・Max・Ultra／組織の中だけ：Team・Enterprise", sources: [hc-share-chats, hc-share-people, hc-share-public], checked: 2026-11-04, status: 確認済み}
    used_in: [shared-artifacts-and-files#who-can-see]
  - fact: {id: chat-sharing-invite-expiry, title: 開かれない招待が切れるまでの期間と、1 日に招待できる人数の上限, value: "期間：30 日（上限の人数は材料にない）", sources: [hc-share-people], checked: 2026-11-04, status: 要確認}
    used_in: [shared-artifacts-and-files#who-can-see]
  - fact: {id: chat-sharing-file-limit, title: コード実行で作ったファイルを含む会話を公開リンクで共有できないプラン, value: "Free・Pro・Max・Ultra", sources: [hc-share-chats, hc-files], checked: 2026-11-04, status: 確認済み}
    used_in: [shared-artifacts-and-files#who-can-see]
```
- data の提案：features の `chat-sharing` の `since` が未確認。tracks の `chat-sharing` はすでにある。`artifacts-overview` への `used_in` は不要
- 用語集：「写し（snapshot）」を、共有した時点の内容の複製の意味で入れる案

## 検査の結果
- `check_page.py` を 2 回流した。エラー 0・警告 0

## 確かめていないこと
- 共有の画面の名前と操作の手順（材料の英語の名前を本文に書かず、一般の言い方にした）。実際の画面は見ていない
- Claude Code の `Artifact` ツールの公開の条件（組織向けのプランで管理者が許可したとき）は research/26 §3.2 の 1 行からで、一次資料を開いていない
- 招待の期限・上限の数は research/26 の写しのみ。一次資料を開いていない
- 競技中の守りの根拠は research/11 の表の 1 行のみ
- 本文を雛形・図なしで書いたため、動作の確認はしていない

## 使用量
- 道具の呼び出し：約 12。Web の取得：0
