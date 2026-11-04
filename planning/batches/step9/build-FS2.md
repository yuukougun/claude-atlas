# 報告 FS2：鮮度の点検の skill の手順3・4・6・7 と外のリンクの道具（工程9）

## 足したこと

| ファイル | 中身 |
| --- | --- |
| `.claude/skills/freshness-check/SKILL.md` | 手順3・4・6・7 を足した。見出しは流れの順に 1〜9 に振り直し、設計の手順の番号を括弧に添えた（1 準備／2 読む〔設計1〕／3 照らす〔2〕／4 一覧／5 Issue の下書き〔3〕／6 直す〔4〕／7 記録を進める〔5〕／8 リンク〔6〕／9 定期〔7〕）。description・「守ること」・道具の早見も合わせた。`allowed-tools` に `Bash(uv run python tools/check_links.py *)` を足した |
| `tools/check_links.py` | 外のリンクの切れと転送を確かめる道具 |
| `tests/tools/test_check_links.py` | 21 試験（問い合わせは偽物に差し替え。実際のネットには出ない） |

skill の中身
- 5 Issue の下書き：題・影響のページと数値・当たった変更の項目・出典の URL・見立て（影響なし／読み直し／作者の承認が要る）を scratchpad に書く。「影響なし」は Issue にしない。GitHub への書き込みはメインか作者（担当は `gh` で書かない）。IT の Issue テンプレートがあれば欄の名前に合わせる、と条件付きで書いた
- 6 直す：日付・数値・名称は メインの判断＋別の担当の確かめ＋`check_all.py`。推奨・安全の既定（正本 `default-safety-settings#by-stage`）・台帳の状態が変わる更新は作者の承認が先（decisions 2026-11-03）。承認までは `checked` を進めない
- 8 リンク：`check_links.py` の使い方と状態の読み方。出典の `url` は転送先に直す
- 9 定期：手で流す前提。定期にするかは作者が決める

## 道具の使い方の例

```
uv run python tools/check_links.py --dry-run                 # 問い合わせず、対象の一覧だけ
uv run python tools/check_links.py --only-problems           # 問い合わせて、正常を除いた表を出す（工程10）
uv run python tools/check_links.py --json --interval 2 --workers 2
```

- 対象：docs/ の公開するページ（`atlas.published()`）の本文の URL（コードの中・日本語の句読点以降を除く）と、`data/sources.yml`・`sources.d/` の出典の `url`。# 以降と末尾の / の違いは同じ URL とし、使っている所（ページ／出典の id）を添える
- 状態：正常／転送（転送先と最初の転送の HTTP を出す）／切れ（4xx・5xx・接続できない・転送の先が切れている・転送が 5 回超）／要確認（401・403・429）／確かめない
- 確かめない：`.claude/settings.json` の deny の WebFetch ドメイン（`*.` 付きも）・data の `noai: true` のドメイン・`check_noai.py` の `KNOWN_NOAI`（atcoder.jp・codeforces.com）・例の URL。転送の先がこれらなら、そこで止めて「転送先は確かめない」と出す
- 作法：同じホストへ 1 秒あける（`--interval`。予約式で並列でも守る）、同時 4 本（`--workers`）、15 秒で切る（`--timeout`）、HEAD で問い合わせ HEAD を断られたとき（400・403・405・501）だけ GET で 1 回。User-Agent は `claude-atlas-link-check`。ファイルは書き換えない
- 終了コード：切れがあれば 1、読めない・引数の誤りは 2、ほかは 0

## 試験の結果

- `uv run python -m unittest discover -s tests/tools -p 'test_check_links.py'`：21 件 OK
- `uv run python -m unittest discover -s tests/tools`：687 件 OK（skipped 5）
- 本物のリポジトリでは `--dry-run` だけを流した（ネットには出ていない）：対象 573 件（問い合わせる 567 件・149 ホスト／確かめない 6 件。すべて atcoder.jp・codeforces.com 系で competition-rules ページ）。本番の実行は工程10。1 ホストに多数の URL がある（github.com など）ので、1 秒間隔だと数分から十数分かかる見込み

## メインに判断してほしいこと

1. 転送の扱い：`http→https` や末尾の / だけの転送も「転送」と出る。工程10の結果を見て、軽微な転送を分けるか決めてほしい
2. 出典の `archive` の URL（Internet Archive）は確かめていない（url だけ）。要るなら足す
3. skill の「5. Issue の下書き」は IT の Issue テンプレートの欄の名前に合わせると書いた。IT の成果と食い違うなら、メインが文言を合わせてほしい
4. 見出しの番号の振り直しで、設計 §9.4 の「少なくとも手順の1・2・5」の記述と skill の節番号が一対一でなくなった（括弧で対応は示した）。設計書の側の更新は私の担当外
5. `check_all.py` は流していない（担当の範囲外のファイルが多いため）。skill の文面に textlint などの検査が掛かるなら、メインが流してほしい

## 道具の呼び出し

約 19 回（Bash 10・Read 0・Write 3・ほか。Web・git・gh は使っていない）。
