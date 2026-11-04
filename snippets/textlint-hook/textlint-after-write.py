#!/usr/bin/env python3
"""Edit・Write の後に、書いた文章のファイルを textlint で検査し、違反を Claude に返す。

- 違反が残っていれば、標準エラーに一覧を書いて exit 2 で終わる（PostToolUse では、標準エラーが Claude に返る）
- 検査の対象外のファイルは、何もせず exit 0 で終わる
- textlint を起動できないときも exit 2 で終わる（黙って検査が止まるのを避ける）
"""
import json
import os
import subprocess
import sys

TARGET_SUFFIXES = (".md", ".mdx", ".txt")  # 検査する拡張子。広げすぎない
MAX_LINES = 20  # Claude に返す違反の行数の上限。文脈を食いつぶさないため


def main() -> int:
    try:
        path = json.load(sys.stdin)["tool_input"]["file_path"]
    except (ValueError, KeyError, TypeError):
        print("textlint フック：入力から file_path を読めなかった。", file=sys.stderr)
        return 2

    if not path.endswith(TARGET_SUFFIXES) or not os.path.isfile(path):
        return 0

    project = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    try:
        # --no-install：未導入のときに、勝手に取得して走らせない
        result = subprocess.run(
            ["npx", "--no-install", "textlint", "--format", "unix", path],
            cwd=project,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"textlint フック：textlint を実行できなかった（{e}）。", file=sys.stderr)
        return 2

    if result.returncode == 0:
        return 0

    lines = (result.stdout or result.stderr).strip().splitlines()
    if result.returncode != 1:
        # 1 は「違反あり」。それ以外は textlint 自体の失敗（設定の誤りなど）
        print("textlint フック：textlint が異常終了した。設定を確かめること。", file=sys.stderr)
    else:
        print(f"textlint の違反が {path} に残っている。次の箇所を直すこと。", file=sys.stderr)
    for line in lines[:MAX_LINES]:
        print(line, file=sys.stderr)
    if len(lines) > MAX_LINES:
        print(f"（ほか {len(lines) - MAX_LINES} 行。先に上の違反を直すこと）", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
