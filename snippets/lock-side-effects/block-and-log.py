#!/usr/bin/env python3
"""PreToolUse（matcher は Bash）：git push の強制上書きだけを止める。

- 当てる範囲は狭くする：`git push` に `--force` か `-f` が付くときだけ。
  `--force-with-lease` は止めない。
- 止めるときは、理由と代わりの手段を事実の形で返す。
- 止めた記録を 1 行ずつ残す（見直しの材料）。記録は PreToolUse の中で取る。
- 入力が読めないときは通す（この規則は、ほかの守りの代わりではない）。
"""
import json
import os
import re
import sys
import time

FORCE = re.compile(r"\bgit\s+push\b[^;&|]*?(?<![\w-])(--force|-f)(?![\w-])")

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

command = (data.get("tool_input") or {}).get("command", "")
if data.get("tool_name") != "Bash" or not FORCE.search(command):
    sys.exit(0)

root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
who = "担当" if data.get("agent_id") else "メイン"
line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')}\tR1\t{who}\t{command[:200]!r}\n"
try:
    with open(os.path.join(root, ".claude", "blocks.log"), "a", encoding="utf-8") as f:
        f.write(line)
except OSError:
    pass

reason = (
    "このリポジトリでは、共有ブランチへの強制上書きの push は行わない。"
    "履歴を直したいときは、新しいブランチへ通常の push をして、"
    "プルリクエストで相談する。"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }
}, ensure_ascii=False))
sys.exit(0)
