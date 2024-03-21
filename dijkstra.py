from heapdict import heapdict
from collections import defaultdict
import sys

def shortest(n, edges):

    def solution(i):                # find the rechable shortest path using back track
        if i == -1:
            return []
        else:
            path_cost[0] += weight[i, back[i]]      # add path cost 
                                                    # I tried using normal integer variable, but it was not callable. 
                                                    # I am not sure how to use it, so I simply used a unit length list that is callable.
            return solution(back[i]) + [i]

    node_edges, weight = defaultdict(list), defaultdict(int)
    for u,v,w in edges:             # make list
        node_edges[u].append(v)
        node_edges[v].append(u)
        weight[u,v] = w
        weight[v,u] = w
    
    Q = heapdict()
    Q[0] = 0
    
    distance = [sys.maxsize] * n    # each node is initially at infinite distance
    distance[0] = 0                 # distance for source node
    back = [-1] * n                 # back list to trace the path

    while Q:
        v,d = Q.popitem()           # pop shortest distance present in queue
        for u in node_edges[v]:
            if distance[v] + weight[v,u] < distance[u]:     # if found better distance for u
                distance[u] = distance[v] + weight[v,u]     # update the path
                back[u] = v                                 # update back track
                Q[u] = distance[u]                          # insert the node to queue
    
    path_cost = [0]
    shortest_path = solution(n-1)

    if shortest_path[0] == 0:       # if the final node is rechable from source node
        return path_cost[0], shortest_path
    else:                           # if the last node is unrechable
        return None