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

def DFS(G):
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [0 for _ in range(n)]
    time = 0

    def DFSVisit(G, u): 
        nonlocal time
        time += 1           #czas odwiedzenia
        visited[u] = 1

        for v in G[u]:
            if not visited[v]: 
                parent[v] = u
                DFSVisit(G, v)
        time += 1           #czas przetworzenia

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    print(visited)
    print(parent)


def main():
    DFS(G)

main()