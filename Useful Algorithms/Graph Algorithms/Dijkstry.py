from queue import PriorityQueue
from math import inf

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


def dijkstry(G, s):
    n = len(G)
    parents = [None] * n
    distances = [inf] * n
    pq = PriorityQueue()
    distances[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parents[v] = u
                pq.put((distances[v], v))
                
    return parents, distances

print(dijkstry(G, 0))