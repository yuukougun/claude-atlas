#!/usr/bin/env python3
# .claude/hooks/filter-test-output.py
# PreToolUse（Bash）で、pytest の実行コマンドを、失敗の行と最後の要約だけを残す形に書き換える。
# 書き換えは JSON の updatedInput で返す。元のコマンドの終了コードは pipefail で保つ。
import json
import re
import sys

# 当てる範囲を狭くする：pytest（uv run pytest を含む）で始まるコマンドだけ
TEST = re.compile(r"^\s*(?:uv run\s+)?pytest\b")

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

if not TEST.match(command):
    sys.exit(0)

filtered = (
    "set -o pipefail; "
    f"({command}) 2>&1 "
    "| grep -E -A3 'FAILED|ERROR|Error|passed|failed' "
    "| tail -n 80"
)

result = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {**data.get("tool_input", {}), "command": filtered},
    }
}
print(json.dumps(result, ensure_ascii=False))
sys.exit(0)
