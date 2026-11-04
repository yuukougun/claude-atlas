---
id: consistent-notation
title: 表記ゆれと漢字の開き
aliases: [表記の統一, 「サーバー」と「サーバ」, 用語集を渡す, 漢字をひらく, prh]
type: recipe
field: japanese
chapter: 文体と表記
order: 60
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる, 縛る]
prevents: [縛っていない, 見えていない]
scenes: [文章, 開発, チーム]
summary: 用語の表記と漢字を開く語を一覧にして渡し、機械で見つけられる揺れは辞書つきの lint で直させる。一覧は人が持つ正本から作り、指示と検査に同じものを使う。
signs:
  - {type: symptom, text: 漢字が多くて硬い文章になる}
  - {type: goal, text: 社内の用語集どおりの表記で書かせたい}
wave: 1
prerequisites: [align-japanese-output]
related: [inconsistent-japanese-style, consistent-politeness, textlint-hook, documents-in-japanese, less-ai-sounding-japanese, where-to-put-instructions, path-scoped-rules]
tracks: [project-instructions, claude-md]
sources: [jinrai-claude-japanese, cc-docs-memory, hc-projects-manage, cc-docs-features-overview-ja, hc-effort-settings, prh-readme]
volatility: 中
sections:
  - {title: 先に整える守り：指示だけに頼らない, anchor: guard}
  - {title: 表記の一覧（用語集）を作る, anchor: glossary}
  - {title: 漢字を開く語を決める, anchor: open-kanji}
  - {title: 一覧を指示と lint の両方に使う, anchor: single-source}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：表記の一覧を 1 つの正本にして、指示と prh の辞書の両方に使うと、機械で見つけられる揺れを減らせる。
    - **いつ引くか**：「サーバー」と「サーバ」が混ざる、漢字が多くて硬い文章になる、社内の用語集どおりに書かせたい、と感じたとき。
    - **前提**：<!-- link:begin align-japanese-output -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること](align-japanese-output.md)<!-- link:end -->

<!-- textlint-disable -->
別名：表記の統一・「サーバー」と「サーバ」・用語集を渡す・漢字をひらく・prh
<!-- textlint-enable -->

表記ゆれと漢字の開きは、用語の綴りと、漢字で書くかかなで書くかを、文書の中で 1 つに揃える作業である。Claude へ任せきりにすると、同じ文書の綴りが混ざったり、漢字の多い硬い文になったりすることがある。ここでは、揃えたい表記を一覧にして渡し、渡し切れない揺れは辞書つきの lint で見つけて直させる流れを組む。

## 先に整える守り：指示だけに頼らない {#guard}

表記の指示は、書いても毎回は守られない。指示の届く範囲と強制力には限りがある。そこで、揺れを見つける仕組みを、一覧を作る前に決めておく。お願いの層は <!-- link:begin align-japanese-output#request-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示](align-japanese-output.md#request-layer)<!-- link:end --> を見る。差し戻す層は <!-- link:begin align-japanese-output#lock-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 確かめて差し戻す層：フックと lint](align-japanese-output.md#lock-layer)<!-- link:end --> を見る。

この recipe の守りは 2 段である。

- 見せる：一覧を、毎回読まれる場所に置く。
- 縛る：同じ一覧から作った辞書で lint を回し、残った揺れを差し戻す。

lint が見つけられるのは、綴りの一致で拾える揺れだけである。語の選び方や文の調子は辞書では拾えない。文末の混在は <!-- link:begin consistent-politeness#lint -->[です・ます／だ・であるを揃える › 混在を lint で見つける](consistent-politeness.md#lint)<!-- link:end --> で扱う。縛る規則は少なく保つほうが回り続けるので、<!-- link:begin align-japanese-output#keep-few -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 縛る規則は少なく保つ](align-japanese-output.md#keep-few)<!-- link:end --> も見ておく。

## 表記の一覧（用語集）を作る {#glossary}

表記の一覧とは、使う表記・使わない表記・探す形（pattern）を、語ごとに 1 行で書いたファイルである。最初から全語を網羅せず、実際に揺れた語から始める。

1. 直近に Claude が書いた文書を読み、揺れている語を拾う。確かめ：同じ語が 2 通りの綴りで出ている箇所が 1 組以上見つかった。
2. 語ごとに、使う表記と使わない表記を決め、使わない表記を見つける pattern を書く。確かめ：使わない表記は pattern に当たり、使う表記は当たらない。
3. 一覧を 1 つのファイルにして、リポジトリや共有フォルダに置く。確かめ：揺れを直すときに開くファイルが、このほかにない。

次の雛形は、そのファイルの例である。`pattern` は prh が探す形で、`/…/` で囲むと正規表現になる。長音の有無のように、使う表記が使わない表記を含む語は、`(?!ー)` で除く。

<!-- gen:begin snippet consistent-notation/glossary -->
<!-- textlint-disable -->

??? example "雛形：表記の正本（用語集）"

    ```yaml
    # 表記の正本。人が持つのはこのファイルだけで、指示の一覧と prh の辞書はここから作る
    # use：使う表記　avoid：使わない表記　pattern：prh が探す形（/…/ は正規表現）
    spelling:
      - {use: サーバー, avoid: [サーバ], pattern: "/サーバ(?!ー)/"}
      - {use: ユーザー, avoid: [ユーザ], pattern: "/ユーザ(?!ー)/"}
      - {use: 問い合わせ, avoid: [問合せ, 問合わせ], pattern: "/問合(?:わ)?せ/"}
    # 漢字を開く語。一文字の語は部分一致で誤検出するので、語の単位で書く
    open:
      - {use: できる, avoid: [出来る], pattern: "/出来る/"}
      - {use: ください, avoid: [下さい], pattern: "/下さい/"}
      - {use: さまざま, avoid: [様々], pattern: "/様々/"}
      - {use: すべて, avoid: [全て], pattern: "/全て/"}
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-notation/glossary -->

公式の日本語版にも、表記が割れている語がある。割れた語は、自分たちで 1 つに決めて一覧に入れる。

<!-- textlint-disable prh -->
!!! example "判断例：公式の日本語版で割れている語の決め方"
    - **状況**：effort という語を、Claude Code の日本語版の文書は effort と書く。ヘルプセンターの日本語版は、努力レベルと書く。
    - **迷う候補**：Claude Code の文書に合わせる。ヘルプセンターの訳に合わせる。
    - **選んだもの**：読み手が主に触れる文書の表記を 1 つ選び、もう一方を「使わない表記」として一覧に入れる。
    - **理由**：どちらも公式の表記で、正しさでは決まらない。決めないと、Claude はその時々で混ぜる。決めた表記と理由を一覧に残せば、あとから見直せる。
<!-- textlint-enable prh -->

割れていない語は、公式の日本語版の多数派に合わせる。割れている語だけを自分で決めると、一覧が短く済む。この辞典も同じ方針で、plan mode・effort・allow ルール／ask ルール／deny ルールの 3 語だけを英語のまま書く。

## 漢字を開く語を決める {#open-kanji}

<!-- textlint-disable prh -->
漢字を開くとは、漢字で書ける語をかなで書くことである。たとえば「出来る」を「できる」、「下さい」を「ください」と書く。実践者の記事は、Claude の文章は漢字の比率が高くなりがちなので、開く規則を指示するとよいと書く（根拠：弱。単独の実践者の記事）。
<!-- textlint-enable prh -->

開く語は、方針の形容ではなく、語の一覧で渡す。「やわらかく書く」と頼むだけでは、どの語を開くかが決まらず、書くたびに変わりうる（推論・実践例なし）。

1. 読んで硬いと感じた箇所から、開きたい語を拾う。確かめ：拾った語が、すべて語の単位で書かれている。
2. 開く語を、表記を揃える語と同じ正本に入れる。使う表記がかな、使わない表記が漢字である。確かめ：同じファイルを開けば、綴りの語と開く語の両方が見える。
3. 一文字の漢字は入れない。prh は綴りの一致を探すので、「事」や「時」のような 1 文字は、「仕事」や「時間」の一部に当たって誤検出する。確かめ：pattern を、開きたい語を含む文に通して、他の語に当たっていない。

語の一覧で足りない硬さは、言い回しや語の選び方の問題である。自分の文章を手本にする方法は <!-- link:begin less-ai-sounding-japanese#own-writing -->[日本語の「AI 臭さ」を減らす › 自分の文章を手本にする](less-ai-sounding-japanese.md#own-writing)<!-- link:end -->、読みにくさの型を挙げて直させる方法は <!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](less-ai-sounding-japanese.md#patterns)<!-- link:end --> にある。

## 一覧を指示と lint の両方に使う {#single-source}

一覧の正本は 1 つだけにする。指示に貼る一覧と、prh の辞書は、正本から作る生成物であり、手で直さない。別々に育てると、指示と辞書で正しい綴りが食い違う。すると、指示に従って直した文を、lint が間違いとして差し戻す。

次のスクリプトは、正本を読んで、辞書と指示の一覧を作る。作る前に、使わない表記が pattern に当たることも確かめる。

<!-- gen:begin snippet consistent-notation/build-notation -->
<!-- textlint-disable -->

??? example "雛形：正本から prh の辞書と指示の一覧を作るスクリプト"

    ```python
    """glossary.yaml から、prh の辞書（prh.yml）と、指示に貼る一覧（notation-list.md）を作る。"""
    import json
    import re
    import sys
    from pathlib import Path

    import yaml

    here = Path(__file__).parent
    glossary = yaml.safe_load((here / "glossary.yaml").read_text(encoding="utf-8"))
    groups = {"spelling": "表記を揃える語", "open": "漢字を開く語"}

    # 正本の食い違いを先に見つける：使わない表記は pattern に当たり、使う表記は当たらないこと
    errors = []
    for group in groups:
        for t in glossary[group]:
            body = t["pattern"].strip("/")
            if re.search(body, t["use"]):
                errors.append(f"{t['use']}：使う表記が pattern に当たっている")
            for a in t["avoid"]:
                if not re.search(body, a):
                    errors.append(f"{a}：使わない表記が pattern に当たらない")
    if errors:
        sys.exit("\n".join(errors))


    def q(s):
        return json.dumps(s, ensure_ascii=False)


    prh = ["version: 1", "rules:"]
    lists = []
    for group, title in groups.items():
        lists.append(f"### {title}")
        for t in glossary[group]:
            prh.append(f"  - expected: {q(t['use'])}")
            prh.append(f"    pattern: {q(t['pattern'])}")
            prh.append("    specs:")
            for a in t["avoid"]:
                prh.append(f"      - from: {q(a)}")
                prh.append(f"        to: {q(t['use'])}")
            lists.append(f"- {t['use']}（{'・'.join(t['avoid'])} とは書かない）")
        lists.append("")

    (here / "prh.yml").write_text("\n".join(prh) + "\n", encoding="utf-8")
    (here / "notation-list.md").write_text("\n".join(lists), encoding="utf-8")
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-notation/build-notation -->

作った辞書は次のようになる。`specs` は、使わない表記がどう直るかの例で、辞書の読み込みの段階で確かめられる（prh の仕様）。この辞書のパスを textlint の設定で渡す方法は、<!-- link:begin textlint-hook#rules -->[textlint をフックで回す › どのルールを機械に任せるか](textlint-hook.md#rules)<!-- link:end --> にある。

<!-- gen:begin snippet consistent-notation/prh-dictionary -->
<!-- textlint-disable -->

??? example "雛形：正本から作った prh の辞書の例"

    ```yaml
    # glossary.yaml から build-notation.py が作った辞書。手で直さず、正本を直して作り直す
    version: 1
    rules:
      - expected: "サーバー"
        pattern: "/サーバ(?!ー)/"
        specs:
          - from: "サーバ"
            to: "サーバー"
      - expected: "ユーザー"
        pattern: "/ユーザ(?!ー)/"
        specs:
          - from: "ユーザ"
            to: "ユーザー"
      - expected: "問い合わせ"
        pattern: "/問合(?:わ)?せ/"
        specs:
          - from: "問合せ"
            to: "問い合わせ"
          - from: "問合わせ"
            to: "問い合わせ"
      - expected: "できる"
        pattern: "/出来る/"
        specs:
          - from: "出来る"
            to: "できる"
      - expected: "ください"
        pattern: "/下さい/"
        specs:
          - from: "下さい"
            to: "ください"
      - expected: "さまざま"
        pattern: "/様々/"
        specs:
          - from: "様々"
            to: "さまざま"
      - expected: "すべて"
        pattern: "/全て/"
        specs:
          - from: "全て"
            to: "すべて"
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-notation/prh-dictionary -->

指示に貼る一覧は、同じ正本から作った次の形になる。

<!-- gen:begin snippet consistent-notation/notation-instruction -->
<!-- textlint-disable -->

??? example "雛形：指示に貼る表記の一覧"

    ```markdown
    ## 表記の決まり

    文章を書くときは、次の表記に揃える。括弧の中は、使わない表記である。
    一覧にない語は、読みやすいほうを選んでよい。ただし、同じ文書の中では 1 つに揃える。

    ### 表記を揃える語
    - サーバー（サーバ とは書かない）
    - ユーザー（ユーザ とは書かない）
    - 問い合わせ（問合せ・問合わせ とは書かない）

    ### 漢字を開く語
    - できる（出来る とは書かない）
    - ください（下さい とは書かない）
    - さまざま（様々 とは書かない）
    - すべて（全て とは書かない）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-notation/notation-instruction -->

置き場所は面で変わる。

=== "アプリ"

    アプリには指示しかない（<!-- link:begin align-japanese-output#app -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › アプリには指示しかない](align-japanese-output.md#app)<!-- link:end -->）。プロジェクトの指示に、生成した一覧を貼る。実践者の記事も、表記のルールを明記するか、Projects のカスタム指示に登録する対策を挙げる。置き場所の選び方は <!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](../app/where-to-put-instructions.md#how-to-choose)<!-- link:end --> にある。

    アプリの中では lint が動かない。書かせた文章を手元の textlint に通すか、貼る前に目で確かめる。

=== "Claude Code"

    作業ディレクトリの根の `CLAUDE.md` に、生成した一覧を貼る。`CLAUDE.md` は、強制する設定ではなく文脈として扱われる。圧縮の後も残るのは根の `CLAUDE.md` で、入れ子の `CLAUDE.md` は要約に消え、必要になったときに読み直される。一覧は根に置く。

    縛るほうは、ファイルを書いた直後に textlint を走らせて、残った違反を Claude に返す。仕組みと設定は <!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](textlint-hook.md#post-tool-use)<!-- link:end --> にある。シェルで書いたファイルは拾えない場合があり、<!-- link:begin textlint-hook#gaps -->[textlint をフックで回す › 拾えない書き込み（シェルで書いたファイル）](textlint-hook.md#gaps)<!-- link:end --> で確かめる。

一覧が長くなると、毎回読まれる文脈を圧迫する。指示に貼るのは実際に揺れた語に絞る。領域ごとの規約は、触れたファイルに合わせて必要なときだけ読ませる方法もある（<!-- link:begin path-scoped-rules -->[.claude/rules と paths で必要なときだけ読ませる](../extend/path-scoped-rules.md)<!-- link:end -->）。ただし圧縮の後は、引き金のファイルを読むまで戻らない（<!-- link:begin path-scoped-rules#after-compaction -->[.claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期](../extend/path-scoped-rules.md#after-compaction)<!-- link:end -->）。

## 確かめ方 {#verify}

全体の確かめは 2 つある。

1. 辞書が壊れていないか。辞書の `specs` が通れば、使わない表記が使う表記へ直る形は保たれている。
2. 揃ったか。揺れの出やすい文章を、新しいセッションで書かせる。その文章を prh に通し、指摘の数を見る。一覧を渡す前の同じ依頼と比べる。ゼロにならなくてよく、減っていれば効いている。

lint が指摘しない揺れは、一覧に載せていない語である。新しい揺れを見つけたら、正本に 1 行足して、辞書と指示の一覧を作り直す。揺れに気づく場所は、レビューや読み返しである。

## 失敗したとき {#failure}

- 一覧を貼っても綴りは直らない：指示が読まれていない、または別の指示に埋もれている。原因を安く確かめる順は <!-- link:begin inconsistent-japanese-style#diagnosis -->[文体や表記が揃わない › 原因を安く確かめる順](../symptoms/inconsistent-japanese-style.md#diagnosis)<!-- link:end --> にある。
- lint が正しい綴りまで指摘する：pattern が他の語の一部に当たっている。語の単位に広げるか、`(?!ー)` のような除外を足す。固有名詞や引用の中の同じ綴りは、辞書側で除くか、その行を検査から外す。
- 文末のです・ますとだ・であるが混ざる：表記の辞書では拾えない。<!-- link:begin consistent-politeness -->[です・ます／だ・であるを揃える](consistent-politeness.md)<!-- link:end --> へ。
- 社内用語を使わせたい：用語の一覧を依頼に添える方法は <!-- link:begin documents-in-japanese#glossary -->[日本語の資料を読ませる・書かせる › 社内用語は一覧で渡す](documents-in-japanese.md#glossary)<!-- link:end --> にある。
- 揺れを直すたびに別の揺れが出る：原因は、一覧の長すぎか、指示と辞書の正本の分裂である。正本を 1 つにして、一覧を短く絞る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude日本語精度｜ChatGPT・Gemini比較と自然な出力のコツ](https://jinrai.co.jp/blog/2026/03/26/claude-japanese/)：仁頼・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)：Anthropic・英語・確認日 2026-11-04
- [Claude Code を拡張する](https://code.claude.com/docs/ja/features-overview)：Anthropic・確認日 2026-11-04
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)：Anthropic・英語・確認日 2026-11-04
- [prh（表記ゆれ・用語を校正するツール）](https://github.com/prh/prh)：prh・英語・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [日本語の出力を揃える：お願いで足りること、仕組みが要ること](align-japanese-output.md)

**関連**

- [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- [です・ます／だ・であるを揃える](consistent-politeness.md)
- [textlint をフックで回す](textlint-hook.md)
- [日本語の資料を読ませる・書かせる](documents-in-japanese.md)
- [日本語の「AI 臭さ」を減らす](less-ai-sounding-japanese.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- [.claude/rules と paths で必要なときだけ読ませる](../extend/path-scoped-rules.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
