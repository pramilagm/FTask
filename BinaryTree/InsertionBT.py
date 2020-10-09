class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insertBinaryTree(root, element):
    if root is None:
        root = Node(element)
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node.left is None:
            node.left = Node(element)
            break
        else:
            q.append(node.left)
        if node.right is None:
            node.right = Node(element)
            break
        else:
            q.append(node.right)


def inorder(temp):

    if (not temp):
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insertBinaryTree(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
