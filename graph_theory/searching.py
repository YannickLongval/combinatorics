# Searching algorithms

graph:dict[str, list[str]] = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}

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
def hasPath(graph:dict[str, list[str]], src:str, dst:str):
    if src == dst: return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst): return True

    return False #Only return false once all of the paths have been checked

BFSIter(graph, "A")