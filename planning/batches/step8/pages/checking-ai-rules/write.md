# write.md：checking-ai-rules（concept・safety）

## 書いたファイル

- `docs/safety/checking-ai-rules.md`（stubs から移した。front matter で変えたキー：`stage` stub→draft、`updated` 2026-11-05。sections・anchor は不変）
- `snippets/checking-ai-rules/rules-checklist.md` と `rules-checklist.expect.yaml`（kind other・safety true・open true）
- `docs/img/checking-ai-rules/measure-types.svg`（何を測るかで型が分かれる図。静的。大会の例が根拠で、授業と仕事への当てはめは本文で「類推」と明記）
- `data/sources.d/checking-ai-rules.yml` は置かなかった（sources は空のまま。理由は「確かめていないこと」）

## 必ず持つものの対応

- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- level（使う）：front matter（変更なし）
- 原理 `principle`（握る）を本文で名指す：`#when-unclear`（「境界を人が握る、という原理（握る）」。競争の例は `competition-rules#hold-the-boundary` へ link）
- `prevents`・`pitfalls`：front matter が空のため、名指す対象がない（本文は原因に結ぶ記述を持たない。下の提案を参照）
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#why-rules-differ`（なぜ、図付き）、`#checklist`（何に効くか＝確かめる点）、`#when-unclear`（誤解＝「文言がない＝使ってよい」を正す）、関連はテンプレートが出す

## メインに判断してほしいこと

- 注意書き（法的な助言ではない）：decisions 2026-11-03 の方針 7 はサイト全体の注意書きだが、card §13 によりページには足していない。「このページは法令の解釈を書かない」という範囲の文だけ rights-and-licenses に置いた。サイトの注意書きの場所は作者の承認を得てメインが決める
- `#when-unclear` の判断例は、高専プロコンの例（公式ページに生成 AI の記述がなく、行動規範の熟読を求める）の一般化として、大会名を出さずに書いた。大会名と版を出すかはメインが判断する

## 提案

```yaml
frontmatter:
  - {id: checking-ai-rules, key: prevents, before: [], after: [境界がない], reason: "本文は、規則の境界を決める側と確かめる側を分ける話で、where-your-data-goes と同じ原因（境界がない）に結べる。付けるなら本文の when-unclear に原因名の名指しを足す"}
```

- 用語集・prh・data への提案はなし。数値の提案（facts-proposal.yml）もなし（本文に変わりやすい値を書いていない）

## 検査の結果

- 1 回目：エラー 0・警告 7（no-doubled-joshi）。直した後の 2 回目：エラー 0・警告 2（行 166 の「が」、行 169 の「に」）。どちらも文の読みやすさを損なわない助詞の重なりと見て、残した（検査は 2 回までのため）。検証と直しの担当が直すか判断する

## 確かめていないこと

- 型ごとの理由（個人の力→禁止、成果物→許可と開示、両方→部門分け）は、調査資料の写し（11 第1節、根拠 強・版依存）に基づく。一次資料は開いていないので、本文は（根拠：中）にした
- 文部科学省の通知・学校の個別のガイドラインは、束に出典の URL がないため載せなかった（sources は空）
- 規則の版・確認日・類型は competition-rules に任せ、ここには書いていない
- Web の取得は 0 回。link の相手の節（competition-rules など）の本文が、このページの言い回しと合うかは未確認
- 図の見た目（SVG のレンダリング）は目視していない

## 使用量

- 道具の呼び出し：約 14 回（check_page は 2 回）。Web の取得：0 回
