#!/usr/bin/env python3
# .claude/hooks/block-migrations-exit2.py
# PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
# exit 2 の返し方：stderr の文がそのまま Claude への理由になる。
import json
import os
import sys

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
in_migrations = "/migrations/" in path.replace("\\", "/")

if in_migrations and os.path.exists(path):
    print(
        "このリポジトリでは、適用済みの migration は書き換えない。"
        "変更は新しい番号の migration ファイルを追加して行う。"
        f"（対象：{path}）",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
