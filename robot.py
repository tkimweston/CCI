def robot(grid, x, y):
    if len(grid) == y and len(grid[0]) == x:
        return True

    vectorX = [1, 0]
    vectorY = [0, 1]

    for i in range(2):
