#Otrzymujemy na wejściu pary ludzi, którzy sie znają. Pierwszego dnia osoba 0 przekazuje wiadomość wsyzstkim swoim znajomym. 
#Napisz algorytm który zwróci dzień w którym najwięcej osób dostało wiadomość oraz ilość tych osób.

E = [(22, 21), (21, 17), (20, 17), (16, 17), (16, 19), (16, 18), (16, 0), (0, 1), (1, 2), (2, 3),
     (3, 4), (4, 5), (5, 0), (5, 6), (6, 7), (7, 8), (8, 0), (7, 9), (9, 10), (10, 11), (10, 12),
     (12, 13), (12, 14), (14, 15), (16, 15), (0, 15)]

from collections import deque


def graph_transform(G): 
    n = len(G)
    v = 0

    for i in range(n): 
        start, end = G[i]
        v = max(v, start, end)

    G = [[] for _ in range(v+1)]

    for edge in E: 
        start, end = edge
        G[start].append(end)
        G[end].append(start)
        
    return G

def BFS(G, s):
    n = len(G)
    distances = [-1 for _ in range(n)]
    visited = [0 for _ in range(n)]

    Q = deque()

    distances[s] = 0
    visited[s] = 1
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                distances[v] = distances[u] + 1
                visited[v] = 1
                Q.append(v)

    count = [0 for _ in range(n)]

    for i in range(n): 
        count[distances[i]] += 1

    day = 0
    people = 0
    max = 0

    for i in range(n): 
        if count[i] > max: 
            max = count[i]
            people = count[i] 
            day = i

    print(day, people)


def main(): 
    G = graph_transform(E)
    BFS(G,0)
main()