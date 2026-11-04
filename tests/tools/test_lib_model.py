"""読む層の全体のモデル（tools/lib/model.py の Atlas）とグラフの部品（tools/lib/graph.py）の試験。
`uv run python -m unittest discover -s tests/tools` で動く。

試験の置き場所（fixtures/lib）の期限の日（design §9.2。手で数えた値）:
  request-vs-lock（reviewed）: ページ 2026-10-20（verified 10-01 と checked 10-20 の新しいほう）＋低 365 日 = 2027-10-20、
                              数値 sample-limit 2026-10-15＋中 90 日 = 2027-01-13 → 2027-01-13（数値）
  instructions-ignored（draft）: verified がないので数値だけ。sample-limit 2027-01-13、sample-default-effort 2026-10-10＋
                              既定の高 30 日 = 2026-11-09、tracks の sample-hooks 2026-10-12＋中 90 日 = 2027-01-10 → 2026-11-09
  how-to-use（draft）: 数値がないので期限の日はない
"""
from __future__ import annotations

import datetime
import itertools
import random
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "lib"
SMALL = Path(__file__).resolve().parent / "fixtures" / "small"

from lib import Atlas, load_atlas, load_catalog_atlas, load_site  # noqa: E402
from lib.base import Ref  # noqa: E402
from lib.graph import cycles, reachable, reverse, strongly_connected, topological_order  # noqa: E402

D = datetime.date


class AtlasCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "lib"
        shutil.copytree(FIXTURE, self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def replace(self, rel: str, old: str, new: str) -> None:
        p = self.root / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text)
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def atlas(self, **kw) -> Atlas:
        return load_atlas(self.root, **kw)


class TestAtlas(AtlasCase):
    def test_fixture(self):
        a = self.atlas()
        self.assertEqual(a.problems(), [])
        self.assertEqual(sorted(a.by_id), ["hooks-basics", "how-to-use", "instructions-ignored", "request-vs-lock"])
        self.assertEqual(a.duplicates, {})
        self.assertEqual([p.id for p in a.ordered()], ["how-to-use", "request-vs-lock", "hooks-basics", "instructions-ignored"])

    def test_resolve_and_anchors(self):
        a = self.atlas()
        self.assertEqual(a.resolve("hooks-basics#exit-codes").id, "hooks-basics")
        self.assertEqual(a.resolve(Ref.parse("request-vs-lock")).id, "request-vs-lock")
        self.assertIsNone(a.resolve("no-such-page"))
        self.assertTrue(a.anchor_ok("hooks-basics#exit-codes"))
        self.assertFalse(a.anchor_ok("hooks-basics#nothing"))
        self.assertIsNone(a.anchor_ok("hooks-basics"))
        self.assertIsNone(a.anchor_ok("no-such-page#x"))

    def test_graphs_and_order(self):
        a = self.atlas()
        self.assertEqual(a.prerequisite_graph(), {"request-vs-lock": [], "hooks-basics": ["request-vs-lock"],
                                                  "how-to-use": [], "instructions-ignored": ["request-vs-lock"]})
        self.assertEqual(a.route_graph(), {"instructions-ignored": ["hooks-basics"]})
        self.assertEqual(a.prerequisite_order(), ["how-to-use", "request-vs-lock", "hooks-basics", "instructions-ignored"])

    def test_duplicate_ids(self):
        p = self.root / "docs" / "start" / "copy.md"
        p.write_text((self.root / "docs" / "start" / "how-to-use.md").read_text(encoding="utf-8"), encoding="utf-8")
        a = self.atlas()
        self.assertEqual([x.file for x in a.duplicates["how-to-use"]],
                         ["docs/start/copy.md", "docs/start/how-to-use.md"])
        self.assertEqual(a.by_id["how-to-use"].file, "docs/start/copy.md")    # パスの順で最初のもの

    def test_published(self):
        a = self.atlas()
        self.assertEqual([p.id for p in a.published()], ["request-vs-lock", "how-to-use", "instructions-ignored"])
        self.assertFalse(a.is_published(a.by_id["hooks-basics"]))           # stubs/ の骨格のページは公開しない
        held = self.atlas(held_back=["how-to-use"])                          # 公開から外した試作のページ
        self.assertFalse(held.is_published(held.by_id["how-to-use"]))
        self.replace("schema/site.yml", "published_stages: [draft, reviewed, done]", "published_stages: [reviewed, done]")
        self.assertEqual([p.id for p in self.atlas().published()], ["request-vs-lock"])

    def test_publication_needs_both_place_and_stage(self):
        """docs/ にあっても stub なら、stubs/ にあれば draft でも公開しない（食い違いは検査の層が誤りにする）。"""
        self.replace("stubs/enforce/hooks-basics.md", "stage: stub", "stage: draft")
        self.replace("docs/start/how-to-use.md", "stage: draft", "stage: stub")
        a = self.atlas()
        self.assertFalse(a.is_published(a.by_id["hooks-basics"]))          # stubs/ にある draft
        self.assertFalse(a.is_published(a.by_id["how-to-use"]))            # docs/ にある stub
        self.assertEqual([p.id for p in a.published()], ["request-vs-lock", "instructions-ignored"])

    def test_docs_wins_over_stubs(self):
        p = self.root / "stubs" / "start" / "how-to-use.md"
        p.parent.mkdir(parents=True)
        p.write_text("---\nid: how-to-use\ntitle: 残った骨格\nstage: stub\n---\n", encoding="utf-8")
        a = self.atlas()
        self.assertEqual([x.file for x in a.duplicates["how-to-use"]], ["docs/start/how-to-use.md", "stubs/start/how-to-use.md"])
        self.assertEqual(a.by_id["how-to-use"].file, "docs/start/how-to-use.md")
        self.assertEqual(a.docs.duplicate_ids().keys(), a.duplicates.keys())

    def test_expiry(self):
        a = self.atlas()
        e = a.expiry(a.by_id["request-vs-lock"])
        self.assertEqual((e.date, e.by.what), (D(2027, 1, 13), "fact:sample-limit"))
        self.assertEqual([(d.what, d.date) for d in e.dues], [("fact:sample-limit", D(2027, 1, 13)),
                                                              ("page", D(2027, 10, 20))])
        self.assertEqual(e.dues[1].checked, D(2026, 10, 20))                # verified と checked の新しいほう
        e = a.expiry(a.by_id["instructions-ignored"])
        self.assertEqual((e.date, e.by.what, e.by.volatility), (D(2026, 11, 9), "fact:sample-default-effort", "高"))
        self.assertEqual([d.what for d in e.dues], ["fact:sample-default-effort", "feature:sample-hooks", "fact:sample-limit"])
        self.assertNotIn("page", [d.what for d in e.dues])                  # draft は verified がない
        self.assertTrue(e.expired(D(2026, 11, 10)))
        self.assertFalse(e.expired(D(2026, 11, 9)))
        e = a.expiry(a.by_id["how-to-use"])
        self.assertEqual((e.date, e.by, e.dues, e.missing), (None, None, (), ()))
        self.assertFalse(e.expired(D(2030, 1, 1)))

    def test_expiry_extra_and_missing(self):
        a = self.atlas()
        e = a.expiry(a.by_id["how-to-use"], extra_facts=["sample-limit", "no-such-fact"])
        self.assertEqual((e.date, e.missing), (D(2027, 1, 13), ("fact:no-such-fact",)))
        self.replace("data/facts.yml", "    checked: 2026-10-15\n", "    checked: 2026-13-15\n")
        self.replace("docs/basics/request-vs-lock.md", "volatility: 低", "volatility: 最低")
        a = self.atlas()
        e = a.expiry(a.by_id["request-vs-lock"])
        self.assertEqual((e.dues, e.missing), ((), ("page", "fact:sample-limit")))

    def test_default_fact_volatility(self):
        self.replace("schema/site.yml", "default_fact_volatility: 高", "default_fact_volatility: 中")
        a = self.atlas()
        e = a.expiry(a.by_id["instructions-ignored"])
        self.assertEqual((e.date, e.by.what), (D(2027, 1, 8), "fact:sample-default-effort"))

    def test_without_data(self):
        a = Atlas(load_site(self.root), self.atlas().pages)
        e = a.expiry(a.by_id["request-vs-lock"])
        self.assertEqual([d.what for d in e.dues], ["page"])


class TestCatalogAtlas(unittest.TestCase):
    def test_small_catalog(self):
        a = load_catalog_atlas(SMALL)
        self.assertEqual(a.problems(), [])
        page = a.by_id["instructions-ignored"]
        self.assertEqual(page.kind, "catalog")
        self.assertEqual([a.resolve(r).id for r in page.route_targets()],
                         ["outdated-advice-ledger", "hooks-basics", "permissions-deny"])
        self.assertTrue(a.anchor_ok("hooks-basics#exit-codes"))
        self.assertEqual(a.fact_ids(page), [])                               # 目次のページに本文はない
        self.assertFalse(a.is_published(page))                               # 目次のページに stage はない
        self.assertEqual([p.id for p in a.ordered()], [p.id for p in a.catalog.pages])

    def test_real_catalog_order_puts_prerequisites_first(self):
        a = load_catalog_atlas(REPO)
        order = a.prerequisite_order()
        self.assertEqual(sorted(order), sorted(a.by_id))
        pos = {pid: i for i, pid in enumerate(order)}
        graph = a.prerequisite_graph()
        self.assertEqual(cycles(graph), [])
        for pid, prereqs in graph.items():
            for q in prereqs:
                self.assertLess(pos[q], pos[pid], (q, pid))


# ---------------------------------------------------------------- グラフ


def random_graph(rng: random.Random, n: int, p: float) -> dict[str, list[str]]:
    nodes = [f"n{i}" for i in range(n)]
    return {u: [v for v in nodes if rng.random() < p] for u in nodes}


def brute_reach(graph: dict[str, list[str]], start: str) -> set[str]:
    seen, stack = set(), list(graph.get(start, ()))
    while stack:
        u = stack.pop()
        if u not in seen:
            seen.add(u)
            stack += graph.get(u, ())
    return seen


class TestGraph(unittest.TestCase):
    def test_strongly_connected_on_random_graphs(self):
        rng = random.Random(20261104)
        for _ in range(200):
            g = random_graph(rng, rng.randint(1, 9), rng.choice([0.1, 0.2, 0.35]))
            comps = strongly_connected(g)
            self.assertEqual(sorted(x for c in comps for x in c), sorted(g))
            where = {x: i for i, c in enumerate(comps) for x in c}
            for u, v in itertools.product(g, g):
                same = u == v or (v in brute_reach(g, u) and u in brute_reach(g, v))
                self.assertEqual(where[u] == where[v], same, (g, u, v))
            self.assertEqual(sorted(sorted(c) for c in cycles(g)),
                             sorted(sorted(c) for c in comps if len(c) > 1 or c[0] in g[c[0]]))

    def test_reachable(self):
        rng = random.Random(7)
        for _ in range(100):
            g = random_graph(rng, rng.randint(1, 8), 0.25)
            for u in g:
                self.assertEqual(reachable(g, [u]), brute_reach(g, u))

    def test_topological_order_on_random_dags(self):
        rng = random.Random(11)
        for _ in range(200):
            n = rng.randint(1, 9)
            nodes = [f"n{i}" for i in range(n)]
            order = nodes[:]
            rng.shuffle(order)
            g = {u: [v for v in nodes if nodes.index(v) < nodes.index(u) and rng.random() < 0.3] for u in nodes}
            out = topological_order(g, order)
            self.assertEqual(sorted(out), sorted(nodes))
            pos = {u: i for i, u in enumerate(out)}
            for u, vs in g.items():
                for v in vs:
                    self.assertLess(pos[v], pos[u])
            if not any(g.values()):
                self.assertEqual(out, order)                     # 前提がなければ order のまま

    def test_topological_order_details(self):
        g = {"a": ["b"], "b": [], "c": ["c"], "d": ["e"], "e": ["d"], "f": ["missing"]}
        out = topological_order(g, ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(out[:4], ["b", "a", "c", "f"])         # 自分への辺と、graph にない前提は数えない
        self.assertEqual(out[4:], ["d", "e"])                    # 循環は最後に order の順
        self.assertEqual(topological_order({"x": [], "y": []}), ["x", "y"])

    def test_reverse(self):
        self.assertEqual(reverse({"a": ["b", "b"], "b": [], "c": ["b"]}), {"a": [], "b": ["a", "c"], "c": []})


if __name__ == "__main__":
    unittest.main()
