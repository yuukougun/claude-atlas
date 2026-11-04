#!/usr/bin/env python3
# .claude/hooks/block-migrations-json.py
# PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
# JSON の返し方：exit 0 で終え、stdout に判定と理由を JSON で出す。
import json
import os
import sys

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
in_migrations = "/migrations/" in path.replace("\\", "/")

if in_migrations and os.path.exists(path):
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "このリポジトリでは、適用済みの migration は書き換えない。"
                "変更は新しい番号の migration ファイルを追加して行う。"
            ),
        }
    }
    print(json.dumps(result, ensure_ascii=False))

sys.exit(0)
