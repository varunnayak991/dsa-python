# Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere

def printGraph(V: int, edges: list[list[int]]) -> list[list[int]]:
    # code here
    l = [[] for _ in range(V)]
    for i in range(len(edges)):

        l[edges[i][0]].append(edges[i][1])
        l[edges[i][1]].append(edges[i][0])

    for i in range(len(l)):
        l[i].sort()
    return l

print(printGraph(5, [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]))