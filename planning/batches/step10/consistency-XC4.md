# XC4 整合の検証（スキル／サブエージェントの組）

| 重さ | ページと節 | 食い違い | 直したこと |
|---|---|---|---|
| 軽い | writing-skills「圧縮の後」 | 再投入の上限を「公式で確かめる」と書き、持ち主 how-skills-load・data（skill-reattach-tokens-*）の値と二重になっていた | 目印で値を出し、how-skills-load#after-compaction へ link |
| 軽い | writing-skills「効かない場面」 | 一覧の上限の値を公式へ丸投げ。data（skill-listing-*）と how-skills-load に値がある | how-skills-load#residual-cost へ link を足した |

他の観点（強制力＝スキルはお願い／サブエージェントの指示はお願い・tools は鍵、Explore/Plan が CLAUDE.md・git status を持たない点、会話履歴が渡らない点、圧縮の影響、fork の用語、description の上限の値）は、7ページ間で食い違いなし。

## メインに決めてほしいこと
なし。参考：「fork」が skill-vs-subagent の `context: fork`（履歴を引き継がない）と subagent-isolation の fork したサブエージェント（履歴を引き継ぐ）の2つの意味で出る。両ページとも区別を明記済みで、現状は矛盾ではない。

## check_page.py
writing-skills：エラー0（2回目の実行で警告の解消を確認）。他ページは変更なし。

## 道具の呼び出し
約10回
