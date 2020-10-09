class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# counting node in an iterative solution


def findNode(root, target):
    if root is None:
        return False
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if node.data == target:
            return True
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)
    return Falsere


def findNodeDFS(root, target):
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal
        # is smaller than the previous one
        # that's not BST.
        if root.data == target:
            return True
        root = root.right
    return False
# find node recursively


def findNodeValRec(root, target):
    if root is not None:
        if root.data == target:
            return True
        return findNodeValRec(root.left, target) or findNodeValRec(root.right, target)
    return False


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
# print(findNode(root, 9))
print(findNodeValRec(root, 3))
print(findNodeDFS(root, 12))
