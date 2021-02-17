def mergeSegments(segments):
    if len(segments) == 0:
        return []
    result = []
    prev = segments[0]
    for segment in segments[1:]:
        if prev[1] >= segment[0]:
            prev[0] = min(prev[0], segment[0])
            prev[1] = max(prev[1], segment[1])
        else:
            result.append(prev)
            prev = segment

    result.append(prev)
    return result

def mergeIntervals(intervals):
    result = [[intervals[0][0], intervals[0][1]]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][0] = min(result[-1][0], intervals[i][0])
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append([intervals[i][0], intervals[i][1]])
    return result


segments = [[1, 4]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
segments = [[1, 4], [2, 5]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
segments = [[10, 12], [12, 15]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
segments = [[1, 4], [2, 4], [6, 8], [7, 9], [10, 15]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
segments = [[1, 15], [2, 4], [6, 8], [7, 9], [10, 15]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
segments = [[1, 4], [2, 4], [6, 8], [7, 9], [10, 15]]
print(mergeSegments(segments))
print(mergeIntervals(segments))
A = [ [30, 63], [66, 94], [36, 87], [16, 86], [26, 85], [24, 50], [17, 84], [5, 25], [67, 81], [23, 54], [84, 99], [48, 85], [23, 28], [3, 86], [63, 79], [18, 73], [6, 68], [34, 40], [61, 66], [60, 96], [95, 99], [1, 10], [4, 82], [19, 78], [23, 61], [30, 45], [53, 87], [10, 42], [80, 93], [33, 73], [64, 65], [29, 71], [73, 89], [2, 98], [62, 67], [84, 98], [43, 58], [20, 45], [86, 92], [22, 100], [72, 74], [5, 52], [48, 56], [69, 93], [8, 98], [37, 47], [19, 45], [22, 99], [34, 97], [21, 80], [58, 77], [48, 66], [59, 91], [18, 33], [2, 7], [8, 92], [12, 32], [17, 83], [11, 16], [60, 75], [9, 11], [3, 61], [4, 18], [53, 68], [17, 39], [18, 93], [15, 55], [4, 34], [48, 85], [61, 65], [59, 77], [15, 37], [62, 82], [4, 78], [80, 96], [4, 42], [15, 48], [27, 45] ]
A.sort()
print(A)
print(A[0])
print(mergeIntervals(A))
