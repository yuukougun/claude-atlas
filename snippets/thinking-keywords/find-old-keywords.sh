#!/bin/sh
# CLAUDE.md・スキル・保存した頼み方から、段階のキーワードの書き残しを探す。読むだけで、何も書き換えない
grep -rnIE "think (hard|harder|more)|ultrathink|熟考|よく考えて" \
  CLAUDE.md "$HOME/.claude/CLAUDE.md" .claude/ 2>/dev/null
