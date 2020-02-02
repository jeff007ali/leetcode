def breakPalindrome(palindrome):
    palindrome = list(palindrome)
    l = len(palindrome)
    if l == 1:
        return ""
    
    for i in range(l):
        j = l - 1 - i
        if i == j:
            continue
        
        if palindrome[i] != 'a':
            palindrome[i] = 'a'
            return "".join(palindrome)
        
    palindrome[l - 1] = 'b'
    return "".join(palindrome)

def breakPalindrome_fast(palindrome):
    palindrome = list(palindrome)
    l = len(palindrome)
    if l == 1:
        return ""
    
    for i in range(l // 2):
        if palindrome[i] != 'a':
            palindrome[i] = 'a'
            return "".join(palindrome)
        
    palindrome[l - 1] = 'b'
    return "".join(palindrome)


print(breakPalindrome_fast('abccba'))