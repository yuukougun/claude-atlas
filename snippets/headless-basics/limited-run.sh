#!/usr/bin/env bash
# 許す道具・止まる上限・出力の形式を明示して claude -p を動かす例。
# 値（--max-turns と --max-budget-usd）は例。自分の作業の大きさに合わせて決める。
set -euo pipefail

# 1. 許す道具を列挙し、列挙にない承認待ちは拒む（dontAsk）。上限と出力形式も渡す。
json=$(claude -p "npm test を実行し、失敗しているテストの原因を直す。直したら npm test をもう一度実行し、結果を報告する。" \
  --permission-mode dontAsk \
  --allowedTools "Read,Edit,Bash(npm test *)" \
  --max-turns 20 \
  --max-budget-usd 2 \
  --output-format json)

# 2. 要約を読む。ここで見るのは「Claude がどう言ったか」だけ。
printf '%s\n' "$json" | jq -r '.result'

# 3. 成功かどうかは終了コードと要約で決めず、自分でテストと差分を確かめる。
npm test
git diff --stat
