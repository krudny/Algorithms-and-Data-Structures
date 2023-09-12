# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

nums = [2,7,9,3,1]

def robber(nums): 
    n = len(nums)
    DP = [0] * n
    DP[0] = nums[0]
    DP[1] = min(nums[0], nums[1])

    for i in range(2, n): 
        DP[i] = max(DP[i-2] + nums[i], DP[i-1])
        
    return max(DP[-1], DP[-2])

print(robber(nums))