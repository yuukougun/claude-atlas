# write.md：browser-control

## 書いたファイル
- docs/surfaces/browser-control.md（stub から移した。stage は draft、updated 2026-11-05、sections に `limits` を足した、sources に既存 id 7 件を入れた）
- snippets/browser-control/verify-local-app.md と .expect.yaml（画面を確かめさせる依頼。features: claude-in-chrome）
- snippets/browser-control/fill-form-dry-run.md と .expect.yaml（送信の手前で止めるフォーム入力。safety: true）
- data/sources.d/browser-control.yml は作っていない（出典は data/sources.yml に既存の id だけを使った）

## 必ず持つものの対応
- 機能の属性のバッジ：`which-to-use` の `compare` の目印（成熟度・面・入った版を data の 2 機能から道具が作る）。要点の囲み直下のバッジはテンプレートが出す
- tracks：front matter の `tracks: [claude-in-chrome, computer-use]`。節は `claude-in-chrome` と `computer-use`
- 使いどころ（どの原因を防ぐか）：`claude-in-chrome`（確かめていない・境界がない）。比例則の守りは `which-to-use` の冒頭で先に指した
- 最小の使い方（面のタブ）：`claude-in-chrome` と `computer-use` のアプリ／Claude Code のタブ
- 雛形：`claude-in-chrome`（2 つ）
- 効かない場面・落とし穴：`limits`、`what-not-to-hand-over`
- 比べる相手：`which-to-use`（コネクタ・Claude in Chrome・computer use の表と判断例）。独立の節にしなかった
- 古くなった助言：持たない（outdated_advice が空で、台帳に行がない）。`limits` の末尾に 1 行だけ書いた
- level：任せる（front matter のまま）

## メインに判断してほしいこと
- 強制力のバッジ：data の 2 機能に `enforcement` がない。拡張のサイト許可（鍵に近い）と computer use のアプリごとの許可を、どの値にするか決めてほしい。本文は値を書いていない
- 成熟度が面と出典で割れる（data の note どおり）。`computer-use` の節で表記の違いを一文で述べ、表は Help Center の beta に合わせたと書いた。id を面で分けるなら、その一文を直す
- `which-to-use` の表の「届く範囲」の列（コネクタは狭く、画面は広い）は、公式の優先順の理由「速く確実」に私が足した整理である。公式が範囲の広さで順を決めているとは書いていない

## 提案
```yaml
proposals:
  - fact: {id: chrome-extension-requirements, title: Claude in Chrome を Claude Code から使う要件（拡張の版・対応ブラウザ・プラン・認証の方法・WSL）, value: "拡張 1.0.36 以降。Chrome・Edge と、検出される Chromium 系。直接の Anthropic のプラン（Pro・Max・Ultra・Team・Enterprise）。/login での認証が要る（API キーと setup-token では無効）。WSL は非対応。第三者のプロバイダー経由は不可", sources: [cc-docs-chrome], checked: 2026-11-05, status: 確認済み}
    used_in: [browser-control#claude-in-chrome]
  - fact: {id: computer-use-requirements, title: computer use（Cowork・Desktop）の対象のプランと OS, value: "macOS・Windows の Desktop。Pro・Max・Ultra。Team と Enterprise は対象外（beta）。投資・取引・暗号資産のアプリは既定でブロック", sources: [hc-computer-use], checked: 2026-11-05, status: 確認済み}
    used_in: [browser-control#computer-use]
```
- 本文はどちらも数字なしで、公式を指す書き方にした。ids が承認されたら、`claude-in-chrome` の節のタブと `computer-use` の節のタブに fact の目印を置く
- Help Center の入門（hc-claude-in-chrome）は、Chrome のみ・有料プランと書く（調査資料 02 §1-12、確認日 2026-10-29）。Claude Code の文書（cc-docs-chrome）は Chrome・Edge と Chromium 系を挙げる。公式同士の食い違いなので、上の提案は両方の出典を持たせるのがよい
- 用語集：「サンドボックス」は prh が sandbox を直したので問題なし。追加の提案はなし

## 検査の結果
- 1 回目：エラー 1（sandbox の表記）・警告 7。2 回目（直した後）：エラー 0・警告 4
- 残した警告：sentence-length（リンクの目印が展開された長い 1 文。実際の文は 2 つの link を並べただけ）、max-ten（computer use の導入の文。読点が 4 つ）、no-doubled-joshi の「に」2 件（`limits` の箇条）。読みにくくはないと判断して残した

## 確かめていないこと
- 雛形の動作は試していない（Chrome の拡張と実機の環境が要る）
- `claude-in-chrome` のアプリのタブは、Help Center の入門の記事の詳細を開いていない。調査資料 02 §1-12 の写しの範囲で書いた
- computer use の CLI の対象 OS・プランは文書を開かず「公式で確かめる」とした
- WSL 非対応は cc-docs-chrome（2026-11-05 に取得）による。Claude Code の本文の基準は WSL・Linux の CLI なので、読者に影響する。ほかの OS と IDE 拡張の動作は未確認と書いた
- 「公式は機微な情報の扱いに強く非推奨」の確認日 2026-10-29 は調査資料の値である

## 使用量
- 道具の呼び出し：約 22 回。Web の取得：2 回（cc-docs-chrome、hc-computer-use）
