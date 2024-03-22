# Viterbi Algorithm For Longest Path in DAG
   
#    Viterbi algorithm has just two steps:
#    a) get a topological order
#    b) follow that order, and do either forward or backward updates

#    This algorithm captures all DP problems on DAGs, for example,
#    longest path, shortest path, number of paths, etc.

#    In this problem, given a DAG (guaranteed acyclic!), output a pair (l, p) 
#    where l is the length of the longest path (number of edges), and p is the path. (you can think of each edge being unit cost)

#    for the above example:

#    longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])      returns (5, [0, 2, 3, 4, 5, 6])
#    longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])      returns (5, [0, 2, 4, 3, 5, 6]) 
#    longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)])        returns (7, [0, 1, 2, 4, 3, 5, 6, 7])  # unique answer

#    Note that longest() takes two arguments, n and list_of_edges, 
#    where n specifies that the nodes are named 0..(n-1).

#    Tie-breaking: arbitrary. any longest path is fine.  

from collections import defaultdict

def longest(n, edges):
    
    def visit(v):
        # If the current vertex has already been visited, return the previously calculated path length
        if v in visited:
            return path_length[v]
        # Mark the current vertex as visited
        visited.add(v)
        # Recursively visit all incoming vertices and update the path length for the current vertex
        for u in incomingE[v]:
            path_length[v] = max(path_length[v], visit(u) + 1)
        return path_length[v]
    
    def solution(v):
        # If the current vertex has already been visited in the solution, return an empty list
        if v in new_visited:
            return []
        new_visited.add(v)
        # Recursively find the solution path by backtracking from the current vertex
        for u in incomingE[v]:
            # Choose the incoming vertex that leads to the next vertex with the maximum path length
            if path_length[v] == path_length[u] + 1:
                return solution(u) + [v]  # Append the current vertex to the solution path
        return [v]  # If no incoming vertex leads to the next vertex with the maximum path length, return the current vertex as the start of the solution path
    
    visited = set()  # Set to keep track of visited vertices during DFS
    incomingE = defaultdict(list)  # Dictionary to store incoming edges for each vertex
    
    # Construct the graph by populating the incoming edges dictionary
    for u, v in edges:
        incomingE[v].append(u)  # Add an incoming edge from vertex u to vertex v
    
    path_length = [0] * n  # List to store the maximum path length for each vertex
    
    # Perform a depth-first search (DFS) to calculate the maximum path length for each vertex
    for vertex in range(n):
        path_length[vertex] = visit(vertex)
    
    new_visited = set()  # Set to keep track of visited vertices during backtracking
    max_root_vertex = path_length.index(max(path_length))  # Find the vertex with the maximum path length
    
    # Return the maximum path length and the solution path starting from the vertex with the maximum path length
    return path_length[max_root_vertex], solution(max_root_vertex)
