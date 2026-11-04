#!/usr/bin/env bash
# clone したリポジトリで、開くだけで動きうる設定を探す。読むだけで、何も実行せず、書き換えない。
# 使い方：bash list-auto-run-files.sh <clone したディレクトリ>
# Claude Code は起動しない。出力は、自分の目で読む。
set -u

cd "${1:?clone したディレクトリを渡す}" || exit 1

echo "== 設定・MCP・エディタの設定のファイル =="
find . -path ./.git -prune -o \
  \( -path './.claude/*' -o -name '.mcp.json' -o -path './.vscode/*' \
     -o -name 'CLAUDE.md' -o -name 'CLAUDE.local.md' \) -type f -print 2>/dev/null

echo
echo "== 自動で動きうるキー（フック・環境変数・MCP・コマンドを呼ぶ設定）=="
grep -rnE 'hooks|"env"|enableAllProjectMcpServers|ANTHROPIC_BASE_URL|mcpServers|[Hh]elper|"command"' \
  .claude .mcp.json .vscode 2>/dev/null || true
