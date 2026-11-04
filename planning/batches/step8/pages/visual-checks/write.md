# write.md：visual-checks（feature・verify）

## 書いたファイル
- docs/verify/visual-checks.md（stubs から mv。stage を draft、updated 2026-11-05）
- snippets/visual-checks/as-a-user.md・.expect.yaml、compare-with-mock.md・.expect.yaml
- front matter の変更：sections を 2 から 6 に（使いどころ・依頼の雛形・効かない場面と落とし穴・比べる相手を足した。既存の anchor は不変）、sources を 7 件（既存の id だけ）。data/sources.d は足していない

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点「強制力」（`feature verify-skill/enforcement`）と、#as-a-user の成熟度（`feature claude-in-chrome/maturity`・`verify-skill/maturity`）。バッジの列はテンプレートが出す
- tracks（claude-in-chrome・verify-skill）：front matter。本文は #as-a-user のタブで両方を扱う
- level（任せる）：front matter。根拠は #when の「任せる幅が広いほど…」
- 構成の目安：使いどころ #when → 最小の使い方（面のタブ）#as-a-user → #screenshots → 雛形 #templates → 効かない場面 #limits → 比べる相手 #compare → 古くなった助言（台帳に行なし。#compare の末尾に一言）

## メインに判断してほしいこと
- 要点の「強制力」の目印が「—」（data の verify-skill の enforcement が null）になる。本文は「値は数値ファイルの登録待ち」と書いた。data への追記後に、この括弧を外してほしい

## 提案
```yaml
proposals:
  - feature_attribute: {id: verify-skill, key: enforcement, value: お願い}   # 値の案。出典 cc-docs-skills で確かめてから
    used_in: [visual-checks#top]
```

## 検査の結果
- check_page.py を 2 回。エラー 0、警告 1（no-doubled-joshi・「に」。#limits の手動専用の項ではなく、161 行付近の 1 文。誤検出ではないが、意味が変わるので残した）

## 確かめていないこと
- 雛形 2 つの動作（未実行）。Claude in Chrome とブラウザ自動操作の道具の組み合わせでの動き
- Playwright の成熟度と確認日（名前を出すだけにした。推薦はしていない）
- Windows・macOS・IDE の拡張での動き
- 「Anthropic のハーネス」の事例は Web で 1 回確かめた（anthropic-eng-effective-harnesses-long-running）。ページの文は束の材料と合わせて自分で書いた

## 使用量
- 道具の呼び出し 14 回ほど、Web の取得 1 回
