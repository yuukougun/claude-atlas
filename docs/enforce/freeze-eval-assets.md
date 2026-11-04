---
id: freeze-eval-assets
title: 評価資産を凍結し、触れる範囲を絞る
aliases: [評価用のファイルを凍結する, 採点器を書き換えさせない, テストを書き換えさせない設定]
type: recipe
field: enforce
chapter: 縛りの運用
order: 140
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: テストや採点のスクリプト、検証用のデータを Claude が書き換えられないようにし、触れてよいファイルを絞れる。deny ルールだけでは子プロセスを止められないので、サンドボックスと組み合わせる。
signs:
  - {type: goal, text: テストや採点のスクリプトを、Claude に書き換えさせたくない}
  - {type: situation, text: スコアを上げる改善を、長い時間 Claude に任せる}
prerequisites: [verifier-three-conditions, sandboxing]
related: [protect-tests, permission-rules, lockbox-and-holdout, rewrote-tests-to-pass, reward-hacking, test-the-verifier, build-test-harness, protected-paths, hook-recipes, misses-broken-evaluation, selection-pressure]
tracks: [permissions, sandbox, hooks]
sources: [cc-docs-permissions, cc-docs-sandboxing]
volatility: 中
sections:
  - {title: 凍結の前に整えること, anchor: before-freezing}
  - {title: 凍結するものと触らせるもの, anchor: what-to-freeze}
  - {title: 設定で止める（権限ルール・サンドボックス・ファイルの権限）, anchor: how-to-freeze}
  - {title: 凍結が効いているかを確かめる, anchor: check}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：テストや採点のスクリプト、検証用のデータを、3 層の設定で Claude に書き換えさせないようにできる。deny だけでは足りない。
    - **いつ引くか**：スコアを上げる改善を長い時間 Claude へ任せる場面で、テストや採点のスクリプトを書き換えさせたくないとき。
    - **前提**：<!-- link:begin verifier-three-conditions -->[検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)<!-- link:end -->・<!-- link:begin sandboxing -->[サンドボックスで封じ込める](sandboxing.md)<!-- link:end -->

<!-- textlint-disable -->
別名：評価用のファイルを凍結する・採点器を書き換えさせない・テストを書き換えさせない設定
<!-- textlint-enable -->

評価資産の凍結は、採点やテストを決めるファイルとデータを、Claude が改善の作業をしている間は変えられない状態に置く手順である。改善を任せる時間が長いほど、点数を上げる近道として採点側を書き換える機会が増える。依頼に「テストは変えないで」と書くのはお願いにすぎない。ここでは、お願いではなく鍵で止める設定を組む。

## 凍結の前に整えること {#before-freezing}

凍結する前に、採点の仕組みそのものが正しいことを確かめておく。間違った採点器を凍結すると、間違いごと固定される。

- 採点器が満たすべき条件のうち、「書き換えられない」を仕組みにするのがこの手順である。正しさと、本番を代表するかは別に点検する。点検の項目は <!-- link:begin verifier-three-conditions#audit -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 三条件を点検する](../eval/verifier-three-conditions.md#audit)<!-- link:end --> にある
- 何もしない解が負け、強い解が勝ち、手で計算した値と合うことを確かめてから固める。順は <!-- link:begin test-the-verifier#freeze -->[検証器そのものを確かめる（red/green・手で計算したケース） › 確かめてから凍結する](../eval/test-the-verifier.md#freeze)<!-- link:end --> にある
- 採点の正本は一か所にする。凍結する範囲が小さいほど、設定の行も少なく済む（<!-- link:begin test-the-verifier#single-scorer -->[検証器そのものを確かめる（red/green・手で計算したケース） › 採点の正本は一か所に](../eval/test-the-verifier.md#single-scorer)<!-- link:end -->）

公開されている自律研究の実践例に、評価指標を定義するファイルを凍結し、エージェントが編集してよいファイルを 1 つに限ったものがある（根拠：弱。単独の実践例）。凍結するものを少なく、触らせるものを少なくする考え方はこの手順と同じである。

## 凍結するものと触らせるもの {#what-to-freeze}

凍結するのは、「勝ち負けを決めるもの」である。触らせるのは、「勝つために直すもの」である。

| 区分 | 例 | 理由 |
| --- | --- | --- |
| 凍結する | 採点のスクリプト、テスト、期待値のファイル、採点に使う入力データ | 変わると、同じ点数が別の意味になる |
| 凍結する | 採点を呼ぶ設定（Makefile・CI の設定・閾値の設定） | スクリプトが無傷でも、呼び方を変えれば採点が変わる |
| 隠す | 人だけが持つ検証用のデータ（hold-out） | 読まれた時点で評価のリークになる |
| 触らせる | 実装のコード、作業メモ、採点の出力先 | 改善の作業そのものである |

人だけが持つ検証用のデータは、書き換えさせないだけでは足りず、読ませない。置き場所と点数だけを返す運用は <!-- link:begin lockbox-and-holdout#keep-out-of-reach -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 読めない所に置く](../eval/lockbox-and-holdout.md#keep-out-of-reach)<!-- link:end --> と <!-- link:begin lockbox-and-holdout#scores-only -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 点数だけを返す](../eval/lockbox-and-holdout.md#scores-only)<!-- link:end --> にある。

凍結するものは、少数のディレクトリにまとめる。たとえば `eval/`（採点のスクリプトと期待値）と `tests/frozen/`（人が確かめたテスト）に寄せると、ルールが数行で済む。ファイルを 1 つずつ並べると、新しいファイルが増えたときに凍結から漏れる。

Claude が採点を走らせることは止めない。読んで走らせるのは許し、書き換えは止める。採点の出力は、凍結した場所の外（たとえば `out/`）へ出す。

## 設定で止める（権限ルール・サンドボックス・ファイルの権限） {#how-to-freeze}

1 つの層だけでは止まらない。権限ルールは Claude の道具に効き、サンドボックスは Bash から起きるプロセスに効く。ファイルの権限は OS が見る。それぞれが止めるものと止めないものは、次のとおりである。

| 層 | 止めるもの | 止めないもの |
| --- | --- | --- |
| 権限ルール（`Edit` の deny） | Claude の編集の道具、認識できるシェルのコマンド（`sed`・`tee` など）、リダイレクトの先 | Python や Node のスクリプトが自分で開いて書くファイル |
| サンドボックス（`denyWrite`・`denyRead`） | Bash などのコマンドと、そこから起きる子プロセスの読み書き | サンドボックスの外で動くフックや MCP サーバー |
| ファイルの権限（OS） | 権限のない利用者からの書き込み | 同じ利用者による権限の付け直し（サンドボックスの `denyWrite` と組み合わせて初めて効く） |

手順は次の順で組む。各段の終わりに、何ができていればよいかを書く。

1. **凍結する場所を決める。** 「凍結する」と「隠す」に当たるものについて、`eval/`・`tests/frozen/`・`data/holdout/` のように置き場所を決める。終わりの確かめ：凍結する場所が、ディレクトリの名前で 3 行以内に言える。
2. **権限ルールで道具を止める。** `permissions.deny` に `Edit(...)` を書く。パスは `/` で始め、プロジェクトの根からの相対になる。`Write(...)` と `NotebookEdit(...)` にパスを付けたルールは受け付けられるが何にも当たらないので、書き込みは `Edit` で書く。`Edit` の deny は組み込みの編集の道具すべてに効く。終わりの確かめ：設定を読み直し、`Write(` で始まるルールが残っていない。
3. **サンドボックスで子プロセスを止める。** `sandbox.enabled` を有効にし、`filesystem.denyWrite` へ同じ場所を書く。サンドボックスのパスの書き方は権限ルールと違う。`/tmp/x` は絶対パス、`~/` はホームを指す。`.` は、プロジェクトの設定なら根を指す。起動できないときは通さないよう、`failIfUnavailable` も有効にする。`allowUnsandboxedCommands` は false にして、サンドボックスの外で再試行させない。有効にする手順は <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](sandboxing.md#minimal)<!-- link:end -->、起動できない場合の扱いは <!-- link:begin sandboxing#fail-if-unavailable -->[サンドボックスで封じ込める › 起動できないときに通さない](sandboxing.md#fail-if-unavailable)<!-- link:end --> にある。終わりの確かめ：設定を置いて新しいセッションを始めたとき、サンドボックスが有効になっている（確かめ方は次の節の依頼でも分かる）。
4. **人だけが持つデータは読みも止める。** 権限ルールの `Read` の deny と、`filesystem.denyRead` の両方に書く。サンドボックスの `denyRead` は Read の道具を止めず、`Read` の deny は子プロセスを止めない。2 つが補い合う。置けるなら、リポジトリの外に置くほうが確実である。
5. **フックを足すなら範囲を狭くする。** フックは、凍結した場所を名指しする操作を前で止める用途に使える。フックはサンドボックスの外で動く。決めた文字列で当てる方式は、取りこぼしも止めすぎも起こす。常設の前に確かめる（<!-- link:begin hook-recipes#verify -->[代表的なフックのレシピ › 常設する前に確かめる](hook-recipes.md#verify)<!-- link:end -->）。jq のような外のコマンドがないときに素通しになる雛形もあるため、スクリプトの側で閉じる。
6. **必要なら OS のファイルの権限を足す。** 凍結する場所の書き込み権限を外す。ただし同じ利用者なら Claude の側から権限を付け直せるので、サンドボックスの `denyWrite` がある環境で、補助として使う。

雛形は 1 つのファイルにまとめてある。パスは自分のリポジトリの置き場所に直して使う。

<!-- gen:begin snippet freeze-eval-assets/freeze-settings -->
<!-- textlint-disable -->

??? example "雛形：評価用のファイルとデータを書き換えさせない設定の例"

    ```json
    {
      "permissions": {
        "deny": [
          "Edit(/eval/**)",
          "Edit(/tests/frozen/**)",
          "Edit(/data/holdout/**)",
          "Read(/data/holdout/**)"
        ]
      },
      "sandbox": {
        "enabled": true,
        "failIfUnavailable": true,
        "allowUnsandboxedCommands": false,
        "filesystem": {
          "denyWrite": ["./eval", "./tests/frozen", "./data/holdout"],
          "denyRead": ["./data/holdout"]
        }
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet freeze-eval-assets/freeze-settings -->

権限ルールとサンドボックスの各機能の詳細は、それぞれのページに任せる。ルールの評価の順と、何にも当たらないパスは <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](permission-rules.md#path-rules)<!-- link:end -->、子プロセスに効かない理由は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](permission-rules.md#child-processes)<!-- link:end --> にある。どの権限モードでも保護される場所は <!-- link:begin protected-paths#protected -->[消せない場所・触れない場所（protected paths） › 保護される場所と、モードごとの扱い](protected-paths.md#protected)<!-- link:end --> にある。サンドボックスが囲えるものと囲えないものは <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](sandboxing.md#scope)<!-- link:end --> を引く。

権限ルールとサンドボックスは別々に効く。公式は、`Read` と `Edit` の deny がサンドボックスの設定にも合わさると書く。それでも雛形は両方に書く。設定を読んだだけで、どこが凍結されているかが分かるためである。

## 凍結が効いているかを確かめる {#check}

設定を置いただけでは、効いているか分からない。パスの書き方を間違えると、ルールはエラーなしで何にも当たらない。凍結は、わざと破ろうとして確かめる。

確かめるときは、評価用のファイルそのものを書き換えさせない。凍結した場所の中に、使い捨ての見張りのファイル（`eval/.freeze-canary.txt`）を作らせる。凍結が効いていれば作れず、効いていなければ見張りのファイルが残るだけで済む。3 つ目の試しのために、人が先に `data/holdout/.freeze-canary.txt` を作り、中身は意味のない文字列にしておく。ファイルがないと、凍結と関係なく読み取りが失敗してしまう。確かめる依頼の例は次のとおりである。

<!-- gen:begin snippet freeze-eval-assets/freeze-canary-check -->
<!-- textlint-disable -->

??? example "雛形：凍結が効いているかを確かめる依頼"

    ```markdown
    凍結が効いているかの確認だ。評価用のファイルは変えない。次の 3 つを順に試し、それぞれ成功したか、止められたか、どのエラーが出たかを、そのまま報告してほしい。

    1. Edit か Write の道具で、`eval/.freeze-canary.txt` という新しいファイルを作る
    2. Bash で `python3 -c "open('eval/.freeze-canary.txt', 'w').write('x')"` を実行する
    3. Bash で `python3 -c "print(open('data/holdout/.freeze-canary.txt').read())"` を実行する

    止められたときに、別の方法で回り込まない。設定を変えない。終わったら `ls eval/.freeze-canary.txt` を実行し、ファイルが残っているかも報告してほしい。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet freeze-eval-assets/freeze-canary-check -->

読み方は次のとおりである。

- 1 つ目（編集の道具）と 2 つ目（Python のスクリプト）の両方が止まる。片方だけなら、止まらなかった層の設定を見直す。1 つ目だけが止まるなら、サンドボックスが働いていない
- 3 つ目（hold-out を読む）が失敗する。読めたなら `denyRead` が当たっていない
- Claude の返答は観察として扱う。合否は、依頼の後に人が `ls eval/.freeze-canary.txt` を実行して決める。返答は、実際のファイルの状態と食い違うことがある
- 見張りのファイルが残っていたら、消してから設定を直し、もう一度試す

!!! example "判断例：Edit の deny だけで足りるか"
    - **状況**：夜通しスコアを上げる改善を任せる。採点のスクリプトは `eval/` にあり、`Edit(/eval/**)` の deny を入れた。
    - **迷う候補**：deny だけで走らせる。サンドボックスの `denyWrite` も足し、見張りのファイルで確かめてから走らせる。
    - **選んだもの**：`denyWrite` も足し、確かめてから走らせる。
    - **理由**：Claude が Python のスクリプトを書いて走らせると、そのスクリプトが `eval/` のファイルを開いて書ける。deny は編集の道具にしか効かない。夜通し見ていない時間ほど、取りこぼしの代償が大きい。

確かめたあとの運用でも、凍結が外れた形跡を見る。凍結した場所の差分を、改善の区切りごとに出す（たとえば `git status` と `git diff --stat -- eval tests/frozen`）。差分が出ていれば、どの層をすり抜けたかを調べる。

## 失敗したとき {#when-it-fails}

凍結しても、評価がずれる経路は残る。症状から入るページを選ぶ。

- テストを書き換えて通された、または特例の分岐で通された：<!-- link:begin rewrote-tests-to-pass -->[テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)<!-- link:end -->。何が書き換えられる状態だったかを切り分け、凍結の穴を埋める
- 手元の評価は良いのに、本番で通用しない：<!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end -->。凍結は評価の正しさや、本番を代表するかを保証しない。凍結する前の守りに戻る
- 正当な編集まで止まる：パスの範囲が広すぎるか、フックが止めすぎている。<!-- link:begin hook-recipes#failures -->[代表的なフックのレシピ › 動かないとき・止めすぎるとき](hook-recipes.md#failures)<!-- link:end --> と <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](permission-rules.md#path-rules)<!-- link:end --> を引く
- 凍結は破られていないのに、試行を重ねるうちに点数だけが上がる：選択圧の問題である。防ぎ方は <!-- link:begin selection-pressure#defenses -->[選択圧：良かった版を選び続ける罠 › 防ぎ方](../eval/selection-pressure.md#defenses)<!-- link:end --> にある

なぜ採点を騙す方向に解かれるかの理由は <!-- link:begin reward-hacking#why -->[採点器を騙す（reward hacking） › なぜそうなるか](../basics/reward-hacking.md#why)<!-- link:end -->、テストの守りの全体像（依頼・差分のレビュー・鍵・見せないデータ）は <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> にある。検証の環境を作らせる場合は、検証の資産を分けて置く（<!-- link:begin build-test-harness#separate-eval-assets -->[検証環境・テスト基盤を作らせる › 検証の資産を分けて置く](../recipes/build-test-harness.md#separate-eval-assets)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [サンドボックスで封じ込める](sandboxing.md)

**関連**

- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [権限ルール（allow・ask・deny）](permission-rules.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [検証環境・テスト基盤を作らせる](../recipes/build-test-harness.md)
- [消せない場所・触れない場所（protected paths）](protected-paths.md)
- [代表的なフックのレシピ](hook-recipes.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
