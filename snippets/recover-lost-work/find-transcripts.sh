#!/usr/bin/env bash
# 手元のトランスクリプトから、語が出てくるファイルの名前だけを新しい順に並べる。
# 読むだけで、何も書き換えない。中身は出さない（貼られた秘密を画面とログに写さないため）。
# 使い方: ./find-transcripts.sh '探す語'
set -u

word="${1:?探す語を1つ渡す}"
root="$HOME/.claude/projects"

if [ ! -d "$root" ]; then
  echo "$root がない。このマシンでは Claude Code の記録が見つからない。"
  exit 1
fi

# -F は正規表現にしない指定、-l はファイル名だけを出す指定
grep -rlF --include='*.jsonl' -- "$word" "$root" 2>/dev/null |
  while IFS= read -r f; do
    printf '%s\t%s\n' "$(date -r "$f" '+%Y-%m-%d %H:%M')" "$f"
  done | sort -r
