"""
input: [2, 3, 5, 8, 13, 16, 29]
k = 3
output: [[2, 5], [5, 8], [13, 16]]
"""

def diffPairs(a, k):
    if len(a) < 2:
        return []

    result = []
    complement = set()

    for i in range(len(a)):
        complement.add(a[i] + k)

    print(complement)
    for i in range(len(a)):
        if a[i] in complement:
            result.append([a[i] - k, a[i]])

    return result

def diffPairs2(a, k):
    if len(a) < 2:
        return []

    result = []
    d = set(a)

    for num in a:
        if num + k in d:
            result.append([num, num + k])

    return result


a = [2, 3, 5, 8, 13, 16, 29]
print(diffPairs(a, 3))
print(diffPairs2(a, 3))