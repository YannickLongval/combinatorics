# Basic Node class for Binary Tree
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.right = right
        self.left = left

# Iterative implementation of DFS for Binary Tree
def depthFirstValuesIter(root:Node) -> list[str]:
    if root is None: return []
    res:list[str] = []
    stack:list[Node] = [root]

    while len(stack) > 0:
        current = stack.pop()
        res.append(current.val)

        if current.right is not None: stack.append(current.right)
        if current.left is not None: stack.append(current.left)

    return res

# Recursive implementation of DFS for Binary Tree
def depthFirstValuesRec(root:Node) -> list[str]:
    if root is None: return []

    leftVal = depthFirstValuesRec(root.left)
    rightVal = depthFirstValuesRec(root.right)

    return [root.val] + leftVal + rightVal

# Iterative implementation of BFS for Binary Tree
# Doesn't make sense to have a recursive implementation
# Due to the nature of BFS
def breadthFirstValues(root:Node) -> list[str]:
    if root is None: return []
    res:list[str] = []
    queue:list[Node] = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        res.append(current.val)

        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)

    return res

# Iterative (BFS) implementation for searching a value in the Binary Tree
def treeIncludesIter(root:Node, target:str) -> bool:

    if root is None: return False

    queue:list[Node] = [root]

    while len(queue) > 0:
        current = queue.pop(0)

        if current.val == target: return True

        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)

    return False

# Recursive (DFS) implementation for searching a value in the Binary Tree
def treeIncludesRec(root:Node, target:str) -> bool:

    if root is None: return False
    if root.val == target: return True
    return treeIncludesRec(root.left, target) or treeIncludesRec(root.right, target)

root:Node = Node("a", Node("b", Node('d'), Node('e')), Node("c", right=Node("f")))

print(depthFirstValuesIter(root))
print(depthFirstValuesRec(root))
print(breadthFirstValues(root))
print(treeIncludesRec(root, 'g'))