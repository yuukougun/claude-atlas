/*
 * claude-atlas：語の照合の規則と、語で表の行を絞り込む欄（planning/design.md §8.5。kyopro-atlas の
 * overrides/assets/js/filter.js〔Issue #59・#60〕を写して直した）
 *
 * 照合の規則（window.CAMatch）。知識マップの「ページ」欄（map.js）も同じ規則を使う
 * - norm(s)：NFKC で全角と半角をそろえ、小文字にし、カタカナをひらがなにし、空白と区切りの記号（- _ ・ ‐ − – ' ’）を除く。
 *   「Plan Mode」「plan-mode」「ＰＬＡＮ　ＭＯＤＥ」は同じになり、「ふっく」は「フック」に当たる
 * - 言い換え：同じものを指す語の組。語が組のどれかを含めば、それをほかの語に置き換えた形でも探す（組のどの語で探しても
 *   同じものが当たる）。組の語の後ろが語の終わりまでひらがなだけなら（送り仮名・助詞）、それを落として置き換える。
 *   組はコードに持たない（語彙を直書きしない）。作る層が欄の data-ca-synonyms（JSON の [[語, 語, …], …]）に書くか、
 *   ほかの JS が CAMatch.addSynonyms(組の列) で足す
 * - 語は空白で区切り、すべての語を含むものだけを残す
 *
 * 絞り込みの欄：本文に <div class="ca-filter"></div> を置いたページで、ページの題の下（要点の囲みの前）に欄を出す。
 * 要点は本文の最初に置く約束（planning/guides/common.md）なので、目印の div は要点の後に置いてよく、ここで前へ移す。
 * - 単位は表の行（tbody の tr。既定）か、data-ca-units="li" のとき本文の箇条書きの項目（article の直下の ul の li）。
 *   data-ca-sections="a b" のように ## の id を書くと、その節の中の表・箇条書きだけを単位にする（説明の箇条書きを除く）
 * - data-ca-placeholder：欄の中の例の文（なければ「語で行を絞り込む」）
 * - 語を入れると、語を含む単位と、それを含む表・箇条書き・見出し（## と ###）だけを残し、ほかの本文は隠す（残すものに
 *   ca-filter-keep を付け、ほかは CSS で隠す）。件数を出す。語を消すと元に戻る。語はアドレスの ?filter= に入れる
 *   （戻る・ブックマークで同じ絞り込みになる）
 * - 隠れた見出しへのリンク（目次など）を押したら、絞り込みを解いてから移る
 * - JS が動かない環境では目印の div は空のままで、表はそのまま見える
 * すべての JS と同じく、Material の document$ を購読して instant navigation のたびに取り付け直す。
 */
(function () {
  "use strict";

  // ---------------------------------------------------------------- 照合の規則

  var DROP = /[\s\-_・‐−–'’]+/g;
  var KANA_TAIL = /^[ぁ-ゖ]+$/; // ひらがなだけ（語の後ろの送り仮名・助詞）

  // NFKC で全角と半角をそろえ、小文字にし、区切りの記号を除く。kana が真ならカタカナをひらがなにする（カタカナとひらがなは
  // 1 字ずつ対応し、区切りの記号でもないので、kana の真偽で文字の位置は変わらない）
  function fold(s, kana) {
    var t = String(s == null ? "" : s).normalize("NFKC").toLowerCase();
    if (kana) {
      var out = "";
      for (var i = 0; i < t.length; i++) {
        var c = t.charCodeAt(i);
        out += c >= 0x30a1 && c <= 0x30f6 ? String.fromCharCode(c - 0x60) : t[i]; // カタカナ → ひらがな
      }
      t = out;
    }
    return t.replace(DROP, "");
  }

  function norm(s) { return fold(s, true); }

  var GROUPS = []; // 言い換えの組：[[{raw, n}, …], …]
  var SEEN_GROUPS = new Set();

  // 言い換えの組を足す（同じ組を二度は足さない）。組は 2 語以上の文字列の列
  function addSynonyms(groups) {
    (Array.isArray(groups) ? groups : []).forEach(function (g) {
      if (!Array.isArray(g)) return;
      var words = g.filter(function (w) { return typeof w === "string" && norm(w); });
      if (words.length < 2) return;
      var key = words.map(norm).sort().join("\u0001");
      if (SEEN_GROUPS.has(key)) return;
      SEEN_GROUPS.add(key);
      GROUPS.push(words.map(function (w) { return { raw: w, n: norm(w) }; }));
    });
  }

  // 組の語 a が、組の語 b の一部か（「取り除」は「取り除く」の一部）
  function partOf(a, b) { return b.n.length > a.n.length && b.n.indexOf(a.n) >= 0; }

  // 語 s（空白で区切った 1 語。正規化の前でも後でもよい）の言い換え：[{n: 探す形, from: 元の語, to: 言い換えの語}]。
  // 正規化した s そのものは含めない。to が "" の形は探すだけで、件数の行には出さない
  // - 語が同じ組の語を重ねて含むときは、長い方だけを置き換える
  // - 組の語の後ろが語の終わりまでひらがなだけなら（送り仮名・助詞）、そのひらがなごと置き換え、ひらがなを落としただけの形も
  //   探す。カタカナはひらがなにする前の形で見る（「設定ファイル」の「ファイル」は落とさない）
  // - 件数の行には、元の語と同じ語の別の形と、組のほかの語の一部の形を出さない
  function synonyms(s) {
    var q = norm(s);
    var k = fold(s, false); // q と同じ位置で、カタカナを残した形
    var out = [];
    function add(n, from, to) {
      if (!n || n === q) return;
      var o = out.filter(function (x) { return x.n === n; })[0];
      if (!o) out.push({ n: n, from: from, to: to });
      else if (to && !o.to) { o.from = from; o.to = to; }
    }
    GROUPS.forEach(function (g) {
      var found = g.filter(function (a) { return a.n && q.indexOf(a.n) >= 0; });
      found.forEach(function (a) {
        if (found.some(function (b) { return partOf(a, b); })) return;
        var at = q.lastIndexOf(a.n);
        var end = at + a.n.length;
        var tail = end < q.length && KANA_TAIL.test(k.slice(end)) ? k.slice(end) : "";
        var from = a.raw + tail;
        var put = function (w) { return tail ? q.slice(0, at).split(a.n).join(w) + w : q.split(a.n).join(w); };
        if (tail) add(put(a.n), from, "");
        g.forEach(function (b) {
          if (b === a) return;
          var hide = partOf(a, b) || g.some(function (c) { return partOf(b, c); });
          add(put(b.n), from, hide ? "" : b.raw);
        });
      });
    });
    return out;
  }

  // 語を空白（全角の空白も）で区切る。正規化すると空になる語（記号だけ）は除く
  function words(query) {
    return String(query || "").normalize("NFKC").split(/\s+/).filter(function (t) { return norm(t); });
  }

  // 空白で区切った語ごとに、[正規化した形, ...言い換え] の列
  function terms(query) {
    return words(query).map(function (t) {
      return [norm(t)].concat(synonyms(t).map(function (s) { return s.n; }));
    });
  }

  // 正規化した文字 text が、すべての語（のどれかの形）を含むか
  function test(text, ts) {
    return ts.every(function (vs) {
      return vs.some(function (v) { return text.indexOf(v) >= 0; });
    });
  }

  window.CAMatch = { norm: norm, synonyms: synonyms, words: words, terms: terms, test: test, addSynonyms: addSynonyms };

  // ---------------------------------------------------------------- 絞り込みの欄

  var PARAM = "filter";
  var DELAY = 150; // 打つたびに絞らず、少し待つ（ms）
  var SKIP = ".ca-page-head, .ca-page-links, .ca-map-link, .ca-page-info, .md-source-file, .md-content__button";
  var cache = new WeakMap(); // 単位の要素 → 正規化した文字（セルの境目をまたいで当たらないよう \u0001 でつなぐ）
  var current = null; // このページの欄

  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    if (text != null) e.textContent = text;
    return e;
  }

  function unitText(u) {
    var t = cache.get(u);
    if (t == null) {
      var parts = u.tagName === "TR" ? Array.prototype.map.call(u.cells, function (c) { return c.textContent; }) : [u.textContent];
      t = parts.map(norm).join("\u0001");
      cache.set(u, t);
    }
    return t;
  }

  function fmt(n) { return n.toLocaleString("ja-JP"); }

  function mount(box) {
    if (box.dataset.caMounted) return;
    var article = box.closest("article") || box.parentElement;
    if (!article) return;
    box.dataset.caMounted = "1";
    var mode = box.dataset.caUnits === "li" ? "li" : "tr";
    var unitName = mode === "li" ? "項目" : "行";
    if (box.dataset.caSynonyms) {
      try { addSynonyms(JSON.parse(box.dataset.caSynonyms)); } catch (e) { console.warn("claude-atlas: data-ca-synonyms を読めない", e); }
    }

    // 要点の囲みの前（ページの題の下）へ移す。狭い画面でも開いてすぐ見える位置にするため
    var abstract = article.querySelector(":scope > .admonition.abstract");
    if (abstract && abstract.compareDocumentPosition(box) & Node.DOCUMENT_POSITION_FOLLOWING) article.insertBefore(box, abstract);

    box.textContent = "";
    box.setAttribute("role", "search");
    var id = "ca-filter-" + Math.random().toString(36).slice(2, 8);
    var row = el("div", { class: "ca-filter__box" });
    var input = el("input", {
      class: "ca-filter__input", type: "search", id: id, autocomplete: "off", spellcheck: "false", enterkeyhint: "search",
      placeholder: box.dataset.caPlaceholder || "語で" + unitName + "を絞り込む",
      "aria-label": "語で" + (mode === "li" ? "項目" : "表の行") + "を絞り込む",
      "aria-describedby": id + "-status",
    });
    var clear = el("button", { class: "ca-filter__clear", type: "button", "aria-label": "絞り込みを消す", title: "絞り込みを消す" }, "×");
    clear.hidden = true;
    row.append(input, clear);
    var status = el("p", { class: "ca-filter__status", id: id + "-status", role: "status", "aria-live": "polite" });
    box.append(row, status);

    // 欄の後ろにある本文の要素（article の直下）。表は Material の JS が後から div で包むので、絞るたびに数え直す
    function blocks() {
      var out = [];
      var after = false;
      Array.prototype.forEach.call(article.children, function (b) {
        if (b === box) { after = true; return; }
        if (after && !b.matches(SKIP)) out.push(b);
      });
      return out;
    }

    // 絞り込む単位を持つ節（## の id。data-ca-sections に空白で区切って書く）。書かなければすべての節
    var sections = (box.dataset.caSections || "").split(/\s+/).filter(Boolean);
    function units(b, h2) {
      if (sections.length && !(h2 && sections.indexOf(h2.id) >= 0)) return [];
      if (mode === "li") return b.tagName === "UL" ? Array.prototype.slice.call(b.children).filter(function (x) { return x.tagName === "LI"; }) : [];
      return Array.prototype.slice.call(b.querySelectorAll("tbody tr"));
    }

    var total = 0;
    var h2now = null;
    blocks().forEach(function (b) {
      if (b.tagName === "H2") h2now = b;
      else total += units(b, h2now).length;
    });
    var hint = fmt(total) + " " + unitName + "。語を入れると、その語を含む" + unitName + "だけを残す（空白で区切ると、すべての語を含む" +
      unitName + "）。全角と半角・カタカナとひらがな・大文字と小文字の違いは問わない。";

    // 絞っている間は、欄の後ろの本文のうち ca-filter-keep の付いた要素だけを見せる（CSS。後から差し替わる図などの要素も
    // 印がないので隠れる）。残す表・箇条書きの中の当たらない行には ca-filter-off を付ける
    function reset() {
      Array.prototype.forEach.call(article.querySelectorAll(".ca-filter-off, .ca-filter-keep"), function (e) {
        e.classList.remove("ca-filter-off", "ca-filter-keep");
      });
      article.classList.remove("ca-filtering");
    }

    function apply() {
      var q = input.value;
      var ts = terms(q);
      clear.hidden = !q;
      writeQuery(q.trim());
      if (!ts.length) {
        reset();
        status.textContent = hint;
        return;
      }
      article.classList.add("ca-filtering");
      var shown = 0;
      var h2 = null;
      var h3 = null;
      var heads = [];
      blocks().forEach(function (b) {
        var tag = b.tagName;
        if (tag === "H2") { h2 = { el: b, on: false }; h3 = null; heads.push(h2); return; }
        if (tag === "H3" || tag === "H4") { h3 = { el: b, on: false }; heads.push(h3); return; }
        var us = units(b, h2 && h2.el);
        var any = false;
        us.forEach(function (u) {
          var on = test(unitText(u), ts);
          u.classList.toggle("ca-filter-off", !on);
          if (on) { any = true; shown++; }
        });
        b.classList.toggle("ca-filter-keep", any);
        if (any) {
          if (h2) h2.on = true;
          if (h3) h3.on = true;
        }
      });
      heads.forEach(function (h) { h.el.classList.toggle("ca-filter-keep", h.on); });

      // 件数の行に出す言い換え：元の語ごとに、言い換えの語をまとめる
      var used = [];
      words(q).forEach(function (t) {
        synonyms(t).forEach(function (s) {
          if (!s.to) return;
          var u = used.filter(function (x) { return x.from === s.from; })[0];
          if (!u) used.push(u = { from: s.from, to: [] });
          if (u.to.indexOf(s.to) < 0) u.to.push(s.to);
        });
      });
      var msg = shown ? fmt(shown) + " " + unitName + "が当たった（全 " + fmt(total) + " " + unitName + "）。"
        : "当たる" + unitName + "がない。語を短くするか、別の言い方で探す。";
      if (used.length) {
        msg += "言い換え：" + used.map(function (u) { return "「" + u.from + "」を「" + u.to.join("」・「") + "」"; }).join("、") +
          "に置き換えた形でも探した。";
      }
      status.textContent = msg;
    }

    var timer = 0;
    function schedule() {
      clearTimeout(timer);
      timer = setTimeout(apply, DELAY);
    }
    input.addEventListener("input", schedule);
    input.addEventListener("search", function () { clearTimeout(timer); apply(); }); // Enter と、欄の × で消したとき
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && input.value) {
        e.preventDefault();
        input.value = "";
        apply();
      }
    });
    clear.addEventListener("click", function () {
      input.value = "";
      apply();
      input.focus();
    });

    // Material が後から本文の要素を差し替える（表を div で包む・図を描く）ので、絞っている間は差し替えのたびに絞り直す
    if (window.MutationObserver) {
      new MutationObserver(function () {
        if (article.classList.contains("ca-filtering")) schedule();
      }).observe(article, { childList: true });
    }

    var api = {
      article: article,
      input: input,
      apply: apply,
      // 隠れた要素へ移るリンクを押したら、絞り込みを解く
      reveal: function (target) {
        if (!input.value || !target || !article.contains(target) || !article.classList.contains("ca-filtering")) return;
        if (target.closest(".ca-filter-off") || !target.getClientRects().length) {
          input.value = "";
          apply();
        }
      },
    };
    current = api;
    box.caFilter = api;

    var initial = new URLSearchParams(location.search).get(PARAM);
    if (initial) input.value = initial;
    apply();
  }

  function writeQuery(q) {
    try {
      var params = new URLSearchParams(location.search);
      if ((params.get(PARAM) || "") === q) return;
      if (q) params.set(PARAM, q);
      else params.delete(PARAM);
      var qs = params.toString();
      history.replaceState(history.state, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
    } catch (e) { /* 書き換えられなくても絞り込みは続ける */ }
  }

  // 同じページの見出しへのリンク（目次・本文）：行き先が隠れていれば、移る前に絞り込みを解く。Material の instant navigation は
  // ページを読み込んだときのアドレス（?filter= を含む）でリンクを絶対の URL に書き換えるので、押したときの絞り込みに合わせて
  // から移す（同じ pathname のリンクは読み込み直さず、そのアドレスへ移るだけなので、合わせないとアドレスと表示がずれる）
  document.addEventListener("click", function (e) {
    if (!current || !current.article.isConnected) return;
    var a = e.target instanceof Element ? e.target.closest("a[href]") : null;
    if (!a || !a.hash || a.origin !== location.origin || a.pathname !== location.pathname) return;
    var id = "";
    try { id = decodeURIComponent(a.hash.slice(1)); } catch (err) { return; }
    if (id) current.reveal(document.getElementById(id));
    if (a.search !== location.search) a.href = location.pathname + location.search + a.hash;
  }, true);

  function onDocument(doc) {
    var root = (doc && doc.body) || document.body;
    Array.prototype.forEach.call(root.querySelectorAll(".ca-filter"), mount);
  }

  if (window.document$) {
    window.document$.subscribe(onDocument);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { onDocument(document); });
  } else {
    onDocument(document);
  }
})();
