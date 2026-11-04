#!/usr/bin/env python3
"""claude-atlas の PreToolUse の hook。止めるのは次の3つだけ（規則の表は .claude/README.md、決めた理由は
planning/design.md §10.5 と design-review.md の DR-08）。

  H1  AI の利用を断るサイトを開かない。WebFetch は permissions の deny が止め、この hook は理由と記録を受け持つ。
      Bash は、取得の道具（curl・wget など）の URL の引数のホストがそのドメインのときだけ、この hook が止める。
      ドメインの一覧は .claude/settings.json の deny の WebFetch(domain:…) から読む（一覧を二か所に持たない）
  H2  生成物を手で書き換えない。permissions の deny（Edit(…)）が止め、この hook は理由と記録を受け持つ。
      パスの一覧は .claude/settings.json の deny の Edit(/…) から読む。Bash はリダイレクト・tee・sed -i の書き先だけを見る
  H3  担当（サブエージェント。入力に agent_id がある呼び出し）の git と gh は読むだけ。制作の印 state/production が
      あるときだけ働き、メイン（agent_id がない呼び出し）は止めない

決まり（design §10.5）：
  - 止めるときは exit 0 と JSON（permissionDecision: deny と理由・代わり）を返す。止めないときは何も出さずに exit 0
  - 当てはめる範囲を狭くする：コマンドの文字列の部分一致では照らさず、字句に分けた後のコマンドの名前と引数で照らす
  - 止めた操作は、制作の印があるときだけ state/blocks.log に1行ずつ記録する（読者の環境には何も書かない）
  - 標準のライブラリだけで動く（Python 3.8 以上）。ネットワークを使わず、ファイルを壊さない
  - この hook の中の誤りは止めない側に倒す（H1・H2 は deny が強制するため）。ただし制作の印があり、担当の Bash の
    呼び出しで git か gh が出てくるときだけは、止める側に倒す（H3 はこの hook だけが強制するため）
  - state/hook-trace があるときは、呼ばれるたびに state/hook-trace.log に1行書く（ワークフローの担当でも hook が
    走り agent_id が付くかを確かめるため。既定では書かない）
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse

HOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HOOKS_DIR))   # <リポジトリ>/.claude/hooks/ の2つ上
SETTINGS = os.path.join(ROOT, ".claude", "settings.json")
STATE = os.path.join(ROOT, "state")
PRODUCTION_MARK = os.path.join(STATE, "production")
BLOCKS_LOG = os.path.join(STATE, "blocks.log")
TRACE_MARK = os.path.join(STATE, "hook-trace")
TRACE_LOG = os.path.join(STATE, "hook-trace.log")

MAX_DEPTH = 4          # $( )・bash -c・eval の入れ子をたどる深さ
SNIPPET = 160          # 理由と記録に入れるコマンドの長さ

# ---- 理由の文（事実の形で書く。research/28 #16） ----
SUFFIX = "この止め方が作業に合わないときは、別の手段で回り込まず、そのことを報告に書く（メインなら作者に相談する）。"
REASONS = {
    "H1": ("{target} は AI の利用を断っているサイトとして、このリポジトリでは開かない（.claude/README.md の H1）。"
           "curl などの別の道具や、写し（Internet Archive など）を通して読むことも同じ扱いになる。"
           "別の一次資料を探し、見つからなければそのことを報告に書く。"),
    "H2": ("{target} は道具が生成するファイルで、このリポジトリでは手で書き換えない（.claude/README.md の H2）。"
           "元のデータ（front matter・data/・snippets/ など）を直して gen_site.py で作り直す。"
           "担当は自分のページだけを書く gen_site.py --page <id> を使い、ほかの作り直しはメインに頼む（報告に書く）。"),
    "H3": ("このリポジトリの制作では、担当（サブエージェント）の git は読むだけ（status・diff・log・show など）で、"
           "gh も読むだけ（view・list など）。commit・push・巻き戻しはメインが行う（ほかの担当の変更を消さないため。"
           ".claude/README.md の H3）。止めたコマンド：{target}。変更は報告に書いて終える。"),
    "H3-error": ("フックの中の誤りで、担当の git・gh のコマンドが読むだけかを判定できなかったので止めた（制作の印があるときは"
                 "止める側に倒す。.claude/README.md の H3）。止めたコマンド：{target}。git・gh を使わずに進め、"
                 "要る操作は報告に書く。"),
}

# ---- シェルの字句（bash の近似） ----
CONTROL_OPS = ("&&", "||", ";;&", ";;", ";&", "|&", ";", "|", "&", "(", ")")
REDIR_OPS = ("&>>", "<<<", "<<-", "&>", ">>", ">|", ">&", "<<", "<>", "<&", ">", "<")
ALL_OPS = sorted(CONTROL_OPS + REDIR_OPS, key=len, reverse=True)
OP_CHARS = "&|;()<>"
WRITE_REDIRS = {">", ">>", ">|", "&>", "&>>", ">&"}
HEREDOC_RE = re.compile(r"<<(-?)[ \t]*(?:'([^'\n]*)'|\"([^\"\n]*)\"|\\?([^\s;&|<>()'\"]+))")

ASSIGN_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\[[^\]]*\])?\+?=")
RESERVED = {"!", "{", "}", "if", "then", "else", "elif", "fi", "do", "done", "while", "until", "case", "esac", "coproc"}
# 前に付けてほかのコマンドを動かすもの。値を取るオプション（次の語を飛ばす）を添える
WRAPPERS = {
    "sudo": {"-u", "-g", "-C", "-D", "-h", "-p", "-r", "-t", "-U", "-T", "--user", "--group"},
    "doas": {"-u", "-C"},
    "env": {"-u", "-C", "--unset", "--chdir"},
    "command": set(), "builtin": set(), "exec": {"-a"}, "nohup": set(), "setsid": set(),
    "nice": {"-n", "--adjustment"},
    "time": {"-f", "-o", "--format", "--output"},
    "timeout": {"-s", "-k", "--signal", "--kill-after"},
    "stdbuf": {"-i", "-o", "-e"},
    "ionice": {"-c", "-n", "-p", "-P", "-u", "--class", "--classdata"},
    "xargs": {"-a", "-d", "-E", "-I", "-L", "-n", "-P", "-s", "--arg-file", "--delimiter", "--max-args",
              "--max-procs", "--max-lines", "--max-chars"},
}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "mksh", "ash"}

# ---- H1：取得の道具 ----
FETCHERS = {"curl", "wget", "wget2", "http", "https", "httpie", "xh", "xhs", "curlie", "aria2c", "lynx", "w3m",
            "links", "elinks"}
URL_RE = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]*://[^\s'\"<>]+")
BARE_HOST_RE = re.compile(r"^(?:[A-Za-z0-9\-]+\.)+[A-Za-z]{2,}\.?(?::\d+)?(?:[/?#].*)?$")

# ---- H3：読むだけの git と gh ----
GIT_READ = {"status", "diff", "log", "show", "blame", "annotate", "ls-files", "ls-tree", "rev-parse", "rev-list",
            "grep", "cat-file", "shortlog", "describe", "merge-base", "show-ref", "for-each-ref", "name-rev", "cherry",
            "count-objects", "check-ignore", "check-attr", "whatchanged", "diff-tree", "diff-files", "diff-index",
            "range-diff", "var", "help", "version"}
GIT_OPTS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--super-prefix", "--config-env"}
GH_READ = {
    "pr": {"view", "list", "diff", "checks", "status"},
    "issue": {"view", "list", "status"},
    "repo": {"view", "list"},
    "run": {"view", "list", "watch"},
    "workflow": {"view", "list"},
    "release": {"view", "list"},
    "label": {"list"},
    "gist": {"view", "list"},
    "auth": {"status"},
    "search": None,    # None：下のすべてが読むだけ
    "status": None,
    "help": None,
    "version": None,
}
GH_OPTS_WITH_VALUE = {"-R", "--repo", "--hostname"}
GH_FIELD_OPTS = ("-f", "-F", "--field", "--raw-field", "--input")

SECRET_RES = (re.compile(r"sk-ant-[A-Za-z0-9_\-]+"),
              re.compile(r"(?i)(bearer\s+)\S+"),
              re.compile(r"(?i)((?:token|key|secret|password)=)\S+"))


class Cmd:
    """単純なコマンド1つ：語の並びと、リダイレクト（演算子・先）の並び。"""
    __slots__ = ("words", "redirects")

    def __init__(self, words: list[str], redirects: list[tuple[str, str]]):
        self.words = words
        self.redirects = redirects


def _find_close(src: str, i: int, open_ch: str = "(", close_ch: str = ")") -> int:
    """src[i] から、開きの括弧に対応する閉じの位置を返す（引用・エスケープ・ヒアドキュメントの本文を飛ばす。
    git commit -m "$(cat <<'EOF' … EOF)" の本文の ' や ( で閉じを見失わないため）。なければ len(src)。"""
    depth, n = 1, len(src)
    pending: list[tuple[str, bool]] = []
    while i < n:
        c = src[i]
        if c == "\\":
            i += 2
            continue
        if c == "\n" and pending:
            i = _skip_heredocs(src, i + 1, pending)
            pending = []
            continue
        if src.startswith("<<", i) and not src.startswith("<<<", i):
            m = HEREDOC_RE.match(src, i)
            if m:
                delim = next(g for g in m.groups()[1:] if g is not None)
                pending.append((delim, m.group(1) == "-"))
                i = m.end()
                continue
        if c == "'":
            j = src.find("'", i + 1)
            i = n if j < 0 else j + 1
            continue
        if c == '"':
            i += 1
            while i < n and src[i] != '"':
                i += 2 if src[i] == "\\" else 1
            i += 1
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return n


def _find_backtick(src: str, i: int) -> int:
    n = len(src)
    while i < n:
        if src[i] == "\\":
            i += 2
            continue
        if src[i] == "`":
            return i
        i += 1
    return n


def _skip_heredocs(src: str, i: int, pending: list[tuple[str, bool]]) -> int:
    """ヒアドキュメントの本文を飛ばし、次の行の始まりを返す（本文の中の > などを書き先と読まないため）。"""
    n = len(src)
    for delim, strip_tabs in pending:
        while i < n:
            j = src.find("\n", i)
            line = src[i:] if j < 0 else src[i:j]
            i = n if j < 0 else j + 1
            if (line.lstrip("\t") if strip_tabs else line) == delim:
                break
    return i


def parse_shell(src: str, depth: int = 0) -> list[Cmd]:
    """bash のコマンド列を単純なコマンドに分ける（近似）。引用・エスケープ・注釈・演算子・リダイレクト・
    ヒアドキュメントを扱い、$( )・` `・<( ) の中身も別のコマンドとして返す。変数の展開はしない。"""
    cmds: list[Cmd] = []
    words: list[str] = []
    redirs: list[tuple[str, str]] = []
    word = None
    pending_redir = None
    heredocs: list[tuple[str, bool]] = []
    i, n = 0, len(src)

    def sub(text: str) -> None:
        if depth < MAX_DEPTH:
            cmds.extend(parse_shell(text, depth + 1))

    def end_word() -> None:
        nonlocal word, pending_redir
        if word is None:
            return
        if pending_redir is not None:
            if pending_redir in ("<<", "<<-"):
                heredocs.append((word, pending_redir == "<<-"))
            else:
                redirs.append((pending_redir, word))
            pending_redir = None
        else:
            words.append(word)
        word = None

    def end_cmd() -> None:
        nonlocal words, redirs, pending_redir
        end_word()
        pending_redir = None
        if words or redirs:
            cmds.append(Cmd(words, redirs))
        words, redirs = [], []

    while i < n:
        c = src[i]
        if c == "\\":
            if i + 1 < n and src[i + 1] != "\n":
                word = (word or "") + src[i + 1]
            i += 2
            continue
        if c == "'":
            j = src.find("'", i + 1)
            j = n if j < 0 else j
            word = (word or "") + src[i + 1:j]
            i = j + 1
            continue
        if c == '"':
            i += 1
            buf = []
            while i < n and src[i] != '"':
                ch = src[i]
                if ch == "\\" and i + 1 < n and src[i + 1] in '"\\$`\n':
                    if src[i + 1] != "\n":
                        buf.append(src[i + 1])
                    i += 2
                    continue
                if src.startswith("$(", i) and not src.startswith("$((", i):
                    j = _find_close(src, i + 2)
                    sub(src[i + 2:j])
                    buf.append(src[i:j + 1])
                    i = j + 1
                    continue
                if ch == "`":
                    j = _find_backtick(src, i + 1)
                    sub(src[i + 1:j])
                    buf.append(src[i:j + 1])
                    i = j + 1
                    continue
                buf.append(ch)
                i += 1
            word = (word or "") + "".join(buf)
            i += 1
            continue
        if src.startswith("$((", i):                              # 算術の展開：中はコマンドでない
            j = _find_close(src, i + 2)
            word = (word or "") + src[i:j + 1]
            i = j + 1
            continue
        if src.startswith("$(", i):
            j = _find_close(src, i + 2)
            sub(src[i + 2:j])
            word = (word or "") + src[i:j + 1]
            i = j + 1
            continue
        if src.startswith("${", i):
            j = _find_close(src, i + 2, "{", "}")
            word = (word or "") + src[i:j + 1]
            i = j + 1
            continue
        if c == "`":
            j = _find_backtick(src, i + 1)
            sub(src[i + 1:j])
            word = (word or "") + src[i:j + 1]
            i = j + 1
            continue
        if c == "#" and word is None:
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == "\n":
            end_cmd()
            i += 1
            if heredocs:
                i = _skip_heredocs(src, i, heredocs)
                heredocs.clear()
            continue
        if c in " \t\r":
            end_word()
            i += 1
            continue
        if c in "<>" and src.startswith("(", i + 1):          # プロセス置換 <( ) と >( )
            j = _find_close(src, i + 2)
            sub(src[i + 2:j])
            word = (word or "") + src[i:j + 1]
            i = j + 1
            continue
        if c in OP_CHARS:
            op = next(o for o in ALL_OPS if src.startswith(o, i))
            if op in REDIR_OPS:
                if word is not None and word.isdigit():
                    word = None                                   # 2> の 2 はファイル記述子
                else:
                    end_word()
                pending_redir = op
            else:
                end_cmd()
            i += len(op)
            continue
        word = (word or "") + c
        i += 1
    end_cmd()
    return cmds


def _basename(word: str) -> str:
    name = re.split(r"[\\/]", word)[-1]
    return name[:-4] if name.lower().endswith(".exe") else name


def effective_argv(words: list[str]) -> list[str]:
    """変数の代入・予約語・前に付けるコマンド（sudo・env・timeout など）を飛ばし、[名前, 引数…] を返す。"""
    i, n = 0, len(words)
    while i < n:
        w = words[i]
        if ASSIGN_RE.match(w) or w in RESERVED:
            i += 1
            continue
        name = _basename(w)
        if name in WRAPPERS:
            takes = WRAPPERS[name]
            i += 1
            while i < n:
                a = words[i]
                if a == "--":
                    i += 1
                    break
                if a.startswith("-") and a != "-":
                    i += 2 if a in takes else 1
                    continue
                if name == "env" and ASSIGN_RE.match(a):
                    i += 1
                    continue
                break
            if name == "timeout" and i < n:
                i += 1                                            # 時間の引数
            continue
        return [name] + words[i + 1:]
    return []


def nested_script(argv: list[str]):
    """bash -c '…'・sh -c・eval の中身を返す（なければ None）。"""
    if not argv:
        return None
    if argv[0] == "eval":
        return " ".join(argv[1:])
    if argv[0] in SHELLS:
        k = 1
        while k < len(argv):
            a = argv[k]
            if a == "--":
                return None
            if a in ("-o", "+o", "-O", "+O"):
                k += 2
                continue
            if a.startswith("-") and not a.startswith("--") and "c" in a[1:]:
                return argv[k + 1] if k + 1 < len(argv) else None
            if not a.startswith(("-", "+")):
                return None                                       # スクリプトのファイル
            k += 1
    return None


def iter_commands(command: str):
    """コマンド列の単純なコマンドを順に (Cmd, argv) で返す。bash -c と eval の中身もたどる。"""
    stack = [(c, 0) for c in reversed(parse_shell(command))]
    while stack:
        cmd, depth = stack.pop()
        argv = effective_argv(cmd.words)
        yield cmd, argv
        if depth < MAX_DEPTH:
            script = nested_script(argv)
            if script:
                for sub in reversed(parse_shell(script)):
                    stack.append((sub, depth + 1))


# ---- 規則の材料（.claude/settings.json の deny から読む） ----
def load_deny(path: str = SETTINGS) -> list[str]:
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        deny = data.get("permissions", {}).get("deny", [])
    except (OSError, ValueError, AttributeError):
        return []
    return [d.strip() for d in deny if isinstance(d, str)] if isinstance(deny, list) else []


def noai_domains(deny: list[str]) -> list[str]:
    out: list[str] = []
    for rule in deny:
        m = re.match(r"^WebFetch\(domain:([^)]+)\)$", rule)
        if not m:
            continue
        d = m.group(1).strip().lower().rstrip(".")
        if d.startswith("*."):
            d = d[2:]
        if d and "*" not in d and d not in out:
            out.append(d)
    return out


def glob_to_regex(pattern: str):
    """gitignore の形のパターン（根からの相対。先頭の / は外したもの）を正規表現にする。"""
    out, i = [], 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out.append("(?:[^/]+/)*")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif pattern[i] == "*":
            out.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(pattern[i]))
            i += 1
    return re.compile("^" + "".join(out) + "$")


def generated_patterns(deny: list[str]) -> list[tuple[str, object]]:
    """deny の Edit(/…)（根からの相対のパス）を (元の文字列, 正規表現) で返す。// や ~/ の形は扱わない。"""
    out = []
    for rule in deny:
        m = re.match(r"^Edit\((/[^/][^)]*)\)$", rule)
        if m:
            out.append((m.group(1), glob_to_regex(m.group(1)[1:])))
    return out


def host_matches(host: str, domains: list[str]):
    h = (host or "").lower().rstrip(".")
    for d in domains:
        if h == d or h.endswith("." + d):
            return d
    return None


def fetch_hosts(argv: list[str]) -> list[str]:
    """取得の道具の引数から、URL のホストを返す（scheme のない atcoder.jp/… の形も見る）。"""
    hosts = []
    for a in argv[1:]:
        candidates = [m.group(0) for m in URL_RE.finditer(a)]
        if not candidates and not a.startswith("-") and BARE_HOST_RE.match(a):
            candidates = ["http://" + a]
        for url in candidates:
            try:
                host = urllib.parse.urlsplit(url).hostname
            except ValueError:
                host = None
            if host:
                hosts.append(host)
    return hosts


def relative_to_root(path: str, cwd: str):
    """path を根からの相対（/ 区切り）にする。根の外なら None。"""
    if not path:
        return None
    p = os.path.expanduser(path)
    if not os.path.isabs(p):
        p = os.path.join(cwd, p)
    try:
        rel = os.path.relpath(os.path.realpath(p), os.path.realpath(ROOT))
    except ValueError:                                            # Windows で別のドライブ
        return None
    rel = rel.replace(os.sep, "/")
    if rel in (".", "..") or rel.startswith("../"):
        return None
    return rel


def write_targets(cmd: Cmd, argv: list[str]) -> list[str]:
    """Claude Code が書き込みと見分けるシェルの形（リダイレクト・tee・sed -i）の書き先を返す。"""
    targets = []
    for op, target in cmd.redirects:
        if op not in WRITE_REDIRS:
            continue
        if op == ">&" and (target.isdigit() or target == "-"):
            continue                                              # 2>&1 などはファイルでない
        targets.append(target)
    if argv and argv[0] == "tee":
        targets += [a for a in argv[1:] if not a.startswith("-")]
    if argv and argv[0] == "sed":
        in_place = any(a == "--in-place" or a.startswith("--in-place=")
                       or (a.startswith("-") and not a.startswith("--") and "i" in a[1:]) for a in argv[1:])
        if in_place:
            targets += [a for a in argv[1:] if not a.startswith("-")]
    return targets


def git_is_read(argv: list[str]) -> bool:
    i = 1
    while i < len(argv):
        a = argv[i]
        if a in GIT_OPTS_WITH_VALUE:
            i += 2
            continue
        if a.startswith("-"):
            if a in ("--version", "--help", "-h"):
                return True
            i += 1
            continue
        if a not in GIT_READ:
            return False
        return not any(x == "--output" or x.startswith("--output=") for x in argv[i + 1:])
    return True                                                   # git だけ：使い方が出る


def gh_api_is_get(args: list[str]) -> bool:
    method, has_field, i = None, False, 0
    while i < len(args):
        a = args[i]
        if a in ("-X", "--method"):
            method = args[i + 1] if i + 1 < len(args) else ""
            i += 2
            continue
        if a.startswith("--method="):
            method = a.split("=", 1)[1]
        elif a.startswith("-X") and len(a) > 2:
            method = a[2:]
        elif a in GH_FIELD_OPTS or a.startswith(("--field=", "--raw-field=", "--input=")) or \
                (a.startswith(("-f", "-F")) and len(a) > 2):
            has_field = True
        i += 1
    if method is None:
        method = "POST" if has_field else "GET"
    return method.upper() == "GET"


def gh_is_read(argv: list[str]) -> bool:
    words, i = [], 1
    while i < len(argv) and len(words) < 2:
        a = argv[i]
        if a in GH_OPTS_WITH_VALUE:
            i += 2
            continue
        if a.startswith("-"):
            if not words and a in ("--version", "--help", "-h"):
                return True
            i += 1
            continue
        words.append(a)
        i += 1
    if not words:
        return True
    if words[0] == "api":
        k = argv.index("api")
        return gh_api_is_get(argv[k + 1:])
    if words[0] not in GH_READ:
        return False
    actions = GH_READ[words[0]]
    return actions is None or len(words) == 1 or words[1] in actions      # gh pr だけ：使い方が出る


# ---- 判定 ----
def production() -> bool:
    return os.path.exists(PRODUCTION_MARK)


def snippet(text: str) -> str:
    s = re.sub(r"[\t\r\n]+", " ", text or "").strip()
    for rx in SECRET_RES:
        s = rx.sub(lambda m: (m.group(1) if m.groups() else "") + "***", s)
    return s if len(s) <= SNIPPET else s[:SNIPPET - 1] + "…"


def evaluate(data: dict) -> list[tuple[str, str]]:
    """止める理由を (規則, 対象) の並びで返す。止めないなら空。"""
    tool = data.get("tool_name") or ""
    tin = data.get("tool_input")
    if not isinstance(tin, dict):
        return []
    deny = load_deny()
    found: list[tuple[str, str]] = []
    if tool == "WebFetch":
        url = tin.get("url") or ""
        try:
            host = urllib.parse.urlsplit(url).hostname or ""
        except ValueError:
            host = ""
        if host_matches(host, noai_domains(deny)):
            found.append(("H1", host))
    elif tool in ("Edit", "Write", "NotebookEdit"):
        path = tin.get("file_path") or tin.get("notebook_path") or ""
        rel = relative_to_root(path, data.get("cwd") or ROOT)
        if rel and any(rx.match(rel) for _, rx in generated_patterns(deny)):
            found.append(("H2", rel))
    elif tool == "Bash":
        command = tin.get("command") or ""
        if not isinstance(command, str) or not command.strip():
            return []
        domains = noai_domains(deny)
        patterns = generated_patterns(deny)
        h3 = bool(data.get("agent_id")) and production()
        cwd = data.get("cwd") or ROOT
        for cmd, argv in iter_commands(command):
            prog = argv[0] if argv else ""
            if prog in ("cd", "pushd") and len(argv) > 1 and argv[1] != "-":
                cwd = os.path.join(cwd, os.path.expanduser(argv[1]))
            elif prog == "cd" and len(argv) == 1:
                cwd = os.path.expanduser("~")
            if prog in FETCHERS and domains:
                for host in fetch_hosts(argv):
                    if host_matches(host, domains):
                        found.append(("H1", host.lower().rstrip(".")))
            if patterns:
                for target in write_targets(cmd, argv):
                    rel = relative_to_root(target, cwd)
                    if rel and any(rx.match(rel) for _, rx in patterns):
                        found.append(("H2", rel))
            if h3 and ((prog == "git" and not git_is_read(argv)) or (prog == "gh" and not gh_is_read(argv))):
                found.append(("H3", " ".join(argv)))
    return list(dict.fromkeys(found))                              # 重なりを外す（順は保つ）


def fail_safe(data: dict) -> list[tuple[str, str]]:
    """evaluate が誤りで終わったとき：制作の印があり、担当の Bash に git か gh が出てくるときだけ止める。"""
    try:
        tin = data.get("tool_input") or {}
        command = tin.get("command") if isinstance(tin, dict) else ""
        if (data.get("tool_name") == "Bash" and data.get("agent_id") and production() and isinstance(command, str)
                and re.search(r"(?<![\w.\-])(git|gh)(?![\w\-])", command)):
            return [("H3-error", command)]
    except Exception:  # noqa: BLE001
        pass
    return []


def actor(data: dict) -> str:
    agent_id = data.get("agent_id")
    if not agent_id:
        return "main"
    return "agent:%s:%s" % (data.get("agent_type") or "-", agent_id)


def append_line(path: str, fields: list[str]) -> None:
    """state/ があるときだけ1行を足す（state/ は作らない）。書けなくても止めない。"""
    try:
        if os.path.isdir(STATE):
            with open(path, "a", encoding="utf-8") as f:
                f.write("\t".join(re.sub(r"[\t\r\n]+", " ", x) for x in fields) + "\n")
    except OSError:
        pass


def reason_text(found: list[tuple[str, str]]) -> str:
    parts = []
    for rule, target in found:
        text = REASONS[rule].format(target=snippet(target))
        if text not in parts:
            parts.append(text)
    return "\n".join(parts + [SUFFIX])


def main() -> int:
    try:
        raw = sys.stdin.buffer.read().decode("utf-8", "replace")
        data = json.loads(raw) if raw.strip() else {}
    except (OSError, ValueError):
        return 0
    if not isinstance(data, dict):
        return 0
    try:
        found = evaluate(data)
    except Exception:  # noqa: BLE001  誤りは止めない側に倒す（担当の git・gh だけ止める側）
        found = fail_safe(data)
    stamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    if os.path.exists(TRACE_MARK):
        append_line(TRACE_LOG, [stamp, str(data.get("hook_event_name") or ""), str(data.get("tool_name") or ""),
                                str(data.get("agent_id") or "-"), str(data.get("agent_type") or "-"),
                                "deny" if found else "-"])
    if not found:
        return 0
    if production():
        for rule, target in found:
            append_line(BLOCKS_LOG, [stamp, rule, actor(data), str(data.get("tool_name") or ""), snippet(target)])
    out = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                  "permissionDecisionReason": reason_text(found)}}
    sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
