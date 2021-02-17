def rotateCCW(m):
    n = len(m)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            temp = m[x][y]
            m[x][y] = m[y][n-1-x]
            m[y][n-1-x] = m[n-1-x][n-1-y]
            m[n-1-x][n-1-y] = m[n-1-y][x]
            m[n-1-y][x] = temp


def rotateCW(m):
    n = len(m)
    for x in range(n // 2):
        for y in range(x, n-x-1):
            temp = m[x][y]
            m[x][y] = m[n-1-y][x]
            m[n-1-y][x] = m[n-1-x][n-1-y]
            m[n-1-x][n-1-y] = m[y][n-1-x]
            m[y][n-1-x] = temp

m = [[1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]]

rotateCCW(m)
print(m)
rotateCW(m)
print(m)