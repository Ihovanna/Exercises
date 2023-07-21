import collections
import heapq

def network_delay_time(times, n, source):
    graph = collections.defaultdict(list) # empty dict that never returns a KeyError

    for (initial_node, destiny, weight) in times:
        graph[initial_node].append((destiny,weight))
        
    q = [(0, source)]
    shortest_path = {}
    while q:
        weight, destiny = heapq.heappop(q)
        if destiny not in shortest_path:
            shortest_path[destiny] = weight
            for destiny_i, weight_i in graph[destiny]:
                heapq.heappush(q, (weight + weight_i, destiny_i))
                
    if len(shortest_path) == n:
        return max(shortest_path.values())
    else:
        return -1
        
times = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
    ]
source = 2
n = 4
print(network_delay_time(times, n, source))

# Test #2 - Output -1
times = [
    [2,1,1],
    [2,3,2],
    [3,1,1]
    ]
source = 1
n = 3
print(network_delay_time(times, n, source))

# Test #3 - Output ?
times = []
source = 0
n = 0
print(network_delay_time(times, n, source))


'''
Ada's Solution:

import collections
from heapq import heappush, heappop
def network_delay_time(times, n, source):
    # Initialize dictionary with default value as a list
    # More information about defaultdict can be found in the documentation for Python: https://docs.python.org/3/library/collections.html#collections.defaultdict
    graph = collections.defaultdict(list)
    # For each edge in the graph, add the neighbors for a node to the graph
    # such that graph[node] = [(neighbor1, time1), (neighbor2, time2)...]
    # The graph is directed, so we only need to append one direction
    for u, v, time in times:
        graph[u].append([v, time])

    # initialize the time needed to reach each node in the graph, overestimating to infinity
    time_needed = [float('inf')] * n
    # set the time to reach the source node to 0
    time_needed[source-1] = 0
    # initialize min heap for traversal
    # priority 0 to travel to the source node
    heap = [[0, source]] 

    visited = set() # used to record all visited nodes
    visited.add(source)

    # while there are nodes in the heap
    while heap:
        # pop off the closest node
        time, curr_node = heappop(heap)
        # traverse through the current node's neighbors
        for neighbor, neighbor_time in graph[curr_node]:
            # calculate the total time to travel to the neighbor
            total_time = time + neighbor_time
            # if the total time is less than the previous time stored to travel to the neighbor
            if total_time < time_needed[neighbor - 1]:
                # store the total time as the time needed to travel to the neighbor
                time_needed[neighbor - 1] = total_time
                # add the node to the list of visited nodes
                visited.add(neighbor)
                # push onto heap to be visited later
                heappush(heap, [total_time, neighbor])

    # return the max time in time_needed list if all of the nodes have been visited, otherwise return -1
    return max(time_needed) if len(visited) == n else -1

'''