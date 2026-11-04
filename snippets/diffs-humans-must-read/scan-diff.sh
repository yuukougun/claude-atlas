#!/bin/sh
# 使い方: sh scan-diff.sh [基準のブランチ]   既定は main
# 赤信号の候補を機械的に拾うだけ。判断は人が差分を読んで行う。
base=${1:-main}

echo "== 変更の大きさ（ファイル別）"
git diff --stat "$base"...HEAD

echo "== テスト・評価・採点・設定・CI に触れたファイル"
git diff --name-only "$base"...HEAD \
  | grep -Ei '(test|spec|eval|score|grade|bench|conftest|\.github/workflows|\.claude/|config|settings)' \
  || echo "(なし)"

echo "== 追加された行にある、赤信号の語"
git diff -U0 "$base"...HEAD \
  | grep -E '^\+[^+]' \
  | grep -E 'except|pass$|skip|xfail|noqa|ignore|seed|threshold' \
  || echo "(なし)"
