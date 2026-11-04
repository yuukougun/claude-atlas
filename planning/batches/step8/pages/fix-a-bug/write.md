# fix-a-bug 執筆の報告

## 書いたファイル
- docs/recipes/fix-a-bug.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 11 件に。sections に guards-first・flow・verify-the-fix を足した。既存 4 節の anchor は変えず）
- snippets/fix-a-bug/ に 4 つ：reproduce-request・hypothesis-request（A-10。本文では Before/After の折りたたみと併用）・no-symptom-patches・restart-request（それぞれ .txt と .expect.yaml）
- 出典はすべて既存の id なので data/sources.d/fix-a-bug.yml は作っていない

## 必ず持つものの対応
- 手順：reproduce-and-define-done（再現と完了の定義、縮小）・hypotheses-before-fixes（仮説と反証）・no-symptom-patches（最小の修正）。全体は flow（図と各段の終わりの印の表）
- 確かめる・縛るのページへの道：guards-first（define-done・evidence-not-reports・protect-tests を link）。前提は evidence-not-reports、関連は front matter の related
- 構成の目安：要点 → guards-first → flow・各手順 → verify-the-fix（確かめ方）→ when-stuck（失敗したとき。症状ページ 4 つへの表）
- level を持つ：整える（front matter のまま）

## メインに判断してほしいこと
- 「checkpoints-and-rewind」を related にない状態で本文から link した（when-stuck と guards-first）。related への追加が要るか
- when-stuck の症状への表は手書き（このページの routes が空のため）。routes に入れるなら front matter の提案が要る

## 提案
- 特になし（数値の提案はなし。研究の割合は書かず、変わりやすい値は本文に書いていない）

## 検査の結果
- 1 回目：エラー 1（hook の表記 → フックに直した）・警告 6
- 修正後：エラー 0・警告 2。残りは no-doubled-joshi 2 件（53 行と 155 行）で、文を直して消したつもりだが、2 回目の検査は決まりの回数を使い切ったので再実行していない。メインの検査で確認を

## 確かめていないこと
- 最後の直しの後の check_page の結果（上のとおり未実行）
- Defects4J の研究の数値（束が未確認とするので書かなかった）。ReduceFix の対象モデルは束に書かれておらず、「Claude とは限らない」と書いた
- アプリでは再現のコマンドを実行できない場面がある、という書き方の裏取り（束にない。「実行できる道具がない会話では」と条件つきにした）
- 公式の best practices の「修正が重ねて失敗したら新しく始める」は束の写しによる。原典は開いていない
- checkpoints-and-rewind の戻せる範囲の細部は、そのページに任せ、本文では「Bash だけが変えたファイルは戻らない場合がある」とだけ書いた
- 雛形 4 つの動作は未確認

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 0 回
