"""

4,532

[4, 5, 3, 2]

[2, 3, 5, 4]

def add(n1, n2): -> n3 where n3 = n1 + n2



return = 5209 + 321 = 5530
should return [0, 3, 5, 5]

n1 [1, 2, 3]
n2 [9, 0, 2, 5]
len1 = 3
len2 = 4


55 + 45


def multiply(n1, n2)

[1, 2, 3]

[9, 0, 2, 5]

45 x 23 =

 45
x23
----
45 * 3 + 
(45 * 2 ) with a 0 pre-pended

I can hear you
So I will start coding



"""

def add(n1, n2):
    len1 = len(n1)
    len2 = len(n2)
    
    l = min(len1, len2)
    carry = 0
    result = []
    for i in range(l):
        r = n1[i] + n2[i] + carry
        result.append(r % 10)
        carry = r // 10
    if len1 > len2:
        for i in range(l, len1):
            result.append(n1[i] + carry)
            carry = 0
    elif len2 > len1:
        for i in range(l, len2):
            result.append(n2[i] + carry)
            carry = 0
    if carry > 0:
        result.append(carry)
    return result
            
def multiply_original_interview(n1, n2):
    multiplier = 1
    for i in range(n2):
        multiplyBy = n2[i] * multiplier
        
        while multiplyBy > 1:
            if multiplier < 10:
                result = []
                for j in range(multiplyBy):
                    result = add(result, n1)

            else:
                shiftRight(result, multiplier // 10)
                multiplyBy -= multiplier
                
        multipler *= 10

""" O(N1 * N2) """
def multiply1(n1, n2):
    result = [0] * (len(n1) + len(n2))
    l = 0
    for i in range(len(n2)):
        carrym = 0
        carrys = 0
        k = l
        for j in range(len(n1)):
            mult = n2[i] * n1[j] + carrym
            carrym = mult // 10
            sum = (result[k] + carrys + mult % 10)
            carrys = sum // 10
            result[k] = sum % 10
            k += 1
        if carrym > 0:
            result[k] += carrym
            carrym = 0
        l += 1
    if carrys > 0:
        result[k] += carrys
    return result

def multiply_as_requested(n1, n2):
    result = [0] * (len(n1) + len(n2))
    for i in range(len(n2)):
        if i > 0:
            result.insert(0, 0)
        temp = [0] * len(n1)
        if n2[i] > 1:
            for k in range(len(n1)):
                temp[k] = n1[k]
            for j in range(n2[i] - 1):
                temp = add(n1, temp)
                print(temp, j)
        result = add(result, temp)

    return result

    
num1 = [1, 2, 3]
num2 = [9, 0, 2, 5]
print(add(num1, num2))
num1 = [1, 2, 3]
num2 = []
print(add(num1, num2))
num1 = [9, 9]
num2 = [9, 9]
print(multiply1(num1, num2))
num1 = [0, 1]
num2 = [0, 1]
print(multiply1(num1, num2))
num1 = [1, 2, 3]
num2 = [9, 0, 2, 5]
print(multiply1(num1, num2))
n1 = []
n2 = []
for i in range(10):
    n1.append(1)
    n2.append(1)
print(multiply1(n1, n2))
num1 = [9, 9]
num2 = [9, 9]
print(multiply_as_requested(num1, num2))
num1 = [0, 1]
num2 = [0, 1]
print(multiply_as_requested(num1, num2))