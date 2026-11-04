# write.md：skill-descriptions（feature・extend）

## 書いたファイル

- `docs/extend/skill-descriptions.md`（stubs から移した。stage は draft）。front matter で変えたキー：`sections`（8 節を足した）・`sources`（cc-docs-skills・cc-docs-features-overview・hc-skills-use・api-docs-skill-best-practices。いずれも既存の id）・`stage`・`updated`
- `snippets/skill-descriptions/`：description-before（.md）・description-after（.md）・trigger-check（.txt）と、それぞれの `.expect.yaml`
- `data/sources.d/skill-descriptions.yml` は作っていない（新しい出典がないため）

## 必ず持つものの対応

- 機能の属性のバッジ（強制力・読み込みの時期など）：冒頭の要点の「強制力」（`feature enforcement`）、`#purpose` の `feature load_timing`。バッジの列はテンプレートが出す
- `tracks`（skills）：front matter。本文では `#purpose`・`#limits` で機能の属性を指す
- 1機能1ページ・公式リファレンスの網羅をしない：全体（frontmatter の全キーは載せず、description に絞った）
- level（仕組みにする）：front matter
- 構成の目安（要点→使いどころ→最小の使い方→雛形→効かない場面→比べる相手→古くなった助言）：`#purpose`（使いどころ・防ぐ原因）→`#usage`（面のタブ）→`#front-load`（雛形 before/after）→`#overlap`（判断例）→`#check`（雛形 trigger-check）→`#limits`→`#compare`→`#old-advice`

## メインに判断してほしいこと

- 台帳の行はなく、古くなった助言は薄い（`#old-advice` は「記事によって上限の字数が違う」の読み替えだけ）。節ごと削るなら、sections からも外す
- 「実践者の間では成否は説明文でほぼ決まるとよく言われる」を（根拠：弱）で 1 文だけ残した。数（9割）は書いていない。要らなければ `#purpose` の最後の 1 文を削る

## 提案

```yaml
frontmatter:
  - {id: skill-descriptions, key: related, before: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents], after: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents, skills-in-the-app, hook-vs-skill, instructions-ignored], reason: "本文で指している。本文が指すページは related に入れたい"}
glossary:
  - {term: description（スキルの説明文）, definition: "スキルの SKILL.md のフロントマターにあり、Claude がそのスキルを読み込むかを決める手がかりになる文。名前とともに毎回の会話に載る", reason: "ほかのページ（writing-skills・writing-subagents）でも使う語"}
```

数値の提案はない（既存の `skill-listing-entry-max-chars`・`skill-description-max-chars`・`skill-listing-budget-fraction` を目印で指した）。

## 検査の結果

- 書き終えた後：エラー 0・警告 5（助詞の重複 4、目印の外の数値 1）
- 直した後：エラー 0・警告 2（`#limits` と `#compare` の箇条の見出しの語で助詞が重なる）。その後、2 つの見出し語を手で直したが、検査は規定の 2 回を使い切ったので再実行していない。警告が残る可能性がある
- 2 回目の直しは、Write でなく Bash（python と sed）で行った。本文の細かい直しだったため

## 確かめていないこと

- `/skills` のメニューにスキルの一覧とオン・オフがあること（writing-skills の本文から写した。公式で再確認していない）
- `when_to_use` と `description` の使い分けの詳細（束の材料は「合計で切り詰め」まで。どちらにも主な用途を先頭に、とだけ書いた）
- `skillOverrides` の値（on・name-only・user-invocable-only・off）の意味。プラグインのスキルに効かないことは writing-skills の記述に合わせた
- アプリで ZIP を上げ直す手順と設定画面の名前（2026-11-03 の展開で変わりつつある。skills-in-the-app に任せた）
- 3 つの雛形の動作（どれも新しいセッションで試していない。expect は観察として書いた）
- 他の OS・IDE 拡張の動作は未確認

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：0 回
