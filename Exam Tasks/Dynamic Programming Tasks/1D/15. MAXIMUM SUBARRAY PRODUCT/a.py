#Given an integer array nums, find a subarray that has the largest product, and return the product.

nums = [2,3,-2,4]

def max_product(nums):
    n = len(nums)
    res = max(nums)

    currMax, currMin = 1, 1

    for num in nums: 
        if num == 0: 
            currMax, currMin = 1, 1
            continue
        
        tmp = currMax * n
        currMax = max(num * currMax, num * currMin, num)
        currMin = min(tmp, num * currMin, num)

        res = max(res, currMax)
    return res

print(max_product(nums))