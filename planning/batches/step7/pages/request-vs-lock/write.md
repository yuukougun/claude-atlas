# 報告：執筆（request-vs-lock）

- 手引きの版：共通 2026-11-04 第1版・型（concept）2026-11-04 第1版

## 1. 書いたファイル

- docs/basics/request-vs-lock.md（stubs から mv）。front matter は sections（6 節：what-happens・why・sorting・two-layers・effects・misconceptions）・sources（6 件）・stage（stub → draft）だけを変えた。updated は元から 2026-11-04
- docs/img/request-vs-lock/two-layers.svg（catalog の visual 案どおりの静的な図「お願いと鍵の二層」）
- snippets/request-vs-lock/lock-settings.json と .expect.yaml（deny ルール。safety: true）、request-claude-md.md と .expect.yaml（CLAUDE.md の例）。catalog の templates は「なし」だったが、二層の書き方を見せるために足した
- data/sources.d/ は作っていない（使った出典 6 件はすべて data/sources.yml にある）

## 5. メインに判断してほしいこと

1. **台帳の anchor**：gen の ledger は台帳の行ごとに `{#<台帳の id>}` の見出しを置き、ほかのページは `outdated-advice-ledger#<id>` で指す設計だが、台帳ページの sections は how-to-read・workarounds・ledger・find-in-your-setup だけで、`#important-caps` で指すと check_pages「link の目印」が止まる。このページは anchor なし（`outdated-advice-ledger`）で指した。台帳ページの sections に行の anchor を足すか、検査が台帳の id を許すかを決めてほしい
2. **link の目印の題名が textlint に当たる**：目印の間に入る題名は本文として検査され、four-principles#lock の題名「四つの原理と比例則…」の「四つ」が arabic-kanji-numbers の警告になる。このページでは本文のリンクを外し、textlint の外にある「関連」の欄に任せた。題名を「4 つの…」にするか、「四つの原理」を例外にするか決めてほしい
3. **面のタブを置かなかった**：手引き §6 は面ごとに手段が違う話をタブで並べると定めるが、このページは面ごとの手段を書かず、request-lock-table に任せた（本文は「どの面でもプロンプトの指示はお願い」「鍵は面で違う」だけ）。タブが要るなら案を出してほしい
4. **お願いの雛形の expect**：CLAUDE.md の例は「この操作が止められる」の形にならない。result を自由文にし「お願いなので毎回とは限らない」と添えた。形を決めてほしい（check_templates は中の形を見ない）
5. **使わなかった材料**：11 p56#11（迎合のページに回すもの）、00 §1 のアプリ側の置き場所の切り分けと research/27 §3.2 の「面によって届く設定が違う」（where-instructions-sit と request-lock-table の持ち分）、公式ブログ Steering Claude Code（Best practices で足りるため開かず）、issue #99704 のモデル別の割合（自己申告で、モデルごとの癖は §9・§14 に沿って本文に入れない）

## 6. 提案

```yaml
frontmatter: []
```

- 用語集：ハーネス｜モデルのまわりでツールを動かし、モデルが見る文脈を管理する層。Claude Code 本体がこれにあたる。（anchor 案：harness。すでにあれば不要）
- 用語集：お願い・鍵｜お願いは Claude が読んで判断する指示（非決定論的な指示）。鍵は Claude の判断によらずハーネスが実行する制御（決定論的な制御）。（anchor 案：request-lock。すでにあれば不要）
- catalog（basics.yaml の request-vs-lock）：templates を「なし」から lock-settings・request-claude-md の 2 つに
- 数値の提案：なし（facts-proposal.yml は作っていない。変わりやすい値は本文に書いていない）

## 7. 検査の結果

- gen_site.py --page request-vs-lock：成功。check_pages.py --page：エラー 0・警告 0（途中の link の目印のエラー 1 件は 5-1 のとおり anchor なしにして解消）
- check_templates.py --page：エラー 0・警告 0。check_svg.py --page：エラー 0・警告 0
- textlint（このページ）：0 件。初回はエラー 6・警告 19 で、用語（auto モード・権限モード・サンドボックス）・数の書き方（3 つ）・助詞の重なり・長い一文を直した。`npm run lint:text` に自分のページの指摘はない
- SVG は headless Chrome で PNG にして目で確かめた（400px）。render_pages（幅 390px のライト・ダーク）は流していない

## 8. 確かめていないこと

- 雛形の動作（deny ルールが実機で止まるか、CLAUDE.md の例の効き目）。check_templates は静的な検査だけ。本文の動作の記述は公式の文書によるもので、WSL・Linux の CLI を含め実機では動かしていない
- アプリと API で鍵に当たる仕組み。調べていない
- issue は #96326・#99704 を開いたが、#98633 は題名と束の要約だけで読んでいない。「毎ターンフックで足しても英語に戻った」は #96326 のコメントの報告で、根拠は弱とした
- hooks reference と sandboxing の文書は開いていない。「種類は設定の `type` で確かめる」は Best practices の例（`"type": "command"`）から、strict mode と再試行の記述は Best practices と permissions から書いた
- 公式の主張は Best practices・permissions・memory・how-claude-code-works を今の版で取り直し、束の記述と食い違わなかった。Wayback の写し（改稿前後の版）は台帳の持ち分として開いていない

## 9. 使用量

- 道具の呼び出し 約 65 回。Web の取得 6 回（公式の文書 4・GitHub の issue 2）、ToolSearch 1 回を含む。かかった時間は計っていない
