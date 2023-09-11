from collections import deque

G = [
    [1,2], #0
    [0,4], #1
    [0,3,5], #2
    [2,4], #3
    [1,3,5], #4
    [2,4,6], #5
    [5,7], #6
    [6], #7
]

def BFS(G, s):
    n = len(G)
    distances = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
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
                parent[v] = u
                visited[v] = 1
                Q.append(v)


    print(distances)
    print(parent)
    print(visited)

def main():
    BFS(G, 0)

main()