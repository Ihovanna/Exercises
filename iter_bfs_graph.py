from collections import deque

class Graph:
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict

    def bsf(self, start_node):
        if not self.adjacency_graph:
            return []
        
        visited = [start_node]
        q = deque([start_node])

        while q:
            current = q.popleft()

            for node in self.adjacent_graph[current]:
                if node not in visited:
                    visited.append(node)
                    q.appendright(node)

        return visited