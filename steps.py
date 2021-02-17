def stairs(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stairs(n - 3) + stairs(n - 2) + stairs(n - 1)

def stairsHelper(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = stairsHelper(n - 3, memo) + stairsHelper(n - 2, memo) + stairsHelper(n - 1, memo)
        return memo[n]

def stairsMemo(n):
    memo = [-1 for _ in range(n + 1)]
    return stairsHelper(n, memo)

print(0, stairs(0))
print(1, stairs(1))
print(2, stairs(2))
print(3, stairs(3))
print(4, stairs(4))
print(5, stairs(5))
print(0, stairsMemo(0))
print(1, stairsMemo(1))
print(2, stairsMemo(2))
print(3, stairsMemo(3))
print(4, stairsMemo(4))
print(5, stairsMemo(5))