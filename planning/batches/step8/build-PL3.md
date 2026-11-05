# build-PL3

## 置いた目印（ページごと）
- agents-md：fact 4（instruction-files-default #choose、direct-read-min-version #limits と #outdated の 2 か所、plugin-id-rename #templates に一文を新設）
- browser-control：fact 2（chrome-extension-requirements、computer-use-requirements〔未確認〕）
- checking-for-updates：fact 1（stable-channel-delay、手順 1）
- choosing-a-model：fact 1（top-model-by-plan〔未確認だが〕…は下記）
- claude-md-loading-order：fact 1（import-max-hops）、fact-table 1（on-demand-char-limit、#limits の箇条の後）
- dynamic-workflows：fact 4（large-warning・size-guideline・concurrent-agents・agent-caps、#when-and-start-small の段落を直し新設）、feature 1（workflows/enforcement）
- plugins-and-marketplaces：feature 1（plugins/enforcement）
- progress-logs-for-long-jobs：fact 4（monitor の 3 つの期限・min-version-restricted-envs）。「ログが大きすぎた例」を（根拠：弱）に直した
- shared-artifacts-and-files：fact-table 1（chat-sharing-plans、招待・公開リンクの箇条を置き換え）、fact 2（invite-expiry〔未確認〕、created-files-restriction）
- usage-context-statusline：feature 1（usage/enforcement）
- using-research：feature 1（research/enforcement）
- when-requests-are-refused：fact 5（cc-per-category-switch-min-version、auto-switch-default、api-categories、billing-by-category、cvp-tiers。いずれも未確認で「未確認」と出る）

choosing-a-model の top-model-by-plan は未確認で、「（未確認）」と出る括弧の形に置いた。

## 置かなかった行と理由
- agents-md #limits の instruction-files-default（任意の行）：#choose にすでに置いたので重複を避けた
- 目印の置き換えで、手書きだった値（版・段数・期限・プランなど）は目印の外から除いた

## 修正メモ
- 強制力の目印「なし」は、そのままでは文として読みにくいので「」で括った（plugins・workflows・usage）
- 「未確認」の fact は、括弧か「〜は、〜である」の形で読めるようにした

## check_page.py（各ページ 1 回）
- 12 ページとも エラー 0。警告は textlint の助詞の重複・文の長さなどで、既存の文が主（agents-md 6、browser-control 4、checking-for-updates 1、claude-md-loading-order 5、dynamic-workflows 3、plugins 2、progress-logs 1、usage 1、when-requests-are-refused 2、ほか 0）
- 括りの「」を足した 3 文は、その後 check_page を流していない

## 道具の呼び出し
Read 1、Bash 6、Edit 約 40。

## 提案
- agents-md の plugin-id-rename は名称の変更なので names に移す案もある（DM4 の指摘どおり）
- agents-md 65 行目は目印の出力が長い（初期値の説明が値に入っている）ので、後続の説明と重なる。置く担当で縮めてよい
