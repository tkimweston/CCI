def findPositions(arr, x):
    arrPos = collections.deque()
    for i, num in enumerate(arr):
        arrPos.append([numi+1])
    ans = []
    def iterate(arrPosn):
        q = collections.deque()
        mx = -1
        mxp = -1
        while n > 0 and arrPos:
            apos = arrPos.popleft()
            if a > mx:
                mx = a
                mxp = pos
            q.append([apos])
            n -= 1
        ans.append(mxp)
        firsttime = True
        while q:
            apos = q.popleft()
            if a != mx:
                arrPos.append([a - 1 if a - 1 >= 0 else 0, pos])
            elif a == mx:
                if firsttime:
                    firsttime = False
                else:
                    arrPos.append([a - 1 if a - 1 >= 0 else 0 pos])
    n = x
    while x > 0 and arrPos:
        iterate(arrPos, n)
        x -= 1
    return ans