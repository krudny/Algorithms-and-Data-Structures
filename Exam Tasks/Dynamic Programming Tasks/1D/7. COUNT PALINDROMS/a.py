s = "aaab"

def count_palindroms(s): 
    n = len(s)
    cnt = 0
    
    for i in range(n): 
        #odd length
        left, right = i, i

        while left >= 0 and right < n and s[left] == s[right]: 
            cnt += 1
            left -= 1
            right += 1


        #even length
        left, right = i, i+1

        while left >= 0 and right < n and s[left] == s[right]: 
            cnt += 1
            left -= 1
            right += 1    
    
    return cnt
        


print(count_palindroms(s))