# Given a sorted array A of n numbers, a query x, and a number k,
#    find the k numbers in A that are closest (in value) to x.
#    For example:

#    find([1,2,3,4,4,7], 5.2, 2) returns   [4,4]
#    find([1,2,3,4,4,7], 6.5, 3) returns   [4,4,7]

from bisect import bisect

# Function to find the k numbers in a sorted array closest to a query number
def find(array, query, num):
    
    # Find the index of the central element using binary search
    c = bisect(array, query)    # O(logn)
    # Set the initial and last indices for the search window
    i = max(c - num, 0)
    l = min(c + num, len(array))
    
    # If the closest index is 0, return the elements from the start of the array
    if c == 0:
        return array[i:l]
    
    # Initialize an array to store the differences between elements and the query
    diff_array = [0] * len(array)
    # Define a function to calculate the absolute difference between a number and the query
    diff = lambda x: abs(x - query)
    
    # Calculate the differences and store them in diff_array
    for x, y in enumerate(array[i: l]):     # x is itr count, y is element # O(k)
        diff_array[x + i] = diff(y)
    
    # Initialize pointers for left and right indices
    left = c - 1
    right = c
    # Iterate until num becomes 0
    while num != 0:     # O(k)
        # If right pointer is within array bounds and the difference to the right is smaller, move right
        if right != len(array) and diff_array[left] > diff_array[right]:
            right += 1
            num -= 1
        else:
            # If left pointer is within array bounds, move left
            if left != -1:
                left -= 1
                num -= 1
    
    # Return the k numbers closest to the query
    return array[left + 1: right]
