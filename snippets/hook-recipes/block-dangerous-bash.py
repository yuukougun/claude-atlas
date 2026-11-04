#!/usr/bin/env python3
# .claude/hooks/block-dangerous-bash.py
# PreToolUse（Bash）で、取り返しのつかない操作を止め、理由と代わりを返す。
# 文字列の照合なので、書き方を変えた同じ操作は拾えない。確実に止めたい操作は deny ルールと組む。
import json
import re
import sys

# (照合する式, 止める理由と代わりの手段)
DANGEROUS = [
    (
        r"\brm\s+-[a-zA-Z]*(?:rf|fr)[a-zA-Z]*\s+(?:/|~|\$HOME|\.|\*)(?:\s|$)",
        "ルート・ホーム・カレントディレクトリ全体の再帰削除は止めた。"
        "消したい対象を具体的なパスで指定し直す。",
    ),
    (
        r"\bgit\s+push\b.*(?:--force(?![-\w])|\s-f(?:\s|$))",
        "git push の強制上書きは止めた。"
        "上書きが要るなら --force-with-lease を使うか、利用者に確認する。",
    ),
    (
        r"\bgit\s+reset\s+--hard\b",
        "git reset --hard は未コミットの変更を消すので止めた。"
        "戻したいファイルを git restore で指定するか、git stash で退避する。",
    ),
]

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

for pattern, reason in DANGEROUS:
    if re.search(pattern, command):
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
        print(json.dumps(result, ensure_ascii=False))
        break

sys.exit(0)
