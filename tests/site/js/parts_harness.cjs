// 見た目の JS（overrides/assets/js/ の expiry.js・filter.js・map.js）のうち、DOM の要らない部分を Node.js で動かし、
// 結果を JSON で標準出力に書く。tests/site/test_site_parts.py が使う（Node.js がなければ、その試験は飛ぶ）。
//
//   node tests/site/js/parts_harness.cjs <overrides の場所> <graph.json の場所>
//
// ブラウザの部品（window・document・location など）は、読み込みが止まらないだけの小さな代わりを置く。
// ページに部品の目印（[data-ca-page]・.ca-filter・.ca-graph）がないので、どの JS もページには何も足さない。
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const [overrides, graphFile] = process.argv.slice(2);
const noop = () => {};
const emptyElement = { querySelector: () => null, querySelectorAll: () => [] };
const context = {
  console, URL, URLSearchParams, Map, Set, WeakMap, Promise, JSON, Math, Date, Object, Array, String, Number, RegExp, Error,
  setTimeout, clearTimeout,
  location: new URL("http://127.0.0.1/claude-atlas/start/knowledge-map/"),
  history: { state: null, replaceState: noop },
  performance: { now: () => 0 },
  fetch: () => Promise.reject(new Error("この試験では読まない")),
  Node: { DOCUMENT_POSITION_FOLLOWING: 4 },
  Element: function Element() {},
};
context.window = context;
context.document = {
  readyState: "complete",
  body: emptyElement,
  documentElement: emptyElement,
  currentScript: null,
  addEventListener: noop,
  querySelector: () => null,
  querySelectorAll: () => [],
};
vm.createContext(context);

function load(name) {
  context.document.currentScript = { src: "http://127.0.0.1/claude-atlas/assets/js/" + name };
  vm.runInContext(fs.readFileSync(path.join(overrides, "assets", "js", name), "utf8"), context, { filename: name });
  context.document.currentScript = null;
}
["expiry.js", "filter.js", "map.js"].forEach(load);

const E = context.CAExpiry;
const M = context.CAMatch;
const C = context.CAMap;
const out = {};

// ---- 期限の比べ方（期限の日が今日より前なら期限切れ。当日はまだ。tools/lib の Expiry.expired と同じ）
out.expired = [
  ["2026-11-03", "2026-11-04"],
  ["2026-11-04", "2026-11-04"],
  ["2026-11-05", "2026-11-04"],
  ["2026-12-31", "2027-01-01"],
  [null, "2026-11-04"],
  ["", "2026-11-04"],
  ["2026-1-3", "2026-11-04"],
  ["2026-11-03T00:00", "2026-11-04"],
].map(([a, b]) => E.isExpired(a, b));
out.today = E.today();

// ---- 照合の規則
out.norm = ["Plan Mode", "plan-mode", "ＰＬＡＮ　ＭＯＤＥ", "プランモード", "ぷらんもーど", "CLAUDE.md", "ＣＬＡＵＤＥ．ｍｄ", "フック・hooks"]
  .map((s) => M.norm(s));
M.addSynonyms([["plan mode", "プランモード", "plan モード"], ["削除", "取り除く", "取り除"]]);
M.addSynonyms([["plan mode", "プランモード", "plan モード"], ["ひとつだけ"], "組でない", [1, 2]]);
const row = M.norm("plan mode で立てた計画が雑");
out.synonym = {
  terms: M.terms("プランモード 計画"),
  hit: M.test(row, M.terms("プランモード 計画")),
  miss: M.test(row, M.terms("プランモード 予定")),
  plain: M.test(row, M.terms("計画")),
  count: M.synonyms("plan mode").length,
  okurigana: M.synonyms("取り除いた").map((s) => [s.n, s.from, s.to]),
  words: M.words("  hooks　 ・  permissions "),
};

// ---- graph.json の読み方
function summary(G) {
  return {
    pages: G.pages.map((p) => p.id),
    edges: G.edges.map((e) => [e.s, e.t, e.kind]),
    parents: Object.fromEntries(Array.from(G.parents, ([k, v]) => [k, v])),
    children: Object.fromEntries(Array.from(G.children, ([k, v]) => [k, v])),
    related: Object.fromEntries(G.pages.map((p) => [p.id, p._related])),
    fields: G.fields.map((f) => [f.id, f.title]),
    levels: G.levels,
    rank: Object.fromEntries(Array.from(G.rank)),
  };
}
// 作る層の形（nodes と edges。tools/gen/pages_out.py の graph_json）
out.graph = summary(C.indexGraph(JSON.parse(fs.readFileSync(graphFile, "utf8"))));
// ページの prerequisites と routes から辺を作る形（edges がないとき）。ないページ・自分自身・重なりは捨て、id#anchor は id にする
out.graphPages = summary(C.indexGraph({
  levels: ["使う", "整える", "任せる", "仕組みにする", "回す", "六つ目"],
  pages: [
    { id: "a", field: "x", level: "使う", prerequisites: [] },
    { id: "b", field: "x", level: "六つ目", prerequisites: ["a", "a", "zz", "b"] },
    { id: "s", field: "y", routes: [{ cause: "c", to: ["b#sec", "zz", "s"] }, "a"], related: ["a", "a#x", "zz", "s", "b"] },
    { id: "a", field: "dup" },
    { title: "id のないページ" },
  ],
}));
out.graphEmpty = summary(C.indexGraph(null));

process.stdout.write(JSON.stringify(out));
