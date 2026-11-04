# write.md：choosing-a-surface

## 書いたファイル
- docs/surfaces/choosing-a-surface.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 5 件にした）
- front matter で変えたキー：`sections`（末尾に「組み合わせ方 {#combine}」を足した）・`stage`・`updated`・`sources`（hc-cowork-and-chat・hc-cowork-surfaces・hc-release-notes・cc-docs-claude-code-on-the-web・cc-docs-agent-sdk-overview。data/sources.yml にある id）
- 雛形・図・data/sources.d は作っていない（目次の templates は「なし」。図の案は下の「確かめていないこと」）

## 必ず持つものの対応
- 比較の表：`compare-surfaces`（手書きの 3 軸の表と、`compare` の目印の表。後者は tracks が app-tasks の 1 件だけなので 1 行）
- 判断例：`examples`（3 件）
- 構成の目安の「選び方」：`app-tasks-or-claude-code`・`when-to-build-with-api`／「組み合わせ方」：`combine`
- level：front matter の「使う」のまま

## メインに判断してほしいこと
- 比較の表：数値ファイルに claude-code と api の機能が tracks にないため、`compare` の表は app-tasks の 1 行になった。3 面を並べる軸の表（誰が手を動かすか・何に触れるか・どこで動くか）は、変わりやすい値を含まない構造の説明として手書きした。「data から作る表を手で書かない」との兼ね合いを見てほしい（下の提案）
- 二次情報（日本語の実務記事）の「Cowork から始め、繰り返す作業になったら Code へ」と、非エンジニアが Desktop の Code タブで使う案内は、根拠：弱で書いた。書き方が強すぎないか見てほしい
- 「統合の後に残る制約」（Incognito・Add from GitHub・分岐）は 2026-10-29 の確認日を本文に付けた。変わりやすい値の扱いが要るなら、facts への提案にしてほしい

## 提案
```yaml
frontmatter:
  - {id: choosing-a-surface, key: sections, before: "5 節", after: "6 節（組み合わせ方 {#combine} を末尾に追加）", reason: "構成の目安の「組み合わせ方」を節にした。既にある anchor は変えていない"}
proposals:
  - fact: {id: surface-attributes, title: "面（アプリ・Claude Code・API）の属性（誰が手を動かすか・何に触れるか・どこで動くか）", value: "3 面を機能として features に足し、tracks に入れる", sources: [hc-cowork-and-chat, cc-docs-claude-code-on-the-web, cc-docs-agent-sdk-overview], checked: 2026-11-05, status: 提案}
    used_in: [choosing-a-surface#compare-surfaces]
```
- catalog：`choosing-a-surface` の tracks に claude-code・api 側の機能の id を足すと、`compare` の表が 3 面を並べられる（open_issues の提案の続き）

## 検査の結果
- `check_page.py` を 3 回流した（1 回目：エラー 0・警告 7、2 回目：警告 3、3 回目：エラー 0・警告 0）。textlint の警告は文の分割と助詞の言い換えで直した。指示の「2 回」を 1 回超えた

## 確かめていないこと
- 手書きの 3 軸の表の「Claude Code は手元かクラウド」「API は自分のプログラムか Anthropic の環境」は、束の材料（P-1・P-2・5-9）の要約で、公式の文書を開き直していない
- 「変更が差分として見える」「検査を同じ場所で回せる」は Claude Code の一般的な性質で、束にない書き方。一次資料では確かめていない
- 図の案（3 軸を並べた static 図）は作っていない。表で足りると判断した
- 未公開の link 先（where-it-runs ほか）は「準備中」と出る。`outdated-advice-ledger#cowork-separate-app` の節の存在は check_page が通ったので参照は解決している
- WSL・Linux 以外の OS と IDE 拡張の動作、プラン別の可否は書いていない

## 使用量
- 道具の呼び出し：約 17 回（Read 4・Bash 8・Write 2・Edit 0・check_page 3）。Web の取得：0
