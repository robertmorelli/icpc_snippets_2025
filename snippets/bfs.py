from collections import deque

def bfs(graph : dict, root : int, visited : set[int]):
    q = deque()
    q.append(root)
    visited.add(root)
    while q:
        v = q.popleft()
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                q.append(n)