# write.md：consistent-notation（表記ゆれと漢字の開き）

## 書いたファイル
- docs/japanese/consistent-notation.md（stub から mv。stage を draft、updated を 2026-11-05 に。front matter は sections〔guard・verify・failure を足した。既存の 3 つは変えていない〕と sources のみ変更）
- snippets/consistent-notation/：glossary.yaml、build-notation.py、prh-dictionary.yaml、notation-instruction.md と、それぞれの .expect.yaml（目次の案は prh の辞書の例。正本・生成スクリプト・指示の一覧を足した）
- data/sources.d/consistent-notation.yml（prh-readme を 1 件）
- sources に既存の id を追加：jinrai-claude-japanese・cc-docs-memory・hc-projects-manage・cc-docs-features-overview-ja・hc-effort-settings

## 必ず持つものの対応
- 手順：glossary（一覧を作る 3 段）・open-kanji（開く語の 3 段）・single-source（生成と置き場所）。各段に「確かめ」を付けた
- 確かめる・縛るのページへの道：guard（align-japanese-output#lock-layer・consistent-politeness#lint）、single-source（textlint-hook#post-tool-use・#gaps）。front matter の prerequisites と related にもある
- level：整える（front matter）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：guard → glossary・open-kanji・single-source → verify → failure

## メインに判断してほしいこと
- 本文の方針の文（「plan mode・effort・allow ルール…の 3 語だけを英語のまま書く」）は design §6.2 とカード §4 の写しで、約束の文ではないと判断した
- scripts の置き場所：雛形は Python（PyYAML）。リポジトリの tools には置かず、読者向けの例にした

## 提案
- 用語集への提案：「表記の正本」「漢字を開く」を用語に入れるか（本文で短く定義した）
- prh.yml への提案：なし（例の語〔サーバ・ユーザ・出来る など〕は雛形の中だけ）

## 検査の結果
- check_page.py：1 回目 エラー 1・警告 6（出来る の prh、助詞の重複など）。直した後 エラー 0・警告 0
- 実際は 3 回流した（直しの当て損ねで 1 回余分に流した。規定は 2 回）

## 確かめていないこと
- prh の書式（expected・pattern・specs・`/…/`）は、README に version・imports しかなく、misc/prh.yml のページを要約した結果から書いた。原文の逐語は未確認。specs が読み込み時に失敗で止まる点も、その要約による
- textlint の prh ルールへ辞書のパスを渡す設定のキーは書いていない（textlint-hook のページに任せた）
- build-notation.py は PyYAML つきの uv run で 1 度動かし、prh.yml と notation-list.md ができることだけ確かめた。prh での実検査と、Claude が一覧に従う様子は未確認
- 「Claude の漢字の比率が高くなりがち」は実践者 1 件の記事（根拠：弱）。「語の一覧のほうが方針の形容より安定する」は推論と明記した
- 公式の日本語版で effort と努力レベルが割れる点は、束の research/27 §3.1 の写しによる。画面の表記は未確認
- 圧縮後の CLAUDE.md の挙動は束の data の note による。WSL 以外・IDE 拡張は未確認

## 使用量
- 道具の呼び出し：約 20 回、Web の取得 2 回（github.com/prh/prh と misc/prh.yml）
