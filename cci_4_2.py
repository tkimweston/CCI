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