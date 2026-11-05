---
id: ai-usage-guidelines
title: 社内ガイドラインに書くこと
aliases: [AI 利用ポリシー, 生成 AI ガイドライン, AI 利用規程]
type: recipe
field: team
chapter: 導入と決まり
order: 10
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: [同意を根拠にする]
scenes: [チーム, 開発]
summary: チームの AI 利用の決まりに、データの区分・許す面とモード・レビューの責任・止まって相談する場面を書ける。書いた禁止はお願いにすぎないので、守らせたいものは設定で縛る。
signs:
  - {type: situation, text: チームで Claude を導入する}
  - {type: situation, text: チームの AI 利用のルールを書くことになった}
  - {type: goal, text: どのデータを AI に渡してよいか、チームで決めたい}
prerequisites: [checking-ai-rules, where-your-data-goes, request-vs-lock]
related: [paved-roads, entrusted-data, disclosure-and-provenance, protecting-secrets, permission-rules, managed-settings-enforcement, risk-tiered-approval, agreement-is-not-evidence, separate-roles, record-decisions, what-to-put-in-claude-md, org-managed-settings-and-mcp]
sources: [cc-docs-permissions]
volatility: 中
sections:
  - {title: 先に確かめること（規則・データの行方・お願いと鍵）, anchor: check-first}
  - {title: 書くこと（データの区分・面とモード・レビューの責任）, anchor: what-to-write}
  - {title: 任せてよい・止まって相談する・禁止, anchor: three-categories}
  - {title: 禁止は設定で縛る, anchor: lock-the-prohibitions}
  - {title: 確かめ方, anchor: how-to-check}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：チームの AI 利用の決まりに、データの区分・許す面とモード・レビューの責任・止まって相談する場面を書ける。
    - **いつ引くか**：チームで Claude を導入するとき、AI 利用のルールを書くことになったとき、どのデータを AI に渡してよいかをチームで決めたいとき。
    - **注意**：決まりに書いた禁止はお願いにすぎない。守らせたいものは設定で縛る。
    - **前提**：<!-- link:begin checking-ai-rules -->[学校・組織・コンテストの規則（類型と確認表）](../safety/checking-ai-rules.md)<!-- link:end -->・<!-- link:begin where-your-data-goes -->[送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)<!-- link:end -->・<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI 利用ポリシー・生成 AI ガイドライン・AI 利用規程
<!-- textlint-enable -->

社内ガイドラインに書くこととは、チームが Claude を使い始める段階で最初に決める 4 つの事柄である。渡してよいデータ、許す面とモード、レビューの責任、止まって相談する場面を指す。このページは、それを CLAUDE.md に載せる 3 区分の決まりとして書き、機械で判定できる禁止だけを設定へ移すまでの手順を示す。

## 先に確かめること（規則・データの行方・お願いと鍵） {#check-first}

決まりを書く前に、チームの外から与えられている条件を 3 つ確かめる。この順に確かめると、書いた後に条件とぶつかって書き直すことが減る。

1. **所属先の規則**：学校・組織・取引先の規則が、AI の利用を禁止・部門分け・許可と開示のどの型で定めているかを見る。規則に AI の文言がないことは、使ってよいことを意味しない。確かめ方は <!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](../safety/checking-ai-rules.md#checklist)<!-- link:end --> にある。
2. **データの行方**：送った会話やコードが学習に使われる条件と、残る期間は、プランの種類で変わる。個人のプランと商用のプランの区別は <!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](../safety/where-your-data-goes.md#consumer-vs-commercial)<!-- link:end --> で見る。
3. **お願いと鍵の区別**：CLAUDE.md の文は Claude が読んで判断するお願いで、例外が出うる。毎回必ず効かせたいものは、設定の鍵に移す。分け方は <!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end --> にある。

確かめ：この 3 つについて、チームの前提を 1 行ずつ書き出せれば、次へ進める。書けないものは、決まりの中で「不明、確認中」として残す。

## 書くこと（データの区分・面とモード・レビューの責任） {#what-to-write}

チームの決まりの土台になるのは、データの区分、許す面とモード、レビューの責任の 3 つである。この順に決める。前の項目が後の項目の前提になるためである。残る 1 つの、止まって相談する場面は、次の節で書く。

**1. データを区分に分ける。** データの区分は、チームが持つデータを、AI に渡したときの被害の大きさで 3〜4 段に分けたものである。区分は中身で決め、置き場所では決めない。

| 区分 | 中身の例 | 渡す先の条件 |
| --- | --- | --- |
| A：公開してよいもの | 公開済みのコード、公式の文書 | どの面でもよい |
| B：社内のもの | 社内のコード、設計の資料 | 利用が許可された面だけ |
| C：預かったもの | 顧客のデータ、NDA・規約の付いたデータ | 契約で扱いが決まっている面だけ |
| D：秘密 | API キー、認証情報、個人を特定できる情報 | 渡さない。置かない |

C の判断は <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end --> が詳しい。D の守り方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> が詳しい。区分を細かくしすぎると、誰も引かない表になる。迷うデータの置き場所（迷ったら 1 つ上の区分として扱う、など）を 1 行で決めておく。

確かめ：チームの実際のデータを 5 つ選び、どれもいずれかの区分に入れられる。入らないものは区分の定義を直す。

**2. 区分ごとに、許す面とモードを決める。** 面は、アプリ・Claude Code・API のどれを使ってよいかである。モードは、確認を省く度合いである。面ごとの注意は次のとおり。

=== "アプリ"

    会話に貼ったものがそのまま送られる面である。人が貼る内容は区分の判断を通らないので、D を貼らないことと、C を貼ってよいプランかどうかを決まりに書く。

=== "Claude Code"

    ファイルを読み、コマンドを実行する面である。作業ディレクトリにあるものは、貼らなくても読まれうる。許すモードを決め、確認を省くモードを使わせない場合は <!-- link:begin managed-settings-enforcement#disable-modes -->管理設定と組織の強制<!-- link:end --> で配布側から外す。

=== "API"

    自社のコードが何を送るかで決まる面である。送る内容を決めるのは人ではなくコードなので、区分の判断をコードの側に置く。クラウドで動く作業は <!-- link:begin entrusted-data#cloud-runs -->[預かったデータ・規約付きのデータを AI に渡してよいか › クラウドで動く作業に気をつける](../safety/entrusted-data.md#cloud-runs)<!-- link:end --> に気をつける。

確かめ：区分と面の表に空欄がない。空欄は「不可」か「要相談」で埋める。

**3. レビューの責任を決める。** レビューの責任は、変更に対して誰が最終の判断をするかである。AI のレビューは補助とし、唯一の、または最終の判定者にはしない。AI の承認は人の承認に数えない。段ごとの承認の数は <!-- link:begin risk-tiered-approval#three-tiers -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 三つの段と承認の数](risk-tiered-approval.md#three-tiers)<!-- link:end --> で決められる。

確かめ：どの変更にも、マージの判断をする人の役割が割り当てられている。AI の承認だけで通る道がない。

## 任せてよい・止まって相談する・禁止 {#three-categories}

決まりを 3 区分に分けて書くと、読む人（と Claude）が、迷ったときに引く先ができる。任せてよいものは、Claude が相談なしに進めてよい作業である。止まって相談するものは、実装の前に案と理由を出して人の返事を待つ作業である。禁止は、やらない作業である。

- **任せてよい**：失敗しても戻せ、区分 A・B のデータだけを触る作業を置く。
- **止まって相談する**：戻しにくい変更、人の判断が要る変更を置く。スキーマ変更、認証・課金、依存の追加が例になる。
- **禁止**：区分 D を読む・貼る、本番への直接の操作、共有ブランチの履歴を壊す操作を置く。

3 区分のどこに入れるかが迷う項目は、禁止にも任せてよいにも寄せず、止まって相談する側に置く。迷う項目を禁止に入れると、現場が回避し始める。禁止を増やす代わりに安全な道を作る考え方は <!-- link:begin paved-roads#defaults-over-attention -->[禁止ではなく安全な道を作る › 注意力に頼らない既定](paved-roads.md#defaults-over-attention)<!-- link:end --> にある。

!!! example "判断例：テストデータに本番のログを混ぜてよいか"
    - **状況**：再現テストを書くために、本番のログの一部を Claude に渡したい。
    - **迷う候補**：社内のログなので区分 B として任せてよい。顧客の識別子が混じりうるので止まって相談する。
    - **選んだもの**：止まって相談する。
    - **理由**：区分は置き場所ではなく中身で決まる。ログに顧客の識別子が入っていれば区分 C になり、渡せる面が契約のある面に限られるため。人が中身を見て、識別子を落としてから渡すか、渡さないかを決める。

次の雛形は、この 3 区分を CLAUDE.md の冒頭に置く形である。`<例：…>` の行は、自分のチームの内容に書き換えて使う。

<!-- gen:begin snippet ai-usage-guidelines/team-rules -->
<!-- textlint-disable -->

??? example "雛形：チームの AI 利用ルール（任せてよい・止まって相談する・禁止）"

    ```markdown
    ## AI 利用のルール

    ### 任せてよい
    - <例：テストの追加、リファクタリング、ドキュメントの下書き。変更は PR にまとめる>

    ### 実装前に止まって相談する
    - <例：データベースのスキーマ変更、認証・課金に関わる変更、依存パッケージの追加>
    - 相談では、案と理由を先に出し、人の返事を待ってから進める

    ### 禁止（ここに書くのはお願い。守らせるものは settings.json の deny ルールとフックで強制する）
    - <例：.env と secrets/ の中身を読む、会話に貼る>
    - <例：main への直接 push と強制 push>
    - <例：区分 C のデータ（顧客から預かったもの）を、契約のない面に渡す>

    ### 判断の根拠
    - Claude が同意したことは、正しさの根拠に数えない。テストの結果・差分・一次資料を根拠にする
    - AI のレビューは補助とする。マージの判断は人が持つ
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet ai-usage-guidelines/team-rules -->

雛形の最後の「判断の根拠」は、Claude が賛成したことを正しさの根拠にしない決まりである。理由は <!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end --> にある。役割を持ち回りで割り当てて守る方法は <!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](separate-roles.md#against-sycophancy)<!-- link:end --> にある。

## 禁止は設定で縛る {#lock-the-prohibitions}

CLAUDE.md に書いた禁止は、Claude が読んで判断するお願いである。例外を許さない禁止であっても、これだけでは毎回守られる保証がない。守らせたい禁止は、deny ルールかフックに移す。CLAUDE.md には、禁止の理由と、止まって相談する基準だけを残す。この分け方の土台は <!-- link:begin request-vs-lock#two-layers -->[お願いと鍵（決定論的か、非決定論的か） › 二層で書く](../basics/request-vs-lock.md#two-layers)<!-- link:end --> にある。

禁止を鍵に移す手順は次のとおり。

1. 禁止の項目を 1 つずつ見て、機械で判定できるかを決める。ファイルのパス、コマンドの形のように、当たる・当たらないが決まるものは機械で判定できる。「顧客に失礼な文面」のように、中身を読んで決めるものはできない。
2. 機械で判定できる項目を、deny ルールに書く。書き方と、ルールが効く範囲は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end --> にある。
3. 利用者の設定で外されたくないものは、管理設定で配る。優先の順番は <!-- link:begin managed-settings-enforcement#precedence -->管理設定と組織の強制<!-- link:end --> にある。
4. 機械で判定できない項目は、CLAUDE.md のお願いのまま残し、レビューで人が見る項目に回す。

次の雛形は、先の CLAUDE.md の禁止のうち、パスとコマンドで判定できるものを deny ルールにしたものである。CLAUDE.md の雛形と組にして置く。

<!-- gen:begin snippet ai-usage-guidelines/deny-prohibitions -->
<!-- textlint-disable -->

??? example "雛形：禁止のうち、機械で判定できるものを deny ルールにする設定"

    ```json
    {
      "permissions": {
        "deny": [
          "Read(./.env)",
          "Read(./.env.*)",
          "Read(./secrets/**)",
          "Bash(git push --force *)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet ai-usage-guidelines/deny-prohibitions -->

上の deny ルールの設定は、すべての経路を塞がない。Read の deny ルールは、Claude の読み取りの道具には効くが、Bash から起動する子プロセスには効かないことがある。この限界は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> が、補い方は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> が詳しい。公式の権限の文書は、末尾の参考にある。

## 確かめ方 {#how-to-check}

決まりが書けているかは、書いた人以外で確かめる。次の 3 つを見る。

- **新しい人が読めるか**：チームに入ったばかりの人が、決まりだけを読んで、手元のデータが渡してよい区分かどうかを答えられる。
- **鍵が効くか**：壊れても困らない作業用のリポジトリに偽の秘密を置き、禁止した操作を頼む。止められるかを観察する。偽の秘密の置き方は <!-- link:begin protecting-secrets#verify -->[秘密情報（.env・API キー）を守る › 偽の秘密で確かめる](../safety/protecting-secrets.md#verify)<!-- link:end --> にある。
- **お願いの行を過信していないか**：CLAUDE.md の禁止の各行に、対応する鍵があるか、鍵にできない理由が書いてある。

決まりを変えたときは、決めたことと理由を <!-- link:begin record-decisions -->[決定を文書に残す（ADR と週次アップデート）](record-decisions.md)<!-- link:end --> の形で残すと、なぜその決まりになったかを後から辿れる。

## 失敗したとき {#when-it-fails}

決まりを置いた後の失敗は、次の 3 つに振り分ける。

- **禁止したのに破られた**：その行が、お願いのままで鍵になっていない可能性がある。このページの「禁止は設定で縛る」の手順で、鍵に移せるかを見直す。deny ルールがあるのに破られたときは <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> で、パスの書き方が当たっているかを確かめる。
- **渡してはいけないデータが渡った**：手元の記録に残っている可能性がある。記録の扱いは <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](../safety/where-your-data-goes.md#local-transcripts)<!-- link:end --> が、秘密が貼られたときの初動は <!-- link:begin protecting-secrets#when-it-fails -->[秘密情報（.env・API キー）を守る › 効かなかったとき](../safety/protecting-secrets.md#when-it-fails)<!-- link:end --> が詳しい。
- **決まりと所属先の規則が食い違った**：規則の文言がないか曖昧なときの確かめ方は <!-- link:begin checking-ai-rules#when-unclear -->[学校・組織・コンテストの規則（類型と確認表） › 文言がないとき・分からないとき](../safety/checking-ai-rules.md#when-unclear)<!-- link:end --> にある。判断がつくまでは、止まって相談する側に倒す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [学校・組織・コンテストの規則（類型と確認表）](../safety/checking-ai-rules.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [禁止ではなく安全な道を作る](paved-roads.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](risk-tiered-approval.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [役割を分ける（書く人・承認する人・疑う人）](separate-roles.md)
- [決定を文書に残す（ADR と週次アップデート）](record-decisions.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
