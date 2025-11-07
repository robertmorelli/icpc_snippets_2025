def dfs_recursive(graph : dict, root : int, visited : set[int]):
    visited.add(root)
    for n in graph[root]:
        if n not in visited:
            dfs_recursive(graph, n, visited)
            
def dfs_iterative(graph : dict, root: int, visited : set[int]):
    s = [root]
    while s:
        v = s.pop()
        if v not in visited:
            visited.add(v)
            for n in graph[v]:
                s.append(n)