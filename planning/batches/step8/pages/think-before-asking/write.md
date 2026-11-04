# think-before-asking 執筆報告

## 書いたファイル
- docs/judgment/think-before-asking.md（stubs から移した。stage を draft に、updated を 2026-11-05 に、sources を追加、sections に what-you-keep・how-to-check の 2 節を追加）
- snippets/think-before-asking/question-role.md と question-role.expect.yaml（目次の templates の「問い役」）
- data/sources.d は作らず、data/sources.yml にある既存の id だけを sources に使った

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`（節の外）
- 判断例（状況・迷う候補・選んだもの・理由）：choose-vs-ideate（「判断例：最適化コンテストの開始直後に、AI をいつ開くか」）
- level を持つ：front matter の level: 整える
- 構成の目安（要点→何が起きるか→なぜ→判断例→握るもの→確かめ方）：self-first（何が起きるか・なぜ）→ choose-vs-ideate（判断例）→ what-you-keep（握るもの）→ how-to-check（確かめ方）。questions-rebuttals-tools・generic-frameworks・five-questions は目次の節で、頼み方と型の中身

## メインに判断してほしいこと
- Psyho の投稿（threadreaderapp.com、sources.yml で noai: true）は資料にしなかった。そのため「直感を育てる単純な解で実験する」の根拠は、terry_u16 の講義資料と AHC001 の解説で代えた
- Shun_PI の資料・a1k0n の事例・p56 の項目は、競技の技術そのものなので kyopro-atlas に任せ、本文に入れていない（sources.yml にも id はあるので、足したければ言ってほしい）
- 判断例で「15〜30 分」を「決めた時間」と言い換えた箇所と、本文の「15〜30 分は目安（根拠：弱）」の扱いでよいか
- decide-when-to-quit（related にない）と competition-rules を、ページ単位で link した。related に足すかは任せる

## 提案
```yaml
frontmatter:
  - {id: think-before-asking, key: related, before: [], after: [decide-when-to-quit, competition-rules], reason: "本文から指している。related に足すなら追記"}
```
（上は任意。足さなくても check_page は通っている）

## 検査の結果
- 1 回目：エラー 0・警告 4（助詞の重複）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 研究の数値（0.648 対 0.899、196 人）は調査資料の写しによる。原論文は開いていない。Wong & Qiu は著者の紹介ページ経由で、原論文未確認（本文に書いた）
- Fan et al. の課題の細部、Kumar et al. の LLM 支援の有無は開いていない。本文は束の記述の範囲にとどめた
- 雛形 question-role は動かしていない（expect は想定）
- 画像生成 AI の研究（Wadinambiarachchi ほか）の中身は開いていない。束の注記（#63）の範囲

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回
