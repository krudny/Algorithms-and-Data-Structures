from math import inf
G = [(0,1,2), (0,2,3), (1,2,3), (1,5,1), (2,4,5), (4,3, 1), (3,2,6), (4,5,6)]

def Bellman_Ford(G, s):
    n = len(G)
    distances = [inf for _ in range(6)]

    distances[s] = 0


    for i in range(n-1):
        for u, v, w in G:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w


    for u, v, w in G:
        if distances[u] != inf and distances[u] + w < distances[v]:
            return None

    
    return distances

print(Bellman_Ford(G,0))