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

    def hasCycle(self):
        slow = self.head
        fast = self.head.next
        i = 0
        while fast:
            if slow == fast:
                return True
            else:
                fast = fast.next
                if i % 2 == 0:
                    slow = slow.next
            i += 1
        return False

    def hasCycle2(self):
        slow = self.head.next
        fast = self.head.next.next

        while slow != fast:
            fast = fast.next.next
            slow = slow.next
        slow = self.head.next
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow

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
sll1.printList()
sll1.head.next.next.next.next.next.next = sll1.head.next.next.next
print()
print(sll1.hasCycle())
print(sll1.hasCycle2())