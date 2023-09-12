# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Solution: we run house robber algorithm twice, without first and last element
nums = [1,3,4,5,6,1,2,1]

def robber(nums): 
    n = len(nums)
    DP = [0] * n
    DP[0] = nums[0]
    DP[1] = min(nums[0], nums[1])

    for i in range(2, n): 
        DP[i] = max(DP[i-2] + nums[i], DP[i-1])
    return max(DP[-1], DP[-2])

def main(): 
    print(max(robber(nums[0:len(nums)-1]), robber(nums[1:len(nums)])))

main()