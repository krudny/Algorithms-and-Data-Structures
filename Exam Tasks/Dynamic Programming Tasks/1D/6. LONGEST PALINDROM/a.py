s = "alakkala"

def longest_palindrom(s): 
    n = len(s)
    max_len = 0
    max_str = ""

    for i in range(n): 
        #ODD LENGTH

        left, right = i, i
        curr_len = 1

        while left >= 0 and right < n and s[left] == s[right]: 
            if curr_len > max_len: 
                max_len = curr_len
                max_str = s[left : right + 1]
            left -= 1
            right += 1
            curr_len += 2

        #EVEN LENGTH
        left, right = i, i+1
        curr_len = 1

        while left >= 0 and right < n and s[left] == s[right]: 
            if curr_len > max_len: 
                max_len = curr_len
                max_str = s[left : right + 1]
            left -= 1
            right += 1
            curr_len += 2

    return max_str
            


print(longest_palindrom(s))