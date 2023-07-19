class Graph:
    def __init__(self, adjacency_dict = {}):
        self.adjacency_dict = adjacency_dict
    
    def dfs_helper(self, start_node, visited_nodes):
        if start_node not in visited_nodes:
            visited_nodes.append(start_node)

            for i in self.adjacency_dict[start_node]:
                self.dfs_helper(i, visited_nodes)
        
        return visited_nodes

    def dfs(self, start_node):
        visited = []

        if not self.adjacency_dict:
            return visited
        
        self.dfs_helper(start_node, visited)

        return visited
