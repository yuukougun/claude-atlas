# six-causes 執筆の報告

## 書いたファイル
- docs/start/six-causes.md（stubs/start/six-causes.md を削除して移した。stage: draft、updated: 2026-11-05、`sources` に cc-docs-best-practices・chroma-research-context-rot・simonwillison-lethal-trifecta を追加。ほかの front matter は変えていない）
- 雛形・図のファイル・data/sources.d は無し（目次の templates が空。図は Mermaid を本文に直書き。出典は data/sources.yml にある 3 件だけ）

## 必ず持つものの対応
- 型 guide は「冒頭の要点のほかに必ず持つものはない」。要点の囲み（何ができるか・いつ引くか・前提）を冒頭に置いた。
- 構成の目安は自由（表とリンクが本体）。表は claude-side（原因の表）、diagnosis（問いの表）、human-side（落とし穴の表）、to-symptoms（振り分けの表）。

## メインに判断してほしいこと
- to-symptoms の「症状のページ｜先に疑う原因」の表を手で書いた（カードに、このページ向けの生成の目印がないため）。原因の対応は 00 §4 と各ページの summary から付けた。症状ページの prevents・pitfalls・routes と食い違う可能性があるので、catalog 側で生成の目印を持つか、症状ページ完成後に突き合わせてほしい。
- 「順を待たずに先に見るもの」（消された直後は復旧が先、流出の兆しは⑥を先）は、この辞典の推奨として書いた。方針としてよいか。

## 提案
```yaml
frontmatter:
  - {id: six-causes, key: related, before: [...], after: [..., lethal-trifecta, verification-ladder, when-to-lock, request-vs-lock, context-rot, tidy-the-desk], reason: "診断の表の ②③④⑥ の根拠・手の持ち主のページへ指せるようにする（本文は未リンク）"}
```
- 用語集：フック・サブエージェント・サンドボックス・スキルは prh が日本語表記を要求する（本文はそれに従った）。

## 検査の結果
- check_page.py：1 回目 エラー 7・警告 19 → 直した後 エラー 0・警告 17（ほか 1 件が上限で省略）
- 残した警告：arabic-kanji-numbers の「六つ」「五つ」は題名・summary・見出しで固定の語（直さない）。max-ten・no-doubled-joshi 等は表の長い文で、読みやすさを損なわないと判断して残した。

## 確かめていないこと
- 「効く手の種類」の列（`/goal`・Rule of Two・`/usage` など）は 00 §2 の写しで、機能の現行の有無と名前は確かめていない。
- Chroma の報告の対象モデル・結果の細部は束にないので、「当時の複数のモデル」としか書いていない。
- 症状ページ 10 件の原因の対応は各ページ本文で未確認（束の summary と 00 §4 から）。
- 「4 つの公式分類が①③④⑤にほぼ対応」は 05 §1 と 00 §2 の対応表からの整理。
- 未公開のページへのリンクの表示は gen_site 任せ。

## 使用量
- 道具の呼び出し 約 12 回、Web の取得 0 回
