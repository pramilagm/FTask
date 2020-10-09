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

# to find the middle element by One pass
    def findMiddleEle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
# to find the kth element by one pass

    def findKthEle(self, k):
        fast = self.head
        slow = self.head
        for i in range(1, k):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data


# recursive solution
llist = SinglyLL()
llist.head = Node(2)
llist.push(2)
llist.push(1)
llist.push(8)
llist.push(11)
llist.push(3)
llist.push(9)
llist.push(7)
# llist.printList()
# # print(llist.findElement(2))
# print(llist.findMiddleEle())
print(llist.findKthEle(6))
