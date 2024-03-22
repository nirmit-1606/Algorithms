# Unbounded Knapsack

#    Given n items, each with weight w_i and value v_i, and each has infinite copies.
#    **All numbers are positive integers.**
#    Find the best value for a bag of W

#    best(3, [(2, 4), (3, 5)])      returns (5, [0, 1])

#    the input to the best() function is W and a list of pairs (w_i, v_i).
#    this output means to take 0 copies of item 1 and 1 copy of item 2.

#    tie-breaking: *reverse* lexicographical: i.e., [1, 0] is better than [0, 1]:
#    (i.e., take as many copies from the first item as possible, etc.)

#    best(3, [(1, 5), (1, 5)])    returns (15, [3, 0])
#    best(3, [(1, 2), (1, 5)])    returns (15, [0, 3])
#    best(3, [(1, 2), (2, 5)])    returns (7, [1, 1])
#    best(58, [(5, 9), (9, 18), (6, 12)])           returns (114, [2, 4, 2])
#    best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])  returns (109, [1, 1, 7, 1])

def best(W, items):
    # Initialize lists to store the best value for each weight and the index of the last item chosen for each weight
    best = [0] * (W + 1)
    back = [-1] * (W + 1)
    
    # Recursive function to find the best value for a given weight
    def find_best(w):
        # Iterate through each item
        for j in range(len(items)):
            # Check if the weight of the current item is less than or equal to the remaining weight w
            if w >= items[j][0]:
                # Calculate the value of including the current item and update the best value if it's greater
                best_wi = find_best(w - items[j][0]) + items[j][1]
                if best_wi > best[w]:
                    best[w] = best_wi
                    back[w] = j
        return best[w]
        
    # Find the best value for the given knapsack capacity W
    res = find_best(W)
    
    # Initialize a list to store the number of copies of each item chosen
    copies = [0] * len(items)
    x = W
    
    # Trace back to determine the number of copies of each item chosen
    while x > 0:
        copies[back[x]] += 1
        x -= items[back[x]][0]
    
    # Return the best value and the list of copies of each item chosen
    return res, copies
