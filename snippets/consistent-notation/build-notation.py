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
