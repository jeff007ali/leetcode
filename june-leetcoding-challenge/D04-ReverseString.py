# Python Zindabaad
def reverseString(s):
    s.reverse()
    print(s)

# Using recursion
def reverseString1(s):
    def recurr(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            recurr(left + 1, right - 1)

    recurr(0, len(s) - 1)
    print(s)

# Using 2 pointers
def reverseString2(s):
    left =  0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    print(s)


reverseString2(["h","e","l","l","o"])
reverseString2(["H","a","n","n","a","h"])
