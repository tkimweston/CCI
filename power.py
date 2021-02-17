import time

def powerRec(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    r = powerRec(x, n // 2)
    if n % 2 == 0:
        return r * r
    else:
        return x * r * r

    
def power(x, n):
    neg = n < 0
    if neg:
        n *= -1

    answer = powerRec(x, n)
    if neg:
        return 1 / answer
    return answer
    
def powerRecMemo(x, n, memo):
    if n == 0:
        return 1
    if n == 1:
        return x

    if n in memo:
        r = memo[n]
    else:
        r = powerRecMemo(x, n // 2, memo)
        memo[n // 2] = r

    if n % 2 == 0:
        return r * r
    else:
        return x * r * r

def powerMemo(x, n):
    neg = n < 0
    if neg:
        n *= -1
    memo = {}

    answer = powerRecMemo(x, n, memo)
    if neg:
        return 1 / answer
    return answer

print(power(2, 2))
print(power(2, 5))
start = time.time()
print(power(2, 2000000))
print(time.time() - start)
print(powerMemo(2, 2))
print(powerMemo(2, 5))
start = time.time()
print(powerMemo(2, 2000000))
print(time.time() - start)