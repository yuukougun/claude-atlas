# write.md：vetting-extensions

## 書いたファイル

- docs/safety/vetting-extensions.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 9 件を追加、sections に guards・checklist・after-install の 3 節を足した。既存の 4 節の anchor は不変。節の並びは guards → provenance → read-contents → changes-after-install → dependencies → checklist → after-install）
- snippets/vetting-extensions/checklist.md（入れる前の確認表。kind other・safety true）と expect.yaml
- snippets/vetting-extensions/inspect-prompt.txt（中身を実行せず読ませる依頼。kind prompt）と expect.yaml
- snippets/vetting-extensions/package-prompt.txt（足す依存を入れる前に確かめさせる依頼。kind prompt）と expect.yaml
- data/sources.d/vetting-extensions.yml は作っていない（使った出典 9 件はすべて data/sources.yml に既にある）

## 必ず持つものの対応

- 手順：provenance（4 段の 1）・read-contents（2）・changes-after-install（3）・dependencies（4）。各節の末尾に「終わりの確かめ」を置いた
- 手順の全体の確かめ：checklist（確認表の雛形と、確認の重さの目安）
- 確かめる・縛るのページへの道（front matter の前提と関連。比例則）：guards（lethal-trifecta#three-capabilities・connecting-mcp#scopes・connecting-mcp#credentials・prompt-injection-in-practice#what-works を先に示した）。前提は冒頭の要点の囲みで link。関連は read-contents（writing-safe-hooks#runs-as-you・mods）・provenance（looks-are-not-quality・connectors-in-the-app#trust・plugins-in-the-app#contents・skills-in-the-app#built-in-and-custom・plugins-and-marketplaces#before-install・org-managed-settings-and-mcp#mcp-allowlist・choosing-mcp-servers）・changes-after-install と after-install（pruning-extensions）・dependencies（uses-nonexistent-apis#diagnosis）に分散して置いた
- level：front matter の「任せる」のまま（変更なし）
- 型の構成の目安：要点 → guards（先に整える守り）→ 手順（4 節）→ checklist（確かめ方）→ after-install（失敗したとき）。失敗したときの「症状ページへ振り分け」は、症状の入口 uses-nonexistent-apis を dependencies で指すのみ（このページに合う症状ページは ほかに見当たらなかった）

## メインに判断してほしいこと

- 判断例を 1 つ置いた（provenance）。「選んだもの」が実質、個人の好みの標準に見えないか確認を
- dependencies の「入れる前に確かめる観点」は一般的な観点にとどめ、具体のコマンドや registry の機能は書いていない（brief どおり、一次資料は開いていない）。必要なら後の波で補う
- mods と plugin の「確認を重くする」の線引き（checklist の「重くする」の列挙）は、このページの推奨であって公式の立場ではない。根拠の印は付けていない（推論・実践例なし）

## 提案

```yaml
frontmatter:
  - {id: vetting-extensions, key: sections, before: "4 節", after: "guards・checklist・after-install の 3 節を足した 7 節", reason: "recipe の構成の目安（守り・確かめ方・失敗したとき）を満たすため。ページ側はすでに反映済み"}
```

用語集への提案：「サンドボックス」は prh の指定どおり使った。「tool poisoning」「rug pull」「slopsquatting」は本文で短く定義した（用語集に無ければ追加を提案する）。

## 検査の結果

- 1 回目：エラー 3（sandbox → サンドボックスの prh）、警告 7
- 直した後：エラー 0、警告 4（回数の上限のため、再度は流していない）
  - 55:68・57:59 の「に」の重複：55 行目は link の間に入る題名（道具が書く）の影響が大きい。57 行目は直す余地あり
  - 97 行目・158 行目の文長：97 は link 題名の展開込み。158 は研究の結果の 1 文で、数値を落とすと意味が変わるため残した

## 確かめていないこと

- 本文の事実は、束の材料（05 の 4-3・4-4・1-7、cc-docs-security・cc-docs-sandboxing の写し）に基づく。一次資料は開いていない（Web の取得 0 回）
- 「スキルの本体（SKILL.md）は Claude が従う指示で、同じ場所のスクリプトも実行されうる」は、束の写しに明記がなく、一般的な理解で書いた。公式の skills の文書で確かめてほしい
- 「遠隔の MCP サーバーの道具の説明はサーバー側で変えられる」は仕組みからの推論。公式の記述で確かめていない
- 「版を固定できる入れ方」は一般論。Claude Code のプラグインや MCP で版を固定する具体の方法は確かめていない
- 「読み込まれる全部の一覧を作る」の具体のコマンド（`/mcp` など）は、確かめていないので書いていない
- 3 つの雛形の動作（expect）は、実機で試していない
- 2026 年の追試の対象のモデルの名前（Claude Sonnet 4.6 など）は本文に書いていない（「現行世代を含む 5 つ」と書いた）。「現行」は日付が動く語なので、必要なら直してほしい
- アプリ側（コネクタ・プラグイン・スキル）の確認の手順は、それぞれのページへ振っただけで、中身は確かめていない

## 使用量

- 道具の呼び出し：約 14 回（Read 3・Bash 5・Write 7 のうち報告を含む）
- Web の取得：0 回
