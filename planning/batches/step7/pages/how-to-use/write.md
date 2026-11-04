# 報告：執筆（how-to-use）

- 手引きの版：共通 2026-11-04 第1版・型（guide）2026-11-04 第1版
- 結果：docs/start/how-to-use.md を draft で書いた。節は10とも置いた。作者の承認が要る2節（freshness・report）は、承認前の文を入れず「準備中」の1文にした（案は 5 の 1）

## 1. 書いたファイル

- docs/start/how-to-use.md（stubs/start/ から mv。docs/start/ は新しく作った）。front matter は stage を stub から draft に、sources を13件足した。sections と updated（2026-11-04）は変えていない
- docs/img/how-to-use/page-anatomy.svg（目次の visual「ページの見取り図」。static）
- snippets/how-to-use/ask-ai-with-llms-txt.txt と同名の .expect.yaml（prompt の雛形1つ。目次の templates は空だが、llms-txt の節の手順をそのまま渡せるので足した）
- data/sources.d/how-to-use.yml（新しい出典7件。どのドメインも data/sources.yml の domains で確かめ済み）

## 4. 止められた操作

- 描画を見るため、サイトの元を作業用のフォルダ（scratchpad）へコピーして mkdocs build する操作が、権限に止められた（2回）。回り込まず、描画の検査（render_pages.py）は流していない。SVG だけは headless Chrome で描いて見た（崩れなし）

## 5. メインに判断してほしいこと

1. **作者の承認が要る文の案（共通 §18）**。承認されたら、2節の「準備中」の1文を置き換える。そのとき summary と要点の「誤りや古い情報」も本文と合う。期限の日数（365・90・30）は書いていない。正本は schema/site.yml の volatility_days で、本文に書くなら fact の目印が要る（facts は出典を持つ外部の値向き）。返事や直す時期は約束していない
   - 案 A（節 freshness「確認日と期限切れの注意書き」）：
     > 確認日と期限切れの注意書きは、ページの情報がいつ時点のものかを示す。
     >
     > ページ上部の確認日のバッジは、出典を読み直した日と、そのとき使った版を示す。点検で影響がないと確かめた日があれば、バッジにポインタを置くと「点検」の日として出る。下書きのページには確認日がなく、「未検証」と出る。
     >
     > ページごとに期限の日がある。ページの確認日（読み直した日と点検の日の新しいほう）にページの期限を足した日と、ページが含む各数値の確認日に数値の期限を足した日のうち、早いほうを、道具が計算する。変わりやすさが高いほど、期限は短い。
     >
     > 期限の日を過ぎたページには、「確認の期限切れ」の注意書きが出る。ブラウザが今日の日付と期限の日を比べて出すので、JavaScript が動かない環境では出ない。注意書きが出たページの助言は、使う前に公式の文書で確かめる。
   - 案 B（節 report「誤りや古い情報の報告」）：
     > 誤りや古い情報を見つけたときは、ページの最下部にある「このページの誤りを報告する」から、GitHub の Issue を開ける。ページの題名・URL・確認日・更新日は、あらかじめ入る。GitHub のアカウントが要る。
     >
     > 報告には、次のことを書いてほしい。
     >
     > - どのページの、どの記述か（題名と URL）
     > - そのページの確認日と版
     > - 何が違うか（食い違う公式の文書などの URL。読んだ日と版があれば添える）
     >
     > 連絡の窓口の全体は、link の目印で ai-and-sources#contact を指す。

     「報告への返事と、直す時期は約束しない」と書くか、何も書かないかは、作者が決める（型の手引き guide §3 は、この辞典がすること・しないことと窓口だけを書くとしている）
2. **症状辞典の入口を直接指す件（catalog notes の (6)）**。`../symptoms/index.md` の手書きリンクは、check_pages「未公開のページへのリンク」が止める（docs/symptoms/index.md がまだない）。「ナビゲーションの『症状辞典』」の平文にした。公開後に手書きのリンクへ直すか、link の目印が分野の入口を指せるようにするか
3. **公開の約束と紛らわしい文**。次は、約束ではなく書き方・仕組みの説明として置いた。承認の対象に含めるか確認してほしい
   - 根拠の強さの節の「読み方の決まり」4項目（モデルの世代を添える・傾向と標本・自己申告と経験則・三段）
   - 面のタブの節の最後（Claude Code は WSL と Linux の CLI を基準にし、ほかは「未確認」と書く）
   - 公式との分担の節の「この辞典は演習を載せない」
4. **確認日の意味が3か所で違う**。バッジは verified（点検の日は title 属性）、llms.txt は verified と checked の新しいほう、期限の計算も新しいほう（design §9.2）。節 badges は「出典を読み直した日と、そのとき使った版」と書いた。案 A はこの違いをそのまま書いた
5. **バッジの列と段階の表示名**。design §6.4 は5項目（レベル・原理・成熟度・変わりやすさ・確認日と版）だが、overrides/main.html は型・面・強制力・段階も出す。節 badges は main.html のとおりに書いた。reviewed の表示名は tools/gen/config.yml の「検証済み」を使った（catalog notes の「design 第2版に合わせる」は確かめていない）
6. **公式の学習サイトの名前**。guides・catalog・decisions は「Anthropic Academy」と書くが、academy.claude.com の入口の題名・見出し・ロゴは「Claude Academy」で、「Anthropic Academy」の語はなかった（2026-11-04）。本文は「Claude Academy」と書いた。名前が変わった事実と時期は読めていない
7. **雛形を足した件**。planning/shows.md は how-to-use を「図か表だけ」としている。表と図のほかに prompt の雛形を1つ足した。不要なら、本文の目印（gen:begin snippet 〜 gen:end snippet）と snippets/how-to-use/ の2ファイルを外せば済む

## 6. 提案

```yaml
frontmatter:
  - {id: how-to-use, key: volatility, before: 低, after: 中, reason: "official-docs の表と badges の版の段落が、公式の文書の URL・題名と、更新の通り道（latest・stable）の説明に依存する。月の単位で変わる層。サイトの仕組みの説明だけなら低でよい"}
```

- 用語集（definitions の節。語・定義の案）：「面」＝Claude を使う入口の種類（アプリ・Claude Code・API）。同じ目的でも、面によって手段が違う。「根拠の印」＝研究や数値を根拠にする主張の後に付ける印（根拠：強・中・弱、類推、推論・実践例なし）。「題名（準備中）」＝まだ公開していないページを指す所に、リンクにせず出す表記。相手を公開するとリンクに変わる
- .textlintrc.json（arabic-kanji-numbers）：他ページの題名（「四つの原理と比例則」「五つの段階と上がる条件」）が link の目印の出力に入り、地の文に置くと警告になる（四つ => 4つ）。題名を算用数字にする、規則に許可を足す、目印の出力を検査から外す、のどれかを決めてほしい。このページは目印を表の中に置いて避けた（表のセルには警告が出なかった。表の中は検査されていない可能性がある）
- 数値の提案：なし（本文に変わりやすい値を書いていない）

## 7. 検査の結果

- gen_site.py --page how-to-use：書いた。--check は最新
- check_pages.py --page how-to-use：エラー0・警告0（初回に手書きリンクでエラー1。平文にして解消）
- npx textlint docs/start/how-to-use.md：0。npm run lint:text：このページの指摘は0
- check_templates.py --page how-to-use：0・0。check_svg.py --page how-to-use：0・0
- 描画（render_pages.py）：流していない（4 を参照）

## 8. 確かめていないこと

- 描画（幅 390px のライトとダーク）。3列の表の折り返しと、`llms.txt` の URL（コード）のはみ出しは未確認
- 雛形は実際の AI で動かしていない。URL の先（llms.txt）はまだ公開されていない
- 公式の文書は 2026-11-04 に読んだ：高度なセットアップ（日英）・Claude Code の llms.txt・CLI リファレンス（英。--version の行）・Platform の入口（日）・ヘルプセンターの入口（日）・Claude Academy の入口・GitHub の2つの README・ベストプラクティス（日）。「すべての設定」は先頭10万字までしか読めていない（latest と stable の説明は高度なセットアップで確かめた）
- ヘルプセンターのリリースノートに日本語版があるかは見ていない（英語の URL を書いた）。ヘルプセンターが扱う範囲（画面の操作・プラン・請求）は、Platform の入口の説明と既存の出典による
- 「公式の日本語版で同じ語の表記が割れる」は decisions 2026-11-04 と prh.yml の説明による。原文は読み直していない
- 「同じ名前のタブは一緒に切り替わる」は mkdocs.yml の説明による（実機で見ていない）

## 9. 使用量

- 道具の呼び出し 約70回（Web の取得12回・curl 2回を含む）。トークンと時間は測っていない
- 束の3ファイルのほかに開いたもの：overrides/main.html・tools/gen/config.yml・pages_out.py（バッジ・段階の表示名と llms.txt の形を確かめるため）、schema/site.yml・mkdocs.yml・.textlintrc.json・prh.yml・tools/checks/body.py・tools/gen/snippets.py と、data/sources.yml・start の骨格9件の front matter（出典の重なりとリンク先の anchor を確かめるため）
