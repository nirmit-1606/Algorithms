def best(W, items):
    best = [[-1] * (W + 1) for _ in range(len(items) + 1)]
    back = [[0] * (W + 1) for _ in range(len(items) + 1)]
    
    best[0] = [0] * (W + 1)
    for i in range(len(best)):
        best[i][0] = 0
        #print(best[i])
        
    def find_best(i, w):
        #print(i, w)
        
        if best[i][w] != -1:
            return best[i][w]
        
        #print(items[i - 1][2])
        for k in range(items[i - 1][2] + 1):
            if w >= k * items[i - 1][0]:
                best_val = find_best(i - 1, w - k * items[i - 1][0]) + k * items[i - 1][1]
                if best[i][w] < best_val:
                    best[i][w] = best_val
                    back[i][w] = k
        return best[i][w]
    
    #x = find_best(len(items), W)
    #print(best)
    #print(back)
    
    def solution(i, w):
        if i <= 0:
            return []
        return solution(i - 1, w - items[i - 1][0] * back[i][w]) + [back[i][w]]
    
    return find_best(len(items), W), solution(len(items), W)
