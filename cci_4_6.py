#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None

    def insertHelper(self, curr, value):
        if curr.value > value:
            if curr.left:
                self.insertHelper(curr.left, value)
            else:
                curr.left = Node(value)
                curr.left.parent = curr
        else:
            if curr.right:
                self.insertHelper(curr.right, value)
            else:
                curr.right = Node(value)
                curr.right.parent = curr

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insertHelper(self.root, value)

def level(root):
    if root == None:
        return -1
    return max(level(root.left), level(root.right)) + 1

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value, end = " ")
    inOrder(root.right)

def preOrder(root):
    if root == None:
        return
    print(root.value, end = " ")
    preOrder(root.left)
    preOrder(root.right)

def posOrder(root):
    if root == None:
        return
    posOrder(root.left)
    posOrder(root.right)
    print(root.value, end = " ")
    
def collect(node, data, depth=0):
    if not node:
        return None
    if depth not in data:
        data[depth] = []

    data[depth].append(node.value)
    collect(node.left, data, depth + 1)
    collect(node.right, data, depth + 1)

def avgByDepth(node):
    data = {}
    collect(node, data)
    result = []
    for _, values in data.items():
        avg = sum(values) / len(values)
        result.append(avg)
    return result

def printTreeTop(node):
    res = []
    current = node.left
    while current:
        res.append(current.value)
        current = current.left
    res = res[-1::-1]
    res.append(node.value)
    current = node.right
    while current:
        res.append(current.value)
        current = current.right
    return res
    
def minimalTree(tree, array):

    def minimalTreeHelper(tree, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        tree.insert(array[mid])
        minimalTreeHelper(tree, array, start, mid - 1)
        minimalTreeHelper(tree, array, mid + 1, end)
        
    return minimalTreeHelper(tree, array, 0, len(array) - 1)

def listOfDepths(root, d, level = 0):
    if root == None:
        return
    
    if level not in d:
        d[level] = []

    d[level].append(root.value)

    listOfDepths(root.left, d, level + 1)
    listOfDepths(root.right, d, level + 1)

def checkBalanced(root):
    if root == None:
        return True

    diff = abs(level(root.left) - level(root.right))
    if diff > 1:
        return False 
    return checkBalanced(root.left) and checkBalanced(root.right)

def checkBalanced2Helper(root):
    if not root:
        return -1

    leftH = checkBalanced2(root.left)
    if leftH == -10:
        return -10
    
    rightH = checkBalanced2(root.right)
    if rightH == -10:
        return -10

    diff = abs(leftH - rightH)
    if diff > 1:
        return -10
    else:
        return max(leftH, rightH) + 1

def checkBalanced2(root):
    return checkBalanced2Helper(root)


def inOrderSucc(n):
    if n == None:
        return None

    if n.right:
        return leftMostChild(n.right)

    q = n
    x = q.parent
    while x != None and x.left != q:
        q = x
        x = x.parent

    return x.value


def leftMostChild(n):
    if n == None:
        return None

    while n.left:
        n = n.left 

    return n.value


tree = Tree()
tree.insert(5)        
tree.insert(2)        
tree.insert(1)        
tree.insert(3)        
tree.insert(4)        
tree.insert(8)        
tree.insert(6)        
tree.insert(9)        
tree.insert(7)        
tree.insert(10)        
inOrder(tree.root)
print("")
posOrder(tree.root)
print("")
print(level(tree.root))
print(avgByDepth(tree.root))
print(printTreeTop(tree.root))
d = {}
listOfDepths(tree.root, d)
print(d)
print(checkBalanced(tree.root))
print(checkBalanced2(tree.root))
print(inOrderSucc(tree.root.right.left.right                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ))