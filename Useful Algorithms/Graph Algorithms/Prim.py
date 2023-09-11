from queue import PriorityQueue
from math import inf
G = [
[(1,3), (2,7)],
[(0,3), (2,1), (5,2)],
[(0,7), (1,1), (3,4)],
[(2,4), (5,1), (4,5)],
[(3,5), (5,6)],
[(1,2), (3,1), (4,6), (6,3)],
[(5,3)]]

def prime(G, s):
    n = len(G)
    weight = [inf for _ in range(n)]
    visited = [0 for _ in range(n)]
    parent = [False for _ in range(n)]

    Q = PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        w, u = Q.get()
        if visited[u]: continue

        visited[u] = 1

        for v, w in G[u]:
            if not visited[v] and w < weight[v]:
                parent[v] = u
                weight[v] = w
                Q.put((w,v))

    return parent, weight

def get_MST(G, s):
    parents, weights = prime(G,s)
    A = []
    for i in range(len(parents)-1, -1, -1):
        A.append((i, parents[i], weights[i]))
    print(A)

print(get_MST(G,0))