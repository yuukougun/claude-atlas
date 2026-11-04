# write.md：parallel-and-loop-costs

## 書いたファイル

- `docs/cost/parallel-and-loop-costs.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections に effects・misconceptions を追加、sources に 9 件）
- `snippets/parallel-and-loop-costs/loop-with-limits.md` と `.expect.yaml`（目次の templates の案）
- `docs/img/parallel-and-loop-costs/multiplication.svg`（目次の visual の案：本数 × 回数 × 1回の文脈）
- `planning/batches/step8/pages/parallel-and-loop-costs/facts-proposal.yml`
- `data/sources.d/parallel-and-loop-costs.yml` は作っていない（sources は既存の id だけ）

## 必ず持つものの対応

- どの原理・原因に関わるか（principle 握る・縛る／prevents 合っていない／pitfalls やめられない）：`#effects`（4 項目で名指し）
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#multiplication`（場面と図）→ `#decide-before-starting` → `#reading-examples` → `#effects` → `#misconceptions` → 関連（テンプレート）

## メインに判断してほしいこと

- 倍率「約7倍」は本文に書かず、条件つきと書いた（facts-proposal.yml）。Manage costs の原文は未確認（束の research/23 #7 に頼る）
- 「約 15 倍」（2025 年の Research 機能）は、研究の固定の記録として本文に書いた（根拠：中）。目印にするなら提案を足す
- `--max-turns`・`--max-budget-usd` は台帳 ralph-loops の本文を根拠に書いた。headless-basics#limits は束の指せる節にないので指さなかった
- `--max-turns` などを「確かに止める」仕組みと書いた。原文での確認はしていない

## 提案

- 雛形の「要る最低の版」が、features で subagents（1.0.60）になっている。tracks 全体だと 2.1.154（workflows）になるため `features: [subagents]` を expect に書いた
- 用語集：prh が「agent teams」を「エージェントチーム」に直す。表記の揺れは出なかったが、別名の行以外は日本語で統一した

## 検査の結果

- check_page.py を 2 回流した。最後はエラー 0・警告 4
- 残した警告 4 件：59 行目（図の代替テキスト）、67・80・81 行目（link の目印の間に道具が入れる長い題名が文に数えられる）。誤検出と判断した

## 確かめていないこと

- 公式の文書（costs・agent-teams・workflows・goal）の原文は開いていない。束の写しと data の note に基づく
- 雛形の動作は確かめていない
- 未公開のページ（dynamic-workflows・usage-credits-basics・checking-unattended-runs・open-ended-loop-trap）への link は「準備中」で出る
- 競技の実例は金額を書かず、向きの目安だけにした（元の数字の出典は未確認）

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：0 回
