---
id: character-encodings
title: 文字コード（Shift_JIS の CSV など）
aliases: [Shift_JIS, CP932, 文字化け, UTF-8 に変換する]
type: recipe
field: japanese
chapter: 資料と環境
order: 100
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない]
scenes: [データ分析, 開発]
summary: Shift_JIS などで保存されたファイルは文字化けや集計の空欄の元になるので、UTF-8 に変えてから渡すか、文字コードを伝えて読ませる。Claude Code の編集の道具がそうしたファイルを拒むこともある。
signs:
  - {type: symptom, text: CSV を集計させたら、日本語の列が空欄や文字化けになった}
  - {type: symptom, text: Shift_JIS のファイルを編集させようとしたら断られた}
  - {type: situation, text: Excel や古い業務システムが書き出したファイルを渡す}
prerequisites: []
related: [files-and-code-execution, how-attachments-are-read, data-analysis, office-paperwork, documents-in-japanese, windows-wsl-ime]
sources: [cc-changelog]
volatility: 中
sections:
  - {title: 渡す前に文字コードを確かめる, anchor: check}
  - {title: UTF-8 に変えてから渡す, anchor: convert}
  - {title: Claude Code の編集の道具と文字コード, anchor: claude-code}
  - {title: 全体の確かめ方, anchor: verify}
  - {title: うまくいかないとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Shift_JIS などの CSV は UTF-8 の複製にしてから渡し、日本語の列が空欄や文字化けになるのを防ぐ。
    - **いつ引くか**：CSV を集計させたら日本語の列が空欄や文字化けになったとき、Shift_JIS のファイルの編集を断られたとき、Excel や古い業務システムが書き出したファイルを渡すとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：Shift_JIS・CP932・文字化け・UTF-8 に変換する
<!-- textlint-enable -->

文字コード（文字をバイトに直す約束）が合わないファイルは、Claude が読んでも日本語が崩れる。このページは、Shift_JIS 系のファイルを UTF-8 の複製にして渡す手順と、Claude Code の編集の道具がそうしたファイルを拒む場合の進め方をまとめる。

## 渡す前に文字コードを確かめる {#check}

文字コードの不一致は、集計や編集を頼む前に見つけると安い。空欄が出てから探すと、原因が文字コードだとは気づきにくいからである。

読めない状態の見分け方は次のとおりである。

- 日本語の列が空欄になる、または `繝` `縺` のような見慣れない漢字が並ぶ。
- 日本語のあるはずの所に `�`（置換文字）が出る。
- 先頭の列名だけ読めず、頭に見えない文字が付く。UTF-8 の BOM（先頭の印）が原因のことが多い。

渡す前に、ターミナルで次の 3 つを確かめる。

1. `iconv -f UTF-8 -t UTF-8 ファイル名 > /dev/null` が成功すれば、UTF-8 として読める。失敗すれば、UTF-8 ではない。
2. 失敗したら `iconv -f CP932 -t UTF-8 ファイル名 | head` で先頭の数行を読み、日本語が読めるかを目で見る。
3. `head -c 3 ファイル名 | xxd` で先頭が `efbbbf` なら BOM 付きの UTF-8 である。

`nkf --guess` や `uchardet` のような判定の道具も使える。ただし判定は推測なので、決め手にせず、変換した結果を目で見て決める。Shift_JIS と書かれていても、Windows の日本語環境が書き出すのは Shift_JIS の拡張である CP932 であることが多い。丸付き数字や機種依存の文字は、CP932 でないと変換で落ちる。書き出した側の設定で変わるので、古い業務システムのファイルは、まず CP932 で試す。

この確かめは、データの裏取りの一部でもある。集計の結果が正しいかは <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](../recipes/data-analysis.md#check-raw-data)<!-- link:end --> で確かめる。ここでは、読み込みの段で壊れていないかだけを先に見る。

## UTF-8 に変えてから渡す {#convert}

原本は変えず、UTF-8 の複製を作って渡すのが基本である。原本を上書きすると、取り込み先のシステムが読めなくなったときに戻せない。

変換は Claude に頼まずに自分で行ってもよい。頼むなら、変換後の確かめまで依頼に入れる。次の依頼は、複製を作らせ、行数と先頭の行を見せさせ、読めたときだけ集計を始めさせる。

<!-- gen:begin snippet character-encodings/convert-prompt -->
<!-- textlint-disable -->

??? example "雛形：複製を作ってから集計させる依頼"

    ```markdown
    添付した `sales.csv` は、Shift_JIS 系（CP932）で保存されている可能性が高い。集計の前に、次の順で進めてほしい。

    1. 原本は変えない。`iconv` で UTF-8 の複製 `sales.utf8.csv` を作る。
    2. 複製の行数が原本と同じか、先頭の 3 行で日本語の列名が読めるかを見せる。
    3. 読めなかったら集計に進まず、文字コードを変えて（EUC-JP など）やり直す。
    4. 読めたら `sales.utf8.csv` で月別の売上を集計する。列ごとの空欄の数も添える。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet character-encodings/convert-prompt -->

自分で行うときは、次のスクリプトが使える。失敗した変換の出力は残らない。

<!-- gen:begin snippet character-encodings/to-utf8 -->
<!-- textlint-disable -->

??? example "雛形：UTF-8 の複製を作って行数を突き合わせるスクリプト"

    ```bash
    #!/usr/bin/env bash
    # 原本は変えず、UTF-8 の複製を作って、行数を突き合わせる
    # 使い方：./to-utf8.sh 入力.csv 出力.csv [元の文字コード（既定は CP932）]
    set -euo pipefail

    src="${1:?入力のファイルを指定する}"
    dst="${2:?出力のファイルを指定する}"
    from="${3:-CP932}"

    # 変換に失敗したときに、途中までの出力を残さない
    tmp="$(mktemp)"
    trap 'rm -f "$tmp"' EXIT
    iconv -f "$from" -t UTF-8 "$src" > "$tmp"
    mv "$tmp" "$dst"
    trap - EXIT

    # 行数が同じか（文字コードを変えても行は増減しない）
    echo "行数：入力 $(wc -l < "$src")、出力 $(wc -l < "$dst")"

    # 日本語が読めるかを、先頭の数行で目で確かめる
    head -n 3 "$dst"
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet character-encodings/to-utf8 -->

面ごとの違いは次のとおりである。

=== "アプリ"

    - 変換した UTF-8 の CSV を添付する。添付の読まれ方は <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](../app/how-attachments-are-read.md#pdf-and-others)<!-- link:end --> にある。
    - 変換していない CSV を渡すときは、コード実行を有効にして、文字コードを伝えて読ませる。たとえば「CP932 として読み込んで」と頼む。コード実行の頼み方は <!-- link:begin files-and-code-execution#usage -->[ファイル作成とコード実行 › 頼み方](../app/files-and-code-execution.md#usage)<!-- link:end --> を引く。
    - アプリが添付の文字コードを自動で判定するかは、このページでは確かめていない。判定に頼らず、文字コードを伝えるか、変換してから渡す。

=== "Claude Code"

    - 作業のフォルダに原本を置き、`iconv` で複製を作らせる。複製は Bash の道具で作るので、編集の道具が拒む場合でも進められる。
    - 複製を作ったら、行数と先頭の行を見せさせる。読めたことを確かめてから、集計や編集を頼む。
    - Windows のシェルで出力が化けるときは、この変換の話ではない。<!-- link:begin windows-wsl-ime#mojibake -->Windows・WSL・IME で困ったら<!-- link:end --> を引く。

## Claude Code の編集の道具と文字コード {#claude-code}

Claude Code の編集の道具（Edit と Write）は、UTF-8 でないファイルを扱うのが苦手である。変更の記録で 2026-11-03 に確かめた経緯は次のとおりである。Shift_JIS・Windows-1252・GBK のファイルを Edit で直すと、非 ASCII の文字が置き換わる不具合があった。その修正として、新しい版の Edit（拒むようになった版：<!-- fact:begin edit-refuses-non-utf8-since -->Claude Code 2.1.296（2026-11-06 時点）<!-- fact:end -->）はそうした編集を拒む。Write も、Shift_JIS などのファイルを黙って UTF-8 に変えず、拒む（拒むようになった版：<!-- fact:begin write-refuses-non-utf8-since -->Claude Code 2.1.299（2026-11-06 時点）<!-- fact:end -->）。拒む版かどうかは、使っている版を変更の記録と突き合わせて確かめる。版の見つけ方は <!-- link:begin windows-wsl-ime#version -->Windows・WSL・IME で困ったら<!-- link:end --> にある。

拒まれたときの進め方は、複製を作ることである。

!!! example "判断例：Shift_JIS のファイルの編集を断られたとき"
    - **状況**：古い業務システムが読み込む CP932 の CSV を、Claude Code で直させようとしたら、編集を断られた。
    - **迷う候補**：原本を UTF-8 に変換して上書きする。または、UTF-8 の複製を直させて、最後に CP932 へ戻す。
    - **選んだもの**：UTF-8 の複製を直させて、最後に CP932 へ戻す。
    - **理由**：取り込み先のシステムが CP932 しか読めないなら、原本を UTF-8 にすると取り込めなくなるからである。戻すときは、`iconv -f UTF-8 -t CP932` が CP932 にない文字でエラーになる。そこで止まれば、直した内容に入れてはいけない文字が分かる。

手順は次のとおりである。

1. 原本から UTF-8 の複製を作る（`iconv -f CP932 -t UTF-8` など。スクリプトの例は「UTF-8 に変えてから渡す」の節にある）。
2. 複製を Claude Code に直させる。編集の道具が使える。
3. 取り込み先が CP932 を要るなら、直した複製を `iconv -f UTF-8 -t CP932` で戻し、別の名前で保存する。変換がエラーで止まったら、その文字を直す。
4. 戻したファイルを、取り込み先に近い形（Excel で開く、取り込みの画面で試す）で開き、日本語が読めるかを確かめる。

Windows のシェルが CP932 の出力を UTF-8 として読む問題は、このページの範囲ではない。<!-- link:begin windows-wsl-ime#mojibake -->Windows・WSL・IME で困ったら<!-- link:end --> を引く。IDE の拡張や WSL 以外の OS での動作は未確認である。

## 全体の確かめ方 {#verify}

変換したファイルは、次の 3 点で確かめる。

- **行数**：原本と複製の行数が同じ。文字コードを変えても、行は増減しない。
- **日本語の列**：先頭の数行で、列名と日本語のセルが読める。空欄の数が、原本を Excel で開いたときと合う。
- **戻したファイル**：CP932 に戻したなら、取り込み先で開いて読める。

集計の結果は、読み込みが正しいことを確かめてから裏取りに進む。裏取りの方法は <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](../recipes/data-analysis.md#check-raw-data)<!-- link:end --> にある。事務作業として繰り返すなら、<!-- link:begin office-paperwork#check -->[事務作業の半自動化（経費・報告） › 全体の確かめ方](../recipes/office-paperwork.md#check)<!-- link:end --> の確かめ方に合わせる。

## うまくいかないとき {#failure}

- **複製を作っても日本語が読めない**：文字コードの指定が違う。CP932 で読めなければ、EUC-JP や UTF-16 を試す。それでも読めないなら、元のファイルが壊れているか、文字コードが混ざっている。
- **変換でエラーになる**：原本の側の文字コードの指定が違うか、変換先の CP932 にない文字がある。エラーの文言と行を確かめ、指定か文字を直して変換し直す。
- **先頭の列名だけ合わない**：BOM が付いている。BOM を外して読ませる（Python の `pandas.read_csv` なら `encoding="utf-8-sig"`）。
- **PDF や文書の日本語が崩れる**：CSV の文字コードではない。<!-- link:begin documents-in-japanese#pdf -->[日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること](documents-in-japanese.md#pdf)<!-- link:end --> を引く。
- **Windows や WSL で入力・表示が化ける**：<!-- link:begin windows-wsl-ime#mojibake -->Windows・WSL・IME で困ったら<!-- link:end --> を引く。
- **作ったファイルの受け取り方が分からない**：<!-- link:begin files-and-code-execution#outputs -->[ファイル作成とコード実行 › 作ったファイルの受け取り方](../app/files-and-code-execution.md#outputs)<!-- link:end --> を引く。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [ファイル作成とコード実行](../app/files-and-code-execution.md)
- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- [データを分析する](../recipes/data-analysis.md)
- [事務作業の半自動化（経費・報告）](../recipes/office-paperwork.md)
- [日本語の資料を読ませる・書かせる](documents-in-japanese.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
