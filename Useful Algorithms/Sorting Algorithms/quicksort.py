#quicksort
A = [2, 5, 6, 1, 2, 9, 12, 234, 123, 3, 5, 6, 3, 44, 3]

T = ['pyktlcdkzjcusqyaclq',
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


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p = q+1


def partition(T, p, r):
    if p >= r:
        return p
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


print(T)
quicksort(T, 0, len(T)-1)
print(T)

