
from heapq import heappush, heappop

def boruvkas(n, edges):
    m = dict()
    p = list(range(n))
    mst = []
    def f(x):
        if p[x] != x: p[x] = f(p[x])
        return p[x]
    while len(mst) < n - 1:
        m.clear()
        for u, v, w in edges:
            ru, rv = map(f, (u, v))
            if ru != rv:
                if ru not in m or w < m[ru][2]: m[ru] = (u, v, w)
                if rv not in m or w < m[rv][2]: m[rv] = (u, v, w)
        for e in m.values():
            if f(e[0]) != f(e[1]):
                mst.append(e)
                p[f(e[0])] = f(e[1])
        if not m: break
    return mst

def prims(n, edges):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((w, u, v))
        g[v].append((w, v, u))
    start = 0
    for i in range(n):
        if g[i]:
            start = i
            break
    vis, h, r = {start}, list(g[start]), []
    while h and len(r) < n - 1:
        w, u, v = heappop(h)
        if v not in vis:
            vis.add(v)
            r.append((u, v, w))
            for edge in g[v]:
                if edge[2] not in vis:
                    heappush(h, edge)
    return r

def kruskals(n, edges):
    p = list(range(n))
    def f(x):
        if p[x] != x: p[x] = f(p[x])
        return p[x]
    r = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = f(u), f(v)
        if ru != rv:
            p[ru] = rv
            r.append((u, v, w))
            if len(r) == n - 1: break
    return r

def main():
    import time
    inp = ""
    with open("../test_data/graph_input.txt", encoding="utf-8") as f:
        inp = f.read()
    edges = [tuple(map(int, line.split(','))) for line in inp.strip().split('\n')]
    n = max(max(u, v) for u, v, _ in edges) + 1
    algorithms = (("Boruvka's", boruvkas), ("Prim's", prims), ("Kruskal's", kruskals))
    reference_weight = sum(w for *_, w in algorithms[0][1](n, edges))
    for name, alg in algorithms:
        start = time.perf_counter()
        result = alg(n, edges)
        elapsed = time.perf_counter() - start
        total_weight = sum(w for *_, w in result)
        status = "PASSED" if total_weight == reference_weight and len(result) == n - 1 else "FAILED"
        print(f"{name:12} {status:6} | Time: {elapsed*1000:7.3f}ms | Weight: {total_weight:6} | Edges: {len(result)}")

if __name__ == "__main__":
    main()