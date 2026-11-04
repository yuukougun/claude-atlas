# Issue テンプレートの下書き（工程9）

置き先：`.github/ISSUE_TEMPLATE/`（作者の承認の後にメインが置く）。

## report-error.yml（誤りや古い情報の報告）

- 合わせた承認済みの文：how-to-use の節 report（書いてほしい3点・「返事と直す時期は約束しない」）、ai-and-sources の節 contact（同じ3点・「Issue は公開される。秘密の情報、個人の情報、認証情報は書かない。」）。approval 1-3 と 2-2。
- 欄の id は overrides/main.html のリンクの値と合わせた：page-title・page-url・page-verified・page-updated。
- 新しく書いた文（承認が要る）
    - 冒頭の1行目「誤りや古い情報を知らせるフォームである。」（2行目の2文は承認済みの文の再掲）
    - 種類の選択肢「誤り／情報が古い／その他」（design §9.5 の「情報が古い」による）
    - 「正しいと思う情報と出典（任意）」「確かめた日（任意）」の欄名と説明
    - 確認のチェック（公開と書かない情報の確認を、必須にする形）

## case-suggestion.yml（ページや症状の提案・困りごとの共有）

- 合わせた承認済みの文：contact の「ページや症状の提案は、ここで受ける」、「Issue は公開される。…」。design §9.5・§10.1 の9、decisions 2026-11-04。
- 新しく書いた文（承認が要る）
    - 「返事、採否、反映の時期は約束しない。いただいた内容を、そのままページにするとも約束しない。」（約束しない旨。2-2 の考え方の延長）
    - 欄名と説明（何をしようとしたか・何が起きたか・試したこと・使った面・版・関係しそうなページ・辞典に足してほしいこと）
    - 確認のチェック（report-error.yml と同じ）

## config.yml

- 案：`blank_issues_enabled: false`、外のリンクなし。理由はファイルのコメント。
- 承認済みの文との対応はなし。利用者に見える文は含まない。

## 反映のときに必要なこと

- tools/gen/config.yml の `report_template` は現在未設定。置くときは `report-error.yml` を指定する（overrides/main.html は template 名をそのまま URL に入れる）。
