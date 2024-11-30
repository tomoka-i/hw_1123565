from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def buildTree(integers):
    if not integers or integers[0] == -1:
        return None

    iterVals = iter(integers)
    root = TreeNode(next(iterVals))
    queue = deque([root])

    while queue:
        node = queue.popleft()

        try:
            leftVal = next(iterVals)
            if leftVal != -1:
                node.left = TreeNode(leftVal)
                queue.append(node.left)

            rightVal = next(iterVals)
            if rightVal != -1:
                node.right = TreeNode(rightVal)
                queue.append(node.right)
        except StopIteration:
            break

    return root

def calculateDiameter(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)

        diameter = max(diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

    dfs(root)
    return diameter + 1

integers = list(map(int, input("Enter level-order traversal: ").strip().split()))

root = buildTree(integers)

print(calculateDiameter(root))
