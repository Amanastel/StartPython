class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def dfs(self, start):
        visited = [False] * self.vertices
        self._dfs_util(start, visited)

    def _dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

# Test the DFS implementation
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

print("DFS traversal:")
graph.dfs(0)
print("\nExpected: 0 1 3 5 2 4")