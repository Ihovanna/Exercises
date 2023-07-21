'''
Return the minimum time it takes for all of the nodes in the graph to receive the signal from 
the source node. If it is not possible for all of the nodes to receive the signal, return -1.
'''

def network_delay_time(times, n, source):
#     # times = list
#     #   times[i] = [u, v, w] = directed edge 
#     #       u = source node
#     #       v = target node
#     #       w = time take to travel from u to v


# Test 1 - Output 2
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
