# 推奨R2：メインの判断に上げるもの

| ページ | 件 | 案（推す案を先に） |
| --- | --- | --- |
| before-using-top-model | 公式同士の食い違い（Fable の記事は別の週の上限なし、Max・Ultra の記事と facts は「別の週の上限」）。本文は Fable の記事に合わせて警告の囲みで 3 通りを並べた | 本文のまま。facts の note・how-usage-limits-work#limit-types の箇条は backlog のとおり事実の担当が確かめて直す |
| when-ai-is-unavailable | 雛形の expect.yaml の features を空にして「要る最低の版」の表示を消すか | features を空にする（この雛形は特定の機能に依存しない）。雛形の持ち主が直し、別の担当が確かめる |
| office-paperwork | 手順の節が守りの節より先にある（目次の sections の順のまま）。`#work-folder` の「確認が出る既定のまま始める」が decisions 2026-11-03「安全の既定の勧め方」と矛盾しないか | 並べ替えない（目次の順）。矛盾の確認は作者側 |
| output-shape | 技法の目安（なぜ効くか）が終盤。#where は箇条でタブでない | そのまま（箇条で読める）。入れ替えは見送り |
| check-the-metric | 出典の題名・日付が記憶による仮の値（OpenAI）。Kaggle ブログの数値は未確認。本文の根拠の印は（根拠：弱） | 印は弱のまま残し、出典の確認はメインが開いて行う（backlog）。確かめられなければ OpenAI の例を削る |
| shared-artifacts-and-files | 競技中の守りを（類推）で `#revoke` の末尾に | そのまま残す（印で十分） |
| tests-first | 実践者の報告の一文（根拠：弱）は一次資料未確認 | そのまま残す（rec1 の先例と同じ）。出典が取れなければ削る |
| browser-agent-cautions | 検査の警告 1 件は browser-control の題名由来 | 放置（生成のテキスト由来） |
| browser-control | 成熟度が面と出典で割れ、表を Help Center の beta に合わせた一文。「届く範囲」の列は担当の整理 | 一文のまま。範囲の列は公式の理由ではないと本文にある形で残す |
| what-each-surface-cannot-do | 表がほぼ「アプリ」1 行で、題名の「できないこと」を表で引けない | data に面の細分か制約の項目を足す（backlog）。それまで本文の手書きの節を残す |
| instructions-hidden-in-materials | 方針 B1 の写しが束にない。本文は隠し指示を外す方法に触れていない | 本文のまま。方針 B1 の文の確認は作者側 |
| looks-are-not-quality | 担当が Bash でページを 1 回直した（内容は文の短縮のみ） | 検査は通っているのでそのまま。以後は Write か Edit |

## メインの決め（2026-11-06）

- 直す（TR-R3 に頼む）：office-paperwork の節を、手順の型の目安（要点 → 先に整える守り → 手順）の順に並べ替える。「確認が出る既定のまま始める」は安全の既定の勧め方と食い違わないので、文はそのまま
- そのまま：ほかの11行は、TR-R2 の推す案のとおり（before-using-top-model は公式同士の食い違いを並べた形のまま。when-ai-is-unavailable の features を空にする指定は道具の件として backlog。what-each-surface-cannot-do の data の形も backlog）
