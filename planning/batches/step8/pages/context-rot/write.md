# context-rot 執筆の報告

## 書いたファイル
- docs/basics/context-rot.md（stubs から移し、stage を draft、updated を 2026-11-05、sources を [chroma-research-context-rot, arxiv-2307-03172] に変えた。ほかのキーは触っていない）
- docs/img/context-rot/similar-sheets.svg（似た書類が混ざる模式図。数値なし）
- 雛形・data/sources.d は作っていない（目次の templates なし。出典は data/sources.yml にある id だけを使った）
- stubs/basics/context-rot.md は移したので削除した

## 必ず持つものの対応
- どの原理・原因に関わるか（principle「見せる」・prevents「散らかっている」を名指し）：#何に効くか（見出し「何に効くか」。anchor なし）
- pitfalls：front matter に無いので持たない
- level あり・要点の最初は「何が分かるか」：冒頭の要点の囲み
- 構成（何が起きるか→なぜ→何に効くか→誤解→関連）：見出し順のとおり。関連はテンプレートが出す。節 #lost-in-the-middle は sections の節

## メインに判断してほしいこと
- 要点の1項目目は summary の1文目と少し言い回しを変えた（textlint の「が」重複を避けるため）。意味は同じ
- 「誤解」の3項目目（失敗を残しておけば、モデルが学ぶ）は、会話の中で学習するという誤解を想定した推論。根拠の印は付けていない。不要なら削除を

## 提案
- なし

## 検査の結果
- 1回目：エラー 0・警告 7。直した後の2回目：エラー 0・警告 4（no-doubled-joshi の「が」「に」。要点1項目目・Chroma 報告の段落・判断例の理由・Liu らの段落）。文を短くする直しは流し直しの回数の制約で見送った。誤検出ではなく、読みやすさの軽い警告

## 確かめていないこと
- Chroma の報告は WebFetch の要約で確かめた（18 モデル・Claude 5 モデル・類似度・distractor 1つと4つ・位置 11 通りで差なし・著者の限界の記述）。原文の細部（図の値）は見ていない
- Liu らの研究の対象モデルの名前は束にないため書いていない。「2023 年当時のモデル」とだけ書いた
- 「Claude の系列は見つからないと答えることが多かった」は Chroma 報告の要約に基づく。他社の名は出していない
- outdated-advice-ledger ページの存在と anchor は、カードの記述に従った（生成の検査は通った）
- anthropic-eng-effective-context-engineering-ai は本文で使っていないので sources に入れていない（attention-budget が持つ）

## 使用量
- 道具の呼び出し：約 14 回（check_page 2 回を含む）。Web の取得：1 回（Chroma）
