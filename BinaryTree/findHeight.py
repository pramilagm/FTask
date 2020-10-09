class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# counting node in an iterative solution


def findHeightIter(root):
    if root is None:
        return 0
    queue = [root]
    height = 0
    while True:
        nodeCount = len(queue)
        if nodeCount == 0:
            return height
        height += 1
        while nodeCount > 0:
            node = queue.pop(0)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
            nodeCount -= 1
# find node recursively


def findHeightRec(root):
    if root is None:
        return 0
    return (1+max(findHeightRec(root.left), findHeightRec(root.right)))


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

#           2
#        7       5
#         6         9
#      1 11       4

print(findHeightIter(root))
print(findHeightRec(root))
