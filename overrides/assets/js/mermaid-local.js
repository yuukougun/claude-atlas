/*
 * Mermaid の写しを、図を描くときに初めて読む（planning/design.md §8.5「外から読まない」）。
 *
 * Material for MkDocs 9.8.0 と Zensical 0.0.74 は、ページに Mermaid の図（pre.mermaid）があると、
 * window.mermaid がないときだけ unpkg.com から Mermaid を読み込み、initialize を1回呼んでから、
 * 図ごとに render を呼ぶ。ここで先に window.mermaid に小さな代わりを置いて、その2つを受ける。
 * 初めて render が呼ばれたときに、このサイトに置いた写し（assets/vendor/）を読み込み、
 * 受けておいた initialize の設定を当ててから描く。写しは読み込まれると window.mermaid を自分に
 * 置き換えるので、以後の図は本物が直接描く。
 *
 * - 図のないページでは写し（約 3.6MB）を読まない。instant navigation で移った先のページでも同じ
 * - このファイルは mkdocs.yml の extra_javascript で読む。テーマの bundle の後、DOMContentLoaded の前に動き
 *   （テーマは DOMContentLoaded の後に図を探す）、instant navigation では読み直されない
 * - 写しの場所は、このファイルの URL から決める（instant navigation で URL が変わっても同じ所を指す）
 * - テーマが initialize と render のほかを呼ぶようになったら、図は描かれないが、外のサイトからは読まない。
 *   テーマの版を上げるときは、描画の検査で図が描かれることを確かめる
 * - 版を上げるときは、下の VERSION と assets/vendor/ のディレクトリ名と SOURCES.txt を一緒に直す
 */
(function () {
  "use strict";

  if (typeof window.mermaid !== "undefined") return;

  var VERSION = "11.17.2";
  var self =
    document.currentScript ||
    document.querySelector('script[src*="assets/js/mermaid-local.js"]');
  if (!self) return;
  var src = new URL(
    "../vendor/mermaid-" + VERSION + "/mermaid.min.js",
    self.src
  ).href;

  var settings = null;
  var loading = null;
  var standIn;

  function load() {
    if (!loading) {
      loading = new Promise(function (resolve, reject) {
        var el = document.createElement("script");
        el.src = src;
        el.onload = function () {
          var real = window.mermaid;
          if (!real || real === standIn) {
            loading = null;
            reject(new Error("Mermaid の写しを読めなかった：" + src));
            return;
          }
          if (settings) real.initialize(settings);
          resolve(real);
        };
        el.onerror = function () {
          loading = null; // 次の図でもう一度試す
          reject(new Error("Mermaid の写しを読めなかった：" + src));
        };
        document.head.appendChild(el);
      });
    }
    return loading;
  }

  standIn = {
    initialize: function (options) {
      settings = options;
    },
    render: function (id, text) {
      return load().then(function (real) {
        return real.render(id, text);
      });
    }
  };

  window.mermaid = standIn;
})();
