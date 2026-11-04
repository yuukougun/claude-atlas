# review.md：documents-in-japanese（検証と直し）

## 指摘

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #keigo 末尾 | 「台帳」が未定義の語で、何と照らすのか読者に通じない | 「名刺や連絡先の記録」に直した |
| 2 | 軽い | #pdf の Claude Code の段落 | 「テキストへ変換する手」が漠然としている（道具は扱わない旨は明記済み） | 直さない。範囲外と明記されており、#failure でも同じ確かめに戻る |
| 3 | 軽い | 面のタブなし | surfaces は 3 面だが手順は面に共通 | 直さない。write.md の判断どおり。面ごとの差は how-attachments-are-read へ任せている |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う。手順は #pdf・#keigo・#glossary、確かめる・縛るへの道は prerequisites と related と #guard・#verify・#failure、level は整える、構成は目安どおり | なし |

U1〜U5・U8・U9 は問題なし（要点は summary と一致、判断例は 4 行で候補が両立、各節は単独で通じる）。

## 検査の結果

- `check_page.py` を直した後に 1 回流した。エラー 0・警告 2（no-doubled-joshi、144 行と 182 行）。どちらも link の目印の間に道具が書いた題名の「に」で、誤検出と見る

## メインに判断してほしいこと

- stage は draft のまま（直しを入れたため）。sources が空なので、出典を足すかは write.md の判断を参照

## 使用量

- 道具の呼び出し：Read 5、Edit 1、Bash 1、Write 1。Web の取得：0
