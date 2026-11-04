# バッチ5：メインが決めること

先例（rules.md）に当たらないものだけ。推す案を先に書く。

| ページ｜件｜案 |
| --- |
| path-scoped-rules｜面のタブが claude-code の 1 つだけ｜残す（surfaces が 1 面のため。面が増えたら足す）。#outdated の 2 点目は（根拠：弱）の印を付けて残した（TR5） |
| skill-descriptions｜#old-advice が薄い（字数の読み替えだけ）｜節を残す（記事ごとに上限が違う読み替えは、読者が実際に迷う）。sections は変えない |
| mcp-or-cli｜tracks に `skills` を足す（比較の表が MCP とスキルの 2 行になる）か｜足す。CLI の行は data に機能がないので backlog（data の形）。stances の「この辞典の推奨」（根拠：中）はそのまま残す |
| checking-citations｜訴訟の事例（techcrunch.com は noai）｜事例なしのまま。noai でない一次が見つかれば足す（backlog の出典）。「引用が原文にない」「出典が主張を支えていない」の 2 形には（推論・実践例なし）を付けた（TR5） |
| where-bypass-is-ok｜templates をコンテナの手順にせず、条件の確認の一覧にした。「この辞典の推奨」は（推論・実践例なし）つき｜条件の一覧のまま（card §10 に沿う）。具体の Dockerfile は載せない。推奨の 4 条件は印つきで残す |
| checking-ai-rules｜prevents に「境界がない」を足す（本文に原因名の名指しがない）｜足さない（本文を直さずに front matter だけ足すと食い違う）。足すなら本文に名指しを足してから。高専プロコンの例は大会名を出さない一般化のまま。サイト全体の「法的な助言ではない」の注意書きの場所は作者の承認を得て決める |
| request-lock-table｜#combine の「壊れにくい手段に任せる」（推論の印つき）。Stop フックで言語を確かめる行｜どちらも残す。言語の行は backlog の調べる担当（keep-replies-in-japanese と揃うか） |
| spec-first｜mock-first の根拠の資料がない（（推論・実践例なし）の印つき）。他ページの雛形を `gen:begin snippet` で取り込む形｜節は軽くせず印つきのまま残す。取り込みは batch4 の決め（let-claude-ask を正本）のとおりで、spec-first 自身は同じ雛形を置いていない（重なりなし） |
| practice-vs-contest-day｜kyopro-atlas の practice-method を URL なしで名前だけ書いた。線引きの根拠が弱・推論｜名前のままにする（公開の URL か相対リンクかは作者の判断）。根拠の印つきなので残す |
| ai-usage-guidelines｜「止まって相談する」の確認日｜モデル名・確認日は書かないまま。検証の担当か作者が確かめたら足す |
| sdk-comparison｜「第三者の製品が claude.ai のログインやプランの上限を提供することは承認がない限り認められていない」を 2 か所に書いた｜残す（Anthropic の規則の紹介で、公開の約束ではない。出典つき） |
| parallel-with-worktrees｜強制力の手書き（鍵ではない）と、`.worktreeinclude` の雛形（safety: true）｜手書きのまま、data の `enforcement: なし` は backlog。雛形は safety の確認の担当に回す（backlog） |
| feature-to-api-mapping｜図の破線の分け方（役割の近さ）と、比例則の警告を残す判断｜どちらもそのまま（目次の備考どおり）。自己リンクは backlog |

## メインの決め（2026-11-05）

- 直す（DM3）：mcp-or-cli の tracks に skills を足す
- そのまま：ほかの12行は、TR5 の推す案のとおり（path-scoped-rules・skill-descriptions・checking-citations・where-bypass-is-ok・checking-ai-rules・request-lock-table・spec-first・ai-usage-guidelines・sdk-comparison・parallel-with-worktrees〔強制力は DM3 が data に入れる〕・feature-to-api-mapping）
- 作者に聞くもの（急がない）：practice-vs-contest-day が名前だけで指す kyopro-atlas のページを、公開の URL で指すか
