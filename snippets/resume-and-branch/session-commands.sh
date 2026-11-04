# 名前を付けて始める（名前は作業の目的が分かる短い語にする）
claude -n oauth-migration

# 翌日、同じディレクトリで直近のセッションを開く
claude --continue

# 一覧から選ぶ、または名前で直接開く
claude --resume
claude --resume oauth-migration

# 元のセッションを残したまま、複製で再開する
claude --continue --fork-session

# 特定のプルリクエストに紐づくセッションを探す
claude --from-pr 1234

# セッションの中での操作
#   /rename oauth-migration     いまのセッションに名前を付ける
#   /resume oauth-migration     名前を指定して別のセッションへ移る
#   /branch try-streaming       複製を作ってそちらへ移る
#   /clear release-prep         いまのセッションに名前を付けて離れ、新しく始める
