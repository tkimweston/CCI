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



sll = SinglyLinkedList()
sll.insertNode(6)
sll.insertNode(5)
sll.insertNode(4)
sll.insertNode(3)
sll.insertNode(2)
sll.insertNode(1)
sll.printList()
print(sll.find(5))
sll.deleteNode(5)
sll.printList()
sll.deleteNode(1)
sll.printList()
sll.deleteNode(6)
sll.printList()
sll.insertNode(7)
sll.printList()
sll.deleteNode(4)
print()
sll.printList()
print()
sll.reverseList()
sll.printList()

