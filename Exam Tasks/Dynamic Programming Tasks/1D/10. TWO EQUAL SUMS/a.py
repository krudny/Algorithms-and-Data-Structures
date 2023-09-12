#Given an integer array nums, return true if you can partition the array into two subsets such that 
#the sum of the elements in both subsets is equal or false otherwise.

nums = [1,5,11,5]

def sum(nums): 
    n = len(nums)
    possible_sums = set()
    possible_sums.add(0)

    target = 0
    for i in range(n): 
        target += nums[i]
    
    target /= 2

    for i in range(n): 
        temp_set = set()
        for sum in possible_sums: 
            temp_set.add(sum+nums[i])
            temp_set.add(sum)
        possible_sums = temp_set

    return True if target in possible_sums else False

print(sum(nums))