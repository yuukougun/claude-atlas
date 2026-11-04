#!/usr/bin/env python3
"""Stop フック：最後の返事が英語なら、日本語で書き直させる。"""
import json
import os
import re
import sys

MIN_LATIN = 40       # 英字がこれより少ない短い返事は判定しない
MIN_JA_SHARE = 0.25  # 英字とかな・漢字のうち、かな・漢字の割合がこれ未満なら英語とみなす
REASON = (
    "直前の返答が日本語ではありません。内容は変えず、日本語で書き直してください。"
    "コード・コマンド・パス・エラーメッセージは原文のままでかまいません。"
)

if os.environ.get("ALLOW_ENGLISH_REPLY") == "1":    # 英語で答えさせる作業では判定を切る
    sys.exit(0)

try:
    data = json.loads(sys.stdin.buffer.read())
except ValueError:
    sys.exit(0)
if data.get("stop_hook_active"):                     # 書き直しの返事は判定しない（止め続けない）
    sys.exit(0)

text = data.get("last_assistant_message") or ""
text = re.sub(r"```.*?```", " ", text, flags=re.S)   # コードの塊
text = re.sub(r"`[^`]*`", " ", text)                 # インラインコード
text = re.sub(r"https?://\S+", " ", text)            # URL
text = re.sub(r"(?:[A-Za-z0-9_.~-]*/)+[A-Za-z0-9_.-]*", " ", text)  # パス
text = re.sub(r"(?m)^>.*$", " ", text)               # 引用

latin = len(re.findall(r"[A-Za-z]", text))
ja = len(re.findall(r"[ぁ-んァ-ヶー一-龠々ｦ-ﾟ]", text))   # かな・漢字
if latin >= MIN_LATIN and ja / (ja + latin) < MIN_JA_SHARE:
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"decision": "block", "reason": REASON}, ensure_ascii=False))
sys.exit(0)
