class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print('Singly LL is empyty')
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def push(self, new_data):
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode

    def countElement(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(count)

# iterative solution to find max element
    def maxElement(self):
        max = self.head.data
        current = self.head
        while current.next is not None:
            current = current.next
            if current.data > max:
                max = current.data

        return max

    def getCountRecur(self, node):
        if node is None:
            return 0
        return 1 + self.getCountRecur(node.next)

    def findCount(self):
        return self.getCountRecur(self.head)

# recursive solution to find max element
    # def maxElemRecursive(self):
    def getMaxRecur(self, node):
        # base case
        if node.next is None:
            return node.data
        return max(node.next.data, self.getMaxRecur(node.next))

    def findMaxRecur(self):
        return self.getMaxRecur(self.head)
# to find first repeated elements

    def findRepeatedElements(self):
        current = self.head

        while current.next:
            if current.data == current.next.data:
                return current.data
            current = current.next
        return -1


llist = SinglyLL()
# llist.head = Node(3)
llist.push(12)
llist.push(8)
llist.push(18)
llist.push(4)
llist.push(4)
llist.push(13)
# llist.printList()
llist.countElement()
print(llist.maxElement())
print(llist.findCount())
print(llist.findMaxRecur())
print(llist.findRepeatedElements())
