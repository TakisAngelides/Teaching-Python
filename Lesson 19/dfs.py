from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        self.graph[u].append(v)

    def dfs(self, u, visited):

        visited.append(u)

        for neighbour in self.graph[u]:

            if neighbour not in visited:

                self.dfs(neighbour, visited)

visited = []

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(2, visited)

print(visited)