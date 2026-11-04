# knowledge-map 執筆の報告

## 書いたファイル
- docs/start/knowledge-map.md（stubs から mv。front matter は sections を 3 つ足し、stage を draft、updated を 2026-11-05 に）
- 雛形・図・出典のファイルはなし（目次の templates がなく、出典 0 件）

## 必ず持つものの対応
- 表とリンクが本体：#graph（`graph` の目印。道具が書く表と図）、#choose（ほかの地図へのリンクの表）
- level なし・sources 任意：持たない（hub は level を持たない。sources は 0 件）

## メインに判断してほしいこと
- #how-to-read の「分野ごとの表示」「祖先と子孫だけの表示」は design §8.5 の方式を書いた。JS の実装がこの 2 つの表示を出すかは未確認。実装が違うなら書き直す。
- #how-to-read の「載せるのは下書き以上の段階だけ」は目次の notes（DR-01）に基づく。

## 提案
なし

## 検査の結果
- check_page.py knowledge-map：エラー 0・警告 0（1 回）

## 確かめていないこと
- graph の目印の中身（生成後の図の見え方・JS の動作）は見ていない。
- 導入の「手で書いた表はない」は、目印の外に表がないことで確かめただけ。
- #choose の表の文言（引くページの案内）は、束の要約だけに基づく。

## 使用量
- 道具の呼び出し：約 7 回。Web の取得：0 回
