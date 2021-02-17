def insertSorted(array, n):
    i = len(array) - 2
    while i > 0:
        if array[i] > n:
            array[i+1] = array[i]
        else:
            break
        i -= 1
    array[i+1] = n
    array.append(0)
    return array

a = [1, 5, 10, 15, 20, 30, 40, 0]
print("Insert Sorted")
print(insertSorted(a, 11))

def reverseArray(array):
    left = 0
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array

a = [1, 5, 10, 15, 20, 30, 40, 0]
print("Reverse Array")
print(reverseArray(a))

def isSubset(a, b):
    for c in a:
        if c in b:
            b = b.replace(c, '', 1)
        else:
            return False
    return True

a = "abc"
b = "$$acb56j"
print("Is Subset")
print(isSubset(a, b))

def isSubset2(a, b):
    lettersInB = set()
    for c in b:
        lettersInB.add(c)

    for c in a:
        if c not in lettersInB:
            return False
    return True

a = "abc"
b = "$acb56j"
print("Is Subset 2")
print(isSubset2(a, b))

def revenue(sales):
    totalSales = {}
    for prod, sale in sales:
        totalSales[prod] = totalSales.get(prod, 0) + sale

    for prod, sale in totalSales.items():
        print("Product: {} - Sales = {}".format(prod, sale))

sales = [[1000, 1],
        [2000, 2],
        [3000, 3],
        [1000, 5],
        [3000, 3],
        [2000, 4]
        ]

print("Sales")
revenue(sales)

def reverseStack(s):
    newStack = []
    while s:
        newStack.append(s.pop())

    return newStack

print("Reverse Stack")
s = [1, 2, 3, 4, 5]
print(reverseStack(s))
print(s)

def reverseStackKeepOriginal(s):
    newStack = []
    temp = []
    while s:
        element = s.pop()
        newStack.append(element)
        temp.append(element)
    while temp:
        s.append(temp.pop())

    return newStack

print("Reverse stack keep original")
s = [1, 2, 3, 4, 5]
print(reverseStackKeepOriginal(s))
print(s)

def removeEvenFromStack(s):
    temp = []
    while s:
        element = s.pop()
        if element % 2 != 0:
            temp.append(element)
    while temp:
        s.append(temp.pop())
    return s

print("Remove Even numbers from Stack, return original stack")
s = [1, 2, 3, 4, 5]
print(removeEvenFromStack(s))

def identicalQueues(q1, q2):
    if len(q1) != len(q2):
        return False
    while q1:
        if q1.pop() != q2.pop():
            return False
    return True

q1 = [1, 2, 3, 4, 5]
q2 = [1, 2, 3, 4, 5]
print("Identical Queues: true case")
print(identicalQueues(q1, q2))
q1 = [1, 2, 3, 4, 5]
q2 = [1, 2, 7, 4, 5]
print("Identical Queues: false case")
print(identicalQueues(q1, q2))

def removeNthElementFromQueue(q, n):
    temp = []
    i = 1
    while q:
        if i != n:
            temp.append(q.pop(0))
        else:
            q.pop(0)
        i += 1

    return temp

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Remove Nth Element from Queue")
print(removeNthElementFromQueue(q, 5))

def mergeArrays(a, b):
    newArray = []
    indexA = 0
    indexB = 0
    while indexA < len(a) and indexB < len(b):
        if a[indexA] < b[indexB]:
            newArray.append(a[indexA])
            indexA += 1
        else:
            newArray.append(b[indexB])
            indexB += 1

    while indexA < len(a):
        newArray.append(a[indexA])
        indexA += 1

    while indexB < len(b):
        newArray.append(b[indexB])
        indexB += 1

    return newArray

a = [1, 10, 15, 20, 25]
b = [5, 6]
print("merge 2 sorted arrays into new array")
print(mergeArrays(a, b))
a = [1, 10, 15, 20, 25]
b = [5, 6, 30, 45, 50, 60, 90]
print("merge 2 sorted arrays into new array")
print(mergeArrays(a, b))

"""
5 10 3 8 2 9 7 1 6 4
5 3 10 8 2 9 7 1 6 4
3 5 10 8 2 9 7 1 6 4
3 5 8 10 2 9 7 1 6 4
3 5 8 2 10 9 7 1 6 4
3 5 2 8 10 9 7 1 6 4
3 2 5 8 10 9 7 1 6 4
2 3 5 8 10 9 7 1 6 4
2 3 5 8 9 10 7 1 6 4
2 3 5 8 9 7 10 1 6 4
2 3 5 8 7 9 10 1 6 4
2 3 5 7 8 9 10 1 6 4
2 3 5 7 8 ...
1 2 3 4 5 6 7 8 9 10
"""
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i -1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
    
a = [10, 5, 3, 8, 2, 9, 7, 1, 6, 4]
print("Insertion Sort")
print(insertionSort(a))

def binarySearchIterative(array, v):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + (right - left) // 2)
        if array[mid] == v:
            return mid
        elif array[mid] > v:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binarySearchRecursive(array, v):
    def binarySearchHelper(array, v, left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if array[mid] == v:
            return mid
        
        if array[mid] < v:
            return binarySearchHelper(array, v, mid+1, right)
        else:
            return binarySearchHelper(array, v, left, mid-1)

    return binarySearchHelper(array, v, 0, len(array)-1)

def binarySearchRotated(array, v):
    left = 0
    right = len(array) - 1
    while left <=right:
        mid = (right + left) // 2
        if array[mid] == v:
            return mid
        # Left half is sorted
        if array[left] < array[mid]:
            # Key is in left half
            if v >= array[left] and v <= array[mid]:
                # Search in left half
                right = mid - 1
            else:
                # Search in right half
                left = mid + 1
        else:
            # Right half is sorted
            if v >= array[mid] and v <= array[right]:
                # Key is in right half
                left = mid + 1
            else:
                right = mid - 1

    return -1

a = [1, 5, 8, 10, 15, 20, 50, 78, 99]
print("Binary Search Iterative")
print(binarySearchIterative(a, 8))
print("Binary Search Recursive")
print(binarySearchRecursive(a, 8))

a = [10, 20, 50, 78, 99, 1, 5, 8]
print(a)
print("Binary Search Rotated: search for 5")
print(binarySearchRotated(a, 5))
print("Binary Search Rotated: search for 20")
print(binarySearchRotated(a, 20))
print("Binary Search Rotated: search for 15")
print(binarySearchRotated(a, 15))
print("Binary Search Rotated: search for 10")
print(binarySearchRotated(a, 10))
a = [3, 3, 3, 3, 3, 3, 3, 3]
print("Binary Search Rotated: search for 3")
print(binarySearchRotated(a, 3))
print("Binary Search Rotated: search for 5")
print(binarySearchRotated(a, 5))

class Node():
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def treeDFS(node, v):
    if node == None:
        return False
    if node.val == v:
        return True
    return treeDFS(node.left, v) or treeDFS(node.right, v)

root = Node(10)
root.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(6)
root.right = Node(12)

print("Tree DFS look for value 1 (true)")
print(treeDFS(root, 1))
print("Tree DFS look for value 20 (false)")
print(treeDFS(root, 20))
print("Tree DFS look for value 5 (true)")
print(treeDFS(root, 5))

def treeInOrder(node):
    if node == None:
        return 
    treeInOrder(node.left)
    print(node.val)
    treeInOrder(node.right)

print("Tree In Order trasversal")
treeInOrder(root)

def treeBFS(node):
    queue = []
    queue.append(node)
    while queue:
        n = queue.pop(0)
        print(n.val)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

print("Tree BFS")
treeBFS(root)

from itertools import permutations

s="abc"
print("All permutations")
result = permutations(s)
for p in result:
    print("".join(p))