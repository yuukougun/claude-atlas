# write.md：pitfalls-of-ai-written-tests

## 書いたファイル

- docs/verify/pitfalls-of-ai-written-tests.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 5 id を追加、sections に what-it-helps と misconceptions を追加）
- snippets/pitfalls-of-ai-written-tests/add-tests.txt・add-tests.expect.yaml（目次の templates の案。kind: prompt、safety: false）
- data/sources.d/ は作っていない（出典は data/sources.yml の既存 id だけ：arxiv-2412-14137・arxiv-2506-02954・arxiv-2605-15229・dolthub-claude-code-gotchas・cc-docs-common-workflows）

## 必ず持つものの対応

- どの原理・どの原因に関わるか（principle `確かめる`・prevents `確かめていない` を本文で名指す）：#what-it-helps（pitfalls は空）
- level 任せる・要点の最初が「何が分かるか」：冒頭の要点（level は front matter のまま）
- 構成の目安（原理のページ型）：何が起きるか＝#pinning-bugs・#weak-tests／なぜ＝#pinning-bugs の期待値の出どころ（比喩付きの図は置いていない。理由は下）／何に効くか＝#what-it-helps／誤解＝#misconceptions／関連＝テンプレートが出す

## メインに判断してほしいこと

- 図（比喩付き）は置かなかった。このページは落とし穴と確かめる手が中心で、既存の比喩に合うものがなかったため。必要なら図の案を別途
- 数値の扱い：束の 59.6〜68.1%（p34#61）と、PBT-Bench の約 31%（p34#63）は、arXiv の要旨を取得して確かめた結果、要旨に見つからなかった（特に 31.4% は「素のプロンプトでの最低の再現率」で、失敗の割合ではない）。そのため本文に書いていない。MutGen の 100% と 4% は要旨で確認でき、「単一の例」と明記して書いた。調査資料側の p34#61・p34#63 の記述は誤読の疑いがある（確認の提案）

## 提案

```yaml
frontmatter:
  - {id: pitfalls-of-ai-written-tests, key: sections, before: [pinning-bugs, weak-tests, test-strength, add-to-untested], after: [pinning-bugs, weak-tests, test-strength, add-to-untested, what-it-helps, misconceptions], reason: "concept の構成（何に効くか・誤解）に合わせて 2 節を追加した（既に反映済み）"}
```

- 用語集：「ミューテーションスコア」「変異」「カバレッジ」を追加してよい（本文で短く定義した）
- 台帳（catalog/verify.yaml）の notes：p34#61・p34#63 は要旨で確認できなかった旨を追記してよい

## 検査の結果

- 1 回目：エラー 0・警告 11。2 回目（直した後）：エラー 0・警告 7
- 残した警告 7（すべて ja-technical-writing の助詞の重複・読点の数。意味を損なわずに直す案がなく、またはこの回数の制限で直せなかった）

## 確かめていないこと

- snippet の動作（add-tests）は未確認。Claude Code での実行はしていない
- 引用した研究の本文は読んでいない（arXiv の要旨だけ）。Mathews と Nagappan の「バグを正当化するテストを残す」の方向は要旨で確認、PBT-Bench の「既定の戦略ではほぼ当たらない領域にバグを仕込んだ」も要旨の表現による。対象モデルの名前は要旨に出ていないため書いていない
- 公式の Common workflows の手順は束の写しに基づき、原文を開き直していない
- 「カバレッジを目標にすると自明なテストが増えやすい」は根拠：弱の見立てで、一次資料での確認はない
- ミューテーションテストの道具の名前は、記憶で書かないため載せていない

## 使用量

- 道具の呼び出し：約 16 回。Web の取得：3 回（arxiv.org の 3 件）
