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
    return False


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
print(findNode(root, 9))
