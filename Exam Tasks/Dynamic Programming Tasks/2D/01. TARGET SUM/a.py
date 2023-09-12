# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target

nums = [1,1,1,1,1]
target = 3

def target_sum(nums, target): 
    n = len(nums)
    dp = {}

    def dfs(i, total):
        if i == n: 
            return 1 if total == target else 0
        
        if (i, total) in dp: 
            return dp[(i, total)] 
        
        dp[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dp[(i, total)]
    
    return dfs(0, 0)


    

print(target_sum(nums, target))