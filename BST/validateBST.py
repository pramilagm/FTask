class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree(root):
    return isBinaryUtl(root, None, None)


def isBinaryUtl(root, left, right):
    if root is None:
        return True
    if left != None and root.data <= left.data:
        return False
    if right != None and root.data >= right.data:
        return False
    return isBinaryUtl(root.left, left, root) and isBinaryUtl(root.right, root, right)


def isBinaryIter(root):
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.data)
        # If next element in inorder traversal
        # is smaller than the previous one
        # that's not BST.
        if root.data <= inorder:
            return False
        inorder = root.data
        root = root.right
    return True


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

#      4
#     2   6
#   1   3 5  7
print(check_binary_search_tree(root))
print(isBinaryIter(root))
