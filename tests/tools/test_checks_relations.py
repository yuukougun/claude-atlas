"""前提と関連の規則（tools/checks/relations.py）が、目次の検査（tools/check_catalog.py）と同じ中身であることの試験
（DR-16「同じ規則を二か所に作らない」。check_catalog.py は骨格の後に退くので、規則の正はこちらに移る）。

`uv run python -m unittest discover -s tests/tools` で動く。どれも、同じ目次を check_catalog.py と検査の層（目次の
モデル）の両方に当て、両方にある検査の指摘（検査の名前・ページの id・文）が同じになることを確かめる。

- 本物の目次（planning/catalog/）と、check_catalog.py の試験の置き場所（fixtures/small。まだない分野・まとめた候補・
  採らない候補がある）
- 乱択：同じ目次を両方で読み、同じ変更（前提・関連・routes・level・priority・type・signs・summary・wave・sections）を
  両方の読んだものに当ててから照らす（試験の置き場所と本物の目次で、それぞれ数百の変更）
- front matter：本物の目次の全ページを骨格の形（stubs/<field>/<id>.md）に書き出して検査の層に当てると、両方にある
  検査の指摘が、目次に当てたものと同じになる（行と置き場所のほかは同じ規則）
"""
from __future__ import annotations

import copy
import random
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
SMALL = Path(__file__).resolve().parent / "fixtures" / "small"

import check_catalog as cc  # noqa: E402
from checks import CATALOG, FRONT_MATTER, checks_for, load_context, run_checks  # noqa: E402
from lib.ledger import load_ledger  # noqa: E402
from lib.yamlio import to_jsonable  # noqa: E402

SHARED = {c.name for c in checks_for(CATALOG)} & {c.name for c in cc.CHECKS}
NEW_RULES = {c.name for c in checks_for(CATALOG)} - {c.name for c in cc.CHECKS}   # 検査の層で足した規則


def cc_findings(cat) -> set:
    """check_catalog.py の指摘（両方にある検査だけ）。同じ文の指摘は1件に数える（検査の層は同じ指摘をまとめる）。"""
    return {(i.check, i.page, i.message) for i in cc.run_checks(cat) if i.check in SHARED}


def layer_findings(ctx) -> set:
    return {(i.check, i.page, i.message) for i in run_checks(ctx) if i.check in SHARED}


def diff(a: set, b: set) -> str:
    only_a = sorted(a - b)
    only_b = sorted(b - a)
    return ("\ncheck_catalog.py だけ:\n  " + "\n  ".join(map(str, only_a)) +
            "\n検査の層だけ:\n  " + "\n  ".join(map(str, only_b)))


class TestSharedRules(unittest.TestCase):
    def test_shared_rules_are_listed(self):
        # check_catalog.py の前提と関連の規則は、検査の層にもある（目次だけの規則は除く）
        catalog_only = {"YAML", "形", "必須", "語彙", "id の書式", "分野とファイル名", "未処理の候補", "tracks の id",
                        "outdated_advice の id", "registry の候補", "registry にない id", "知らない項目", "章", "設定"}
        self.assertEqual({c.name for c in cc.CHECKS} - SHARED, catalog_only)
        self.assertEqual(NEW_RULES, {"平文の欄"})
        for c in checks_for(CATALOG):
            self.assertIn(FRONT_MATTER, c.targets, c.name)       # 同じ関数を front matter にも当てる
            sev = next(x.severity for x in cc.CHECKS if x.name == c.name) if c.name in SHARED else c.severity
            self.assertEqual(c.severity, sev, c.name)

    def test_real_catalog(self):
        cat = cc.load_catalog(REPO)
        ctx = load_context(REPO, CATALOG)
        a, b = cc_findings(cat), layer_findings(ctx)
        self.assertEqual(a, b, diff(a, b))

    def test_small_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "small"
            shutil.copytree(SMALL, root)
            a, b = cc_findings(cc.load_catalog(root)), layer_findings(load_context(root, CATALOG))
            self.assertEqual(a, b, diff(a, b))
            self.assertEqual(a, set())      # fixtures/small は指摘のない目次


class TestRandomEdits(unittest.TestCase):
    """同じ変更を、check_catalog.py の読んだものと検査の層の読んだものの両方に当てて照らす。"""

    def mutate(self, rng: random.Random, pages_a: dict, pages_b: dict, ids: list[str], extra_ids: list[str]) -> None:
        pid = rng.choice(sorted(pages_a))
        ra, rb = pages_a[pid].raw, pages_b[pid].raw
        pool = ids + extra_ids
        choice = rng.randrange(11)

        def refs(n):
            out = [rng.choice(pool) for _ in range(n)]
            return [x + ("#" + rng.choice(["diagnosis", "exit-codes", "nope", "by-stage"]) if rng.random() < 0.15 else "")
                    for x in out]
        if choice == 0:
            value = refs(rng.randrange(0, 6))
            key = "prerequisites"
        elif choice == 1:
            value = refs(rng.randrange(0, 4))
            key = "related"
        elif choice == 2:
            causes = ["見えていない", "縛っていない", "預けすぎる", "散らかっている", "知らない原因"]
            value = [{"cause": rng.choice(causes), "to": refs(rng.randrange(0, 5))} for _ in range(rng.randrange(0, 3))]
            key = "routes"
        elif choice == 3:
            value = rng.choice(["使う", "整える", "任せる", "仕組みにする", "回す", "", None])
            key = "level"
        elif choice == 4:
            value = rng.choice(["必須", "推奨", "任意"])
            key = "priority"
        elif choice == 5:
            value = rng.choice(["concept", "feature", "symptom", "guide", "hub", "recipe", "ledger"])
            key = "type"
        elif choice == 6:
            texts = ["CLAUDE.md に書いたのに守られない", "長い会話の途中から規則を無視し始める", "作った skill が使われない",
                     "　CLAUDE.md に書いたのに、守られない！", "`.env` を触らせたくない"]
            value = [{"type": rng.choice(["symptom", "goal", "situation"]), "text": rng.choice(texts)}
                     for _ in range(rng.randrange(0, 4))]
            key = "signs"
        elif choice == 7:
            value = rng.choice(["短い。", "とても長い要約。" * 20, "一つ目。二つ目。三つ目。", "このページで扱う。", "かっこ（。）の中。"])
            key = "summary"
        elif choice == 8:
            value = rng.choice([1, None, True])
            key = "wave"
        elif choice == 9:
            value = [{"title": "節", "anchor": rng.choice(["diagnosis", "exit-codes", "a"]),
                      "level": rng.choice(["使う", "回す", "整える"])} for _ in range(rng.randrange(0, 3))]
            key = "sections"
        else:
            value = [rng.choice(["claude-md", "hooks", "nope-feature"])] if rng.random() < 0.7 else []
            key = "tracks"
        for r in (ra, rb):
            if value is None:
                r.pop(key, None)
            else:
                r[key] = copy.deepcopy(value)

    def run_random(self, root: Path, rounds: int, edits: int, seed: int) -> None:
        cat = cc.load_catalog(root)
        ctx = load_context(root, CATALOG)
        pages_a = {p.id: p for p in cat.pages if p.id}
        pages_b = {p.id: p for p in ctx.pages if p.id}
        self.assertEqual(sorted(pages_a), sorted(pages_b))
        ids = sorted(pages_a)
        extra = sorted(set(cat.merged_ids) | set(cat.dropped_ids) | set(list(cat.candidates)[:20])) + ["no-such-page", ""]
        rng = random.Random(seed)
        seen: set[str] = set()
        for n in range(rounds):
            for _ in range(edits):
                self.mutate(rng, pages_a, pages_b, ids, extra)
            a, b = cc_findings(cat), layer_findings(ctx)
            self.assertEqual(a, b, f"{n} 回目" + diff(a, b))
            seen |= {c for c, _, _ in a}
        self.assertGreaterEqual(len(seen), 18, f"変更で出た検査が少ない（照らし合わせが空振りしている）: {sorted(seen)}")

    def test_random_edits_small(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "small"
            shutil.copytree(SMALL, root)
            self.run_random(root, rounds=40, edits=6, seed=20261104)

    def test_random_edits_real_catalog(self):
        self.run_random(REPO, rounds=12, edits=25, seed=1104)


class TestSameRulesOnFrontMatter(unittest.TestCase):
    """本物の目次の全ページを骨格の形で書き出し、front matter として検査の層に当てる。"""

    def test_skeleton_of_real_catalog(self):
        ledger = load_ledger(REPO)
        keys = ledger.catalog_keys()
        cat = cc.load_catalog(REPO)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(REPO / "schema", root / "schema")
            for f, ff in cat.files.items():
                for i, p in enumerate(ff.pages):
                    fm = {k: p.raw[k] for k in keys if k in p.raw}
                    fm.update(field=f, order=(i + 1) * 10, stage="stub", updated="2026-11-04")
                    if p.text("type") not in ("guide", "hub"):
                        fm["sources"] = []
                    path = root / "stubs" / f / f"{p.id}.md"
                    path.parent.mkdir(parents=True, exist_ok=True)
                    text = yaml.safe_dump(to_jsonable(fm), allow_unicode=True, sort_keys=False)
                    path.write_text(f"---\n{text}---\n", encoding="utf-8")
            ctx = load_context(root, FRONT_MATTER)
            got = layer_findings(ctx)
            want = cc_findings(cat)
            # 目次と front matter で文が違う検査（参照の解決の説明・機能の id の置き場所）は名前と id で照らす
            loose = {"参照", "機能の tracks", "入ってくる道"}
            self.assertEqual({x for x in got if x[0] not in loose}, {x for x in want if x[0] not in loose},
                             diff(want, got))
            self.assertEqual({(c, p) for c, p, _ in got if c in loose}, {(c, p) for c, p, _ in want if c in loose})
            # 形（page.schema.json）も通る（B2 の試験と同じ形で書き出した）
            self.assertEqual([i for i in run_checks(ctx) if i.check == "形"], [])


if __name__ == "__main__":
    unittest.main()
