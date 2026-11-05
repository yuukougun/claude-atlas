# build-DM4：推奨のページの数値の提案と強制力を data にまとめる（工程8）

## 結果
- 足した facts：64 件（data/facts.yml の facts の末尾。確認済み 41・未確認 23。表の fact 4 件を含む：chat-sharing-plans・api-credits-eligible-plans-and-amounts・plan-prices-individual・model-prompting-tendencies）。facts は 104 件から 168 件に
- 既存の fact の状態を上げたもの 2 件：incognito-retention-period（未確認→確認済み。incognito-chats の担当が hc-incognito を開いて確かめた、write.md）・artifacts-storage-limit（未確認→確認済み。artifacts-as-apps の提案が 2026-11-05 に hc-artifacts を取得して同じ値と確かめた）
- 強制力を入れた機能：17 件。なし 15（agent-sdk・btw・cloud-sessions・sessions・plugins・app-context-management・insights・usage・feedback・agent-view・cross-session-messaging・projects・usage-credits・code-intelligence・workflows）、お願い 2（research・verify-skill）
- facts-placement-rec.md：85 行（表の行）・38 ページ。足した fact の id 64 件はすべて少なくとも 1 行に出る
- 提案を集めた数：128 ページのうち、提案があるのは 37 ページ（facts-proposal.yml 18 ページ、write.md の proposals のほか）。YAML の提案の項目は 88 件。ほかの 91 ページは「提案なし」か、YAML のない文の提案（下の「入れなかった」）
- 検査：`check_pages.py` エラー 0（警告 4 は比例則 3・前提と関連の数 1 で既存）／facts.schema.json に対する jsonschema 検証 エラー 0
- 道具の呼び出し：約 45 回。Web 0 回。gen_site.py は流していない

## 判断（メインが見る点）
- 合流：cloud-scheduled-task-min-interval（loop-and-scheduling の同名と cloud-schedules の scheduled-tasks-min-interval）、prompt-cache-default-ttl（why-prompt-caching と prompt-caching-in-practice の prompt-cache-ttl）、prompt-cache-price-multipliers（why-prompt-caching の prompt-cache-read-multiplier と同じ値）、refusals-billing-by-category（when-requests-are-refused と asking-for-reasoning の reasoning-extraction-billing。後者の具体的な値で 1 つ）
- 既存の id を使い、新しく作らなかったもの：agent-sdk-default-permission-mode → permission-mode-default-noninteractive（同じ値）、chat-sharing-file-limit → shared-chat-with-created-files-restriction（同じ値）、claude-md-on-demand-size-limit → claude-md-on-demand-char-limit（表に 200K で 40000 字がある）、artifact-storage-limit → artifacts-storage-limit
- status：提案が確認済みでも、page の write.md が「一次資料を開いていない・束の写しのまま・再確認していない」と書くものは 未確認（check-billing-path の 3 件・what-feedback-sends・usage-credits-basics・choosing-a-plan の plan-prices-individual・stateless-messages-api の message-threads-lifetime・when-requests-are-refused の 4 件・character-encodings の 2 件・before-using-top-model の top-model-by-plan・computer-use-requirements・cloud-schedules の 2.1.317 の警告）。DM1・DM3 と同じ決め方。when-requests-are-refused の 4 件と check-billing-path の 3 件は、提案の YAML が確認済み（2026-11-04）だが、担当が開き直していないので 未確認にした。不安なら、メインか検証役が一次資料で確かめて上げる
- chrome-extension-requirements は、公式同士の食い違い（Help Center は Chrome のみ・有料プラン）を `conflict` に持たせた（hc-claude-in-chrome）
- top-model-by-plan は、Fable の記事が「別の週の上限なし」と書き、usage-limit-types-by-plan の最上位のモデルの別の週の上限の列・features usage-limits の note と食い違う。本文の fact の値は Fable の記事に合わせた。正本の見直し（backlog 推奨R2）は持ち主へ。未確認のまま
- 強制力の線引き：decisions 2026-11-05 のとおり。Claude が読んで従うよう頼むだけ＝お願い（research：条件は依頼に書く／verify-skill：スキルは feature skills と同じお願い）、止める仕組みがない＝なし。verify-skill は backlog が「cc-docs-skills で確かめてから」としていたが、スキルの強制力がお願い（確認済み）であることから導いて入れた。不安なら外す
- 強制力の目印を置く担当へ：手書きの強制力の文があるページ 9 つは placement に行を立てた（btw・plugins・insights・usage・code-intelligence・workflows・research・agent-view・verify-skill）。残りの 8 機能は手書きがなく、テンプレートの tracks の先頭のバッジが出る
- 追加の補足：agents-md-plugin-id-rename は、名称の変更なので names へ移す案もある。facts には提案どおり入れた

## 強制力を入れなかった機能と理由
| 機能 | 理由 |
| --- | --- |
| settings | 管理の層は鍵、個人の層はお願いが混ざる（backlog も主を鍵と見るか確認とする） |
| scheduled-tasks | 起動を担うだけ＝なし／依頼文はお願い／保護ルール・環境は鍵の混在 |
| github-actions | 起動を担うだけ＝なし／permissions は鍵／依頼文はお願いの混在（backlog は「1 つなら なし」と推すが、混在のまま入れない） |
| subagents | 継承の仕様はなしだが、tools・permissionMode の指定は鍵で、機能の中で値が混ざる（DM3 と同じ判断） |
| bare-mode・safe-mode | backlog は bare-mode を鍵、safe-mode を なし とするが、どちらも「起動時に拡張の読み込みを止める」で同じ性質。一方だけ決めると食い違うので両方入れない。作者の判断を仰ぐ。safe-mode の提案の status は要確認 |
| incognito | 保持と管理者への見え方は止められない（鍵に近い）が、Help Center 由来で未確認。backlog も なし に留保をつける |
| browser-control（claude-in-chrome・computer-use） | Chrome 拡張のサイト許可は鍵に近く、computer use のアプリごとの許可は鍵（要確認）。値が機能の中で割れる |
| init | features に id がない（init-and-first-claude-md の機能が data にない）。足すなら features の項目から |

## 入れなかった提案
| 提案 | 理由 |
| --- | --- |
| using-research の research-model | 値が「未記入（hc-research で確かめる）」 |
| long-chat-limits の app-context-window-sizes | 値が「500K または 200K」で 1 つに決まらず、プランごとの表は再確認が要ると提案も書く |
| tool-use-loop の tool-choice-forced-support | 値が「モデルごとの表を作る」の指示で、要確認 |
| when-requests-are-refused の refusals-flagged-models・refusals-cc-display-texts | 値が「要確認」の文だけ（一覧は公式の記事・errors で取り直す） |
| cloud-schedules の scheduled-tasks-hourly-cap | 値が「確認が要る（値は未取得）」 |
| agent-view-and-background の agent-view-worktree-delete | 値が「挙動の記述」で数値でなく、提案も「features の note でもよい」とする |
| choosing-a-plan の claude-code-in-free-plan | 提案が任意で、本文に置き場がない。研究の写しのみ |
| ai-in-contests-today の 4 件（ahc058-ale-agent-result・ale-bench-ablation-gemini-2-5-pro・ale-bench-per-problem-variance・anthropic-public-ctf-2025） | 研究・大会の結果の固定の記録で、日付・研究名・対象を添えて手書きでよい（common §9・decisions 2026-11-05 の「研究の結果と変わりやすい値」、DM1 と同じ扱い） |
| backlog に文で書いた提案：cloud-sessions-and-teleport の v2.1.317（入れ子の `claude -p`）・large-context-window（窓の大きさ・単価・トークナイザーの id）・lockbox-and-holdout（月 1 回の頻度）・instructing-reviewers（数値ファイルがあれば） | 提案の YAML がなく、値と出典の id が束にない。出典が決まれば足せる |
| usage-limit-types-by-plan の見直し（top-model の別の週の上限の列） | 既存の fact の値の変更で、公式同士の食い違い。持ち主か作者の判断 |

## 注意（検証役向け）
- 未確認 23 件の値は、提案のとおりに写しただけ。確認日は提案の日付のまま（合流は新しいほうの提案のものに合わせたが、prompt-cache 系は 2026-11-05 の取得の提案）
- 確認済み 41 件の根拠は、各ページの write.md の取得の記述と提案の status（DM1・DM3 と同じ）。DM4 は事実の検証をしていない
- progress-logs-for-long-jobs と recover-lost-work の backlog にある hook-monitor-min-version・key-transcript-and-background の確認済み化は、一次資料を確かめられないので 未確認のまま（既存の項目に触れていない）
- model-prompting-tendencies の表の形（モデル × 偏りと対処）は、いまの model-quirks の表（偏りの種類 × 出方）と形が違う。置くときは置き換えか併記かを決める
- 縛りに関する手順違反の報告：facts-placement-rec.md の行の並べ替え（code-intelligence-plugins の行の移動）を 1 回、Bash の python で書いた（指示は Write・Edit だけ）。中身は自分の書いた行を動かしただけで、ほかのファイルは Bash で書いていない
