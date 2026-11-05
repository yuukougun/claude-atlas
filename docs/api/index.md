---
title: API・SDK の概念
---

<!-- tools/gen_site.py が生成する。手で直さない -->

# API・SDK の概念

## アプリと API の対応

- [アプリの機能と API の概念の対応表](feature-to-api-mapping.md)（任せる・下書き）：プロジェクトのキャッシュ・長い会話の自動の要約・メモリ・スキルなどが、API のどの概念に当たるかが分かる。
- [Messages API と会話の正体](stateless-messages-api.md)（任せる・下書き）：Messages API の基本の形は状態を持たず、呼び出し側が system と messages で毎回それまでの全体を渡すことが分かる。

## API の主な機能

- [tool use のループ](tool-use-loop.md)（仕組みにする・下書き）：Claude が道具の呼び出しを頼み、呼び出し側が実行して結果を返すループの形が分かる。
- [structured outputs（形式を保証する）](structured-outputs-basics.md)（仕組みにする・下書き）：出力やツールの呼び出しを、指定したスキーマどおりの形で受け取れる。
- [プロンプトキャッシングの実務](prompt-caching-in-practice.md)（仕組みにする・下書き）：毎回同じ先頭部分をキャッシュして、API の費用と待ち時間を抑えられる。

## 上限とエラー

- [rate limits とエラー（混雑と再試行）](rate-limits-and-errors.md)（仕組みにする・下書き）：API が返す上限のエラーと混雑のエラーを見分け、待って再試行するか、送る量や時期を変えるかを決められる。

## エージェントを組む

- [Client SDK・Agent SDK・Managed Agents・CLI の比較](sdk-comparison.md)（仕組みにする・下書き）：Client SDK・Agent SDK・Managed Agents・CLI を、ループを誰が回すか、どこで動くかで比べ、自分の用途に合う層を選べる。
- [Agent SDK（Claude Code をライブラリとして使う）](agent-sdk-basics.md)（回す・下書き）：Claude Code と同じ道具とループを、自分のプログラムからライブラリとして使える。
- [長時間エージェントのコンテキスト管理](long-running-agent-context.md)（回す・下書き）：長く動くエージェントで文脈が溢れないよう、要約・古い結果の削除・外部の記憶をどう組み合わせるかが分かる。
