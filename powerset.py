def powerset(array):
    subsets = [[]]
    for e in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [e])

    return subsets

def powerset2(array):
    subset = [None for _ in array]
    helper(array, subset, 0)

def helper(array, subset, index):
    if index == len(array):
        print(subset)
    else:
        subset[index] = None
        helper(array, subset, index + 1)
        subset[index] = array[index]
        helper(array, subset, index + 1)

def powersetbinary(set):
    N = len(set)
    MAX_VAL = 1 << N
    for subset in range(MAX_VAL):
        print("{ ", end='')
        for i in range(N):
            mask = 1 << i
            if (subset & mask) == mask:
                print('{} '.format(set[i]), end='')
        print('}')

inp = [1, 2, 3]
print(powerset(inp))
print(powerset2(inp))
print(powersetbinary(inp))

