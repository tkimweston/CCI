def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

a = [5, 3, 6, 7, 8, 2, 10]
insertionSort(a)
print(a)
a = [31, 41, 59, 26, 41, 58]
insertionSort(a)
print(a)