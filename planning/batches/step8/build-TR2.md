# build-TR2：バッチ2の終わりの扱い

- 直したページ：11ページ13か所。related 追加3（data-vs-instructions・state-the-scope・claude-md-length）、summary 直し1（checkpoints-and-rewind）、束にない知識の直し9（reward-hacking・how-thinking-works・state-the-scope API タブ・working-with-git・where-your-data-goes・always-on-costs・allow-i-dont-know の偽 flag 削除2か所・felt-vs-measured の数字外し）
- summary-overgeneralization：型の必ず持つもの（principle=確かめる・prevents=確かめていない を what-helps で結ぶ）は満たす。arXiv 2504.00025 の概要で「新しいモデルは一般化の正確さが低い傾向」・10 LLM・4,900件・26〜73%・DeepSeek/ChatGPT-4o/LLaMA 3.3 70B を確認済みで、直し不要
- 原文で確認：attention-budget の n の2乗（Anthropic の記事）、suspected-degradation の「API は含まれない」、always-on-costs の Best practices の表（言い回しだけ直した）。attention-budget・suspected-degradation は直し不要
- backlog に足した件：数値16行、用語集9行、道具・data 10行、出典2行（計37）
- batch2-decisions.md：19行
- check_page.py：直した11ページすべてエラー0（各1回）
- Web の取得：5回（pnas.org は403で確認できず）。道具の呼び出し：約20回
