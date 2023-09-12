# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.

# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
# Return the maximum number of connecting lines we can draw in this way.

nums1 = [10,5,2,1,5,3]
nums2 = [10,5,2,1,5,2]

def uncrossed(nums1, nums2): 
    n = len(nums1)
    m = len(nums2)

    DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n): 
        for j in range(m): 
            if nums1[i] == nums2[j]:
                DP[i + 1][j + 1] = 1 + DP[i][j]
            else: 
                DP[i + 1][j + 1] = max(DP[i][j + 1], DP[i + 1][j])

    for row in DP: 
        print(row)
    return DP[n][m]


print(uncrossed(nums1, nums2))