def longestPalindrome(s):
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

print(longestPalindrome("sasfgsrtf"))
