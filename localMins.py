def localMins(a):
    if len(a) < 2:
        return [min(a)]
    mins = []
    dec = a[1] < a[0]
    asc = a[1] > a[0]
    if asc:
        mins.append(a[0])
    for i in range(2, len(a)):
        if dec and a[i] > a[i - 1]:
            dec = False
            asc = True
            mins.append(a[i - 1])
        elif asc and a[i] < a[i - 1]:
            dec = True
            asc = False
    if dec:
        mins.append(a[-1])
    return mins

def localMins2(a):
    if len(a) < 2:
        return min(a)

    mins = []

    if a[0] < a[1]:
        mins.append(a[0])

    for i in range(1, len(a) - 1):
        if a[i] < a[i - 1] and a[i] < a[i + 1]:
            mins.append(a[i])

    if a[-2] > a[-1]:
        mins.append(a[-1])
    return mins

a = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(localMins(a))
a = [8, 4, 2, 1, 3, 6, 7, 9, 5, 3, 2, 5, 7, 9, 4, 1, 4, 5]
print(localMins(a))
a = [1, 3, 5, 8, 4, 2, 1, 3, 6, 7, 9, 5, 3, 2, 5, 7, 9, 4, 1, 4, 5]
print(localMins(a))

a = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(localMins2(a))
a = [8, 4, 2, 1, 3, 6, 7, 9, 5, 3, 2, 5, 7, 9, 4, 1, 4, 5]
print(localMins2(a))
a = [1, 3, 5, 8, 4, 2, 1, 3, 6, 7, 9, 5, 3, 2, 5, 7, 9, 4, 1, 4, 5]
print(localMins2(a))