# バッチ3：メインが決めること

先例（rules.md）に当たらないものだけ。推す案を先に書く。

| ページ｜件｜案 |
| --- |
| humans-set-the-parallel-limit｜「まず 1〜3 本から」の推奨と実践者の本数（自己申告）を載せた。公開の勧めに当たるか｜（推論・実践例なし）の印があるので残す。作者が「勧めの文」と見るなら「実践者は1〜4本ほどと報告する」に弱める |
| choosing-parallel-modes｜「1〜2 割は捨てる」「3〜4 本ほど」を自己申告・根拠：弱で載せた｜残す。数値の目印にはしない（個人の構成で、標準ではない） |
| vetting-extensions｜判断例の「選んだもの」が個人の好みに見えないか／mods・plugin の「確認を重くする」の線引き（この辞典の推奨で根拠の印なし）｜線引きに（この辞典の推奨）の印を足して残す。判断例は理由が読めれば残す |
| lethal-trifecta｜アプリの二条件の読み（条件1＝A、条件2＝C、B は数えない）｜（推論・実践例なし）と書いてあるので残す |
| five-questions-before-delegating｜「外部記憶」を「会話が圧縮されても残る記録」と読み替え。4段の分け方の出典 id がない｜（根拠：弱）のまま残す。出典 id が見つかれば足す |
| goal-until-done｜雛形 run-unattended の --max-turns・--max-budget-usd の効き方が未確認（台帳に基づく）｜台帳の記述どおりと注記して残し、動作確認の担当に回す |
| what-not-to-delegate｜AtCoder World Tour Finals 2026 の箇条は報道の題名ベース。人名は出していない｜research/25 P1 の注記（OpenAI のモデルが人間の上位勢を上回ったと報じられた。Psyho は不参加）と食い違わないので残す。「考察の出どころが AI であることは、すでに起こりうる」だけ「起こりうる」を残し断定しない |
| human-pitfalls・learning-with-ai｜研究の割合・件数の手書き（研究名・年・対象つき）｜先例どおり手書きのまま（済） |
| decide-when-to-quit｜判断例1の理由がやや込み入る｜簡素化は読者の反応を見てから。今は直さない |
| unexpected-memories｜症状「会話を消したのに覚えている」の人向けに項目5を先頭近くへ動かすか｜動かさない（順は原因の安さの順）。入口は症状のページの要点で足りる |
| fix-a-bug｜when-stuck の表を routes にするか｜手書きのまま。routes の変更は front matter の提案として backlog |
| refused-or-blocked｜「人の側の落とし穴」を言い換えて通そうとする癖の1段落で足すか、pitfalls に追加するか｜1段落のまま。pitfalls の追加は作者の判断 |
| 診断の先頭・末尾に原因の外の項目を足したページ（hits-limits-quickly の「長さの上限との取り違え」「枠の側」・too-slow の障害・混雑・blames-the-tools の「人が自分で実行する」）｜一番安い確認なので残す。型の手引きの「六つの原因を安く確かめる順」に原因の外の項目を認めるかは作者が決める |
| learning-with-ai｜題と要点の「速く進む」を弱めた（TR3 が直した）｜済。catalog の sections の題を同期する（backlog） |

## メインの決め（2026-11-05）

- 直す（FX）：vetting-extensions の線引きに（この辞典の推奨）の印を足す。what-not-to-delegate の大会の箇条を断定しない形にする
- 手引き：症状のページの診断の最初か最後に、原因の外の、いちばん安い確認を1項目まで置いてよい（symptom.md §2・card §11 に足した。FX が確かめる）
- そのまま（直さない）：humans-set-the-parallel-limit（推論の印つきの推奨。この辞典の推奨の範囲で、公開の約束ではない）・choosing-parallel-modes・lethal-trifecta・five-questions-before-delegating・goal-until-done（雛形は動作を確かめていない注記のまま）・human-pitfalls・learning-with-ai・decide-when-to-quit・unexpected-memories・fix-a-bug（routes の案は backlog）・refused-or-blocked（pitfalls の追加はしない）
- learning-with-ai の目次の節の題の同期は要らない（骨格の後は front matter が正。目次は凍結。design §5.2 の5）
