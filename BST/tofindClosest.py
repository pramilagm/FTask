class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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

# recursive way


def tofindClosest(root, target):
    return findClosetHelper(root, target, root.val)


def findClosetHelper(root, target, closest):
    if root is None:
        return closest
    if abs(target - closest) > abs(target - root.val):
        closest = root.val
    if target < root.val:
        return findClosetHelper(root.left, target, closest)
    if target > root.val:
        return findClosetHelper(root.right, target, closest)

# Iterative way


def findClosestI(root, target):
    return findClosetIterative(root, target, root.val)


def findClosetIterative(root, target, closest):
    current = root
    while current is not None:
        if abs(target - closest) > abs(target - current.val):
            closest = current.val
        if target < current.val:
            target = current.left
        elif target > current.val:
            target = current.right
        else:
            break
    return closest


r = Node(50)
insertionBST(r, Node(30))
insertionBST(r, Node(20))
insertionBST(r, Node(40))
insertionBST(r, Node(70))
insertionBST(r, Node(60))
insertionBST(r, Node(80))
# print(tofindClosest(r, 65))
print(findClosestI(r, 82))
