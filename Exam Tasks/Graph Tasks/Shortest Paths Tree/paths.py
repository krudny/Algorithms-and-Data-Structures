G = [
[(1,2), (2,4)],
[(0,2), (3,11), (4, 3)],
[(0,4), (3,13)],
[(1,11), (2,13), (5, 17), (6, 1)],
[(1,3), (5,5)], 
[(3,17), (4,5), (7,7)],
[(3,1), (7,3)], 
[(5,7), (6,3)]
]

s = 0
t = 7

from queue import PriorityQueue
from math import inf


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

def count_edges(G, t):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        count = 0
        for v in G[u]:
            if not visited[v]:
                count += dfs(v)
            count += 1
        return count

    return dfs(t)


def main(): 
    P = dijkstra(G, s)

    print(count_edges(P, t))

main()