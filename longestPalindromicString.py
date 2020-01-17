# try 1
# TODO : need to fix for some testcases 
def longestPalindrome1(s):
    l = len(s)
    # print("len of str : " + str(l))
    maxPali = ""

    if s and len(s) <= 2:
        return s[0]

    for i in range(1, l - 1):
        if((len(maxPali) / 2) > (l - i - 1)):
            break
        # print("i : " + str(i))
        # print("maxPali : " + maxPali)
        j = 1
        temp = s[i]
        while i + j < l and s[i - j] == s[i + j]:
            temp = s[i - j] + temp + s[i + j]
            j = j + 1
            # print("temp : " + temp)

        if len(maxPali) <= 1:
            # print("max is zero")
            if s[i] == s[i-1]:
                temp = s[i] + s[i-1]
            elif s[i] == s[i+1]:
                temp = s[i] + s[i+1]

        if len(temp) > len(maxPali):
            # print("Max apli swap")
            maxPali = temp




    # print("Final Answer : " + maxPali)

    return maxPali

# try 2
def longestPalindrome2(s):
    longPali = ""
        
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(longPali) < j-i and s[i:j] == s[i:j][::-1]:
                longPali = s[i:j]
                break
    return longPali

# try 3
def longestPalindrome3(s):
    strlen = len(s)
    # if length of string < 2 or s is palindrome already
    if strlen < 2 or s == s[::-1]:
        return s
    start, maxlen = 0, 1
    for i in range(strlen):
        oddstart  = i - maxlen - 1
        evenstart = i - maxlen
        odd  = s[oddstart:i+1]  # len(odd)  = maxlen + 2
        even = s[evenstart:i+1] # len(even) = maxlen + 1
        print(i)
        print("odd : {}".format(odd))
        print("even : {}".format(even))
            #i = 2
            #maxlen = 1
            #start = 0
            #odd = s[2-1-1:3]….bab
            #even = s[1:3]…ab
        if oddstart >= 0 and odd == odd[::-1]:
            start = oddstart
            maxlen += 2
        elif evenstart >= 0 and even == even[::-1]:
            start = evenstart
            maxlen += 1
    return s[start:start+maxlen]

print(longestPalindrome3("babad"))
