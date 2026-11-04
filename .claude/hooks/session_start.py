#!/usr/bin/env python3
"""claude-atlas の SessionStart の hook（.claude/README.md の H4）。知らせるだけで、何も止めない。

制作の印 state/production があり、環境に API キーかクラウドの事業者の認証を使う変数があるときだけ、利用者（systemMessage）と
Claude（additionalContext）に「従量の課金になる」と知らせる。変数の値は読まず、名前だけを出す。
止める確かめは tools/check_templates.py の中の必須の確かめが受け持つ（design §8.7・§10.5、design-review の DR-08）。
印がないとき（読者がリポジトリを開いたとき）は何もしないで終わる。標準のライブラリだけで動く（Python 3.8 以上）。
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRODUCTION_MARK = os.path.join(ROOT, "state", "production")

KEY_RE = re.compile(r"^ANTHROPIC_(?:[A-Z0-9]+_)*(?:API_KEY|AUTH_TOKEN)$")   # ANTHROPIC_API_KEY・ANTHROPIC_AUTH_TOKEN など
PROVIDER_FLAGS = ("CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "CLAUDE_CODE_USE_FOUNDRY")
OFF = {"", "0", "false", "no", "off"}

MESSAGE = ("制作の印（state/production）があり、環境に {names} がある。API キーやクラウドの事業者の認証があると、"
           "claude -p などはそれを使い、従量の課金になる（.claude/README.md の H4）。雛形の実機の確認"
           "（check_templates.py --live）の前に、この変数を外す。")


def billing_vars(env) -> list[str]:
    names = sorted(k for k, v in env.items() if KEY_RE.match(k) and v)
    names += [k for k in PROVIDER_FLAGS if env.get(k, "").strip().lower() not in OFF]
    return names


def main() -> int:
    try:
        sys.stdin.buffer.read()
    except OSError:
        pass
    try:
        if not os.path.exists(PRODUCTION_MARK):
            return 0
        names = billing_vars(os.environ)
        if not names:
            return 0
        text = MESSAGE.format(names="・".join(names))
        out = {"systemMessage": text,
               "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}
        sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
    except Exception:  # noqa: BLE001  知らせるだけの hook なので、誤りでも何もしないで終わる
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
