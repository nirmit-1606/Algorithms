from collections import defaultdict

def longest(n, edges):
    
    def visit(v):
        if v in visited:
            return path_length[v]
        visited.add(v)
        for u in incomingE[v]:
            path_length[v] = max(path_length[v], visit(u) + 1)
        return path_length[v]
    
    def solution(v):
        if v in new_visited:
            return []
        new_visited.add(v)
        for u in incomingE[v]:
            if path_length[v] == path_length[u] + 1:
                return solution(u) + [v]
        return [v]
    
    visited = set()
    incomingE = defaultdict(list)
    #outgoingE = defaultdict(list)
    
    for u, v in edges:
        incomingE[v].append(u)
        #outgoingE[u].append(v)
    
    path_length = [0] * n
    
    for vertex in range(n):
        path_length[vertex] = visit(vertex)
    
    new_visited = set()
    max_root_vertex = path_length.index(max(path_length))
    
    return path_length[max_root_vertex], solution(max_root_vertex)