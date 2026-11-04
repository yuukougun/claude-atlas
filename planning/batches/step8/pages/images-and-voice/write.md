# write.md：images-and-voice

## 書いたファイル
- docs/prompting/images-and-voice.md（stubs から mv。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：sections（`why`・`limits` を足した。`images`・`voice` は不変）、sources（既存 id 5 つ：cc-docs-common-workflows・cc-docs-voice-dictation・cc-docs-commands・cc-docs-settings-reference・hc-voice-mode）、stage、updated
- snippets/images-and-voice/screenshot-request.{txt,expect.yaml}、spoken-brief.{txt,expect.yaml}（目次の templates は「なし」。分かりやすさのために 2 つ足した）
- data/sources.d/images-and-voice.yml は書いていない（出典は data/sources.yml の既存 id だけで足りた）

## 必ず持つものの対応
- どの原理に関わるか（principle「見せる」）：`why`（冒頭の1文で名指し）
- どの原因に関わるか（prevents「見えていない」）：`why`
- pitfalls：front matter に pitfalls がないので名指しなし（束にもない）
- level（整える）を持つ：front matter。要点の最初は「何が分かるか」
- 技法ページの構成：要点 → 頼み方の例（Before/After）`images`・`voice` → 何が変わるか `images`（After で足したもの）→ なぜ効くか `why` → 効かない場面・やりすぎ `limits` → 関連（テンプレート）

## メインに判断してほしいこと
- 判断例を 1 つ置いた（エラーは画像か文字か）。画像の貼り付けは Claude Code の公式（common-workflows）で確かめた手順だけ。アプリ側の画像添付の手順は束と取得で確かめられず、how-attachments-are-read へ回した
- 音声の既定のキー・録音の上限時間・版・成熟度の数値は本文に書かず、成熟度は `compare 面 成熟度` の目印で出した

## 提案
```yaml
frontmatter:
  - {id: images-and-voice, key: related, before: [visual-checks, how-attachments-are-read, voice-and-mobile, input-symbols, let-claude-ask], after: [visual-checks, how-attachments-are-read, voice-and-mobile, input-symbols, let-claude-ask, keep-replies-in-japanese], reason: "音声入力の言語は language の設定が決める。束の備考どおり、japanese の keep-replies-in-japanese の language-setting の節を指したい（束に指せる節がなく、本文では指せていない）"}
```
- 用語集：追加の提案なし

## 検査の結果
- 書き終えた後：エラー 0・警告 3。直した後：エラー 0・警告 2
- 残した警告：no-doubled-joshi「に」2 件（143 行・203 行）。文を言い換えれば消えるが、検査は 2 回までなので直していない

## 確かめていないこと
- スニペット 2 つは動作を確かめていない（雛形として載せた）
- Claude Code の音声入力は WSL・Linux 基準で、macOS・Windows ネイティブ・IDE 拡張の挙動は本文で「未確認」とした
- アプリの画像添付の手順、画像の読み取り精度（「小さな文字や色の差は読み違えうる」はページの summary に沿った書き方で、独立の根拠はない）
- 束 6.3（01 の画像貼り付け）は見つからなかったため、公式の common-workflows を 1 回取得して補った

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：2 回（voice-dictation、common-workflows）
