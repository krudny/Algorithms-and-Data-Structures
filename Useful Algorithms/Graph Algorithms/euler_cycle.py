from collections import deque
G = [[1,3],[0,2,4,5],[1,3],[0,2,4,6],[1,3,5,6],[1,4,7,6],[3,5,4,7],[5,6]]

def euler(G):
    Q = deque()
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]

    def is_possible(G):
        for i in range(n):
            if len(G[i]) % 2 == 1: return False
        return True

    if not is_possible(G): return False
    
    def DFSVisit(G, u):
        visited[u] = 1
        for v in G[u]:
            parent[v] = u
            G[u].remove(v)
            G[v].remove(u)
            DFSVisit(G, v)
        Q.appendleft(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    
    for i in range(n):
        if not visited[i]: return False
        
    print(Q)
    return True

print(euler(G))