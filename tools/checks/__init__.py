"""検査の層（設計書 §8.3）：検査1つを関数1つにして登録する。読むのは読む層（tools/lib/）だけを通す。

部品:
  core.py         登録の仕組み（@check・Finding・Issue・run_checks）と出力の形
  context.py      検査に渡すもの（Context）：ページのモデル（front matter か目次）・data・nav.yml・settings.json・今日
  rules.py        規則が名指しする語彙と数、site.yml の語彙の読み方
  config.py       nav.yml（nav と exclude_docs）と .claude/settings.json（deny）の読み方
  relations.py    前提と関連の規則（front matter と目次の両方。tools/check_catalog.py と同じ中身）
  frontmatter.py  front matter の形（schema）・ファイルの名前と置き場所・stage・章・設定
  body.py         本文：目印・sections と見出し・要点・別名の行・手書きのリンク・link の目印・ナビゲーション
  data_checks.py  数値と出典：data の形と参照・id・出典の URL・AI の利用の指定・断るドメインと deny
  freshness.py    確認日の期限・目印の外の数値
  templates.py    雛形の静的な検査（tools/check_templates.py が使う）

入口は tools/check_pages.py（FRONT_MATTER と CATALOG）と tools/check_templates.py（TEMPLATES）。
"""
from .context import Context, load_context
from .core import (CATALOG, CHECKS, ERROR, FRONT_MATTER, TEMPLATES, WARNING, Check, Finding, Issue, check, checks_epilog,
                   checks_for, format_issue, run_checks, summary_line)
from . import relations, frontmatter, body, data_checks, freshness, templates  # noqa: F401,E402  （検査を登録する）

__all__ = ["CATALOG", "CHECKS", "Check", "Context", "ERROR", "FRONT_MATTER", "Finding", "Issue", "TEMPLATES", "WARNING",
           "check", "checks_epilog", "checks_for", "format_issue", "load_context", "run_checks", "summary_line"]
