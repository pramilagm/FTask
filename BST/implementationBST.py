class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insertionBST(root, node):
    if root is None:
        root = node
        return root
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertionBST(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertionBST(root.left, node)


def findMinNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteBST(root, key):

    if root is None:
        return root
    if root.val > key:
        root.left = deleteBST(root.left, key)
    elif root.val < key:
        root.right = deleteBST(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = findMinNode(root.right)
        root.val = temp.val
        # Delete the inorder successor
        root.right = deleteBST(root.right, temp.val)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insertionBST(r, Node(30))
insertionBST(r, Node(20))
insertionBST(r, Node(40))
insertionBST(r, Node(70))
insertionBST(r, Node(60))
insertionBST(r, Node(80))
inorder(r)
print('----------------------After deletion')
deleteBST(r, 20)

# Print inoder traversal of the BST
inorder(r)
