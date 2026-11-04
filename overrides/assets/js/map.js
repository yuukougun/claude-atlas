/*
 * claude-atlas：知識マップ（planning/design.md §7・§8.5。kyopro-atlas の overrides/assets/js/map.js を写して直した。
 * 読者の進捗を記録する部品と、それに頼る塗り分けは持ち込まない。D17）
 *
 * 本文の <div class="ca-graph" data-graph="<graph.json への相対の URL>"></div>（作る層が知識マップのページの目印
 * gen:begin graph の間に書く。tools/gen/pagebits.py）に、graph.json のページのつながりを描く。data-graph がなければ
 * この JS の URL から決めた assets/data/graph.json を読む（<div id="ca-map"></div> も同じに扱う）。辺は前提
 * （prerequisites。前提のページ → そのページ）と、症状のページの振り分け（routes。症状のページ → 対処のページ）の2種類。
 * Cytoscape.js と dagre（assets/vendor/ の写し）は地図のあるページでだけ読み込む。外のサイトからは読まない。
 *
 * - 既定は分野ごとの表示（?field=<分野>）。その分野のページに加え、ほかの分野の直接の前（前提か振り分けの元）を破線の枠で、
 *   この分野の先にある分野を「→ 分野」の点で出す。始めの分野は、地図の div の data-field、なければ辺のある最初の分野
 * - ?focus=<id>：そのページの祖先（たどれる前をすべて）と子孫（次に読む・振り分けの先）だけを描く。子孫が多いときは
 *   深さを絞って始める（?depth=<1〜3>、0 はすべて）。graph.json に related があれば、配置の後で選んだページのすぐ下
 *   （か上）の空いた所に「関連」の囲みとして足す（配置には使わない。比例則の守りのページもここに出る）
 * - ?view=all：分野を頂点にした全体の図。辺の太さは分野をまたぐ辺の本数。分野を押すとその分野の表示になる
 * - 枠の色はレベル（委任の段階。ca.css の --ca-lv-1〜5。graph.json の levels の順）。点の説明は地図の中に重ねて出す。
 *   点を押す（タップ・クリック）か長押しすると説明を固定し、×・Esc・地図の空いた所を押すと閉じる。マウスを乗せると説明を
 *   仮に出す。そのページへは、説明の「ページを開く」か、点のダブルクリック（ダブルタップ）で移る
 * - 「ページ」欄：題名・短い題名・別名（それぞれのかっこの中と外も）・id を、filter.js の照合の規則（window.CAMatch）で比べ、
 *   完全一致 → 前方一致 → 部分一致の順に選ぶ。同じ段では、当たった名前が短い → レベルの低い → graph.json の順
 * - 色は Material の CSS 変数と ca.css の変数から取り、ライトとダークの切り替えに追従する
 *
 * graph.json の形（作る層と決める。読むのは indexGraph だけ）：
 *   {"fields": [{"id", "title"}], "levels": [<低い順>],
 *    "pages": [{"id", "title", "nav_title"?, "aliases"?, "url"（サイトのルートから）, "field", "level"?, "type"?,
 *               "summary"?, "prerequisites"?: [id], "routes"?: [{"cause", "to": [id か id#anchor]}] か [id],
 *               "related"?: [id か id#anchor]}],
 *    "edges"?: [{"source"|"from", "target"|"to", "kind"|"type": "prerequisite" | "route"}]}
 *   pages の代わりに nodes でもよい。edges があれば、ページの prerequisites と routes より edges を使う
 */
(function () {
  "use strict";

  var SRC = document.currentScript ? document.currentScript.src : location.href;
  var ASSETS = new URL("../", SRC); // …/assets/
  var ROOT = new URL("../../", SRC); // サイトのルート（graph.json の url はここからの相対）
  var LIBS = ["vendor/cytoscape-3.34.4/cytoscape.min.js", "vendor/cytoscape-dagre-4.0.1/cytoscape-dagre.min.js"];
  var MAX_LEVELS = 5; // ca.css の --ca-lv-1〜5
  var MAX_DESCENDANTS = 80; // 焦点の表示で子孫がこれより多いときは、深さを絞って始める
  var FONT_SIZE = 13;
  var FIELD_FONT_SIZE = 15; // 全体の図の分野の点
  var LINE_HEIGHT = 1.25;
  var PAD_X = 10;
  var PAD_Y = 6;
  var MAX_LABEL_W = 168;
  var READABLE_ZOOM = 0.8; // 全体を収めると文字がこれより小さくなるときは、この倍率で一部を見せる（指でずらして読む）
  var MIN_FOCUS_ZOOM = 0.45; // 焦点の表示で、選んだページと関連の囲みを入れるために下げてよい倍率の下限
  var REL_GAP = 10; // 関連の囲みの中の点の間
  var REL_PAD = 10; // 関連の囲みの枠と点の間（スタイルの padding と同じ）
  var REL_LABEL = 22; // 関連の囲みの上の「関連」の文字の分
  var REL_MARGIN = 36; // 関連の囲みとほかの点の間
  var LAYOUT = { name: "dagre", rankDir: "LR", nodeSep: 14, rankSep: 56, edgeSep: 8, fit: false, animate: false };
  var LAYOUT_FIELDS = { name: "dagre", rankDir: "TB", nodeSep: 30, rankSep: 60, fit: false, animate: false };

  var current = null; // このページの地図

  // ---------------------------------------------------------------- 読み込み

  var scripts = Object.create(null);

  function loadScript(rel) {
    var src = new URL(rel, ASSETS).href;
    if (!scripts[src]) {
      scripts[src] = new Promise(function (resolve, reject) {
        var s = document.createElement("script");
        s.src = src;
        s.onload = function () { resolve(); };
        s.onerror = function () {
          delete scripts[src];
          reject(new Error("読み込めない：" + rel));
        };
        document.head.appendChild(s);
      });
    }
    return scripts[src];
  }

  function loadLibs() {
    return (window.cytoscape ? Promise.resolve() : loadScript(LIBS[0]))
      .then(function () { return window.cytoscapeDagre ? null : loadScript(LIBS[1]); })
      .then(function () {
        var has = false;
        try { has = !!window.cytoscape("layout", "dagre"); } catch (e) { has = false; }
        if (!has) window.cytoscape.use(window.cytoscapeDagre); // window.cytoscape があれば dagre は読み込み時に自分で登録する
      });
  }

  var graphs = Object.create(null); // URL → 読み込みの Promise（instant navigation でほかのページから戻っても読み直さない）

  // 地図の div の data-graph（ページからの相対）か、この JS の URL から決めた assets/data/graph.json
  function graphUrl(root) {
    var rel = root.getAttribute("data-graph");
    return rel ? new URL(rel, location.href).href : new URL("data/graph.json", ASSETS).href;
  }

  function loadGraph(url) {
    if (!graphs[url]) {
      graphs[url] = fetch(url, { credentials: "same-origin" })
        .then(function (r) {
          if (!r.ok) throw new Error("graph.json を読めない（" + r.status + "）");
          return r.json();
        })
        .catch(function (e) {
          delete graphs[url];
          throw e;
        });
    }
    return graphs[url];
  }

  // ---------------------------------------------------------------- データ

  function strings(v) {
    return Array.isArray(v) ? v.filter(function (x) { return typeof x === "string" && x; }) : [];
  }

  function targetOf(ref) { return String(ref).split("#")[0]; } // id#anchor → id

  function routeTargets(routes) {
    var out = [];
    (Array.isArray(routes) ? routes : []).forEach(function (r) {
      if (typeof r === "string") out.push(targetOf(r));
      else if (r && Array.isArray(r.to)) strings(r.to).forEach(function (t) { out.push(targetOf(t)); });
    });
    return out;
  }

  function edgeKind(e) {
    var k = String(e.kind || e.type || "prerequisite");
    return /^route/.test(k) ? "route" : /^rel/.test(k) ? "related" : "prerequisite";
  }

  // graph.json → 地図が使う形。ページの id → ページ、辺の向き（parents・children）、分野の並び、レベルの段
  function indexGraph(g) {
    g = g || {};
    var raw = Array.isArray(g.pages) ? g.pages : Array.isArray(g.nodes) ? g.nodes : [];
    var pages = raw.filter(function (p) { return p && typeof p.id === "string" && p.id; });
    var byId = new Map();
    pages.forEach(function (p) { if (!byId.has(p.id)) byId.set(p.id, p); });
    pages = Array.from(byId.values());

    var edges = [];
    var seen = new Set();
    function addEdge(s, t, kind) {
      if (s === t || !byId.has(s) || !byId.has(t)) return;
      var key = s + "\u0001" + t + "\u0001" + kind;
      if (seen.has(key)) return;
      seen.add(key);
      edges.push({ s: s, t: t, kind: kind });
    }
    var related = new Map();
    if (Array.isArray(g.edges)) {
      g.edges.forEach(function (e) {
        if (!e) return;
        var s = targetOf(e.source != null ? e.source : e.from);
        var t = targetOf(e.target != null ? e.target : e.to);
        var kind = edgeKind(e);
        if (kind === "related") {
          if (!related.has(s)) related.set(s, []);
          related.get(s).push(t);
        } else {
          addEdge(s, t, kind);
        }
      });
    } else {
      pages.forEach(function (p) {
        strings(p.prerequisites).forEach(function (q) { addEdge(targetOf(q), p.id, "prerequisite"); });
        routeTargets(p.routes).forEach(function (t) { addEdge(p.id, t, "route"); });
      });
    }
    pages.forEach(function (p) {
      var rel = strings(p.related).map(targetOf).concat(related.get(p.id) || []);
      p._related = rel.filter(function (r, k) { return r !== p.id && byId.has(r) && rel.indexOf(r) === k; });
    });

    var parents = new Map();
    var children = new Map();
    edges.forEach(function (e) {
      if (!children.has(e.s)) children.set(e.s, []);
      children.get(e.s).push(e.t);
      if (!parents.has(e.t)) parents.set(e.t, []);
      parents.get(e.t).push(e.s);
    });

    var fields = [];
    var fieldTitle = new Map();
    (Array.isArray(g.fields) ? g.fields : []).forEach(function (f) {
      var id = typeof f === "string" ? f : f && f.id;
      if (typeof id !== "string" || fieldTitle.has(id)) return;
      fieldTitle.set(id, (f && f.title) || id);
      fields.push({ id: id, title: fieldTitle.get(id) });
    });
    pages.forEach(function (p) {
      if (typeof p.field === "string" && !fieldTitle.has(p.field)) {
        fieldTitle.set(p.field, p.field);
        fields.push({ id: p.field, title: p.field });
      }
    });
    var hasPages = new Set(pages.map(function (p) { return p.field; }));
    var levels = strings(g.levels);
    var rank = new Map(levels.map(function (l, i) { return [l, Math.min(i + 1, MAX_LEVELS)]; }));
    return {
      pages: pages, byId: byId, edges: edges, parents: parents, children: children, fields: fields,
      fieldTitle: fieldTitle, hasPages: hasPages, levels: levels, rank: rank,
    };
  }

  function levelRank(G, p) { return (p && G.rank.get(p.level)) || 0; }

  // ---------------------------------------------------------------- 名前で探す

  // 照合の規則は filter.js の window.CAMatch（絞り込みの欄と同じ）。読めなかったときだけ、最低限の規則で代える
  function matcher() {
    if (window.CAMatch) return window.CAMatch;
    return {
      norm: function (s) { return String(s == null ? "" : s).normalize("NFKC").toLowerCase().replace(/[\s\-_・]+/g, ""); },
      synonyms: function () { return []; },
    };
  }

  var PAREN = /[（(]([^（）()]*)[）)]/g;

  // ページの名前（正規化したもの）：題名・短い題名・別名と、それぞれのかっこの中と外、id
  function pageNames(p, norm) {
    var out = [];
    [p.title, p.nav_title].concat(strings(p.aliases)).forEach(function (t) {
      if (!t) return;
      out.push(t);
      var inner = [];
      var outer = String(t).replace(PAREN, function (_m, x) { inner.push(x); return ""; });
      if (inner.length) out = out.concat([outer], inner);
    });
    out.push(p.id);
    var seen = new Set();
    return out.map(norm).filter(function (n) {
      if (!n || seen.has(n)) return false;
      seen.add(n);
      return true;
    });
  }

  function compareKeys(a, b) {
    for (var i = 0; i < a.length; i++) if (a[i] !== b[i]) return a[i] - b[i];
    return 0;
  }

  // 語に合うページを、よく合う順に並べる。完全一致（0）→ 前方一致（1）→ 部分一致（2）の段で比べ、同じ段では
  // 当たった名前が短い → レベルの低い → graph.json の順。語そのものに合うページがなければ、言い換えでも探す
  function findPages(G, query) {
    var M = matcher();
    if (!G.names) G.names = new Map(G.pages.map(function (p) { return [p.id, pageNames(p, M.norm)]; }));
    var q = M.norm(query);
    if (!q) return [];
    var tries = [[q], M.synonyms(query).map(function (s) { return s.n; })];
    for (var t = 0; t < tries.length; t++) {
      var vs = tries[t];
      var found = [];
      G.pages.forEach(function (p, i) {
        var best = null;
        G.names.get(p.id).forEach(function (n) {
          vs.forEach(function (v) {
            var at = n.indexOf(v);
            if (at < 0) return;
            var r = levelRank(G, p);
            var key = [n === v ? 0 : at === 0 ? 1 : 2, n.length, r || MAX_LEVELS + 1, i];
            if (!best || compareKeys(key, best) < 0) best = key;
          });
        });
        if (best) found.push({ p: p, key: best });
      });
      if (found.length) {
        return found.sort(function (a, b) { return compareKeys(a.key, b.key); }).map(function (x) { return x.p; });
      }
    }
    return [];
  }

  // 祖先（前をたどったすべて）と、深さつきの子孫
  function relatives(G, id, depth) {
    var anc = new Set();
    var stack = [id];
    while (stack.length) {
      var x = stack.pop();
      (G.parents.get(x) || []).forEach(function (q) {
        if (q !== id && !anc.has(q)) {
          anc.add(q);
          stack.push(q);
        }
      });
    }
    var desc = new Map();
    var frontier = [id];
    var d = 0;
    while (frontier.length && (!depth || d < depth)) {
      d++;
      var next = [];
      frontier.forEach(function (x) {
        (G.children.get(x) || []).forEach(function (c) {
          if (c !== id && !desc.has(c)) {
            desc.set(c, d);
            next.push(c);
          }
        });
      });
      frontier = next;
    }
    return { anc: anc, desc: desc };
  }

  // 子孫が多すぎないように始めの深さを決める（0 はすべて）
  function autoDepth(G, id) {
    var all = relatives(G, id, 0).desc;
    if (all.size <= MAX_DESCENDANTS) return 0;
    var best = 1;
    for (var d = 2; d <= 3; d++) {
      var c = 0;
      all.forEach(function (v) { if (v <= d) c++; });
      if (c <= MAX_DESCENDANTS) best = d;
    }
    return best;
  }

  // ---------------------------------------------------------------- 文字の大きさと色

  var ctx2d = null;
  var sizeCache = new Map();

  function textWidth(text, font) {
    if (!ctx2d) ctx2d = document.createElement("canvas").getContext("2d");
    ctx2d.font = font;
    return ctx2d.measureText(text).width;
  }

  // 日本語は単語の区切りがないので、英数字の並びは1語、それ以外は1文字ずつで折り返す
  function wrapLine(text, font, maxW) {
    var tokens = text.match(/[A-Za-z0-9_.+#'-]+|\s+|[^\sA-Za-z0-9_.+#'-]/g) || [text];
    var lines = [];
    var cur = "";
    tokens.forEach(function (tok) {
      if (!cur && /^\s+$/.test(tok)) return;
      if (cur && textWidth(cur + tok, font) > maxW) {
        lines.push(cur.replace(/\s+$/, ""));
        cur = /^\s+$/.test(tok) ? "" : tok;
      } else {
        cur += tok;
      }
      while (cur.length > 1 && textWidth(cur, font) > maxW) {
        var k = cur.length - 1;
        while (k > 1 && textWidth(cur.slice(0, k), font) > maxW) k--;
        lines.push(cur.slice(0, k));
        cur = cur.slice(k);
      }
    });
    if (cur.replace(/\s+$/, "")) lines.push(cur.replace(/\s+$/, ""));
    return lines.length ? lines : [text];
  }

  // 折り返したラベルと、それが収まる点の幅・高さ
  function labelBox(text, family, size) {
    var font = size + "px " + family;
    var key = font + "\u0000" + text;
    var hit = sizeCache.get(key);
    if (hit) return hit;
    var maxW = MAX_LABEL_W * size / FONT_SIZE;
    var lines = [];
    String(text).split("\n").forEach(function (t) { lines = lines.concat(wrapLine(t, font, maxW)); });
    var w = 0;
    lines.forEach(function (l) { w = Math.max(w, textWidth(l, font)); });
    var box = {
      label: lines.join("\n"),
      w: Math.ceil(w) + 2 * PAD_X,
      h: Math.ceil(lines.length * size * LINE_HEIGHT) + 2 * PAD_Y,
    };
    sizeCache.set(key, box);
    return box;
  }

  function parseColor(s) {
    var m = /rgba?\(([^)]+)\)/.exec(s || "");
    if (!m) return [0, 0, 0, 1];
    var p = m[1].split(/[\s,/]+/).filter(Boolean).map(Number);
    return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
  }

  // CSS の色（変数を含む）を、背景に重ねた不透明な rgb() にする。Cytoscape.js は 8 桁の16進数と透明度を扱えない
  function cssColor(root, expr) {
    var probe = document.createElement("span");
    probe.style.display = "none";
    probe.style.color = expr;
    root.appendChild(probe);
    var c = getComputedStyle(probe).color;
    probe.remove();
    return parseColor(c);
  }

  function over(c, bg) {
    var a = c[3];
    return "rgb(" + [0, 1, 2].map(function (i) { return Math.round(c[i] * a + bg[i] * (1 - a)); }).join(",") + ")";
  }

  function palette(root) {
    var bg = cssColor(root, "var(--md-default-bg-color)");
    bg[3] = 1;
    function v(name) { return over(cssColor(root, "var(" + name + ")"), bg); }
    var P = {
      bg: over(bg, bg),
      fg: v("--md-default-fg-color"),
      fgLight: v("--md-default-fg-color--light"),
      fgLighter: v("--md-default-fg-color--lighter"),
      accent: v("--md-accent-fg-color"),
      primary: v("--md-primary-fg-color"),
      route: v("--ca-route-color"),
      lv: {},
      font: getComputedStyle(root).fontFamily || "sans-serif",
    };
    for (var i = 1; i <= MAX_LEVELS; i++) P.lv[i] = v("--ca-lv-" + i);
    return P;
  }

  function buildStyle(P) {
    var s = [
      {
        selector: "node",
        style: {
          shape: "round-rectangle",
          width: "data(w)",
          height: "data(h)",
          label: "data(label)",
          "text-wrap": "wrap",
          "text-max-width": "2000px",
          "text-valign": "center",
          "text-halign": "center",
          "font-size": FONT_SIZE,
          "line-height": LINE_HEIGHT,
          "font-family": P.font,
          color: P.fg,
          "background-color": P.bg,
          "border-width": 2,
          "border-color": P.fgLighter,
        },
      },
      { selector: "node.ext", style: { "border-style": "dashed", color: P.fgLight } },
      { selector: "node.rel", style: { "border-style": "dotted", color: P.fgLight } },
      {
        selector: "node.relbox",
        style: {
          shape: "round-rectangle",
          label: "data(label)",
          "text-valign": "top",
          "text-halign": "center",
          "text-margin-x": "data(lx)", // 「関連」の文字は囲みの左の端に寄せる（中央は選んだページからの線が通る）
          "font-size": 11,
          color: P.fgLight,
          "background-color": P.fgLighter,
          "background-opacity": 0.06,
          "border-width": 1,
          "border-style": "dashed",
          "border-color": P.fgLighter,
          padding: 10,
        },
      },
      {
        selector: "node.field",
        style: { "border-color": P.primary, "border-width": 2, "font-size": FIELD_FONT_SIZE },
      },
      { selector: "node.next", style: { "border-color": P.primary, "border-style": "dashed", color: P.fgLight } },
      { selector: "node.src", style: { "overlay-color": P.accent, "overlay-opacity": 0.25, "overlay-padding": 4 } },
      { selector: "node.focus", style: { "border-width": 4, "font-weight": "bold" } },
      { selector: "node.hover", style: { "overlay-color": P.fg, "overlay-opacity": 0.08, "overlay-padding": 3 } },
      {
        selector: "edge",
        style: {
          width: 1.5,
          "curve-style": "bezier",
          "line-color": P.fgLighter,
          "target-arrow-color": P.fgLighter,
          "target-arrow-shape": "triangle",
          "arrow-scale": 0.9,
        },
      },
      { selector: "edge.route", style: { "line-style": "dashed", "line-color": P.route, "target-arrow-color": P.route } },
      { selector: "edge.agg", style: { width: "data(wpx)" } },
      { selector: "edge.weak", style: { opacity: 0.5 } },
      { selector: "edge.rel", style: { "line-style": "dotted", "target-arrow-shape": "none", width: 1.2, opacity: 0.8 } },
      { selector: "edge.hl", style: { width: 3, "line-color": P.accent, "target-arrow-color": P.accent, "z-index": 10 } },
    ];
    for (var i = 1; i <= MAX_LEVELS; i++) s.push({ selector: "node.lv-" + i, style: { "border-color": P.lv[i] } });
    return s;
  }

  // ---------------------------------------------------------------- 画面の部品

  function html(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function button(text) {
    var b = html("button", null, text);
    b.type = "button";
    return b;
  }

  function buildUI(root) {
    root.textContent = "";
    var toolbar = html("div", "ca-map__toolbar");
    var seg = html("div", "ca-map__seg");
    seg.setAttribute("role", "group");
    seg.setAttribute("aria-label", "表示のしかた");
    var bField = button("分野ごと");
    var bAll = button("全体（分野）");
    seg.append(bField, bAll);
    var fieldLabel = html("label", null, "分野");
    var fieldSel = document.createElement("select");
    fieldLabel.appendChild(fieldSel);
    var findLabel = html("label", null, "ページ");
    var find = document.createElement("input");
    find.type = "search";
    find.placeholder = "名前・別名で探して中心に";
    find.setAttribute("autocomplete", "off");
    find.setAttribute("enterkeyhint", "search");
    find.setAttribute("list", "ca-map-pages");
    find.setAttribute("aria-label", "ページを名前で探して、その前後を表示する");
    findLabel.appendChild(find);
    var list = document.createElement("datalist");
    list.id = "ca-map-pages";
    var depthLabel = html("label", null, "次に読むの深さ");
    var depthSel = document.createElement("select");
    [["1", "1"], ["2", "2"], ["3", "3"], ["0", "すべて"]].forEach(function (o) { depthSel.add(new Option(o[1], o[0])); });
    depthLabel.appendChild(depthSel);
    depthLabel.hidden = true;
    var bFit = button("全体を収める");
    toolbar.append(seg, fieldLabel, findLabel, list, depthLabel, bFit);

    var status = html("p", "ca-map__status");
    status.setAttribute("aria-live", "polite");
    // 地図と、その上に重ねる点の説明。説明は地図の中に出すので、狭い画面でも点を押した場所から離れない
    var stage = html("div", "ca-map__stage");
    var canvas = html("div", "ca-map__canvas");
    canvas.setAttribute("role", "img");
    canvas.setAttribute("aria-label", "ページの前提と振り分けの図。同じつながりは、各ページの下の前提・次に読む・関連にもある");
    var info = html("div", "ca-map__info");
    info.hidden = true;
    info.setAttribute("role", "region");
    info.setAttribute("aria-label", "点の説明");
    info.setAttribute("aria-live", "polite");
    var infoClose = button("×");
    infoClose.className = "ca-map__close";
    infoClose.setAttribute("aria-label", "説明を閉じる");
    infoClose.title = "説明を閉じる（Esc）";
    var infoBody = html("div", "ca-map__info-body");
    info.append(infoClose, infoBody);
    stage.append(canvas, info);

    var legend = html("ul", "ca-map__legend");
    root.append(toolbar, status, stage, legend);
    return {
      bField: bField, bAll: bAll, fieldLabel: fieldLabel, fieldSel: fieldSel, find: find, list: list,
      depthLabel: depthLabel, depthSel: depthSel, bFit: bFit, status: status, canvas: canvas, info: info,
      infoClose: infoClose, infoBody: infoBody, legend: legend,
    };
  }

  function fillLegend(ul, G) {
    function item(sw, text) {
      var li = html("li");
      if (sw) {
        var s = html("span", "ca-sw " + sw);
        s.setAttribute("aria-hidden", "true");
        li.appendChild(s);
      }
      li.appendChild(document.createTextNode(text));
      ul.appendChild(li);
    }
    G.levels.forEach(function (l, i) { item("ca-lv-" + Math.min(i + 1, MAX_LEVELS), l); });
    item("ca-sw--edge", "実線の矢印：前提（矢印の先のページの前に読む）");
    item("ca-sw--route", "破線の矢印：症状のページから、原因ごとの対処のページへ");
    item("ca-sw--ext", "破線の枠：ほかの分野のページ");
    if (G.pages.some(function (p) { return p._related.length; })) item("ca-sw--rel", "点線：関連（焦点の表示だけ。配置には使わない）");
  }

  // ---------------------------------------------------------------- 地図

  function createMap(root, ui, G) {
    var P = palette(root);
    var cy = window.cytoscape({
      container: ui.canvas,
      elements: [],
      style: buildStyle(P),
      minZoom: 0.08,
      maxZoom: 2.5,
      boxSelectionEnabled: false,
      autoungrabify: true, // 点は動かせない（指で触ると地図全体が動く）
      autounselectify: true,
    });
    var state = { view: "field", field: null, focus: null, depth: 0 };
    var notice = "";
    var holdUntil = 0;
    var api = { root: root, cy: cy, state: state, timings: {} };

    function pageNode(p, extra) {
      var box = labelBox(p.nav_title || p.title || p.id, P.font, FONT_SIZE);
      var cls = ["page", "lv-" + levelRank(G, p)].concat(extra || []);
      return { group: "nodes", data: { id: p.id, label: box.label, w: box.w, h: box.h }, classes: cls.join(" ") };
    }

    function edge(s, t, kind) {
      var cls = kind === "route" ? "route" : kind === "rel" ? "rel" : "";
      return { group: "edges", data: { id: s + "->" + t + ":" + (kind || "p"), source: s, target: t }, classes: cls };
    }

    function edgesAmong(ids) {
      return G.edges.filter(function (e) { return ids.has(e.s) && ids.has(e.t); }).map(function (e) { return edge(e.s, e.t, e.kind); });
    }

    // 分野のページ＋ほかの分野の直接の前（1ページずつ）＋この分野の先にある分野（分野ごとに1つの「→」の点にまとめる）。
    // 「→」の点は配置に使わず、配置の後で右に並べる。辺は引かず、マウスを乗せる・長押しすると元のページを光らせる
    function fieldElements(field) {
      var core = new Set();
      G.pages.forEach(function (p) { if (p.field === field) core.add(p.id); });
      var ext = new Set();
      var next = new Map(); // 分野 → その分野の、core から辺が入るページ
      core.forEach(function (id) {
        (G.parents.get(id) || []).forEach(function (q) { if (!core.has(q)) ext.add(q); });
        (G.children.get(id) || []).forEach(function (c) {
          if (core.has(c)) return;
          var f = G.byId.get(c).field;
          if (!next.has(f)) next.set(f, new Set());
          next.get(f).add(c);
        });
      });
      var els = [];
      core.forEach(function (id) { els.push(pageNode(G.byId.get(id))); });
      ext.forEach(function (id) { els.push(pageNode(G.byId.get(id), ["ext"])); });
      next.forEach(function (pages, f) {
        var box = labelBox("→ " + (G.fieldTitle.get(f) || f) + "\n" + pages.size + " ページ", P.font, FONT_SIZE);
        var sources = [];
        core.forEach(function (id) {
          if ((G.children.get(id) || []).some(function (c) { return pages.has(c); })) sources.push(id);
        });
        els.push({
          group: "nodes",
          data: { id: "next:" + f, field: f, label: box.label, w: box.w, h: box.h, pages: Array.from(pages), sources: sources },
          classes: "next",
        });
      });
      var shown = new Set(core);
      ext.forEach(function (id) { shown.add(id); });
      // ほかの分野どうしの辺は引かない（この分野のページに触れる辺だけ）
      edgesAmong(shown).forEach(function (e) {
        if (core.has(e.data.source) || core.has(e.data.target)) els.push(e);
      });
      return { elements: els, core: core.size, ext: ext.size, next: next.size };
    }

    function focusElements(id, depth) {
      var R = relatives(G, id, depth);
      var ids = new Set([id]);
      R.anc.forEach(function (x) { ids.add(x); });
      R.desc.forEach(function (_d, x) { ids.add(x); });
      var els = [];
      ids.forEach(function (x) { els.push(pageNode(G.byId.get(x), x === id ? ["focus"] : [])); });
      els = els.concat(edgesAmong(ids));
      return { elements: els, anc: R.anc.size, desc: R.desc.size, total: relatives(G, id, 0).desc.size };
    }

    function overviewElements() {
      var count = new Map(G.fields.map(function (f) { return [f.id, 0]; }));
      G.pages.forEach(function (p) { if (count.has(p.field)) count.set(p.field, count.get(p.field) + 1); });
      var els = G.fields.filter(function (f) { return G.hasPages.has(f.id); }).map(function (f) {
        var box = labelBox(f.title + "\n" + count.get(f.id) + " ページ", P.font, FIELD_FONT_SIZE);
        return { group: "nodes", data: { id: "field:" + f.id, field: f.id, label: box.label, w: box.w, h: box.h }, classes: "field" };
      });
      var agg = new Map();
      G.edges.forEach(function (e) {
        var a = G.byId.get(e.s).field;
        var b = G.byId.get(e.t).field;
        if (a === b) return;
        var k = a + ">" + b;
        agg.set(k, (agg.get(k) || 0) + 1);
      });
      var max = 1;
      agg.forEach(function (n) { max = Math.max(max, n); });
      agg.forEach(function (n, k) {
        var ab = k.split(">");
        els.push({
          group: "edges",
          data: { id: "agg:" + k, source: "field:" + ab[0], target: "field:" + ab[1], n: n, wpx: 1 + 5 * Math.sqrt(n / max) },
          classes: n === 1 ? "agg weak" : "agg",
        });
      });
      return { elements: els };
    }

    // 関連の囲みの中の並び：点を列ごとに上から詰める。列の数は 1〜3 のうち、囲みが地図に最も大きく入るもの
    function relGrid(nodes) {
      var best = null;
      for (var cols = 1; cols <= Math.min(3, nodes.length); cols++) {
        var rows = Math.ceil(nodes.length / cols);
        var colW = [];
        var colH = [];
        var pos = nodes.map(function (nd, k) {
          var c = Math.floor(k / rows);
          var y = colH[c] || 0;
          colW[c] = Math.max(colW[c] || 0, nd.data.w);
          colH[c] = y + nd.data.h + REL_GAP;
          return { c: c, y: y + nd.data.h / 2 };
        });
        var xs = [];
        var x = REL_PAD;
        colW.forEach(function (w, c) { xs[c] = x + w / 2; x += w + REL_GAP * 2; });
        var w = x - REL_GAP * 2 + REL_PAD;
        var h = REL_LABEL + 2 * REL_PAD + Math.max.apply(null, colH) - REL_GAP;
        var z = Math.min((cy.width() - 48) / w, (cy.height() - 48) / h);
        if (!best || z > best.z + 1e-9) {
          best = { z: z, w: w, h: h, at: pos.map(function (q) { return { x: xs[q.c], y: REL_LABEL + REL_PAD + q.y }; }) };
        }
      }
      return best;
    }

    // related は配置の後で足す（配置には使わない）。図にまだない関連のページは「関連」の囲みに入れ、選んだページの
    // すぐ下（か上）の空いた所に置く。ほかの点と重なれば、重なった点の外までずらし、上下で近い方を選ぶ
    function addRelated(id) {
      var rel = G.byId.get(id)._related;
      if (!rel.length) return;
      var f = cy.getElementById(id);
      var fb = f.boundingBox();
      var missing = rel.filter(function (r) { return cy.getElementById(r).empty(); });
      var nodes = missing.map(function (r) { return pageNode(G.byId.get(r), ["rel"]); });
      var adds = [];
      if (nodes.length) {
        var grid = relGrid(nodes);
        var cx = (fb.x1 + fb.x2) / 2;
        var x1 = cx - grid.w / 2;
        var x2 = cx + grid.w / 2;
        var others = cy.nodes().not(f).map(function (n) { return n.boundingBox(); });
        var half = REL_MARGIN / 2;
        var clash = function (top) {
          return others.filter(function (b) {
            return b.x2 > x1 - half && b.x1 < x2 + half && b.y2 > top - half && b.y1 < top + grid.h + half;
          });
        };
        var below = fb.y2 + REL_MARGIN;
        var above = fb.y1 - REL_MARGIN - grid.h;
        for (var k = 0, c; k < 500 && (c = clash(below)).length; k++) {
          below = Math.max.apply(null, c.map(function (b) { return b.y2; })) + REL_MARGIN;
        }
        for (k = 0; k < 500 && (c = clash(above)).length; k++) {
          above = Math.min.apply(null, c.map(function (b) { return b.y1; })) - REL_MARGIN - grid.h;
        }
        var top = below - fb.y2 <= fb.y1 - (above + grid.h) ? below : above;
        adds.push({ group: "nodes", data: { id: "__related", label: "関連", w: 1, h: 1, lx: REL_PAD + 12 - grid.w / 2 }, classes: "relbox" });
        nodes.forEach(function (nd, i) {
          nd.data.parent = "__related";
          nd.position = { x: x1 + grid.at[i].x, y: top + grid.at[i].y };
          adds.push(nd);
        });
      }
      rel.forEach(function (r) { adds.push(edge(id, r, "rel")); });
      cy.add(adds);
    }

    // 「→」の点を、元のページの高さの平均の順に、図の右に1列に並べる
    function placeNext() {
      var nexts = cy.nodes(".next");
      if (nexts.empty()) return;
      var bb = cy.elements().not(nexts).boundingBox();
      var items = nexts.map(function (n) {
        var ys = n.data("sources").map(function (id) { return cy.getElementById(id).position("y"); });
        return { n: n, y: ys.reduce(function (a, b) { return a + b; }, 0) / Math.max(1, ys.length) };
      }).sort(function (a, b) { return a.y - b.y; });
      var total = items.reduce(function (t, it) { return t + it.n.data("h") + 12; }, -12);
      var y = (bb.y1 + bb.y2) / 2 - total / 2;
      var x = bb.x2 + 70;
      items.forEach(function (it) {
        it.n.position({ x: x + it.n.data("w") / 2, y: y + it.n.data("h") / 2 });
        y += it.n.data("h") + 12;
      });
    }

    function fit() {
      var eles = cy.elements();
      if (eles.empty()) return;
      cy.resize(); // 入れ物の大きさが変わっていても合わせる
      cy.fit(eles, 24);
      if (state.view === "all" || cy.zoom() >= READABLE_ZOOM) return; // 全体の図は点が少ないので必ず全部を収める
      cy.zoom(READABLE_ZOOM);
      var bb = eles.boundingBox();
      var h = cy.height();
      if (state.view === "focus") {
        // 選んだページと関連の囲みが両方入るように寄せる。読める倍率で入らなければ、MIN_FOCUS_ZOOM まで倍率を下げる
        var target = cy.getElementById(state.focus).union(cy.getElementById("__related"));
        var tb = target.boundingBox();
        var zf = Math.min(READABLE_ZOOM, (cy.width() - 48) / tb.w, (h - 48) / tb.h);
        cy.zoom(Math.max(MIN_FOCUS_ZOOM, zf));
        cy.center(target);
      } else {
        // 左（前の側）から読めるように、左端をそろえ、縦は収まれば中央、収まらなければ上をそろえる
        var z = cy.zoom();
        var py = bb.h * z <= h - 48 ? (h - bb.h * z) / 2 - bb.y1 * z : 24 - bb.y1 * z;
        cy.pan({ x: 24 - bb.x1 * z, y: py });
      }
    }

    function setStatus(parts, withClear) {
      ui.status.textContent = (notice ? notice + " " : "") + parts;
      if (withClear) {
        var b = button("解除");
        b.addEventListener("click", function () { setState({ view: "field", field: G.byId.get(state.focus).field }); });
        ui.status.appendChild(b);
      }
    }

    function showStatus(built) {
      if (state.view === "all") {
        setStatus("分野どうしのつながりを、辺の太さ（分野をまたぐ辺の本数）で表す。分野を押すとその分野の表示になる。");
      } else if (state.view === "focus") {
        var p = G.byId.get(state.focus);
        var shown = built.desc < built.total ? "（全 " + built.total + " ページのうち、深さ " + state.depth + " まで）" : "";
        setStatus((p.nav_title || p.title || p.id) + "：前にあるページ " + built.anc + "・先にあるページ " + built.desc + shown +
          "。前提と、症状のページからの振り分けをたどる。", true);
      } else {
        setStatus((G.fieldTitle.get(state.field) || state.field) + "：" + built.core + " ページ。破線の枠はほかの分野にある前の" +
          "ページ、「→」はこの分野の先にある分野（押すとその分野へ）。");
      }
    }

    function render() {
      var t0 = performance.now();
      var built;
      if (state.view === "all") built = overviewElements();
      else if (state.view === "focus") built = focusElements(state.focus, state.depth);
      else built = fieldElements(state.field);
      var t1 = performance.now();
      cy.batch(function () {
        cy.elements().remove();
        cy.add(built.elements);
      });
      var t2 = performance.now();
      cy.elements().not(".next").layout(state.view === "all" ? LAYOUT_FIELDS : LAYOUT).run();
      placeNext();
      var t3 = performance.now();
      if (state.view === "focus") addRelated(state.focus);
      fit();
      var t4 = performance.now();

      showStatus(built);
      notice = "";
      syncToolbar();
      writeQuery();
      api.timings = {
        build: t1 - t0, add: t2 - t1, layout: t3 - t2, after: t4 - t3, total: t4 - t0,
        nodes: cy.nodes().length, edges: cy.edges().length,
      };
      requestAnimationFrame(function () {
        api.timings.firstFrame = performance.now() - t0; // 描き始めてから最初の画面まで
      });
    }

    function setState(patch) {
      Object.keys(patch).forEach(function (k) { state[k] = patch[k]; });
      if (state.view === "focus" && patch.focus && !("depth" in patch)) state.depth = autoDepth(G, state.focus);
      closeInfo();
      render();
    }

    function syncToolbar() {
      ui.bField.setAttribute("aria-pressed", String(state.view !== "all"));
      ui.bAll.setAttribute("aria-pressed", String(state.view === "all"));
      ui.fieldLabel.hidden = state.view !== "field";
      ui.fieldSel.value = state.field || "";
      ui.depthLabel.hidden = state.view !== "focus";
      ui.depthSel.value = String(state.depth || 0);
    }

    function writeQuery() {
      var q = new URLSearchParams();
      if (state.view === "focus") {
        q.set("focus", state.focus);
        if (state.depth) q.set("depth", String(state.depth));
      } else if (state.view === "all") {
        q.set("view", "all");
      } else if (state.field) {
        q.set("field", state.field);
      }
      var qs = q.toString();
      try {
        history.replaceState(history.state, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
      } catch (e) { /* 書き換えられなくても表示は続ける */ }
    }

    function pageUrl(p) { return new URL(p.url || "", ROOT).href; }

    // instant navigation に任せるため、location を直接変えずにリンクを押す
    function navigate(url) {
      var a = document.createElement("a");
      a.href = url;
      a.hidden = true;
      document.body.appendChild(a);
      a.click();
      a.remove();
    }

    // ---- 点の説明（地図の中に重ねる）
    // 固定（pinned）した説明は、×・Esc・地図の空いた所を押すまで残り、マウスを乗せたほかの点の説明に替わらない。
    // マウスを乗せただけの説明は仮のもので、点と説明の両方から離れると少し待って消える
    var pinned = false;
    var overInfo = false;
    var hideTimer = 0;

    function openInfo(fill, n, pin) {
      clearTimeout(hideTimer);
      ui.infoBody.textContent = "";
      fill(ui.infoBody);
      if (!pin) ui.infoBody.appendChild(html("p", "ca-map__hint", "点を押すと、この説明を固定する"));
      pinned = !!pin;
      ui.info.classList.toggle("ca-map__info--pinned", pinned);
      // 点が地図の下半分にあれば説明を上に、上半分にあれば下に重ねて、点を隠さない
      ui.info.classList.toggle("ca-map__info--top", !!n && n.renderedPosition("y") > cy.height() / 2);
      ui.info.hidden = false;
      if (pinned) reveal(ui.info);
    }

    function closeInfo() {
      clearTimeout(hideTimer);
      pinned = false;
      overInfo = false;
      ui.info.hidden = true;
      cy.nodes(".src").removeClass("src");
    }

    function hideSoon() {
      if (pinned) return;
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () { if (!pinned && !overInfo) closeInfo(); }, 400);
    }

    // 説明が画面の外（固定のヘッダーの下を含む）にあれば、見える所までページを送る
    function reveal(el) {
      var r = el.getBoundingClientRect();
      var header = document.querySelector(".md-header");
      var top = (header ? Math.max(0, header.getBoundingClientRect().bottom) : 0) + 8;
      var bottom = window.innerHeight - 8;
      var dy = r.bottom > bottom ? r.bottom - bottom : 0;
      if (r.top - dy < top) dy = r.top - top;
      if (dy) window.scrollBy({ top: dy, behavior: "smooth" });
    }

    function fillPage(box, p) {
      var head = html("p", "ca-map__info-head");
      var link = html("a", null, p.title || p.id);
      link.href = pageUrl(p);
      var strong = html("strong");
      strong.appendChild(link);
      head.appendChild(strong);
      if (p.level) head.append(" ", html("span", "ca-mini ca-lv-" + levelRank(G, p), p.level));
      head.append(" " + (G.fieldTitle.get(p.field) || p.field || ""));
      box.appendChild(head);
      if (p.summary) box.appendChild(html("p", null, p.summary));
      var acts = html("p", "ca-map__acts");
      var open = html("a", "ca-map__open", "ページを開く");
      open.href = pageUrl(p);
      acts.appendChild(open);
      if (!(state.view === "focus" && state.focus === p.id)) {
        var center = button("この点を中心に表示");
        center.addEventListener("click", function () { setState({ view: "focus", focus: p.id }); });
        acts.appendChild(center);
      }
      box.appendChild(acts);
    }

    function showPage(n, pin) {
      var p = G.byId.get(n.id());
      openInfo(function (box) { fillPage(box, p); }, n, pin);
    }

    function hover(n, on) {
      n.toggleClass("hover", on);
      n.connectedEdges().not(".rel").toggleClass("hl", on);
    }

    // 点を押す（クリック・タップ）・長押しで説明を固定する。ダブルクリック（ダブルタップ）でそのページへ移る
    cy.on("tap", "node.page", function (e) {
      if (Date.now() < holdUntil) return; // 長押しの直後の tap は、長押しで出した説明をそのままにする
      showPage(e.target, true);
    });
    cy.on("dbltap", "node.page", function (e) { navigate(pageUrl(G.byId.get(e.target.id()))); });
    cy.on("taphold", "node.page", function (e) {
      holdUntil = Date.now() + 1000;
      showPage(e.target, true);
    });
    cy.on("tap", "node.field, node.next", function (e) {
      if (Date.now() < holdUntil) return;
      setState({ view: "field", field: e.target.data("field") });
    });
    cy.on("tap", function (e) { if (e.target === cy && pinned) closeInfo(); }); // 地図の空いた所を押すと閉じる

    function showNext(n, on, pin) {
      n.toggleClass("hover", on);
      if (pinned && !pin) return; // 固定した説明は替えない
      cy.nodes(".src").removeClass("src");
      if (!on) { hideSoon(); return; }
      cy.collection(n.data("sources").map(function (id) { return cy.getElementById(id); }).filter(function (x) { return x.nonempty(); }))
        .addClass("src");
      var titles = n.data("pages").map(function (id) { var q = G.byId.get(id); return q.nav_title || q.title || id; });
      var text = "→ " + (G.fieldTitle.get(n.data("field")) || n.data("field")) + "：" + titles.slice(0, 8).join("・") +
        (titles.length > 8 ? " ほか " + (titles.length - 8) + " ページ" : "") + "。光っているページから辺が出る（押すとその分野の表示）";
      openInfo(function (box) { box.appendChild(html("p", null, text)); }, n, pin);
    }
    cy.on("mouseover", "node.next", function (e) { showNext(e.target, true, false); });
    cy.on("mouseout", "node.next", function (e) { showNext(e.target, false, false); });
    cy.on("taphold", "node.next", function (e) {
      holdUntil = Date.now() + 1000;
      showNext(e.target, true, true);
    });
    cy.on("mouseover", "node.page", function (e) {
      hover(e.target, true);
      if (!pinned) showPage(e.target, false);
    });
    cy.on("mouseover", "node.field", function (e) { hover(e.target, true); });
    cy.on("mouseout", "node.page, node.field", function (e) {
      hover(e.target, false);
      hideSoon();
    });
    cy.on("mouseover", "edge.agg", function (e) {
      if (pinned) return;
      var d = e.target.data();
      var text = (G.fieldTitle.get(d.source.slice(6)) || "") + " → " + (G.fieldTitle.get(d.target.slice(6)) || "") +
        "：分野をまたぐ辺 " + d.n + " 本";
      openInfo(function (box) { box.appendChild(html("p", null, text)); }, null, false);
    });
    cy.on("mouseout", "edge.agg", hideSoon);
    cy.on("pan zoom", function () { if (!pinned && !ui.info.hidden) closeInfo(); }); // 仮の説明は地図を動かすと消す

    // 点の上から地図の外へ一気に出ると、Cytoscape.js は点の mouseout を出さないので、地図から出たときにも仮の説明を消す
    ui.canvas.addEventListener("mouseleave", function () {
      cy.nodes(".hover").removeClass("hover");
      cy.edges(".hl").removeClass("hl");
      if (!pinned) cy.nodes(".src").removeClass("src");
      hideSoon();
    });
    ui.info.addEventListener("mouseenter", function () { overInfo = true; clearTimeout(hideTimer); });
    ui.info.addEventListener("mouseleave", function () { overInfo = false; hideSoon(); });
    ui.infoClose.addEventListener("click", closeInfo);
    function onKey(e) {
      if (e.key === "Escape" && !ui.info.hidden && root.isConnected) closeInfo();
    }
    document.addEventListener("keydown", onKey);

    // ツールバー：「ページ」欄の候補は題名と別名（別名は「→ 題名」を添える）。同じ文字の候補は最初の 1 つだけ
    G.fields.forEach(function (f) { if (G.hasPages.has(f.id)) ui.fieldSel.add(new Option(f.title, f.id)); });
    var listed = new Set();
    function addOption(value, label) {
      if (!value || listed.has(value)) return;
      listed.add(value);
      var o = document.createElement("option");
      o.value = value;
      if (label) o.label = label;
      ui.list.appendChild(o);
    }
    G.pages.forEach(function (p) { addOption(p.title, null); });
    G.pages.forEach(function (p) { strings(p.aliases).forEach(function (a) { addOption(a, "→ " + (p.title || p.id)); }); });
    ui.bField.addEventListener("click", function () {
      var f = state.field || (state.focus && G.byId.get(state.focus).field) || defaultField();
      setState({ view: "field", field: f });
    });
    ui.bAll.addEventListener("click", function () { setState({ view: "all" }); });
    ui.fieldSel.addEventListener("change", function () { setState({ view: "field", field: ui.fieldSel.value }); });
    ui.depthSel.addEventListener("change", function () { setState({ depth: Number(ui.depthSel.value) }); });
    // 「ページ」欄：いちばん合うページを中心にし、ほかの候補（5 件まで）を上の行にボタンで出す
    function showAlternatives(v, list) {
      if (!list.length) return;
      var span = html("span", "ca-map__alts");
      span.appendChild(document.createTextNode("「" + v + "」のほかの候補："));
      list.forEach(function (p) {
        var b = button(p.nav_title || p.title || p.id);
        b.addEventListener("click", function () { setState({ view: "focus", focus: p.id, field: p.field }); });
        span.appendChild(b);
      });
      ui.status.appendChild(span);
    }
    ui.find.addEventListener("change", function () {
      var v = ui.find.value.trim();
      var found = findPages(G, v);
      if (found.length) {
        ui.find.value = "";
        ui.find.blur(); // スマホではキーボードを閉じて地図を見せる
        setState({ view: "focus", focus: found[0].id, field: found[0].field });
        showAlternatives(v, found.slice(1, 6));
      } else if (v) {
        ui.status.textContent = "「" + v + "」に合うページがない。別名・英語名・名前の一部でも探せる。";
      }
    });
    ui.bFit.addEventListener("click", function () { cy.fit(cy.elements(), 24); });

    // 始めの分野：地図の div の data-field、なければ辺のある最初の分野、それもなければページのある最初の分野
    function defaultField() {
      var want = root.getAttribute("data-field");
      if (want && G.hasPages.has(want)) return want;
      var withEdges = new Set();
      G.edges.forEach(function (e) { withEdges.add(G.byId.get(e.s).field); withEdges.add(G.byId.get(e.t).field); });
      var f = G.fields.filter(function (x) { return withEdges.has(x.id); })[0] || G.fields.filter(function (x) { return G.hasPages.has(x.id); })[0];
      return f ? f.id : null;
    }

    function start(q) {
      if (q.focus && G.byId.has(q.focus)) {
        state.view = "focus";
        state.focus = q.focus;
        state.field = G.byId.get(q.focus).field;
        var d = q.depth == null ? NaN : Number(q.depth);
        state.depth = d >= 0 && d <= 3 && Math.floor(d) === d ? d : autoDepth(G, q.focus);
      } else if (q.view === "all") {
        state.view = "all";
        state.field = defaultField();
      } else {
        state.view = "field";
        state.field = q.field && G.hasPages.has(q.field) ? q.field : defaultField();
      }
      if (q.focus && !G.byId.has(q.focus)) notice = "ページ「" + q.focus + "」が地図にないので、分野ごとの表示にした。";
      render();
    }

    // ライトとダークの切り替えに追従する
    var observer = new MutationObserver(function () {
      P = palette(root);
      cy.style(buildStyle(P));
    });
    observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme", "data-md-color-primary", "data-md-color-accent"] });

    api.start = start;
    api.setState = setState;
    api.findPages = function (q) { return findPages(G, q).map(function (p) { return p.id; }); };
    api.destroy = function () {
      document.removeEventListener("keydown", onKey);
      clearTimeout(hideTimer);
      observer.disconnect();
      cy.destroy();
    };
    return api;
  }

  function parseQuery() {
    var q = new URLSearchParams(location.search);
    return { focus: q.get("focus"), field: q.get("field"), view: q.get("view"), depth: q.get("depth") };
  }

  function mount(root) {
    if (root.dataset.caMounted) return;
    root.dataset.caMounted = "1";
    var t0 = performance.now();
    var ui = buildUI(root);
    ui.status.textContent = "地図を読み込んでいる…";
    Promise.all([loadLibs(), loadGraph(graphUrl(root))])
      .then(function (res) {
        if (!root.isConnected) return;
        var t1 = performance.now();
        var G = indexGraph(res[1]);
        if (!G.pages.length) {
          ui.status.textContent = "地図に載せるページがまだない。";
          return;
        }
        fillLegend(ui.legend, G);
        var map = createMap(root, ui, G);
        current = map;
        root.caMap = map;
        map.start(parseQuery());
        map.timings.load = t1 - t0;
        map.timings.mount = performance.now() - t0;
      })
      .catch(function (e) {
        root.dataset.caMounted = "";
        ui.status.textContent = "地図を表示できなかった（" + e.message + "）。同じつながりは、各ページの下の前提・次に読む・関連にある。";
        console.error("claude-atlas: 知識マップを表示できなかった", e);
      });
  }

  function onDocument(doc) {
    if (current && !current.root.isConnected) {
      current.destroy();
      current = null;
    }
    var root = ((doc && doc.body) || document.body).querySelector(".ca-graph, #ca-map");
    if (root) mount(root);
  }

  window.CAMap = { indexGraph: indexGraph };

  if (window.document$) {
    window.document$.subscribe(onDocument);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { onDocument(document); });
  } else {
    onDocument(document);
  }
})();
