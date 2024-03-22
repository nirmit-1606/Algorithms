# Dijkstra
   
#    Given an undirected graph, find the shortest path from source (node 0)
#    to target (node n-1). 
   
#    Edge weights are guaranteed to be non-negative, since Dijkstra doesn't work
#    with negative weights, e.g.
 
#        3
#    0 ------ 1   
#      \    /
#     2 \  / -2
#        \/
#        2
   
#    in this example, Dijkstra would return length 2 (path 0-2), 
#    but path 0-1-2 is better (length 1).

#    For example (return a pair of shortest-distance and shortest-path):
   
#        1
#    0 ------ 1   
#      \    /  \
#     5 \  /1   \6
#        \/   2  \
#        2 ------ 3
            
#    shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])     returns (4, [0,1,2,3])

#    If the target node (n-1) is unreachable from the source (0), return None:

#    shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])     returns None

#    Another example:

#       1          1
#    0-----1    2-----3

#    shortest(4, [(0,1,1), (2,3,1)])    returns None

#    Tiebreaking: arbitrary. Any shortest path would do.

from Source.heapdict import heapdict
from collections import defaultdict
import sys

def shortest(n, edges):

    def solution(i):
        # Recursively find the shortest path using backtracking
        if i == -1:
            return []
        else:
            path_cost[0] += weight[i, back[i]]  # Add the edge weight to the path cost
            return solution(back[i]) + [i]  # Recursively append the current node to the solution path

    # Initialize a defaultdict to store the edges for each node and a defaultdict to store edge weights
    node_edges, weight = defaultdict(list), defaultdict(int)
    
    # Populate the dictionaries with edge information from the input list
    for u, v, w in edges:
        node_edges[u].append(v)
        node_edges[v].append(u)  # Since the graph is undirected, add both directions
        weight[u, v] = w
        weight[v, u] = w
    
    # Initialize a priority queue to store nodes and their distances
    Q = heapdict()
    Q[0] = 0  # Initialize the source node with distance 0
    
    # Initialize a list to store distances from the source node to each node
    distance = [sys.maxsize] * n  # Each node is initially at infinite distance
    distance[0] = 0  # Distance for the source node is set to 0
    
    # Initialize a list to store the previous node in the shortest path for each node
    back = [-1] * n
    
    # Main loop of Dijkstra's algorithm
    while Q:
        v, d = Q.popitem()  # Pop the node with the shortest distance from the priority queue
        for u in node_edges[v]:
            # Update the distance for adjacent nodes if a shorter path is found
            if distance[v] + weight[v, u] < distance[u]:
                distance[u] = distance[v] + weight[v, u]
                back[u] = v  # Update the previous node for backtracking
                Q[u] = distance[u]  # Update the priority queue with the new distance
    
    path_cost = [0]  # Initialize a list to store the path cost
    shortest_path = solution(n - 1)  # Find the shortest path using backtracking from the target node
    
    # Check if the target node is reachable from the source node
    if shortest_path[0] == 0:
        return path_cost[0], shortest_path  # Return the path cost and the shortest path
    else:
        return None  # If the target node is unreachable, return None
