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

    def removeDups(self):
        d = set()
        current = self.head
        while current.next:
            if current.next.val in d:
                current.next = current.next.next
            else:
                d.add(current.next.val)
                current = current.next

    def returnKth(self, k):
        current = self.head
        runner = current
        i = 0
        while current:
            if i >= k:
                runner = runner.next 
            current = current.next
            i += 1

        if runner:
            return runner
        else:
            return -1

    def deleteMiddle(self, m):
        if m == None or m.next == None:
            return False
        m.val = m.next.val
        m.next = m.next.next


sll = SinglyLinkedList()
sll.insertNode(6)
sll.insertNode(6)
sll.insertNode(5)
sll.insertNode(4)
sll.insertNode(3)
sll.insertNode(3)
sll.insertNode(3)
sll.insertNode(2)
sll.insertNode(1)
sll.printList()
sll.removeDups()
sll.printList()
sll.deleteMiddle(sll.returnKth(3))
sll.printList()