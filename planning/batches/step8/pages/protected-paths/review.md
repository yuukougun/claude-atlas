# review.md：protected-paths（feature・enforce）

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #outside-working-directory のタブ | 「（提案済み）」は読者に意味がなく、採用後は古くなる | 「手元の版で使えるかは、公式の変更履歴で確かめる」に置き換えた |
| 2 | 直したほうがよい | #protected の保護の説明 | 「担当の Claude」が何を指すか不明 | 「Claude が黙って書き換えにくくなる」に直した |
| 3 | 直したほうがよい | #critical-rm | 「最後の形」「この仕組みが先に働く」が断片で指すものが曖昧 | 「変数が付いた形」「この節の検査が先に働くからである」に直した |
| 4 | 軽い | 判断例（.claude） | 迷う候補の 2 つ目が弱い | 直さない |
| U6 | 問題なし | 全体 | 強制力のバッジ（冒頭）・tracks・level・使いどころ #when・最小の使い方（タブ）#outside-working-directory・雛形 #templates・落とし穴 #pitfalls・比べる相手 #compare が write.md の対応と本文で合う。古くなった助言は台帳の行がなく省略で妥当 | なし |

## 検査の結果
- check_page.py 1回：エラー 0・警告 5（長い題名の link 展開による文の長さと助詞の重複。本文の文は短く誤検出として残した）
- stage は直したので draft のまま

## メインに判断してほしいこと
- facts.yml に block-writes-outside-min-version がまだない。採用後に、タブの版の文を fact の目印に置き換えたい（write.md の提案どおり）

## 使用量
- 道具の呼び出し：約 8 回。Web の取得：0 回
