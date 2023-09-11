#najdłuższy spójny palindom
s = "kamilalavzxc"

def longest_palindrom(s):
    n = len(s)
    max_length = 0
    
    for i in range(n):
        left = i-1
        right = i+1
        curr_length = 1
        
        while left > -1 and right < n and s[left] == s[right]: 
            curr_length += 2
            max_length = max(max_length,curr_length)
            left -= 1
            right += 1

        left = i
        right = i+1
        curr_length = 0
        
        while left > -1 and right < n and s[left] == s[right]: 
            curr_length += 2
            max_length = max(max_length,curr_length)
            left -= 1
            right += 1
    
    print(max_length)


def main():
    longest_palindrom(s)

main()