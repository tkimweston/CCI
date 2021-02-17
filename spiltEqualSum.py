""" O(N) """
def splitEqualSum(a):
    if len(a) == 1:
        return False
    if len(a) == 2 and a[0] != a[1]:
        return False

    left = 1
    right = len(a) - 2
    leftSum = a[0]
    rightSum = a[len(a) - 1]
    while left <= right:
        if leftSum < rightSum:
            leftSum += a[left]
            left += 1
        elif leftSum > rightSum:
            rightSum += a[right]
            right -= 1
        else:
            leftSum += a[left]
            rightSum += a[right]
            left += 1
            right -= 1
    if leftSum == rightSum:
        return True
    else:
        return False

""" O(N^2) """
def splitEqualSum2(array):
    summ = array[0]
    for index in range(1, len(array)):
        if summ == sum(array[index:]):
            return True
        summ += array[index]
    return False


a = [3, 4, 6, 13]
print(splitEqualSum(a))
print(splitEqualSum2(a))
a = [1, 2, 3, 4, 7, 2, 1]
print(splitEqualSum(a))
print(splitEqualSum2(a))
a = [1, 2, 5, 7]
print(splitEqualSum(a))
print(splitEqualSum2(a))
a = [10, 5, 3, 2]
print(splitEqualSum(a))
print(splitEqualSum2(a))
