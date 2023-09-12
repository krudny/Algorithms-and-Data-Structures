# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# We create perfect squares in linear time, then we do coin change algorithm. 

n = 13

from math import inf

def perfect_squares(n):
    squares = set()

    i = 1
    while i*i <= n: 
        squares.add(i*i)
        i += 1

    DP = [inf] * (n+1)
    DP[0] = 0

    for i in range(1, n+1): 
        for square in squares: 
            if i - square >= 0: 
                DP[i] = min(DP[i], 1 + DP[i-square])
    return DP[-1]

print(perfect_squares(n))

