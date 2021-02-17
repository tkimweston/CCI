def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i -1
        while j >= 0 and key < array[j]:
            print(i, j)
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
    
a = [10, 5, 3, 8, 2, 9, 7, 1, 6, 4]
print(insertionSort(a))

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
