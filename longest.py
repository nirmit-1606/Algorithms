pathLength = 0

def longest(arr):
    global pathLength
    lp = longestPath(arr)
    #arr.append(5)
    #print(lp)
    p_l = pathLength - 1
    pathLength = 0
    return p_l

def longestPath(arr):
    
    global pathLength
    
    if arr == []:
        return []
    
    root = arr[1]
    #print(root)
        
    leftPath = longestPath(arr[0])
    rightPath = longestPath(arr[2])
    
    if len(leftPath) >= len(rightPath):
        leftPath.append(root)
    else:
        rightPath.append(root)
        
    if pathLength < len(leftPath) + len(rightPath):
        pathLength = len(leftPath) + len(rightPath)
        
    if len(leftPath) > len(rightPath):
        return leftPath
    
    return rightPath

#longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])

#longest([[[], 1, []], 2, [[], 3, []]])

longest([[], 1,[]])

#longest([[[[[],5,[[],2,[[[],9,[]],1,[]]]], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])

#longest([[[[[],1,[]],2,[[[],4,[]],5,[]]],6,[[],8,[[],9,[]]]],10,[[[],11,[]],12,[[],15,[]]]])
