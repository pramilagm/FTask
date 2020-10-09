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

    def removeNodesValue(self, key):
        current = self.head
        prev = None
        while current is not None and current.data == key:
            self.head = current.next
            current = self.head
        while current:
            while current is not None and current.data != key:
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = prev.next
# find an element
# Iterative solution

    def findElement(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def findElementRec(self, key):
        if self.head is None:
            return False
        if self.head.data == key:
            return True
        return self.findElement(self.head.next, key)


# recursive solution
llist = SinglyLL()
llist.head = Node(2)
llist.push(2)
llist.push(1)
llist.push(8)
llist.push(2)
llist.push(3)
llist.push(2)
llist.push(7)
llist.removeNodesValue(2)
llist.printList()
print(llist.findElement(2))
