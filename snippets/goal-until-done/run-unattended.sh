# 席を外して回す例。auto モードで確認を減らし、サンドボックスで囲んだ環境で流す
claude -p "/goal tests/ 以下のテストがすべて通っている。確かめ方：最後に npm test を実行し、終了コードと出力の末尾を会話に表示する。変えないもの：git status --porcelain tests eval の出力が空であることも会話に表示されている。上限：または 20 ターンで止まり、残っている失敗を報告する（or stop after 20 turns）。" \
  --permission-mode auto \
  --max-turns 40 \
  --max-budget-usd 10 \
  --output-format stream-json --verbose
