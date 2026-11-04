# write.md：what-uses-up-limits

## 書いたファイル
- docs/cost/what-uses-up-limits.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 8 件、sections に effects・misconceptions を足した）
- docs/img/what-uses-up-limits/resend.svg（毎ターンの読み直しが積み上がり、休んだ後は全部を読み直す図）
- snippets/what-uses-up-limits/ask-usage-breakdown.md と .expect.yaml（内訳を読んで減らす候補を出させる依頼。目次の templates は「なし」だったが、節 find-what-uses-it に置いた）
- data/sources.d/what-uses-up-limits.yml は作っていない（sources は既存の id だけ）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 見せる・prevents 散らかっている／合っていない）：#effects
- level を持つ・要点の最初が「何が分かるか」：front matter と冒頭の要点
- 構成（何が起きるか→なぜ〔比喩付きの図〕→何に効くか→誤解→関連）：#causes・#long-sessions（図と比喩）・#effects・#misconceptions。関連はテンプレートが出す
- pitfalls：front matter が空なので、名指す対象なし

## メインに判断してほしいこと
- 節 effects・misconceptions を足した。目次の sections が 3 つだったので、catalog 側の同期が要るなら反映を頼む

## 提案
```yaml
frontmatter:
  - {id: what-uses-up-limits, key: sections, before: [causes, long-sessions, find-what-uses-it], after: [causes, long-sessions, find-what-uses-it, effects, misconceptions], reason: "concept の必ず持つもの（何に効くか・誤解）を節にした"}
```

## 検査の結果
- 1 回目：エラー 1（prh：skill）・警告 4。直した後：エラー 0・警告 2
- 残した警告 2：no-doubled-joshi「が」（#effects の末尾の段落〔リンクの題名が長く「が」が重なる〕と、#misconceptions の think hard の項）。読みやすさは損なわないと判断

## 確かめていないこと
- 表の「要因」の内容は、束の写し（Help Center の案内と費用の文書）に基づく。一次資料は開き直していない。Web の取得は 0 回
- idle compaction（放置した大きな会話の要約）は、束の材料 6.6 にあるが sources に出典の id がなく、版の条件もあるので本文に書かなかった
- マルチエージェントが通常のチャットより多く使う旨は、数を書かずに出典（anthropic-eng-multi-agent-research-system）だけ付けた
- アプリでの内訳の有無は未確認と読める書き方にした。/usage の内訳の項目名は画面で変わるため、skill・サブエージェント・プラグイン・MCP と書いたのは 2026-10 時点の公式の記述に限る
- 雛形の動作は確かめていない

## 使用量
- 道具の呼び出し 約 12 回、Web の取得 0 回
