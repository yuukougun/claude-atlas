# hook-recipes 執筆の報告

## 書いたファイル
- `docs/enforce/hook-recipes.md`（stubs から mv。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（先に整える守り {#guards}・フックを登録する {#register}・常設する前に確かめる {#verify}・動かないとき・止めすぎるとき {#failures} を足した。既存の 6 つの anchor は変えていない）、`sources`（既にある id の cc-docs-hooks・cc-docs-hooks-guide・cc-docs-features-overview）、`stage`、`updated`
- 雛形（`snippets/hook-recipes/`、それぞれ .expect.yaml 付き）：format-after-edit.py・block-dangerous-bash.py・redirect-pip-to-uv.py・filter-test-output.py・deny-subagent-commit.py・register-hooks.json（通知の 2 つも含む）

## 必ず持つものの対応
- 手順：format-after-edit・block-dangerous・redirect-commands・filter-test-output・subagent-only の各節（各段に「確かめ」を付けた）。登録は register
- 確かめる・縛るのページへの道：guards（block-with-exit-2#reason・writing-safe-hooks#fail-open・#matcher・lock-side-effects#what-to-lock）と、front matter の prerequisites（block-with-exit-2・writing-safe-hooks）
- level：front matter の「仕組みにする」（変更なし）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：guards → register・各レシピ → verify → failures（症状の振り分けは表で関連ページへ）

## メインに判断してほしいこと
- 雛形 filter-test-output は `updatedInput` と `permissionDecision: allow` を一緒に返す。公式の文書の抜粋に allow と並べた例があるが、allow が必須かは全文で確かめていない。確かめる担当に見てほしい
- 通知のコマンドは `notify-send`（Linux のデスクトップ）。WSL などは本文で「未確認」と書いた
- 目次の備考にある「制作の .claude/settings.json の H3 の動作確認を雛形の動作確認に使う」は、確認の結果を見ていないため使っていない。制作の H2・H3 は注釈付きの文章で示した
- 「PATH の差し替えで止めた実践者の例」は、第三者を名指ししないため名前を出さず、（根拠：弱）で書いた

## 提案
```yaml
sources:
  - note: "担当にだけ禁じる節の「disallowedTools は指定子を付けても Bash 全体が外れる」は research/28 #14 の S3（サブエージェントの文書）による。このページの sources に載せる id が無い（cc-docs-subagents など）。足すなら data/sources.d への追加が要る"
facts:
  - note: "agent_id が入力に付く最低の版（research/28 #1：v2.1.69、2026-03-04）を数値の id にすると、deny-subagent-commit の min_version_fact に使える。本文には版を書いていない"
```
front matter の他キーの直しの提案はなし。

## 検査の結果
- 1 回目：エラー 3・警告 10（prh の「拒否ルール」「permissions」、目印を同じ行に置いた警告、textlint の警告）。2 回目：エラー 0・警告 1
- 残した警告：no-doubled-joshi（「に」の重複）1 件。生成後の行 346 付近。読みにくくないため残した

## 確かめていないこと
- 雛形はどれも動かしていない（動作の確認は別の担当）。正規表現の照合は手元で実行していない
- `agent_id` がワークフローの担当で付くか。`if` の判定が Bash の複合コマンドでどこまで当たるか
- `updatedInput` で書き換えたコマンドの確認の画面が出るか（allow を返すため飛ぶ可能性がある）
- 囲み内の字下げした段落は textlint が検査しないため、目で読んだだけ

## 使用量
- 道具の呼び出し：約 30 回。Web の取得：1 回（code.claude.com/docs/en/hooks。抜粋のみ）
