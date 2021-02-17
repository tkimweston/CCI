def arrayOfProducts(a):
    leftProd = [1] * len(a)
    rightProd = [1] * len(a)
    result = [1] * len(a)
    ProdSoFar = 1
    for i in range(len(a)):
        leftProd[i] = ProdSoFar
        ProdSoFar *= a[i]
    ProdSoFar = 1
    for i in reversed(range(len(a))):
        rightProd[i] = ProdSoFar
        ProdSoFar *= a[i]
    for i in range(len(a)):
        result[i] = leftProd[i] * rightProd[i]
    return result

def arrayOfProducts2(a):
    soFar = 1
    result = [1] * len(a)
    for i in range(len(a)):
        result[i] = soFar
        soFar *= a[i]
    soFar = 1
    for i in reversed(range(len(a))):
        result[i] *= soFar
        soFar *= a[i]
    return result

a = [5, 1, 4, 2]
print(arrayOfProducts(a))
print(arrayOfProducts2(a))