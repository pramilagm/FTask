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

    def pushRec(self, new_data):
        if self.next is None:
            self.next = Node(new_data)
        self.next.pushRec(new_data)

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

    def removeKthElement(self, n):
        slow = self.head
        fast = self.head
        for i in range(1, n+1):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

    def utilSumRec(self, head):
        if head is None:
            return 0
        return head.data + self.utilSumRec(head.next)

    def sumRec(self):
        return self.utilSumRec(self.head)


llist = SinglyLL()
llist.head = Node(3)
llist.push(12)
llist.push(8)
llist.push(18)
llist.push(4)
llist.push(4)
llist.push(13)
llist.printList()
# llist.countElement()
# print(llist.maxElement())
# print(llist.findCount())
# print(llist.findMaxRecur())
# print(llist.findRepeatedElements())
# llist.removeKthElement(3)
# llist.pushRec(12)
# llist.pushRec(14)
# llist.printList()
print(llist.sumRec())
