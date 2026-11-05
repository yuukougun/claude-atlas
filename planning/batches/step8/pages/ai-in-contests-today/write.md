# write.md：ai-in-contests-today

## 書いたファイル
- docs/contest/ai-in-contests-today.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 8 件。sections は変更なし）
- docs/img/ai-in-contests-today/ablation.svg（目次の visual 案：ALE-Bench のアブレーションの棒グラフ。Gemini 2.5 Pro・確認日 2026-11-03 付き）
- data/sources.d/ai-in-contests-today.yml（deepmind.google の domain と、出典 1 件 deepmind-gemini-icpc-2025。check_noai で noai の指定なしを確認）
- planning/batches/step8/pages/ai-in-contests-today/facts-proposal.yml（数値 4 件の提案）
- 雛形は作っていない（目次の templates が「なし」）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle：確かめる・握る）：確かめる→#how-ai-wins（「原理『確かめる』のコンテスト側からの裏づけ」）、握る→#human-contributions（「原理『握る』にあたる」）。prevents・pitfalls は空のため名指しなし
- level：front matter の level: 使う
- 要点の最初の項目は「何が分かるか」：冒頭の要点の囲み
- 構成の目安（原理・仕組み型）：要点 → 何が起きるか（例）#dated-results → なぜそうなるか（図）#how-ai-wins → 何に効くか・限界 #where-ai-falls-short・#human-contributions → 誤解（「ほぼ全形式でトップ」「考察は人にしかできない」）#where-ai-falls-short・#human-contributions → 持ち込めるもの・判断例 #what-you-can-reuse → 関連（テンプレートが出す）

## メインに判断してほしいこと
- 成績の数値（804 人・約 1,300 ドル・呼び出し回数・PicoCTF の順位など）は、目次の notes に従い本文に書かず facts-proposal.yml に提案した。本文は ALE-Bench の論文の結果（Gemini 2.5 Pro、o4-mini-high）と、Anthropic の CTF の 0 問・上位 3% を「固定の記録」として手で書いた（card §7）。fact の目印へ寄せるかを判断してほしい
- 出典のない成績は載せなかった：AWTF 2025（Psyho 対 OpenAI）、ICPC 2025 の OpenAI の 12 問、IOI 2025 の 6 位相当、AWTF 2026 Algorithm の 5 問、MLE-bench の約 64%、BSidesSF 2026・SECCON CTF 14・DARPA AIxCC・CSAW・Kaggle 5 位の事例、HTB の 22 位の推定。束に出典の url がなく、一次資料を確かめていない。載せるなら出典の追加が要る
- AWTF 2026 Heuristic の出典は Understanding AI と OfficeChai（二次の報道）だが、本文の表では出典を直接リンクにしておらず、sources 一覧（参考）で示す。順位表（CPHOF）や ALGO ARTIS の X は sources に未登録のため使っていない

## 提案
- front matter の直しの提案はなし
- data への提案は facts-proposal.yml（4 件）
- 用語集・prh への提案：「アブレーション」を本文で短く定義して使った（用語集にあれば合わせる）

## 検査の結果
- 書き終えた後：エラー 0・警告 4（no-doubled-joshi 4）
- 直した後：エラー 0・警告 2（no-doubled-joshi）。残した 2 件は、生成されたリンクの題名（「…と、底上げで足りる場面」などの節題）が文に入って助詞が重なったもので、本文の手書きの部分ではなく、誤検出ぎみ

## 確かめていないこと
- Google DeepMind のブログ本文は今回開いていない。ICPC の但し書きは束の写し（research/24 B-36）に基づく
- Anthropic の CTF 報告のモデル名と世代は束にない。本文は「報告で確かめる」とした（旧世代の結果を現行の傾向にしない注意として）
- AHC058 の作問者の発言、ICFP 2025 の 320 試行・約 60 ドルは、束の 11 の表（根拠：中）に基づく。sakana.ai のページは今回開いていない
- 表の「AHC で優勝した最初の例」は Akiba の X に基づく束の記述（B-33）で、X は今回開いていない
- 公式の順位表（AtCoder）は atcoder.jp を開かない決まりのため確かめていない
- 図の数値（1167・1264・1879・約 +100・約 +600・6.8%）は束の写し（B-32、論文本文で一致と記録）から書いた

## 使用量
- 道具の呼び出し：約 14 回（Read 6、Bash 6、Write 6、Edit 1、check_page 2 回を含む）。Web の取得：0（check_noai の確認 1 回のみ）
