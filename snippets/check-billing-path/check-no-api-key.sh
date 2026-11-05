#!/usr/bin/env bash
# claude -p を動かす前に、API 側の課金になりうる設定が残っていないかを確かめる。
# 変数の値は画面にもログにも出さない（有無と、見つかったファイル名だけを出す）。
# 使い方：./check-no-api-key.sh && claude -p "..."
set -u

found=0

# 1. 環境変数（値は読まず、設定されているかだけを見る）
for name in ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN CLAUDE_CODE_USE_BEDROCK; do
  if [ -n "${!name:-}" ]; then
    echo "設定あり：$name（値は表示しない）"
    found=1
  fi
done

# 2. apiKeyHelper を書いた設定ファイル（-l でファイル名だけを出す）
for f in "$HOME/.claude/settings.json" .claude/settings.json .claude/settings.local.json; do
  if [ -f "$f" ] && grep -q 'apiKeyHelper' "$f"; then
    echo "apiKeyHelper あり：$f"
    found=1
  fi
done

# 3. シェルの設定ファイルに書いたままになっていないか（-l でファイル名だけを出す）
for f in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
  if [ -f "$f" ] && grep -q 'ANTHROPIC_API_KEY' "$f"; then
    echo "シェルの設定に記述あり：$f"
    found=1
  fi
done

if [ "$found" -eq 1 ]; then
  echo "API 側の課金になりうる設定がある。意図したものでなければ外してから動かす。"
  exit 1
fi
echo "環境変数と設定ファイルに、API 側の認証は見つからなかった。"
