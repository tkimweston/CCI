""" Kadane's Algorithm """

def largestSum(array):
    currentSum = array[0]
    maxSum = array[0]
    for i in range(1, len(array)):
        currentSum = max(array[i], currentSum + array[i])
        maxSum = max(maxSum, currentSum)
    return maxSum

a = [2, -8, 3, -2, 4, -10]
print(largestSum(a))
