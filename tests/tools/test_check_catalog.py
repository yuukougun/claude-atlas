"""tools/check_catalog.py（目次の検査）の試験。python3 -m unittest discover -s tests/tools で動く。

fixtures/small/ は、エラーも警告も出ない小さな目次（schema/site.yml は本物の写し。ただし first_wave の named は
試験用のページにした。planning/catalog/README.md は道具が読むところの抜き書き。eval の分野のファイルはまだない形）。
各試験は、それを一時フォルダに写して1か所だけ変え、出るはずの指摘（検査の名前とページの id の組）だけが出ることを
確かめる。試験は検査ごとに書き、@covers で記録する（test_every_check_has_a_test が、登録したすべての検査に試験が
あることを確かめる）。

試験用の目次の症状のページの routes（catalog/README §4.4 の6）：instructions-ignored は 散らかっている → outdated-advice-ledger、
縛っていない → hooks-basics#exit-codes・permissions-deny。done-but-not-done（wave: 1 なし）は 確かめていない → hooks-basics。
"""
from __future__ import annotations

import contextlib
import io
import random
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / "tools" / "check_catalog.py"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "small"
sys.path.insert(0, str(REPO / "tools"))
import check_catalog as cc  # noqa: E402

COVERED: set[str] = set()
DELETE = object()
ALL_PAGES = ["how-to-use", "request-vs-lock", "completion-check", "fact-check", "hooks-basics", "permissions-deny",
             "parallel-sessions", "instructions-ignored", "done-but-not-done", "outdated-advice-ledger"]
LINE_RE = re.compile(r"^(エラー|警告): (planning/catalog|schema)/[a-z.]+(:\d+)?: \S+: \[[^\]]+\] \S.*$")


def covers(*names: str):
    """その試験が確かめる検査の名前を記録する。"""
    COVERED.update(names)
    return lambda func: func


def make_routes(*pairs: tuple[str, list[str]]) -> list[dict]:
    """routes の値を (cause, to) の組から作る。"""
    return [{"cause": cause, "to": list(to)} for cause, to in pairs]


II_ROUTES = (("散らかっている", ["outdated-advice-ledger"]),        # 試験用の目次の instructions-ignored の routes
             ("縛っていない", ["hooks-basics#exit-codes", "permissions-deny"]))


class CatalogCase(unittest.TestCase):
    """小さな目次を一時フォルダに写し、変えてから検査する。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "small"
        shutil.copytree(FIXTURE, self.root)
        self.catdir = self.root / "planning" / "catalog"

    def tearDown(self):
        self._tmp.cleanup()

    # ---- 目次を変える

    def path(self, name: str) -> Path:
        return self.root / "schema" / "site.yml" if name == "site.yml" else self.catdir / name

    def read(self, name: str):
        return yaml.safe_load(self.path(name).read_text(encoding="utf-8"))

    def write(self, name: str, data) -> None:
        text = data if isinstance(data, str) else yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
        self.path(name).write_text(text, encoding="utf-8")

    def edit(self, name: str, func) -> None:
        data = self.read(name)
        func(data)
        self.write(name, data)

    def edit_page(self, name: str, pid: str, **changes) -> None:
        def apply(data):
            page = next(p for p in data["pages"] if p.get("id") == pid)
            for key, value in changes.items():
                if value is DELETE:
                    page.pop(key, None)
                else:
                    page[key] = value
        self.edit(name, apply)

    def page(self, name: str, pid: str) -> dict:
        return next(p for p in self.read(name)["pages"] if p.get("id") == pid)

    def line_of(self, name: str, text: str) -> int:
        """ファイルの中で text を含む最初の行の番号（1 から）。"""
        lines = self.path(name).read_text(encoding="utf-8").splitlines()
        return next(n for n, line in enumerate(lines, 1) if text in line)

    def add_candidate(self, **entry) -> None:
        self.edit("registry.yaml", lambda d: d["pages"].append(entry))

    # ---- 検査する

    def issues(self) -> list[cc.Issue]:
        return cc.run_checks(cc.load_catalog(self.root))

    def assertFound(self, *expected: tuple[str, str]) -> list[cc.Issue]:
        """指摘の（検査の名前, ページの id）の組が、expected とちょうど同じであることを確かめる。"""
        issues = self.issues()
        got = sorted({(i.check, i.page) for i in issues})
        self.assertEqual(got, sorted(set(expected)), "\n" + "\n".join(cc.format_issue(i) for i in issues))
        return issues

    def run_cli(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cc.main(["--root", str(self.root), *args])
        return code, out.getvalue(), err.getvalue()


def only(issues: list[cc.Issue], check: str) -> list[cc.Issue]:
    return [i for i in issues if i.check == check]


class TestFixture(CatalogCase):
    def test_fixture_is_clean(self):
        self.assertFound()

    def test_reads_every_field_file(self):
        cat = cc.load_catalog(self.root)
        self.assertEqual([p.id for p in cat.pages], ALL_PAGES)   # site.yml の fields の順
        self.assertEqual(sorted(cat.files), ["basics", "changes", "delegate", "enforce", "start", "symptoms", "verify"])
        self.assertEqual(cat.by_id["instructions-ignored"].line, 4)   # pages の要素の始まりの行


class TestYaml(CatalogCase):
    @covers("YAML")
    def test_broken_yaml(self):
        self.write("symptoms.yaml", "field: symptoms\npages:\n  - id: [broken\n    title: x\n")
        # symptoms のページが読めないので、そこからしか指されていない parallel-sessions は入ってくる道を失う。
        # symptoms の候補を指す参照は「まだ確かめられない」になり、エラーにしない
        issues = self.assertFound(("YAML", "-"), ("入ってくる道", "parallel-sessions"))
        err = only(issues, "YAML")[0]
        self.assertEqual(err.severity, cc.ERROR)
        self.assertEqual(err.file, "planning/catalog/symptoms.yaml")
        self.assertIsNotNone(err.line)
        self.assertIn("YAML が読めない", err.message)

    @covers("YAML")
    def test_duplicate_key(self):
        text = self.path("basics.yaml").read_text(encoding="utf-8")
        self.write("basics.yaml", text.replace("    volatility: 低\n", "    volatility: 低\n    summary: 二つ目。\n"))
        issues = self.assertFound(("YAML", "-"))
        self.assertIn("「summary」が2回", issues[0].message)
        self.assertEqual(issues[0].line, self.line_of("basics.yaml", "summary: 二つ目。"))

    @covers("YAML")
    def test_broken_registry_is_shown_for_every_field(self):
        self.write("registry.yaml", "pages: [\n")
        issues = self.issues()
        err = only(issues, "YAML")
        self.assertEqual(len(err), 1)
        self.assertEqual(err[0].fields, cc.ALWAYS)
        self.assertIn(err[0], cc.select(issues, "symptoms"))


class TestShape(CatalogCase):
    @covers("形")
    def test_string_instead_of_list(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", aliases="指示を無視される")
        issues = self.assertFound(("形", "instructions-ignored"))
        self.assertIn("aliases をリスト", issues[0].message)

    @covers("形")
    def test_visual_must_be_a_mapping(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", visual="二層の図")
        self.assertFound(("形", "instructions-ignored"))

    @covers("形")
    def test_wave_must_be_1(self):
        self.edit_page("start.yaml", "how-to-use", wave=2)
        # start の核がなくなり、入口の分野のページに wave: 1 がないことにもなる
        self.assertFound(("形", "how-to-use"), ("wave", "-"), ("wave", "how-to-use"))

    @covers("形")
    def test_safety_must_be_bool(self):
        self.edit_page("enforce.yaml", "hooks-basics", templates=[{"name": "例", "kind": "hook", "safety": "yes"}])
        self.assertFound(("形", "hooks-basics"))

    @covers("形")
    def test_top_level_must_be_a_mapping(self):
        self.write("basics.yaml", "- request-vs-lock\n")
        # basics が読めないので、request-vs-lock への参照は「まだ確かめられない」になる
        self.assertFound(("形", "-"))

    @covers("形")
    def test_page_must_be_a_mapping(self):
        self.edit("basics.yaml", lambda d: d["pages"].append("oops"))
        issues = self.assertFound(("形", "-"))
        self.assertIn("pages の 2 番目", issues[0].message)


class TestRequired(CatalogCase):
    @covers("必須")
    def test_missing_summary(self):
        self.edit_page("basics.yaml", "request-vs-lock", summary=DELETE)
        self.assertFound(("必須", "request-vs-lock"))

    @covers("必須")
    def test_missing_level_depends_on_type(self):
        self.edit_page("basics.yaml", "request-vs-lock", level=DELETE)
        self.assertFound(("必須", "request-vs-lock"))

    @covers("必須")
    def test_page_without_id_is_named_by_position(self):
        self.edit_page("verify.yaml", "fact-check", id=DELETE)
        # fact-check は registry にないので、completion-check の related からの参照も解決しない
        self.assertFound(("必須", "(pages の 2 番目)"), ("参照", "completion-check"))

    @covers("必須")
    def test_missing_file_field(self):
        self.edit("symptoms.yaml", lambda d: d.pop("field"))
        self.assertFound(("必須", "-"))

    @covers("必須")
    def test_merged_without_into(self):
        self.edit("symptoms.yaml", lambda d: d["merged"][0].pop("into"))
        self.assertFound(("必須", "rules-not-followed"))

    @covers("必須")
    def test_section_without_anchor(self):
        self.edit_page("enforce.yaml", "hooks-basics", sections=[{"title": "終了コードで止める"}])
        self.assertFound(("必須", "hooks-basics"), ("参照", "instructions-ignored"))   # hooks-basics#exit-codes

    @covers("必須")
    def test_registry_entry_without_title(self):
        self.edit("registry.yaml", lambda d: d["pages"][0].pop("title"))
        self.assertFound(("必須", "how-to-use"))

    @covers("必須")
    def test_fields_without_level_from_site_yml(self):
        self.edit("site.yml", lambda d: d.update(fields_without_level=["basics"]))
        self.edit_page("basics.yaml", "request-vs-lock", level=DELETE)
        self.assertFound()


class TestVocab(CatalogCase):
    @covers("語彙")
    def test_unknown_type(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", type="symptomm")
        issues = self.assertFound(("語彙", "instructions-ignored"))
        self.assertEqual(issues[0].severity, cc.ERROR)
        self.assertIn("type の「symptomm」", issues[0].message)

    @covers("語彙")
    def test_unknown_value_in_a_list(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", surfaces=["claude-code", "cli"])
        self.assertFound(("語彙", "done-but-not-done"))

    @covers("語彙")
    def test_unknown_sign_type(self):
        def change(d):
            next(p for p in d["pages"] if p["id"] == "instructions-ignored")["signs"][1]["type"] = "problem"
        self.edit("symptoms.yaml", change)
        self.assertFound(("語彙", "instructions-ignored"), ("症状の signs", "instructions-ignored"))

    @covers("語彙")
    def test_unknown_visual_and_template_kind(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", visual={"kind": "anim", "text": "図"},
                       templates=[{"name": "例", "kind": "script", "safety": False}])
        issues = self.assertFound(("語彙", "instructions-ignored"))
        self.assertEqual(len(issues), 2)

    @covers("語彙")
    def test_unknown_scalar_values(self):
        self.edit_page("basics.yaml", "request-vs-lock", volatility="普通")
        self.edit_page("verify.yaml", "fact-check", priority="最優先")
        self.edit_page("delegate.yaml", "parallel-sessions", level="極める")
        self.edit_page("enforce.yaml", "hooks-basics", sections=[{"title": "節", "anchor": "exit-codes", "level": "達人"}])
        self.assertFound(("語彙", "request-vs-lock"), ("語彙", "fact-check"), ("語彙", "parallel-sessions"),
                         ("語彙", "hooks-basics"))

    @covers("語彙")
    def test_registry_values(self):
        self.edit("registry.yaml", lambda d: d["pages"][0].update(type="guidebook"))
        self.edit("registry.yaml", lambda d: d["pages"][-1].update(field="evals"))
        self.assertFound(("語彙", "how-to-use"), ("語彙", "verifier-basics"))

    @covers("語彙")
    def test_vocabulary_is_read_from_site_yml(self):
        self.edit("site.yml", lambda d: d["types"].append("tutorial"))
        self.edit_page("verify.yaml", "fact-check", type="tutorial")
        self.assertFound()
        self.edit("site.yml", lambda d: d["volatility_days"].pop("低"))
        self.assertFound(*[("語彙", p) for p in ("how-to-use", "request-vs-lock", "completion-check", "fact-check")])


class TestIdFormat(CatalogCase):
    @covers("id の書式")
    def test_bad_page_id(self):
        self.edit_page("verify.yaml", "fact-check", id="Fact_Check")
        self.edit_page("verify.yaml", "completion-check", related=["Fact_Check", "verifier-basics"])
        self.assertFound(("id の書式", "Fact_Check"))

    @covers("id の書式")
    def test_bad_anchor(self):
        self.edit_page("enforce.yaml", "hooks-basics", sections=[{"title": "節", "anchor": "Exit_Codes"}])
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(II_ROUTES[0], ("縛っていない", ["hooks-basics#Exit_Codes", "permissions-deny"])))
        self.assertFound(("id の書式", "hooks-basics"))

    @covers("id の書式")
    def test_bad_registry_id(self):
        self.add_candidate(id="Bad Id", field="eval", title="書式の悪い候補")
        self.assertFound(("id の書式", "Bad Id"))


class TestDuplicates(CatalogCase):
    @covers("id の重複")
    def test_same_page_id_in_two_fields(self):
        copy = dict(self.page("verify.yaml", "completion-check"), chapter="確かめ方")
        self.edit("symptoms.yaml", lambda d: d["pages"].append(copy))
        issues = self.assertFound(("id の重複", "completion-check"))
        self.assertEqual(issues[0].fields, frozenset({"symptoms", "verify"}))   # どちらの --field にも出る
        self.assertEqual(issues[0].file, "planning/catalog/symptoms.yaml")

    @covers("id の重複")
    def test_page_and_dropped(self):
        self.edit("symptoms.yaml", lambda d: d["dropped"].append({"id": "done-but-not-done", "reason": "x"}))
        self.assertFound(("id の重複", "done-but-not-done"))

    @covers("id の重複")
    def test_duplicate_anchor(self):
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       sections=[{"title": "一", "anchor": "diagnosis"}, {"title": "二", "anchor": "diagnosis"}])
        self.assertFound(("id の重複", "instructions-ignored"))

    @covers("id の重複")
    def test_duplicate_registry_id(self):
        self.add_candidate(id="hooks-basics", field="enforce", title="重複した候補")
        self.assertFound(("id の重複", "hooks-basics"))


class TestFieldNames(CatalogCase):
    @covers("分野とファイル名")
    def test_field_differs_from_file_name(self):
        self.edit("symptoms.yaml", lambda d: d.update(field="symptom"))
        self.assertFound(("分野とファイル名", "-"))

    @covers("分野とファイル名")
    def test_file_name_not_a_field(self):
        shutil.copy(self.path("changes.yaml"), self.path("change.yaml"))
        issues = self.assertFound(("分野とファイル名", "-"))
        self.assertEqual(issues[0].file, "planning/catalog/change.yaml")
        self.assertIn(issues[0], cc.select(issues, "verify"))   # どの分野の --field にも出す


class TestRefs(CatalogCase):
    @covers("参照")
    def test_missing_id(self):
        self.edit_page("verify.yaml", "fact-check", related=["no-such-page"])
        issues = self.assertFound(("参照", "fact-check"))
        self.assertIn("存在しない id", issues[0].message)

    @covers("参照")
    def test_empty_id(self):
        self.edit_page("start.yaml", "how-to-use", related=["instructions-ignored", "outdated-advice-ledger", ""])
        self.assertFound(("参照", "how-to-use"))

    @covers("参照")
    def test_missing_anchor(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", related=["instructions-ignored#nothing", "parallel-sessions"])
        issues = self.assertFound(("参照", "done-but-not-done"))
        self.assertIn("あるのは diagnosis", issues[0].message)

    @covers("参照")
    def test_anchor_to_page_without_sections(self):
        self.edit_page("start.yaml", "how-to-use", related=["instructions-ignored", "outdated-advice-ledger",
                                                            "request-vs-lock#why"])
        issues = self.assertFound(("参照", "how-to-use"))
        self.assertIn("sections がない", issues[0].message)

    @covers("参照")
    def test_ref_to_merged_candidate(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", related=["parallel-sessions", "rules-not-followed"])
        self.edit_page("symptoms.yaml", "instructions-ignored", related=["completion-check"])
        # instructions-ignored の related から外したので、done-but-not-done に入ってくる道がなくなる
        issues = self.assertFound(("参照", "done-but-not-done"), ("入ってくる道", "done-but-not-done"))
        self.assertIn("「instructions-ignored」にまとめた", only(issues, "参照")[0].message)

    @covers("参照")
    def test_ref_to_dropped_candidate(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       related=["instructions-ignored#diagnosis", "parallel-sessions", "old-candidate"])
        issues = self.assertFound(("参照", "done-but-not-done"))
        self.assertIn("dropped", issues[0].message)

    @covers("参照")
    def test_candidate_without_field_file_is_not_flagged(self):
        self.edit_page("verify.yaml", "completion-check", related=["fact-check", "verifier-basics#metrics"])
        self.assertFound()

    @covers("参照")
    def test_merged_into_missing(self):
        self.edit("symptoms.yaml", lambda d: d["merged"][0].update(into="no-such-page"))
        self.assertFound(("参照", "rules-not-followed"))


class TestUnprocessed(CatalogCase):
    @covers("未処理の候補", "registry の候補")
    def test_candidate_missing_from_existing_field_file(self):
        self.add_candidate(id="secret-scan", field="enforce", title="秘密を探す", type="feature", priority="推奨")
        self.edit_page("enforce.yaml", "permissions-deny", related=["hooks-basics", "secret-scan"])
        issues = self.assertFound(("registry の候補", "secret-scan"), ("未処理の候補", "permissions-deny"))
        for i in issues:
            self.assertEqual(i.severity, cc.WARNING)
            self.assertIn("enforce", i.fields)


class TestRefStyle(CatalogCase):
    @covers("参照の書き方")
    def test_anchor_in_prerequisites(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", prerequisites=["request-vs-lock#why"])
        self.assertFound(("参照の書き方", "instructions-ignored"))

    @covers("参照の書き方")
    def test_self_in_related(self):
        self.edit_page("verify.yaml", "fact-check", related=["fact-check"])
        self.assertFound(("参照の書き方", "fact-check"))


class TestCycles(CatalogCase):
    @covers("循環")
    def test_two_page_cycle(self):
        self.edit_page("basics.yaml", "request-vs-lock", prerequisites=["instructions-ignored"])
        issues = self.assertFound(("循環", "request-vs-lock"))
        self.assertIn("request-vs-lock → instructions-ignored → request-vs-lock", issues[0].message)
        self.assertEqual(issues[0].fields, frozenset({"basics", "symptoms"}))

    @covers("循環")
    def test_three_page_cycle_is_reported_once(self):
        self.edit_page("basics.yaml", "request-vs-lock", prerequisites=["completion-check"])
        self.edit_page("verify.yaml", "completion-check", prerequisites=["instructions-ignored"])
        issues = self.assertFound(("循環", "request-vs-lock"))
        self.assertEqual(len(issues), 1)
        self.assertIn("request-vs-lock → completion-check → instructions-ignored → request-vs-lock", issues[0].message)

    @covers("循環")
    def test_self_prerequisite(self):
        self.edit_page("verify.yaml", "fact-check", prerequisites=["completion-check", "fact-check"])
        self.assertFound(("循環", "fact-check"))


class TestGraph(unittest.TestCase):
    def test_strongly_connected_and_cycles_on_random_graphs(self):
        rnd = random.Random(20261104)
        for _ in range(300):
            nodes = [f"p{i}" for i in range(rnd.randint(1, 9))]
            graph = {u: [v for v in nodes if rnd.random() < 0.25] for u in nodes}
            reach = {u: {u} | set(graph[u]) for u in nodes}
            for k in nodes:          # 推移閉包（Floyd–Warshall）
                for u in nodes:
                    if k in reach[u]:
                        reach[u] |= reach[k]
            expected = {frozenset(v for v in nodes if v in reach[u] and u in reach[v]) for u in nodes}
            comps = cc.strongly_connected(graph)
            self.assertEqual({frozenset(c) for c in comps}, expected, graph)
            for comp in comps:
                if len(comp) == 1 and comp[0] not in graph[comp[0]]:
                    continue
                cycle = cc.cycle_through(graph, comp[0], set(comp))
                self.assertEqual(cycle[0], comp[0])
                for u, v in zip(cycle, cycle[1:] + cycle[:1]):
                    self.assertIn(v, graph[u], (graph, cycle))

    def test_reached_from_on_random_graphs(self):
        """推移的な前提の検査がたどる部分。循環のあるグラフでも止まり、届く id と最短の道が総当たりと合う。
        avoid は通らない。グラフのキーにない id（ファイルのまだない分野の候補）には届くが、その先はたどらない。"""
        rnd = random.Random(20261105)
        for _ in range(300):
            nodes = [f"p{i}" for i in range(rnd.randint(1, 9))]
            pool = nodes + ["leaf-1", "leaf-2"]
            graph = {u: [v for v in pool if rnd.random() < 0.3] for u in nodes}
            for start in nodes:
                avoid = rnd.choice([None, *[v for v in nodes if v != start]])
                dist = {start: 0}        # 総当たり（すべての辺で緩和を繰り返す）
                for _ in pool:
                    for u in list(dist):
                        for v in graph.get(u, ()):
                            if v != avoid and dist.get(v, len(pool) + 1) > dist[u] + 1:
                                dist[v] = dist[u] + 1
                parent = cc.reached_from(graph, start, avoid)
                self.assertEqual(set(parent), set(dist), (graph, start, avoid))
                for v in parent:
                    path = cc.path_to(parent, v)
                    self.assertEqual((path[0], path[-1], len(path) - 1), (start, v, dist[v]), (graph, path))
                    self.assertNotIn(avoid, path)
                    for a, b in zip(path, path[1:]):
                        self.assertIn(b, graph[a], (graph, path))


class TestOverlap(CatalogCase):
    @covers("前提と関連の重複")
    def test_same_page_in_prerequisites_and_related(self):
        self.edit_page("enforce.yaml", "hooks-basics", related=["permissions-deny", "request-vs-lock"])
        self.assertFound(("前提と関連の重複", "hooks-basics"))

    @covers("前提と関連の重複")
    def test_twice_in_related(self):
        self.edit_page("enforce.yaml", "permissions-deny", related=["hooks-basics", "hooks-basics"])
        self.assertFound(("前提と関連の重複", "permissions-deny"))

    @covers("前提と関連の重複")
    def test_page_and_its_section_in_related_are_not_duplicates(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       related=["instructions-ignored#diagnosis", "instructions-ignored", "parallel-sessions"])
        self.assertFound()


class TestLevels(CatalogCase):
    @covers("レベルの逆転")
    def test_prerequisite_above_the_page(self):
        self.edit_page("verify.yaml", "fact-check", prerequisites=["completion-check", "hooks-basics"])
        issues = self.assertFound(("レベルの逆転", "fact-check"))
        self.assertIn("仕組みにする", issues[0].message)

    @covers("level の付け方")
    def test_level_on_a_type_without_level(self):
        self.edit_page("start.yaml", "how-to-use", level="整える")
        self.assertFound(("level の付け方", "how-to-use"))

    @covers("level の付け方")
    def test_section_level_below_the_page(self):
        self.edit_page("enforce.yaml", "hooks-basics", sections=[{"title": "節", "anchor": "exit-codes", "level": "整える"}])
        self.assertFound(("level の付け方", "hooks-basics"))

    @covers("level の付け方")
    def test_level_in_a_field_without_level(self):
        self.edit("site.yml", lambda d: d.update(fields_without_level=["basics"]))
        self.assertFound(("level の付け方", "request-vs-lock"))


class TestPriority(CatalogCase):
    @covers("必須の前提")
    def test_required_page_with_recommended_prerequisite(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", prerequisites=["request-vs-lock", "fact-check"])
        issues = self.assertFound(("必須の前提", "instructions-ignored"))
        self.assertEqual(issues[0].fields, frozenset({"symptoms", "verify"}))


class TestTransitivePrerequisites(CatalogCase):
    @covers("推移的な前提")
    def test_reached_through_another_prerequisite(self):
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=["fact-check", "completion-check"])
        issues = self.assertFound(("推移的な前提", "parallel-sessions"))
        self.assertEqual(issues[0].severity, cc.WARNING)
        self.assertEqual(issues[0].message, "前提「completion-check」は、ほかの前提「fact-check」からたどって届く: "
                                            "fact-check → completion-check（推移的に届く前提は書かない。要るなら related に移す）")
        self.assertEqual(issues[0].fields, frozenset({"delegate"}))   # 直すのは、このページの prerequisites
        self.assertRegex(cc.format_issue(issues[0]), LINE_RE)

    @covers("推移的な前提")
    def test_path_over_pages_from_two_prerequisites(self):
        self.edit_page("verify.yaml", "completion-check", prerequisites=["request-vs-lock"])
        self.edit_page("delegate.yaml", "parallel-sessions",
                       prerequisites=["fact-check", "done-but-not-done", "request-vs-lock"])
        issues = self.assertFound(("推移的な前提", "parallel-sessions"))
        self.assertEqual(len(issues), 1)   # fact-check と done-but-not-done は互いに届かない
        self.assertIn("前提「request-vs-lock」は、ほかの前提「fact-check」「done-but-not-done」からたどって届く: "
                      "fact-check → completion-check → request-vs-lock、"
                      "done-but-not-done → completion-check → request-vs-lock（", issues[0].message)

    @covers("推移的な前提")
    def test_anchor_is_compared_by_page_id(self):
        self.edit_page("verify.yaml", "fact-check", prerequisites=["completion-check#criteria"])
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=["fact-check", "completion-check#criteria"])
        issues = self.assertFound(("参照の書き方", "fact-check"), ("参照の書き方", "parallel-sessions"),
                                  ("推移的な前提", "parallel-sessions"))
        self.assertIn("前提「completion-check」は、ほかの前提「fact-check」から", only(issues, "推移的な前提")[0].message)

    @covers("推移的な前提")
    def test_prerequisites_that_do_not_reach_each_other(self):
        # hooks-basics と permissions-deny は同じ request-vs-lock を前提にするが、互いには届かない。
        # related は見ない（fact-check から届く completion-check を related に置くのはよい）
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=["hooks-basics", "permissions-deny", "fact-check"],
                       related=["completion-check"])
        self.assertFound()

    @covers("推移的な前提")
    def test_cycle_does_not_stop_the_check(self):
        self.edit_page("basics.yaml", "request-vs-lock", prerequisites=["instructions-ignored"])
        self.edit_page("enforce.yaml", "hooks-basics", prerequisites=["request-vs-lock", "instructions-ignored"])
        issues = self.assertFound(("循環", "request-vs-lock"), ("推移的な前提", "hooks-basics"))
        self.assertEqual(len(only(issues, "推移的な前提")), 2)   # 循環の中の2ページは、互いに届く

    @covers("推移的な前提")
    def test_path_through_the_page_itself_is_not_counted(self):
        # request-vs-lock → instructions-ignored → request-vs-lock の循環。instructions-ignored から completion-check へは
        # request-vs-lock 自身を通らないと届かないので、推移的な前提にしない（循環のエラーだけが出る）
        self.edit_page("basics.yaml", "request-vs-lock", prerequisites=["instructions-ignored", "completion-check"])
        self.assertFound(("循環", "request-vs-lock"))

    @covers("推移的な前提")
    def test_candidate_without_field_file(self):
        # eval のファイルはまだないが、completion-check の前提に verifier-basics と書いてあるので届く
        self.edit_page("verify.yaml", "completion-check", prerequisites=["verifier-basics"], related=["fact-check"])
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=["completion-check", "verifier-basics"])
        issues = self.assertFound(("推移的な前提", "done-but-not-done"))
        self.assertIn("completion-check → verifier-basics", issues[0].message)


class TestProportional(CatalogCase):
    @covers("比例則")
    def test_delegating_page_without_guard(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=["request-vs-lock"])
        self.assertFound(("比例則", "done-but-not-done"))

    @covers("比例則")
    def test_pages_in_guard_fields_are_exempt(self):
        self.edit_page("enforce.yaml", "hooks-basics", related=[])
        self.assertFound()

    @covers("比例則")
    def test_candidate_of_a_guard_field_counts(self):
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=[], related=["verifier-basics"])
        self.assertFound()   # eval のファイルはまだないが、registry で eval の候補なので比例則を満たす

    @covers("比例則")
    def test_levels_and_guards_come_from_site_yml(self):
        self.edit("site.yml", lambda d: d["proportional_rule"].update(levels=["整える"]))
        self.assertFound(("比例則", "request-vs-lock"))


class TestIncoming(CatalogCase):
    @covers("入ってくる道")
    def test_page_without_incoming(self):
        self.edit_page("verify.yaml", "completion-check", related=["verifier-basics"])
        self.assertFound(("入ってくる道", "fact-check"))

    @covers("入ってくる道")
    def test_entry_field_is_exempt_and_read_from_site_yml(self):
        cat = cc.load_catalog(self.root)
        self.assertFalse(any(r.target == "how-to-use" for p in cat.pages for _, r in cc.page_refs(p)))
        self.assertFound()   # start の how-to-use は、どこからも指されなくてよい
        self.edit("site.yml", lambda d: d.update(entry_fields=["changes"]))
        self.assertFound(("入ってくる道", "how-to-use"))


class TestSummary(CatalogCase):
    @covers("summary")
    def test_length(self):
        self.edit_page("basics.yaml", "request-vs-lock", summary="あ" * 119 + "。")
        self.assertFound()
        self.edit_page("basics.yaml", "request-vs-lock", summary="あ" * 120 + "。")
        issues = self.assertFound(("summary", "request-vs-lock"))
        self.assertIn("121 字", issues[0].message)

    @covers("summary")
    def test_banned_word(self):
        self.edit_page("basics.yaml", "request-vs-lock", summary="お願いと鍵の違いを扱う。")
        issues = self.assertFound(("summary", "request-vs-lock"))
        self.assertIn("「扱う」", issues[0].message)

    @covers("summary")
    def test_sentences(self):
        self.edit_page("basics.yaml", "request-vs-lock", summary="「一。二。」と言う。違いが分かる。")
        self.assertFound()
        self.edit_page("basics.yaml", "request-vs-lock", summary="一つ目。二つ目。三つ目")
        self.assertFound(("summary", "request-vs-lock"))

    @covers("summary")
    def test_rules_come_from_site_yml(self):
        self.edit("site.yml", lambda d: d.update(summary_max_chars=10, summary_banned_words=["鍵"]))
        issues = self.assertFound(*[("summary", p) for p in ALL_PAGES])
        self.assertEqual(len([i for i in issues if "使わない語" in i.message]), 1)   # request-vs-lock だけ


class TestSymptomAndFeature(CatalogCase):
    @covers("症状の signs")
    def test_one_symptom_sign(self):
        def change(d):
            page = next(p for p in d["pages"] if p["id"] == "done-but-not-done")
            page["signs"] = page["signs"][:1]
        self.edit("symptoms.yaml", change)
        self.assertFound(("症状の signs", "done-but-not-done"))

    @covers("症状の signs")
    def test_goal_signs_do_not_count(self):
        def change(d):
            next(p for p in d["pages"] if p["id"] == "done-but-not-done")["signs"][0]["type"] = "goal"
        self.edit("symptoms.yaml", change)
        self.assertFound(("症状の signs", "done-but-not-done"))

    @covers("症状の prevents")
    def test_empty_prevents(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", prevents=[])
        self.assertFound(("症状の prevents", "done-but-not-done"))

    @covers("機能の tracks")
    def test_feature_without_tracks(self):
        self.edit_page("enforce.yaml", "hooks-basics", tracks=[])
        self.assertFound(("機能の tracks", "hooks-basics"))


class TestReverseIndexOverlap(CatalogCase):
    """試験用の目次の症状のページの signs：instructions-ignored「CLAUDE.md に書いたのに守られない」「長い会話の途中から
    規則を無視し始める」、done-but-not-done「完了と言うのにテストが通らない」「直したと言うのに同じ不具合が出る」。"""

    def add_signs(self, name: str, pid: str, *signs: tuple[str, str]) -> None:
        have = self.page(name, pid).get("signs") or []
        self.edit_page(name, pid, signs=have + [{"type": t, "text": x} for t, x in signs])

    @covers("逆引きの重複")
    def test_symptom_sentence_on_another_page(self):
        self.add_signs("enforce.yaml", "hooks-basics", ("symptom", "CLAUDE.md に書いたのに守られない"))
        issues = self.assertFound(("逆引きの重複", "hooks-basics"))
        i = issues[0]
        self.assertEqual(i.severity, cc.WARNING)
        self.assertEqual(i.message, "signs の「CLAUDE.md に書いたのに守られない」が、症状のページ instructions-ignored の sign"
                                    "「CLAUDE.md に書いたのに守られない」と同じ（逆引きで同じ困りごとが二か所に出る。対処のページには、"
                                    "より狭い場面の困りごとか、やりたいことの形で置く）")
        self.assertEqual(i.fields, frozenset({"enforce", "symptoms"}))   # どちらの分野の --field にも出る
        self.assertNotIn(i, cc.select(issues, "verify"))
        self.assertRegex(cc.format_issue(i), LINE_RE)

    @covers("逆引きの重複")
    def test_spaces_and_symbols_are_ignored(self):
        self.add_signs("verify.yaml", "completion-check", ("goal", "（完了）と言うのに、テストが 通らない！"))
        issues = self.assertFound(("逆引きの重複", "completion-check"))   # signs の type は問わない
        self.assertIn("「（完了）と言うのに、テストが 通らない！」が、症状のページ done-but-not-done の sign"
                      "「完了と言うのにテストが通らない」と、空白と記号を除くと同じ", issues[0].message)

    def test_sign_key(self):
        base = cc.sign_key("完了と言うのにテストが通らない")
        self.assertEqual(base, "完了と言うのにテストが通らない")
        for ch in "「」『』、。・,.!?！？（）() 　\t\n":     # 指示の例の記号と、半角・全角の空白
            self.assertEqual(cc.sign_key(f"{ch}完了と{ch}言うのにテストが通らない{ch}"), base, repr(ch))
        self.assertEqual(cc.sign_key("ＣＬＡＵＤＥ．ｍｄ が効かない"), cc.sign_key("CLAUDE.md が効かない"))   # 全角と半角
        self.assertEqual(cc.sign_key("人々のコード"), "人々のコード")   # 踊り字と長音は文字として残す
        self.assertNotEqual(cc.sign_key("完了と言うのにテストが落ちる"), base)

    @covers("逆引きの重複")
    def test_narrower_sentences_and_non_symptom_pages_are_fine(self):
        # 対処のページには、より狭い場面の困りごとや goal を置く（README §4.5 の4 の例）。症状のページでない
        # ページどうしで同じ文をそろえるのはよい（逆引きで1項目に並ぶ）
        self.add_signs("enforce.yaml", "hooks-basics", ("symptom", "CLAUDE.md に書いた禁止が破られる"),
                       ("goal", "危ないコマンドを確実に止めたい"))
        self.add_signs("enforce.yaml", "permissions-deny", ("goal", "危ないコマンドを確実に止めたい"))
        self.assertFound()

    @covers("逆引きの重複")
    def test_same_symptom_page_is_not_compared(self):
        self.add_signs("symptoms.yaml", "instructions-ignored", ("symptom", "CLAUDE.md に書いたのに、守られない"))
        self.assertFound()

    @covers("逆引きの重複")
    def test_two_symptom_pages_and_another_page(self):
        sentence = "CLAUDE.md に書いたのに守られない"
        self.add_signs("symptoms.yaml", "done-but-not-done", ("symptom", sentence))
        self.add_signs("enforce.yaml", "hooks-basics", ("goal", sentence))
        issues = self.assertFound(("逆引きの重複", "instructions-ignored"), ("逆引きの重複", "done-but-not-done"),
                                  ("逆引きの重複", "hooks-basics"))
        self.assertEqual(len(issues), 3)
        for i in issues:
            hint = "症状のページどうしで重なっている" if i.page != "hooks-basics" else "逆引きで同じ困りごとが二か所に出る"
            self.assertIn(hint, i.message)
        hooks = next(i for i in issues if i.page == "hooks-basics")   # 1つの文に、当たった症状のページをすべて出す
        self.assertIn(f"症状のページ instructions-ignored の sign「{sentence}」、done-but-not-done の sign「{sentence}」と同じ",
                      hooks.message)


class TestRoutes(CatalogCase):
    """症状のページの routes（catalog/README §4.4 の6）。形・必須・語彙・参照は、ほかのキーと同じ検査が見る。"""

    @covers("routes")
    def test_routes_on_a_page_that_is_not_a_symptom(self):
        self.edit_page("enforce.yaml", "hooks-basics", routes=make_routes(("縛っていない", ["completion-check"])))
        issues = self.assertFound(("routes", "hooks-basics"))
        self.assertEqual(issues[0].severity, cc.ERROR)
        self.assertEqual(issues[0].message, "routes は type が symptom のページだけが持つ（このページは feature。ほかのページ"
                                            "への道は related に書く）")
        self.assertEqual(issues[0].fields, frozenset({"enforce"}))
        self.assertRegex(cc.format_issue(issues[0]), LINE_RE)

    @covers("routes")
    def test_empty_to(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(II_ROUTES[0], ("縛っていない", [])))
        issues = self.assertFound(("routes", "instructions-ignored"))
        self.assertIn("routes（縛っていない）の to が空（振り分け先のページを1件以上書く）", issues[0].message)

    @covers("routes")
    def test_symptom_pages_and_pages_without_a_known_type(self):
        self.edit_page("enforce.yaml", "hooks-basics", routes=None)   # routes: null は書いていないのと同じ
        self.assertFound()
        # type が語彙にないページの routes は、type のエラーだけを出す（症状のページのつもりかもしれない）
        self.edit_page("symptoms.yaml", "done-but-not-done", type="symptomm")
        self.assertFound(("語彙", "done-but-not-done"))

    @covers("語彙")
    def test_route_cause_vocabulary(self):
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(("散らかってる", ["outdated-advice-ledger"]), II_ROUTES[1]))
        # 綴りを誤った cause は「散らかっている」の routes に数えない
        issues = self.assertFound(("語彙", "instructions-ignored"), ("routes と原因", "instructions-ignored"))
        self.assertIn("routes の cause の「散らかってる」が語彙にない（見えていない・散らかっている・確かめていない・縛っていない・"
                      "合っていない・境界がない・預けすぎる・同意を根拠にする・やめられない・体感を信じる・みんなの案になる）",
                      only(issues, "語彙")[0].message)

    @covers("参照")
    def test_route_targets_are_resolved(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(
            ("散らかっている", ["outdated-advice-ledger", "no-such-page", "rules-not-followed"]),
            ("縛っていない", ["hooks-basics#nothing", "permissions-deny", ""])))
        issues = self.assertFound(("参照", "instructions-ignored"))
        messages = [i.message for i in issues]
        self.assertEqual(len(messages), 4, messages)
        self.assertIn("routes（散らかっている）の to の「no-such-page」が存在しない id", messages[0])
        self.assertIn("routes（散らかっている）の to の「rules-not-followed」は", messages[1])
        self.assertIn("「instructions-ignored」にまとめた", messages[1])
        self.assertEqual(messages[2], "routes（縛っていない）の to の「hooks-basics#nothing」: hooks-basics の sections に "
                                      "anchor「nothing」がない（あるのは exit-codes）")
        self.assertEqual(messages[3], "routes（縛っていない）の to に空の id がある（''）")

    @covers("参照")
    def test_route_to_candidate_without_field_file_is_not_flagged(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics", "verifier-basics#metrics"])))
        self.assertFound()

    @covers("形")
    def test_route_shapes(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=[
            {"cause": "散らかっている", "to": "outdated-advice-ledger"},
            {"cause": "縛っていない", "to": ["hooks-basics#exit-codes", "permissions-deny"]},
            "縛っていない"])
        self.edit_page("symptoms.yaml", "done-but-not-done", routes={"cause": "確かめていない", "to": ["hooks-basics"]})
        issues = self.assertFound(("形", "instructions-ignored"), ("形", "done-but-not-done"))
        messages = [i.message for i in issues]
        self.assertIn("routes の要素の to をリスト（[…]）にする（いまは 'outdated-advice-ledger'）", messages)
        self.assertIn("routes の 3 番目をマッピング（{…}）にする（いまは '縛っていない'）", messages)
        self.assertIn("routes をリスト（[…]）にする（いまは {'cause': '確かめていない', 'to': ['hooks-basi…）", messages)

    @covers("必須")
    def test_route_without_cause_or_to(self):
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=[{"cause": "散らかっている", "to": ["outdated-advice-ledger"]},
                               {"to": ["hooks-basics#exit-codes", "permissions-deny"]}])
        self.edit_page("symptoms.yaml", "done-but-not-done", routes=[{"cause": "確かめていない"}])
        issues = self.assertFound(("必須", "instructions-ignored"), ("必須", "done-but-not-done"),
                                  ("routes と原因", "instructions-ignored"))   # 縛っていない の routes がなくなる
        self.assertIn("routes の要素に cause がない", only(issues, "必須")[0].message)
        self.assertIn("routes の要素に to がない（{'cause': '確かめていない'}）", only(issues, "必須")[1].message)

    @covers("知らない項目")
    def test_unknown_key_in_routes(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=[{"cause": "確かめていない", "to": ["hooks-basics"], "reason": "テストを走らせる"}])
        issues = self.assertFound(("知らない項目", "done-but-not-done"))
        self.assertIn("routes の要素の知らない項目「reason」", issues[0].message)

    @covers("未処理の候補")
    def test_route_to_unprocessed_candidate(self):
        self.add_candidate(id="secret-scan", field="enforce", title="秘密を探す", type="feature", priority="推奨")
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics", "secret-scan"])))
        issues = self.assertFound(("registry の候補", "secret-scan"), ("未処理の候補", "done-but-not-done"))
        i = only(issues, "未処理の候補")[0]
        self.assertIn("routes（確かめていない）の to の「secret-scan」は registry の候補だが", i.message)
        self.assertEqual(i.fields, frozenset({"symptoms", "enforce"}))

    @covers("入ってくる道")
    def test_routes_count_as_incoming(self):
        # permissions-deny に入ってくる道を、instructions-ignored の routes だけにする
        self.edit_page("enforce.yaml", "hooks-basics", related=[])
        self.edit_page("delegate.yaml", "parallel-sessions", related=[])
        self.assertFound()
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(II_ROUTES[0], ("縛っていない", ["hooks-basics#exit-codes"])))
        issues = self.assertFound(("入ってくる道", "permissions-deny"))
        self.assertIn("どのページの prerequisites・related・routes にも出てこない", issues[0].message)

    @covers("レベルの逆転", "必須の前提")
    def test_rules_for_prerequisites_do_not_apply_to_routes(self):
        # instructions-ignored（整える・必須）の routes に、上の段で推奨の parallel-sessions（回す・推奨）を置いてよい
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(II_ROUTES[0], ("縛っていない", ["parallel-sessions", "permissions-deny"])))
        self.assertFound()
        # 同じページを前提にも置くと、前提の規則が当たる
        self.edit_page("symptoms.yaml", "instructions-ignored", prerequisites=["request-vs-lock", "parallel-sessions"])
        self.assertFound(("レベルの逆転", "instructions-ignored"), ("必須の前提", "instructions-ignored"),
                         ("症状の前提", "instructions-ignored"), ("routes の重なり", "instructions-ignored"))

    @covers("比例則")
    def test_routes_do_not_count_for_the_proportional_rule(self):
        # done-but-not-done（任せる）の routes には enforce の hooks-basics があるが、比例則は前提と関連だけを見る
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=["request-vs-lock"])
        self.assertFound(("比例則", "done-but-not-done"))
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       related=["instructions-ignored#diagnosis", "parallel-sessions", "fact-check"])
        self.assertFound()   # verify の fact-check を関連に置けば満たす


class TestRouteWarnings(CatalogCase):
    @covers("症状の前提")
    def test_prerequisite_that_is_not_a_concept(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=["completion-check", "outdated-advice-ledger"])
        issues = self.assertFound(("症状の前提", "done-but-not-done"))
        self.assertEqual(issues[0].severity, cc.WARNING)
        self.assertEqual(issues[0].message, "前提「outdated-advice-ledger」の type が ledger（症状のページの前提は、診断を読む"
                                            "のに要る concept・guide・hub のページだけにする。対処のページは routes に置く）")
        self.assertEqual(issues[0].fields, frozenset({"symptoms"}))
        self.assertRegex(cc.format_issue(issues[0]), LINE_RE)

    @covers("症状の前提")
    def test_concept_guide_and_hub_are_fine(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", prerequisites=["request-vs-lock", "how-to-use"])
        self.assertFound()
        self.edit_page("start.yaml", "how-to-use", type="hub")
        self.assertFound()
        # 症状のページでないページの前提は見ない
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=["hooks-basics"])
        self.assertFound()
        # 前提の type が語彙にないときは、そのページのエラーだけを出す
        self.edit_page("basics.yaml", "request-vs-lock", type="conceptt")
        self.assertFound(("語彙", "request-vs-lock"))

    @covers("設定")
    def test_named_types_must_be_in_vocabulary(self):
        self.edit("site.yml", lambda d: d["types"].remove("hub"))
        issues = self.assertFound(("設定", "-"))   # types_without_level の hub の指摘も出る
        self.assertTrue(any("道具の規則が名指しする「hub」が site.yml の types にない（症状の前提の検査が当たらない" in i.message
                            for i in issues), [i.message for i in issues])

    @covers("症状の routes")
    def test_symptom_page_without_routes(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", routes=DELETE)
        issues = self.assertFound(("症状の routes", "done-but-not-done"))
        self.assertEqual(issues[0].severity, cc.WARNING)
        self.assertEqual(issues[0].message, "symptom のページに routes がない（原因ごとに、中心の対処のページを1〜3 件、"
                                            "近い順に書く）")
        self.edit_page("symptoms.yaml", "done-but-not-done", routes=[])
        self.assertFound(("症状の routes", "done-but-not-done"))

    @covers("症状の routes")
    def test_routes_are_not_asked_of_other_pages(self):
        cat = cc.load_catalog(self.root)
        self.assertEqual([p.id for p in cat.pages if p.parts("routes")], ["instructions-ignored", "done-but-not-done"])
        self.assertFound()

    @covers("routes と原因")
    def test_cause_that_the_page_does_not_diagnose(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics"]), ("縛っていない", ["permissions-deny"])))
        issues = self.assertFound(("routes と原因", "done-but-not-done"))
        self.assertEqual(issues[0].message, "routes の cause「縛っていない」が、このページの prevents・pitfalls にない"
                                            "（診断で問う原因に足すか、routes から外す）")

    @covers("routes と原因")
    def test_cause_without_routes(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(II_ROUTES[1]))
        self.edit_page("symptoms.yaml", "done-but-not-done", pitfalls=["預けすぎる"])
        issues = self.assertFound(("routes と原因", "instructions-ignored"), ("routes と原因", "done-but-not-done"))
        self.assertEqual([i.message for i in issues], [
            "prevents の「散らかっている」に routes がない（その原因の中心の対処を routes に書く。対処のページがない原因なら、"
            "notes に書く）",
            "pitfalls の「預けすぎる」に routes がない（その原因の中心の対処を routes に書く。対処のページがない原因なら、"
            "notes に書く）"])

    @covers("routes と原因")
    def test_pitfalls_can_be_routed_and_empty_prevents_is_left_to_its_check(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", pitfalls=["預けすぎる"],
                       routes=make_routes(("確かめていない", ["hooks-basics"]), ("預けすぎる", ["fact-check"])))
        self.assertFound()
        self.edit_page("symptoms.yaml", "done-but-not-done", prevents=[])
        self.assertFound(("症状の prevents", "done-but-not-done"))
        self.edit("site.yml", lambda d: d.pop("pitfalls"))   # 語彙が読めなければ、この検査をしない
        self.assertFound(("症状の prevents", "done-but-not-done"), ("設定", "-"))

    @covers("routes の重なり")
    def test_same_cause_and_same_target_twice(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(
            II_ROUTES[0], ("縛っていない", ["hooks-basics#exit-codes", "permissions-deny", "permissions-deny"]),
            ("散らかっている", ["fact-check"])))
        issues = self.assertFound(("routes の重なり", "instructions-ignored"))
        self.assertEqual([i.message for i in issues], ["routes の cause「散らかっている」が 2 回ある（1つにまとめる）",
                                                       "routes（縛っていない）の to に「permissions-deny」が 2 回ある"])

    @covers("routes の重なり")
    def test_route_target_also_in_prerequisites_or_related(self):
        # ページの id で比べる：routes の hooks-basics#exit-codes と related の hooks-basics（instructions-ignored）、
        # routes の hooks-basics と related の hooks-basics#exit-codes（done-but-not-done）
        self.edit_page("symptoms.yaml", "instructions-ignored", related=["done-but-not-done", "completion-check", "hooks-basics"],
                       routes=make_routes(("散らかっている", ["request-vs-lock"]), II_ROUTES[1]))
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       related=["instructions-ignored#diagnosis", "parallel-sessions", "hooks-basics#exit-codes"])
        issues = self.assertFound(("routes の重なり", "instructions-ignored"), ("routes の重なり", "done-but-not-done"))
        self.assertEqual([i.message for i in issues], [
            "routes の先「request-vs-lock」が prerequisites にもある（どちらか一方にする。前提は、診断を読むのに要る概念の"
            "ページだけ）",
            "routes の先「hooks-basics」が related にもある（related から外す。related には、routes にない近いページ"
            "だけを置く）",
            "routes の先「hooks-basics」が related にもある（related から外す。related には、routes にない近いページ"
            "だけを置く）"])
        self.assertEqual([i.page for i in issues], ["instructions-ignored", "instructions-ignored", "done-but-not-done"])

    @covers("routes の重なり")
    def test_same_page_in_two_causes_is_fine(self):
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(("散らかっている", ["hooks-basics"]), II_ROUTES[1]))
        self.assertFound()

    @covers("routes の数")
    def test_four_targets_for_one_cause(self):
        three = ["hooks-basics#exit-codes", "permissions-deny", "fact-check"]
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(II_ROUTES[0], ("縛っていない", three)))
        self.assertFound()
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(II_ROUTES[0], ("縛っていない", three + ["parallel-sessions"])))
        issues = self.assertFound(("routes の数", "instructions-ignored"))
        self.assertEqual(issues[0].message, "routes（縛っていない）の to が 4 件（中心の対処を 3 件までにする。ほかは related "
                                            "に置く）")


class TestTracks(CatalogCase):
    @covers("tracks の id")
    def test_unknown_track(self):
        self.edit_page("enforce.yaml", "hooks-basics", tracks=["hooks", "hook-events"])
        issues = self.assertFound(("tracks の id", "hooks-basics"))
        self.assertIn("README.md §5", issues[0].message)

    @covers("tracks の id")
    def test_new_features_of_any_file_count(self):
        def move(d):
            d["new_features"] = [{"id": "parallel-dashboard", "title": "並列の一覧", "note": "x"}]
        self.edit("enforce.yaml", move)
        self.edit("delegate.yaml", lambda d: d.pop("new_features"))
        self.assertFound()

    @covers("tracks の id")
    def test_features_yaml_takes_precedence(self):
        self.write("features.yaml", {"features": [{"id": "claude-md"}, {"id": "hooks"}, {"id": "permissions"}]})
        issues = self.assertFound(("tracks の id", "parallel-sessions"))   # worktrees は README の表にだけある
        self.assertIn("features.yaml", issues[0].message)

    @covers("tracks の id")
    def test_features_yaml_forms(self):
        grouped = {"Claude Code の文脈と指示": ["claude-md"], "Claude Code の縛り": ["hooks", "permissions"],
                   "Claude Code の任せ方": [{"id": "worktrees", "title": "worktree"}]}
        self.write("features.yaml", grouped)
        self.assertFound()
        keyed = {"features": {"claude-md": {"title": "CLAUDE.md"}, "hooks": None, "permissions": None, "worktrees": None}}
        self.write("features.yaml", keyed)
        self.assertFound()


class TestLedger(CatalogCase):
    @covers("outdated_advice の id")
    def test_unknown_advice(self):
        self.edit_page("symptoms.yaml", "instructions-ignored", outdated_advice=["important-caps", "no-such-advice"])
        self.assertFound(("outdated_advice の id", "instructions-ignored"))


class TestRegistry(CatalogCase):
    @covers("registry の候補")
    def test_candidate_not_processed(self):
        self.edit("symptoms.yaml", lambda d: d.update(dropped=[]))
        issues = self.assertFound(("registry の候補", "old-candidate"))
        self.assertEqual(issues[0].file, "planning/catalog/symptoms.yaml")

    @covers("registry の候補")
    def test_candidate_in_another_field(self):
        self.add_candidate(id="fact-check", field="enforce", title="事実を確かめる")
        issues = self.assertFound(("registry の候補", "fact-check"))
        self.assertIn("verify.yaml", issues[0].message)
        self.assertEqual(issues[0].fields, frozenset({"enforce", "verify"}))

    @covers("registry の候補")
    def test_merged_id_not_in_registry(self):
        self.edit("symptoms.yaml", lambda d: d["merged"].append({"id": "ghost-candidate", "into": "instructions-ignored"}))
        self.assertFound(("registry の候補", "ghost-candidate"))

    @covers("registry にない id")
    def test_new_page_without_mark(self):
        self.edit_page("verify.yaml", "fact-check", notes=DELETE)
        self.assertFound(("registry にない id", "fact-check"))

    @covers("registry にない id")
    def test_mark_in_file_notes(self):
        self.edit_page("verify.yaml", "fact-check", notes=DELETE)
        self.edit("verify.yaml", lambda d: d.update(notes=["新規：fact-check は試験用のページ"]))
        self.assertFound()


class TestCounts(CatalogCase):
    @covers("前提と関連の数")
    def test_prerequisites(self):
        # 互いに前提をたどって届かない5ページ（届くものがあると「推移的な前提」の警告も出る）
        pre = ["fact-check", "done-but-not-done", "hooks-basics", "permissions-deny", "instructions-ignored"]
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=pre[:4], related=[])
        self.assertFound()
        self.edit_page("delegate.yaml", "parallel-sessions", prerequisites=pre)
        self.assertFound(("前提と関連の数", "parallel-sessions"))

    @covers("前提と関連の数")
    def test_related(self):
        ids = [f"extra-{n}" for n in range(1, 22)]
        for x in ids:
            self.add_candidate(id=x, field="eval", title=x)   # eval のファイルはないので、まだ確かめられない参照
        self.edit_page("verify.yaml", "fact-check", related=ids[:20])
        self.assertFound()
        self.edit_page("verify.yaml", "fact-check", related=ids)
        self.assertFound(("前提と関連の数", "fact-check"))


class TestFieldPrefix(CatalogCase):
    @covers("id の分野名")
    def test_own_field_name_at_the_head(self):
        self.edit_page("verify.yaml", "fact-check", id="verify-facts")
        self.edit_page("verify.yaml", "completion-check", related=["verify-facts", "verifier-basics"])
        self.assertFound(("id の分野名", "verify-facts"))

    @covers("id の分野名")
    def test_other_field_names_are_not_checked(self):
        self.edit_page("verify.yaml", "fact-check", id="context-facts")   # basics の context-rot のような id
        self.edit_page("verify.yaml", "completion-check", related=["context-facts", "verifier-basics"])
        self.assertFound()

    @covers("id の分野名")
    def test_registry_candidate(self):
        self.add_candidate(id="eval-basics", field="eval", title="評価の基本")
        self.assertFound(("id の分野名", "eval-basics"))


class TestOtherWarnings(CatalogCase):
    @covers("知らない項目")
    def test_misspelled_page_key(self):
        self.edit_page("verify.yaml", "fact-check", prerequisite=["request-vs-lock"])
        issues = self.assertFound(("知らない項目", "fact-check"))
        self.assertIn("「prerequisite」", issues[0].message)

    @covers("知らない項目")
    def test_unknown_file_key(self):
        self.edit("symptoms.yaml", lambda d: d.update(merge=[]))
        self.assertFound(("知らない項目", "-"))

    @covers("章")
    def test_chapter_not_in_chapters(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", chapter="検証")
        # 確かめ方の章にはページがなくなる
        self.assertFound(("章", "done-but-not-done"), ("章", "-"))

    @covers("wave")
    def test_wave_outside_core_fields(self):
        self.edit_page("enforce.yaml", "hooks-basics", wave=1)
        self.assertFound(("wave", "hooks-basics"))

    @covers("wave")
    def test_core_field_without_wave(self):
        self.edit_page("changes.yaml", "outdated-advice-ledger", wave=DELETE)
        issues = self.assertFound(("wave", "-"))
        self.assertEqual(issues[0].file, "planning/catalog/changes.yaml")

    @covers("wave")
    def test_every_entry_and_symptom_page_needs_wave(self):
        # 入口（start）と症状辞典は全ページに付ける（catalog/README §4.6 の2）。ほかの核の分野は総論などだけでよい
        self.edit_page("symptoms.yaml", "done-but-not-done", wave=DELETE)
        issues = self.assertFound(("wave", "done-but-not-done"))
        self.assertEqual(issues[0].message, "wave: 1 がない（入口の分野のページと症状のページは、全ページに付ける）")
        # 入口の分野は site.yml の entry_fields から読む。changes を入口にすると、start のページは全ページでなくてよい
        # （start の核がないことと、how-to-use に入ってくる道がないことだけが出る）
        self.edit("site.yml", lambda d: d.update(entry_fields=["changes"]))
        self.edit_page("symptoms.yaml", "done-but-not-done", wave=1)
        self.edit_page("start.yaml", "how-to-use", wave=DELETE)
        self.assertFound(("wave", "-"), ("入ってくる道", "how-to-use"))


class TestConfig(CatalogCase):
    @covers("設定")
    def test_no_registry(self):
        self.path("registry.yaml").unlink()
        # registry がないと、まだない分野の候補（verifier-basics）も存在しない id になる
        issues = self.assertFound(("設定", "-"), ("参照", "completion-check"))
        self.assertEqual(only(issues, "設定")[0].fields, cc.ALWAYS)

    @covers("設定")
    def test_missing_vocabulary_skips_its_check(self):
        self.edit("site.yml", lambda d: d.pop("pitfalls"))
        self.edit_page("symptoms.yaml", "instructions-ignored", pitfalls=["だれか"])
        issues = self.assertFound(("設定", "-"))
        self.assertIn("pitfalls", issues[0].message)

    @covers("設定")
    def test_kinds_from_site_yml_override_readme(self):
        self.edit("site.yml", lambda d: d.update(visual_kinds=["static", "mermaid"]))
        self.edit_page("symptoms.yaml", "instructions-ignored", visual={"kind": "dynamic", "text": "動く図"})
        self.assertFound(("語彙", "instructions-ignored"))

    @covers("設定")
    def test_no_readme(self):
        self.path("README.md").unlink()
        issues = self.assertFound(("設定", "-"))
        self.assertEqual(len(issues), 3)   # visual の kind・templates の kind・機能の id の表

    @covers("設定")
    def test_rule_value_missing_from_vocabulary(self):
        self.edit("site.yml", lambda d: d["types"].remove("symptom"))
        issues = self.assertFound(("設定", "-"), ("語彙", "instructions-ignored"), ("語彙", "done-but-not-done"),
                                  ("語彙", "rules-not-followed"), ("語彙", "old-candidate"))
        self.assertIn("「symptom」", only(issues, "設定")[0].message)


def wave_ids(fw: cc.FirstWave) -> dict[str, list[str]]:
    return {"core": [p.id for p in fw.core], "prerequisites": [p.id for p in fw.prerequisites],
            "routes": [p.id for p in fw.routes], "named": [p.id for p in fw.named]}


class TestFirstWave(CatalogCase):
    """第一波の数え方（catalog/README §4.6 の3）。試験用の目次の site.yml は first_wave: {routes: first,
    named: [parallel-sessions]}。核（wave: 1）は how-to-use・instructions-ignored・done-but-not-done・outdated-advice-ledger。
    routes の先の priority は、outdated-advice-ledger と permissions-deny が必須、hooks-basics が推奨。"""

    def wave(self, mode: str | None = None) -> cc.FirstWave:
        return cc.first_wave(cc.load_catalog(self.root), mode)

    def lacking(self, fw: cc.FirstWave) -> list[tuple[str, str, tuple[str, ...]]]:
        return [(x.page.id, x.cause, x.targets) for x in fw.lacking]

    def test_fixture(self):
        fw = self.wave()
        self.assertEqual(fw.mode, "first")
        self.assertEqual(wave_ids(fw), {
            "core": ["how-to-use", "instructions-ignored", "done-but-not-done", "outdated-advice-ledger"],
            "prerequisites": ["request-vs-lock", "completion-check"],
            # 各 cause の to のうち最初の必須の先：散らかっている は outdated-advice-ledger（もう核にある）、縛っていない は
            # 推奨の hooks-basics#exit-codes を飛ばして permissions-deny。done-but-not-done の 確かめていない は推奨の先だけ
            "routes": ["permissions-deny"],
            "named": ["parallel-sessions"]})   # その前提の completion-check は、もう前提から入っている
        self.assertEqual(self.lacking(fw), [("done-but-not-done", "確かめていない", ("hooks-basics",))])
        self.assertEqual(fw.unresolved, [])
        self.assertEqual(len(fw.pages), 8)

    def test_routes_modes(self):
        self.assertEqual(wave_ids(self.wave("none"))["routes"], [])
        self.assertEqual(wave_ids(self.wave("first"))["routes"], ["permissions-deny"])
        self.assertEqual(wave_ids(self.wave("all"))["routes"], ["hooks-basics", "permissions-deny"])   # 優先度を問わない
        self.assertEqual([len(self.wave(m).pages) for m in cc.FIRST_WAVE_ROUTES], [7, 8, 9])
        self.assertEqual(self.lacking(self.wave("all")), self.lacking(self.wave("none")))   # 数え方によらない
        self.edit("site.yml", lambda d: d["first_wave"].update(routes="all"))
        self.assertEqual((self.wave().mode, len(self.wave().pages)), ("all", 9))

    def test_first_takes_only_the_first_required_target(self):
        self.edit_page("verify.yaml", "fact-check", priority="必須")
        self.edit_page("symptoms.yaml", "instructions-ignored", routes=make_routes(
            II_ROUTES[0], ("縛っていない", ["hooks-basics#exit-codes", "fact-check", "permissions-deny"])))
        fw = self.wave()
        self.assertEqual(wave_ids(fw)["routes"], ["fact-check"])
        self.assertNotIn("permissions-deny", [p.id for p in fw.pages])   # 2つ目の必須の先は入れない
        self.assertEqual(wave_ids(self.wave("all"))["routes"], ["hooks-basics", "fact-check", "permissions-deny"])

    def test_priority_of_a_candidate_without_field_file_comes_from_registry(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics", "verifier-basics"])))   # registry では必須
        fw = self.wave()
        self.assertEqual((self.lacking(fw), fw.unresolved), ([], ["verifier-basics"]))
        self.edit("registry.yaml", lambda d: next(e for e in d["pages"] if e["id"] == "verifier-basics").update(priority="推奨"))
        fw = self.wave()
        self.assertEqual(self.lacking(fw), [("done-but-not-done", "確かめていない", ("hooks-basics", "verifier-basics"))])
        self.assertEqual(fw.unresolved, [])

    def test_closure_takes_prerequisites_of_routes_and_named(self):
        # done-but-not-done の前提を外すと、completion-check は核から前提で届かなくなる
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=["request-vs-lock"])
        self.assertEqual(wave_ids(self.wave())["named"], ["parallel-sessions", "completion-check"])   # named の前提
        self.edit_page("verify.yaml", "fact-check", priority="必須")
        self.edit_page("symptoms.yaml", "done-but-not-done", routes=make_routes(("確かめていない", ["fact-check"])))
        fw = self.wave()
        self.assertEqual(wave_ids(fw)["routes"], ["permissions-deny", "fact-check", "completion-check"])   # routes の先の前提
        self.assertEqual(wave_ids(fw)["named"], ["parallel-sessions"])

    def test_routes_are_taken_only_from_core_symptom_pages(self):
        self.edit_page("verify.yaml", "fact-check", priority="必須")
        self.edit_page("symptoms.yaml", "done-but-not-done", routes=make_routes(("確かめていない", ["fact-check"])))
        self.assertIn("fact-check", [p.id for p in self.wave().pages])
        # 核でない症状のページの routes は種にしない。routes の先から入った症状のページの routes もたどらない
        self.edit_page("symptoms.yaml", "done-but-not-done", wave=DELETE)
        self.assertNotIn("fact-check", [p.id for p in self.wave("all").pages])
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(("散らかっている", ["done-but-not-done"]), II_ROUTES[1]), related=["completion-check"])
        fw = self.wave("all")
        self.assertEqual(wave_ids(fw)["routes"], ["done-but-not-done", "hooks-basics", "permissions-deny", "completion-check"])
        self.assertNotIn("fact-check", [p.id for p in fw.pages])
        self.assertEqual(self.lacking(fw), [])   # 核でない done-but-not-done の cause は数えない
        # 症状のページでないページの routes（エラー）もたどらない
        self.edit_page("start.yaml", "how-to-use", routes=make_routes(("見えていない", ["fact-check"])))
        self.assertNotIn("fact-check", [p.id for p in self.wave("all").pages])

    def test_named_counts_only_what_it_adds(self):
        # permissions-deny は first でも routes から入るので、named から足すものはない
        self.edit("site.yml", lambda d: d["first_wave"].update(named=["permissions-deny"]))
        self.assertEqual(wave_ids(self.wave("none"))["named"], ["permissions-deny"])
        self.assertEqual(wave_ids(self.wave("first"))["named"], [])
        self.edit("site.yml", lambda d: d["first_wave"].update(named=[]))
        self.assertEqual(len(self.wave().pages), 7)

    def test_unresolved_candidates(self):
        # ファイルのまだない分野の候補（verifier-basics）は、前提・routes・named のどれから指してもたどれない候補にする
        self.edit_page("symptoms.yaml", "instructions-ignored",
                       routes=make_routes(II_ROUTES[0], ("縛っていない", ["verifier-basics"])))
        self.assertEqual(self.wave().unresolved, ["verifier-basics"])
        self.assertEqual(self.wave("none").unresolved, [])
        self.edit("site.yml", lambda d: d["first_wave"].update(named=["verifier-basics"]))
        self.assertEqual(self.wave("none").unresolved, ["verifier-basics"])

    def test_follows_prerequisites_transitively(self):
        # completion-check に、核から前提を2段たどって届く形にする（instructions-ignored → request-vs-lock → completion-check）
        self.edit_page("symptoms.yaml", "done-but-not-done", prerequisites=[],
                       related=["instructions-ignored#diagnosis", "parallel-sessions", "fact-check"])
        self.edit_page("basics.yaml", "request-vs-lock", prerequisites=["completion-check"])
        self.edit_page("verify.yaml", "completion-check", prerequisites=["verifier-basics"], related=["fact-check"])
        self.assertFound()
        fw = self.wave()
        self.assertEqual(wave_ids(fw)["prerequisites"], ["request-vs-lock", "completion-check"])
        self.assertEqual(fw.unresolved, ["verifier-basics"])
        code, out, _ = self.run_cli("--stats")
        self.assertIn("第一波: 8 ページ（wave: 1 が 4、前提でたどって届くもの 2、routes から 1、named から 1）｜start 1・"
                      "basics 1・verify 1・enforce 1・delegate 1・symptoms 2・changes 1", out)
        self.assertIn("  たどれない候補（分野のファイルにまだない）: verifier-basics", out)


class TestFirstWaveConfig(CatalogCase):
    """site.yml の first_wave が読めないときは「設定」の警告にして、routes を none・named を空として数える。"""

    def config(self) -> list[str]:
        return [i.message for i in only(self.issues(), "設定")]

    @covers("設定")
    def test_missing_first_wave(self):
        self.edit("site.yml", lambda d: d.pop("first_wave"))
        issues = self.assertFound(("設定", "-"))
        self.assertIn("first_wave がない", issues[0].message)
        self.assertEqual(issues[0].fields, cc.ALWAYS)
        fw = cc.first_wave(cc.load_catalog(self.root))
        self.assertEqual((fw.mode, len(fw.pages)), ("none", 6))   # 工程3の数え方（核と前提だけ）

    @covers("設定")
    def test_bad_values(self):
        self.edit("site.yml", lambda d: d.update(first_wave={"routes": "some", "named": "parallel-sessions", "name": []}))
        self.assertFound(("設定", "-"))
        messages = self.config()
        self.assertEqual(len(messages), 3, messages)
        self.assertTrue(any("routes の「some」が none・first・all のどれでもない" in m for m in messages), messages)
        self.assertTrue(any("named が文字列のリストでない" in m for m in messages), messages)
        self.assertTrue(any("知らない項目「name」" in m for m in messages), messages)
        fw = cc.first_wave(cc.load_catalog(self.root))
        self.assertEqual((fw.mode, fw.named), ("none", []))
        self.edit("site.yml", lambda d: d.update(first_wave=["first"]))
        self.assertTrue(any("first_wave がマッピング" in m for m in self.config()))

    @covers("設定")
    def test_named_must_point_to_a_page(self):
        self.edit("site.yml", lambda d: d["first_wave"].update(named=["no-such-page", "rules-not-followed", "verifier-basics"]))
        issues = self.assertFound(("設定", "-"))
        self.assertEqual(len(issues), 2)   # ファイルのまだない分野の候補（verifier-basics）は指摘しない
        self.assertIn("named の「no-such-page」が存在しない id", issues[0].message)
        self.assertIn("named の「rules-not-followed」は", issues[1].message)
        self.assertIn("「instructions-ignored」にまとめた", issues[1].message)
        self.assertEqual(issues[0].file, "schema/site.yml")

    @covers("設定")
    def test_named_anchor(self):
        self.edit("site.yml", lambda d: d["first_wave"].update(named=["instructions-ignored#diagnosis", "hooks-basics#nothing"]))
        issues = self.assertFound(("設定", "-"))
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].message, "site.yml の first_wave の named の「hooks-basics#nothing」: hooks-basics の "
                                            "sections に anchor「nothing」がない（ページは第一波に数える）")
        self.assertEqual(wave_ids(cc.first_wave(cc.load_catalog(self.root)))["named"], ["hooks-basics"])

    def test_real_site_yml(self):
        findings: list = []
        vocab = cc.load_vocab(REPO, findings)
        self.assertEqual(findings, [])
        self.assertIn(vocab.first_wave_routes, cc.FIRST_WAVE_ROUTES)
        self.assertTrue(vocab.first_wave_named)


class TestCli(CatalogCase):
    def test_exit_codes(self):
        self.assertEqual(self.run_cli()[0], 0)
        self.edit_page("symptoms.yaml", "done-but-not-done", prevents=[])   # 警告だけ
        self.assertEqual(self.run_cli()[0], 0)
        self.edit_page("enforce.yaml", "hooks-basics", type="featur")       # エラー
        self.assertEqual(self.run_cli()[0], 1)

    def test_output_lines(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", prevents=[])
        self.edit_page("enforce.yaml", "hooks-basics", type="featur")
        code, out, _ = self.run_cli()
        lines = out.splitlines()
        self.assertEqual(code, 1)
        line = self.line_of("enforce.yaml", "- id: hooks-basics")   # ページの始まりの行
        self.assertEqual(lines[0], f"エラー: planning/catalog/enforce.yaml:{line}: hooks-basics: [語彙] type の「featur」が"
                                   "語彙にない（concept・feature・symptom・comparison・recipe・judgment・ledger・guide・hub）")
        self.assertTrue(lines[1].startswith("警告: planning/catalog/symptoms.yaml:"), lines[1])
        for line in lines[:-1]:
            self.assertRegex(line, LINE_RE)
        self.assertEqual(lines[-1], "エラー 1 件（語彙 1）、警告 1 件（症状の prevents 1）（分野のファイル 7・ページ 10 を読んだ）")

    def test_field_filter(self):
        self.edit_page("enforce.yaml", "hooks-basics", type="featur")
        code, out, _ = self.run_cli("--field", "symptoms")
        self.assertEqual(code, 0)
        self.assertNotIn("enforce.yaml", out)
        self.assertTrue(out.splitlines()[-1].startswith("symptoms に関わる指摘：エラー 0 件"))
        code, out, _ = self.run_cli("--field", "enforce")
        self.assertEqual(code, 1)
        self.assertIn("hooks-basics", out)

    def test_field_shows_issues_that_cross_fields(self):
        copy = dict(self.page("verify.yaml", "completion-check"), chapter="確かめ方")
        self.edit("symptoms.yaml", lambda d: d["pages"].append(copy))
        for field in ("symptoms", "verify"):
            code, out, _ = self.run_cli("--field", field)
            self.assertEqual(code, 1, field)
            self.assertIn("[id の重複]", out)
        self.assertEqual(self.run_cli("--field", "enforce")[0], 0)

    def test_field_without_file(self):
        code, out, _ = self.run_cli("--field", "eval", "--stats")
        self.assertEqual(code, 0)
        self.assertIn("注: planning/catalog/eval.yaml はまだない", out)
        self.assertIn("eval（評価と実験）: ファイルなし｜registry の候補 1", out)

    def test_quiet(self):
        self.edit_page("symptoms.yaml", "done-but-not-done", prevents=[])
        code, out, _ = self.run_cli("-q")
        self.assertEqual(code, 0)
        self.assertNotIn("警告:", out)
        self.assertIn("警告 1 件（症状の prevents 1）。-q で出していない", out)

    def test_stats(self):
        code, out, _ = self.run_cli("--stats")
        self.assertEqual(code, 0)
        self.assertIn("  symptoms（症状辞典）: 2 ページ｜優先度 必須 2｜レベル 整える 1・任せる 1｜型 symptom 2｜"
                      "registry の候補 4（採る 2・まとめた 1・採らない 1）", out)
        self.assertIn("  計: 10 ページ｜優先度 必須 7・推奨 3｜", out)
        self.assertIn("第一波: 8 ページ（wave: 1 が 4、前提でたどって届くもの 2、routes から 1、named から 1）｜start 1・basics 1・"
                      "verify 1・enforce 1・delegate 1・symptoms 2・changes 1\n"
                      "  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは first）: none 7・first 8・all 9\n"
                      "  必須の先がない cause（first ではそこから入れない）: 1（うち、first で先がどれも第一波に入らないもの 1）｜"
                      "done-but-not-done（確かめていない）\n"
                      "必須: 7 ページ", out)
        self.assertNotIn("たどれない候補", out)

    def test_stats_without_lacking_causes(self):
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics", "completion-check"])))
        code, out, _ = self.run_cli("--stats")
        self.assertIn("  必須の先がない cause（first ではそこから入れない）: 0\n", out)
        # 必須の先がない cause の先が、ほかの道で第一波に入っていれば、準備中にはならない
        self.edit_page("symptoms.yaml", "done-but-not-done",
                       routes=make_routes(("確かめていない", ["hooks-basics"])), prerequisites=["completion-check", "hooks-basics"])
        code, out, _ = self.run_cli("--stats")
        self.assertIn("  必須の先がない cause（first ではそこから入れない）: 1（うち、first で先がどれも第一波に入らないもの 0）｜"
                      "done-but-not-done（確かめていない）\n", out)

    def test_stats_for_one_field(self):
        code, out, _ = self.run_cli("--stats", "--field", "symptoms")
        self.assertIn("集計（symptoms の分野）:", out)
        self.assertIn("第一波（symptoms のページ）: 2 ページ（wave: 1 が 2、前提でたどって届くもの 0、routes から 0、named から 0。"
                      "全体では 8 ページ）", out)
        self.assertIn("必須: 2 ページ", out)
        self.assertNotIn("verify（確かめる）", out)
        code, out, _ = self.run_cli("--stats", "--field", "enforce")
        self.assertIn("第一波（enforce のページ）: 1 ページ（wave: 1 が 0、前提でたどって届くもの 0、routes から 1、named から 0。"
                      "全体では 8 ページ）\n"
                      "  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは first）: none 0・first 1・all 2"
                      "（全体では none 7・first 8・all 9）\n"
                      "  必須の先がない cause（first ではそこから入れない）: 1", out)   # cause は全体の数

    def test_cannot_check(self):
        code, _, err = self.run_cli("--field", "nope")
        self.assertEqual(code, 2)
        self.assertIn("--field の「nope」", err)
        self.path("site.yml").unlink()
        code, _, err = self.run_cli()
        self.assertEqual(code, 2)
        self.assertIn("schema/site.yml が読めない", err)

    def test_help(self):
        res = subprocess.run([sys.executable, str(TOOL), "-h"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("使い方:", res.stdout)
        self.assertIn("--field", res.stdout)
        for c in cc.CHECKS:
            self.assertIn(f"[{c.name}] ", res.stdout)

    def test_real_repository_runs(self):
        """本物の目次（書きかけでもよい）で落ちずに終わる。"""
        res = subprocess.run([sys.executable, str(TOOL), "--stats"], capture_output=True, text=True, encoding="utf-8",
                             cwd=REPO)
        self.assertIn(res.returncode, (0, 1), res.stderr)
        self.assertNotIn("Traceback", res.stderr)
        self.assertIn("を読んだ）", res.stdout.splitlines()[-1])


class TestRealSources(unittest.TestCase):
    """本物の schema/site.yml と planning/catalog/README.md を、道具が読めること。"""

    def test_site_yml_and_readme_kinds(self):
        findings: list = []
        vocab = cc.load_vocab(REPO, findings)
        readme = (REPO / "planning" / "catalog" / "README.md").read_text(encoding="utf-8")
        cc.fill_kinds(vocab, readme, findings)
        self.assertEqual(findings, [])
        self.assertEqual(vocab.entry_fields, ["start"])
        self.assertEqual(vocab.top_priority, "必須")
        self.assertIsNotNone(vocab.visual_kinds)
        self.assertIsNotNone(vocab.template_kinds)
        if "visual_kinds" not in (yaml.safe_load((REPO / "schema" / "site.yml").read_text(encoding="utf-8")) or {}):
            self.assertEqual(vocab.visual_kinds, ["static", "mermaid", "dynamic"])
            self.assertEqual(vocab.template_kinds, ["settings", "hook", "skill", "subagent", "claude-md", "prompt", "other"])

    def test_readme_feature_table(self):
        readme = (REPO / "planning" / "catalog" / "README.md").read_text(encoding="utf-8")
        ids = cc.parse_feature_table(readme)
        for x in ("claude-md", "hooks", "permission-modes", "worktrees", "projects", "prompt-caching", "usage-credits"):
            self.assertIn(x, ids)
        self.assertGreaterEqual(len(ids), 70)
        self.assertEqual([x for x in ids if not cc.ID_RE.match(x)], [])
        self.assertNotIn("tracks", ids)   # 表の外の `tracks` は読まない


class TestCheckRegistry(unittest.TestCase):
    def test_every_check_has_a_test(self):
        self.assertEqual(COVERED, {c.name for c in cc.CHECKS})

    def test_checks_are_well_formed(self):
        names = [c.name for c in cc.CHECKS]
        self.assertEqual(len(names), len(set(names)))
        for c in cc.CHECKS:
            self.assertIn(c.severity, (cc.ERROR, cc.WARNING))
            self.assertTrue(c.summary, c.name)


if __name__ == "__main__":
    unittest.main()
