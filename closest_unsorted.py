# Given an array A of n numbers, a query x, and a number k,
#    find the k numbers in A that are closest (in value) to x.
#    For example:

#    find([4,1,3,2,7,4], 5.2, 2)	returns   [4,4]
#    find([4,1,3,2,7,4], 6.5, 3)	returns   [4,7,4]
#    find([5,3,4,1,6,3], 3.5, 2)	returns   [3,4]

import sys

def find(arr, query, num):
    # Calculate the differences between each element in the array and the query
    dif_arr = [abs(a - query) for a in arr]
    # Initialize variables to store the lowest difference and its index
    low = sys.maxsize
    low_i = 0

    # Find the index of the lowest difference element
    for i in range(len(dif_arr)):
        if low > dif_arr[i]:
            low = dif_arr[i]
            low_i = i

    # Initialize an array to store the closest elements
    cl_arr = [arr[low_i]]
    # If more than one closest element is required
    if num > 1:
        for i in range(low_i + 1, len(dif_arr)):
            # If the difference is equal to the lowest difference, add the element to cl_arr
            if dif_arr[i] == dif_arr[low_i]:
                while len(cl_arr) < num:
                    cl_arr.append(arr[i])

    return cl_arr
