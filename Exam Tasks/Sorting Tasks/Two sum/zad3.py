'''Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy'''

T = [-12, -10, -10, -8, -6, -3, -2, -1, 0, 0, 1, 3, 6, 8, 9]
H = [3,4,12,4,5,6]

def sum(T, x, i): 
    n = len(T)
    left = 0
    right = n-1
    
    while left < right: 
        if T[left] + T[right] == x and left != i and right != i: return True
        elif T[left] + T[right] == x:
            if right == i: right -= 1
            if left == i: left += 1
        elif T[left] + T[right] < x: 
            left += 1
        elif T[left] + T[right] > x: 
            right -= 1
        
    return False

        
def find(T): 
    n = len(T)
    T.sort()

    for i in range(n): 
        if not sum(T, T[i], i): return False

    return True

def main(): 
    print(find(T))

main()