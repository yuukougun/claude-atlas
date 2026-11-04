# write.md：forgot-after-compaction

## 書いたファイル
- docs/symptoms/forgot-after-compaction.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に 11 件、sections に forms・examples・prevention を足した。anchor diagnosis は不変）
- snippets/forgot-after-compaction/list-known-promises.txt と .expect.yaml（圧縮の直後に、見えている約束と置き場所を挙げさせる依頼。目次の templates は「なし」で、診断の手段として足した）
- data/sources.d は書いていない（使った出典は data/sources.yml にすべてある）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順）：#diagnosis（6 項目。散らかっている 1〜4、縛っていない 5、版 6。人の側の落とし穴は節末の 1 段落で six-causes#diagnosis を指す）
- 原因ごとの振り分け先（routes）：#diagnosis 内の routes の目印（front matter の routes から生成）
- 構成の目安：要点（冒頭）→ #forms → #diagnosis → routes → #examples → #prevention
- 対処の本体は書かず、各分野のページへの link で指した

## メインに判断してほしいこと
- 診断の 6 項目目（版）は、圧縮まわりの不具合が更新履歴で直った旨だけを書き、版の数値は本文に出していない。入った版（v2.1.317 など）を目印で示すなら、数値ファイルへの追加が要る（下の提案）
- アプリと API は「未確認」と 1 文で書いた（束に材料がないため）。タブにしていない
- 「人の側の落とし穴」は、診断の節末で six-causes を指すだけにした

## 提案
```yaml
proposals:
  - fact: {id: compaction-bugfix-min-version, title: 圧縮の後の "Prompt is too long" と要約の取りこぼしを直した版, value: v2.1.317, sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [forgot-after-compaction#diagnosis]
```
（根拠は束 6.5。本文には目印をまだ置いていない。採用するなら診断の 6 項目目に目印を足す）

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告は 4 件から 1 件に減った
- 残した警告 1 件：132 行の no-doubled-joshi（助詞「に」）。link の目印の間に道具が題名を入れた後の文で出る。前後の文は直したので、題名由来の誤検出と見る

## 確かめていないこと
- 診断 1 の「圧縮の直後に Claude に約束を挙げさせる」は観察の手段で、返答が正確かは試していない（雛形は未実行）
- アプリと API の圧縮の挙動
- 判断例 2（進捗ファイルで手順の段を持たせる）は、束の材料からの推論で、実際に手順が飛ぶ例を再現していない
- GitHub の 3 件の Issue は題名のみ（束のとおり。本文・修正状況は未検証）
- 版 6 の「更新履歴に出ている」は束の 6.5 に基づく。CHANGELOG の原文は開いていない

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0
