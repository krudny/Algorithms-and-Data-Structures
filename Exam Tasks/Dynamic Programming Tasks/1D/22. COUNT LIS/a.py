# Given an integer array nums, return the number of longest increasing subsequences.

nums = [1,3,5,4,7]

def count_lis(nums):   
    n = len(nums)

    dp = {}

    lenLis, res = 0,0


    for i in range(n-1, -1, -1): 
        maxLen, maxCnt = 1,1

        for j in range(i+1, n):
            if nums[j] > nums[i]: 
                length, count = dp[j]
                if length + 1 > maxLen: 
                    maxLen, maxCnt = length + 1, count
                elif length + 1 == maxLen: 
                    maxCnt += count

        if maxLen > lenLis:
            lenLis, res = maxLen, maxCnt
        elif maxLen == lenLis: 
            res += maxCnt

        dp[i] = [maxLen, maxCnt]
 
    return res

print(count_lis(nums))