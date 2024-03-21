import sys

def find(arr, query, num):

    dif_arr = [abs(a - query) for a in arr]
    low = sys.maxsize
    low_i = 0

    # find index of lowest element
    for i in range(len(dif_arr)):
        if low > dif_arr[i]:
            low = dif_arr[i]
            low_i = i

    cl_arr = [arr[low_i]]
    if num > 1:
        for i in range(low_i+1, len(dif_arr)):
            if dif_arr[i] == dif_arr[low_i]:
                while len(cl_arr) < num:
                    cl_arr.append(arr[i])

        # code for finding second nearest element

    return cl_arr


print(find([4,1,3,2,7,4], 5.2, 2))	# should return   [4,4]
print(find([4,1,3,2,7,4], 6.5, 3))  # should return   [4,7,4]
print(find([5,3,4,1,6,3], 3.5, 2))	# should return   [3,4]
