# 工程4：目次の直し F3（prompting・japanese・context）

- 担当：F3。日付：2026-11-04。指示：[brief-fix.md](brief-fix.md)
- 書いたファイル：`planning/catalog/prompting.yaml`・`japanese.yaml`・`context.yaml` と、この報告だけ
- 読んだもの：design-review.md（全部）、catalog/README.md（全部）、schema/site.yml、review-R1.md・review-R3.md（全部）、review-R2.md・review-R4.md（受け持ちのページに触れる行と R2-13）、fix-aliases.md、受け持ちの3ファイル（全部）。ほかの分野は、関わるページを読むだけにした（symptoms の全ページの signs・前提・関連、basics・verify・models・cli・extend・judgment・app・api・enforce・recipes の関わるページ、features.yaml、registry.yaml の該当行、research/00・02・03・04・25・27 の該当箇所）
- 言い換えの重なりは、作業用の一時の道具（リポジトリの外）で、受け持ちの signs と症状のページの signs・ほかのページの signs の全組を2字の重なりと difflib の比で並べ、上位と、症状のページが前提・関連で指す組を目で見て決めた
- ほかの担当が同時に直していたので、最後の検査の前にもう一度読み、notes を今の状態に合わせた

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | prompting：emphasis-words・state-the-scope・share-targets-and-bounds・output-shape・xml-tags・let-claude-ask・ask-for-options・allow-i-dont-know・permission-to-stop・requesting-prose・show-examples。japanese：align-japanese-output・keep-replies-in-japanese・consistent-politeness・less-ai-sounding-japanese・textlint-hook。context：rewind-dont-correct・promises-after-compaction・inspect-context・handing-long-documents | 症状のページの困りごとの言い換えを、goal か、その対処が直接の答えになる狭い場面にした（§2）。R3 付表A のうち受け持ちの5組（6・8・12・14・15。R1-04 の受け持ちの3組はこの中に入る）のほか、道具と目で見つけた言い換え（plausible-falsehoods・rewrote-tests-to-pass・misses-broken-evaluation・not-what-i-meant・inconsistent-japanese-style・skipped-later-pages・going-in-circles・too-slow・followed-injected-instructions）も直した。対処のページどうしの近い文は DR-15 に沿って、同じ問いは同じ文にそろえ（show-examples と requesting-prose）、そうでないものは場面を書き分けた（emphasis-words・output-shape・let-claude-ask・ask-for-options） | R1-06 の「長い作業を明日も続けたい」（handoff-documents・progress-files と cli の resume-and-branch）は、わざと1つの問いにまとめた同じ文なので変えていない（progress-files の notes に理由がある）。R1-06 の (3)「強調しても守られない」は、強調の効き目に直接答える emphasis-words を持ち主にして残した（basics と extend は同じ工程で外すか goal にした） |
| b | なし | — | 受け持ちの signs を「記事・古い・前は・手元・以前・通じない」で探して、該当は0件（「古い業務システム」の1件は別の意味） |
| d | compact-and-auto-compact・images-and-voice・rewind-dont-correct | 外す側の別名を外した。images-and-voice の「音声入力」は例外として残した（§3） | — |
| e | textlint-hook | 推移的な前提 hooks-basics を外して related に移した（§4） | 推移的な前提の警告は、工程4の前の時点で受け持ちに1件だけだった。delegate の付表B は受け持ちにない |
| h | ask-for-options | R1-18：goal「設計や技術の選び方を壁打ちしたい」と別名「設計の壁打ち」を足した | R1-13〜R1-17 は受け持ちのページにない |
| p（F1 の行） | long-context-first・handing-long-documents | basics が lost-in-the-middle を context-rot にまとめた（節 lost-in-the-middle）ので、related を `context-rot#lost-in-the-middle` に指し直した | — |
| q | does-double-check-work（prompting） | 独自の判断を notes に1行で書けないので、verify の verification-ladder（節 verbal-checks）にまとめた（§5）。受け持ちからの参照（allow-i-dont-know・before-after-prompts）は `verification-ladder#verbal-checks` に指し直した | — |
| u | refine-in-conversation・rewind-dont-correct | refine-in-conversation の節 edit-the-request は1行にして rewind-dont-correct を指す、と notes に書いた（anchor と題は変えない）。訂正を重ねる場面の sign は rewind-dont-correct の1か所にし、refine-in-conversation には直接答える goal を足した。rewind-dont-correct の sign は going-in-circles の言い換えでもあったので、訂正を書く前の状況の形にした | refine-in-conversation の summary の2文目（ずれが大きいときは頼み直す）は、1行の節と食い違わないので残した |
| v | inspect-context | /context の内訳の読み方の持ち主が節 reading であること、/usage の持ち主は what-uses-up-limits#find-what-uses-it であることを notes に書いた。持ち主のページを読むのに見る道具の一覧は要らないので、前提の usage-context-statusline を related の先頭に移した | cli の usage-context-statusline は F4 が同じ工程で inspect-context#reading を指す形にし、別名 /context も外していた（読んで確かめた） |
| w | suggest-or-do・asking-for-reasoning・before-after-prompts | summary の1文目を「答えそのもの」か「何ができるか」にした（suggest-or-do：動詞で書き分けると何が減るか。asking-for-reasoning：理由を知りたいときにすること。before-after-prompts：自分の依頼に足りないものを見つけられる）。字数は 87・89・98 | settings-layers は F4 の受け持ち |
| x | なし | — | 症状のページの routes は F7 の受け持ち。受け持ちのページは振り分け先になるだけで、直すものはない |
| ほか（i・n・o・DR-18） | なし | — | 受け持ちのページは memory-faq・改名した id・題名の変わりやすい値・名称の台帳の行を持たない（n の large-context-window はメインが直し済み） |
| DR-17 | suggest-or-do・asking-for-reasoning・before-after-prompts | summary の1文目は w で反映した | 「見せ方」を notes に書くことはしていない。メインが試作の前に題材の一覧を作るとあり、書き方（形）が設計書の第2版でまだ決まっていないため。候補は §6 の6 |

## 2. 言い換えの重なり（a）で直した sign

「重なり」は、重なっていた相手のページと文。種類が変わったものは（前の種類→後の種類）を添えた。

| ページ | 前 | 後 | 重なり |
| --- | --- | --- | --- |
| emphasis-words | 絶対に守らせたい規則がある（goal） | 強調に頼らずに、大事な指示を守らせたい | when-to-lock「例外なく守らせたい規則がある」と同じ問い（DR-15 の書き分け） |
| state-the-scope | 小さな修正のつもりが、大きな書き換えになった（symptom→goal） | 小さな修正は、小さいまま終わらせたい | does-more-than-asked「小さな修正を頼んだのに周りまで書き換えられる」（付表A の14） |
| share-targets-and-bounds | 少し改善しただけで「これ以上は難しい」と言う（symptom→goal） | 最適化を、目標の値に届くまで粘らせたい | wont-rethink-approach「少し試しただけで「これ以上は無理です」と言われる」（付表A の6、R1-04） |
| output-shape | 決まった形式で必ず返させたい（goal） | 返事の書式や長さを、用途に合わせて指定したい | structured-outputs-basics「出力を必ず決まった形で受け取りたい」と同じ問い（形の保証はあちらが直接の答え。DR-15） |
| xml-tags | 資料の中の文を、こちらの指示と取り違える | 指示・資料・例を一つの依頼に詰め込むと、どれがどれか混ざる | followed-injected-instructions の題名「読ませたページやファイルの指示に従ってしまった」・別名「資料の中の指示に従う」 |
| refine-in-conversation | 訂正を重ねるほど返事がこじれていく（symptom） | 外した。goal「返事を見ながら、依頼を少しずつ詰めたい」を足した | rewind-dont-correct の sign（R3-24。u） |
| let-claude-ask | 作らせてから、前提の食い違いに気づく | 頼んだ後になって、伝え忘れた条件が次々に出てくる | spec-first・when-to-plan と同じ困りごと（逆引きで近い行が3つ。DR-15） |
| ask-for-options | AI の最初の案にそのまま引っ張られてしまう | 一つの案しか出てこず、ほかと比べられない | think-before-asking「最初に AI の案を見ると、それ以外が思いつかなくなる」（順序の本体はあちら。DR-15） |
| allow-i-dont-know | 知らないはずのことまで自信満々に答える（symptom→goal） | 分からないときは、分からないと答えてほしい | plausible-falsehoods（もっともらしい嘘） |
| allow-i-dont-know | 存在しない文献や数字を、それらしく出してくる（symptom→goal） | 根拠のない部分は、推測だと分かるように書いてほしい | plausible-falsehoods「存在しない論文や URL を挙げられる」（付表A の12） |
| permission-to-stop | テストが通らないと、テストのほうを変えて通そうとする（symptom→goal） | テストが間違っていそうなら、書き換えずに報告してほしい | rewrote-tests-to-pass「テストのほうを書き換えて通された」 |
| permission-to-stop | 評価のおかしさに気づいても、黙って進める（symptom） | 外した（goal「仕様と食い違うときは、手を止めて知らせてほしい」が同じ場面を受ける） | misses-broken-evaluation「評価のやり方の誤りを指摘してくれない」 |
| requesting-prose | 書かせた文章が、型どおりの言い回しばかりになる | 「もっと自然に」と頼んでも、文章が良くならない | not-what-i-meant「文章が AI っぽい」、less-ai-sounding-japanese の sign |
| requesting-prose | 飾りが多く、中身の薄い文章になる（symptom→goal） | 読み手と目的に合った文章を書かせたい | not-what-i-meant「文章が AI っぽい」 |
| show-examples | 自分の書き方に寄せた文章を書かせたい（goal） | 自分の文体に近い文章を書かせたい | requesting-prose と同じ問いなので同じ文にそろえた（逆引きで1行に束ねる。DR-15） |
| align-japanese-output | 日本語で、と何度書いても英語や文体の揺れが戻ってくる（symptom→situation） | 日本語の指示を足しても揃わず、仕組みにすべきか迷っている | replies-in-english・inconsistent-japanese-style |
| keep-replies-in-japanese | 日本語で話しているのに、途中から返事が英語になる | 言語を日本語に設定しても、英語の返事が混ざる | replies-in-english の3文（付表A の8、R1-04。狭い場面は R1-04 の例） |
| keep-replies-in-japanese | 日本語の設定や指示をしても、英語に戻る（symptom→goal） | Claude Code の返事を、いつも日本語にしたい | 同上 |
| keep-replies-in-japanese | ツールを使った直後の一言だけ英語で出る（symptom→goal） | 最後の返事が英語のときは、自動で日本語に直させたい | 同上（replies-in-english「ツールの結果を読んだ後の一言だけ英語になる」） |
| consistent-politeness | 途中から文体が変わる（symptom→goal） | 文書を、です・ますか、だ・であるのどちらかに揃えたい | inconsistent-japanese-style「指定した文体が長い文章の途中で崩れる」 |
| less-ai-sounding-japanese | 日本語の文章が「AI っぽい」定型の言い回しばかりになる | 推敲を頼んでも、日本語の言い回しの癖が直らない | not-what-i-meant「文章が AI っぽい」 |
| textlint-hook | 何度言っても表記の揺れが残る | 用語集を渡して頼んでも、表記の揺れが残る | inconsistent-japanese-style（別名「表記ゆれ」、sign「「サーバー」と「サーバ」が混在する」） |
| rewind-dont-correct | 「そうじゃない」と何度返しても方向が直らない（symptom→situation） | 期待と違う返事が来て、訂正を書こうとしている | going-in-circles「直してと言うたびに同じ間違いが戻ってくる」、refine-in-conversation の sign（u） |
| promises-after-compaction | 最初に伝えた禁止事項を、途中から守らなくなった（symptom→goal） | 長いセッションで、最初に決めた約束を最後まで守らせたい | forgets-in-long-chats「最初に伝えた前提を途中から忘れる」・forgot-after-compaction（付表A の15、R1-04） |
| promises-after-compaction | 圧縮されても守ってほしいことを、どこに書けばよいか知りたい（goal） | 圧縮のあとも守らせたい約束を、どこに書けばよいか知りたい | basics の what-survives-compaction にあった同じ問いの文にした（basics は同じ工程でその goal を「何が残り、何が消えるのか」に替えたので、置き場所の問いはこのページだけが持つ） |
| inspect-context | 拡張を足してから、起動した直後から文脈が重い気がする（situation→goal） | 拡張を足した後、起動直後にどれだけ場所を取っているか確かめたい | too-slow「入れた拡張が多すぎて重い」 |
| handing-long-documents | 資料に書いてあることを無視した答えが返る（symptom→goal） | 長い資料を、読み落とされにくい形にしてから渡したい | skipped-later-pages「添付したのに読んでいないような答えが返る」 |

足した sign（h）：ask-for-options に goal「設計や技術の選び方を壁打ちしたい」。

狭い場面として残した主なもの：share-targets-and-bounds「最適化を頼むと、早々に打ち切る」（最適化の場面）、emphasis-words「IMPORTANT や「必ず」を付けても守られない」（R1-06 の持ち主）、suggest-or-do「相談のつもりだったのに、ファイルを書き換えられた」、progress-files「新しいセッションのたびに、前回どこまで進んだかを説明し直している」（repeating-the-same-explanation に近いが、進み具合の場面で直接の答えはこのページ）、compact-and-auto-compact「席を外して戻ったら、会話が要約されていた」（放置したときの圧縮）、commit-and-comment-language「返事は日本語なのに、コミットメッセージだけ英語になる」。

asking-for-reasoning の goal「なぜその答えになったのか、過程を全部見せてほしい」は、basics の unfaithful-reasoning が同じ工程でこの文にそろえたので、変えていない（逆引きで1行に束ねる）。

## 3. 別名の重なり（d）

| ページ | 別名 | 扱い | 理由 |
| --- | --- | --- | --- |
| compact-and-auto-compact | compaction | 外した | 主は題名にその語を含む basics の what-survives-compaction（fix-aliases どおり） |
| images-and-voice | voice mode | 外した | アプリの音声モード（Voice mode）で、主は app の voice-and-mobile |
| rewind-dont-correct | Esc を2回 | 外した | 主は cli の checkpoints-and-rewind（同じ機能の操作） |
| images-and-voice | 音声入力 | 残した（外す側だが例外） | features.yaml の voice-dictation の題名「音声入力（/voice）」で、Claude Code の音声入力を扱うのはこのページだけ。外すと Claude Code の音声入力を名前で引けない（アプリの側は音声モードと Quick entry の音声入力） |
| images-and-voice | /voice | 足した | このページが tracks で持つ voice-dictation の公式のコマンド名。外した voice mode の代わりで、ほかのページの別名にない |
| ask-for-options | 設計の壁打ち | 足した | h（R1-18） |
| suggest-or-do・compact-and-auto-compact・inspect-context・keep-replies-in-japanese | 提案だけで止まる・自動圧縮・/context・英語に戻る | 残した | fix-aliases で受け持ちのページが主。自動圧縮と /context は、外す側（basics・cli）が同じ工程で外したのを確かめた。提案だけで止まる・英語に戻るは症状のページ（F7、未着手）に残っている。主の選び方の疑問は §6 の2 |

## 4. 外した前提（e）

| ページ | 外した前提 | 移した先 | 理由 |
| --- | --- | --- | --- |
| textlint-hook | hooks-basics | related（hook-recipes の次） | 前提の block-with-exit-2 からたどって届く（推移的な前提の警告）。フックのレシピなので近く、関連には置く |
| inspect-context | usage-context-statusline | related の先頭 | v に伴う。/context の内訳の読み方の持ち主のページを読むのに、見る道具の一覧は要らない（推移的な前提ではない）。level の規則にも入ってくる道にも影響しない |

## 5. まとめたページ・新しいページ・priority と level

- **まとめた**：does-double-check-work（prompting、推奨・整える）→ verify の verification-ladder（節 verbal-checks）。要点「言葉で確認を書き足すより、確かめる手段を渡す」は verification-ladder の節 verbal-checks と summary の2文目と同じで、00 §3 分野09 もこの区別を検証の階段に置く。証拠の求め方は evidence-not-reports、過剰な確認になるモデルの傾向は models の model-quirks・after-switching-models、台帳 add-double-check は verification-ladder も指していて、独自の判断を1行で書けなかった（R3-17）。merged の reason に書いた。verify の側（F5）は同じ工程で、題名と別名（「「念のため確認して」は効くか」「double-check して」）を verification-ladder の aliases に移し、related から外していた。私が open_issues に一度書いた「節 verbal-checks の level を整えるにする」案は、節の level をページの level 以上にする規則（design §3.1 の5）に合わないと F5 が notes に書いていたので、取り下げた
- **新しいページ**：なし
- **priority・level**：変えていない
- 集計：prompting は 24 → 23 ページ（必須 13・推奨 11 → 10）。context 15・japanese 11 は変わらない。第一波 125（prompting 7・context 5・japanese 6）と必須 174 も変わらない

## 6. メインへ

1. **まとめたページを指す参照（残り1件）**：does-double-check-work を指す symptoms の claims-done-but-isnt の related を直してほしい（verification-ladder をすでに持つので、外すだけでよい）。models の model-quirks・after-switching-models の2件は、F2 が同じ工程で `verification-ladder#verbal-checks` に直していた
2. **症状の言い方の別名の主**（決めきれなかった点）：「提案だけで止まる」（suggest-or-do と keeps-stopping）と「英語に戻る」（keep-replies-in-japanese と replies-in-english）は、fix-aliases では分野の並びで受け持ちのページが主になり、表どおり残した。どちらも名前ではなく困りごとの言い方なので、症状のページを主にするほうが振り分けを飛ばさない（特に keeps-stopping は原因が effort・モデルの傾向・確認の設定・頼み方と複数あり、suggest-or-do は一つにすぎない）。替えるなら、F7 に症状のページの側へ残すよう伝えてほしい。こちらから外す（受け持ちのファイルの2語）
3. **「音声入力」**：images-and-voice（Claude Code の /voice）と app の voice-and-mobile（アプリの音声モードと Quick entry の音声入力）の両方に残る。用語索引で面の印（アプリ・Claude Code）を付けて並べるか、片方を主にするかを決めてほしい。start の用語集の節 same-names-across-surfaces が「音声モードと /voice」を書き分ける
4. **features.yaml の compaction の主のページ**：機能 compaction の題名「圧縮（/compact と自動圧縮）」は context の compact-and-auto-compact（feature）に当たる。別名「compaction」は表どおり basics の what-survives-compaction に残したので、DR-15 で features.yaml に page を持たせるときは compact-and-auto-compact を主にするのが合う
5. **recipes の spec-first（F7）**：symptom「作らせ終えてから、思っていたものと違うと気づく」は、症状の not-what-i-meant「頼んだものと違うものが出てくる」の言い換えに近い。受け持ちの let-claude-ask と cli の when-to-plan は同じ工程で場面を書き分けたので、F7 の a で見てほしい
6. **DR-17 の「見せ方」の候補**（一覧を作るときの材料）：検証ノートは keep-replies-in-japanese#measure（英語への回帰を数える）・commit-and-comment-language#verify-note・documents-in-japanese#pdf、Before/After は prompting の全ページ（ファイルの notes の方針）と before-after-prompts・rewind-dont-correct・long-context-first の visual、制作の記録の題材は handoff-documents・progress-files（上限や区切りで止まって再開した例）と promises-after-compaction（圧縮を越えて約束を残す例）

## 7. 検査の結果

- `python3 tools/check_catalog.py --field prompting`・`--field japanese`・`--field context`：どれもエラー 0 件・警告 0 件（推移的な前提の警告は、直す前の japanese の1件を消した）
- 全体（`python3 tools/check_catalog.py`、最後に流した時点。ほかの担当が直している途中の数）：エラー 4 件・警告 35 件。受け持ちのファイルのものは0件。エラーのうち、私がまとめた does-double-check-work を指すほかの分野の参照は1件（symptoms の claims-done-but-isnt。§6 の1。まとめた直後は models の2件と合わせて3件だった）。残りの3件はほかの担当のまとめ（lost-in-the-middle・memory-faq）を指す symptoms の参照で、受け持ちに関わらない
- 残した警告：なし

## 8. 確かめていないこと

- 言い換えの判定は、2字の重なりと difflib の比の上位と、症状のページが前提・関連で指す組を目で見たもので、言葉の違う言い換えを見落としている可能性がある。狭い場面として残した sign（§2 の末尾）は、F7 が routes を決めた後に見直す余地がある
- ほかの担当が同時に直していたので、相手のページの文は最後に読んだ時点（03:4x）のもの。F7（symptoms・recipes）はまだ始まっていない
- 新しい sign の文が読者の言葉として引かれやすいかは、逆引きを生成して試していない（DR-15 の試作で確かめる）
- 「音声入力」が Claude Code の公式の日本語版での名前かは、features.yaml の題名と research/27・01 の記述に頼った（Web は開いていない）。/voice は research/01 のコマンドの一覧による
- does-double-check-work のまとめ先（verification-ladder、任せる）に、まとめる前の段（整える）の読者が着くことの良し悪しは、本文を書くときに見る（節の level はページの level 以上の規則があるので、目次では下げられない）
