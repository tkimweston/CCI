from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSHelper(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSHelper(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSHelper(v, visited)

    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def dfs2Helper(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for n in self.graph[v]:
            if n not in visited:
                self.dfs2Helper(n, visited)

    def dfs2(self, v):
        visited = set()
        self.dfs2Helper(v, visited)

    def dfs3(self, v, visited, count, nodes):
        visited.add(v)
        nodes[v] = count
        print(v, end=" ")
        for n in self.graph[v]:
            if n not in visited:
                self.dfs3(n, visited, count, nodes)

    def pathHelper(self, s, e, visited):
        if s == e:
            return True
        visited.add(s)
        for n in self.graph[s]:
            if n not in visited:
                return self.pathHelper(n, e, visited)

        return False
        
    def path(self, s, e):
        visited = set()
        return self.pathHelper(s, e, visited)

    def findComponents(self):
        visited = set()
        count = 0
        nodes = {}
        for k, v in self.graph.items():
            if k not in nodes:
                nodes[k] = 0
            for n in v:
                if n not in nodes:
                    nodes[n] = 0

        for n in nodes:
            if n not in visited:
                count += 1
                self.dfs3(n, visited, count, nodes)
        print(count, nodes)
        return

g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(7, 7)


g.DFS(2)
print()
g.dfs2(2)
print()
g.BFS(2)
print()
print(g.path(0, 3))
print(g.path(1, 2))
print(g.path(3, 0))
print(g.path(4, 6))
print(g.path(0, 6))
g.findComponents()
