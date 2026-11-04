#!/usr/bin/env python3
# .claude/hooks/redirect-pip-to-uv.py
# PreToolUse（Bash）で、pip での導入を止め、決めたコマンド（uv）を理由とともに返す。
# 「uv pip install」は先頭が uv なので照合に当たらない。許すかどうかは規則として決める。
import json
import re
import sys

# コマンドの各部分の先頭にある pip（python -m pip を含む）の install・uninstall
PIP = re.compile(
    r"(?:^|&&|\|\||;|\|)\s*(?:python3?\s+-m\s+)?pip3?\s+(?:install|uninstall)\b"
)

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

if PIP.search(command):
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "このリポジトリでは Python の依存を uv で管理する。pip は使わない。"
                "パッケージの追加は `uv add <名前>`、コマンドの実行は `uv run <コマンド>` で行う。"
            ),
        }
    }
    print(json.dumps(result, ensure_ascii=False))

sys.exit(0)
