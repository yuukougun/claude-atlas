#!/usr/bin/env python3
# .claude/hooks/block-destructive.py
# PreToolUse（Bash）で、取り返しのつかない操作を止める。
# exit 2 の返し方：stderr の文がそのまま Claude への理由になる。
import json
import re
import shlex
import sys

# ホームやルートを丸ごと指す削除の対象
DANGEROUS_TARGETS = {
    "~", "~/", "~/*", "/", "/*",
    "$HOME", "${HOME}", "$HOME/", "${HOME}/", "$HOME/*", "${HOME}/*",
}
SQL_DESTRUCTIVE = re.compile(r"\b(drop\s+(database|table|schema)|truncate\s+table)\b", re.I)


def check(command: str) -> str | None:
    # && や ; や | で区切られた各コマンドを見る
    for segment in re.split(r"&&|\|\||[;&|\n]", command):
        try:
            tokens = shlex.split(segment)
        except ValueError:
            continue
        if not tokens:
            continue
        # git push の強制（--force、--force-with-lease、-f、+ref）
        if tokens[:2] == ["git", "push"]:
            rest = tokens[2:]
            if any(t.startswith("--force") or t == "-f" or t.startswith("+") for t in rest):
                return (
                    "強制 push は止めている。リモートの履歴は書き換えない。"
                    "通常の push で足りない場合は、人に相談する。"
                )
        # rm -r（-rf など）でホームやルートを指す削除
        if tokens[0] == "rm":
            flags = [t for t in tokens[1:] if t.startswith("-")]
            recursive = any(
                t == "--recursive" or (not t.startswith("--") and ("r" in t or "R" in t))
                for t in flags
            )
            if recursive and any(t in DANGEROUS_TARGETS for t in tokens[1:]):
                return (
                    "ホームやルートを丸ごと消す rm は止めている。"
                    "消す対象は、作業ディレクトリの中の具体的なパスで指定する。"
                )
    if SQL_DESTRUCTIVE.search(command):
        return (
            "DROP や TRUNCATE を含む SQL は止めている。"
            "データベースを壊す操作は、人が実行する。"
        )
    return None


data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")
reason = check(command)
if reason:
    print(reason, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
