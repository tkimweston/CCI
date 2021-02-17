class Stack():
    def __init__(self):
        self.size = 0
        self.top = 0
        self.stack = []
    
    def len(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, val):
        self.stack.append(val)
        self.top += 1
        self.size += 1

    def peek(self):
        if self.size == 0:
            return -1
        return self.stack[self.top - 1]

    def pop(self):
        if self.size == 0:
            return -1
        retVal = self.stack.pop()
        self.top -= 1
        self.size -= 1
        return retVal

    def printStack(self):
        print(self.stack)

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.printStack()
print(stack1.isEmpty())
print(stack1.len())
print(stack1.pop())
print(stack1.peek())
print(stack1.len())
stack1.printStack()