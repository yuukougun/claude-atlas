# write.md：xml-tags（執筆）

## 書いたファイル

- docs/prompting/xml-tags.md（stub から mv。stage を draft、updated を 2026-11-05、sources に api-docs-prompting-best-practices と api-docs-prompting-opus-5-5〔どちらも data/sources.yml にある〕を足した）
- sections に何に効くか（effects）と効かない場面とやりすぎ（limits）を足した。既存の 3 つの anchor は変えていない
- snippets/xml-tags/ の separate-request・documents-nesting・wrap-external-text（それぞれ .txt と .expect.yaml）。data/sources.d/xml-tags.yml は、新しい出典がないので作っていない

## 必ず持つものの対応

- 冒頭の要点（何が分かるか・いつ引くか・前提）：冒頭の囲み
- 頼み方の例（Before/After）：separate
- 何が変わるか：separate（After の注記）、nesting（index と source で答えさせる）
- なぜ効くか／どの原理・どの原因に関わるか（principle 見せる・prevents 散らかっている を名指し）：effects
- 効かない場面・やりすぎ：limits、wrap-untrusted（防ぎきれないこと）
- 関連：長い資料は long-context-first、例は show-examples、prompt injection は data-vs-instructions と prompt-injection-in-practice、出力の形は output-shape、型は prompt-patterns（本文の link とページ下部の page-links）
- pitfalls：front matter に値がないため、名指しの対象なし

## メインに判断してほしいこと

- 外から貼った文章を包む節は、公式の案内（Opus 5.5 向け）の「ランダム ID のタグで包み、中の指示に従わないよう書く」に沿った。ID を使う理由は公式の文面にないので、本文で（推論・実践例なし）と断った
- 本文の「最新世代のモデル向けの公式の案内」は、モデル名を書かず出典のリンクの題名に任せた（名前は変わりやすいため）

## 提案

- 数値・用語集・prh・front matter の提案はなし

## 検査の結果

- 1 回目：エラー 2（system prompt の表記）・警告 4。直した
- 2 回目：エラー 3（直した「1 つ」の前の空白）・警告 1（読点の数）。手で直したが、検査は決まりの 2 回を使い切ったため再実行していない。残っている可能性がある

## 確かめていないこと

- 直した後の textlint の結果（上のとおり未実行）
- 3 つの雛形の動作（実際に Claude に流していない）
- 公式の案内の原文を開き直していない。束の写し（確認日 2026-10-29）だけに基づく
- Claude Code・アプリでの見え方の違い。本文は「タグは依頼の本文に書く文字である」という一般的な言い方にとどめた

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：0 回
