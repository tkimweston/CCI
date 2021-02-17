def findHighLowIndex(a, key):
    if len(a) == 0:
        return -1

    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            left = mid - 1
            while left >= 0 and a[left] == key:
                left -= 1
            right = mid + 1
            while right <= len(a) - 1 and a[right] == key:
                right += 1
            return [left + 1, right - 1]
        elif key > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def findLowIndex(a, key):
    if len(a) == 0:
        return -1

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if key > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(a) and a[low] == key:
        return low
    return -1

def findHighIndex(a, key):
    if len(a) == 0:
        return -1

    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if high < len(a) and a[high] == key:
        return high
    return -1
        
def findHighLowIndex2(a, key):
    low = findLowIndex(a, key)
    high = findHighIndex(a, key)
    if low == -1 or high == -1:
        return -1
    return [low, high]

a = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
print(findHighLowIndex(a, 1))
print(findHighLowIndex(a, 2))
print(findHighLowIndex(a, 3))
print(findHighLowIndex(a, 4))
print(findHighLowIndex(a, 5))
print(findHighLowIndex(a, 6))
print(findHighLowIndex(a, 7))
print(findHighLowIndex2(a, 1))
print(findHighLowIndex2(a, 2))
print(findHighLowIndex2(a, 3))
print(findHighLowIndex2(a, 4))
print(findHighLowIndex2(a, 5))
print(findHighLowIndex2(a, 6))
print(findHighLowIndex2(a, 7))