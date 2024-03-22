# Quickselect with Randomized Pivot
#   Test cases:

#   qselect(2, [3, 10, 4, 7, 19])   should return 4
#   qselect(4, [11, 2, 8, 3])   should return 11

import random

# Function to partition the array around a randomly chosen pivot element
def partition(array, left, right): 
    # Choose a random index within the range of left and right pointers
    pivot_i = random.randint(left, right)  
    # Swap the pivot element with the rightmost element
    pivot = array[pivot_i] 
    array[right], array[pivot_i] = array[pivot_i], array[right]
    # Initialize a pointer i to keep track of the position of the smaller elements
    i = left - 1
    # Iterate through the array from left to right-1
    for j in range(left, right): 
        # If the current element is smaller than the pivot, swap it with the element at index i+1
        if array[j] < pivot:
            i += 1 
            array[i], array[j] = array[j], array[i]
    # Swap the pivot element with the element at index i+1, placing the pivot in its correct position
    array[i+1], array[right] = array[right], array[i+1] 
    # Return the index of the pivot element
    return i + 1

# Function to find the nth lowest element using quickselect algorithm
def qselect(n_low, array, left=0, right=0):
    # If right pointer is not provided, set it to the last index of the array
    if right == 0:
        right = len(array)-1
    # Base case: if left and right pointers are equal, return the element at that index
    if left == right:
        return array[left]
    # Partition the array around a pivot and get its index
    p = partition(array, left, right)
    # Calculate the rank of the pivot element
    i = p - left + 1
    # If the rank of the pivot is equal to the desired rank, return the pivot element
    if n_low == i:
        return array[p]
    # If the desired rank is smaller than the rank of the pivot, recurse on the left partition
    if n_low < i:
        return qselect(n_low, array, left, p - 1)
    # If the desired rank is larger than the rank of the pivot, recurse on the right partition
    else:
        return qselect(n_low - i, array, p + 1, right)
