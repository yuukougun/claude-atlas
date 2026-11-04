# 見せ方の一覧（注釈付きのセッション記録・検証ノート・Before/After）

- 版：2026-11-04 第1版（工程7の始め。design §6.10・DR-17）
- どのページで何を見せるかの一覧。目次の notes に担当が書いた「見せ方」と、工程6までの報告（fix-F1・F3・F5 の「見せ方」）を材料にした
- 繰り返して確かめる検証ノートは数件に限る（decisions 2026-11-03「検証ノートの実験」）。試せない確かめは作者に頼む（工程7の終わりにまとめて）

## 1. 試作のページ（工程7）

| ページ | 見せ方 | 中身 |
| --- | --- | --- |
| keep-replies-in-japanese | 検証ノート（繰り返す） | 英語への回帰を数える（language の設定の有無・ツールの直後の一言）。制作の環境で、少ない試行と数件の繰り返し |
| writing-skills | 検証ノート | スキルの有り無しを新しいセッションで比べる（description が呼ばれる条件） |
| agreement-is-not-evidence | Before/After | 同意を根拠にした頼み方と、反論を求める頼み方の返答の違い（例は架空の題材） |
| four-specifics | Before/After | 4つを書かない頼み方と書いた頼み方の違い |
| instructions-ignored | なし（振り分けが本体） | 診断の節は routes から振り分ける |
| request-vs-lock・claude-md-vs-rules-skills-styles・competition-rules・outdated-advice-ledger・how-to-use | 図か表だけ | 目次の visual のとおり |

## 2. 第一波以降の候補（工程8で割り当てる）

- 検証ノート：keep-replies-in-japanese#measure、commit-and-comment-language#verify-note、documents-in-japanese#pdf、suspected-degradation#measure（版と effort を記録して同じ課題を比べる）、thinking-keywords（「よく考えて」と書いても effort が上がらないこと）
- Before/After：prompting の全ページ（ファイルの notes の方針）、before-after-prompts・rewind-dont-correct・long-context-first、ask-without-sycophancy、retros-without-ai-verdicts
- 注釈付きのセッション記録（制作の記録から）：handoff-documents・progress-files（上限や区切りで止まって再開した例）、promises-after-compaction（圧縮を越えて約束を残す例）、lock-side-effects（hooks が止めた例と見直し。state/blocks.log）、independent-review（検証の指摘と直しの前後）
