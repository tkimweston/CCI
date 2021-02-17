#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insertHelper(self, curr, value):
        if curr.value > value:
            if curr.left:
                self.insertHelper(curr.left, value)
            else:
                curr.left = Node(value)
        else:
            if curr.right:
                self.insertHelper(curr.right, value)
            else:
                curr.right = Node(value)

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

def isBST1Helper(root, array):
    if root == None:
        return 

    isBST1Helper(root.left, array)
    array.append(root.value)
    isBST1Helper(root.right, array)

    return

def isBST1(root):
    array = []
    isBST1Helper(root, array)

    prev = array[0]
    for i in range(1, len(array)):
        if prev > array[i]:
            return False

    return True
    

def isBST2(root, lastPrinted = 0):
    if root == None:
        return True

    if isBST2(root.left) == False:
        return False

    if lastPrinted != 0 and root.value <= lastPrinted:
        return False
    lastPrinted = root.value

    if isBST2(root.right) == False:
        return False

    return True

def isBSTMinMax(node, min = None, max = None):
    if node == None:
        return True

    if (min != None and node.value <= min) or (max != None and node.value > max):
        return False
    
    if not isBSTMinMax(node.left, min, node.value) or not isBSTMinMax(node.right, node.value, max):
        return False

    return True

root = Tree()
root.insert(10)        
root.insert(9)        
root.insert(100)        
root.insert(50)        
preOrder(root.root)
print("")
inOrder(root.root)
print("")
posOrder(root.root)
print("")
print(level(root.root))
root.insert(8)
root.insert(7)
root.insert(6)
print("")
inOrder(root.root)
print("")
print(level(root.root))
print(avgByDepth(root.root))
print(printTreeTop(root.root))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minTree = Tree()
minimalTree(minTree, a)
print(level(minTree.root))
inOrder(minTree.root)
print()
d = {}
listOfDepths(minTree.root, d)
print(d)
print(checkBalanced(minTree.root))
print(checkBalanced(root.root))
print(checkBalanced2(minTree.root))
print(checkBalanced2(root.root))
print('isBST1')
print(isBST1(minTree.root))
print('isBST2')
print(isBST2(minTree.root))
print('isBSTMinMax')
print(isBSTMinMax(minTree.root))