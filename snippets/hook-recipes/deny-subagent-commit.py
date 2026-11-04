#!/usr/bin/env python3
# .claude/hooks/deny-subagent-commit.py
# PreToolUse（Bash）で、サブエージェントの中から来た git commit・git push だけを止める。
# 見分けは入力の agent_id の有無。agent_type は --agent で起動したメインにも付くので使わない。
import json
import re
import sys

# git のオプション（-C <パス>、-c <キー=値>、--long-option）を飛ばして commit・push を探す
GIT_WRITE = re.compile(
    r"\bgit\s+(?:(?:-C|-c)\s+\S+\s+|--\S+\s+)*(?:commit|push)\b"
)

data = json.load(sys.stdin)

# agent_id が無い＝メインの会話。何もせず通す
if not data.get("agent_id"):
    sys.exit(0)

command = data.get("tool_input", {}).get("command", "")

if GIT_WRITE.search(command):
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "担当（サブエージェント）は git commit と git push をしない。"
                "commit はメインが行う。変更したファイルと内容を報告に書いて終える。"
            ),
        }
    }
    print(json.dumps(result, ensure_ascii=False))

sys.exit(0)
