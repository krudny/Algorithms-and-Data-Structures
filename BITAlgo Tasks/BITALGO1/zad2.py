'''Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tablicę w czasie 
O(n). Można założyć, że stringi składają się wyłącznie z małych liter afabetu łacińskiego.'''
'''Najpierw sortujemy po dlugosci stringi, a potem radixem po kolumnach'''

A = ['pyktlcdkzjcusqyaclq',
 'ujqmpochdfaihlkklc',
 'biihzwgkjomdpmoln',
 '',
 'armjytweokmrotgfg',
 'efmoga',
 'hwohp',
 'nauzmwkboolwhjsnxgxapw',
 'hszjqurnnspzruvpeoaixcgx',
 'jakiyfgopbnjoaezkonfy',
 'aavwhzjqjbbtp',
 'oxwrblgghliplhc',
 'imdkumdcdhtzmdfy',
 'qdgtxvtwf',
 'anhdozn',
 '',
 'sgkzoqovwdxswatnpot',
 'a',
 'aaa',
 'aaaaaa']


def counting_sort_by_length(A, max_len):
    n = len(A)
    count = [0] * max_len
    output = [0] * n

    for i in range(n):
        length = len(A[i])
        count[length] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    
    for i in range(n-1, -1, -1):
        count[len(A[i])] -= 1
        output[count[len(A[i])]] = A[i]

    return output

def counting_sort(A, col_idx):
    n = len(A)
    output = [None] * n
    count = [0] * 26
    a_code = ord('a')

    i = len(A)-1
    while col_idx < len(A[i]) and i >= 0:
        count[ord(A[i][col_idx]) - a_code] += 1
        i -= 1
    prev_to_last_idx = i

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(A)-1, prev_to_last_idx, -1):
        letter_idx = ord(A[i][col_idx]) - a_code
        output[prev_to_last_idx + count[letter_idx]] = A[i]
        count[letter_idx] -= 1

    for i in range(prev_to_last_idx + 1, len(output)):
        A[i] = output[i]

def radix_sort(A):
    max_len = len(max(A, key = len))
    
    A = counting_sort_by_length(A, max_len + 1)
    
    for col_idx in range(max_len-1, -1, -1):
        counting_sort(A, col_idx)
    
    for row in A:
        print(row)

   
def main():
    radix_sort(A)

 

main()