# build-PL2（数値と強制力の目印）

## 置いた目印（22）
- agent-view-and-background：1（feature agent-view/enforcement。「止められるもの」を「強制力」に直した）
- artifacts-as-apps：3（artifact-runtime-plans を #runtime と #pitfalls、artifacts-storage-limit を #runtime）
- before-using-top-model：2（top-model-weekly-share、top-model-claude-code-min-version）
- cloud-schedules：5（scheduled-tasks-plans、cloud-scheduled-task-min-interval、scheduled-tasks-github-lapse、scheduled-tasks-schedule-warning-version〔未確認：括弧の中に「未確認」〕、scheduled-tasks-run-history-question-version）
- output-style-modes：3
- protected-paths：1
- rate-limits-and-errors：3（sdk-auto-retry-default 1、claude-code-auto-retry-default 2）
- split-models-by-role：1
- tool-use-loop：1
- using-auto-memory：1
- what-feedback-sends：1（未確認：括弧の中に「未確認」）
- check-billing-path・model-quirks：0

## 置かなかった行（5）と理由
- top-model-by-plan（before-using-top-model#which-limit）：未確認で、4 つの箇条を「未確認」だけに替えると文として読めない。箇条は残した
- api-credits-eligible-plans-and-amounts（check-billing-path の fact-table）：未確認で、表が「未確認」の 1 語になる。一度置いて出力を見て、外した（元の文に戻した）
- api-key-env-p-mode-uses-key-without-confirmation（表のセル）：未確認で、セルが「未確認」だけになる
- auth-precedence-order（7 項目の一覧）：未確認で、一覧が「未確認」だけになる
- model-prompting-tendencies（model-quirks の fact-table）：同じ理由で、置いて外した
- 上の 4 つの fact は、メインが確認済みに上げた後に置き直せる（置き方は facts-placement-rec.md のとおり）

## 本文の直し
- 「値を避ける言い回し」を、目印を使う文に直した（プラン・上限・版・回数・既定）
- competition-day-operations：review 指摘2の一文「AI の提案は、同じ文脈の中では似た方向に偏りやすい。」を削った（目印はなし）

## check_page.py
- 13 ページを各 1 回流した。すべてエラー 0。警告は textlint の既存のもの（助詞の重複・文の長さ）。rate-limits の長い 1 文は直した
- 未確認の 2 つの表を外した後は、再実行していない（外しただけで、目印は残っていない）

## 道具の呼び出し
- 約 10 回（Read 19 回を含めると約 45 回。Edit 33 回、Bash 5 回）
