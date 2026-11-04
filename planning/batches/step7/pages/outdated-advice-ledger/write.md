# 報告：執筆（outdated-advice-ledger）

- 手引きの版：共通 2026-11-04 第1版・型（ledger）2026-11-04 第1版・指示 brief-page v2

## 1. 書いたファイル
- docs/changes/outdated-advice-ledger.md（stubs/changes/ から mv）。front matter：stage を stub から draft に、sources に 6 件（cc-docs-best-practices・cc-docs-model-config・cc-docs-permission-modes・cc-docs-skills・cc-docs-goal・cc-changelog）を足した。sections と updated（今日の 2026-11-04）は変えていない
- docs/img/outdated-advice-ledger/workaround-to-mechanism.svg（目次の visual〔static〕。回避策 5 組と、補っていた原理）
- snippets/outdated-advice-ledger/find-old-advice.sh と find-old-advice.expect.yaml（手元の設定を台帳の古い言い回しで grep する、読むだけの雛形。目次の templates は「なし」だが、「自分の設定で見つける」節のために足した。安全の雛形ではない）
- planning/batches/step7/pages/outdated-advice-ledger/facts-proposal.yml（数値の提案 1 件）と、この write.md
- 構成：要点・別名・導入 → 台帳の読み方（欄・状態の 3 つ・時期と版の読み方・判断例 1 つ）→ 回避策は正式な仕組みに置き換わる（図 1 枚・5 組の一覧・次に古くなるものの見当）→ 台帳（生成の部分）→ 自分の設定や記事で見つける（面のタブ 3 つ・雛形 1 つ）

## 2. 範囲を越えたこと
- なし。ただし textlint で字下げした部分を確かめるため、リポジトリの根に一時ファイル 2 つ（zz-dedent-check-tmp.md・.dedent-check-tmp.md）を作り、すぐ消した

## 5. メインに判断してほしいこと
1. 検査：check_pages の「link の目印」は sections の anchor しか見ない。ほかのページが `outdated-advice-ledger#<台帳の行の id>`（例：important-caps）を link の目印で指すと止まる（執筆の途中で request-vs-lock に 1 件出て、後で消えた）。tools/gen/ledger.py の説明は、ほかのページがその形で指すとしている。生成の見出しの anchor を認めるか、指し方を決めてほしい
2. 構成：型の手引き §2 の目安は「要点 → 生成の表 → 読み方」、目次の sections の並びは「読み方 → 規則 → 台帳 → 見つける」で食い違う。表が長いので、目次の並びに従い、読み方と規則を先に置いた
3. 書き方：「四つの原理」は textlint の arabic-kanji-numbers（四つ => 4つ）で警告になる。link の目印の間に道具が書く題名（four-principles の「四つの原理と比例則（…）」）にも出るため、本文では「四つの」を避け、four-principles への本文中のリンクも置かなかった（ページ下の関連には出る）。固有の言い方として許すか、題名を「4 つ」にするか決めてほしい

## 6. 提案
```yaml
frontmatter:
  - {id: outdated-advice-ledger, key: summary, before: "撤回・置換された助言を、今どうするか・変わった時期と版・どの原理の回避策だったかと並べて引ける。回避策が正式な仕組みに置き換わる規則から、次に古くなるものの見当もつく。", after: "撤回・置換・条件付きになった助言を、今どうするか・変わった時期と版・どの原理の回避策だったかと並べて引ける。回避策が正式な仕組みに置き換わる規則から、次に古くなるものの見当もつく。", reason: "台帳には状態が条件付きの行もある。任意。直したら要点の「何ができるか」も同じ文に合わせる"}
```
- 用語集：「回避策」＝原理を満たす正式な仕組みやモデルの力が足りない間に、言葉・手順・自作のスクリプトで補った手段。仕組みが入るか、モデルが言われなくてもできるようになると役目を終える（anchor の案：definitions#workaround。本文は workarounds 節の最初で同じ意味を 1 文で定義した）
- 用語集：台帳の状態 3 語（撤回＝使えないか使わないほうがよい／置換＝同じ目的を別の正式な仕組みや新しい名前が担う／条件付き＝今も効くが前提が変わった）。出どころは research/00 §5。本文の定義は自分の言葉で書いた。用語集にも置くなら、台帳のページを正にしてほしい
- data：facts.yml に facts-proposal.yml の 1 件（`/doctor prompt-audit` が使える最低の版）。取り込まれたら、Claude Code のタブに fact の目印で版を足せる（今は版を手で書かず、台帳の IMPORTANT の行を指した）
- tools：台帳の行は data に確認日（checked）を持つが、gen:begin ledger は出さない。変わりやすいので、行ごとに確認日の欄を足すとよい（config.yml の ledger と gen/ledger.py）

## 7. 検査の結果
- gen_site.py --page outdated-advice-ledger：注意 0。--check で自分のページは古くない（古いのは nav.yml だけで、担当外）
- check_pages.py --page：エラー 0・警告 0。check_templates.py --page：0・0。check_svg.py --page：0・0
- npm run lint:text と npx textlint（自分のページ）：エラー 0・警告 0。textlint が見ない囲み・タブの字下げした部分は、字下げを外した写しにかけて 0 件を確かめた（写しは消した）

## 8. 確かめていないこと
- 台帳の行（data/outdated-advice.yml）は生成の元で、一次資料で読み直していない（行の checked は 2026-11-04）。変えていない
- 手書きの部分で公式の文書を読んで確かめたこと（2026-11-04）：Best practices の「What you can stop doing」の前書きと表、Model configuration の think hard と ultrathink の扱い、Skills の「.claude/commands/ は今も動く」、変更履歴の `/doctor prompt-audit`（2.1.283）
- 行の内容を信頼して書き、公式の文書を読み直していないこと：auto モードとサンドボックスへの置き換わり、/goal、アプリの画面の展開、API の引数と 400 エラー。アプリと API のタブの内容は、アプリの画面と API で試していない
- 雛形は、偽の HOME とダミーのファイルで 1 回流して、行頭に id が付くことと、該当がなければ何も出ないことを見ただけで、雛形の動作確認（verified.yaml）ではない。macOS の grep・bash 3.2 は試していない
- 描画：図は headless Chrome で SVG 単体を幅 400・ライトで描いて見た。ページ全体（幅 390・ダーク・タブと折りたたみ）は、試作のページが公開から外れ、通常のビルドに入らないため見ていない
- WSL・Linux の Claude Code を基準に書いた。ほかの OS と IDE の拡張は未確認

## 9. 使用量
- 道具の呼び出し 約 100 回（読み取りと確認が大半）。Web の取得 4 回（curl。code.claude.com の best-practices・changelog・skills・model-config の .md）。時間 約 30 分
- 束にないために開いたもの：生成の目印と挙動（tools/gen/ の config.yml・ledger.py・markers.py・core.py・snippets.py・terms.py）、台帳の行の中身（data/outdated-advice.yml。束の一覧は id・状態・時期・題名だけ）、四つの原理と状態の定義（requirements §3.1・research/00 §5 の表の後）、検査と書き方の規則（check_pages --list・prh.yml・.textlintrc.json）、つながるページの sections（stubs）
