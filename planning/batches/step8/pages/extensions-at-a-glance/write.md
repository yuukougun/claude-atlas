# write.md：extensions-at-a-glance（comparison・extend）

## 書いたファイル
- `docs/extend/extensions-at-a-glance.md`（stub から mv。stage を draft に、updated を 2026-11-05 に）。front matter で変えたキーは `sections`（layers・table・how-to-choose・combine の 4 節）・`sources`（既存 id 10 件）・`stage`・`updated` だけ
- `docs/img/extensions-at-a-glance/four-layers.svg`（4 つの層の静的な図。400x290、文字はテキスト、最後の層は破線で色だけに頼らない）
- 雛形と `data/sources.d/` は作っていない（目次の templates は「なし」。新しい出典も足していない）

## 必ず持つものの対応
- 冒頭の要点：最初の `!!!` の囲み（何ができるか＝「〜なら A、〜なら B」の置き分け）
- 比較の表（道具が作る）：`#table`（`compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか`）
- 判断例：`#how-to-choose`（4 本）
- 組み合わせ方：`#combine`
- 確かめ方：`#combine` の末尾に畳んだ（薄いので節を作らず）
- level：front matter の `level: 任せる` を維持

## メインに判断してほしいこと
- 本文の「4 つの層」は 01 KQ1 Takeaway の構造（後半の注記つきの文は使っていない）を要約した。公式の分け方そのものではないので「この辞典が要約したもの」と書いた。この言い方でよいか
- 「重なり方」の 4 項目（CLAUDE.md は加算、スキルとサブエージェントは名前で上書き、MCP は名前で上書き、フックはマージ）は、01 0-4 の写しから書いた。data の facts にないので出典は features-overview のみ。優先度の順は書かず公式へ誘導した

## 提案
- 数値の提案なし
- data：`rules` の `survives_compaction` は条件付きで、表に「条件による」と出る前提で本文を書いた（すでに `conditional` あり）。`subagents` の強制力、`mcp` の圧縮の扱い、`plugins`・`code-intelligence` の強制力は null か欠で「未確認」と出る。本文の「空欄の読み方」でその理由を説明した。表に「未確認」が多く見えるのが気になるなら、data 側で「1 語で言えない」という値の表現を持てるかを検討してほしい

## 検査の結果
- `check_page.py` を 2 回流した。エラー 0、警告 5（textlint の読点 4 つ以上が 1、助詞「で」「に」「に」「も」の重なりが各 1）。2 回の上限に達したため残した。どれも文意は通る誤検出に近いが、直すなら次の行：44、54、84、86、116

## 確かめていないこと
- 表の値（生成）が本文の説明と食い違わないかは、生成後の表を目で全部は見ていない
- つながるページの未公開の題名が入ったときの前後の文の読みやすさ
- 「判断例：巨大なログから原因を調べる」で、サブエージェントが指定したスキルを使える点は data の note（指定したスキルで文脈を作る）に基づく。操作で試していない
- 「プラグインは配る単位として便利」の一般論は束の材料の言い換えで、一次資料で再確認していない

## 使用量
- 道具の呼び出し：Read 4、Bash 5、Write 3（SVG はシェルの heredoc）。Web の取得 0
