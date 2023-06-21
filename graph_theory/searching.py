# Searching algorithms

# One representation of a graph: adjacency list
# Keys are the nodes, values are the edges
graph:dict[str, list[str]] = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}

# Another respresentation of a graph: edge list
# Each tuple is an edge between two nodes
edges:list[tuple[str,str]] = [
    ("I", "J"),
    ("K", "I"),
    ("M", "K"),
    ("K", "L"),
    ("O", "N"),
]

# Convert an edge list to an adjacency list
def edgeToAdjacency(edges:list[tuple[str,str]])->dict[str, list[str]]:
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph

def hasPathUndirected(graph:dict[str, list[str]], src:str, dst:str, visited:set[str])->bool:
    if src == dst: return True
    if src in visited: return False

    visited.add(src)

    for neighbor in graph[src]:
        if hasPathUndirected(graph, neighbor, dst, visited):
            return True
        
    return False

def undirectedPath(edges:list[tuple[str,str]], nodeA:str, nodeB:str)->bool:
    graph = edgeToAdjacency(edges)
    return hasPathUndirected(graph, nodeA, nodeB, set())

print(undirectedPath(edges, "I", "O"))

# An iterative implementation of Depth First Search
def DFSIter(graph:dict[str, list[str]], start:str):
    # Array implementation of a stack (top of stack is at end of array)
    stack:list[str] = [start]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)

# A recursive implementation of Depth First Search
def DFSRec(graph:dict[str, list[str]], start:str):
    print(start)
    for neighbor in graph[start]:
        DFSRec(graph, neighbor)

# An iterative implementation of Breadth First Search
# Note there is no recursive implementation since recursion
# inherently follows the stucture of a stack, as opposed to 
# a queue which is used for BFS.
def BFSIter(graph:dict[str, list[str]], start:str):
    # Array implementation of a Queue (beginning of queue is at start of array)
    queue:list[str] = [start]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)

# Algorithm to determine whether or not a path can be found between 2 points 
# Using a DFS
def hasPathDFS(graph:dict[str, list[str]], src:str, dst:str)->bool:
    if src == dst: return True

    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dst): return True

    return False #Only return false once all of the paths have been checked

# Algorithm to determine whether or not a path can be found between 2 points 
# Using a BFS
def hasPathBFS(graph:dict[str, list[str]], src:str, dst:str)->bool:
    # Array implementation of a Queue (beginning of queue is at start of array)
    queue:list[str] = [src]

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == dst: return True
        for neighbor in graph[curr]:
            queue.append(neighbor)

    return False #Only return false once all of the paths have been checked

print(hasPathBFS(graph, "A", "F"))