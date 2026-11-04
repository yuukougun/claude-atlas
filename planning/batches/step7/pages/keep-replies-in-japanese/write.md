# 報告：執筆（keep-replies-in-japanese）

- 手引きの版：共通 2026-11-04 第1版・型（recipe）2026-11-04 第1版

## 1. 書いたファイル

- docs/japanese/keep-replies-in-japanese.md：stubs から mv。front matter は stage（stub→draft）と sources（空→15 件）だけ変えた。sections と updated は元のまま（updated は 2026-11-04）
- snippets/keep-replies-in-japanese/：user-settings.json・reply-language.md・require-japanese.py・hook-settings.json と、それぞれの .expect.yaml（8 ファイル）。目次の templates の 2 案（language の設定・Stop フック）に、CLAUDE.md の規則と Stop フックの登録を足した
- docs/img/keep-replies-in-japanese/turn-points.svg：目次の図の案（1 ターンの中で英語が出る場所と、届くフック）
- data/sources.d/keep-replies-in-japanese.yml：api-docs-multilingual-support を足した。cc-docs-cloud-environments は claude-md-vs-rules-skills-styles が同じ URL で先に足したので、足さずに id で指した（先の側が消えると指せなくなる。統合のときに data/sources.yml へ）
- planning/batches/step7/pages/keep-replies-in-japanese/write.md・facts-proposal.yml

## 5. メインに判断してほしいこと

1. 検証ノート（measure の節）に結果がない。方法（research/27 P12）と、結果を入れる空の表だけを書いた。回数の上限・試す環境・モデルと版の固定が決まったら、流して埋める
2. 手引き §9（モデルごとの癖は本文に手で書かない）と、目次の notes（特定のモデルで増えた報告を、根拠の強さと確認日を付けて本文に書く）が食い違う。facts が空で目印を置けないので、モデル名と版は本文に出さず「新しい世代のモデルで増えた（根拠：中）」とだけ書いた。名前を出すなら、facts に足して目印で書く
3. 雛形の expect.yaml は、道具が読む title・place・safety・features に、conditions・expect・control を足した私の案。形を決めてほしい
4. 雛形の「要る最低の版」は features の since から出るので、Stop フックの雛形に hooks の版が出る。実際は `last_assistant_message` が入った版以上が要る（版は未確認）。本文に断りを書いた。expect.yaml に最低の版を直接書ける項目があるとよい
5. 用語集がまだ節の題だけなので、語の初出の案内は「お願いと鍵」の request-vs-lock にした（用語集の節は指していない）
6. 道具の気づき：Write の content に `\uXXXX` と書くと文字に展開された（require-japanese.py の字の範囲は、文字そのもので書いた）。link の目印は「題名 › 節の題名（準備中）」を出すので、節を指す文が長くなる

## 6. 提案

```yaml
frontmatter:
  - {id: keep-replies-in-japanese, key: related, before: [replies-in-english, where-to-put-instructions, stop-hooks, output-style-modes, settings-layers, what-subagents-dont-inherit, what-survives-compaction, cloud-sessions-and-teleport, agent-loop, where-instructions-sit, hook-recipes, commit-and-comment-language, measure-changes], after: [replies-in-english, where-to-put-instructions, stop-hooks, output-style-modes, settings-layers, what-subagents-dont-inherit, what-survives-compaction, cloud-sessions-and-teleport, agent-loop, where-instructions-sit, hook-recipes, commit-and-comment-language, measure-changes, request-vs-lock], reason: "導入で「お願いと鍵」の説明先として指した。ページ下部の関連にも出したい（任意）"}
```

- tools/checks/template_keys.yml：`settings.top` に `language` を足す。根拠は All settings の `language`（Scope は Any file、値は言語名の文字列。2026-11-04 に読んだ）。ないので check_templates.py が user-settings.json でエラー 1 件を出す
- 用語集（definitions）：ターン＝依頼を送ってから最後の返事までの 1 区切り（途中でツールを何度も呼ぶ）。ツールの合間の一言＝Claude がツールを呼ぶ前後に書く短い文（最後の返事とは別で、Stop フックは見ない）。差し戻し＝フックが Claude に返事のやり直しを求め、ターンを終えさせないこと
- data/facts.yml：facts-proposal.yml の stop-hook-block-cap（Stop フックが続けて止められる回数の上限）。足したら、stop-hook の節の「続けて止められる回数に上限がある」の項目に fact の目印を置く

## 7. 検査の結果

- gen_site.py --page：目印を埋めた（エラー 0）
- check_pages.py --page：エラー 0・警告 0
- npx textlint（このページ）と npm run lint:text：0（最初に警告が 9 件あり、すべて直した）
- check_svg.py --page：0。headless Chrome で図を描いて目で見た
- check_templates.py --page：エラー 1（settings のキー。`language` が許す一覧にない。上の提案）。ほかは 0
- require-japanese.py：擬似の JSON を 12 ケース流して想定どおり（英語は差し戻し。日本語・短い返事・stop_hook_active・ALLOW_ENGLISH_REPLY・JSON の誤りは何も出さない）。実機の Claude Code では流していない

## 8. 確かめていないこと

- Stop フックの雛形と登録の実機の動作（差し戻しが起きるか、フックのエラーの表示）、`last_assistant_message` が入った版、SubagentStop に同じスクリプトを登録できること
- `language` で自動のセッションの題名が日本語になること（公式の記述に基づく目安）。`/status` の Setting sources と `/context` の Memory files も、公式の記述に基づく
- GitHub の issue は #96326・#99800・#101940 の 3 件だけ開いた。利用者が数えた割合は本文に使っていない。「新しい世代で増えた」は research/27 §3.3 による
- 開いた公式の文書：hooks・settings・settings-reference・memory・output-styles・sub-agents・cloud-environments・claude-code-on-the-web・cli-reference・Platform の多言語・Help Center の言語。context-window と CHANGELOG は開いていない（出力スタイルとフックが圧縮の後も効くことは、data の features の note による）
- macOS・Windows・IDE の拡張・デスクトップアプリでの動作。ページ全体の描画（幅 390px のライトとダーク。メインが流す）

## 9. 使用量

- 道具の呼び出し 約 120 回（Bash 約 55・WebFetch 18・Edit 17・Write 13・Read 10）、Web の取得 18 回、約 35 分
