from bisect import bisect

def find(array, query, num):
    
    c = bisect(array, query)  # central element # O(logn) 
    i = max(c - num, 0) # initial index
    l = min(c + num, len(array)) # last index
    
    # if the closest index is 0
    if c == 0:
        return array[i:l]
    
    diff_array = [0] * len(array)
    diff = lambda x: abs(x - query)
    
    #subtract array from query
    for x, y in enumerate(array[i: l]): # x is itr count, y is element # O(k) 
        diff_array[x + i] = diff(y)
    
    #find the indices range
    
    left = c - 1
    right = c
    while num != 0: # O(k) 
        if right != len(array) and diff_array[left] > diff_array[right]:
            right += 1
            num -= 1
        else:
            if left != -1:
                left -= 1
                num -= 1
    
    return array[left + 1 : right]

#print(find([1,2,3,4,4,6,6], 5, 3))
#print(find([1,2,3,4,4,5,6], 4, 5))
