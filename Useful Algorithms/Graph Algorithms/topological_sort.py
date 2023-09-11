# MUSI BYC DAG
from collections import deque
G = [
    [1,2], #0
    [2,4], #1
    [], #2
    [], #3
    [3,6], #4
    [4], #5
    [], #6
]

def topological_sort(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    Q = deque()

    def DFSVisit(G, u): 
        nonlocal Q
        visited[u] = 1
        for v in G[u]:
            if not visited[v]: 
                DFSVisit(G, v)
        Q.appendleft(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    for item in Q: 
        print(item, " ",  end = "")



def main():
    topological_sort(G)

main()