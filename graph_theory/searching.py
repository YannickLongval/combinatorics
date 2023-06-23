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

grid = [
    ["L", "W", "L", "W", "L"],
    ["W", "L", "W", "L", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
    ["W", "L", "W", "L", "L"]
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

# print(undirectedPath(edges, "I", "O"))

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

# recursive helper function for connectedComponentCount() to recursively traverse component
def explore(graph:dict[str, list[str]], current:str, visited:set[str]):
    if current in visited: return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

# Algorithm to determine how many connected components are in the graph
def connectedComponentsCount(graph:dict[str, list[str]]) -> int:
    visited = set()
    count = 0

    for node in graph.keys():
        if explore(graph, node, visited):
            count += 1

    return count

# helper function for largestComponent to recursively count number of nodes in component
def exploreSize(graph:dict[str, list[str]], node:str, visited:set[str]) -> int:
    if node in visited: return 0

    visited.add(node)

    size = 1

    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    return size

# Algorithm to count how many nodes are in the largest component
def largestComponent(graph:dict[str, list[str]]) -> int:
    visited = set()

    longest = 0

    for node in graph.keys():
        size = exploreSize(graph, node, visited)
        if size > longest: longest = size

    return longest

# Algorithm to find the shortest path between two nodes in a graph
def shortestPath(edges:list[tuple[str,str]], nodeA:str, nodeB:str) -> int:
    graph = edgeToAdjacency(edges)

    visited = {nodeA}

    # queue contains pair of str and int, which are the node and the distance from the starting point
    queue:list[tuple[str, int]] = [(nodeA, 0)]

    while len(queue) > 0:
        node, distance = queue.pop(0)

        if node == nodeB: return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)
    return -1

# helper function for islandCount() to recursively traverse island
def exploreIsland(grid:list[list[str]], r:int, c:int, visited:set[str]) -> bool:
    rowInBounds = 0 <= r < len(grid)
    colInBounds = 0 <= c < len(grid[0])
    if not rowInBounds or not colInBounds: return False

    if grid[r][c] == "W": return False
    
    pos = str(r) + ',' + str(c)

    if pos in visited: return False
    visited.add(pos)

    exploreIsland(grid, r - 1, c, visited)
    exploreIsland(grid, r + 1, c, visited)
    exploreIsland(grid, r, c - 1, visited)
    exploreIsland(grid, r, c + 1, visited)

    return True

# using graph theory to count spaces in a grid
def islandCount(grid:list[list[str]]) -> int:
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if exploreIsland(grid, r, c, visited): count += 1
    return count

# helper function for minimumIsland() to recursively count size of island
def exploreSize(grid:list[list[str]], r:int, c:int, visited:set[str]) -> int:
    rowInBounds = 0 <= r < len(grid)
    colInBounds = 0 <= c < len(grid[0])
    if not rowInBounds or not colInBounds: return 0

    if grid[r][c] == "W": return 0
    
    pos = str(r) + ',' + str(c)

    if pos in visited: return 0
    visited.add(pos)

    size = 1
    size += exploreIsland(grid, r - 1, c, visited)
    size += exploreIsland(grid, r + 1, c, visited)
    size += exploreIsland(grid, r, c - 1, visited)
    size += exploreIsland(grid, r, c + 1, visited)

    return size 

# using graph theory to find the smallest group in a grid
def minimumIsland(grid:list[list[str]]) -> int:
    visited = set()
    minIsland = len(grid) * len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            size = exploreSize(grid, r, c, visited)
            if size > 0 and size < minIsland: minIsland = size
    return minIsland

            
print(islandCount(grid))
# print(shortestPath(edges, "I", "I"))
# print(shortestPath(edges, "I", "J"))
# print(shortestPath(edges, "I", "M"))
# print(largestComponent(edgeToAdjacency(edges)))
# print(connectedComponentsCount(edgeToAdjacency(edges)))
# print(hasPathBFS(graph, "A", "F"))