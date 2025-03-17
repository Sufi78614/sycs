from collections import defaultdict
graph=defaultdict(list)
def addEdges(graph,u,v):
    graph[u].append(v)
def generate_edges(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges
addEdges(graph,'a','c')
addEdges(graph,'b','c')
addEdges(graph,'b','e')
addEdges(graph,'c','d')
addEdges(graph,'c','e')
addEdges(graph,'c','a')
addEdges(graph,'c','b')
addEdges(graph,'e','b')
addEdges(graph,'d','c')
addEdges(graph,'e','c')
print(generate_edges(graph))
