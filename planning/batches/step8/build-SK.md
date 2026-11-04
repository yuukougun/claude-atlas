# 報告 SK：鮮度の点検の skill（工程8。design §9.4 の手順の1・2・5）

## 作ったもの

| ファイル | 中身 |
| --- | --- |
| `tools/freshness.py` | `last`・`match`・`stamp`・`checked`（読む層 tools/lib を使う。`--root` で根を替えられる） |
| `tools/freshness.yml` | match の設定：`exclude`（当たりすぎる一般の語。goal・fork・mod・research・workflow など22語）と `min_length`（英数字の語の最短、3） |
| `tests/tools/test_freshness.py` | 27 試験（一時フォルダの小さなサイト。fixtures は gen の site.yml を写すだけ） |
| `.claude/skills/freshness-check/SKILL.md` | 手順1・2・5 の skill（`disable-model-invocation: true`。kyopro-atlas の record-problem の frontmatter に合わせた） |

data/inspection.yml と schema/inspection.schema.json は既にあり（`last`: date・claude_code・release_notes・news・note）、形が足りたので、**schema/keys.yml と data/freshness.yml は触っていない**（make_schema.py --check は「最新」）。

## 使い方の例

```
uv run python tools/freshness.py last
uv run python tools/freshness.py match -f <scratchpad>/freshness-2026-11-10.txt     # 影響のあるページと数値、当たった語（持ち主・行）
uv run python tools/freshness.py checked what-survives-compaction choosing-a-plan --date 2026-11-10
uv run python tools/freshness.py stamp --version 2.1.330 --date 2026-11-10 --release-notes-date 2026-11-08 --news-date 2026-11-09
```

match の照合の先：features の match_terms と id（主のページ＋tracks で指すページ）／ページの tracks（features にない id）と aliases／facts の id（本文の fact の目印を持つページ）／names の旧名・今の名前・id（name の目印を持つページ＋その機能のページ）。数値は `features/<id>`・`facts/<id>`・`names/<id>` で出す。英語は大文字小文字・複数形（-s/-es）・「-」「_」空白の違いを吸収し、前後が英数字なら当てない。除外した語で当たったものは、最後に「参考」として出す。本物のリポジトリで実行して、2016 語を照らせることを確かめた（本物の data は読んだだけ。何も書いていない）。

stamp は、release_notes・news の日が既定で --date。記録より古い版・日付は断る（--force で書く）。注は残る。checked は front matter の閉じる `---` の前に足すか、既存の行を替える。すでに同じか新しい日付なら変えない。verified には触れない。

## 試験の結果

- `uv run python -m unittest discover -s tests/tools -p 'test_freshness.py'`：27 件 OK
- `uv run python -m unittest discover -s tests/tools`：666 件 OK（skipped 5）。1回目に 2 件の失敗が出たが、再実行で消えた（その間に別の担当が data/facts.yml を直していたため、と考える。私の変更に関わる失敗ではない）
- `uv run python tools/make_schema.py --check`：すべて最新

## メインに判断してほしいこと

1. **除外の語の初期値**（tools/freshness.yml）は、features の match_terms を見て選んだ一般の語。点検を一度流して、うるさい語を足す・消す。「skills」「hooks」「plugins」のような機能の名前そのものは外していない（CHANGELOG のほぼ毎版に出て、一覧が長くなる見込み。そのときは exclude に足すか、持ち主ごとに見る）
2. **tools/freshness.yml を新しく置いた**（指示の「書いてよいファイル」に明記がなかった）。除外の語を data/inspection.yml に入れる案は、schema が additionalProperties: false で keys.yml の変更が要るので避けた。置き場所を変えるなら言ってほしい
3. **checked を進める対象**：skill では「一覧に出て、当たった行を読んで影響なしと確かめたページ」だけにした（照合に当たらなかったページには付けない。読んで確かめたことではないため）。照合に当たらないページの期限は verified で決まる。広く付ける方針なら変えてほしい。なお `checked` は verified があるページの期限の起点にだけ効く（model.expiry）。draft は数値の分で決まる
4. **Anthropic のニュースの一覧 URL**（https://www.anthropic.com/news）は data/sources.yml に項目がなく、www.anthropic.com のドメインの noai 確認（2026-11-04、noai: false）だけがある。skill はこの URL を使い、開く前に check_noai.py をかける手順にした。出典の項目に足すか決めてほしい
5. **gen_site.py の再生成**：checked は期限の日（data 属性）に影響するはずなので、skill は「書いた後にメインが gen_site.py と check_all.py を流す」と書いた。実際に生成物が変わるかは、実際の点検まで確かめていない
6. 手順3（Issue）と4（直し）は skill に入れていない。見立ての分類（影響なし・読み直し・作者の承認が要る）と、安全の既定の正本 `default-safety-settings#by-stage` に触れうる変更は必ず「承認が要る」に入れる指示だけ書いた
7. `check_all.py` を1回流した：11 通過、gen_site（--check。nav.yml と docs/assets/data/pages.json が古い。ほかの担当のページ追加による生成物のずれで、私の変更には関わらない）と tests-tools が失敗。tests-tools は私の流した直後の全体では OK で、同時に別の担当が data/ とページを直している間の一時的な失敗と考える。メインがバッチの終わりに gen_site.py を流す際に再確認してほしい

## 道具の呼び出しの数

約 30 回（読み 12・書き 6・実行 12 ほど）。
