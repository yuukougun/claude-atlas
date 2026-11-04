---
name: freshness-check
description: 教材の鮮度の点検（design §9.4 の手順の1・2・5）。前回の点検の版と日付より後の Claude Code の CHANGELOG・Help Center と Claude Platform のリリースノート・Anthropic のニュースを読み、出てくる語を tools/freshness.py で features の照合の語・tracks・aliases・数値の id・names に照らして、影響のあるページと数値の一覧を出す。直した後に checked と前回の点検の版・日付を進める。Issue にすること（手順3）と直すこと（手順4）はこの skill の外。
disable-model-invocation: true
argument-hint: "[読む範囲の指定（省略可。例：CHANGELOG だけ）]"
allowed-tools:
  - Bash(uv run python tools/freshness.py *)
  - Bash(uv run python tools/check_noai.py *)
  - WebFetch(domain:code.claude.com)
  - WebFetch(domain:raw.githubusercontent.com)
  - WebFetch(domain:github.com)
  - WebFetch(domain:support.claude.com)
  - WebFetch(domain:platform.claude.com)
  - WebFetch(domain:claude.com)
  - WebFetch(domain:www.anthropic.com)
---

# 鮮度の点検（手順の1・2・5）

Claude や Claude Code の変更が、教材のどのページと数値に影響するかを洗い出し、点検の記録を進める。変更の記録の語を機械で照らして一覧にし、読み直しと直しは次の担当に渡す。設計は `planning/design.md` §9。

## 守ること

- **この skill がするのは、読む（手順1）・照らして一覧にする（手順2）・記録を進める（手順5）だけ**。Issue にする（手順3）と直す（手順4）はしない。直しは、日付・数値・名称ならメインの判断と別の担当の検証と機械の検査で行い、教材の推奨・安全の既定・古くなった助言の台帳の状態が変わる更新は作者が承認する（decisions 2026-11-03「鮮度の更新の承認」。点検ごとにまとめて頼む）
- 資料は一次資料（下の表）だけ。**開く前に URL を `uv run python tools/check_noai.py <URL>` で確かめ**、AI の利用を断る指定があれば開かずに報告に書く。atcoder.jp・codeforces.com は開かない
- 記憶で補わない。読めなかった所は「読めなかった」と書き、読んだ範囲だけを記録に進める
- 書いてよいのは、scratchpad の写しと、道具（`tools/freshness.py`）が書くもの（`data/inspection.yml` とページの front matter の `checked`）だけ。`verified` と数値の確認日（`data/facts.yml`）は、出典を読み直した担当が書くので、ここでは書かない。ページ本文・data/ のほかの所・設定は直さない。git の commit・push はしない（メインが行う）

## 手順

### 1. 前回の点検を確かめる

```
uv run python tools/freshness.py last
```

`date`（点検の日）・`claude_code`（CHANGELOG を読んだ最後の版）・`release_notes`（リリースノートを読んだ最後の日）・`news`（ニュースを読んだ最後の日）が出る。全部 null なら初回で、読める範囲を新しいほうから読み、読んだ範囲までを記録する（読む量はメインと決める）。

### 2. 前回より後の分だけを読む（手順1）

| 資料 | URL | 読み方 |
| --- | --- | --- |
| Claude Code の CHANGELOG | `https://code.claude.com/docs/en/changelog`（版ごとに日付がある）。本文は `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`（日付はない。古い 0.2.x の日付は当てにならない） | `last` の版より後の版の項目 |
| Help Center のリリースノート | `https://support.claude.com/en/articles/12138966-release-notes` | `release_notes` の日より後の項目 |
| Claude Platform のリリースノート | `https://platform.claude.com/docs/en/release-notes/overview` | `release_notes` の日より後の項目 |
| Anthropic のニュース | `https://www.anthropic.com/news`（一覧。個別の記事は記事ごとの URL） | `news` の日より後の見出しを見て、教材の対象（Claude のアプリ・Claude Code・API・モデル・プラン・料金・利用上限・安全）に関わる記事だけ本文を読む |

- 開く URL は、上の表を `data/sources.yml` の出典（`cc-docs-changelog`・`cc-changelog`・`hc-release-notes`・`api-release-notes`）と照らして使う。転送で URL が変わっていたら、変わった先も `check_noai.py` で確かめる
- プランの改名のように、リリースノートに載らず Help Center の記事と料金のページ（`https://claude.com/pricing`）にだけ出る変更がある。リリースノートやニュースにプラン・料金・上限の話が出たら、その記事と料金のページも読む（research/22）
- 読んだ範囲を控える：CHANGELOG を読んだ最後の版（`x.y.z`）、リリースノートを読んだ最後の日、ニュースを読んだ最後の日。手順の最後の `stamp` に使う

### 3. 写して照らす（手順2）

1. 前回より後の項目を、**英語の原文のまま**、scratchpad の1つのファイル（例 `<scratchpad>/freshness-<日付>.txt`）に写す。前回より前の分、教材に関わらない版の定型の項目は写さなくてよい（ただし迷ったら写す。照らすのは機械で、写しの量は費用にならない）
2. 照らす：

```
uv run python tools/freshness.py match -f <scratchpad>/freshness-<日付>.txt
```

   JSON が要るときは `--json`。標準入力（`-`）や引数のテキストでもよい。当たりすぎる一般の語は `tools/freshness.yml` の `exclude` で外れていて、外した語で当たったものは出力の最後に「参考」として出る。この回だけ外したい語は `--exclude <語>` で足す
3. 出力の読み方：
   - **影響のあるページ**：ページの id・題・段階（stub は本文がまだないので直しは要らないが、書くときの材料に控える）と、**どの語で当たったか**（持ち主：`features:<id>` の照合の語か id、ページの `tracks`・`aliases`、`facts:<id>`、`names:<id>` の旧名・今の名前）と写しの何行目か
   - **影響のある数値**：`features/<id>`（機能の属性）・`facts/<id>`・`names/<id>` と、その数値を使うページ
4. 当たりは候補にすぎない。**写しの当たった行に戻って**、そのページの主張（数値・名前・成熟度・強制力・手順・推奨）に実際に触れる変更かを見分ける。一般の語の偶然の当たりは「影響なし」とし、毎回出るなら `exclude` に足す案を報告に書く（`tools/freshness.yml` を直すのはメイン）
5. **機械が拾えないもの**も写しから探す：照合の語のない新しい機能・コマンド・設定、名前の変更（`names` にない旧名）、モデルの退役や新モデル、利用上限・料金・プランの変更、安全に関わる既定の変更。見つけたら「照合の先がない変更」として一覧に足す（features の項目や新しいページの提案は、メインが決める）

### 4. 一覧を出す

最終の返答（報告）に、次の形で書く。ファイルには書かない。

```
## 点検の一覧（前回：版 <last の版>・<last の日> → 今回読んだ範囲：版 <Y>・<日付>）
### 影響のあるページ
| ページ id | 題 | 段階 | 当たった語（持ち主・行） | 変更の中身（原文の短い要約） | 見立て |
### 影響のある数値
| 数値 id | 当たった語 | 変更の中身 | 使うページ | 見立て |
### 照合の先がない変更
- <変更>（原文の行）：提案
### 読んだ範囲
CHANGELOG の最後の版／リリースノートの最後の日／ニュースの最後の日／読めなかった所
```

「見立て」は次の3つのどれかにして、理由を添える。

- **影響なし**：当たった行がページの主張に触れない（checked を進める候補）
- **読み直し**：ページか数値の主張に触れうる。出典を読み直す担当が要る
- **作者の承認が要る**：直すと、教材の推奨・安全の既定（正本は `default-safety-settings#by-stage`。この節に触れうる変更は必ずここに入れる）・古くなった助言の台帳の状態が変わる

一覧はここで終わり、Issue にするか・どう直すかはメインと作者が決める。

### 5. 記録を進める（手順5）

メインの判断で一覧の見立てが決まった後に行う（直しの途中では行わない）。

1. **影響がないと確かめたページ**の `checked` を進める：

```
uv run python tools/freshness.py checked <ページの id> [<id> …] --date <今日>
```

   - 対象は、一覧に出て、当たった行を読んで「影響なし」と確かめたページだけ。照合に当たらなかったページには付けない（当たらなかったことは、読んで確かめたことではない）
   - すでに同じか新しい日付なら変えない。ページがない id は報告に出る。`checked` は `verified` があるページの期限の起点にだけ効く（draft は数値の分で計算する。design §9.2）
2. **出典を読み直したページと数値**の `verified` と数値の確認日は、読み直した担当が書く。ここでは進めない。
3. **前回の点検の版と日付**を書く（読んだ範囲までを書く。読めなかった資料の日付は進めない）：

```
uv run python tools/freshness.py stamp --version <CHANGELOG を読んだ最後の版> --date <今日> \
  --release-notes-date <リリースノートを読んだ最後の日> --news-date <ニュースを読んだ最後の日> [--note "<注>"]
```

   - `--release-notes-date`・`--news-date` を省くと `--date` になる。読んだ最後の日がそれより前なら必ず指定する
   - 記録より古い版・日付は断られる（直すときだけ `--force`）
4. 書いたファイル（`data/inspection.yml` と `checked` を進めたページ）を報告に並べる。`checked` は期限の日（生成物の data 属性）に影響するので、**メインが `uv run python tools/gen_site.py` と `tools/check_all.py` を流して commit する**

## 道具の早見

| 道具 | 何をするか |
| --- | --- |
| `freshness.py last [--json]` | 前回の点検の版と日付を出す |
| `freshness.py match <テキスト> / -f FILE / -  [--exclude 語] [--json]` | 写しの語を照合の先に照らして一覧を出す |
| `freshness.py stamp --version X.Y.Z --date D [--release-notes-date D] [--news-date D] [--note 文] [--force]` | `data/inspection.yml` に書く |
| `freshness.py checked <id>… --date D` | ページの front matter の `checked` を進める |
| `check_noai.py <URL>` | 資料を開く前に、AI の利用を断る指定を確かめる |
