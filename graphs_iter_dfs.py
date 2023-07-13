from collections import deque

class Graph:
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict

    def dfs(self, start_node):
        if not self.adjacency_dict:
            return []
        
        q = deque([start_node])
        visited = []
        current = ''

        while q:
            popped_node = q.pop()
            if popped_node not in visited:
                current = popped_node
                visited.append(popped_node)
            
            # loop through current node's neighbor's
            neighbors = self.adjacency_dict[popped_node]
            for i in neighbors:
                if i not in visited:
                    q.append(i)
        
        return visited