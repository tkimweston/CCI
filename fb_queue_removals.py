def findPositions(arr, x):
      # Write your code here
  original = []
  removed = []
  result = []
  for i in range(len(arr)-1, -1, -1):
    original.append([arr[i], i + 1])
  for i in range(x):
    for j in range(min(x, len(original))):
      removed.append(original.pop())
    print(removed)
    max = 0
    maxIndex = -1
    for k in range(len(removed)):
      if removed[k][0] > max:
        max = removed[k][0]
        maxIndex = k
      elif removed[k][0] == max and maxIndex == -1:
        maxIndex = k
      if removed[k][0] > 0:
        removed[k][0] -= 1
    result.append(removed[maxIndex][1])
    del removed[maxIndex]
    print(result, removed)
    while len(removed) > 0:
      original.append(removed.pop())
      
  return result

  