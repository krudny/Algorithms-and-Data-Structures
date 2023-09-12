# Given an array of distinct integers nums and a integer target, 
# return the number of possible combinations that add up to target.

# Bottom up approach, we count how many ways we can make i target

nums = [1,2,3]
target = 4

def comb(nums, target):
    n = len(nums)
    DP = [0] * (target + 1)
    DP[0] = 1

    for i in range(1, target + 1): 
        for num in nums: 
            DP[i] += DP[i - num]
        
    return DP[-1]


print(comb(nums, target))