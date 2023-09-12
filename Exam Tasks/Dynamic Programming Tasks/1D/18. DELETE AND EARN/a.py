# You are given an integer array nums. You want to maximize the number of points you get by performing 
# the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. 
# Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

# Return the maximum number of points you can earn by applying the above operation some number of times.

# We use house robber solution, and we check if adjencant number is 1 less. If so, we take max of (i-1, i-2 + curr). If no, we add i-1 + curr

nums = [2,2,3,3,3,4]


def delete(nums): 
    n = len(nums)
    CNT = {}
    A = []

    for num in nums: 
        if num not in CNT: 
            CNT[num] = 1
        else: 
            CNT[num] += 1

    for key in CNT:
        A.append(key)
    A.sort()

    DP = [0] * len(A)
    DP[0] = A[0] * CNT[A[0]]

    for i in range(1, len(A)):
        if A[i] - 1 == A[i-1]: 
            DP[i] = max(DP[i-1], DP[i-2] + A[i] * CNT[A[i]])
        else: 
            DP[i] = DP[i-1] + A[i] * CNT[A[i]]

    return DP[-1]

print(delete(nums))