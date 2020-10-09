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

    def sumUtil(self, head):
        if head is None:
            return 0
        return head.data + self.sumUtil(head.next)

    def sum(self):
        return self.sumUtil(self.head)


def sumTwoLL(head1, head2):
    carry = 0
    result = n = Node(0)
    while head1 or head2 or carry:
        if head1:
            carry += head1.data
            head1 = head1.next
        if head2:
            carry += head2.data
            head2 = head2.next
        carry, val = divmod(carry, 10)
        n.next = n = Node(val)
    return result.next


llist = SinglyLL()
llist.head = Node(3)
llist.push(8)
llist.push(4)
llist.push(4)


list1 = SinglyLL()
list1.head = Node(3)
list1.push(12)
list1.push(8)
list1.push(4)
list1.push(4)
print(sumTwoLL(llist.head, list1.head))
# print(llist.sum())
