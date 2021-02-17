import heapq

a = [1, 5, 9, 2, 4, 10, 3, 6, 11]
a
heapq._heapify_max(a)
a
print(heapq._heappop_max(a))
a
print(heapq._heappop_max(a))
a
heapq._heappush_max(a, 15)
a
print(heapq._heappop_max(a))
a