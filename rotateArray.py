def rotateLeft(a, d):
    swap(a, 0, d)
    swap(a, d + 1, len(a) - 1)
    swap(a, 0, len(a) - 1)

def swap(a, left, right):
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

def rotateRight(a, d):
    swap(a, 0, d - 1)
    swap(a, d, len(a) - 1)
    swap(a, 0, len(a) - 1)

def rotateInPlace(a, d):
    temp = a[d]
    while     

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotateLeft(a, 4)
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotateRight(a, 4)
print(a)