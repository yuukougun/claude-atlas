#!/bin/bash
# ステータスラインに、文脈の使用率と、短い周期の上限の使用率を 1 行で出す。
# Claude Code が標準入力に渡すセッションの JSON を読み、値のある項目だけを並べる。
input=$(cat)

ctx=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
limit=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')

line=""
[ -n "$ctx" ] && line="文脈 $(printf '%.0f' "$ctx")%"
[ -n "$limit" ] && line="${line:+$line | }上限 $(printf '%.0f' "$limit")%"

echo "${line:-(値なし)}"
