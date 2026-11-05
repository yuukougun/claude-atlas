#!/usr/bin/env bash
# 原本は変えず、UTF-8 の複製を作って、行数を突き合わせる
# 使い方：./to-utf8.sh 入力.csv 出力.csv [元の文字コード（既定は CP932）]
set -euo pipefail

src="${1:?入力のファイルを指定する}"
dst="${2:?出力のファイルを指定する}"
from="${3:-CP932}"

# 変換に失敗したときに、途中までの出力を残さない
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
iconv -f "$from" -t UTF-8 "$src" > "$tmp"
mv "$tmp" "$dst"
trap - EXIT

# 行数が同じか（文字コードを変えても行は増減しない）
echo "行数：入力 $(wc -l < "$src")、出力 $(wc -l < "$dst")"

# 日本語が読めるかを、先頭の数行で目で確かめる
head -n 3 "$dst"
