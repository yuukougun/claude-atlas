# 工程3 C11：recipes（用途別レシピ）の目次の報告

- 担当：C11（2026-11-04）
- 書いたもの：[planning/catalog/recipes.yaml](../../catalog/recipes.yaml)
- 従ったもの：[brief-catalog.md](brief-catalog.md)、design §1〜§7、catalog/README.md、schema/site.yml、registry.yaml、requirements §1・§3〜§6・§10.3、decisions 2026-11-03

## 1. 書いたファイルとページ数

recipes：21ページ（registry の候補22のうち、採る21・まとめた1・採らない0）。新しく足したページはない。

| 内訳 | 数 |
| --- | --- |
| 優先度 | 必須 4・推奨 11・任意 6 |
| レベル | 整える 6・任せる 15 |
| 型 | recipe 21 |
| 変わりやすさ | 低 10・中 11 |
| 雛形（templates） | 27（prompt 22・other 4・claude-md 1。safety: true は0） |

章（ナビゲーションの順）：

| 章 | ページ |
| --- | --- |
| 読んで理解する | explore-a-codebase（必須）・read-specs-yourself |
| 直す | fix-a-bug（必須）・shrink-failing-inputs・bisect-regressions |
| 作る・変える | spec-first（必須）・refactor-and-migrate・performance-tuning・frontend-design・create-and-review-prs |
| 確かめる道具を作らせる | add-tests・property-based-tests・build-test-harness・build-observation-tools |
| データと分析 | data-analysis・audit-ml-pipelines |
| 調べものと文書 | research-and-reports（必須）・write-docs・make-slides |
| 事務とノート | office-paperwork・notes-and-pkm |

作り方で決めたこと：

- **比例則**：21ページのすべてが、前提か関連に verify・eval・enforce・safety のページを持つ。前提に直接置けなかったのは2ページで、property-based-tests（前提の add-tests を通して届く。関連に differential-testing・test-the-verifier）と build-observation-tools（結論を任せず道具だけを任せるので、任せる幅を狭める使い方。関連に test-the-verifier）。どちらも notes に理由を書いた
- **必須の4ページの前提**は、どれも必須のページにした（choose-what-to-read・fact-checking・define-done・evidence-not-reports・let-claude-ask・when-to-plan・search-research-thinking・checking-citations）
- **上の段の内容は節に分けた**：spec-first と refactor-and-migrate の「/goal の停止条件」（仕組みにする）、refactor-and-migrate の「多数のファイルに同じ変更を流す」（回す）、office-paperwork の「手順をファイルとスキルに育てる」「雑務をまとめたリポジトリ」（仕組みにする）
- **用語**：読者に見える項目（題名・要約・サイン・別名・節）は、公式の日本語版の多数派（research/27 §3.1）に合わせて「スキル」「コミット」と書いた
- **題名を変えた**：data-analysis を「データ分析（SQL を書かずに）」から「データを分析する」にした。decisions 2026-11-03「読者の前提」により SQL を書かない人向けの説明を省き、再実行できる集計・生データでの裏取り・観察と解釈の分離に絞った
- **registry の見当の優先度**（新しい候補8つ）は、どれも見当のまま決め、notes に理由を書いた：推奨は read-specs-yourself・build-observation-tools・build-test-harness・performance-tuning、任意は property-based-tests・shrink-failing-inputs・bisect-regressions・audit-ml-pipelines（根拠が1研究か単独のブログ、または領域が狭い）

## 2. まとめた・採らなかった候補と、新しいページ

| 候補 | 扱い | 理由 |
| --- | --- | --- |
| chores-monorepo（雑務をまとめたモノレポ、任意） | merged → office-paperwork（節 chores-repo、level：仕組みにする） | 業務ごとのディレクトリと README に文脈をためる型は、事務作業を「人 → AI → 人」で回す流れを仕組みにする段の形で、独自の判断が重なる。題名の語は aliases に残した |

採らなかった候補と、新しく足したページはない。requirements §4.4 の7つ（read-specs-yourself・build-observation-tools・build-test-harness・property-based-tests・shrink-failing-inputs・bisect-regressions・performance-tuning）はすべてページにした。

## 3. wave: 1

なし（recipes は第一波の核の分野ではない）。

## 4. ほかの分野への提案と new_features

open_issues は10件（ほかの担当がすでに張っていた参照と、取り込み済みの提案は外した）。要約：

1. **delegate（C9）**：/goal の停止条件の雛形（10 付録A-14 を直したもの）を goal-until-done・spec-first・refactor-and-migrate で共有し、snippets は1か所に置く
2. **eval（C8）**：test-the-verifier から add-tests へ related を。A-11 の直しは measure-changes#by-stratum を指した。bisect-regressions と build-test-harness が verifier-three-conditions を前提にするので、その段を任せるより上にしないでほしい
3. **verify（C8）**：suspect-too-good-results から audit-ml-pipelines へ、visual-checks・looks-are-not-quality から frontend-design・make-slides へ、fact-checking から read-specs-yourself へ（ほかのレシピへの参照は verify.yaml にもう入っている）
4. **prompting（C3）**：同じ雛形が両方の分野にある（A-6 は let-claude-ask と spec-first、A-8 は prompt-patterns と data-analysis）。snippets は1か所に置いて両方で取り込む。A-10 は fix-a-bug だけ
5. **enforce（C7）**：move-judgment-into-scripts から bisect-regressions へ、freeze-eval-assets から build-test-harness へ
6. **safety（C7）**：entrusted-data から office-paperwork へ、where-your-data-goes から data-analysis・office-paperwork へ
7. **symptoms（C12）**：振り分け先にレシピの節を（claims-done-but-isnt・rewrote-tests-to-pass → fix-a-bug#no-symptom-patches、not-what-i-meant・does-more-than-asked → spec-first、deleted-something-important → notes-and-pkm、going-in-circles は fix-a-bug#when-stuck）。依存のパッケージを入れる前の確かめ方（symptoms から safety への提案で recipes も候補に挙がった）は、safety の vetting-extensions の節に置く案を返した
8. **team（C9）**：grow-review-checklists から create-and-review-prs へ
9. **japanese（C3）**：documents-in-japanese から write-docs・research-and-reports へ、character-encodings から office-paperwork へ
10. **決めきれなかった点**：audit-ml-pipelines（任意）は、読者に機械学習の層が少なければ data-analysis の節にしてよい（工程4で判断してほしい）

ほかの担当の提案で、こちらが受けたもの：

- delegate（C9）：spec-first の related に goal-until-done、refactor-and-migrate の related に batch-and-p-loops・dynamic-workflows（最初から入れていた）
- safety（C7）：explore-a-codebase → before-opening-unknown-repos、data-analysis → entrusted-data（最初から入れていた）
- team（C9）：create-and-review-prs の related に risk-tiered-approval・grow-review-checklists（最初から入れていた）
- verify（C8）：add-tests の前提に pitfalls-of-ai-written-tests、fix-a-bug・spec-first の related に tests-first、performance-tuning・data-analysis の related に suspect-too-good-results（最初から入れていた。performance-tuning では前提に置いた）
- contest（C10）：build-observation-tools の related の insight-patterns は think-before-asking にまとめた → related から外した（think-before-asking はもう前提にある）。こちらの提案（practice-vs-contest-day と形式の早見表から read-specs-yourself へ、evaluators-by-format から build-test-harness へ、search-code-checklist は固有の点検だけ）は contest が取り込んだので、open_issues から外した
- app（C5）：research-and-writing-in-the-app を research-and-reports にまとめた（こちらの提案と同じ） → research-and-reports の related に artifacts-overview・using-projects を足し（using-research と、前提の search-research-thinking は入れてあった）、tracks に projects・artifacts を、節「アプリと Claude Code の使い分け」にリサーチ・プロジェクト・アーティファクトを足した。write-docs の related に artifacts-overview を足した（make-slides はもう前提に持つ）
- eval（C8）：stratified-and-worst-case を measure-changes にまとめた → performance-tuning・data-analysis・audit-ml-pipelines の related を measure-changes#by-stratum に直した。eval の提案（build-test-harness の前提に verifier-three-conditions、shrink-failing-inputs・property-based-tests・bisect-regressions・refactor-and-migrate に differential-testing、data-analysis に check-the-metric と lockbox-and-holdout）は、bisect-regressions の differential-testing と data-analysis の lockbox-and-holdout を足して受けた（ほかは入れてあった。shrink-failing-inputs と refactor-and-migrate では前提に置いた）
- cli（C4）：for-non-engineers を採らなかった → 00 §4 のサイン「コードを書かない仕事に Claude Code を使いたい」を office-paperwork の signs に入れ（前のサインと差し替え）、00 分野07 の要点（作業用のフォルダで始める）を節 work-folder にした。権限のモードは手で決めず、前提に足した safety の default-safety-settings（段階ごとの既定）に従って書く。related に permission-modes-overview を足した
- prompting（C3）：spec-first と write-docs の related に let-claude-ask と requesting-prose → write-docs に requesting-prose を足した（spec-first は let-claude-ask を前提に持つ）
- surfaces（C2）：office-and-workspace を peripheral-products にまとめた → make-slides と office-paperwork の related を peripheral-products#office-add-ins に直した。peripheral-products からは make-slides・office-paperwork へもう張ってある

new_features の提案：なし（tracks は catalog/README §5 の id だけで足りた）。

**補完調査の雛形（10 付録A）の載せ方**（requirements §10.3・11 第5節の不具合を直す前提で templates に書いた）：

| 雛形 | ページ | 直し方 |
| --- | --- | --- |
| A-6 | spec-first（prompting の let-claude-ask と共有） | ツール名を書かずに「インタビューして」と頼む形にする（research/26 #17）。評価環境の例に汎用の機能の例を並べる。版依存なので確認日と版 |
| A-8 | data-analysis（prompting の prompt-patterns と共有） | なし |
| A-10 | fix-a-bug | なし（Before/After の折りたたみ） |
| A-11 | performance-tuning | 出力が変わる候補（乱数生成器の差し替え・exp の近似）は別のコミットに分け、受け入れ条件を、出力の一致から、決めた入力の集合で平均と最悪の帯が劣化しないことに切り替える（11 第4節 #22） |
| A-12 | audit-ml-pipelines | なし（初版で省いてよい） |
| A-14 | spec-first・refactor-and-migrate（delegate の goal-until-done と共有） | 判定役は会話しか読まないので、テストと評価のファイルを変えていないことを git status の出力で会話に示させる（11 第4節 #23）。版依存（高）なので確認日と版 |
| A-16 の後半 | research-and-reports | なし |
| A-17 | create-and-review-prs | 「自分の言葉で3行」の3は根拠のない数（11 第4節 #65）なので例として書く |

A-4（評価資産を守る hook。fail-open など直す点が多い）は、設定の例を enforce の freeze-eval-assets が、考え方と依頼の文例を verify の protect-tests が持つ（verify から enforce への提案）ので、build-test-harness からはリンクだけにした。安全とデータの雛形はこの分野に置いていない。

## 5. 検査の結果

`python3 tools/check_catalog.py --field recipes`：**エラー0件、警告0件**（最後に走らせた時点で、23分野のファイルがそろい、japanese と symptoms も registry の候補をすべて処理した後。ページ361を読んだ）。

- ほかの担当のまとめで、途中に参照のエラーが出たものは直した：surfaces（office-and-workspace → peripheral-products。2件）、contest（insight-patterns → think-before-asking。1件）、eval（stratified-and-worst-case → measure-changes。3件）。直し方は §4 の「受けたもの」
- 書きかけの prompting・japanese・symptoms を指す「未処理の候補」の警告は、それぞれが書き終わって消えた
- 残した警告はない
- 全体の検査（`--stats`）では、recipes は21ページ（必須4・推奨11・任意6、整える6・任せる15、recipe 21）。全体のエラー4件・警告6件は、どれもほかの分野のファイルの指摘で、recipes.yaml の行はない
- recipes のページは第一波に入らない（核のページの前提から届くものがない）。第一波を広げる必要はないと考えるが、symptoms の going-in-circles などが fix-a-bug を前提にすれば入る
- 道具の検査に加えて、自分のスクリプトで、前提の段の逆転・必須の前提・前提と関連の重複・同じ id の2回・`id#anchor` の anchor・入ってくる道（どのページも、この分野のほかのページから1件以上の参照を持つ）・summary の字数と文の数・題名と要約とサインに数字がないこと・半角と全角の間の空白・人名がないことを確かめた

## 6. 確かめていないこと・迷った点

- **訂正・注記の付いた主張を根拠にしていない点**：01 KQ2 の 2-1（改稿前の Best practices。「シニアエンジニアに聞くように」「AskUserQuestion でインタビュー」）、11 p34#84（SWE-fficiency の古い版の数値）、11 p56#58（team のリスク段階の訂正の付いた行。create-and-review-prs の「AI の承認を人の承認に数えない」は research/25 §3.3 の原文の確認で書いた）。注記ではないが 11 第4節で疑わしいとされた主張（#45 のリークの割合、#52 の「縮小はスクリプトのほうが強い」）も、summary と signs の根拠にしていない
- **偽の高速化の研究**（11 p34#85・#86）は Claude 以外のモデルの結果なので、「モデルを問わず起きる」の根拠にだけ使う、と notes に書いた（research/24 A-9）
- **ほかの担当が後で直すと**、こちらの参照が切れうる（今は全部解決している）。全分野の第2版の検査で見てほしい
- **迷った点**：
  1. chores-monorepo を office-paperwork にまとめるか、任意のページとして残すか。重なりが大きいのでまとめた
  2. audit-ml-pipelines を残すか、data-analysis の節にするか。11 が新ページ（任意）として挙げるので残し、open_issues に判断を残した
  3. /goal の雛形（A-14）を載せるページ。11 第5節は delegate に置くとするが、brief の指示と 11 p56#115（自律反復は仕様の決まった実装に限る）から、spec-first と refactor-and-migrate にも節として置き、雛形は共有にした
  4. read-specs-yourself の範囲。競技の「問題文とテスターを細部まで読む」技術そのものは kyopro-atlas に任せ（decisions の書き方の方針5）、AI への渡し方と確かめ方に絞った
  5. office-paperwork の「作業用のフォルダで始める」節。00 分野07 は「手動モードで始める」とするが、安全の既定は decisions 2026-11-03 に従い safety の default-safety-settings（段階ごとの既定）に任せ、こちらでは決めなかった
  6. 依存のパッケージを入れる前の確かめ方（symptoms から safety への提案で、recipes も候補に挙がった）。安全の手順なので safety に置く案を返し、recipes には置かなかった
- 一次資料は見ていない（Web を使わない指示）。Common workflows の要点は 01 KQ3 の要約による
