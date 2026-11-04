#!/usr/bin/env python3
# .claude/hooks/stop-until-tests-pass.py
# Stop で、テストが通るまでターンを終えさせない。
# 差し戻しは MAX_BLOCKS 回までにする。それでも通らなければ、通っていないことを画面に残して終わらせる。
# 組み込みの上限（ツールの呼び出しを挟まずに続けて止められる回数）とは別に、自分の上限を持つためである。
import json
import subprocess
import sys
import tempfile
from pathlib import Path

TEST_CMD = ["pytest", "-q", "-x"]  # 確かめるコマンド。自分のプロジェクトのものに替える
TIMEOUT = 300  # 秒。テストがこれより長くかかるなら、確かめる範囲を絞る
MAX_BLOCKS = 3  # 差し戻す回数の上限
TAIL_LINES = 40  # 理由に載せる出力の行数

data = json.load(sys.stdin)
counter = Path(tempfile.gettempdir()) / f"stop-hook-{data.get('session_id', 'unknown')}.count"

# stop_hook_active が偽なら、Stop フックの差し戻しで続いているのではない新しい終わりである。数え直す。
if not data.get("stop_hook_active"):
    counter.unlink(missing_ok=True)

try:
    done = subprocess.run(
        TEST_CMD,
        cwd=data.get("cwd"),
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )
except (OSError, subprocess.TimeoutExpired) as error:
    # 確かめを走らせられないときは、止めずに通す。差し戻しても直せないので、ループになるだけである。
    print(f"テストを走らせられなかったので、確かめずに終わらせる: {error}", file=sys.stderr)
    sys.exit(0)

if done.returncode == 0:
    counter.unlink(missing_ok=True)
    sys.exit(0)

blocks = int(counter.read_text()) if counter.exists() else 0
if blocks >= MAX_BLOCKS:
    counter.unlink(missing_ok=True)
    notice = f"テストが通らないまま、差し戻しを {MAX_BLOCKS} 回で打ち切った。確かめが通っていない。"
    print(json.dumps({"systemMessage": notice}, ensure_ascii=False))
    sys.exit(0)

counter.write_text(str(blocks + 1))
output = (done.stdout + done.stderr).splitlines()[-TAIL_LINES:]
reason = (
    "テストがまだ通らないので、終わらせない。"
    "次の出力の失敗を直してから、もう一度テストを走らせて結果を示すこと。\n" + "\n".join(output)
)
print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
sys.exit(0)
