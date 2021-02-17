class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def insertNode(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def find(self, val):
        current = self.head
        while current and current.val != val:
            current = current.next
        return current != None

    def deleteNode(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current:
            current.next = current.next.next

    def reverseList(self):
        prev = None
        next = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
def intersect(l1, l2):
    p1 = l1.head
    p2 = l2.head
    while p1 != p2:
        if not p1.next:
            p1 = l2.head
        else:
            p1 = p1.next
        if not p2.next:
            p2 = l1.head
        else:
            p2 = p2.next
    return p1 != None

sll1 = SinglyLinkedList()
sll1.insertNode(6)
sll1.insertNode(5)
sll1.insertNode(4)
sll1.insertNode(3)
sll1.insertNode(2)
sll1.insertNode(1)
sll2 = SinglyLinkedList()
sll2.insertNode(7)
sll2.head.next = sll1.head.next.next.next
sll1.printList()
print()
sll2.printList()
print(intersect(sll1, sll2))
print()
sll3 = SinglyLinkedList()
sll3.insertNode(10)
sll3.insertNode(11)
sll4 = SinglyLinkedList()
sll4.insertNode(12)
sll4.insertNode(13)
sll4.insertNode(15)
print(intersect(sll3, sll4))