# build-PK3：make_packet.py の直し

## 変えたこと
1. 束の「1. ページ」の末尾に、tools/gen/config.yml の hosts にあるページだけ「このページが持つ生成の目印」を足した（目印ごとに `gen:begin/end 名前` を置く・手で表を書かない、と card §9 のその行の説明）。hosts にないページは変わらない。card §9 に行がない名前（例 ledger-index）は「説明の行がない」と出す。
2. 材料の抜き出しの規則を直した（resolve_group）。

## 2 の見立て
原因は道具の規則。目次は「05 §3-5（…）と Inferences」と書いてあり、Inferences は §3 末尾の同名の節を指す。道具は §3-5 の中で Inferences を探し、なければ資料全体の最初の一致（§1 の 191 行）に落ちていた。語の印が手前の所の中で見つからないとき、手前の所を囲む見出しを内側から順に広げて探してから、全体に落ちるようにした。直した。why-hallucinations の 6.2 は 05 の 379〜390 行（§3 の Inferences。説明のしかた・たとえ）になった。目次の書き方は直さなくてよい。

## 試験
`uv run python -m unittest discover -s tests/tools -p 'test_make_packet.py'`：94 件 OK（新規 2 件。fixtures に tools/gen/config.yml と planning/guides/card.md を足した）。
試し：six-causes（causes）・reverse-index（signs symptom/goal/situation）に節が入り、tokens には入らない。

## メインに判断してほしいこと
- 直したあと 6.2 は節 §3 の Inferences（トークン・hallucination など全部のたとえ 1430 字）になる。このページに要る分より広いが、同じ資料の「他の話題」ではなく §3 の意図した節。
- 既存のほかのページでも、同様に語の印が全体の先頭へ落ちていた項目があれば束が変わる（--all で再生成して差を見るのはメイン）。
- card §9 に ledger-index の行がない。

## 道具の呼び出し
約 17 回。
