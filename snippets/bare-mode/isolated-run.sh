#!/usr/bin/env bash
# 手元の設定を混ぜずに claude -p を動かす例。サブスクリプションのまま使える形
# 使い方: MODEL=<モデルの名前> ./isolated-run.sh "プロンプト"
set -euo pipefail

# 鍵の環境変数を外す。残っていると、-p は必ずその鍵を使い、API の従量課金になる
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN

# 専用の置き場所。~/.claude の設定・CLAUDE.md・rules・skills・agents・plugins・自動メモリは読まれない
# 初回だけ、この置き場所で claude を対話で起動して /login しておく
export CLAUDE_CONFIG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude-isolated}"
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
export ENABLE_CLAUDEAI_MCP_SERVERS=false

# project と local の設定だけを読む。MCP は --mcp-config で渡したものだけにする
# モデルは固定する。記録のために版も残す
claude --version >&2
claude -p "$1" \
  --setting-sources project,local \
  --strict-mcp-config \
  --model "${MODEL:?MODEL にモデルの名前を入れる}" \
  --output-format json
