---
name: github-cli
description: PR・issue・CI の状況を調べるとき、GitHub の MCP ではなく gh コマンドで読む。書き込み（マージ・クローズ・コメント）は、人が頼んだときだけ行う
---

# gh で GitHub の状況を調べる

GitHub の情報は、`gh` をシェルで実行して読む。出力は必要な分だけに絞る。

1. PR の概要と会話は `gh pr view <番号> --comments` で読む。CI の状態は `gh pr checks <番号>` で読む。
2. issue は `gh issue view <番号>` で読む。
3. CI が落ちたときは、`gh run list --limit 5` で実行を探し、`gh run view <run-id> --log-failed` で失敗したジョブのログだけを読む。
4. 出力が長いときは、`--json` で項目を選んで `--jq` で絞るか、`| head -n 80` で先頭だけを読む。全文を会話に貼らない。
5. 使い方が分からないサブコマンドは、推測せずに `gh <サブコマンド> --help` で確かめる。
6. PR のマージ、issue のクローズ、コメントの投稿は、人が頼んだときだけ行う。頼まれていないときは、実行するコマンドを示して止まる。
