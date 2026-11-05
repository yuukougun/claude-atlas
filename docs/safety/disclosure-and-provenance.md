---
id: disclosure-and-provenance
title: AI 利用の開示と出所の記録
aliases: [AI 利用の申告, AI を使った旨の明記, 出所の明示, フェアプレー]
type: concept
field: safety
chapter: 規則と開示
order: 170
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る]
prevents: []
pitfalls: []
scenes: [学習, コンテスト, チーム, 文章, 開発]
summary: AI をどこにどう使ったかを開示し、事前に作ったコードや資料の出所を記録しておくと、規則の確認と説明の求めに答えられる。開示の求め方は場ごとに違うので、規則で確かめる。
signs:
  - {type: situation, text: レポートや提出物に、AI を使った箇所を書くよう求められた}
  - {type: goal, text: AI で作ったコードを使ったことを、後で説明できるようにしたい}
prerequisites: [checking-ai-rules]
related: [instructions-hidden-in-materials, competition-rules, practice-vs-contest-day, own-generated-code, record-decisions, less-ai-sounding-japanese]
sources: [mext-genai-university-overview, anthropic-fable-mythos-5-1]
volatility: 中
sections:
  - {title: 開示・相談・出所・意図の四つの観点, anchor: four-points}
  - {title: 出所を記録する, anchor: provenance}
  - {title: 説明できる状態を保つ, anchor: explainable}
  - {title: 何に効くか, anchor: effects}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：AI をどこにどう使ったかを開示し、出所を記録しておくと、規則の確認と説明の求めに答えられる。
    - **いつ引くか**：レポートや提出物に AI を使った箇所を書くよう求められたとき。AI で作ったコードを使ったことを、後で説明できるようにしたいとき。
    - **前提**：<!-- link:begin checking-ai-rules -->[学校・組織・コンテストの規則（類型と確認表）](checking-ai-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI 利用の申告・AI を使った旨の明記・出所の明示・フェアプレー
<!-- textlint-enable -->

AI 利用の開示と出所の記録は、AI を使った事実と、使ったコードや資料の来歴を、自分の手で残しておく習慣である。開示の求め方は学校・組織・大会で違う。そのため、何を書くかは規則で決まり、この習慣は、規則に合わせて書ける材料を手元に持っておくためにある。

## 開示・相談・出所・意図の四つの観点 {#four-points}

AI の利用に関わる公正さは、開示・相談・出所・意図の 4 つの観点で確かめると抜けにくい。コンテストの規則を見比べた調査では、フェアプレーの扱いがこの 4 つに収束する傾向があった（根拠：中。版に依存する傾向であり、個々の規則は読んで確かめる）。

- **開示**：どこに AI を使ったかを、規則が求める形で書く。解説・応募時の記載・自己申告・録画など、求め方は場ごとに違う。
- **外部への相談**：人に相談してはいけない場では、AI への相談も同じ線で扱われることがある。AI を相談相手に含めるかどうかは、規則の文言で確かめる。
- **出所**：事前に作ったコードや資料を持ち込める場では、それがどこから来たかを示せるようにする。
- **意図**：条文が細部を決めていない所は、主催者や出題者が何を確かめたいのかを尊重して判断する。

運営側は、参加者が AI を使っていないことを証明できない。そのため多くの大会は参加者の誠実さに頼っており、規則を読まなかったことは言い訳にならない（根拠：中）。学校のレポート課題も同じ構造である。

規則の型の見分け方と確認表は、<!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](checking-ai-rules.md#checklist)<!-- link:end --> にある。主な大会の類型と確認日は、<!-- link:begin competition-rules#rules-by-type -->[大会の規則の早見（禁止・部門分け・許可と開示） › 類型ごとの大会（確認日付き）](../contest/competition-rules.md#rules-by-type)<!-- link:end --> で引く。ここでは条文を要約せず、確認先だけを示す。

## 出所を記録する {#provenance}

出所の記録とは、AI を使った箇所と、持ち込んだコードや資料の来歴を、作業と同じ時期に自分の手で残すことである。後から思い出して書くと、どこまでが AI の下書きで、どこからが自分の手直しかが曖昧になる。

残す項目は、次の 4 つに絞ると続けやすい。

- **箇所**：提出物のどの部分か。ファイル名や節の名前で書く。
- **使い方**：下書き・説明の依頼・レビュー・テストの作成など、AI に何を頼んだか。
- **自分で確かめたこと**：動かした、読み直した、一次資料と照らした、など。
- **持ち込んだ物の来歴**：事前に作ったコードや資料が、自作か、生成か、配布物か。配布物なら、置いた場所とライセンスの確認。

次の雛形は、この 4 つを 1 枚にした記録の型である。提出物と同じ場所に置き、作業のたびに足す。

<!-- gen:begin snippet disclosure-and-provenance/provenance-log -->
<!-- textlint-disable -->

???+ example "雛形：AI 利用の記録の型"

    ```markdown
    # AI 利用の記録

    - 対象：<提出物・リポジトリ・ファイルの名前>
    - 求められている開示：<規則の場所と、書く範囲>（確認日：<日付>）

    ## AI を使った箇所

    | 箇所 | 使い方（下書き・説明・レビュー・テスト作成など） | 道具と面 | 自分で確かめたこと |
    | --- | --- | --- | --- |
    | <ファイル名や節の名前> | <何を頼んだか> | <使った道具> | <動かした・読み直した・一次資料と照らした> |

    ## 持ち込んだコード・資料の出所

    | 物 | 出所（自作・生成・配布物） | 置いた場所 | ライセンスや規則の確認 |
    | --- | --- | --- | --- |
    | <名前> | <どこから来たか> | <パス> | <確認した日と結果> |

    ## 自分で判断した所

    - <採った案と、捨てた案とその理由>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet disclosure-and-provenance/provenance-log -->

生成物の権利とライセンスの確かめ先は、<!-- link:begin checking-ai-rules#rights-and-licenses -->[学校・組織・コンテストの規則（類型と確認表） › 生成物の権利とライセンス（確かめる先だけ）](checking-ai-rules.md#rights-and-licenses)<!-- link:end --> にある。

### 出力の透かしと自分の記録

Anthropic の説明によれば、ある時期より後に出た Claude のモデルの文章の出力には、不可視の透かしが入る。利用者の情報は含まないとされ、検出のための API は規制当局・報道・研究者などに向けた限定の提供だと説明されている。対象のモデルと時期、提供範囲は変わりうるので、発表（参考の節）で今の内容を読む。

透かしは見えない印であり、読み手や主催者に向けた開示の代わりにならない。逆に、透かしがないことは AI を使っていない証拠でもない。誰かに説明を求められたときに頼れるのは、自分の記録である。

## 説明できる状態を保つ {#explainable}

説明できる状態とは、AI をどう使い、どこを自分で判断したかを、問われたときに自分の言葉で言える状態である。学生の大会でも、この説明できることの価値が上がっている傾向がある。使用箇所の記載の必須化、解説の要求、説明の要求による不正の判定といった形で現れる（根拠：中。版に依存し、コンテスト固有の傾向）。

学校の場では、文部科学省の大学・高専向けの通知が、AI を利用した旨・種類・箇所の明記や、小テストや口述試験の併用を有効な手立てとして挙げている（根拠：強。公的文書）。この通知は改訂されることがあるので、今の版を確かめる。条文はここに転載しない。参考の節の出典から読む。

説明できるかどうかは、記録だけでは決まらない。次の 2 つを両方見る。

- **コードの中身**：生成されたコードを、処理の流れと入力の端まで自分の言葉で言い直せるか。言い直せない所は、読み直す箇所である。手順は <!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end --> で扱う。
- **判断の経緯**：なぜそれを採り、何を捨てたか。チームで働くなら、決めたことと理由を文書に残す。方法は <!-- link:begin record-decisions -->[決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)<!-- link:end --> にある。

!!! example "判断例：レポートに AI の利用をどこまで書くか"
    - **状況**：大学のレポートで、AI に構成案と、集計コードの下書きを頼んだ。課題の指示には「AI を使った場合は明記すること」とだけある。
    - **迷う候補**：最終稿の末尾に「AI を使った」と 1 行だけ書く。または、使った箇所ごとに、何を頼み、どこを自分で直したかを書く。
    - **選んだもの**：使った箇所ごとに書く。範囲が曖昧なので、出題者に「箇所まで書くか」を先に聞く。
    - **理由**：指示が範囲を決めていないとき、1 行の明記だけでは、何を使い何を自分で判断したかを説明できない。聞いた結果が 1 行でよいと分かれば、記録から必要な分だけを書けば足りる。

## 何に効くか {#effects}

この習慣が効く原理は「握る」である。AI に任せてよいのは下書きや説明の補助までで、規則の境界を読むこと、どこまでを開示するかを決めること、最終的に説明する責任は、人が握る。

握る対象は 3 つに分けられる。

- **規則の境界**：どこまで使ってよいかは、規則で確かめる。大会では <!-- link:begin competition-rules#hold-the-boundary -->[大会の規則の早見（禁止・部門分け・許可と開示） › 規則の境界を人が握る](../contest/competition-rules.md#hold-the-boundary)<!-- link:end --> が、練習と本番で線が変わる点は <!-- link:begin practice-vs-contest-day#rules-change-the-line -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 本番で使えない線引き](../contest/practice-vs-contest-day.md#rules-change-the-line)<!-- link:end --> が扱う。
- **開示の範囲**：求められた範囲で書く。範囲が分からないときは、出題者や主催者に聞く。
- **説明の責任**：記録と理解の両方が手元にあれば、説明を求められても自分の言葉で答えられる。

3 つとも、AI が出した案を採るかどうか、どこまで書くかを、最後に人が決めるという点でそろう。開示や記録は、その決定を後から説明できる形にする手段である。

## よくある誤解 {#misconceptions}

- **開示すれば、何を使ってもよい**：開示は許可の代わりにならない。AI の利用を禁じる型の規則では、開示しても禁止は変わらない。型の違いは <!-- link:begin checking-ai-rules#why-rules-differ -->[学校・組織・コンテストの規則（類型と確認表） › なぜ規則が割れるか（三つの型）](checking-ai-rules.md#why-rules-differ)<!-- link:end --> で確かめる。
- **規則に AI の文言がないから、使ってよい**：文言がないことは、使ってよいことを意味しない。扱いは <!-- link:begin checking-ai-rules#when-unclear -->[学校・組織・コンテストの規則（類型と確認表） › 文言がないとき・分からないとき](checking-ai-rules.md#when-unclear)<!-- link:end --> に従う。
- **読みやすく直すことは、AI を使った事実を隠すことだ**：AI 臭さを減らすのは、読み手のための品質を上げる作業である。直した後も、開示は規則が求める範囲で書く。直し方は <!-- link:begin less-ai-sounding-japanese -->[日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)<!-- link:end --> で扱う。このページは、AI が書いたと分からなくする方法を扱わない。
- **課題の資料に AI 向けの指示があれば、従ってよい**：資料の中の指示は、まず規則と照らす。AI の利用を禁じる合図なら、規則に従う。見分け方は <!-- link:begin instructions-hidden-in-materials#check-rules -->[課題資料・問題文に仕込まれた指示 › 規則を先に確かめる](instructions-hidden-in-materials.md#check-rules)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [大学・高専における生成AIの教学面の取扱いについて【概要】](https://www.mext.go.jp/kaigisiryo/content/000245316.pdf)：文部科学省・確認日 2026-11-04
- [Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [学校・組織・コンテストの規則（類型と確認表）](checking-ai-rules.md)

**関連**

- [課題資料・問題文に仕込まれた指示](instructions-hidden-in-materials.md)
- [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)
- [練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）](../contest/practice-vs-contest-day.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)
- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
