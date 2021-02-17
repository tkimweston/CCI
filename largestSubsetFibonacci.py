def solution(arr):
    maxFibo = max(arr)
    fiboList = []
    fiboList.append(1)
    fiboList.append(1)
    fibo = 2
    i = 2
    while fibo <= maxFibo:
        fibo = fiboList[i-2] + fiboList[i-1]
        fiboList.append(fibo)
        i += 1
    print(fiboList)
    result = []
    for num in arr:
        if num in fiboList:
            result.append(num)
    return result

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(solution(a))