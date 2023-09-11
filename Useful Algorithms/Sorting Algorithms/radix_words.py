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

#For char A-Z use count only to 27 and -ord('a')

def counting_sort(A, col):
    n = len(A)
    count = [0] * 256
    output = [0] * n

    for i in range(n):
        if col < len(A[i]): 
            letter = ord(A[i][col]) 
        else:
            letter = 0
        count[letter] += 1

    for i in range(1,256):
        count[i] = count[i] + count[i-1]

    for i in range(n-1, -1, -1):
        if col < len(A[i]):
            letter = ord(A[i][col])
            output[count[letter]-1] = A[i]
            count[letter] -= 1
        else: 
            output[count[0] - 1] = A[i]
            count[0] -= 1

    for i in range(n): 
        A[i] = output[i]

def radix_sort(A): 
    n = len(A)
    max_len = 0

    for word in A:
        max_len = max(max_len, len(word))
    
    for col in range(max_len, -1, -1):
        counting_sort(A, col)

    print(A)




def main():
    radix_sort(A)

main()
