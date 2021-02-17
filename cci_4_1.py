from collections import deque

def routeBetweenNodes(g, s, e):
    if s == e:
        return True
    q = deque()    
    visited = [False] * len(g)
    q.appendleft(s)
    while len(q) > 0:
        u = q.pop()
        for v in g[u]:
            if visited[v] == False:
                if v == e:
                    return True
                else:
                    q.appendleft(v)
        visited[u] = True
    return False
    

g = {}
g[0] = [1, 4, 5]
g[1] = [3, 4]
g[2] = [1]
g[3] = [2, 4]
g[4] = []
g[5] = []

print(routeBetweenNodes(g, 0, 3))
print(routeBetweenNodes(g, 3, 5))
print(routeBetweenNodes(g, 2, 3))