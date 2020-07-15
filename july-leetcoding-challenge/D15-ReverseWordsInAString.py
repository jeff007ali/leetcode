def reverseWords(s):
    words = s.split()
    rev=''
    
    for w in words[::-1]:
            rev+=w+' '
    
    return rev.rstrip()


print(reverseWords("the sky is blue"))
print(reverseWords("  hello world!  "))
print(reverseWords("a good   example"))