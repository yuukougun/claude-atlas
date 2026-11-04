/*
 * claude-atlas：期限切れの注意書き（planning/design.md §8.5・§9.2・§9.3、DR-11）
 *
 * 作る層（tools/gen_site.py）が、公開するページごとの期限の日（「ページの確認日＋ページの期限」と「各数値の確認日＋
 * 数値の期限」のうち早いもの）を数え、nav.yml の extra.ca.expires と assets/data/pages.json に書く。テンプレート
 * （overrides/main.html）は、ページの上部（.ca-page-head[data-ca-page]）の data-ca-expires に extra.ca.expires の値を
 * 出す（値のないページは空）。この JS は、期限の日とブラウザの今日（端末の日付）を比べるだけにする。
 * 期限の日が今日より前なら、隠してある注意書き（[data-ca-expiry]）に期限の日を入れて出す（期限の日の当日はまだ出さない。
 * tools/lib の Expiry.expired と同じ）。生成物は日によって変わらず、ビルドした日にも左右されない。
 *
 * - data-ca-expires がない（extra.ca.expires がない）ときだけ、pages.json の項目を id で引く。pages.json は、ページの上部の
 *   data-ca-pages-json（テンプレートが extra.ca.pages_json から書く）か、この JS の URL から決めた所（../data/pages.json）を、
 *   最初に要ったときに1回だけ読む（instant navigation でほかのページへ移っても読み直さない）。読めなければ注意書きは
 *   出さず、コンソールに書く
 * - pages.json の形：{"pages": [{"id": …, "expires": "YYYY-MM-DD" か null, …}]}。pages を id で引ける形
 *   （{"pages": {<id>: {…}}}）と、最上位がページの列の形も読む。期限の日のキーは expires
 * - JS が動かない環境では注意書きは出ない（design §8.5 で、比べるのはブラウザと決めた）
 * すべての JS と同じく、Material の document$ を購読して instant navigation のたびに見直す。
 */
(function () {
  "use strict";

  var SRC = document.currentScript ? document.currentScript.src : location.href;
  var DEFAULT_DATA = new URL("../data/pages.json", SRC).href;
  var DATE = /^\d{4}-\d{2}-\d{2}$/;
  var loading = Object.create(null); // URL → 読み込みの Promise

  function load(url) {
    if (!loading[url]) {
      loading[url] = fetch(url, { credentials: "same-origin" })
        .then(function (r) {
          if (!r.ok) throw new Error("pages.json を読めない（" + r.status + "）");
          return r.json();
        })
        .then(index)
        .catch(function (e) {
          delete loading[url]; // 次のページでもう一度試す
          throw e;
        });
    }
    return loading[url];
  }

  // pages.json → id から項目を引く Map
  function index(data) {
    var byId = new Map();
    var pages = data && !Array.isArray(data) && data.pages !== undefined ? data.pages : data;
    if (Array.isArray(pages)) {
      pages.forEach(function (p) { if (p && typeof p.id === "string") byId.set(p.id, p); });
    } else if (pages && typeof pages === "object") {
      Object.keys(pages).forEach(function (id) { if (pages[id] && typeof pages[id] === "object") byId.set(id, pages[id]); });
    }
    return byId;
  }

  function pad(n) { return (n < 10 ? "0" : "") + n; }

  // 端末の今日（ローカルの日付）を YYYY-MM-DD で
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
  }

  // 期限の日が今日より前か（どちらも YYYY-MM-DD。文字の大小が日付の前後と同じ）
  function isExpired(expires, now) {
    return typeof expires === "string" && DATE.test(expires) && DATE.test(now) && expires < now;
  }

  function show(box, expires) {
    var t = box.querySelector("[data-ca-expiry-date]");
    if (t) {
      t.textContent = expires;
      t.setAttribute("datetime", expires);
    }
    box.hidden = false;
  }

  function check(doc) {
    var root = (doc && doc.body) || document.body;
    var head = root.querySelector("[data-ca-page]");
    var box = head && head.querySelector("[data-ca-expiry]");
    if (!box) return Promise.resolve(null);
    box.hidden = true;
    var now = today();
    var direct = head.getAttribute("data-ca-expires");
    if (direct !== null) {
      if (isExpired(direct, now)) show(box, direct);
      return Promise.resolve(direct || null);
    }
    var id = head.getAttribute("data-ca-page");
    var rel = head.getAttribute("data-ca-pages-json");
    return load(rel ? new URL(rel, location.href).href : DEFAULT_DATA).then(function (byId) {
      var p = byId.get(id);
      var expires = p && typeof p.expires === "string" ? p.expires : null;
      if (box.isConnected && isExpired(expires, now)) show(box, expires);
      return expires;
    }).catch(function (e) {
      console.warn("claude-atlas: 期限切れの注意書きを確かめられなかった", e);
      return null;
    });
  }

  window.CAExpiry = { isExpired: isExpired, today: today, check: check };

  if (window.document$) {
    window.document$.subscribe(check);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { check(document); });
  } else {
    check(document);
  }
})();
