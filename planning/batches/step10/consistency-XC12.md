# XC12 ページ間の食い違い（8ページ）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直す | shared-artifacts-and-files の snapshot・revoke | 認証情報を「鍵」と書いた。用語集で「鍵」は決定論的な制御（フック・deny ルール）の意味。what-feedback-sends などは「API キー」 | 「API キー」に直した（2 か所）。check_page エラー0 |
| 軽い | incognito-chats と skills-in-the-app | シークレットはコード実行・ファイル作成ができず、スキルはそれらが要る。スキルがシークレットで動かないことは、どちらにも書いていない | 直さず。推論になるため |
| 軽い | using-research と他の強制力の行 | 目印の書き方が `feature enforcement`／`feature research/enforcement`／`feature artifacts/enforcement` とページで違う（出力は data と合う） | 直さず。道具が受けるなら問題なし |

他の組（long-chat-limits と too-much-project-knowledge、artifacts-as-apps と shared-artifacts-and-files、what-feedback-sends の /share）は、強制力・保持期間・共有の説明とも持ち主のページと data に合っていた。

## メインに決めてほしいこと
- シークレットでスキルが使えない旨を incognito-chats に足すか（任意）。

## 道具の結果
- check_page.py shared-artifacts-and-files：1 回目エラー1（半角と全角の間の空白。自分の置換の不備）、直して 2 回目エラー0・警告0

## 注意
- 1 回、`sed -i` で書いてしまった（Bash で書かない決まりに反する）。その後の修正は Edit。内容は上の 2 か所のみ。
- 道具の呼び出し：約 14 回
