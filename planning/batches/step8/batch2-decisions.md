# バッチ2：メインが決めること

先例（rules.md）に当たらないものだけ。推す案を先に書く。

| ページ｜件｜案 |
| --- |
| product-map｜`#identify-surface` の見分けの手がかり4項目と旧称3件の手書き（一次資料で未確認）｜事実の検証役に回す。旧称は手書きでよい（過去の固定の名）。確かめられない項目は削る |
| roadmap｜表の最右列の割り当てが持ち主のページと合うか／根拠の印の付け方｜持ち主のページが書けた後に、検証役が突き合わせる。図（はしご）は表が代えるので作らない |
| knowledge-map｜`#how-to-read` の2つの表示（分野・祖先と子孫）が JS の実装と合うか｜実装を確かめる担当を立てる。違えば本文を直す（backlog にも記載） |
| rereads-whole-history｜公式の対話型の図へのリンクの URL が未確認。判断例が when-to-start-fresh と重なる｜URL を検証役が確かめて足す。判断例は残す |
| subagent-isolation・where-instructions-sit・when-to-lock ほか｜面タブを置かなかった（材料に API・アプリの手段がない）｜置かないまま公開。調べる担当が出れば足す |
| knowledge-cutoff｜Claude Code タブ「日付を渡しているかは確かめていない」を調べる担当／`#what-helps` の「が」の警告｜調べる担当を立てる。警告は下書きでは止めない |
| rewind-dont-correct・choose-what-to-read・state-the-scope｜アプリの編集・添付・範囲を縛る手段が未確認のまま「画面で確かめる／未確認」と書いてある｜公式のヘルプで調べる担当を1つ立て、まとめて埋める。それまでは未確認のまま |
| suspected-degradation｜`#postmortem-example` の表を本文に直接書いてよいか（日付とモデル名の固定の記録）／ポストモーテムを用語集に入れるか｜固定の記録として直接書いてよい（「API は含まれない」は原文で確認済み）。ただし症状のページに入った要旨なので、縮めるかは作者が判断 |
| working-with-git｜「慣れた」の目安（辞典の案）／auto モードが止める git 操作を確認日付きで書いた｜目安は「辞典の目安」と明記されているので残す。auto モードの記述は日付つきの現行の記述。外すかは作者が判断 |
| claude-md-length｜「月1回の棚卸し」「681行（自己申告）」「約2.5k トークン（二次要約）」を根拠：弱で載せる程度／削除した文を戻す条件｜根拠：弱の印付きなので残す。戻すのは memory の文書で確かめた後 |
| independent-review｜claude.dev ブログの原文1文を引用／`#who` の表の「責任を持つか」列は出典なしの整理｜短い引用は他者の引用として残す。列は「本ページの整理」と明記して残す |
| verifier-defines-problem・felt-vs-measured・test-the-verifier｜構成の目安から外れた節の追加（`#why`・`#misconceptions`・`#map`・`what-you-keep`）／判断例が架空｜追加は残す。`#map` は hub と重なるなら後で削る |
| measure-changes｜95%区間の式・勝率の検算（research/24 B-53）と架空の数字の表／task 数「数個〜20個」を推論と明記｜検算は検証役が1度確かめる。架空の表は「架空」と明記してあるので残す |
| selection-pressure｜報道1本・原典未確認の「53件中16件」を根拠：弱で本文に置いた／「4〜5回」を本文の手書きにした｜16件は削る（原典がない）。4〜5回は backlog の fact 化で目印に替える |
| what-auto-mode-stops・protect-tests｜誤検知率0.4%・見逃し率17%・5.7% などを研究の結果として手書き（記事の日付・n を添えた）／「強制力」を手書き｜研究の結果の先例どおり手書きでよい。強制力は backlog の「enforcement の属性」の判断を待つ |
| prompt-injection-in-practice｜Invariant Labs・Check Point の事例を会社名つきで載せた（方針 B1）／WhatsApp 事例の「確認画面に一部しか見えない形」は隠し方に触れる｜会社名つきは残す。「確認画面」の細部は攻撃の手口に当たるので削る |
| default-safety-settings｜`#by-stage` は教材の推奨で、安全の既定の変更に当たる（決定 2026-11-03 のとおり書いた）／組み合わせ方を独立の節にするか｜決定のとおり書いてあるので作者の承認を取って出す。独立の節は不要 |
| where-your-data-goes｜プラン名を書かず「個人向け／商用」にした／学校のアカウントは未確認／名前の目印の使い方｜書かないまま。学校は未確認のまま。プラン名は names の目印で書く案を決める |

## メインの決め（2026-11-05）

直す（TR3 がバッチ3の分と一緒に当てる）：

1. product-map：旧称3件は、data/facts.yml の names に項目があれば名前の目印（card §9）で書く。なければ手書きのまま。見分けの手がかり4項目は、束の材料に基づくなら残し、束にもない知識なら rules.md の「束にない知識」として扱う
2. knowledge-map：`#how-to-read` の2つの表示（分野・祖先と子孫）を、サイトの JavaScript（overrides/ の下）の実装と突き合わせ、違えば本文を直す
3. rereads-whole-history：公式の対話型の図への URL を1回開いて確かめる。確かめられなければリンクを外す
4. independent-review：ブログの原文の1文の引用を、自分の言葉の言い換えにする（common §11「ほかの記事の文を転載しない」）
5. measure-changes：95% 区間の式と勝率の検算を、計算で確かめる（Web は使わない）。誤りがあれば直す
6. selection-pressure：「53件中16件」は削る。「4〜5回」は数字を書かない言い方にし、数値の提案として backlog に回す
7. what-auto-mode-stops・protect-tests：手書きの「強制力」を、data に項目があれば feature の目印に替える。なければ backlog の「enforcement の属性」に回す。研究の結果の割合は手書きのままでよい
8. prompt-injection-in-practice：WhatsApp の事例の「確認画面に一部しか見えない形」など、隠し方の細部を削る（会社名つきの事例は残す）

そのまま（直さない）：roadmap（持ち主のページとの突き合わせは第一波の後）・面のタブを置かなかったページ・knowledge-cutoff・アプリの手段が未確認のページ（調べるのは backlog）・suspected-degradation（固定の記録。ポストモーテムは用語集の backlog へ）・working-with-git・claude-md-length・independent-review の表の列・構成の目安から外れた節・measure-changes の架空の表・where-your-data-goes。default-safety-settings は、2026-11-03 の「安全の既定の勧め方」の決めのとおりに書いてあれば、追加の承認は要らない（作者の承認が要るのは、既定を変える更新だけ。decisions「鮮度の更新の承認」）
