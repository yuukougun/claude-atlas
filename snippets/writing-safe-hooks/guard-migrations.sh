#!/usr/bin/env bash
# .claude/hooks/guard-migrations.sh
# PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
# 失敗は止めに倒す：判定に要る道具が無い・入力が読めないときは exit 2 で終える。
# 終わり方は exit 0（通す）か exit 2（止める）のどちらかに決め、途中の失敗を 0 で終わらせない。

if ! command -v jq >/dev/null 2>&1; then
  echo "jq が見つからず判定できないため、操作を止める。jq を入れてから再開する。" >&2
  exit 2
fi

input=$(cat)
path=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty') || {
  echo "フックの入力を読めず判定できないため、操作を止める。" >&2
  exit 2
}

case "$path" in
  */migrations/*)
    if [ -e "$path" ]; then
      echo "このリポジトリでは、適用済みの migration は書き換えない。変更は新しい番号の migration ファイルを追加して行う。（対象：$path）" >&2
      exit 2
    fi
    ;;
esac

exit 0
