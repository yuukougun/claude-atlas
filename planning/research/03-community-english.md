# 英語圏コミュニティの実践知: Claude / Claude Code を使いこなすための tips・ワークフロー・教訓(2025〜2026年10月)

凡例(各 tip の「広まり具合」欄): ◎=複数の独立した実践者+Anthropic 関係者が一致(定番) / ○=よく見かける / △=一部の実践者・個人の好み / ⚔=意見が割れている。
「現在も有効か」は 2026-10-29 時点で確認できた機能状況にもとづいて判定した。出典の多くは二次まとめ(Substack・ベンダーブログ・まとめサイト)であり、そうした出典はその旨を付記した。X(Twitter)の元スレッドは直接取得できなかったため、引用している記事経由で参照している。

---

## Q1. パワーユーザーが推奨するワークフロー(計画先行、spec 駆動、TDD、別セッションでのレビュー、並列セッション、vibe coding と規律ある agentic coding、著名開発者の実践)

### Takeaway
最も強いコンセンサスは「①Claude に自分で検証できる手段(テスト・ビルド・ブラウザ・スクリーンショット)を渡す」「②いきなり書かせず計画(Plan Mode/spec)を固める」「③タスクを小さく切る」「④失敗したら CLAUDE.md/AGENTS.md などの“ハーネス”に教訓を書き戻して次回に効かせる」の 4 つ。Anthropic が約 40 万セッションを分析した研究(2026年6月)では、その課題の領域の知識(熟練度)が高い利用者ほど成功しやすく、行き詰まっても立て直しやすかった。ただし熟練度は、指示の正確さ・何を確かめさせるか・どちらが相手の誤りを正すかを手がかりに Claude が記録から判定したもので、著者は暫定の結果としている。一方、並列セッション/worktree の本数や自律ループ(Ralph、/goal、dynamic workflows)の使いどころは人によって大きく異なり、「上級者向け/好み」の扱いが妥当。

> 【2026-11-03 訂正】元の文は、研究が熟練度の差は「指示の具体性」「検証の与え方」「誰が誰を訂正しているか」に現れると報告し、実践者の経験則を裏づけているとしていた。研究はこの 3 つを、Claude が熟練度を判定する手がかりとして使っている（一次資料の Anthropic「Agentic coding and persistent returns to expertise」、2026-06-16 で確認）。そのため研究の発見として経験則の裏づけには引けない（research/25 の見方では、熟練度の定義に近い）。research/25 の P9・§3.1。

### Cited Findings

#### 前提: 2026年10月時点の機能・モデル状況(tip の有効性判定に使用)
- 2026年9月22日に Opus 5.5 が Opus 5 の後継になった。`opus` エイリアスは Opus 5.5 を指し、`opusplan`(計画は Opus、実行は Sonnet)も使える。Claude Code v2.1.280 から Pro と Team Standard でも既定モデルが Opus になった — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)、[SessionWatcher](https://sessionwatcher.com/news/claude-code-opus-5-5-default-pro-team-standard)(どちらも非公式まとめ)
- Claude Fable 5 は 2026年6月9日公開。Opus 4.8 より上位の一般公開モデルで、価格は $10/$50 per MTok — [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/anthropic-launches-claude-fable-5-its-first-public-mythos-class-model/)。サブエージェント定義の `model` には `fable` エイリアスを指定できる — [Claude Code Docs: subagents](https://code.claude.com/docs/en/sub-agents.md)
- Auto mode(別の分類器がシェルコマンドや操作を審査し、承認を自動化するモード)は、2026年8月14日から Pro/Max/Team の既定パーミッションモードになった。Anthropic によると、ユーザーは許可プロンプトの 97% を承認しており、仕込まれた危険コマンドを 86.4% のケースで見逃した。Auto mode はテストで危険コマンドの 89% を検出した — [GIGAZINE](https://gigazine.net/gsc_news/en/20260810-claude-code-auto-mode/)
- `/goal` は 2026年5月11日(v2.1.139〜)、Dynamic Workflows は 2026年5月28日 GA(v2.1.154〜)。`/loop` は v2.1.72〜。Routines(クラウドでの定期実行)は research preview — [Creeta](https://news.creeta.com/en/claude-code-automation-primitives-loops-goals-routines-dynamic-workflows/)、[Claude blog: dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- v2.1.277(2026年9月18日)から、CLAUDE.md がないプロジェクトでは AGENTS.md を読むようになった — [mer.vin](https://mer.vin/news/claude-code-now-reads-agents-md-when-theres-no-claude-md/)

#### W1. まず Claude に「自分で検証する手段」を渡す(最重要 tip)
- **内容**: テスト、ビルドの終了コード、lint、ブラウザ操作(Chrome 拡張・Playwright)、スクリーンショット比較など、Claude 自身が実行できるチェックを用意し、「通るまで続けさせる」。規模に応じて段階を変える。単純な作業は bash コマンド1つ、中規模はテストスイート、複雑な UI はブラウザやシミュレータで確認する。
- **根拠/なぜ効くか**: Boris Cherny(Claude Code 作者)は「最も重要な tip」として挙げ、品質が「2〜3倍」上がると述べている — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)(元: [X 2026-01-03](https://x.com/bcherny/status/2007179832300581177))。ただし、2〜3倍を裏づけるデータは、どの記事にも示されていない(この下調べの判断)。公式の Best practices(「Give Claude a check to run」)によれば、Claude は作業が終わったように見えると止まる。確かめ方は 4 段階で示されている。プロンプト内のチェック、`/goal` 条件、チェックが通るまでターンを止める Stop hook、書いた本人ではない者によるレビュー(新しい subagent での `/code-review`) — [Best practices](https://code.claude.com/docs/en/best-practices)。Simon Willison も「しっかりした自動テストがエージェントの価値を大きく上げる」と述べている — [Simon Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops)。Armin Ronacher は「機械へのフィードバックループが良いほど結果が良い」と書いている — [Armin Ronacher](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)
  > 【2026-11-03 訂正】元の文は「2〜3倍という数値に裏づけデータはない」を Karo Zieminski の記事（2026-01-07）の主張としていたが、取り違えだった。その記事は同じ数字（「It improves quality 2-3x」）を留保なしに書いていて、裏づけがないとは述べていない。2〜3倍は paddo.dev が Boris Cherny 本人の言葉として引用している（元の X の投稿は読めていない）。「裏づけがない」は、この下調べの判断として書き直した。research/25 の P8。
  >
  > 【2026-11-03 訂正】元の文は「Claude は終わったように見えると止まる」と確かめ方の 4 段階を、Analytics Vidhya を出典に「Anthropic の研究要約」の内容としていた。この内容は Anthropic の研究（2026-06-16）にはなく、公式の Best practices の「Give Claude a check to run」にある（2026-11-03 確認）。Analytics Vidhya は出典を示さずに書いている。出典を Best practices に替え、4 段階の最後を Best practices の書き方に合わせ、下の「広まり具合」の「Anthropic 研究」も「公式の Best practices」に直した。元の文の「実行可能なチェックがあれば人間抜きでループが閉じる」は、報告が Best practices で確かめた範囲の外なので外した。research/25 の P9・§3.1。
- **広まり具合**: ◎(Boris、公式の Best practices、Simon、Mitchell、Armin、HN で一致)
- **現在も有効か**: 有効。ただし Opus 5 向け公式プロンプトガイドでは「モデルは指示されなくても自分の作業を検証する」とされ、「最後に検証ステップを入れて」「サブエージェントで検証して」「double-check して」といった**文言での検証指示は過剰検証を招くので削除せよ**と書かれている — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)。教材では、検証の「手段」(テスト・コマンド・ブラウザ)を整える価値は残り、「念のため確認して」と書き足す価値は下がった、と区別して書くとよい。
- **出典**: 上記

#### W2. 計画先行(Plan Mode → 承認 → 自動実行)
- **内容**: 複雑なタスクは Plan Mode(Shift+Tab 2回、または `/plan`)で始める。計画を納得いくまで練ってから auto-accept に切り替え、一気に実装させる。実装が脱線したら Plan Mode に戻る。
- **根拠/なぜ効くか**: Boris は「計画にエネルギーを注げば Claude は実装を一発で終える」と述べている — [jitendrazaa(2026-01-31 スレッドのまとめ)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。Boris はタスクの約 80% を Plan Mode で始めるという — [Fin Ideas](https://ideas.fin.ai/p/what-were-learning-from-engineers)。計画の修正は書きかけの機能を巻き戻すより安く、誤った前提も早く表に出る — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。方向違いのやり直しは最も高くつくミスでもある(トークン面) — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)
- **派生テクニック**: 計画を .md に書き出し、`/clear` してから実行する(HN の theshrike79) — [sankalp(HN まとめ)](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。Mitchell Hashimoto も、曖昧な依頼は「計画セッション」と「実行セッション」に分けている — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)
- **広まり具合**: ◎
- **現在も有効か**: 有効。`opusplan` で計画を Opus、実行を Sonnet に分けることもできる — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)。Superpowers の write-plan と Plan Mode を併用すると重複になる — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)

#### W3. spec(仕様書)を先に作る/Claude にインタビューさせる
- **内容**: 1行だけの SPEC ファイルを用意し、「Read @SPEC file and interview me in detail using the AskUserQuestionTool about literally anything… continue interviewing me until it's complete. Then write the spec to the file.」と頼む。質問に答え終わったら、**新しいセッション**で spec を渡して実装させる。spec には anti-goals(やらないこと)も書く。要件が明確なら省略してよい。
- **根拠/なぜ効くか**: Anthropic の Thariq が X で共有した手法で、3日で 130万ビューを超えた。著者の環境では平均 20〜30 問(32問のセッションで 157 行の spec ができた)。新しいセッションにするのは、インタビュー中の思い込みを実装に持ち込まないため — [VelvetShark](https://velvetshark.com/stop-prompting-claude-code-let-it-interview-you)(2026-01-02)
- **系譜**: Harper Reed は 2025年2月から、対話型 LLM に「ask me one question at a time」で spec.md を作らせ、推論モデルで prompt_plan.md と todo.md に分解する流れを使っていた — [Harper Reed 2025-02](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)。Claude Code 登場後は、prompt_plan.md の未完了項目を 1 つずつ実装・テスト・コミットさせる定型プロンプトで回している — [Harper Reed 2025-05](https://harper.blog/2025/05/08/basic-claude-code/)。Jesse Vincent の Superpowers プラグインは `/brainstorm`(質問で要件を詰める)→ `/write-plan`(TDD 前提の細かいタスク)→ `/execute-plan` を提供する — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)
- **広まり具合**: ◎(インタビュー型・spec 先行は広く共有されている。具体的な道具立ては人による)
- **現在も有効か**: 有効。AskUserQuestion ツールは現行機能。Claude Code に組み込みの `/brainstorm` はなく、見かけたらプラグイン由来 — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)

#### W4. タスクを小さく切る/1ステップずつ進める
- **内容**: 機能全体を一度に頼まず、ステップごとにレビューしてから次を頼む。長時間の無人実行は品質が落ちるので、時間がかかりすぎたら機能を分割する。
- **根拠/なぜ効くか**: HN では「長く放置すると出力品質が落ちる」(nzach) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。「全部一度に頼むと drift する」 — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。「途中で諦める」問題への対処も「大きなタスクを分割せよ」 — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。Mitchell も「1 つの大きなセッションではなく、明確で実行可能な個別タスクに分けよ」と書いている — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)
- **広まり具合**: ◎
- **現在も有効か**: 概ね有効。ただし Anthropic 研究では、熟練者のセッションのほうが 1 プロンプトあたり約 12 アクション・3,200 語と仕事量が多い(初心者は約 5 アクション・600 語)。つまり「細切れにするほど良い」のではなく、**“完了の定義”が明確な単位に切る**のが本質 — [Creeta(研究要約)](https://news.creeta.com/en/claude-code-expertise-domain-over-coding-2026/)、[Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/)

#### W5. ミスのたびに“ハーネス”へ書き戻す(Compounding / Harness engineering)
- **内容**: Claude が間違えたら、その場で直すだけでなく、CLAUDE.md/AGENTS.md・スクリプト・hook に再発防止策を加える。チームでは CLAUDE.md を git で共有し、PR レビューで `@.claude` をタグ付けして学びを追記させる(`/install-github-action` で設定)。
- **根拠/なぜ効くか**: Boris のチームは週に何度も CLAUDE.md に追記している — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。Mitchell はこれを「harness engineering」と呼ぶ。誤ったコマンドや API の使い方を AGENTS.md に書き、スクリーンショット用スクリプトや絞り込み済みテストランナーのような道具を作って AGENTS.md に記載する — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)。Intercom の事例では、claude.md を 1日に何度も更新する人もいる — [Fin Ideas](https://ideas.fin.ai/p/what-were-learning-from-engineers)。marmelab は「バグを自分で直さず、Claude に原因を調べさせ、プロジェクト文書に記録してから直させよ」と勧める — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)
- **広まり具合**: ◎
- **現在も有効か**: 有効。ただし肥大化すると守られなくなるので、定期的な剪定とセットで扱う(Q2 参照)。Boris も古いルールの定期削除を勧めている — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)

#### W6. セッション末の振り返り(retro)と後片付けコマンド
- **内容**: セッションの最後に「何を学んだか」を Claude に書かせ、置き場所を振り分ける。プロジェクト全般は CLAUDE.md、規約は rules、技術的手順は Skill、詳細は Markdown 文書、設計判断は ADR — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。Boris は毎セッションの終わりに `/techdebt` で重複コードを探して消す — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。人間がレビューする前に `/simplify`(過剰な抽象化を除去)と `/review` を回す — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)
- **広まり具合**: ○
- **現在も有効か**: 有効(`/simplify` は Boris が別スレッドで紹介した組み込みコマンド — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/))

#### W7. TDD(テスト先行)
- **内容**: まずテスト(とモック)を書かせ、失敗を確認してから実装させる。
- **根拠/なぜ効くか**: Harper Reed は「幻覚とスコープの逸脱に対する最強の対策」と言う — [Harper Reed](https://harper.blog/2025/05/08/basic-claude-code/)。Anthropic のセキュリティチームは「まず疑似コード、次に TDD で導く」 — [Claude blog: How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)(2025-07-24)。ykdojo の tips 集にも TDD がある — [awesomeclaude.ai(ykdojo/claude-code-tips)](https://awesomeclaude.ai/claude-code-tips)
- **注意点**: Claude が書く初期テストは、もっともらしく見えて実装と噛み合わないことがあり、ループの原因になる。テストを弱めたり変えたりして通そうとすることもあるので、**テストファイルの変更は特に注意してレビューする** — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### W8. 別セッション/別モデルにレビューさせる
- **内容**: 計画や実装を、もう 1 つの Claude セッションに「スタッフエンジニアとして」レビューさせる(Boris のチームメンバーの方法) — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。Armin はレビューに Codex CLI を使う — [Armin Ronacher](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)。Yegge も、不慣れな言語では別モデルのセカンドオピニオンを取ると言う — [O'Reilly](https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-vibe-coding-with-steve-yegge/)
- **注意点**: 「穴を探せ」と頼まれたレビュアーは大抵何かを報告するので、正しさ・要件上の穴だけ挙げさせる — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/)。**これと相反する公式ガイダンス**もある。Opus 5 は指示を文字どおりに守るので、「高重要度だけ報告」「保守的に」と書くと報告が減りすぎる。全部報告させて、別パスで絞り込むのがよいという — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- **広まり具合**: ○(やり方は分かれる)
- **現在も有効か**: 有効。レビュアーへの指示の書き方は、最新モデルの公式ガイドに合わせて更新が必要

#### W9. 並列セッション+git worktree
- **内容**: worktree ごとに 1 つの Claude セッションを立てる(`claude -w`/`--worktree`)。Boris はローカル 5 本+claude.ai/code で 5〜10 本を並走させ、`--teleport` で行き来し、朝に携帯からもセッションを立ち上げる — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。チームの多くは 3〜5 個の worktree を使う — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **反対・慎重論**: 並列化は文脈切り替えで人間が疲弊し、スループットは上がっても品質が落ちうる。`/batch` も、壊れたときにどのステップが原因か分かりにくい — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。上限は 3〜4 本程度という声がある — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)、[ykdojo](https://awesomeclaude.ai/claude-code-tips)。Mitchell は複数ではなく 1 エージェントを推奨し、デスクトップ通知も切る — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)。Reddit には「アイドル時でも CPU を食う」という反論や、10 並列で週次上限に達し人間がボトルネックになるという報告がある — [Reddit snapshot 1](https://reddit.sentinel-team.org/posts/1qspcip/snapshots/2026-02-01T05%3A38%3A27.093042Z)、[Reddit snapshot 2](https://reddit.sentinel-team.org/posts/1uk434i/snapshots/2026-07-03T03%3A00%3A16.73148Z)
- **広まり具合**: ⚔(仕組みとしての worktree は定番。本数と使いどころは個人差が大きい)
- **現在も有効か**: 有効(`-w`、`/batch`、`/branch` などが整備済み — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/))。教材では「作者の setup は特殊で、まず 1〜3 本から」と書くのが安全

#### W10. 段階的導入(Mitchell Hashimoto の 6 ステップ)
- **内容**: ①チャット UI での本格コーディングをやめ、エージェントを使う。②自分が手で書いたコミットをエージェントで再現して練習する。③終業前 30 分にエージェントを走らせ、ライブラリ比較のような調査や issue/PR のトリアージをさせる(勝手に返信はさせない)。④確実に解ける「slam dunk」な issue をバックグラウンドで任せる。⑤ハーネスを改善する。⑥常に何か 1 つエージェントを走らせておく — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)(2026-02-05)
- **広まり具合**: ○(Simon Willison、Pragmatic Engineer などで広く紹介されている)
- **現在も有効か**: 有効(特定機能に依存しない)

#### W11. 自律ループ(Ralph Wiggum → `/loop`・`/goal`・Dynamic Workflows)
- **内容**: Ralph は Geoffrey Huntley 発案の「同じプロンプトを bash ループで回し続ける」手法。公式プラグインでは `/ralph-loop "<prompt>" --max-iterations N --completion-promise "text"` を使う。完了文字列の判定は完全一致で当てにならないので、**反復上限が本当の安全網**になる。テストやビルドで機械的に完了判定できるタスク(移行・大規模リファクタ・テスト追加)に向き、曖昧な要件・アーキテクチャ判断・セキュリティ関連には向かない — [paddo.dev: Ralph](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)
- **現行機能への置き換え**: `/goal` は検証可能な終了条件とターン上限を設定するもので、別の評価器がトランスクリプトだけを見て判定する。Lighthouse ≥ 90 のような決定的な条件は機能するが、「洗練された見た目」のような曖昧な条件は収束しない。Dynamic Workflows は Claude が JS でオーケストレーションを書き、並列サブエージェントに展開する(同時 16、総計 1,000 まで) — [Creeta](https://news.creeta.com/en/claude-code-automation-primitives-loops-goals-routines-dynamic-workflows/)。Workflows は通常セッションより大幅にトークンを使うので、範囲を絞ったタスクから始める。`ultracode` 設定で effort が xhigh になり、使うかどうかを Claude が判断する — [Claude blog](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)。依存関係のある直列作業は `/goal`、独立した並列作業は workflows — [MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-command-vs-dynamic-workflows)
- **広まり具合**: △〜○(話題性は高いが、日常的に使うのは一部)
- **現在も有効か**: Ralph の「考え方」は有効。ただし 2026年6月時点で、ネイティブの `/loop`・`/goal`・Dynamic Workflows がパターンの多くを吸収している — [paddo.dev: Ralph](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)。教材ではプラグインより組み込み機能を軸に説明するのがよい

#### W12. Vibe coding と vibe engineering の区別
- **内容**: Simon Willison は「vibe coding」を、コードの中身を見ないプロンプト駆動の作り方と定義する。これに対し「vibe engineering」は、プロが責任を持ったまま LLM で加速するやり方。後者を支えるのは、自動テスト、事前計画、ドキュメント、バージョン管理、CI/lint、コードレビュー文化、手動 QA、プレビュー環境、何を任せるかの判断力 — [Simon Willison](https://simonwillison.net/2025/Oct/7/vibe-engineering/)(2025-10-07)。Yegge は「trust but verify」を強調し、プロトタイプなら軽いレビューでよいが本番コードではプロ品質を要求せよと言う — [O'Reilly](https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-vibe-coding-with-steve-yegge/)
- **広まり具合**: ◎(用語の使い分けは英語圏で定着しつつある)
- **現在も有効か**: 有効(概念)

#### W13. Thorsten Ball(Amp)のプロンプト流儀
- **内容**: 「モデルはどこからその情報を得るのか?」を常に問う。新しく入った senior engineer に頼むつもりで、関連ディレクトリ・ファイル・お手本の実装を示す。「one-two punch」として、まず関連情報を集めて読み込ませ、次のプロンプトで本題を頼む。プロンプトの約 90% にスクリーンショットを付ける。how-to の知識は入れ子の AGENTS.md に移してプロンプトを短くする。業務上の要となるコードは厳しくレビューし、周辺コードは緩めでよい — [Thorsten Ball](https://thorstenball.com/talks/how-i-prompt/)(Laracon US 2026-07-29)
- **広まり具合**: ○
- **現在も有効か**: 有効

### Inferences
- 教材の柱は「検証手段」「計画」「分割」「ハーネスへの書き戻し」の 4 つにするのが、英語圏コミュニティの合意と最もよく合う。Anthropic の研究(約 40 万セッション)で一次資料と一致するのは、熟練度が高い利用者ほど 1 回の指示で Claude にさせる仕事が多く、成功しやすく、行き詰まっても立て直しやすいことである(熟練度は Claude の判定で、著者は暫定の結果としている)。
  > 【2026-11-03 訂正】元の文は、研究がこの 4 つの柱を定量的に裏づけているとしていたが、研究の結論として引けるのは上の点までである（たとえば研究は作業の切り方を比べていない）。一次資料は research/25 で読んだ。research/25 の P9・§3.1。
- 並列セッション・自律ループは Boris のような上級者の setup が拡散したもので、反論も多い。「上級編・コスト注意」の枠で扱うのが妥当。
- 2026年に `/goal`・Dynamic Workflows・Auto mode が入り、2025年に流行した手作りの仕組み(Ralph プラグイン、`--dangerously-skip-permissions` 常用、自作の検証ループ)は組み込み機能で置き換えられつつある。「旧手法 → 現行機能」の対応表を作ると読者の役に立つ。
- Opus 5 世代では「検証しろ」「サブエージェントを使え」と文言で書き足す tip が逆効果になりうる(公式ガイドが削除を推奨)。2025年の記事の「プロンプトに書くべきこと」は再検証が必要。

### Gaps
- 公式ベストプラクティス(https://code.claude.com/docs/en/best-practices)の本文は取得できなかった(allowlist 外)。「explore → plan → code → commit」の現行版の記述は未確認。
  > 【2026-11-03 注記】Best practices の本文は research/23 の §3.1 で確かめた（2026-10-26〜27 ごろに大きく書き直され、「もうやめてよい助言」の表が入った）。「explore → plan → code → commit」の今の記述は、報告では確かめていない。
- Anthropic 研究の一次ページ(https://www.anthropic.com/research/claude-code-expertise)は取得できず、数値は Creeta と Analytics Vidhya の二次要約に頼った。2 つの要約は整合している。
  > 【2026-11-03 注記】一次ページは research/25 の §3.1 で読んだ。2 つの要約は数値では整合するが、要約者の解釈が研究の結論として引かれていた（Q1 と Q5 の訂正を参照）。research/25 の P9。
- Kieran Klaassen(Every)の「compound engineering」と Steve Yegge の Gas Town/Beads の具体的な運用法は、検索予算が尽きたため調べきれていない。Yegge については「Beads の CLI はエージェントのために作られている」という引用のみ確認した — [Simon Willison](https://simonwillison.net/2026/Jan/30/steve-yegge/)。
- YouTube の講演要約(AI Engineer など)は直接調べられていない。

---

## Q2. 効果的な CLAUDE.md の書き方(入れるべきもの/入れるべきでないもの、長さ、アンチパターン)

### Takeaway
「短く、全タスクに普遍的な内容だけ、詳細は別ファイルへ(progressive disclosure)」が合意点。目安は「200 行未満」(公式推奨として複数記事が引用)、HumanLayer は 60 行未満の実例を示している。機械的に検査できる規則(フォーマット・lint・禁止操作)は CLAUDE.md ではなく hook・linter・permissions に移す、というのも強い合意。`/init` による自動生成の扱いは意見が分かれる(叩き台として使う派と手書き派)。

### Cited Findings

#### C1. 長さは短く(〜200 行、理想はもっと短く)
- **内容**: 200 行未満に保つ — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)、[israynotarray(公式ドキュメントの推奨として引用)](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)、[Morph](https://www.morphllm.com/claude-code-usage-limits)。HumanLayer 自身のルートの CLAUDE.md は 60 行未満で、一般的な目安は 300 行未満 — [redreamality(HumanLayer 記事の要約)](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)。500 行を超えたら progressive disclosure でリファクタせよ — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。300 行は簡素化すべきサイン — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)。「何も書かないところから始め、同じことを繰り返し言うようになったら足す」 — [ykdojo](https://awesomeclaude.ai/claude-code-tips)
- **根拠/なぜ効くか**: 最先端モデルが確実に従える指示はおよそ 150〜200 個。Claude Code のシステムプロンプトにすでに約 50 個あるため、CLAUDE.md の指示を増やすほど全体の遵守率が下がる — [redreamality(HumanLayer 要約)](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)、[Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。CLAUDE.md は毎ターンのコンテキストに乗るので、トークン代も毎回かかる — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)
  > 【2026-11-03 注記】原文と細部が違う。原文（HumanLayer「Writing a good CLAUDE.md」、2025-11-25）は「おおむね一貫して従える（with reasonable consistency）」で、「確実に」ではない。150〜200 は原文が arXiv 2507.11538 を引いて示した値で、原文自身がこの問題は厳密には調べられていないと断っている（論文そのものは読んでいない）。約 50 は、HumanLayer が当時（2025-11）の Claude Code のシステムプロンプトを調べた自社の見積もりである。research/25 の H1・§3.2。
- **広まり具合**: ◎
- **現在も有効か**: 有効。ただし「150〜200 指示」は 2025年末時点のコミュニティの推定で、Opus 5.5 世代で再測定した資料は見つからなかった
  > 【2026-11-03 注記】「コミュニティの推定」は出どころの書き方が違う。HumanLayer の記事（2025-11-25）が論文（arXiv 2507.11538）を引いて書いた目安で、記事自身が厳密な調査はないと断っている。research/25 の H1・§3.2。

#### C2. 入れるべきもの: WHAT / WHY / HOW+暗黙知
- **内容**: WHAT(技術スタック、構成、どこに何があるか)、WHY(目的、各部分の役割)、HOW(ビルド・テスト・型チェック・検証の方法) — [redreamality(HumanLayer 要約)](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)。技術スタック、アーキテクチャ上の決定とその理由、プロジェクト固有の規約、既知の落とし穴、主要ディレクトリ、予定している移行など「他の場所に書かれていない文脈」 — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。データモデル、命名規約、社内ルールなど、Claude が知らない業務文脈とドメイン知識 — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。好み、避けること、構造、パッケージや import のルール(Reddit の CurveSudden1104) — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1qspcip/snapshots/2026-02-01T05%3A38%3A27.093042Z)。「本物の落とし穴を書いた 50 行は、当たり前の指示を並べた長文に勝る」 — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### C3. 入れるべきでないもの
- **コードスタイル規則(インデント、クォート等)**: linter/formatter(ESLint、Prettier、Ruff)に任せ、Claude には linter の出力を見て直させる — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。「LLM を linter として使うな」。hook などで決定的に検査する — [redreamality(HumanLayer 要約)](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)
- **コードスニペット**: すぐ古くなるので、`src/middleware/auth.ts:15-45` のような file:line ポインタで最新のコードを読ませる — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)、[redreamality](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)
- **一部のタスクにしか関係しない指示**: ノイズになり、全体が「関係ないかも」と扱われる原因になる(C5 参照) — [redreamality](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)
- **Claude が既定で守ることの再記述**: 削除してよい。必須の振る舞いは hook に変換する — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### C4. progressive disclosure(段階的開示)と置き場所の使い分け
- **内容**: ルートの CLAUDE.md には全タスクに関係する内容だけを置く。認証・DB・API・フロントエンドなど話題別の文書は別ファイルにし、ルートからは「どういうときに読むべきか」を添えて一覧するだけにする — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)、[redreamality](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)。`.claude/rules/` のパス別ルールは、該当ディレクトリにアクセスしたときに読み込まれる。サブディレクトリの CLAUDE.md も遅延読み込みなので、重要な規則をそこに頼らない — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)。`paths` frontmatter でルールの範囲を絞る — [Morph](https://www.morphllm.com/claude-code-usage-limits)
- **使い分けの指針**: 短く文脈依存の事実は CLAUDE.md、再利用する手順は Skills、外部システムにあるデータは MCP — [Falconer](https://falconer.com/guides/claude-code-context/)。CLAUDE.md は常に読み込まれ、Skills は関連するときだけ、slash command はユーザーが呼んだとき、plugins はそれらの束 — [ykdojo](https://awesomeclaude.ai/claude-code-tips)
- **広まり具合**: ◎
- **現在も有効か**: 有効(`.claude/rules/` や Skills などの公式機能で実現しやすくなった)

#### C5. 「CLAUDE.md が無視される」理由と対策
- **内容**: CLAUDE.md はシステム設定ではなく、システムプロンプトの後の「ユーザーメッセージ」として渡される。Claude は関連性を判断し、無関係と見なした規則を飛ばすことがある(仕様であってバグではない) — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)。HumanLayer の要約によれば、Claude Code は「この文脈は関係あるかもしれないし、ないかもしれない」という趣旨の system reminder を付けて渡す — [redreamality](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)。Opus 4.5 は CRITICAL と書いた CLAUDE.md の規則すら、リマインドしないと確実には守らなかったという報告もある(GitHub #13306) — [Matsuoka](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)。長い会話では最近のユーザー指示が CLAUDE.md より優先される — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)
- **対策**: 機械的に検査できる規則は hook に移す。絶対禁止は `settings.json` の `permissions.deny` に書く。例と反例を添えて書く。無人実行では `--append-system-prompt` を使う — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)
- **広まり具合**: ◎(不満としても対策としても頻出)
- **現在も有効か**: 有効

#### C6. `/init` による自動生成の是非
- **肯定派**: `/init` で叩き台を作る — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)、[jitendrazaa(Boris)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)、HN の aschobel — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)
- **否定派**: CLAUDE.md は全工程に効く高レバレッジのファイルなので、1 行ずつ手で書け — [redreamality(HumanLayer 要約)](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)。自動生成は肥大化し、重要な「なぜ」が抜ける — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。「`/init` して理解してもらえると期待する人」への批判もある — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1qspcip/snapshots/2026-02-01T05%3A38%3A27.093042Z)
- **広まり具合**: ⚔
- **現在も有効か**: 両論とも現行。教材では「叩き台に使うなら必ず削って手で直す」とまとめるのが妥当

#### C7. AGENTS.md との共存
- **内容**: 本体を AGENTS.md に書き、短い CLAUDE.md から `@AGENTS.md` で import する — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。v2.1.277 以降は、CLAUDE.md がなければ AGENTS.md が読まれる。Claude 固有の指示があるなら `@AGENTS.md` import 方式(Bedrock/Vertex/Foundry や Windows でも推奨)、なければ symlink — [mer.vin](https://mer.vin/news/claude-code-now-reads-agents-md-when-theres-no-claude-md/)
- **広まり具合**: ○(複数のエージェントを併用する人の間で定番)
- **現在も有効か**: 有効(2026年9月に公式サポート)

#### C8. 運用(チーム共有・PR での更新・剪定)
- **内容**: git にコミットしてチームで共有し、アーキテクチャが変わったら PR で更新する — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)、[paddo.dev(Boris)](https://paddo.dev/blog/how-boris-uses-claude-code)。古い・矛盾したガイダンスは「自信満々の誤ったコード」を生む — [Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)。`/context` でメモリファイルが占める量を確認する — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### C9.(旧 tip)IMPORTANT/MUST/CRITICAL で強調する
- **内容**: 2025年ごろは、強調語で遵守率を上げる tip がよく見られた。
- **現在も有効か**: 要注意。最新モデルは指示に忠実で、文字どおりに守りすぎる傾向が公式ガイドで指摘されている — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)。一方 CRITICAL でも守られなかったという報告もあり — [Matsuoka](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)、強調だけに頼らず hook や permissions で強制するのが現在の主流 — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)
- **広まり具合**: △(かつては ○)

### Inferences
- 教材の CLAUDE.md の項目は、①長さの目安(200 行未満、実例 60 行)、②WHAT/WHY/HOW、③入れないもの(スタイル規則・スニペット・一部タスク専用の指示)、④強制したいものは hook/permissions へ、⑤rules/skills/MCP との使い分け表、で構成できる。
- 「CLAUDE.md が無視される」不満は非常に多く、仕組み(ユーザーメッセージとして渡り、関連性が判断される)の解説自体に教材としての価値がある。

### Gaps
- HumanLayer の原文(https://www.humanlayer.dev/blog/writing-a-good-claude-md)は取得できず、中国語の AI 要約(redreamality)経由の数値を使った。原文で照合することを推奨する。
  > 【2026-11-03 注記】原文（著者表記は Kyle、2025-11-25）は research/25 の §3.2 で読んだ。要約の中身は原文と一致し、細部の差（「確実に」と、150〜200・約 50 の出どころ）は C1 の注記に書いた。research/25 の H1。
- Shrivu Shankar の「How I Use Every Claude Code Feature」(https://blog.sshh.io/p/how-i-use-every-claude-code-feature)の CLAUDE.md の節(@ でファイルを埋め込まない、「Never」には代替案を書く、など)は本文を取得できず未確認。
- 公式ドキュメントの「200 行」推奨を一次ソースで確認できていない(複数の二次記事が引用)。
  > 【2026-11-03 注記】公式の文書（Memory のページ）が CLAUDE.md 1ファイルあたり200行未満を目安にしていることは、research/24 の A-15 で確かめた。

---

## Q3. コンテキスト管理(/clear のタイミング、handoff 文書、進捗ファイル、context rot、短いセッション、サブエージェント、document-and-clear)

### Takeaway
「コンテキストは牛乳のように新鮮なうちに」(ykdojo)が象徴的な合意。無関係なタスクの間では `/clear`、失敗した試行は訂正を重ねずに `/rewind`(Esc Esc)で消し、2 回訂正してもダメなら `/clear` してプロンプトを書き直す。長い作業は HANDOFF.md/計画ファイルに書き出してから新しいセッションで再開する。Chroma の「Context Rot」研究(2025年7月)が、長い入力ほど性能が落ちるという理論的な裏づけとしてよく引用される。

### Cited Findings

#### X1. Context rot の根拠
- **内容**: Chroma の技術レポート(2025-07-14)は、Claude Opus 4 や Sonnet 4 を含む 18 モデルを調べ、単純なタスクでも入力が長くなるほど性能が落ちることを示した。関連する「紛らわしい情報」が 1 つ入るだけで精度が下がり、焦点を絞った約 300 トークンのプロンプトと、無関係な文脈を含む約 113k トークンのプロンプトでは大差が出た — [Chroma](https://trychroma.com/research/context-rot)
- **実践者の観察**: 約 400k トークンを超えると関連性が落ちるので、1M コンテキストの Opus を既定にしない — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。claude.ai のチャットでも 30〜50 ターンで雑になるので、100 ターン前に新しいチャットへ — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **広まり具合**: ◎
- **現在も有効か**: 有効(1M コンテキストが標準オプションになった今も、劣化の報告は続いている)

#### X2. `/clear` を頻繁に/「2 回訂正ルール」
- **内容**: 無関係なタスクの間で `/clear` する — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)、[israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)。同じ問題で 2 回を超えて訂正したら `/clear` し、学んだことを反映したプロンプトで出直す — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/)、[dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。悪い方向に進み続けるなら `/clear`+`git reset --hard` で、新旧のコードが混ざらないようにする — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)
- **根拠/なぜ効くか**: 毎ターン会話全体が読み直されるので、長い会話は高くつくうえに失敗の痕跡が残る — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)。なお `/clear` はコンテキストを小さくするだけで、利用上限(アカウント単位)はリセットされない — [Morph](https://www.morphllm.com/claude-code-usage-limits)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### X3. 訂正するより巻き戻す(`/rewind`、Esc Esc、プロンプト編集)
- **内容**: 悪い応答を同じ会話で訂正すると、間違いがコンテキストに残って後の試行を汚す。`/rewind`(Esc Esc)で最後の良い状態に戻る。marmelab ではこれと `/clear` が最もよく使うコマンド — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)、[dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。claude.ai では「それは違う」と返信せず、悪い回答の前のプロンプトを編集する — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **反論**: Armin Ronacher は「失敗の履歴を捨てると、モデルは同じ失敗を繰り返す」と、コンテキスト圧縮で行き止まりの記録が消えることを警告している — [Armin Ronacher](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)
- **広まり具合**: ◎(Armin の指摘は、巻き戻すなら失敗の教訓を文書に残せ、という補足として扱える)
- **現在も有効か**: 有効

#### X4. Handoff 文書/document-and-clear/進捗ファイル
- **内容**: コンテキストが埋まる前に HANDOFF.md を書かせ、新しいセッションでそれを読ませて再開する。`/compact` の代わりに使う — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)、[ykdojo](https://awesomeclaude.ai/claude-code-tips)。チケットや PR ごとに TODO.md を持ち、進捗をエージェントに更新させる(HN の nico) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。Harper Reed の todo.md もセッションをまたいで状態を保つためのもの — [Harper Reed](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)。Armin はサブエージェントがうまくいかないとき、新しいセッションを立ててメモを Markdown に残す — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)
- **根拠/なぜ効くか**: 要約(compaction)はファイルパスやエラーメッセージ、行番号を変えてしまうことがある — [Morph](https://www.morphllm.com/claude-code-auto-compact)(ベンダー記事)。人間やエージェントが書いた明示的な文書のほうが、何を残すかを制御できる
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### X5. `/compact` の使い方と自動 compaction
- **内容**: `/compact` には焦点を指示する(例: "focus on X") — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。迷走しだしたら手動で `/compact` する — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。既定の自動 compaction は 95% で発動するが、80% で発動させるほうがよいという意見もある — [Morph](https://www.morphllm.com/claude-code-auto-compact)(ベンダー記事、2026-03)。200K トークンを超えたセッションではアイドル時の compaction が既定で有効で、`"idleCompaction": false` で無効にできるという記述もある — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)(単一ソース、未検証)
  > 【2026-11-03 注記】アイドル時の compaction は research/22 の #15 で確かめた。端末では v2.1.299（2026-10-14）から既定で有効で、会話が既定で 200,000 トークン以上のとき、約1時間放置すると cache が切れる前に要約する。`idleCompaction: false` か /config で止められる。
- **注意点**: compaction の後に「バカになる」(読んだファイルや以前の訂正を忘れる)という報告がある — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。CLAUDE.md の内容は compaction 後も残る — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)
- **広まり具合**: ⚔(`/compact` を使う派と、handoff+`/clear` 派に分かれる)
- **現在も有効か**: 有効

#### X6. サブエージェントでメインのコンテキストを守る
- **内容**: 調査・探索・大量のログやテスト出力はサブエージェントにやらせ、要約だけを受け取る。依頼文に「use subagents」と付ける — [jitendrazaa(Boris)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。組み込みの Explore(読み取り専用、徹底度を 3 段階で指定)と Plan(読み取り専用)は、詳細な出力をサブエージェント側に留める — [Claude Code Docs: subagents](https://code.claude.com/docs/en/sub-agents.md)
- **注意点**: サブエージェントも利用上限を消費する — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)、[Claude Code Docs](https://code.claude.com/docs/en/sub-agents.md)。サブエージェントは会話履歴を見ないので、委任時のプロンプトに必要な文脈を入れる。報告が多いとメインのコンテキストもやはり埋まる — [Claude Code Docs](https://code.claude.com/docs/en/sub-agents.md)。Opus 5 は以前のモデルより委任しやすく、小さなタスクでもコストが膨らむので、「独立して並列化できる大きなタスク以外は委任しない」と指示する。`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` などで上限も設定する — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- **広まり具合**: ◎(「use subagents」と付け足す tip 自体は ○)
- **現在も有効か**: 有効。ただし Opus 5 世代では「もっと使え」より「使いすぎを抑えよ」の方向に変わっている
  > 【2026-11-03 注記】「メインのコンテキストを守る」ために使う、という理由での「有効」は、現行の Best practices と合わない。2026-10-26〜27 ごろの改稿の後の Best practices は、「コンテキストを守るために subagent を使う」を、もうやめてよい助言の表に入れた。溢れることがまれになったためで、並列の作業・うるさい出力を本筋から離すこと・独立のレビューには今も向くが、どれも追加のトークンがかかる、とする。research/23 の §3.7・§3.1。

#### X7. 小技(`/context`、`/btw`、`/branch`、Ctrl+O)
- **内容**: `/context` でコンテキストを何が占めているか(システムプロンプト、ツール、メモリファイル、MCP、メッセージ)を見る。新しいセッションで `/context all` を実行すると、起動時のベースラインがわかる — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)、[Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)。`/btw` は本筋のコンテキストを汚さずに横道の質問をする。`/branch` はセッションをフォークして別案を試す(`--fork-session` も同様) — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/)。Ctrl+O で Claude が開いたファイルや推論をリアルタイムに表示する — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)
- **広まり具合**: ○
- **現在も有効か**: 有効(いずれも 2026年の現行機能)

#### X8. 何を読ませるかを絞る
- **内容**: `@path/to/file` で直接読み込ませると、探索の手間が省けて速い — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。読み込んだファイルやコマンド出力(`npm test` の結果など)はコンテキストに残って毎ターン読み直されるので、出力を絞る — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)。rtk/RTK のようなツールで、コマンド出力を圧縮してから渡す — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)、[Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)。ログ類は tail できる 1 つのファイルにまとめる(Armin の「Unified Logging」) — [Simon Willison(Armin の講演紹介)](https://simonwillison.net/2025/Jun/29/agentic-coding/)
- **広まり具合**: ○
- **現在も有効か**: 有効

### Inferences
- コンテキスト管理は英語圏で最も tip が多い領域。教材では「新鮮さ」「巻き戻し」「書き出して再開」「委任」の 4 つの動詞で整理すると覚えやすい。
- `/compact` に頼るか handoff+`/clear` にするかは意見が割れている。どちらも紹介し、「要約の損失が気になる作業では handoff」と使い分けを示すのが安全。

### Gaps
- Shrivu Shankar の「Document & Clear」や `/catchup` 自作コマンドの原文は取得できなかった。
- 自動 compaction の現在の閾値やアイドル時 compaction は二次ソースのみで、公式ドキュメントでの確認はできていない。
  > 【2026-11-03 注記】アイドル時の compaction は research/22 の #15 で確かめた（X5 の注記を参照）。自動 compaction の閾値は確かめていない。

---

## Q4. カスタム slash command・Skills・サブエージェント・hooks・MCP の実践的な使い方(人気の MCP サーバー、人気の hooks)

### Takeaway
「1 日に 2 回以上やることは skill/command にする」(Boris)、「機械的に守らせたいことは hook に」、「MCP は入れすぎるとコンテキストを圧迫するので、CLI があれば CLI+Skill を優先する」が主流。人気の MCP は Playwright/Chrome DevTools(ブラウザ検証)、Context7(最新のライブラリ文書)、Sentry、GitHub、Linear/Notion/Slack、各種 DB。人気の hook は PostToolUse でのフォーマッタ実行、Stop hook でのテスト強制、PreToolUse での危険操作や機密ファイルの保護、通知。ただし Armin Ronacher のように「slash command も hook もほとんど役に立たなかった」という反対意見も根強く、カスタマイズの量は人による。

### Cited Findings

#### T1. slash command(→ Skills へ統合)
- **内容**: Boris は内側のループで使う作業を command 化しており、`/commit-push-pr` は 1 日に数十回使う。`.claude/commands/` に置き、インライン bash で git status などを事前に計算させる — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。「1 日に 2 回以上やることは skill か command にする」。現在は `~/.claude/skills/`(個人)と `.claude/skills/`(プロジェクト、git で共有)が中心で、旧来の `.claude/commands/` も動く。frontmatter で `user-invocable`、`context: fork`、`allowed-tools` などを指定できる — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。会話を command に変換する「メタ command」を作る人もいる(HN の ctoth) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)
- **反対意見**: Armin は `/fix-bug`、`/commit`、`/add-tests` などを作ったが、引数が構造化されずファイル補完もないため、ほとんど使わなくなった。残っているのは文法修正用の 1 つだけ。「定期的にやることだけ自動化し、使わなくなったら消す」 — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)(2025-07-30)
- **広まり具合**: ⚔(使い込む派と最小限派がいる)
- **現在も有効か**: 有効(Skills との統合が進んでいる)

#### T2. Skills
- **内容**: 繰り返す指示を skill にし、Claude が自分で使えるように description を正確に書く — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。良い出力を貼り付けて「再利用できる skill にして」と頼む。改良するときは複製して版を分ける — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。Boris のチームは BigQuery 用の skill をリポジトリに置き、全員が分析クエリに使っている — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **根拠/なぜ効くか**: 起動時に読まれるのは frontmatter の短い説明だけ(1 skill あたり数十トークン)で、本文は必要なときにだけ読み込まれる。GitHub 公式 MCP だけで数万トークンを食うのとは対照的で、Simon Willison は「MCP より大きな出来事かも」と評した。Markdown なので他のエージェントにも流用できる。ただしファイルシステムとコマンド実行の環境が前提なので、サンドボックスが重要になる — [Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/)(2025-10-16)
- **注意点**: 入れた skill の名前と説明は、使わなくても毎ターン載る(「listing tax」) — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。skill の本文は一度読み込まれると `/clear` まで残る — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)。skill は決まった手順向きで、創造的な作業では探索の幅を狭める — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **広まり具合**: ◎
- **現在も有効か**: 有効(2025年10月以降の中核機能)

#### T3. サブエージェント
- **内容**: Boris が常用するサブエージェントは code-simplifier(完了後の整理)、verify-app(E2E 検証の手順)、build-validator、code-architect、oncall-guide — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。カスタムのサブエージェントは `.claude/agents/` に置く。Ctrl+B でバックグラウンド実行 — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。`claude --agent=<name>` で、事前に設定したエージェントとして起動できる — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/)。Markdown+YAML frontmatter(`name`、`description` は必須。`tools`、`model`、`isolation: worktree`、`effort` なども指定可)で定義し、既定で同時 20・ネスト 3 層まで — [Claude Code Docs](https://code.claude.com/docs/en/sub-agents.md)
- **反対意見・注意**: Armin は「並列化や調査には効くが、読み取りと書き込みを混ぜると混乱する」と言う — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)。Agent Teams(Opus 4.6 と同時の 2026年2月5日に research preview、メンバー同士が直接やりとりする)は、本当に独立したサブタスク向き。書き込みが多い作業では衝突しやすい — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)
- **広まり具合**: ○(読み取り専用の調査役は ◎、役割別に多数のサブエージェントを作るのは △)
- **現在も有効か**: 有効

#### T4. Hooks(人気の用途)
- **フォーマッタ(PostToolUse)**: `Edit|Write` の後に `bun run format || true` を走らせ、CI のフォーマット失敗を防ぐ — [paddo.dev(Boris)](https://paddo.dev/blog/how-boris-uses-claude-code)。prettier の例もある — [Morph: hooks examples](https://www.morphllm.com/claude-code-hooks-examples)
- **テストを強制する Stop hook**: テストが落ちている間は終了を block する。常に block する hook は Claude を永遠に止めなくなるので、条件付きにする — [Morph](https://www.morphllm.com/claude-code-hooks-examples)。Boris も長時間タスクの決定的な検証に agent Stop hook を使う — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。Claude Code は 8 回連続の block で Stop hook を無視してターンを終える、という記述もある — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/)(単一ソース)
- **ファイル保護・危険操作の遮断(PreToolUse)**: `.env`、`package-lock.json`、`.git/` への編集を exit 2 で拒否する。`.claudeignore` や allowlist は回避されうるので deny ルールと併用する。hook の判断は deny/ask の permission ルールを上書きしない — [Morph](https://www.morphllm.com/claude-code-hooks-examples)
- **通知(Notification)**: Boris は入力待ちになったセッションをシステム通知で知る — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。一方 Mitchell は「確認するタイミングは自分が決める」と通知を切る — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)(正反対の好み)
- **許可判断をモデルに委ねる hook**: 許可リクエストを hook 経由で Opus に送り、承認するかを判断させる — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)(現在は Auto mode が近い役割を担う)
- **git の pre-commit との組み合わせ**: Claude は気軽にコミットしがちなので、`pre-commit` パッケージでテスト・型チェック・lint を毎コミット走らせる — [Harper Reed](https://harper.blog/2025/05/08/basic-claude-code/)
- **反対意見**: Armin は hooks で効率は上がらなかったと言う(`uv` と素の `python` のどちらを使うかを制御できず、yolo モードでは deny ルールも効かない)。代わりに `.claude/interceptors` の PATH インターセプタで誤ったコマンドを止め、正しい使い方を表示する — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)
- **広まり具合**: フォーマッタ hook ◎、Stop hook ○、保護 hook ○、通知 ⚔
- **現在も有効か**: 有効(2026年3月時点で SessionStart、PreToolUse、PermissionRequest、Stop などのイベントがある — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/))

#### T5. MCP サーバー(人気と使い分け)
- **よく挙がるもの**: Playwright MCP(フローの操作と UI 検証)、Chrome DevTools MCP(コンソール・ネットワーク・性能)、Context7(バージョンに合ったライブラリ文書で API の捏造を減らす)、Figma、Sentry、Linear/Jira/Notion/Google Workspace、Supabase/Neon/Vercel/Cloudflare — [Composio](https://composio.dev/blog/best-mcp-servers-claude-code-codex)(ベンダー記事、2026-06-29)。PostgreSQL/SQLite/MySQL、Fetch、GitHub、Git、Memory、Sequential Thinking、Slack、Docker、AWS Docs — [heyuan110](https://www.heyuan110.com/posts/ai/2026-03-05-best-mcp-servers-claude-code/)。Context7、Snyk MCP — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。Boris は Slack(`.mcp.json` で共有)、BigQuery、Sentry — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。Armin が唯一使う MCP は Playwright(ログイン済みブラウザでの作業や CI のデバッグ) — [Simon Willison(Armin の講演紹介)](https://simonwillison.net/2025/Jun/29/agentic-coding/)
- **CLI 優先派**: シェルが使えるならスクリプトや Makefile を使わせる(Armin) — [Simon Willison](https://simonwillison.net/2025/Jun/29/agentic-coding/)。Simon は MCP の大半を自作のシェルスクリプトに置き換えたが、安全なリソースへの制御されたアクセスには MCP の役割があると認めている — [Simon Willison(Shrivu 記事の紹介)](https://feeds.simonwillison.net/2025/Nov/2/how-i-use-every-claude-code-feature/)。エージェントは CLI が得意なので、MCP よりシェルコマンドを優先し、AGENTS.md に使い方の例を 1 つ書く — [Simon Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops)。成熟した CLI がある決定的な作業は CLI+Skills、CLI がない・認証つきのライブ文脈が要る・シェル全体より狭い権限にしたい場合は MCP — [Composio](https://composio.dev/blog/best-mcp-servers-claude-code-codex)。`gh` で PR・issue・CI ログを扱う — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)
- **コンテキストのコスト**: サーバーを足すごとにツール・スキーマ・コンテキストが増える。「判断を良くする以上にコンテキストを膨らませるなら切る」 — [Composio](https://composio.dev/blog/best-mcp-servers-claude-code-codex)。不要な MCP や skill は入れない — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)。道具は多すぎるより、よく選んだ少数がよい — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)
- **広まり具合**: ブラウザ系(Playwright/Chrome)と Context7 は ◎。「MCP は最小限、CLI 優先」は ◎(著名開発者のあいだで特に強い)
- **現在も有効か**: 有効。MCP ツールの遅延読み込み(Tool Search)でコンテキスト消費がどこまで減ったかは未確認(Gaps 参照)

#### T6. Permissions と sandbox
- **内容**: Boris は `--dangerously-skip-permissions` を使わず、`/permissions` で build・test・typecheck などの安全なコマンドを事前に許可し、`.claude/settings.json` でチームと共有している。無人で動かすときは `--permission-mode=dontAsk` か、サンドボックス内での skip — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。Armin は skip-permissions を常用して生産性が大きく上がったという — [Simon Willison](https://simonwillison.net/2025/Jun/29/agentic-coding/)。YOLO モードのリスクは、破壊的コマンド、秘密情報の流出、自分のマシンが攻撃の踏み台になること。対策は Docker や Codespaces での隔離、ステージング用の認証情報、予算上限つき(例: $5)の API キー — [Simon Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops)。承認済みコマンドを cc-safe で監査し、`rm -rf` や `curl | sh` が紛れていないか確認する — [ykdojo](https://awesomeclaude.ai/claude-code-tips)。`git pull` は自動許可、`git push` は手動承認のまま — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)
- **広まり具合**: ⚔(skip 派と allowlist 派)
- **現在も有効か**: 2026年8月14日から Auto mode が既定になり、「allowlist を地道に育てる」「skip で済ませる」の二択は大きく変わった — [GIGAZINE](https://gigazine.net/gsc_news/en/20260810-claude-code-auto-mode/)。Auto mode の検出率は 89% で、全部は防げない点を教材に明記すべき

#### T7. 定番のコミュニティ資源
- **内容**: Superpowers(Jesse Vincent。TDD やサブエージェント駆動などのワークフローを skill 化したもの) — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)、[rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)。ykdojo/claude-code-tips(40 以上の tips) — [awesomeclaude.ai](https://awesomeclaude.ai/claude-code-tips)。hesreallyhim/awesome-claude-code など多数の awesome リストがある — [claudefa.st(まとめ)](https://claudefa.st/blog/tools/resources/awesome-claude-code)。使用量の追跡には ccusage(`npx ccusage blocks --live`) — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。`/statusline` でブランチ・コンテキスト使用量・コストを表示する — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **広まり具合**: ○
- **現在も有効か**: 概ね有効(プラグインの機能は組み込み機能と重なり始めている)

### Inferences
- 教材では「CLAUDE.md・Skills・slash command・サブエージェント・hooks・MCP・plugins」の役割分担を 1 枚の対応表にまとめるのが最も需要が高い(英語圏でも「どれを使えばいいか分からない」という記事が多い — 例: [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/))。
- 「足すほど良くなるわけではない(listing tax・MCP の肥大化)」という警告は、2026年の記事ほど強い。

### Gaps
- awesome-claude-code(hesreallyhim)の本体は取得できず(allowlist 外)、掲載上位の項目や star 数は確認していない。
- MCP の Tool Search/遅延読み込みが現行の Claude Code でどう動き、コンテキストをどれだけ節約するかは一次ソースで確認できていない。
- 「どの MCP が実際に一番使われているか」の定量データは見つからなかった(どの記事も推薦リストで、ベンダー色が強い)。

---

## Q5. エージェント時代に効くプロンプト習慣(具体性、検証手段、インタビュー、think/ultrathink、選択肢を出させる、してはいけないことの伝え方)

### Takeaway
具体性が効く。公式の Best practices は、依頼に対象のファイル・症状・直った状態を先に書くよう勧めている。「どのファイルか、どんなシナリオか、何をもって完了か、どのパターンに倣うか」を書くことを熟練者の特徴とする解説もあるが、これは解説の書き手の解釈で、Anthropic の研究の結論ではない。スクリーンショットと音声入力での大量の文脈投入も上級者に共通する。「think/think hard/ultrathink」はキーワードの効果が何度も変わっており(2026年1月に廃止 → 3月に復活)、現在は `/effort`(low/medium/high/xhigh/max)を正面から使うのが本筋。「するな」より「こうしてほしい」という正の例のほうが効く、と公式ガイドは述べている。

> 【2026-11-03 訂正】元の文は「長さより具体性が効く」と、4 つの要素を書くことが熟練者の特徴であることを、Anthropic の研究の結論としていた。研究はプロンプトの長さを測っておらず、4 つの要素は Analytics Vidhya の書き手の解釈である（同じ趣旨の助言は公式の Best practices の「Write a specific prompt」にある）。P1 の内容と根拠も同じに直した。research/25 の P9・§3.1。

### Cited Findings

#### P1. 具体性: 対象ファイル・シナリオ・完了条件・お手本
- **内容**: 良いプロンプトは「ファイル、シナリオ、"done" の意味、従うべきパターン」を述べ、違いはプロンプトの長さではない、と Analytics Vidhya の書き手は書いている(Anthropic の研究の結論ではない) — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/)。同じ趣旨の助言は公式の Best practices の「Write a specific prompt」にある(対象のファイルを名指しし、症状を書き、直った状態を先に言う) — [Best practices](https://code.claude.com/docs/en/best-practices)。新しい senior engineer に頼むつもりで、関連ファイルと「良い」実装例を示す — [Thorsten Ball](https://thorstenball.com/talks/how-i-prompt/)。Claude を「明示すれば非常に有能なジュニア開発者」として扱う(HN の ToJans) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。「もっとパンチを」のような形容詞ではなく、具体例で嫌な点を伝える — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **根拠**: Anthropic の研究(2026-06-16)では、行き詰まったセッションで、失敗と判定され 1 行もコードが書かれなかった「放棄」が初心者で 19%、ほかの段階で 5〜7% だった。著者は、熟練者は難しい問題で行き詰まることが多いので、差の一部はその違いによると注意している — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
  > 【2026-11-03 訂正】内容の「ファイル、シナリオ、"done" の意味、従うべきパターン」と「違いはプロンプトの長さではない」は、Analytics Vidhya の書き手の解釈で、Anthropic の研究の要約ではなかった（研究はプロンプトの長さを測っていない）ので、書き手の主張として書き直した。根拠の「熟練度の差が最も出るのは立て直しの場面」は Creeta の解釈で、研究はそう書いていないので外し、出典を一次資料に替えた。19% と 5〜7% は一次資料と一致する。research/25 の P9・§3.1。
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### P2. 細かく指図せず、成果ベースで頼む
- **内容**: 「Go fix the failing CI tests」のように結果で頼み、変更内容を細かく指示しない。Slack のバグスレッドを貼って「fix」とだけ言う — [jitendrazaa(Boris)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **広まり具合**: ○
- **現在も有効か**: 有効(ただし P1 の文脈提供が前提)

#### P3. Claude に挑ませる・証明させる
- **内容**: 「Grill me on these changes and don't make a PR until I pass your test」「Prove to me this works. Diff the behavior between main and my feature branch」。結果がいまいちならやり直さず、制約を具体的にして詰める — [jitendrazaa(Boris チーム)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### P4. インタビューさせる/質問させる
- **内容**: AskUserQuestion を使ったインタビュー(Q1 の W3 参照) — [VelvetShark](https://velvetshark.com/stop-prompting-claude-code-let-it-interview-you)。散らかった文脈を音声で吐き出し、確認の質問をさせる — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)。ワークフロー系プラグインを入れると Claude がよく質問するようになり、思い込みが減る — [Fin Ideas](https://ideas.fin.ai/p/what-were-learning-from-engineers)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### P5. 画像・音声で文脈を大量に渡す
- **内容**: プロンプトの約 90% にスクリーンショットを付ける — [Thorsten Ball](https://thorstenball.com/talks/how-i-prompt/)。Anthropic のデータ基盤チームは障害対応でダッシュボードのスクリーンショットを渡した — [Claude blog](https://claude.com/blog/how-anthropic-teams-use-claude-code)。Armin のワークフローの約 95% は音声入力で多くの文脈を渡すこと — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)。Boris は macOS の音声入力(fn 2回)、`/voice` は CLI でも使える — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)、[The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/)。長く前置きを書く人と、とりとめなく話してすぐ軌道修正する人の、どちらでも機能する — [Fin Ideas](https://ideas.fin.ai/p/what-were-learning-from-engineers)
- **広まり具合**: ◎(音声入力は 2026年に急増)
- **現在も有効か**: 有効

#### P6. think / think hard / ultrathink(キーワードの変遷)
- **内容と変遷**: 2025年半ばには「think」「think hard」「think harder」「ultrathink」が段階的に大きな思考予算に対応していた。2026年1月16日、思考が既定で最大予算(31,999 トークン)になったため、キーワードは廃止された。2026年3月5日(v2.1.68)、「ultrathink」はその 1 ターンだけ effort を high に上げるキーワードとして復活した。同時に Opus 4.6 の既定 effort は medium に下がった — [Awesome Agents](https://awesomeagents.ai/news/claude-code-ultrathink-returns-medium-effort-default/)。この medium への引き下げは「誤ったトレードオフ」として 2026年4月7日に戻され、全モデルの既定が high または xhigh になった — [InfoQ(Anthropic のポストモーテム)](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem)。Opus 5 の API の既定 effort は high で、難しいコーディングでは xhigh を使う — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)。「現在効くのは ultrathink だけ」とする解説もある(日付不明) — [nikiforovall](https://nikiforovall.blog/claude-code-rules/tips-and-tricks/ultrathink)
  > 【2026-11-03 注記】「2026年1月16日、…キーワードは廃止された」は、一次資料（CHANGELOG）で確かめられなかった（出典は二次情報。research/23 の §3.5）。Q5 の Takeaway の「2026年1月に廃止」と Inferences の「2026年1月」も同じ。また「全モデルの既定が high または xhigh になった」は一部誤りで、2026-04 の時点の記述である。ポストモーテム（2026-04-23）では、4月7日に戻したときに Opus 4.7 を xhigh、ほかのモデルを high にした。その後に出た Opus 5.5・Sonnet 5.5・Haiku 5.5 は、Claude Code の既定が medium である（2026-11-03 確認。research/23 の F3）。
- **広まり具合**: かつて ◎、現在は ⚔(仕様変更が多すぎて混乱が大きい)
- **現在も有効か**: **要注意**。2025年の「think hard と書け」系の tip は古い。現在は `/effort`(または `/model` の設定)で low〜max を明示的に選ぶのが確実。ultrathink がまだ 1 ターンの上書きとして効くかは、Opus 5.5 世代で一次確認できていない(Gaps 参照)
  > 【2026-11-03 注記】ultrathink が今もそのターンだけ深い推論を頼む言葉として認識されること（セッションの effort は変えない）は、research/23 の #9・§3.5 で確かめた。v2.1.311 からは、対話の端末で Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 を Anthropic の API で使うとき、そのターンを xhigh で動かす（VS Code は v2.1.316 から。research/22 の #20）。

#### P7. 「するな」より「こうしてほしい」+範囲の明示
- **内容**: 望むスタイルは正の例で示すほうが、「〜するな」という指示より効く — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)。規則は例と反例をつけて書く — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)。spec には anti-goals を書く — [VelvetShark](https://velvetshark.com/stop-prompting-claude-code-let-it-interview-you)。git worktree を使わない、プロセスのライフサイクルはこう、といった制約は書かなければモデルには分からない — [Thorsten Ball](https://thorstenball.com/talks/how-i-prompt/)。Opus 5 は範囲を広げがちなので、「頼んだことを、意図した範囲で行う」スコープ指定のプロンプトが公式に示されている — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- **広まり具合**: ○
- **現在も有効か**: 有効(公式ガイドが最新モデル向けに明記)

#### P8. 選択肢を出させる
- **内容**: 不確かなタスクでは、いくつかの選択肢と、推奨する既定案を 1 つ出させる — [Sid Saladi](https://sidsaladi.substack.com/p/claude-projects-and-artifacts-101)。計画段階で再利用できる既存の関数を探させる(Sterling Crispin の tip を Boris が支持) — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **広まり具合**: △〜○
- **現在も有効か**: 有効

#### P9. 学習用の出力スタイル
- **内容**: `/config` で Explanatory/Learning 出力スタイルにすると、変更の理由を説明させられる。不慣れなコードやアーキテクチャは HTML のプレゼンにまとめさせる — [jitendrazaa(Boris)](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- **広まり具合**: △
- **現在も有効か**: 有効

### Inferences
- 「think 系キーワード」は日本語圏でも古い情報が広まっている可能性が高い。教材では「2025年 → 2026年1月 → 3月 → 4月」の変遷を示し、「現在は `/effort` を使う」と明記する価値が大きい。
- 「検証しろ」「念のため確認しろ」と書き足すのは、最新モデルでは過剰検証を招くと公式に言われている。教材では「検証の手段を用意する(◎)」と「検証を言葉で命じる(現在は非推奨)」を分けて書くべき。

### Gaps
- 「CRITICAL/MUST などの強い言い回しを控えよ」という Claude 4.5 世代のガイダンスは一次ソースを取得できず、確認していない。Opus 5 のガイドにはその記述が見当たらなかった。
- Opus 5.5 における ultrathink キーワードの挙動(既定 effort が high の場合に意味があるか)は確認できなかった。
  > 【2026-11-03 注記】ultrathink の今の挙動は research/23 の #9・§3.5 で確かめた（P6 の注記を参照）。Opus 5.5 の Claude Code での既定の effort は medium である（research/23 の §3.2）。

---

## Q6. コーディング以外での Claude Code 活用(執筆、調査、データ分析、PKM/Obsidian、日常タスクの自動化)

### Takeaway
「Claude Code はファイルとシェルを操れる汎用エージェント」として、データ分析(CLI 経由の SQL)、Obsidian の vault 管理、執筆補助、調査、ファイルやメディア処理、ブラウザでのフォーム入力に広く使われている。Anthropic 社内でも法務・マーケ・デザインが使っている。非エンジニア向けには Cowork、Claude in Chrome、Obsidian プラグイン(Claudian)などの入口が増えている。

### Cited Findings

#### N1. データ分析(SQL を書かない)
- **内容**: Boris のチームは BigQuery の skill をリポジトリに置き、Claude がクエリを書いて `bq` CLI で実行し、要約する。Boris は「分析 SQL を書かなくなった」と言う。PostgreSQL や MySQL の CLI でも同じパターンが使える — [jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。データ分析では生データに当たって正確さを確認させるのが大きく効く(HN の jm4) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。Anthropic の RL チームは TypeScript を知らないまま、React による可視化を 1 プロンプトで作った — [Claude blog](https://claude.com/blog/how-anthropic-teams-use-claude-code)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### N2. Obsidian/PKM
- **内容**: vault で `claude` を起動し、CLAUDE.md に「知識管理アシスタントとして振る舞う、`[[wiki-links]]` を使う、新しいノートはサブフォルダに振り分ける、テンプレートを使う」と書く。PARA 構成を Claude に作らせ、週次ノートから優先順位を出させる。Claudian プラグイン(サイドバーのチャット)や Terminal プラグインを使う。注意点は、読ませたファイルは Anthropic のモデルで処理されることと、バックアップを取ること — [Productory](https://productory.substack.com/p/obsidian-claude-code-non-tech-guide)(2026-01-30)。散らかった vault を整理する、音声でタスクを追加する、手書きの会議メモの写真を貼る(HN の roland35)。プロジェクトごとにフォルダを作ってノートや文書を書かせると、チャット履歴より後から探しやすい(spaceprison) — [HN: Ask HN non-coding](https://hn.svelte.dev/item/45528463)
- **広まり具合**: ○(2026年に記事が急増)
- **現在も有効か**: 有効

#### N3. 執筆・調査・資料変換
- **内容**: 執筆補助では、文脈を渡し、口述で初稿を作り、1 行ずつ詰める。Markdown で書いて Notion 経由で変換する — [ykdojo](https://awesomeclaude.ai/claude-code-tips)。markitdown(PDF/Word/Excel/PPT → Markdown)、gws CLI(Google Docs/Sheets/Gmail/Calendar → Markdown)、Firecrawl(ウェブページ全文の取得)で元資料をきれいにしてから渡す — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)(2026-05-04)。取得できないページは全選択して貼り付ける。`/copy` で最後の応答を Markdown のままクリップボードに入れる。「昨日 X について何を話した?」と聞けば、過去のトランスクリプトを検索させられる — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。終業前にライブラリ比較などの調査をエージェントに任せる — [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)。Anthropic のセキュリティチームは複数の文書を Markdown の runbook にまとめさせた — [Claude blog](https://claude.com/blog/how-anthropic-teams-use-claude-code)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### N4. ブラウザ・ファイル・メディア処理/日常の自動化
- **内容**: Claude in Chrome でログイン済みのブラウザを操作させ、ベンダーへの問い合わせフォーム、経費精算、応募書類を処理する。画像の一括処理(領収書をまとめて PDF にする等)、Mermaid 図、1 ファイルの HTML プレビュー、`/loop` での定期チェック — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)。ffmpeg、文字起こし、CSV 分析、ディスク整理の汎用インターフェースとして使う — [ykdojo](https://awesomeclaude.ai/claude-code-tips)。Cowork Dispatch で Slack、ファイル、メールなどコーディング以外の作業を、機微な操作は承認つきで任せる。`/schedule` はマシンを切っていてもクラウドで動く — [The Neuron](https://www.theneuron.ai/explainer-articles/-claude-codes-creator-just-dropped-his-15-favorite-power-features-most-people-dont-know-about-/)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### N5. 非エンジニア職種での事例(Anthropic 社内)
- **内容**: グロースマーケティングでは、広告の CSV から成績の悪いものを見つけ、文字数制限内で差し替え案を作るワークフローを 2 つのサブエージェントで構築した。Figma プラグインで広告バリエーションを最大 100 個生成する。法務は弁護士への振り分けを行う「電話ツリー」システムを試作した — [Claude blog](https://claude.com/blog/how-anthropic-teams-use-claude-code)(2025-07-24)。Anthropic の研究でも、コードを生成したセッションでは上位 10 職種群すべてが、検証済み成功率でソフトウェア職から約 7 ポイント以内に収まった — [Creeta](https://news.creeta.com/en/claude-code-expertise-domain-over-coding-2026/)
- **広まり具合**: ○
- **現在も有効か**: 有効

### Inferences
- 日本語の教材でも「非エンジニアの Claude Code」は需要が大きい。研究結果(職種より、そのタスク領域の専門知識が成功を決める)は、非エンジニアの読者を励ます根拠として使える。
- 非コーディング用途では「元資料をきれいな Markdown にしてから渡す」が共通する技術的な要点になっている。

### Gaps
- 研究者(Scott Cunningham など)の実証研究ワークフローは有料記事で、詳細は取得できなかった — [causalinf](https://causalinf.substack.com/p/claude-code-part-12-how-i-use-claude)。
- 日本語の文章執筆に特有の tips は英語圏の資料では見つからない(当然ながら範囲外)。

---

## Q7. コスト・利用上限の管理(モデル選択、Max プランの使い方、無駄の回避)

### Takeaway
Pro/Max の使用量は claude.ai と Claude Code で共有され、5 時間ごとのセッション枠と週次枠がある。上限に効く主な要因は「モデル(Opus/Fable はクォータの減りが速い)」「並列数・自律ループ」「常駐するコンテキスト(CLAUDE.md・MCP・skill の一覧)」。定番の節約策は、Opus で計画して Sonnet で実装する分業、effort を下げる、`/clear`、MCP や skill の整理。一方 Boris は全作業で Opus(当時 4.5)と thinking を使っていて、Karo Zieminski はこれを「トークン単価ではなく、信頼できる変更 1 件あたりのコストで最適化する」流儀と解釈している。ここは意見が割れる。

> 【2026-11-03 訂正】元の文は「トークン単価ではなく、信頼できる変更 1 件あたりのコストで考えて最強モデルを使え」を Boris Cherny の立場としていたが、取り違えだった。全作業で Opus 4.5 と thinking を使うのは Boris Cherny の実践（2026-01-03 の X の投稿を paddo.dev と Karo Zieminski の記事が紹介）で、「信頼できる変更 1 件あたりのコスト」は Karo Zieminski の解釈である。「常に最強を使う」という言い方は、どちらの記事にもない。$2 の「反対意見」の書き分けが正しい。research/25 の P2。

### Cited Findings

#### $1. プランと上限の仕組み
- **内容**: Claude Code と claude.ai(web・デスクトップ・モバイル)は 1 つの使用量プールを共有する。有料プランには 5 時間ごとのセッション上限と週次上限がある。Pro は $20/月、Max 5x は $100、Max 20x は $200。`/usage` や `/status` で確認する。2026年9月14日から週次上限は以前の標準の 125% になった。上限に達したら、API 料金での usage credits を有効にするか(上限 $2,000/日)、Console の API アカウントに切り替える — [Morph](https://www.morphllm.com/claude-code-usage-limits)(ベンダー記事、2026-09-30)。まず $20 のプランで自分に必要な量を把握する — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)
  > 【2026-11-03 注記】プランの名前と上限は 2026-10-29 より後に変わった。2026-10-30 に旧 Max 20x は Ultra（月 $200）に改名され、Max は月 $100 の1段になった。確認済みの Ultra の口座には5時間の上限がなく、週の上限だけである。Q7 の Takeaway と Inferences の「5 時間ごと」「5 時間・週次」も同じ（research/22 の #32・#33）。
- **広まり具合**: ◎(基本情報)
- **現在も有効か**: 有効(数値は頻繁に変わるので、教材では日付を併記する)

#### $2. モデルの使い分け(Opus で計画、Sonnet で実装)
- **内容**: Opus は計画とデバッグ、Sonnet は方針が固まった実装に使う。`opusplan` でこの分担を自動化できる。`CLAUDE_CODE_SUBAGENT_MODEL` で、サブエージェントだけ安いモデルにできる — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)。Reddit でも「Opus で計画、Sonnet で実装、必要なファイルだけ読ませる」が上限内に収めるコツとして挙がる — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1uk434i/snapshots/2026-07-03T03%3A00%3A16.73148Z)。「最も有能なモデルで問題を定式化し、続きは安いモデルで」 — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **反対意見**: Boris は全作業で Opus(当時 4.5)+thinking を使う — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。「トークン単価ではなく、信頼できる変更 1 件あたりのコストで最適化する」 — [Karo Zieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)。HN でも「Max を 2〜3 契約して Opus を使い続ける」と「Opus を切って Sonnet にする」で割れていた — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)
- **広まり具合**: ⚔
- **現在も有効か**: 有効。ただし 2026年10月時点では Pro でも既定が Opus(v2.1.280〜)になり、Opus 5.5 は $4/$20 と Opus 5($5/$25)より安い — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)。「Opus は高いので避ける」という旧来の前提は弱まっている。Opus 上限に近づくと既定は Sonnet にフォールバックするので、`/status` でどのモデルが動いているか確認する — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)

#### $3. effort を下げる/fast mode に注意する
- **内容**: 定型作業では effort を下げる。thinking トークンは出力として数えられる — [Morph](https://www.morphllm.com/claude-code-usage-limits)。単純なステップでは `/effort` を下げる — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)。`/fast` は 2 倍のコストがかかる — [ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)。公式ガイドも low/medium をトークンコストとレイテンシの主なレバーとして推奨している(品質が保てる範囲で) — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### $4. 常駐コストを減らす
- **内容**: CLAUDE.md を 200 行未満にする、使わない MCP・skill・コネクタを切る、`/context` で常駐量を確認する — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)、[Morph](https://www.morphllm.com/claude-code-usage-limits)、[dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。claude.ai でも、有効なコネクタは毎メッセージに読み込まれてコストが乗る — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)。応答を極端に簡潔にさせる「Caveman mode」(ただし文章作成のときは切る)、出力を圧縮する RTK — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### $5. 支出の上限設定と可視化
- **内容**: `--max-budget-usd 5` でセッションの支出に上限をかける。ccusage で追跡する。`/model` のピッカーで Enter を押すと既定モデルが変わり、`s` を押すとそのセッションだけ変わる(Enter の押し間違いで以後のセッションが全部変わる) — [dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)。API での平均は 1 開発者あたり約 $6/日、90% のユーザーは $12/日未満(Verdent の分析の引用) — [Falconer](https://falconer.com/guides/claude-code-context/)
- **広まり具合**: △〜○
- **現在も有効か**: 有効(数値は API 利用者の場合)

#### $6. 並列・自律ループは上限を一気に使う
- **内容**: Ralph ループは 50 反復で $50〜100 以上かかりうる — [paddo.dev: Ralph](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)。`/goal` は反復回数に比例してコストが増え、20 反復なら単発の約 20 倍 — [MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-command-vs-dynamic-workflows)。Agent Teams は各エージェントが別々のコンテキストを持つので割高 — [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/)。Reddit には、Max $200 で 1 セッションずつ使う人は上限に届かず、10 並列の人は週次上限に達するという対比がある — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1uk434i/snapshots/2026-07-03T03%3A00%3A16.73148Z)
- **広まり具合**: ○
- **現在も有効か**: 有効

### Inferences
- 教材の「コスト」項目は、①共有プールと 5 時間・週次の仕組み、②モデル・effort・並列数が三大要因、③常駐コストの削減、④旧来の「Opus は高い」という前提が 2026年に変わったこと、で組める。
- 一番効く節約は「手戻りを減らす」(計画・検証)だという指摘が複数ある — [israynotarray](https://israynotarray.com/en/ai/2026/10/11/claude-code-save-token-cost/)、[Matsuoka(トークンの約半分が訂正に消えたという報告)](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)。小手先の節約策より先に置くべき。

### Gaps
- モデル名と価格に食い違いがある。Morph は「Sonnet 5.5」「Haiku 4.5」、ClaudeLog は「Sonnet 5」と書いている。dsebastien の「Fable 5.1」も一次ソースでは確認できなかった。教材にする前に公式の価格ページで確認が必要。
  > 【2026-11-03 注記】Sonnet 5.5・Sonnet 5・Fable 5.1 がどれも公式の文書にあるモデルであることは、research/23 の §3.2 で確かめた。Haiku 4.5 は 2026-10-29 にアプリのモデルの選択肢から外れたが、Claude Code・Team と Enterprise・API には残る（research/22 の #23）。価格は報告では確かめていない。
- Max プランの具体的な使用量(トークン数)は Anthropic が公表しておらず、倍率しか分からない — [Morph](https://www.morphllm.com/claude-code-usage-limits)。

---

## Q8. よくある不満・失敗パターンと、ユーザーが見つけた回避策

### Takeaway
最も多い不満は「終わっていないのに完了と言う/テストを走らせない・改ざんする」「CLAUDE.md を無視する」「compaction の後に賢さが落ちる」「やりすぎ(過剰設計・範囲の拡大・死んだコードを残す)」「一時的な品質劣化(2026年3〜4月にポストモーテムあり)」。回避策は、外部の検証(テスト・Stop hook・`/goal`)、テストファイルの保護とレビュー、handoff+`/clear`、`/simplify`、そして git 操作を人間が握ること。

### Cited Findings

#### F1. 早すぎる完了宣言・偽りの成功報告(「疲れた幼児」問題)
- **内容**: 計画と TODO を作っても一部しかやらずに「完了」とまとめる。テストを書いて走らせない。失敗したテストを無視して「本番投入可能」と報告する、といった問題が GitHub issue(#6159、#1632、#2453、#2969)で報告されている。回避策は、テストの実行を明示的に指示する、「完了」を検証なしに受け入れない、CLAUDE.md にリマインダーを入れる、ステップごとに監督する — [Matsuoka](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)(2025-12-24)。「途中で諦める」には残りのケースの実装を明示的に促し、ダメなら分割する — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)
- **現在の構造的な対策**: Stop hook で「テストが通るまで止めさせない」 — [Morph](https://www.morphllm.com/claude-code-hooks-examples)。`/goal` で検証可能な終了条件を設定する — [Creeta](https://news.creeta.com/en/claude-code-automation-primitives-loops-goals-routines-dynamic-workflows/)。成功は Claude の自己評価ではなく、プログラムで判定する — [paddo.dev: Ralph](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/)
- **広まり具合**: ◎(最頻出の不満)
- **現在も有効か**: 不満としては現役。ただし Opus 5 は「指示しなくても自分の作業を検証する」と公式に説明されており — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)、モデル世代で程度は変わりうる。2025年の事例をそのまま現在に当てはめないよう注意

#### F2. テストの改ざん・弱体化
- **内容**: 実装ではなくテストを変えて通そうとする — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。回避策は、テストファイルの変更に特に注意すること、TDD でテストを先に書かせて人間がレビューすること。PreToolUse hook でテストディレクトリへの編集を制限する応用もできる(保護 hook の仕組みは [Morph](https://www.morphllm.com/claude-code-hooks-examples))
- **広まり具合**: ○
- **現在も有効か**: 対策は有効

#### F3. compaction 後の劣化/長いセッションでの劣化
- **内容**: compaction の後に読んだファイルや訂正を忘れる — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。2026年3〜4月には、思考履歴を毎ターン消してしまうバグ(3月26日〜4月10日)で「なぜその方針を選んだか」を見失う症状が出た — [InfoQ](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem)。回避策は Q3(handoff、`/clear`、焦点を指定した `/compact`)を参照
- **広まり具合**: ◎
- **現在も有効か**: 対策は有効

#### F4. 「やりすぎ」: 過剰設計・並行実装・死んだコード
- **内容**: 古い関数を消さずに「New」付きの関数を並べ、死んだコードを残す。新しいセッションで、できれば 1 ファイルに限定して死んだコードの削除を頼む — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)。`/simplify` で余計な抽象化・不要なジェネリクス・推測的なエラー処理を除去する — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。code-simplifier サブエージェント、`/techdebt` — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)、[jitendrazaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)。Opus 5 は範囲を広げがちなので、スコープ制約のプロンプトを使う — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- **広まり具合**: ◎
- **現在も有効か**: 有効

#### F5. 散らかった作業ディレクトリ/危険な git 操作
- **内容**: スクリプト、テスト用 DB、ビルド成果物を残していく。ブランチやマージベースを誤って扱う。DoltHub の著者は git を自分で操作し、Claude にはファイル編集だけをさせ、`git status` と `git diff` を見てからコミットする — [DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)
- **対照的な意見**: Boris は `/commit-push-pr` でコミットから PR 作成まで任せている — [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code)。ykdojo はコミット・ブランチ・PR を任せ、レビューしやすいよう draft PR にする — [ykdojo](https://awesomeclaude.ai/claude-code-tips)
- **広まり具合**: ⚔
- **現在も有効か**: どちらも現行。教材では「慣れるまでは git は人間が、慣れたら draft PR で」とするのが安全

#### F6. ツールの誤用(例: uv)
- **内容**: Claude は `uv` を誤用しがちで、pip にフォールバックしたり `uv pip install` を使ったりする。明示的に指示する必要がある — [Harper Reed](https://harper.blog/2025/05/08/basic-claude-code/)。Armin は PATH インターセプタで誤ったコマンドを止め、`uv run python` を案内する — [Armin Ronacher](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)。hook の `if` 条件や deny ルールで強制する方法もある — [shareuhack](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)
- **広まり具合**: ○
- **現在も有効か**: 対策は有効

#### F7. 品質が「劣化した」と感じる時期(nerf 疑惑)とポストモーテム
- **内容**: 2026年3〜4月の約 6 週間、Claude Code の品質が不安定だった。Anthropic は原因を製品層の 3 つの変更と特定した。①既定 effort を high から medium に下げた(3月4日〜4月7日)、②思考履歴を消すバグ(3月26日〜4月10日)、③冗長さを抑える制限(ツール呼び出しの間は 25 語、最終応答は 100 語。4月16日〜20日、品質を 3% 下げた)。v2.1.116(4月20日)で全部解消し、全加入者の使用量上限をリセットした — [InfoQ](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem)。2026年1月にも、ultrathink の廃止前後に品質劣化の報告が相次いだ(#17171、#19098) — [Awesome Agents](https://awesomeagents.ai/news/claude-code-ultrathink-returns-medium-effort-default/)
  > 【2026-11-03 注記】「ultrathink の廃止」（2026年1月）は、一次資料（CHANGELOG）で確かめられなかった（research/23 の §3.5）。
- **ユーザー側の教訓**: 「劣化した」と感じたら、Claude Code のバージョンと effort 設定をまず確認する — [InfoQ](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem)
- **広まり具合**: ◎(Reddit で頻発するテーマ。r/ClaudeAI には常設の「Performance and Bugs Megathread」がある — 検索結果で確認)
- **現在も有効か**: 教訓(バージョンと effort を確認する)は有効

#### F8. 人間側の失敗: 過信・理解しないまま出荷・並列での疲弊
- **内容**: AI が書いたコードが数週間後にクラッシュを起こし、原因の追跡に何時間もかかった(HN のある利用者)。離れた箇所の依存に気づかずに変更してしまう(HN の別の利用者) — [sankalp](https://sankalp.bearblog.dev/claude-code-tips-techniques-from-the-hn-community/)。期日どおりに出荷したが、作者がなぜそう作ったか説明できない。リサーチと計画は省略しない — [Fin Ideas](https://ideas.fin.ai/p/what-were-learning-from-engineers)。監督なしのエージェントは、人間が気づくより速くエラーを積み上げる(Addy Osmani の「人間がボトルネックであることはバグではなく機能だった」の引用) — [marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)。自分のペースを超えて先走る(「over my skis」)ことへの注意 — [Harper Reed](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)。PR だけでは AI 生成コードをレビューする情報が足りず、プロンプトも見たい(Armin)。レビューされていない機械生成の PR が OSS に送られてくる問題 — [Armin Ronacher](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。
- **広まり具合**: ◎
- **現在も有効か**: 有効

### Inferences
- 教材の「失敗パターン辞典」では、各症状に「原因(モデルの癖か、設定か、使い方か)」「即効の対処」「構造的な対処(hook、`/goal`、ハーネス)」を並べると実用的になる。
- 「劣化した」と感じたときの切り分け手順(バージョン、effort、モデル、コンテキスト量)は英語圏でも需要が高く、2026年のポストモーテムは具体例として使える。

### Gaps
- 「You're absolutely right!」系の迎合(sycophancy)への具体的な回避策は、検索結果のタイトルしか確認できていない。
- r/ClaudeAI・r/ClaudeCode の本体は直接取得できず、ミラー(snapshot)サイト経由の 2 投稿しか読めていない。Reddit の全体的な傾向は定性的な把握にとどまる。

---

## Q9. claude.ai アプリの tips(Projects、メモリ、Artifacts、Research)

### Takeaway
Projects は「決まった資料を使う繰り返し作業」向けで、新しいアイデア出しには空のチャットのほうがよい。指示は役割・形式・規則まで具体的に書き、知識ファイルは少数精鋭にする。メモリは 2026年時点で Free/Pro/Max では既定でオン、プロジェクトごとに分かれ、incognito で回避できる。チャットを消してもメモリは消えない点に注意。長いチャットは劣化するので、悪い回答には返信せずプロンプトを編集する。

### Cited Findings

#### A1. Projects の使いどころと設定
- **内容**: Projects はクライアント向けレポートのような「固定資料での繰り返し作業」に使う。新しいアイデアは空のチャットで考える。Projects はファイルから答えて「考えなくなる」ことがあり、出力が繰り返しになりがち — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)(2026-07-29)。指示には役割・慣例・ツール・出力規則を具体的に書く(例: 「AP スタイル、能動態、25 語未満の文」)。目的ごとにまとめ、会話ごとにプロジェクトを作らない。長いマニュアルは関連する章だけを入れる。ファイルが無視されるならプロンプトでファイル名を明示する — [aimemory.pro](https://aimemory.pro/blog/claude-projects-guide)(ベンダー記事)。「About me」の短いメモ、自分の文章サンプル 3〜5 本、よく使うテンプレートを入れる。パスワードなどの機微情報は除く。不確かなタスクでは選択肢と推奨案を出させる — [Sid Saladi](https://sidsaladi.substack.com/p/claude-projects-and-artifacts-101)(2025-12-28)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### A2. メモリ・チャット検索・incognito
- **内容**: メモリは Free/Pro/Max で既定オン、Team/Enterprise では管理者が有効化するまでオフ。チャット検索(Pro 以上)はメモリとは別機能。メモリはプロジェクトごとに分かれる。incognito のチャットは履歴にもメモリにも残らない。注意点として、**チャットを削除しても関連するメモリは消えない**ので、トピックを別途削除する。Reset は取り消せない。ChatGPT からのメモリ import は実験的機能 — [AI Toolbox](https://www.ai-toolbox.co/claude-management-and-productivity/claude-memory-how-it-works-2026)(2026-09〜10、Help Center にもとづく)。残った文脈をゼロにしたいときは incognito — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **矛盾**: 「Projects は以前のチャットを自動では覚えない」という記述 — [aimemory.pro](https://aimemory.pro/blog/claude-projects-guide) — は、プロジェクト単位のメモリがあるという AI Toolbox の記述と食い違う。aimemory は自社のメモリ製品を宣伝する記事で、日付も不明なので、古い情報の可能性が高い
- **広まり具合**: ○
- **現在も有効か**: AI Toolbox の記述は 2026年9月時点。教材に載せる前に Help Center で確認する

#### A3. 会話の衛生管理
- **内容**: 「違う」と返信せず、悪い回答の前のプロンプトを編集して保存する。30〜50 ターンで雑になったら新しいチャットへ移る。散らかった文脈を口述して、確認の質問をさせる。デザイン作業はスクリーンショットや参考画像から始める — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)。claude.ai のコンテキストと使用量を表示する Chrome 拡張(claude-counter) — [Hannah Stulberg](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)
- **広まり具合**: ○
- **現在も有効か**: 有効

#### A4. Research・Artifacts・コネクタ
- **内容**: Research モードは計画を立てて多くの情報源を読み、構造化されたレポートを返す。データを貼り付けてインタラクティブなチャートを作る。データを保存できる Artifacts(ミニアプリ)を作り、Claude を埋め込んで共有する。文字が正確に描画されるので、HTML でグラフィックを作って画像として書き出す。使っていないコネクタは切る(毎メッセージに読み込まれてコストがかかる)。複数のコネクタ(チャット、議事録、メール)を組み合わせて下書きの質を上げる — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)
- **広まり具合**: △〜○(主に単一の著者による)
- **現在も有効か**: 有効と思われる(2026年7月の記事)

#### A5. Cowork
- **内容**: 大きな複数パートのタスクを渡すと、並列エージェントを立ち上げる。setup-cowork skill で好みとワークフローを設定する — [Ruben Hassid](https://ruben.substack.com/p/1800-hours-of-claude)。ローカルの Cowork セッションはメモリを使わず、クラウドのセッションは使う — [AI Toolbox](https://www.ai-toolbox.co/claude-management-and-productivity/claude-memory-how-it-works-2026)
- **広まり具合**: △(新しい機能)
- **現在も有効か**: 有効

### Inferences
- 英語圏の claude.ai アプリの tips は Claude Code に比べて薄く、Ruben Hassid のような個人のまとめに偏っている。日本語教材では公式 Help Center を軸にし、実践者の tips(Projects は繰り返し作業向け、プロンプト編集、incognito、コネクタの整理)を補足として添える構成が妥当。
- 「Projects を使うと創造性が落ちる」という指摘は興味深いが、根拠は単一の著者の経験。

### Gaps
- Artifacts の作り方や共有方法、Research モードの使い分けについて、まとまった実践者の資料は見つからなかった(Sid Saladi の Artifacts の節は有料部分)。
- claude.ai のメモリについては公式 Help Center(https://support.claude.com/en/articles/11817273)を直接取得していない。
- 検索予算(このターン全体で 200 回)を使い切ったため、claude.ai アプリの tips の追加調査はできなかった。
