#!/usr/bin/env bash
# 直近のタグから HEAD までのコミットを、1 行 1 件で標準出力に出す。
# 使い方: collect-changes.sh [起点にするタグ]
set -euo pipefail

since="${1:-}"
if [ -z "$since" ]; then
  since="$(git describe --tags --abbrev=0 2>/dev/null || true)"
fi
if [ -z "$since" ]; then
  echo "起点にするタグが見つからない。第 1 引数にタグ名を渡す。" >&2
  exit 1
fi

git log --no-merges --pretty='- %s (%h)' "${since}..HEAD"
