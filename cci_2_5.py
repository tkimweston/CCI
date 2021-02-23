class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, val):
        temp = Node(val)
        temp.next = self.head
        self.tail = self.head
        self.head = temp

    def insertTail(self, val):
        temp = Node(val)
        if not self.head:
            self.head = temp
        if not self.tail:
            self.tail = temp
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

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
            return runner.val
        else:
            return -1

    def deleteMiddle(self):
        current = self.head
        runner = current
        i = 0
        while current:
            print('current')
            if i > 0 and i % 2 == 0:
                print('runner')
                runner = runner.next
            current = current.next
            i += 1
        runner.next = runner.next.next

# optimized 2/15/21
# 2/23/21: simplified while loop
def sumList(a, b):
    pa = a.head
    pb = b.head
    new = SinglyLinkedList()
    carry = 0
    while pa or pb or carry > 0:
        sum = carry
        if pa:
            sum += pa.val
        if pb:
            sum += pb.val
        carry = sum // 10
        new.insertTail(sum % 10)
        if pa:
            pa = pa.next
        if pb:
            pb = pb.next

    return new

slla = SinglyLinkedList()
slla.insertNode(6)
slla.insertNode(1)
slla.insertNode(7)
slla.printList()
sllb = SinglyLinkedList()
sllb.insertNode(2)
sllb.insertNode(9)
sllb.insertNode(5)
sllb.printList()
slls = sumList(slla, sllb)
slls.printList()
sllc = SinglyLinkedList()
sllc.insertNode(9)
sllc.insertNode(9)
sllc.printList()
slld = SinglyLinkedList()
slld.insertNode(9)
slld.insertNode(9)
slld.insertNode(9)
slld.printList()
slls = sumList(sllc, slld)
slls.printList()