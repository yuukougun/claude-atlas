# 工程7 TB（台帳と data）の報告

## 当てたこと

### 23（T1〜T5）
- `tools/gen/ledger.py`：
  - T1 新しい block `ledger-index`（列：古い助言（`#<行の id>` へのリンク）・状態・変わった時期・面。ファイルの順）
  - T2 行の見出しの直下に「古い助言（状態：撤回）」の 1 行
  - T3 `period_with_label`（時期の後に `changed.label` を（…）で付ける）
  - T4 `name` を持つ行と `principle_kind: feature` の行は、原理の欄の見出しを「この機能が受け持つ原理」にする
  - T5 `see_also` を「同じ話題の行：」のリンクにする（相手の id が台帳になければ注意）
- `schema/keys.yml`（outdated-advice の節に `surfaces`（required）・`principle_kind`・`see_also`・`changed.label`。facts の names の `changed.label` も 1 行。features の所は触っていない）。`make_schema.py` は流した。
- `data/outdated-advice.yml`：全 37 行に `surfaces`。D1 の label を 9 行（think-hard-keywords・yolo-skip-permissions・approve-everything-first・tell-it-to-use-subagents・subagent-per-step・interactive-tutorial・removed-commands・ralph-loops・tmux-agent-orgs）。`principle_kind: feature` を 3 行（styles-for-tone・cowork-separate-app・memory-daily-summary）。`see_also` を 3 行（tell-it-to-use-subagents・subagent-per-step・subagents-to-save-context が互いを指す）
- `data/facts.yml`：names の web-to-cloud-sessions・customize-to-plugins に D1 の label
- 試験：`tests/tools/test_gen_ledger.py`（新規。6 件）。必須の `surfaces` に合わせて、`tests/tools/fixtures/{lib,checks,gen,packet}/data/outdated-advice.yml` の各行に `surfaces: [claude-code]` を足した
- **台帳のページに置く目印（PF2）**：`## 台帳 {#ledger}` の節の、`<!-- gen:begin ledger -->` の前に `<!-- gen:begin ledger-index -->` と `<!-- gen:end ledger-index -->` の組。節の導入の文も一覧表に合わせて直す（「行は…どの順にも並んでいない」は、表で状態・時期・面を見比べられる、に）。あわせて `tools/gen/config.yml` の hosts を `outdated-advice-ledger: [ledger-index, ledger]` にする（config.yml は担当外。なくても生成は動くが、目印がないときの注意が出ない）
- 結果：`test_gen_ledger` 6 件 OK。全体の試験 596 件中、失敗は `test_generated_files_are_fresh` の 1 件のみ（台帳のページほか 5 ページがまだ作り直されていないため。メインが `gen_site.py` を流せば直る）。`check_pages.py`：エラー 0。

### 24（D2〜D7）
- `data/outdated-advice.yml` に文面を写した：D2（think-hard-keywords の now）・D3（add-double-check の now と how_to_find）・D4（routines-name の now と how_to_find）・D5（architecture-in-claude-md・keep-going-dont-be-lazy の why_then）・D6（interactive-tutorial・lower-temperature の now）・D7（removed-commands の now の組み直し、customize-tabs の「2026-11-30」の文を how_to_find から now の末尾へ）
- names `routines-to-scheduled-tasks` の current を「クラウドの予定のタスク（cloud scheduled tasks）」に変えた（`data/facts.yml`）。一次資料の確認：https://code.claude.com/docs/en/routines を 2026-11-05 に取得。題は「Automate work with scheduled tasks」、本文に「A cloud scheduled task, formerly a routine」とある
- 原理の付け直し：avoid-opus-as-expensive を `[確かめる]` から `[握る, 確かめる]`（モデルを選ぶ・使う量の判断は、読み方の節の「握る」の定義に当たる）。budget-tokens・lower-temperature・think-hard-keywords は、読み方の節が「確かめる」に「考える量や出力の安定」を含めるので、変えなかった。action-beta-direct-prompt（確かめる）は迷うので変えていない（下）

### 25
- ralph-loops の title を「プラグインや自作の bash ループで回し続ける」に。「Ralph」は how_to_find に 1 回（「記事で「Ralph」の名で紹介される回し方（…）も、同じ仕組みの行として探す。」）。行の id は変えていない

### 32
- `data/facts.yml` に `subagent-handback-min-version`（値 2.1.271、sentence「Claude Code {value} 以降」、出典 cc-docs-hooks、checked 2026-11-05、volatility 中、status 確認済み）。本文の目印は PF1

### 42(c)
- `data/facts.yml` の names に `academy-claude-rename`（current: Claude Academy、old: Anthropic Academy）。https://academy.claude.com/ を 2026-11-05 に取得し、題と見出しが「Claude Academy」で、旧名も改名の日も書かれていないと確かめた。`tools/check_noai.py https://academy.claude.com/` は「noai・noimageai の指定はない」
- academy.claude.com は data/sources.yml の domains に既にあり、出典 `claude-academy`（data/sources.d/how-to-use.yml）も既にあるので、sources.yml は変えていない（URL の重複でエラーになったため、足したものを戻した）
- 時期：changed を date 2026-07-31（旧名の最後の用例＝tutorialsdojo の記事の公開日）〜until 2026-11-04（新名の確認）の範囲にし、note に「改名の時期は不明」と書いた

## メインに判断してほしいこと
1. academy の names は changed.date が必須のため、範囲で入れた。年表（change-timeline-2026）と用語索引の旧名に「2026-07-31〜2026-11-04」と出る。改名がその間とは限らないので、出したくなければ status を 未確認 にする（年表と旧名の一覧から外れる）。
2. 年表（timeline）には label を付けていない（長い文で行が読みにくくなるため。`terms.py` の `period_text` も TA の所で直せない）。付けるなら `timeline` の `period_text` を `period_with_label` に替える 1 行。用語索引の旧名（terms.py の old_names）にも出ない。
3. `surfaces` の値は、各行の内容から私が決めた（例：prefill・budget-tokens・temperature・thinking-tags・interactive-tutorial・console-prompt-generator は api、cowork-separate-app・memory-daily-summary・customize-tabs・styles-for-tone は app、important-caps・keep-going・add-double-check・avoid-opus は 3 面）。一次資料での照合はしていない。見直してほしい。
4. 原理の付け直しで迷って変えなかった行：action-beta-direct-prompt（GitHub Action の入力の移行。確かめる／縛る のどちらとも言い切れない）。avoid-opus-as-expensive の 握る 追加は、作者の意図と違えば戻す。
5. T4 の対象は 9 行の指定だが、`name` を持つ行はすべて見出しが替わるため、指定にない workflow-keyword-extra-usage（workflow → ultracode の改名）も「この機能が受け持つ原理」になる。改名の行なので合うと考えた。
6. `principle_kind` は文字列（feature だけを見る）。site.yml の語彙にしていない（担当外）。
7. D7 の版（2.1.91・2.1.92・2.1.222・2.1.83・2.1.277）と D3 の Opus 5.5 の手引きの引用は、fix.md のとおり写した。私は照らし直していない。
8. 全体の試験で TA の所は落ちなかった（途中に一度 `test_routes_table` が落ちたが、TA の変更が入った後は通った）。

## 使用量
- 道具の呼び出し 約 45 回。Web の取得 2 回（code.claude.com の routines、academy.claude.com）。check_noai 1 回。
