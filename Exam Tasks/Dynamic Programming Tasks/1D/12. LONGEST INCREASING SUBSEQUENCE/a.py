#Given an integer array nums, return the length of the longest strictly increasing subsequence

nums = [0,1,0,3,2,3,5,1,2]

def LIS(A): 
    n = len(A)
    DP = [1] * n
    P = [-1] * n

    for i in range(1, n):
        for j in range(i-1, -1, -1): 
            if A[i] > A[j]: 
                if DP[j] + 1 > DP[i]: 
                    DP[i] = DP[j] + 1
                    P[i] = j
    print([0,1,2,3,4,5,6,7,8,9])
    print(nums)
    print(P)
                
    
    return DP[-1]

print(LIS(nums))