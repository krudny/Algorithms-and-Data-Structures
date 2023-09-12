#Count the nth fibonacci number in O(n) time complexity

def fib(n): 
    if n == 0: return 0 

    a, b, c = 1, 1, 1

    for i in range(2, n): 
        c = a + b
        a, b = b, c

    return c


print(fib(19))