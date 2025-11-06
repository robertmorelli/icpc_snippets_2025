def alg(n, edges):
    m = dict()
    p = list(range(n))
    mst = []
    def f(x):
        if p[x] != x: p[x] = f(p[x])  # path compression
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
    return mst

def main():
    inp = ""
    with open("../test_data/graph_input.txt", encoding="utf-8") as f:
        inp = f.read()
    outp = ""
    with open("../test_data/mst_output.txt", encoding="utf-8") as f:
        outp = f.read()
    edges = [tuple(map(int, line.split(','))) for line in inp.strip().split('\n')]
    expected = [tuple(map(int, line.split(','))) for line in outp.strip().split('\n')]
    n = max(max(u, v) for u, v, w in edges) + 1
    result = alg(n, edges)
    result_pairs = [(u, v) for u, v, w in result]
    result_set = set((min(u,v), max(u,v)) for u, v in result_pairs)
    expected_set = set((min(u,v), max(u,v)) for u, v in expected)
    print("PASSED" if result_set == expected_set else "FAILED")

if __name__ == "__main__":
    main()