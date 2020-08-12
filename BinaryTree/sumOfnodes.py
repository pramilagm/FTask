class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# iterative solution using queue
def sumOfnodes(root):
    if root is None:
        return 0
    queue = [root]
    sum = 0
    while len(queue) > 0:
        node = queue.pop(0)
        sum += node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return sum
# recursive solution


def sumRecur(root):
    if root is None:
        return 0
    return (root.val + sumRecur(root.left) + sumRecur(root.right))


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
print(sumOfnodes(root))
print(sumRecur(root))
