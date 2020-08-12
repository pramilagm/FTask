class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def tofindMax(root):
    if root is None:
        return float('-inf')
    res = root.data

    lchild = tofindMax(root.left)
    rchild = tofindMax(root.right)
    if lchild > res:
        res = lchild
    if rchild > res:
        res = rchild
    return res


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
print(tofindMax(root))
