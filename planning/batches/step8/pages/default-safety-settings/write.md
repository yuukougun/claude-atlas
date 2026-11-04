# write.md：default-safety-settings

## 書いたファイル
- docs/safety/default-safety-settings.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 9 件を足した。ほかのキーは変えていない）
- docs/img/default-safety-settings/stages.svg（段階の積み上げ図）
- planning/batches/step8/pages/default-safety-settings/facts-default-safety-settings.yml（数値の提案）
- 雛形・data/sources.d は作っていない（目次の templates が「なし」。出典は既存の id だけで足りた）

## 必ず持つものの対応
- 要点：冒頭の囲み（abstract）
- 比較の表（生成）：#defaults-by-surface（`compare 面 強制力 成熟度 確認日`）
- 判断例：#by-stage に 2 つ（依存の入れ替えを任せる／顧客から預かった資料）
- 選び方：#by-stage（段階ごとに足すもの。判断例を含む）
- 組み合わせ方：#limits の末尾「組み合わせ方」（鍵に置くもの・確認を減らす側・会話に書くもの）
- level：front matter に「整える」がある

## メインに判断してほしいこと
- 面ごとの既定の値（開始モード・アプリの Auto／Manual・サンドボックスの有無・シークレットの保持）は、既定値なので本文に手で書かず、観点ごとに確かめ先の節を指した。下の提案の facts を data に足したら、#defaults-by-surface の観点の箇条に fact の目印を置く（used_in に書いた）
- 節の見出しが「面ごとの既定（生成の表）」で、title が「（生成の表）」を含む。読者に見える見出しとして不自然なので、title の変更を提案する（anchor は変えない）
- #by-stage は教材の推奨で、安全の既定の変更に当たる。決定 2026-11-03 の内容（公式の既定を基準、任せるからサンドボックスと秘密の読み取りの禁止、無人は使い捨ての環境、預かったデータは契約のある面だけ）のとおりに書いた。「手動のモードで始める」は足していない

## 提案
- facts-default-safety-settings.yml：4 件（claude-code-default-start-mode・app-default-permission-mode・sandbox-default-state・incognito-retention-period）。値は束の data と research の写しから起こしたもので、一次資料を開いて確かめていない
- frontmatter（YAML）：
```yaml
frontmatter:
  - {id: default-safety-settings, key: sections, before: [面ごとの既定（生成の表）], after: [面ごとの既定], reason: "見出しに作り方の注記が出るため"}
```

## 検査の結果
- 1 回目：エラー 0・警告 4（冗長な表現・文の長さ・読点・助詞の重複）。直して 2 回目：エラー 0・警告 2（文の長さ 1 文、読点 1）
- 2 回目の後に、その警告の 1 文を分けて直した。3 回目は流していない（回数の決めのため）。警告が残っていれば、#limits の「3.」の最初の文だけである

## 確かめていないこと
- 本文の事実は束の写しに基づく。一次資料は開いていない（Web の取得は 0 回）
- 89 %・13.6 % の実験の対象モデルは束にないので、記事の時点のものと書いた。2026-08-07 の記事で確かめていない
- 「API だけで組む構成には権限モードがない」は、束に書かれていない一般的な理解による記述で、公式で確かめていない
- 公式の 4 つの勧め（#limits の 4.）は、束の調査資料（根拠：中〜強／版依存）の要約で、原文では確かめていない
- 図の表示と compare の表の見た目は、画面では見ていない
- WSL・Linux 以外の OS と IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 13 回（Read 3・Bash 8・Write 2。うち check_page 2 回）。Web の取得：0 回
