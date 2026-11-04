#!/usr/bin/env bash
# 手元の設定ファイルから、台帳に載っている古い言い回しを探す。読むだけで、何も書き換えない。
# 使い方：プロジェクトの根で  bash find-old-advice.sh
# 出力の行頭の [#…] は台帳の行の id。台帳のページの URL の末尾に付けると、その行へ移る。
# 見つかった行は、古いと決まったわけではなく、疑う手がかりである。
# 探すのは、台帳のうち言い回しで探せる行だけ。出力が空でも、古い助言が残っていないとは言えない。
# 台帳に行が足されたら、下の rules にも言い回しを足す。

# 探す場所。なければ飛ばす。~/.claude/projects/ の会話の記録は、過去の会話に言い回しが出るだけなので探さない
targets=(
  CLAUDE.md CLAUDE.local.md .mcp.json .github/workflows
  .claude/settings.json .claude/settings.local.json
  .claude/commands .claude/skills .claude/agents .claude/rules
  "$HOME/.claude/CLAUDE.md" "$HOME/.claude/settings.json"
  "$HOME/.claude/commands" "$HOME/.claude/skills" "$HOME/.claude/agents" "$HOME/.claude/rules"
  "$HOME/.bashrc" "$HOME/.zshrc"
)

# 台帳の行の id | 探す言い回し（grep -E の正規表現）
rules=(
  'important-caps|IMPORTANT|YOU MUST|NEVER'
  'think-hard-keywords|think hard|think harder|熟考|よく考えて'
  'keep-going-dont-be-lazy|keep going|don.t stop|don.t be lazy|loop until done|最後までやり切れ'
  'add-double-check|double-check|re-verify|最後に見直して'
  'architecture-in-claude-md|├──|└──'
  'yolo-skip-permissions|dangerously-skip-permissions|bypassPermissions'
  'code-on-the-web-remote|claude --remote( |$)'
  'slash-cost-and-stats|/cost|/stats'
  'fork-to-branch|/fork'
  'removed-commands|/vim|/tag|/pr-comments|/ultraplan|TaskOutput'
  'mcp-sse-transport|"type" *: *"sse"|--transport sse'
  'action-beta-direct-prompt|claude-code-action@beta|direct_prompt'
  'workflow-keyword-extra-usage|extra usage|/extra-usage'
)

for rule in "${rules[@]}"; do
  id=${rule%%|*}
  pattern=${rule#*|}
  grep -rnEI -e "$pattern" "${targets[@]}" 2>/dev/null | sed "s|^|[#$id] |"
done
