import heapq

def ksmallest(k, data_stream):
    
    heap_data = list(data_stream[:k])
    
    for i in range(k, len(data_stream)):
        if heap_data[0] > data_stream[i]:
            heap_data[0] = data_stream[i]
            heapq._heapify_max(heap_data)
    
    heap_data.sort()
    return heap_data

# ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]) should return [2, 3, 5, 7]
# ksmallest(3, range(1000000, 0, -1)) should return [1, 2, 3]