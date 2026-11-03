# 工程4の直し：重なった別名の主のページ（DR-19 d）

- メインが道具で作った（2026-11-04）。別名（aliases）を小文字にし、空白を除いて比べた。題名と同じ語が別のページの別名にあるものも入れた
- 主のページは見当の規則で選んだ：題名がその語 → 題名にその語を含む → 機能（feature）のページ → 分野の並びで最初。違うと思えば、受け持ちの担当が報告に理由を書いて替えてよい
- 直し方：主でないページからその別名を外す。ただし、そのページが扱う別の機能の公式の名前で、外すと引けなくなるものは残し、報告に書く

重なり：49語

| 別名 | 主のページ | 選んだ理由 | 外す側のページ |
| --- | --- | --- | --- |
| ステートレス | rereads-whole-history（basics） | 分野の並びで最初（見当） | stateless-messages-api（api） |
| compaction | what-survives-compaction（basics） | 題名にこの語を含む | compact-and-auto-compact（context） |
| ツールの呼び出し | agent-loop（basics） | 分野の並びで最初（見当） | tool-use-loop（api） |
| thinking | how-thinking-works（basics） | 題名にこの語を含む | search-research-thinking（app） |
| extended thinking | how-thinking-works（basics） | 分野の並びで最初（見当） | search-research-thinking（app） |
| 過度な一般化 | summary-overgeneralization（basics） | 題名にこの語を含む | summary-overstates-source（symptoms） |
| 要約の言い過ぎ | summary-overgeneralization（basics） | 分野の並びで最初（見当） | summary-overstates-source（symptoms） |
| sycophancy | sycophancy（basics） | 題名にこの語を含む | caves-when-pushed（symptoms） |
| reward hacking | reward-hacking（basics） | 題名にこの語を含む | rewrote-tests-to-pass（symptoms） |
| prompt injection | data-vs-instructions（basics） | 題名にこの語を含む | prompt-injection-in-practice（safety） |
| 間接プロンプトインジェクション | data-vs-instructions（basics） | 分野の並びで最初（見当） | prompt-injection-in-practice（safety） |
| 拡張思考 | effort-levels（models） | 機能のページ | how-thinking-works（basics） |
| 性能が落ちた | suspected-degradation（models） | 分野の並びで最初（見当） | seems-less-capable（symptoms） |
| 提案だけで止まる | suggest-or-do（prompting） | 分野の並びで最初（見当） | keeps-stopping（symptoms） |
| 自動圧縮 | compact-and-auto-compact（context） | 題名にこの語を含む | what-survives-compaction（basics） |
| /context | inspect-context（context） | 題名にこの語を含む | usage-context-statusline（cli） |
| Research | using-research（app） | 機能のページ | search-research-thinking（app） |
| /deep-research | using-research（app） | 機能のページ | dynamic-workflows（delegate） |
| Skills | skills-in-the-app（app） | 機能のページ | how-skills-load（extend） |
| Agent Skills | skills-in-the-app（app） | 機能のページ | how-skills-load（extend） |
| Plugins | plugins-in-the-app（app） | 機能のページ | plugins-and-marketplaces（extend） |
| permission modes | permission-modes-in-the-app（app） | 機能のページ | permission-modes-overview（cli） |
| Scheduled tasks | tasks-and-schedules-in-the-app（app） | 機能のページ | loop-and-scheduling（delegate） |
| 組織の指示 | shared-projects-and-org-skills（app） | 機能のページ | where-to-put-instructions（app） |
| 音声入力 | voice-and-mobile（app） | 機能のページ | images-and-voice（prompting） |
| voice mode | voice-and-mobile（app） | 機能のページ | images-and-voice（prompting） |
| Esc を2回 | checkpoints-and-rewind（cli） | 機能のページ | rewind-dont-correct（context） |
| /cost | usage-context-statusline（cli） | 機能のページ | insights-and-usage-review（eval）、what-uses-up-limits（cost） |
| /stats | usage-context-statusline（cli） | 機能のページ | insights-and-usage-review（eval） |
| settings.local.json | settings-layers（cli） | 機能のページ | share-team-settings（team） |
| claude.ai/code | cloud-sessions-and-teleport（cli） | 機能のページ | claude-code-surfaces（surfaces） |
| Claude Code on the Web | cloud-sessions-and-teleport（cli） | 機能のページ | claude-code-surfaces（surfaces） |
| Remote Control | control-from-phone（cli） | 題名にこの語を含む | where-it-runs（surfaces） |
| subagent | writing-subagents（extend） | 機能のページ | subagent-isolation（basics） |
| .mcp.json | connecting-mcp（extend） | 機能のページ | share-team-settings（team） |
| 認知負債 | own-generated-code（verify） | 分野の並びで最初（見当） | how-much-understanding-to-keep（judgment） |
| managed settings | managed-settings-enforcement（enforce） | 機能のページ | org-managed-settings-and-mcp（team） |
| managed-settings.json | managed-settings-enforcement（enforce） | 機能のページ | org-managed-settings-and-mcp（team） |
| server-managed settings | managed-settings-enforcement（enforce） | 機能のページ | org-managed-settings-and-mcp（team） |
| 承認疲れ | approval-fatigue（safety） | 題名がこの語 | wrong-amount-of-approvals（symptoms） |
| tool poisoning | prompt-injection-in-practice（safety） | 分野の並びで最初（見当） | vetting-extensions（safety） |
| 破壊的な操作 | destructive-commands（safety） | 分野の並びで最初（見当） | deleted-something-important（symptoms） |
| 拒否された | when-requests-are-refused（safety） | 分野の並びで最初（見当） | refused-or-blocked（symptoms） |
| 分類器に止められた | when-requests-are-refused（safety） | 分野の並びで最初（見当） | refused-or-blocked（symptoms） |
| 自動化バイアス | over-reliance（judgment） | 分野の並びで最初（見当） | curb-sycophancy-and-overtrust（team） |
| prompt caching | prompt-caching-in-practice（api） | 機能のページ | why-prompt-caching（basics） |
| 経費精算 | paying-in-yen（cost） | 分野の並びで最初（見当） | office-paperwork（recipes） |
| 英語に戻る | keep-replies-in-japanese（japanese） | 分野の並びで最初（見当） | replies-in-english（symptoms） |
| 評価環境 | build-test-harness（recipes） | 分野の並びで最初（見当） | evaluators-by-format（contest） |
