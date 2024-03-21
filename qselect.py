import random

def partition(array, left, right): 
    pivot_i = random.randint(left, right)  
    pivot = array[pivot_i] 
    array[right], array[pivot_i] = array[pivot_i], array[right]
    i = left - 1
    for j in range(left, right): 
        if array[j] < pivot:
            i += 1 
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1] 
    return i + 1


def qselect(n_low, array, left=0, right=0):
    if right == 0:
        right = len(array)-1
    if left == right:
        return array[left]
    p = partition(array, left, right)
    i = p - left + 1
    if n_low == i:
        return array[p]
    if n_low < i:
        return qselect(n_low, array, left, p - 1)
    else:
        return qselect(n_low - i, array, p + 1, right)
