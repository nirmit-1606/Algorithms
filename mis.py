def max_wis(arr):
    print(arr)
    
    if len(arr) < 2:
        if len(arr) > 0 and arr[0] > 0:
            return arr[0], arr 
        else: 
            return 0, []
    
    dp = [(None, False, float('inf'))] * len(arr)
    
    dp[0] = (arr[0], True, -1) if arr[0] > 0 else (0, False, -1)
    dp[1] = (arr[1], True, -1) if arr[1] > arr[0] and arr[1] > 0 else (max(0, arr[0]), False, 0)
    
    def fill_dp(idx):
        if dp[idx][0] == None:
            max1 = fill_dp(idx - 1)[0]
            max2 = fill_dp(idx - 2)[0] + arr[idx]
            if max1 >= max2:
                dp[idx] = (max1, False, idx - 1)
            else:
                dp[idx] = (max2, True, idx - 2)
                
        return dp[idx]
    
    fill_dp(len(arr) - 1)
    
    max_set = []
    
    idx = len(arr) - 1
    while idx > -1:
        if dp[idx][1]:
            max_set.append(arr[idx])
        idx = dp[idx][2]
    
    #print(dp)
    
    return dp[len(arr)-1][0], max_set[::-1]
