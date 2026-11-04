#!/usr/bin/env bash
# モデルを替える前に、見直す対象の候補を探す。読むだけで、何も書き換えない。
# プロジェクトのルートで実行する。
set -u

echo "== API の引数（budget_tokens・temperature・top_p・top_k）=="
grep -rnE 'budget_tokens|temperature|top_p|top_k' \
  --include='*.py' --include='*.ts' --include='*.js' --include='*.json' \
  --include='*.yaml' --include='*.yml' \
  --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=.venv . || true

echo
echo "== 強調語と、確認を命じる一文 =="
grep -rnE 'IMPORTANT|YOU MUST|NEVER|double-check|re-verify|最後に見直|最後に確認' \
  CLAUDE.md .claude 2>/dev/null || true

echo
echo "メモ：最後が assistant のメッセージで終わる要求（prefill）は grep では見つけにくい。"
echo "messages を組み立てるコードを目で読んで確かめる。"
