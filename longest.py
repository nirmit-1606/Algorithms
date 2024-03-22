# Length of the longest path in a binary tree (number of edges)
#   Test cases:

#   longest([[], 1, []])    should return 0
#   longest([[[], 1, []], 2, [[], 3, []]])  should return 2
#   longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]) should return 5

# Global variable to store the length of the longest path
pathLength = 0

# Function to find the length of the longest path in a binary tree
def longest(arr):
    global pathLength
    # Call the function to find the longest path and store its length
    lp = longestPath(arr)
    # Store the length of the longest path before resetting pathLength
    p_l = pathLength - 1
    # Reset pathLength for subsequent calls
    pathLength = 0
    return p_l

# Function to recursively find the longest path in a binary tree
def longestPath(arr):
    
    global pathLength
    
    # Base case: if the input array is empty, return an empty list
    if arr == []:
        return []
    
    # Extract the root node from the array
    root = arr[1]
    
    # Recursively find the longest path in the left subtree
    leftPath = longestPath(arr[0])
    # Recursively find the longest path in the right subtree
    rightPath = longestPath(arr[2])
    
    # Extend the longer path with the root node
    if len(leftPath) >= len(rightPath):
        leftPath.append(root)
    else:
        rightPath.append(root)
        
    # Update the pathLength if the sum of lengths of leftPath and rightPath is greater
    if pathLength < len(leftPath) + len(rightPath):
        pathLength = len(leftPath) + len(rightPath)
        
    # Return the longer path between leftPath and rightPath
    if len(leftPath) > len(rightPath):
        return leftPath
    
    return rightPath
