# when-to-add-what 執筆報告

## 書いたファイル

- `docs/extend/when-to-add-what.md`（stub から移した。stage: draft、updated: 2026-11-05。front matter で変えたのは `sections`・`sources`・`stage`・`updated`）
- `snippets/when-to-add-what/sort-repeats.md` と `.expect.yaml`（目次の templates は「なし」。分かりやすさのために 1 つ足した：言い直したメモを移し先に仕分けさせる依頼）
- `sources` は既存の id だけ：cc-docs-features-overview・cc-docs-features-overview-ja・cc-docs-context-window・claude-blog-steering-code-skills-hooks。`data/sources.d/when-to-add-what.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 原理（見せる・縛る）を名指す：`#effects`
- 原因（見えていない・縛っていない）を名指す：`#effects`
- pitfalls：front matter が空なので持たない（理由：ページに対応する落とし穴の指定がない）
- level（任せる）を持つ：front matter。要点の最初は「何が分かるか」
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-happens`（例）・`#why`（なぜ。図は置かず、比喩も使っていない）・`#effects`・`#misconceptions`・関連はテンプレートが出す。足した節：`#triggers`（表）・`#noticing`（雛形）・`#costs`（compare）・`#examples`（判断例 3 件）

## メインに判断してほしいこと

- 図：目次の visual 案（繰り返しの種類と移す先を結ぶ static 図）は作っていない。`#triggers` の表で同じ内容を出している。図が要るなら別の担当に頼む
- 比喩を使っていない（`#why` に「広い机」を使える所はあるが、無理に入れなかった）
- `#why` の「実践者の幅」は、個人名を出さず、根拠：弱で書いた（束の 6.4 と 6.5 の写しによる）

## 提案

回数（公式の「Build your setup over time」の表の値）は変わりやすい値なので、本文に書かず、種類だけの表にした。数値ファイルに入れれば、`#triggers` の表の下の段落に目印を置ける。値は束の 6.3 の表記（同じ規約・コマンドを 2 回間違えた→CLAUDE.md、同じ手順書を 3 回目に貼った→スキル）による。公式の表の原文で再確認が要る。

```yaml
proposals:
  - fact: {id: add-trigger-claude-md-mistake-count, title: CLAUDE.md に足す目安（同じ規約・コマンドを間違えた回数）, value: 2 回, sources: [cc-docs-features-overview], checked: 2026-11-05, status: 要確認}
    used_in: [when-to-add-what#triggers]
  - fact: {id: add-trigger-skill-paste-count, title: スキルに足す目安（同じ手順書を貼った回数）, value: 3 回目, sources: [cc-docs-features-overview], checked: 2026-11-05, status: 要確認}
    used_in: [when-to-add-what#triggers]
frontmatter: []
```

## 検査の結果

- 1 回目：エラー 0・警告 10（textlint：算用数字・読点の数・助詞の重なり）。本文を直した
- 2 回目：エラー 0・警告 0

## 確かめていないこと

- 公式の文書（Extend Claude Code）の表の原文は開いていない。表の行は束の写し（6.1・6.3）による
- 雛形の動作は確かめていない
- 出力スタイル・サブエージェント・プラグインの `compare` の表の「—」「未確認」は data の値のまま。各ページが公開されたときのリンク表示は未確認
- 「古い記事のカスタムコマンドはスキルにまとめられた」は data の skills の note による。一次資料では開いていない
- 「共有する拡張は複数の人が使うものに絞る（根拠：中、実務の一致）」は束の 6.7（p56#65 の補完）による。根拠の強さの印は束の評価（中）に合わせた
- WSL 以外の OS・IDE 拡張の動作は扱っていない

## 使用量

- 道具の呼び出し：約 12 回（Read 3、Bash 6、Write 4 など）。Web の取得：0 回
