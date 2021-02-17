def twoSum(a, sum):
    if len(a) == 1:
        return False
    diffs = set()

    for num in a:
        if num in diffs:
            return [num, sum - num]
        else:
            diffs.add(sum - num)
            print(diffs)

a = [7, 1, 5, 3, 6, 4]
print(twoSum(a, 4))