#!/usr/bin/env python3
# .claude/hooks/format-after-edit.py
# PostToolUse（Edit・Write）で、書き換えた Python のファイルに ruff format をかける。
# 整形に失敗したら exit 2 で stderr を返す。PostToolUse は操作を止められないが、
# stderr の文は Claude に届くので、構文エラーなどを直させられる。
import json
import subprocess
import sys

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")

# 当てる範囲を狭くする：Python のファイルだけ
if not path.endswith(".py"):
    sys.exit(0)

try:
    result = subprocess.run(
        ["ruff", "format", path], capture_output=True, text=True, timeout=30
    )
except (FileNotFoundError, subprocess.TimeoutExpired):
    # フォーマッタが無い・遅いときは、何もせず通す（整形は止める用途ではない）
    sys.exit(0)

if result.returncode != 0:
    print(
        f"ruff format が失敗した。構文エラーなら該当の行を直す。（対象：{path}）\n"
        f"{result.stderr}",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
