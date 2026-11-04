#!/usr/bin/env bash
# 手元の Claude Code の版と、更新の通り道の設定を一度に控える。読むだけで、何も書き換えない。
set -u

echo "== 手元の版 =="
claude --version

echo
echo "== 更新の通り道と下限の設定（user・project・local） =="
grep -n -E '"(autoUpdatesChannel|minimumVersion)"' \
  ~/.claude/settings.json \
  .claude/settings.json \
  .claude/settings.local.json 2>/dev/null \
  || echo "設定に autoUpdatesChannel も minimumVersion もない（通り道は既定の latest）"

echo
echo "== 公開されている版の目印（npm が使える環境だけ） =="
# latest と stable が今どの版を指すかを見る。Homebrew や apt で入れた人も、版の比べ方は同じ。
npm view @anthropic-ai/claude-code dist-tags --json 2>/dev/null \
  || echo "npm が使えないので省略（公式の変更履歴で版を確かめる）"
