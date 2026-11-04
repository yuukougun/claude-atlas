"""前提のグラフの部品（作る層の知識マップ・ロードマップと、検査の層の循環・推移的な前提が使う）。

グラフは「ページの id → そのページの前提のページの id のリスト」（辺は前提へ向く）。strongly_connected は
tools/check_catalog.py から写した（再帰しない Tarjan）。
"""
from __future__ import annotations

import collections
import heapq
from typing import Iterable


def strongly_connected(graph: dict[str, list[str]]) -> list[list[str]]:
    """強連結成分（Tarjan。再帰しない）。graph にない頂点への辺は、その頂点も成分として返す。"""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    result: list[list[str]] = []
    counter = 0
    for root in graph:
        if root in index:
            continue
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(graph.get(root, ())))]
        while work:
            node, it = work[-1]
            pushed = False
            for nxt in it:
                if nxt not in index:
                    index[nxt] = low[nxt] = counter
                    counter += 1
                    stack.append(nxt)
                    on_stack.add(nxt)
                    work.append((nxt, iter(graph.get(nxt, ()))))
                    pushed = True
                    break
                if nxt in on_stack:
                    low[node] = min(low[node], index[nxt])
            if pushed:
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    comp.append(w)
                    if w == node:
                        break
                result.append(comp)
    return result


def cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    """循環している成分（2頂点以上の強連結成分と、自分自身への辺のある頂点）。"""
    return [c for c in strongly_connected(graph) if len(c) > 1 or c[0] in graph.get(c[0], ())]


def reachable(graph: dict[str, list[str]], starts: Iterable[str]) -> set[str]:
    """starts から辺を1本以上たどって届く頂点（starts 自身は、循環で戻るときだけ入る）。"""
    seen: set[str] = set()
    queue = collections.deque(n for s in starts for n in graph.get(s, ()))
    while queue:
        u = queue.popleft()
        if u in seen:
            continue
        seen.add(u)
        queue.extend(graph.get(u, ()))
    return seen


def reverse(graph: dict[str, list[str]]) -> dict[str, list[str]]:
    """辺の向きを逆にしたグラフ（前提 → それを前提にするページ）。頂点は graph と同じ順。"""
    out: dict[str, list[str]] = {u: [] for u in graph}
    for u, vs in graph.items():
        for v in vs:
            out.setdefault(v, [])
            if u not in out[v]:
                out[v].append(u)
    return out


def topological_order(graph: dict[str, list[str]], order: Iterable[str] | None = None) -> list[str]:
    """前提が先に来る並び（Kahn）。同じ段では order の順（省くと graph の順）。循環に入る頂点は最後に order の順で
    足す（循環の検査は cycles）。graph にない前提の id は数えない。"""
    nodes = list(dict.fromkeys(order)) if order is not None else list(graph)
    listed = set(nodes)
    nodes += [u for u in graph if u not in listed]
    rank = {u: i for i, u in enumerate(nodes)}
    pending = {u: len({v for v in graph.get(u, ()) if v in rank and v != u}) for u in nodes}
    dependents = reverse({u: [v for v in graph.get(u, ()) if v in rank] for u in nodes})
    out: list[str] = []
    heap = [(rank[u], u) for u in nodes if pending[u] == 0]
    heapq.heapify(heap)
    done: set[str] = set()
    while heap:
        _, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        out.append(u)
        for w in dependents.get(u, ()):
            if w == u or w in done:
                continue
            pending[w] -= 1
            if pending[w] == 0:
                heapq.heappush(heap, (rank[w], w))
    out += [u for u in nodes if u not in done]
    return out
