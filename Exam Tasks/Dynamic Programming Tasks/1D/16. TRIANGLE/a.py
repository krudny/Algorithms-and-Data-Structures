# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, 
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

#Bottom up solution, from n-2 row we build minimum sum path

triangle = [[2],
            [3,4],
            [6,5,7],
            [4,1,8,3]]

def min_path(triangle): 
    n = len(triangle)

    for i in range(n-2, -1, -1): 
        for j in range(len(triangle[i])):
            triangle[i][j] = min(triangle[i][j] + triangle[i+1][j], triangle[i][j] + triangle[i+1][j+1])

    return triangle[0][0]

print(min_path(triangle))