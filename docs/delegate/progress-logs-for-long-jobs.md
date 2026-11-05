---
id: progress-logs-for-long-jobs
title: 長時間ジョブの進捗ログを設計する
aliases: [進捗ログ, 長時間のジョブの監視]
type: recipe
field: delegate
chapter: 続けさせる
order: 70
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 確かめていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 長時間の作業に、要約した指標を定期的に書き出す進捗ログを用意し、Claude にも人にも状況が見えるようにできる。生のログを大量に出すと、Claude 自身が状況を追えなくなる。
signs:
  - {type: goal, text: 長時間の実験やジョブの途中経過を見えるようにしたい}
  - {type: symptom, text: 長いジョブのログが大きすぎて、Claude が状況を追えない}
prerequisites: [progress-files]
related: [checking-unattended-runs, experiment-log, build-observation-tools, goal-until-done, agent-view-and-background, handoff-documents, long-running-agent-context, compact-and-auto-compact, completion-notifications, blames-the-tools]
tracks: [monitor-tool]
sources: [cc-docs-tools-reference, cc-docs-sandboxing, cc-changelog, cc-docs-changelog]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 手順, anchor: steps}
  - {title: 雛形, anchor: templates}
  - {title: 確かめ方, anchor: check}
  - {title: 進捗ファイルなどとの違い, anchor: vs-progress-files}
  - {title: 失敗したとき, anchor: troubleshoot}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：長時間の作業に、要約した指標を定期的に書き出す進捗ログを用意し、Claude にも人にも状況が見えるようにできる。
    - **いつ引くか**：長時間の実験やジョブの途中経過を見えるようにしたいとき。長いジョブのログが大きすぎて、Claude が状況を追えないとき。
    - **前提**：<!-- link:begin progress-files -->[進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)<!-- link:end -->

<!-- textlint-disable -->
別名：進捗ログ・長時間のジョブの監視
<!-- textlint-enable -->

長時間ジョブの進捗ログを設計するとは、数時間かかる実験やデータ処理に、状況を要約した指標だけを定期的に書き出すファイルを持たせることである。生のログは別のファイルに逃がし、Claude と人は要約のほうだけを読む。

生のログをそのまま Claude に読ませると、出力が会話に積み上がり、Claude 自身が状況を追えなくなる。長時間ジョブを任せたのに、ログが大きすぎ、エージェント自身は監視できなかった例がある（根拠：弱）。要約の指標は、この読む量を一定に抑える。

## 先に整える守り {#guards}

進捗ログは状況を見えるようにする仕組みで、ジョブが正しく終わったことの証明ではない。無人で長く回す前に、次の 4 つを決めておく。

- **終わりの判断を進捗ログだけに置かない**：進捗の指標が良く見えても、結果が正しいとは限らない。確かめる順序と、最後の判断を人へ置く考え方は <!-- link:begin checking-unattended-runs#guards-first -->[無人実行の結果を確かめる › 先に整える守り](../verify/checking-unattended-runs.md#guards-first)<!-- link:end --> で扱っている。
- **止める条件と上限を先に決める**：ジョブを任せ続けるなら、終わりの状態と上限を条件に書く。書き方は <!-- link:begin goal-until-done#writing-conditions -->[/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](goal-until-done.md#writing-conditions)<!-- link:end --> を見る。
- **見張りに許す操作を絞る**：Monitor の道具は、背景で動かしたコマンドの出力を 1 行ずつ Claude に返す Claude Code の道具で、Bash と同じ権限ルールで動く。見張りのコマンドは、読むだけのもの（`tail` や `grep`）に限り、Bash の allow ルールと deny ルールで範囲を決める。
- **フックの効く範囲を知っておく**：Bash に当てたフックは Monitor が起動するシェルコマンドにも走る（版の条件：<!-- fact:begin hook-monitor-min-version -->Claude Code 2.1.314 以降（2026-11-06 時点）<!-- fact:end -->）。止める・確認を求めることはできるが、許可や書き換えはできない。それより前の版では、Bash のフックは Monitor のコマンドを素通しにしていた。

席を外して背景のセッションに投げる場合は、投げる前に決める守りが別にある。<!-- link:begin agent-view-and-background#guards-first -->[agent view と背景セッション › 投げる前に決める守り](agent-view-and-background.md#guards-first)<!-- link:end --> を見る。

## 手順 {#steps}

各段の終わりに、何を見れば済んだと言えるかを添える。

1. **見たい指標を 3〜5 個に絞る**
    - 進み具合（何件中の何件か）・速さ・結果の良さを表す値・エラーの件数・最後に更新した時刻を基本にする。
    - 終わり：「この数行を見れば、順調か異常かを判断できる」と言える。言えなければ、指標が足りないか多すぎる。
2. **ログを 2 本に分ける**
    - 生のログ（`raw.log`）は人が後で調べる用に、すべて残す。要約（`progress.jsonl`）には、1 の指標だけを 1 行 1 件で書く。
    - 終わり：ジョブを動かすと、2 つのファイルができ、要約のほうが 1 画面で読める行数にとどまっている。
3. **書く間隔を、ステップではなく時間で決める**
    - 毎ステップ書くと、要約が生のログと同じ量になる。1 分に 1 回、あるいは 5 分に 1 回のように、時間で間引く。
    - 終わり：ジョブの全体の長さを間隔で割った行数が、末尾を読んで全体が見渡せる程度に収まっている。
4. **終わりと失敗の行を必ず書く**
    - 状態（`running`・`done`・`failed`）を行に入れ、終わりと失敗は間隔に関係なく書く。例外で落ちたときも、`failed` の行を書いてから落ちるようにする。
    - 終わり：ジョブを故意に失敗させると、`failed` の行が最後に残る。
5. **Claude に読み方を指示する**
    - 状況は要約の末尾だけで答えさせる。生のログは丸ごと読ませず、異常の時刻の前後だけを `grep` で読ませる。値の直しやジョブの停止は、報告して指示を待たせる。
    - 終わり：状況を聞くと、Claude が要約の末尾だけを読んで答える。
6. **見張りを張る**
    - Claude Code では、Monitor の道具が、背景のコマンドの出力を 1 行ずつ Claude に返す。要約のファイルの末尾を見張り、異常の行だけを流すように絞る。生のログを直接見張らせない。「errors が前の行より増えた」のような前の行との比較は `grep` だけでは絞れないので、絞る短いスクリプトを Claude に書かせるか、書き手が異常のときだけ別の行を書くようにする。
    - 見張りには期限があり、期限が来ると見張りは終わって、Claude には 1 回だけ知らせが来る。まだ要るなら張り直させる。既定の期限は<!-- fact:begin monitor-default-deadline -->5 分（2026-11-05 時点）<!-- fact:end -->、上限は対話で<!-- fact:begin monitor-max-deadline -->30 分（2026-11-05 時点）<!-- fact:end -->、`-p` で<!-- fact:begin monitor-print-mode-max-deadline -->10 分（2026-11-05 時点）<!-- fact:end -->である。提供経路か通信の抑制の環境変数があるときは、<!-- fact:begin monitor-min-version-restricted-envs -->Claude Code 2.1.310 以降（2026-11-05 時点）<!-- fact:end -->が要る。
    - 終わり：異常の行が出たときだけ、Claude が割り込んで報告する。
7. **人の側の見方を決める**
    - 人は `tail -f progress.jsonl` で眺めればよい。席を離れるなら、終わりや異常の知らせを受ける仕組みを使う。仕組みの選び方は <!-- link:begin completion-notifications#when-to-notify -->終わったら知らせてもらう<!-- link:end --> を見る。
    - 終わり：離席中に異常が起きたとき、戻る前に気づける。

要約の行は、たとえば次の形になる。

```json
{"ts":"2026-11-05T09:10:00","status":"running","step":600,"total":2000,"elapsed_s":600,"errors":0,"score":0.412}
{"ts":"2026-11-05T09:11:00","status":"running","step":640,"total":2000,"elapsed_s":660,"errors":3,"score":0.409}
```

!!! example "判断例：生のログを直接見張らせるか、要約を見張らせるか"
    - **状況**：数時間かかる学習のジョブを背景で動かしていて、Claude に異常を知らせてほしい。生のログは 1 秒に数十行出る。
    - **迷う候補**：生のログを Monitor で見張って、`ERROR` を含む行を流す。要約のファイルを見張って、`failed` と `errors` の増加だけを流す。
    - **選んだもの**：要約のファイルを見張る。
    - **理由**：生のログの `ERROR` は、再試行で直る軽い警告でも出るので、知らせが細切れになり、Claude の読む量が増える。要約の `errors` の増加なら、ジョブが集計した異常だけが届く。生のログは、異常の時刻が分かってから前後だけを読めば足りる。

## 雛形 {#templates}

要約の書き手と、読み方を指示する依頼の 2 つを載せる。ファイル名と指標の名前は例なので、自分のジョブに合わせて置き換える。

<!-- gen:begin snippet progress-logs-for-long-jobs/progress-writer -->
<!-- textlint-disable -->

??? example "雛形：要約の指標だけを定期的に書き出す進捗ログの書き手（Python）"

    ```python
    # progress-writer.py
    # 要約の指標だけを 1 行の JSON にして progress.jsonl へ書き足す。
    # 生のログ（ループの中の print や例外の全文）は、別のファイル（raw.log）へ出す。
    import json
    import time


    class Progress:
        def __init__(self, path="progress.jsonl", total=None, every_sec=60):
            self.path = path
            self.total = total          # 全体の大きさ（ステップ数・件数など）。分からなければ None
            self.every_sec = every_sec  # 書く間隔。ステップごとではなく時間で間引く
            self.start = time.time()
            self.last = 0.0

        def _write(self, status, step, metrics):
            now = time.time()
            row = {
                "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "status": status,       # running / done / failed のどれか
                "step": step,
                "total": self.total,
                "elapsed_s": round(now - self.start),
                **metrics,              # 見たい指標（損失・エラーの件数・処理の速さなど）
            }
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            self.last = now

        def tick(self, step, **metrics):
            # 呼ぶのは毎ステップでよい。書くのは every_sec 秒に 1 回だけ
            if time.time() - self.last >= self.every_sec:
                self._write("running", step, metrics)

        def finish(self, status, step=None, **metrics):
            # 終わりと失敗は、間隔に関係なく必ず書く
            self._write(status, step, metrics)


    if __name__ == "__main__":
        # 動作の確かめ用。間隔を 1 秒にして、5 秒ほどの擬似ジョブを回す
        p = Progress(total=50, every_sec=1)
        errors = 0
        try:
            for i in range(1, 51):
                time.sleep(0.1)
                if i % 17 == 0:
                    errors += 1
                p.tick(i, errors=errors, score=round(1 / i, 4))
            p.finish("done", step=50, errors=errors)
        except Exception as e:
            p.finish("failed", error=type(e).__name__)
            raise
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.98。

<!-- textlint-enable -->
<!-- gen:end snippet progress-logs-for-long-jobs/progress-writer -->

<!-- gen:begin snippet progress-logs-for-long-jobs/watch-request -->
<!-- textlint-disable -->

??? example "雛形：要約の進捗ログだけを読ませ、異常の行だけで知らせさせる依頼"

    ```text
    ./run_experiment.sh をバックグラウンドで動かしてある。生のログは raw.log、要約は progress.jsonl に出ている。次の決まりで見張ってほしい。

    - 状況を聞かれたら、progress.jsonl の末尾 20 行だけを読んで答える。raw.log を丸ごと読んだり、cat で全部出したりしない
    - Monitor で progress.jsonl の末尾を見張る。流すのは、status が failed の行と、errors の値が前の行より増えた行だけにする（grep などで絞り、絞らない行は Claude に返さない）
    - 異常の行が出たら、その時刻の前後だけを raw.log から grep で読み、原因の見当を 3 行以内で報告する
    - 見張りの期限が切れたら、ジョブがまだ動いているときだけ見張りを張り直す
    - 値の直し・ジョブの停止・再実行はしない。報告して、こちらの指示を待つ
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.98。

<!-- textlint-enable -->
<!-- gen:end snippet progress-logs-for-long-jobs/watch-request -->

## 確かめ方 {#check}

進捗ログができたら、次の 3 つを実際に試す。

1. 新しいセッションの Claude に「いまどこまで進んだか」と聞く。要約の末尾だけを読んで、進み具合と直近の指標を答えられれば、要約として足りている。生のログを丸ごと読みに行ったなら、依頼の文が足りないか、要約に必要な指標が入っていない。
2. ジョブを故意に失敗させる。`failed` の行が書かれ、見張りから異常の知らせが届くことを見る。
3. 要約の行数と大きさを、ジョブの途中で見る。読む量が時間とともに増え続けているなら、間隔が短すぎる。

要約の指標は、結果の正しさを示さない。ジョブが終わった後の確かめは <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> のように、出力・記録・差分で行う。

## 進捗ファイルなどとの違い {#vs-progress-files}

進捗ログと近い仕組みを、役割で分ける。

- <!-- link:begin progress-files -->[進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)<!-- link:end -->：人と Claude が対話で再開するための状態（計画・やること・決めたこと）を持つ。このページの進捗ログは、無人の長時間ジョブを観察して判断するための、実行中の要約の指標を持つ。状態をファイルに書く考え方は共通である。
- <!-- link:begin experiment-log -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)<!-- link:end -->：実験ごとの仮説・提案者・分母・結果の判定を、実行の前後に残す。進捗ログは、実行の最中の様子だけを扱う。
- <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end -->：可視化や集計の道具を Claude に作らせる。進捗ログの書き手も、その道具の 1 つとして作らせてよい。
- <!-- link:begin handoff-documents -->[handoff 文書と document-and-clear](../context/handoff-documents.md)<!-- link:end -->：会話を新しくするときの引き継ぎ文書を持つ。要約のファイルは、圧縮や会話の入れ替えで消えない場所に置くので、新しい会話からも続きを読める。

## 失敗したとき {#troubleshoot}

進捗ログがあってもうまくいかないときは、症状で次を見る。

- **要約を作ったのに Claude の文脈が膨らむ**：Claude が生のログも読んでいる。依頼に、読んでよいファイルと、読んではいけないファイルを書く。長い作業で文脈を保つ考え方は <!-- link:begin long-running-agent-context#external-state -->[長時間エージェントのコンテキスト管理 › 状態をファイルに持たせる](../api/long-running-agent-context.md#external-state)<!-- link:end --> を見る。
- **圧縮で経過を忘れる**：経過を会話ではなく、要約のファイルから読ませる。圧縮で何が消えるかと、書き出してから新しくする判断は <!-- link:begin compact-and-auto-compact#compact-or-clear -->[/compact と自動圧縮 › 圧縮か、書き出して /clear か](../context/compact-and-auto-compact.md#compact-or-clear)<!-- link:end --> を見る。
- **見張りが止まって、知らせが来なくなる**：見張りの期限が切れている。要約の最終行の時刻でジョブが生きていることを確かめてから、Claude に見張りを張り直させる。
- **Claude が「道具が壊れた」と言い出す**：長い作業の劣化の兆しのことがある。<!-- link:begin blames-the-tools#diagnosis -->[環境や道具が壊れたと言い出す › 原因を安く確かめる順](../symptoms/blames-the-tools.md#diagnosis)<!-- link:end --> の順に安く確かめる。
- **要約が止まっているのに、ジョブは動いているように見える**：書き手の側の不具合である。最終行の `ts` が、書く間隔の何倍も前なら、ジョブが固まっている可能性を疑う。

この手順は Claude Code を想定している。Monitor の道具が使えない環境や、ほかの OS と IDE 拡張での動きは未確認である。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)

**関連**

- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)
- [/goal（完了するまで続けさせる）](goal-until-done.md)
- [agent view と背景セッション](agent-view-and-background.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [長時間エージェントのコンテキスト管理](../api/long-running-agent-context.md)
- [/compact と自動圧縮](../context/compact-and-auto-compact.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Tools reference](https://code.claude.com/docs/en/tools-reference)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
