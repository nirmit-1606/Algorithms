# Maximum Weighted Independent Set 

#    Independent set is a set where no two numbers are neighbors in the original list.
#    https://en.wikipedia.org/wiki/Independent_set_(graph_theory)

#    input:  a list of numbers (could be negative)
#    output: a pair of the max sum and the list of numbers chosen

#    max_wis([7,8,5])   returns (12, [7,5])
#    max_wis([-1,8,10]) returns (10, [10])
#    max_wis([])        returns (0, [])

#    Note: if all numbers are negative, the optimal solution is 0,
#           since [] is an independent set according to the definition above.

#    max_wis([-5, -1, -4])  returns (0, [])

def max_wis(arr):
    # Base cases for an empty or singleton list
    if len(arr) < 2:
        # If the list has one element and it's positive, it's the only element in the set
        if len(arr) > 0 and arr[0] > 0:
            return arr[0], arr 
        else: 
            # Otherwise, the set is empty
            return 0, []
    
    # Initialize dynamic programming table with tuples of (max_sum, include_current, prev_index)
    dp = [(None, False, float('inf'))] * len(arr)
    
    # Initialize values for the first two elements in the table
    dp[0] = (arr[0], True, -1) if arr[0] > 0 else (0, False, -1)
    dp[1] = (arr[1], True, -1) if arr[1] > arr[0] and arr[1] > 0 else (max(0, arr[0]), False, 0)
    
    # Function to fill the dynamic programming table
    def fill_dp(idx):
        # If the value at current index hasn't been computed yet
        if dp[idx][0] == None:
            # Recursively compute the maximum sum either by including or excluding the current element
            max1 = fill_dp(idx - 1)[0]  # Maximum sum excluding the current element
            max2 = fill_dp(idx - 2)[0] + arr[idx]  # Maximum sum including the current element
            
            # Choose the maximum sum and update the include_current and prev_index flags accordingly
            if max1 >= max2:
                dp[idx] = (max1, False, idx - 1)
            else:
                dp[idx] = (max2, True, idx - 2)
                
        return dp[idx]
    
    # Fill the dynamic programming table starting from the last index
    fill_dp(len(arr) - 1)
    
    # Retrieve the elements in the maximum weighted independent set
    max_set = []
    idx = len(arr) - 1
    while idx > -1:
        if dp[idx][1]:  # If the current element is included in the set
            max_set.append(arr[idx])
        idx = dp[idx][2]  # Move to the previous index based on the prev_index flag
    
    # Return the maximum sum and the list of numbers chosen for the maximum weighted independent set
    return dp[len(arr) - 1][0], max_set[::-1]  # Reverse max_set to maintain the original order
