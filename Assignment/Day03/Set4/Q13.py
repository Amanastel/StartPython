from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Test the BFS implementation
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

print("BFS traversal:")
graph.bfs(0)
print("\nExpected: 0 1 2 3 4 5")