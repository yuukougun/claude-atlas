# incognito-chats 執筆報告

## 書いたファイル

- docs/app/incognito-chats.md（stubs から mv。stage を draft、updated を 2026-11-05）
- front matter で変えたキー：`sections`（when・usage・compare を足した。retention・limits は残した）、`sources`（hc-incognito・hc-memory・hc-release-notes。いずれも既存の id）、`stage`、`updated`
- 雛形・図・data/sources.d は置いていない（目次の templates と visual が「なし」。置く必要のある雛形が思いつかなかった）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが tracks（incognito）から出す。本文には書いていない。ただし data に強制力の値がないため、要点の「強制力」は目印を使わず文で書いた（下の「メインに判断してほしいこと」）
- `tracks`：front matter の `incognito`（変更なし）
- 用途（使いどころと注意点）：#when（使いどころ）・#retention・#limits（注意点）
- 要点（強制力・確認日と版）：冒頭の要点の囲み
- 使いどころ（どの原因を防ぐか）：#when（境界がない・散らかっている）
- 最小の使い方（面のタブ）：#usage（`surfaces` が app だけなので「アプリ」のタブ 1 つ）
- 雛形（折りたたみ）：持たない。理由は上
- 効かない場面・落とし穴：#retention（それでも残るもの）・#limits
- 比べる相手：#compare（メモリの止め方・見直しとの表）
- 古くなった助言：持たない。data の台帳にこのページの行がない
- level：front matter の「整える」（変更なし）

## メインに判断してほしいこと

- 強制力：data の incognito 機能に enforcement の値がない。要点には「アプリの仕組みで、お願いではない。保持と管理者への見え方は止められない」と文で書いた。data に enforcement を足すなら、値の提案が要る（鍵のように見えるが、Help Center の記述からの読み取りで、値の語彙に当てはまるかは未確認）
- 「組織向けのプラン」「さらに上位のプラン」と、プラン名を伏せて書いた（プラン名は変わりやすい値のため）。名前を出すなら data に fact が要る

## 提案

```yaml
frontmatter: []
```

- data：incognito-retention-period（status: 未確認）を使った。Help Center（hc-incognito）を 1 回開いて、30 日の既定・Enterprise の扱いが記述と合うことは見たので、status を確認済みにする提案
- 用語集：monthly recap の訳を「月次のふり返り」とした。用語集にあれば合わせる

## 検査の結果

- 1 回目：エラー 0・警告 8。直した後：エラー 0・警告 3
- 残した警告 3（no-doubled-joshi「に」：34・35・50 行目）：front matter の signs「記憶や履歴に影響させずに試したい」の言い回しに合わせた文で、言い換えると意味が曖昧になるため残した

## 確かめていないこと

- Help Center の記述（2026-11-05 に 1 回取得）以外の一次資料は開いていない。モバイル・Desktop での使えるかは記事に記述がなく、本文では面を app とだけ書いた
- 画面の見た目（ゴーストのアイコン・黒い枠）は記事の記述の写しで、実機で確かめていない
- 「始めた時点で既存のメモリを使わない」は取得した記事の文による。プロフィールの設定が使えるという記述との境界は細かく確かめていない
- 最後の行の見出しの末尾の空白を直した後の再検査はしていない（回数の上限のため）
- 判断例は一般的な状況の例で、実在の事例ではない

## 使用量

- 道具の呼び出し：約 14 回、Web の取得：1 回
