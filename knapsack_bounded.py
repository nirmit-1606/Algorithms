# Bounded Knapsack

#    You have n items, each with weight w_i and value v_i, and has c_i copies.
#    **All numbers are positive integers.**
#    Find the best value for a bag of W

#    best(3, [(2, 4, 2), (3, 5, 3)])  returns (5, [0, 1])

#    the input to the best() function is W and a list of triples (w_i, v_i, c_i).

#    tie-breaking:

#    best(3, [(1, 5, 2), (1, 5, 3)])  returns (15, [2, 1])
#    best(3, [(1, 5, 1), (1, 5, 3)])  returns (15, [1, 2])
#    best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])   returns (130, [6, 4, 1])
#    best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])  returns (236, [6, 7, 3, 7, 2])

def best(W, items):
    # Initialize a 2D list to store the best value for each item and weight combination
    best = [[-1] * (W + 1) for _ in range(len(items) + 1)]
    # Initialize a 2D list to store the number of copies of each item chosen for each weight
    back = [[0] * (W + 1) for _ in range(len(items) + 1)]
    
    # Base case: when the weight is 0, the best value is also 0 for any item
    best[0] = [0] * (W + 1)
    for i in range(len(best)):
        best[i][0] = 0
        
    # Recursive function to find the best value for a given item and weight
    def find_best(i, w):
        # If the best value for the current item and weight combination has already been computed, return it
        if best[i][w] != -1:
            return best[i][w]
        
        # Iterate through the possible number of copies of the current item
        for k in range(items[i - 1][2] + 1):
            # Check if the weight allows including k copies of the current item
            if w >= k * items[i - 1][0]:
                # Calculate the value of including k copies of the current item and update the best value if it's greater
                best_val = find_best(i - 1, w - k * items[i - 1][0]) + k * items[i - 1][1]
                if best[i][w] < best_val:
                    best[i][w] = best_val
                    # Store the number of copies of the current item chosen for the current weight
                    back[i][w] = k
        return best[i][w]
    
    # Find the best value for the given knapsack capacity W
    res = find_best(len(items), W)
    
    # Recursive function to trace back and determine the number of copies of each item chosen
    def solution(i, w):
        if i <= 0:
            return []
        # Recursively determine the solution by subtracting the weight of the chosen item copies
        return solution(i - 1, w - items[i - 1][0] * back[i][w]) + [back[i][w]]
    
    # Return the best value and the list of copies of each item chosen
    return res, solution(len(items), W)
