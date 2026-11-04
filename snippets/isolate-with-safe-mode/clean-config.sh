#!/usr/bin/env bash
# 自分の設定を何も持たない状態で Claude Code を起動する（--safe-mode でも不調が残るときの次の手）
# 実行前に、動いている Claude Code のセッションを閉じる

mkdir -p ~/claude-clean/empty
cd ~/claude-clean/empty || exit 1

# 新しい設定フォルダを使い、プロジェクトの設定（.claude/settings.json・CLAUDE.md・.mcp.json）を読まない
# 初回の設定画面とログインがもう一度出る。それが新しい設定フォルダが効いている印
CLAUDE_CONFIG_DIR=~/claude-clean/config claude --setting-sources user
