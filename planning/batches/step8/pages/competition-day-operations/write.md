# write.md：competition-day-operations（recipe・contest）

## 書いたファイル
- `docs/contest/competition-day-operations.md`（stubs から移した。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（guards・overall-check・when-it-fails の 3 節を足した。既存 6 節の anchor は変えず）、`sources`（7 件。いずれも data/sources.yml にある id）、`stage`、`updated`
- `docs/img/competition-day-operations/timeline.svg`（本番の時間線の図）
- `snippets/competition-day-operations/day-runbook.md`・`.expect.yaml`（本番の手順表。目次の templates の案）
- `snippets/competition-day-operations/opening-request.md`・`.expect.yaml`（開始直後に評価器を先に出させる依頼。足した雛形）
- `data/sources.d/competition-day-operations.yml` は作っていない（新しい出典がないため）

## 必ず持つものの対応
- 手順：`#day-before`・`#opening`・`#midgame`・`#endgame`・`#submission`・`#fallback`（各段に「終わりの確かめ」）
- 確かめる・縛るのページへの道（比例則）：`#guards`（evaluators-by-format・verification-ladder・freeze-eval-assets・permission-rules・competition-rules・decide-when-to-quit）。front matter の prerequisites と related にも enforce・safety・verify のページがある
- 構成の目安の順：要点 → 守り `#guards` → 手順 → 確かめ方 `#overall-check` → 失敗したとき `#when-it-fails`（症状ページへの振り分け）
- level：任せる（front matter のまま）

## メインに判断してほしいこと
- 書かなかったもの：長期 AHC の部門選択の期限の話（未確認 A-3）、Universal Cup のプロンプトインジェクション禁止（工程2で未確認）、2026-08-16 の障害の日付と長さ（未確認。出典の bleepingcomputer.com は noai の記録）、「最も安い保険」（「保険として有効」にとどめた）、本番 1 か月前などの数値（「出典のない例」と文で触れただけ）、模擬本番の演習
- ISUCON13 の初参加チームの準備（3.5 時間）と DEF CON 33 の講演は、sources.yml に id がないため引かなかった。使うなら出典 id の追加が要る
- 「終了の 1〜2 時間前」の数値は本文に書かず、凍結の時刻は前日に決める形にした

## 提案
```yaml
frontmatter: []
```
- 用語集：「評価器」（点や正しさを提出の前に自分で測る道具）を本文で短く定義した。用語集に既にあるか確認を
- facts の提案はなし（変わりやすい値は本文に書いていない。CTF の順位は研究の時点の記録として、名・年・対象を添えて書いた）

## 検査の結果
- `check_page.py` を 2 回流した。最後は エラー 0・警告 5
- 残した警告：sentence-length 2 件（71・113 行。リンクの目印の間に入る題名が文字数に入るため）、no-doubled-joshi の「に」3 件（71・77・153 行。リンクの題名が入った後の文で、分けると読みにくくなる）

## 確かめていないこと
- 事実は束の写しに基づく。一次資料を開いていない（Web の取得 0 回）。Anthropic の CTF の数字（32 分・22 位・161 チーム・AI 8 チーム）は束の research/24 B-57 の写しによる
- 2 つの雛形は動かしていない。Claude Code の WSL 以外の OS と、アプリ・IDE 拡張での動きは確かめていない
- 手順の「間隔」「時刻」は例を置かず、読者が決める形にした。実際の大会でその運用が回るかは試していない
- 全体は事例からの推論である旨を冒頭に書いた

## 使用量
- 道具の呼び出し：約 19 回（Read 2、Bash 8、Write 8、Edit 6 を含む）。Web の取得：0 回
