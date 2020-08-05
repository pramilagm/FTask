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


llist = SinglyLL()
# llist.head = Node(3)
llist.push(5)
llist.push(8)
llist.push(8)
llist.push(7)
# llist.printList()
llist.countElement()
