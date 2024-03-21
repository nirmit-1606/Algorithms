def best(W, items):
    best = [0] * (W + 1)
    back = [-1] * (W + 1)
    
    def find_best(w):
        for j in range(len(items)):
            if w >= items[j][0]:
                best_wi = find_best(w - items[j][0]) + items[j][1]
                #best[w] = max(best[w], find_best(w - items[j][0]) + items[j][1])
                if best_wi > best[w]:
                    best[w] = best_wi
                    back[w] = j
                #print(best[w])
        return best[w]
        
    res = find_best(W)
    #print(back)
    
    copies = [0] * len(items)
    x = W
    while x > 0:
        copies[back[x]] += 1
        x -= items[back[x]][0]
    
    return res, copies

print(best(3, [(1, 5), (1, 5)]))    # (15, [3, 0])

print(best(3, [(1, 2), (1, 5)]))    # (15, [0, 3])

print(best(3, [(1, 2), (2, 5)]))    # (7, [1, 1])

print(best(58, [(5, 9), (9, 18), (6, 12)])) # (114, [2, 4, 2])

print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))    # (109, [1, 1, 7, 1])