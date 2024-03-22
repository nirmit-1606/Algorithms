# Find the k smallest numbers in a data stream of length n (k<<n),
#    using only O(k) space (the stream itself might be too big to fit in memory).

#    ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])    should return [2, 3, 5, 7]
#    ksmallest(3, range(1000000, 0, -1))    should return [1, 2, 3]

#    Note: 
#    a) it should work with both lists and lazy lists
#    b) the output list should be sorted

import heapq

def ksmallest(k, data_stream):
    # Initialize a heap with the first k elements from the data stream
    heap_data = list(data_stream[:k])
    
    # Convert the list into a max heap
    heapq._heapify_max(heap_data)
    
    # Iterate over the remaining elements in the data stream
    for i in range(k, len(data_stream)):
        # If the current element is smaller than the maximum element in the heap
        if heap_data[0] > data_stream[i]:
            # Replace the maximum element in the heap with the current element
            heap_data[0] = data_stream[i]
            # Rearrange the heap to maintain the max heap property
            heapq._heapify_max(heap_data)
    
    # Sort the heap to get the k smallest elements in sorted order
    heap_data.sort()
    return heap_data

# Test cases
print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))  # should return [2, 3, 5, 7]
print(ksmallest(3, range(1000000, 0, -1)))         # should return [1, 2, 3]
