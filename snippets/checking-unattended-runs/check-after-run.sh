#!/usr/bin/env bash
# 無人の実行の後に、Claude の外で結果を確かめる例。
# 使い方：./check-after-run.sh <始めの HEAD> <claude -p の終了コード> <保存した出力のファイル>
# 再実行のコマンド（ここでは npm test）は、自分のプロジェクトのものに置き換える。
set -euo pipefail

start_head=$1
claude_exit=$2
output_file=$3

echo "== 1. 終了コード（0 でも成功とは決めない）"
echo "claude -p の終了コード: ${claude_exit}"

echo "== 2. 出力（空なら失敗として扱う）"
if [ ! -s "$output_file" ]; then
  echo "出力が空。失敗として扱う" >&2
  exit 1
fi
wc -c "$output_file"
tail -n 5 "$output_file"

echo "== 3. 差分（始めの HEAD から今まで）"
git log --oneline "${start_head}..HEAD"
git diff --stat "${start_head}..HEAD"
git status --short
echo "-- テスト・設定・CI に当たるファイルの変更（先に読む）"
git diff --name-only "${start_head}..HEAD" | grep -E '(test|spec|\.github/|\.claude/)' || echo "(該当なし)"

echo "== 4. Claude の外で再実行（件数が始めと同じかを見る）"
npm test
