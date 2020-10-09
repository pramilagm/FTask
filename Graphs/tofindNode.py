class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacent = []

    def __repr__(self):
        return f'Node: {self.value}'


n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)
n4 = GraphNode(4)
n5 = GraphNode(5)

n1.adjacent.extend([n2, n3, n4])
n2.adjacent.extend([n1, n3, n4])
n3.adjacent.extend([n1, n2, n4])
n4.adjacent.extend([n1, n2, n3])


def findNode(node, target):
    toVisit = [node]
    seen = set([])
    print(seen)
    while toVisit:
        curr = toVisit.pop()
        print(curr)
        if curr == target:
            return True
        seen.add(curr)
        toVisit.extend(list(set(curr.adjacent) - seen))
    return False


print('Expected: True Got: ', findNode(n1, n4))
print('Expect: False Got:', findNode(n1, n5))
