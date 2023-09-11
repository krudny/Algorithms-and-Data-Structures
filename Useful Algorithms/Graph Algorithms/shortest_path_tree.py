from queue import PriorityQueue
from math import inf

#shortest paths tree

G = [
[(1, 3), (6, 2)],
[(0, 3), (2, 2), (8, 1)],
[(1, 2), (3, 5)],
[(4, 20), (2, 5), (8, 1)],
[(5, 8), (3, 20), (7, 2)],
[(6, 3), (7, 1), (4, 8)],
[(0, 2), (7, 1), (5, 3)],
[(6, 1), (5, 1), (8, 7), (4, 2)],
[(7, 7), (1, 1), (3, 1)]]

def dijkstra(G, s):
    n = len(G)
    weights = [inf] * n
    parents = [[] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = [parent]
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))
        elif min_w == weights[u]:
            parents[u].append(parent)

    parents[s] = []

    return parents

print(dijkstra(G, 0))