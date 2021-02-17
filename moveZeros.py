def moveZeros(a):
    for i in range(len(a)):
        if a[i] == 0:
            if i > 0:
                j = i
                while j > 0: 
                    a[j - 1], a[j] = a[j], a[j - 1]
                    j -= 1

a = [1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 8, 9]
moveZeros(a)
print(a)    

def moveZeros2(a):
    if len(a) < 1:
        return
    writeIdx = len(a) - 1
    readIdx = len(a) - 1
    while readIdx >= 0:
        if a[readIdx] != 0:
            a[writeIdx] = a[readIdx]
            writeIdx -= 1
        readIdx -= 1
    while writeIdx >= 0:
        a[writeIdx] = 0
        writeIdx -= 1

def moveZeros3(arr):
    writeIdx = len(arr) - 1
    readIdx = len(arr) - 1
    while readIdx >= 0:
        if arr[readIdx] != 0:
            arr[writeIdx] = arr[readIdx]
            writeIdx -= 1
        readIdx -= 1
    while writeIdx >= 0:
        arr[writeIdx] = 0
        writeIdx -= 1

a = [1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 8, 9]
moveZeros2(a)
print(a) 
a = [0, 1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 8, 9]
moveZeros2(a)
print(a) 
a = [0, 1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 8, 9]
moveZeros3(a)
print(a) 