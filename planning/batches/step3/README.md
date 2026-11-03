# 工程3（設計）のバッチ

設計書（[../../design.md](../../design.md)）の第1版はメインが書いた。ここでは、目次（catalog）を担当に分けて作る。規則は [../../catalog/README.md](../../catalog/README.md)、語彙は `schema/site.yml`。

- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す
- 担当が書くのは割り当てたファイルと自分の報告だけ。共有のファイル（registry・features・設計書）への変更は、報告に「提案」として書く

## 1段目：一覧と検査の道具（並列）

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| C0 | `planning/catalog/registry.yaml`（全候補の id・分野・題名・優先度・レベルの見当・出どころ、台帳の項目の id） | `registry-C0.md` | 完了（候補378：必須164・推奨161・任意53。台帳35。核の候補47） |
| T1 | `tools/check_catalog.py` と `tests/tools/test_check_catalog.py` | `tool-T1.md` | 完了（検査31：エラー10・警告21。試験114が通る） |

## 2段目：分野ごとの目次（一覧ができてから、並列）

共通の指示は [brief-catalog.md](brief-catalog.md)。1つの担当が22〜39ページほどになるよう分けた。symptoms はほかのすべての分野へ振り分けるので、1つの担当にした。

| 担当 | 分野（registry の候補数） | 報告 | 状態 |
| --- | --- | --- | --- |
| C1 | start（8）・changes（5）・basics（20） | `catalog-C1.md` | 完了（start 10・changes 4・basics 20） |
| C2 | surfaces（11）・models（14）・cost（12） | `catalog-C2.md` | 完了（surfaces 6・models 11・cost 11） |
| C3 | prompting（24）・japanese（12） | `catalog-C3.md` | 完了（prompting 24・japanese 11） |
| C4 | context（19）・cli（19） | `catalog-C4.md` | 完了（context 15・cli 19） |
| C5 | app（22）・api（14） | `catalog-C5.md` | 完了（app 20・api 11） |
| C6 | extend（26） | `catalog-C6.md` | 完了（extend 24） |
| C7 | enforce（15）・safety（17） | `catalog-C7.md` | 完了（enforce 15・safety 18） |
| C8 | verify（17）・eval（13） | `catalog-C8.md` | 完了（verify 17・eval 13） |
| C9 | delegate（23）・team（16） | `catalog-C9.md` | 完了（delegate 22・team 16） |
| C10 | judgment（11）・contest（12） | `catalog-C10.md` | 完了（judgment 11・contest 9） |
| C11 | recipes（22） | `catalog-C11.md` | 完了（recipes 21） |
| C12 | symptoms（26） | `catalog-C12.md` | 完了（symptoms 33） |

2段目の結果：361ページ（必須174・推奨150・任意37）。registry の378候補は、採る346・まとめた31・採らない1。メインが、ほかの分野で消えた id を指していた4か所を直し、eval の2ページ（test-the-verifier・experiment-log）に `wave: 1` を付けた。検査はエラー0・警告6（比例則）。

## 3段目：提案の統合（2段目の後、並列）

共通の指示は [brief-integrate.md](brief-integrate.md)。材料は [open-issues.md](open-issues.md)（担当の open_issues 165件の全文と振り分け）と、`catalog-C12.md` §7 の逆引きの表。担当ごとの抜き出しは `state/step3-integrate/<担当>-input.md`（追跡しない。open-issues.md から作り直せる）。分野ごとに持ち主を1人に決め、同じファイルを2人が書かないようにした。メインは先に、機能の id の一覧（`features.yaml`）を置き、台帳に2項目を足した。

| 担当 | 受け持ちの分野 | 報告 | 状態 |
| --- | --- | --- | --- |
| I1 | start・changes・basics・judgment | `integrate-I1.md` | 完了（25ページを直した。メインへ3） |
| I2 | surfaces・models・cost・api・app | `integrate-I2.md` | 完了（25ページ。メインへ4） |
| I3 | prompting・japanese・context | `integrate-I3.md` | 完了（21ページ。メインへ2） |
| I4 | cli・extend・contest | `integrate-I4.md` | 完了（メインへ3） |
| I5 | verify・eval・enforce | `integrate-I5.md` | 完了（メインへ2） |
| I6 | safety・delegate・team | `integrate-I6.md` | 完了（31ページ。メインへ6） |
| I7 | symptoms・recipes | `integrate-I7.md` | 完了（symptoms 20・recipes 5ページ。メインへ3） |

メインが扱うもの（open-issues.md の「メイン」の印）：設計書への反映（境界の表・横断のページ・数値ファイルの表・生成のページ）、用語の仮の決定を工程5で確かめること、作者に確かめてもらう候補の一覧、kyopro-atlas の書き方との食い違いの報告。

3段目の結果：検査はエラー0・警告4（比例則。どれも notes に理由がある）。症状のページの sign と同じ文（記号と空白を除いて同じ）が対処のページにあるものは0件になった。題名は M1 の表で揃えた。メインへの事項は計23件で、対応は工程4の design-review.md に書く。

### 統合の担当がメインに上げた点への対応（2026-11-04）

| 点 | 対応 |
| --- | --- |
| 症状の原因別の表を生成する（I1-1） | 設計書 §8.3 の作る層に足した |
| 逆引きの重複・推移的な前提を検査する（I1-2・I4-2・I7-1） | 設計書 §8.6 に足した。目次の検査（check_catalog.py）にも警告として足す（担当 T2）。見つかったものは工程4の直しで外す |
| 用語集と用語索引の id（I1-3） | 入れ替えた（用語集 glossary、用語索引 term-index） |
| 言い換えの重なり（I2-1・I5-2・I6-1） | catalog/README §4.5 の4に規則を足した（言い換えも重ねない。対処のページはより狭い場面か goal の形）。似た組（9組）は工程4の直しで扱う |
| 題名のモデルの系統名（I2-2） | 「最上位のモデルを使う前に」（id は before-using-top-model）。Fable は aliases |
| 表にない語の表記（I2-3・I4-3・I6-5） | 用語集（glossary）の notes に足した。用語集を書くときに公式の多数派を確かめて決める |
| API の読者の入口（I2-4） | 設計書 §7 の面別の一覧で受ける。いまは変えない |
| 出力スタイルの置き場所（I4-1） | 設計書 §4.2 に行を足した |
| plugin-eval・refusals の note（I5-1・I6-2・I7-3） | features.yaml に足した。自動のモデルの切り替えの設定は refusals で追う |
| 「手動のモードで始める」を安全の既定に足すか（I6-3） | 足さない（安全の既定の変更は作者の承認が要る。いまの既定で足りる） |
| 安全の既定の点検の目印（I6-4） | 設計書 §9.4 に正本の節を名指しした |
| memory-faq と how-memory-works（I6-6） | 工程4の見直しで扱う |
| 第一波の症状のページから、第一波でない対処のページへの道（I7-2） | 工程5でユーザーに確かめる。いまの規則では、症状のページの関連437件のうち213件が第一波の外を指す。症状ごとに中心の対処1ページを足すと第一波は158ページ、2ページなら191ページ |
