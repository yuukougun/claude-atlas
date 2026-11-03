# 工程3：分野の目次の担当への共通の指示

- 版：2026-11-04 v1
- 担当ごとの分野の割り当ては [README.md](README.md) の2段目の表にある

## 1. 背景

claude-atlas は、Claude 全般（claude.ai アプリ・Claude Code・モデルと effort・頼み方・API と SDK の概念・安全とデータ・組織での運用）を使いこなすための、辞書として引く日本語の教材である。読者は開発の経験（git・ターミナル・プログラミング）がある人で、うまくいかなかった場面ややりたいことから引く。機能の紹介ではなく判断を教える。リポジトリは `/home/yuuki/projects/kyopro2/claude-atlas`。今日は 2026-11-04。

目次（planning/catalog/）は、骨格（工程8a）で各ページの front matter の元になり、執筆の指示にもなる。全候補の id の一覧（`planning/catalog/registry.yaml`）はできている。あなたは割り当てられた分野の詳細を書く。

## 2. 最初に読むもの

1. `planning/design.md` の §1〜§7（特に §2 分野と型、§3 レベルと分類とキーの台帳、§4 粒度と境界、§5 目次の作り方、§6 編集方針）
2. `planning/catalog/README.md`（全部。形式と規則）
3. `schema/site.yml`（語彙）
4. `planning/catalog/registry.yaml`（自分の分野の候補と、ほかの分野の id。ほかの分野のページは、ここの id で指す）
5. `planning/requirements.md` の §1・§3〜§6
6. `planning/decisions.md` の 2026-11-03 の節（特に「読者の前提」「第一波に足すもの」「安全の既定の勧め方」「書き方の方針」の2つの節）

## 3. 材料

- `planning/research/00-content-report.md` の §3（自分の分野の表）、§4（逆引きの73項目。自分の分野のページの signs の材料）、§5（古くなった助言。台帳の id は registry の ledger）
- `planning/research/11-contest-crosscheck.md` 第1節（追加候補）と第2節（既存のページに足す内容）の、自分の分野の行
- `planning/requirements.md` §4.3〜§4.4
- 工程2の報告 `planning/research/22〜28`（訂正と、確かめた事実）と `planning/research/21-step1-findings.md` §2
- 必要なら、各分野の詳しい調査（01〜06・10）の該当の節

## 4. すること

1. 割り当てられた分野ごとに `planning/catalog/<field>.yaml` を書く（形式は catalog/README.md §3、規則は §4）
2. registry の自分の分野の候補を、すべて pages・merged・dropped のどれかに入れる
3. `python3 tools/check_catalog.py --field <field>` で検査する（道具は別の担当が作っている。まだなければ、YAML が読めることを `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <ファイル>` で確かめる）。エラーは0にする。警告は、理由があれば `notes` に書いて残してよい
4. 自分の報告を書く

## 5. 大事な決まり（要点）

- 読者は開発の経験がある人。「使う」のページは少なく短くし、「整える」〜「仕組みにする」を厚くする
- 面ごとにページを分けない（タブで並べる）。症状は1症状1ページで、題名は読者の言葉
- summary・signs・title に、変わりやすい値（数値・既定値・料金・モデルの世代・上限）を書かない
- 調査資料の訂正・注記の付いた主張（`【2026-11-03 訂正】`・`【2026-11-03 注記】`）を、要約やサインの根拠にしない
- 必須のページの前提は必須にする。前提は直接のものだけ（4つまで）
- 比例則：任せる幅を広げる内容のページは、verify・eval・enforce・safety のページを前提か関連に持つ
- 安全とデータの雛形は `safety: true`
- 第三者を否定的な文脈で名指ししない（materials と notes にも、個人の名前を書かない）

## 6. 守ること

- 書いてよいのは、割り当てられた分野のファイルと、自分の報告（`planning/batches/step3/catalog-<担当>.md`）だけ。registry・features・設計書・ほかの分野のファイルは変えない。変えたいことは報告と `open_issues` に「提案」として書く
- git の操作をしない。Web を開かない（材料は調査資料と工程2の報告）

## 7. 報告の形（`planning/batches/step3/catalog-<担当>.md`）

1. 書いたファイルと、分野ごとのページ数（優先度・レベル・型の内訳）
2. merged・dropped にした候補と理由、新しく足したページと理由
3. `wave: 1` を付けたページ（核の分野だけ）
4. ほかの分野への提案（open_issues の要約）と、`new_features` の提案
5. 検査の結果（エラー・警告の数と、残した警告の理由）
6. 確かめていないこと、迷った点

最後の返答（メインへの報告）は300字まで。
