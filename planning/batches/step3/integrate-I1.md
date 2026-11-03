# 工程3 I1：目次の統合の報告（start・changes・basics・judgment）

- 担当：I1（2026-11-04）
- 書いたもの：[planning/catalog/start.yaml](../../catalog/start.yaml)・[changes.yaml](../../catalog/changes.yaml)・[basics.yaml](../../catalog/basics.yaml)・[judgment.yaml](../../catalog/judgment.yaml)・この報告
- 読んだもの：brief-integrate.md、catalog/README、design §2〜§4・§6.2（とメインが直した §7・§8.4・§9.1・§10.8）、schema/site.yml、材料 `state/step3-integrate/I1-input.md`、受け持ちの4ファイル、catalog-C1.md・catalog-C10.md、catalog-C12.md §7、registry の ledger、features.yaml、ほかの分野のファイル（読むだけ）、research/22 #3・§3.4、research/23 §4.2、research/27 #18、02 §1-2・§5、00 §4
- ページの id と anchor は消していない・変えていない（anchor を1つ足した）。ページの追加・統合・削除・分野の移動はない。git と Web は使っていない
- 変えたページは25（start 7・changes 3・basics 13・judgment 2）。どれも notes の末尾に「（2026-11-04 統合：…）」を付けた。各ファイルの冒頭にこの報告への注記を入れた。open_issues は工程2の記録として変えていない

## 1. 材料 A の各項目の扱い（54件）

| 番号 | 扱い | 変えたページ・反映しない理由 |
| --- | --- | --- |
| start#1 | 取り込み済みを確かめた | judgment の human-pitfalls は six-causes を関連に持つ。human-pitfalls-intro を指すページはない |
| start#2 | 取り込み済みを確かめた | 症状の全33ページが six-causes を前提か関連に持つ（symptoms の持ち分） |
| start#3 | 反映しない（M11） | 印のキーは足さない。生成の6ページ（reverse-index・glossary・roadmap・knowledge-map・outdated-advice-ledger・change-timeline-2026）の notes に「生成」とあるのを確かめた |
| start#4 | 取り込み済みを確かめた | design §7 に用語集の行がある。terminology の notes の「design §7 にない」を直した |
| start#5 | 反映した | glossary の notes：旧名の印と変わった時期は、数値ファイルの名称の項目を aliases と照らして生成する（design §7・§9.1、M7） |
| start#6 | 反映した（M1） | 受け持ちの要約4つを M1 の表に揃えた（§3）。terminology の notes に決めたことを書いた |
| start#7 | 反映した | ai-and-sources の notes に、作者に見せる時期（第一波の最初のバッチより前。design §10.8）を書いた |
| start#8 | 反映しない（M10） | wave は変えない |
| basics#1 | 反映した | tokens の notes を、japanese のまとめ（more-tokens-in-japanese → can-i-prompt-in-japanese#tokens）に合わせた |
| basics#2 | 取り込み済みを確かめた | context の promises-after-compaction・compact-and-auto-compact と symptoms の forgot-after-compaction が what-survives-compaction を前提にしている。what-survives-compaction の notes を結果に合わせた（一覧はこのページに一本化） |
| basics#3 | 取り込み済みを確かめた | api の stateless-messages-api は二つ目の案（API に固有の操作に絞り、rereads-whole-history を前提にする）を取った。rereads-whole-history の notes を直した |
| basics#4 | 取り込み済みを確かめた | api の tool-use-loop は agent-loop を前提にしている。agent-loop の notes を直した |
| basics#5 | 取り込み済みを確かめた | agreement-is-not-evidence（judgment）と caves-when-pushed は sycophancy を、verifier-three-conditions と protect-tests は reward-hacking を前提にしている。rewrote-tests-to-pass は verifier-three-conditions を通して届き、関連にも reward-hacking がある |
| basics#6 | 取り込み済みを確かめた | basics 側は済み。instructions-ignored は where-instructions-sit と request-vs-lock を前提にした。app の where-to-put-instructions と cli の init-and-first-claude-md は前提にしていない（「前提にできる」という任意の提案で、相手の判断） |
| basics#7 | 取り込み済みを確かめた | prompting の long-context-first は lost-in-the-middle を関連に置いた。lost-in-the-middle の notes を直した |
| basics#8 | 取り込み済みを確かめた | verify の fact-checking は why-hallucinations を前提にし、nondeterminism・summary-overgeneralization を関連に置いている |
| basics#9 | 反映した（M1） | start#6 と同じ |
| surfaces#4 | 取り込み済みを確かめた | product-map は choosing-a-surface・where-it-runs・claude-code-surfaces・peripheral-products などを指している |
| models#1 | 反映した | outdated-advice-ledger の related に effort-levels・choosing-a-model を足した（thinking-keywords と同じ扱い）。notes の「行の材料」に、budget-tokens と avoid-opus-as-expensive の行からのリンクを書いた |
| models#4 | 取り込み済みを確かめた | how-thinking-works は effort-levels・thinking-keywords・choosing-a-model を、checking-for-updates は suspected-degradation・after-switching-models を指している |
| prompting#6 | 取り込み済みを確かめた | think-before-asking の related の先頭が ask-for-options |
| prompting#9 | 反映した | outdated-advice-ledger の notes の「行の材料」に、important-caps の今どうするかと時期を書いた（research/23 §4.2） |
| prompting#10 | 取り込み済みを確かめた | nondeterminism が outdated_advice で lower-temperature を指している（notes に書き添えた） |
| context#3 | 反映した | what-survives-compaction の notes に、11 第3節 3-2 #5 の「skill の一覧は圧縮の後に戻らない」を使わないことを書いた |
| context#4 | 反映しない（M8） | 目次は変えない。rereads-whole-history の notes に「執筆のときに公式の図と比べて決める」と書いた |
| context#5 | 反映した | subagent-isolation の outdated_advice に subagents-to-save-context（M3）を足した。台帳の notes に、この行の今どうするかと、save-context-for-200k の idle compaction を書いた |
| app#3 | 反映した | styles-for-tone は registry に入った（M3）。台帳の notes に行の今どうするか・時期・状態を書き、台帳の数を37項目に直した（ファイル冒頭の注記・notes・materials） |
| app#5 | 反映した（M7） | terminology の notes、節 same-names-across-surfaces（新しい anchor）、related（how-memory-works・using-auto-memory・skills-in-the-app#migrated-styles・output-style-modes） |
| cli#5 | 反映した（M7） | terminology の notes に plan モード（仮。別名にプランモード）を書いた |
| cli#6 | 反映した | checking-for-updates の notes に stable と latest の通り道を書き、sign を1つ足した（§2） |
| cli#10 | 取り込み済みを確かめた | cli の command-cheatsheet は glossary#old-names を指し、anchor がある |
| extend#3 | 反映した | context#5 と同じ（subagent-isolation の outdated_advice） |
| verify#3 | 反映した | learning-with-ai の notes：A-16 の雛形はこのページだけに置き、own-generated-code は出荷の基準として書き分ける |
| eval#4 | 取り込み済みを確かめた | decide-when-to-quit は experiment-log・selection-pressure を指している |
| enforce#2 | 反映した | what-survives-compaction の related の when-to-lock を when-to-lock#spoken-rules-fade にした。受け持ちに spoken-prohibitions-fade を指すページはない |
| safety#6 | 取り込み済みを確かめた | data-vs-instructions の related の先頭が prompt-injection-in-practice |
| safety#10 | 反映した（M6） | four-principles と roadmap の related に default-safety-settings#by-stage を足し、notes に「既定の中身を繰り返さず正本を指す」と書いた。four-principles は related が20件を超えるので terminology を外した（how-to-use と glossary から入れる） |
| delegate#1 | 反映した | outdated-advice-ledger の related の goal-until-done を goal-until-done#from-homemade-loops にした |
| delegate#2 | 反映した | terminology の notes（読者の「委任の段階」と作業ごとの「任せ方の段階」を節 definitions で分ける）と related（five-questions-before-delegating#autonomy-stages）。roadmap の related に terminology#definitions を足し、notes に書いた |
| delegate#7 | 取り込み済みを確かめた | four-principles・roadmap・decide-when-to-quit・how-much-understanding-to-keep が delegate のページを指している |
| judgment#1 | 反映した | verify#3 と同じ（learning-with-ai） |
| judgment#2 | 取り込み済みを確かめた | delegate の what-not-to-delegate は任せるのまま |
| judgment#3 | 対象外（symptoms） | caves-when-pushed と wont-rethink-approach は案のとおり。going-in-circles の related に decide-when-to-quit はまだない（§7） |
| cost#1 | 反映した | glossary と change-timeline-2026 の notes に、プランの改名と上限の呼び方の変更を数値ファイルの名称の項目から入れると書いた |
| cost#3 | 取り込み済みを確かめた | 受け持ちの側に関わるのは tokens の関連だけで、japanese#1 で直した |
| japanese#1 | 反映した | tokens の related の can-i-prompt-in-japanese を can-i-prompt-in-japanese#tokens にした |
| japanese#3 | 反映した | tokens の notes に分担（ここは仕組みと日本語の量の考え方、節約の判断と数え方は can-i-prompt-in-japanese#tokens）を書いた |
| japanese#6 | 反映した | 台帳の materials と notes に、日本語の「熟考」の一次資料（CHANGELOG 1.0.8。research/27 #18）を書いた。Styles の行は japanese の consistent-politeness・align-japanese-output が outdated_advice で指している（I3） |
| team#3 | 取り込み済みを確かめた | judgment の5ページと four-principles（ai-amplifies-organizations）が team のページを指している |
| contest#2 | 取り込み済みを確かめた | 受け持ちに、まとめた3候補を指す参照はない。think-before-asking は format-cheatsheet#heuristic を指している |
| contest#5 | 対象外（メイン） | kyopro-atlas との書き方の食い違いの報告。受け持ちの側に変えるものはない |
| symptoms#9 | 反映した（一部）・メインへ | six-causes の related に、使うの段の必須の症状で抜けていた plausible-falsehoods を足した。related は20件までなので全33は置けない。全ページへの道は、節 to-symptoms の表（症状のページの prevents・pitfalls から生成）と逆引き（signs から生成）で作ると six-causes・reverse-index の notes に書いた。生成の設定は §5 の1 |
| symptoms#12 | 取り込み済みを確かめた | summary-overgeneralization の related の先頭が summary-overstates-source |
| changes#2 | 取り込み済みを確かめた | old-and-new-names を指すページはない。glossary の aliases に「旧名と新名の対応表」を足した |

## 2. 材料 B の行の扱い

| # | 項目 | 扱い |
| --- | --- | --- |
| 11 | 推論の過程を全部見せてほしい | basics/unfaithful-reasoning に `{type: goal, text: "推論の過程を全部見せてほしい"}` を足した |
| 28 | 1M コンテキストなら気にしなくてよいのか | 足さない。attention-budget に同じ意味の goal「コンテキストが広くなったのなら、資料を全部入れてよいのか知りたい」がある（C1 が変わりやすい値の「1M」を除いて書いた形） |
| 64 | 「think hard」は効くのか | changes/outdated-advice-ledger に `{type: goal, text: "「think hard」は効くのか"}` を足した |

**M2 の3つ目（症状の文を対処のページに重ねない）に合わせて外した文**。どれも 00 §4 の症状の項目で、症状のページの signs にある。B の行の外だが、M2 の理由（同じ文が二か所に出ると振り分けを飛ばす）がそのまま当たるので直した。症状のページから外したページへの道（前提か関連）があることは確かめた。

| ページ | 外した文 | ある症状のページ | 代わりに置いたもの |
| --- | --- | --- | --- |
| basics/context-rot | 会話が長くなると精度が落ちる | forgets-in-long-chats | goal「長い会話で答えの質が落ちていく理由を知りたい」 |
| basics/knowledge-cutoff | 最近の出来事や新しい版について間違える | doesnt-know-latest | goal「Claude が最近の出来事や今日の日付を知らない理由を知りたい」 |
| basics/nondeterminism | 同じ質問で毎回答えが違う | plausible-falsehoods（「どれが正しいか分からない」まで補った形） | goal「同じ頼み方でも答えが毎回変わる理由を知りたい」 |
| basics/sycophancy | こちらの誤った指摘にも、すぐ同意する | caves-when-pushed | なし（goal「Claude が賛成しがちな理由を知りたい」が残る） |
| changes/outdated-advice-ledger | 古い記事や本のやり方が今は通じない | doesnt-know-latest（「古い記事のやり方が通じない」） | なし（#64 を足した） |

**B のほかに足した sign**（新しい節や notes の中身に合わせたもの）

- start/terminology：goal「アプリと Claude Code で名前が同じ機能が、同じものか知りたい」（M7 の区別を書く節 same-names-across-surfaces の入口）
- changes/checking-for-updates：symptom「公式の文書にある機能やコマンドが、手元では見つからない」（cli#6。対応する症状のページはない）

## 3. 題名を変えたページ

なし。M1 の表で受け持ちの題名を確かめ、変える語はなかった。「圧縮（compaction）」「思考（thinking）」のような英語の併記は、ほかの分野（自動メモリ（auto memory）など）と同じ書き方なので残した。

M1 で直した要約（と、合わせて直した図の案）：

| ページ | 前 → 後 |
| --- | --- |
| basics/rereads-whole-history | cache で安くなる → キャッシュで安くなる |
| basics/why-prompt-caching | そこから後の cache が外れる → キャッシュが外れる（後半の文も §4 の見直しで直した。図の案も同じ） |
| basics/request-vs-lock | skill・hook → スキル・フック（図の案の skill・hook・sandbox も、スキル・フック・サンドボックスに） |
| judgment/postmortems | CLAUDE.md・hook・レビュー → CLAUDE.md・フック・レビュー |
| changes/outdated-advice-ledger（図の案だけ） | hooks・auto mode と sandbox・skills → フック・auto モードとサンドボックス・スキル |

## 4. 新しいページ、priority・level を変えたページ

- 新しいページ：なし。priority を変えたページ：なし
- **level を変えた：basics/why-prompt-caching 任せる → 整える**（M9 の「level がそもそも合っているか」）。最初に要るのは長い作業を任せる段階ではなく、資料の置き方や effort・モデルの使い方を整える段階と判断した。アプリでもプロジェクトに置いた資料はキャッシュされ、使用量が抑えられる（02 §1-2・§5、Help Center の Usage limit best practices。訂正・注記なし）。これを関連に置く app の using-projects、effort を変えるとキャッシュが外れる how-thinking-works、cost の what-uses-up-limits はどれも整える。あわせて面にアプリを足し（タブで並べる）、related に using-projects を足し、要約の後半を「途中で何を変えないかと、よく使う資料をどこに置くかを決める土台になる」にした。段の規則は保たれる（前提の rereads-whole-history は使う、このページを前提にする api の prompt-caching-in-practice は仕組みにする）。優先度は推奨のまま。費用の仕組みの説明で、任せる幅を広げる内容ではない（notes に書いた）。下げたので比例則の警告は消えた
- 足した anchor：start/terminology の `same-names-across-surfaces`（面ごとに似た名前の機能）

## 5. メインへ（3件）

1. **six-causes の節 to-symptoms の表の生成**（symptoms#9）：症状の全33ページへの道は related（20件まで）では作れない。手書きのページの一部を、症状のページの prevents・pitfalls から生成する（design §8.4 の gen の目印）よう、土台作りで作る層の設定に入れてほしい。逆引き（reverse-index）は signs から生成するので、そちらは設定のままで全ページに届く
2. **検査の提案（check_catalog.py）**：症状のページの sign と同じ文が、ほかのページの signs にあれば警告する（M2 の3つ目を保つ。§2 の5件は工程2で入ったもの。執筆者が sign を提案するときにも戻りうる）。2026-11-04 の時点で、ほかの分野に同じ文は見つからなかった（似ている度合いで全分野を探した）
3. **glossary と terminology の id**（C1 の報告の迷った点2）：claude-atlas は glossary を用語索引（生成）、terminology を用語集（手書き）にしたが、kyopro-atlas は glossary を用語集、term-index を用語索引にしていて、英語の glossary もふつうは用語集を指す。id は URL になるので、入れ替えるなら骨格の前に決める（ほかの分野から glossary・glossary#old-names を指すページが多い）

## 6. 検査の結果

`python3 tools/check_catalog.py --field <field>`（最後の実行、分野のファイル23・ページ361）

| 分野 | エラー | 警告 |
| --- | --- | --- |
| start | 0 | 0 |
| changes | 0 | 0 |
| basics | 0 | 0 |
| judgment | 0 | 0 |

- 統合の前は basics に比例則の警告が1件（why-prompt-caching）あった。§4 の段の見直しで消えた
- 全体の検査（`python3 tools/check_catalog.py`）は、エラー0・警告4（比例則：extend の agents-md、api の feature-to-api-mapping・prompt-caching-in-practice、team の ideate-independently。どれもほかの担当の分野）
- 道具が見ない点も確かめた：受け持ちの題名・要約・sign・別名の半角と全角の間の空白、数字（年表の「2026 年」だけで、範囲を示す年）、別名が題名と同じでないこと、要約の字数（最長は why-prompt-caching の110字）
- 台帳の37行は、どれもいずれかのページの outdated_advice から指されている（2026-11-04 の時点。ほかの担当が書いている途中の数え）

## 7. 確かめていないこと、迷った点

**確かめていないこと**

- 一次資料は見ていない（Web を使わない指示）。why-prompt-caching のアプリの面の根拠は 02 §1-2・§5（確認日 2026-10-29）だけで、プロジェクトの資料がキャッシュのどの段に入るかは確かめていない（図の案には書かなかった）
- going-in-circles（symptoms）の related に decide-when-to-quit がない（judgment#3 の案。I7 の材料にもある）。I7 の報告で入ったかを確かめてほしい
- ほかの担当が同時に書いているので、ほかの分野への参照（default-safety-settings#by-stage・when-to-lock#spoken-rules-fade・goal-until-done#from-homemade-loops・can-i-prompt-in-japanese#tokens・five-questions-before-delegating#autonomy-stages・skills-in-the-app#migrated-styles など）は最後の実行の時点で解決している、というところまで

**迷った点**

1. **why-prompt-caching の段を下げたこと**（§4）。任せるのまま notes に理由を書いて警告を残す道もあった。最初に要る段の規則で決めたが、メインが任せるに戻すなら、notes の理由の文を戻せば足りる
2. **既にあった症状の文を外したこと**（§2）。M2 の文面は B の行を足すときの指示だが、理由がそのまま当たるので受け持ちの5件を直した。似た意味でも文が違うものは残した：judgment/agreement-is-not-evidence「Claude も賛成したのに、方針が間違っていた」と caves-when-pushed「Claude も賛成したのに計画が失敗した」、knowledge-cutoff「古い版の書き方を、今の方法として勧めてくる」と doesnt-know-latest「古い書き方のコードや設定を出してくる」、data-vs-instructions「読ませた資料の中の指示に従ってしまった」と followed-injected-instructions「読ませた Web ページに書かれた指示どおりに動いた」。ほかの分野にも似た組がある（enforce の when-to-lock と instructions-ignored など）
3. **B #28 を足さなかったこと**。既にある sign は「資料を全部入れてよいか」で、項目の「気にしなくてよいか」より少し狭いが、答え（窓に入ることとよく使えることは別）が同じなので同じ意味と読んだ
4. **four-principles から terminology を外したこと**（related の20件の上限）。比例則の節に近い default-safety-settings#by-stage を優先した
5. **terminology に節と sign を足したこと**。M7 の区別（アプリのメモリと自動メモリ、Styles と出力スタイル）を受ける場がなかったので、features.yaml の note にある面ごとに似た名前の組とあわせて1つの節にした
6. **台帳の notes が長くなったこと**。design §9.1 が「台帳の行の変わった時期の材料は changes の目次の notes と changes#3」とするので、data/outdated-advice.yml を作るときの材料（important-caps・think-hard-keywords・research/22 §3.4 の3行・リンク先・足した2行）を outdated-advice-ledger の notes にまとめた
