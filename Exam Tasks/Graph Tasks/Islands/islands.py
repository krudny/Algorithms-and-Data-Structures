G = [
    [0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,0,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0]
]

a = 5
b = 2

from math import inf
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    distances = [inf] * n
    pq = PriorityQueue()
    distances[s] = 0
    pq.put((0, s))
    
    while not pq.empty():
        _, u = pq.get()
        for v, weight in G[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                pq.put((distances[v], v))
                
    return distances


def create_graph(G): 
    n = len(G)
    M = [[0 for _ in range(3*n)] for _ in range(3*n)]

    for i in range(n): 
        s1, s2, s3 = 3*i, 3*i+1, 3*i+2 # s1 = bridge 1B, s2 = ferry 5B, s3 = plane 8B

        for j in range(n): 
            e1, e2, e3 = 3*j, 3*j+1, 3*j+2

            if G[i][j] == 1: 
                M[s2][e1] = 1
                M[s3][e1] = 1
            elif G[i][j] == 5: 
                M[s1][e2] = 5
                M[s3][e2] = 5
            elif G[i][j] == 8: 
                M[s1][e3] = 8
                M[s2][e3] = 8
    return M

def convert_to_list(graph):
    n = len(graph)
    list_graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                list_graph[i].append((j, graph[i][j]))
    return list_graph


def islands(G, a, b): 
    M = create_graph(G)
    J = convert_to_list(M)

    s1, s2, s3 = 3*a, 3*a + 1, 3*a + 2
    e1, e2, e3 = 3*b, 3*b + 1, 3*b + 2

    dis1 = dijkstra(J, s1)
    dis2 = dijkstra(J, s2)
    dis3 = dijkstra(J, s3)

    min1, min2, min3 = inf, inf, inf

    min1 = min(dis1[e1], dis1[e2], dis1[e3])
    min2 = min(dis2[e1], dis2[e2], dis2[e3])
    min3 = min(dis3[e1], dis3[e2], dis3[e3])

    return min(min1, min2, min3)

def main(): 
    print(islands(G, a, b))

main()