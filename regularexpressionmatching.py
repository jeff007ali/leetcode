def isMatch(s, p):
    if not p:
        return not s

    if '*' not in p and len(s) != len(p):
        return False

    if p == ".*":
        return True

    flag = False
    rp = ""
    while p:
        if s:
            print("inside S => pat : {} and str : {}".format(p, s))
            if p[0] in [s[0], '.']:
                flag = False
                if p[1:2] == "*":
                    s = s[1:]
                else:
                    s = s[1:]
                    p = p[1:]
            else:
                if p[1:2] == '*' and not flag:
                    p = p[2:]
                    flag = True
                else:
                    print("S > here")
                    return False
        else:
            print("inside P => pat : {} and str : {}".format(p, s))
            if not rp:
                rp = p
            print("RP : {}".format(rp))
            if not p[1:2] == "*":
                if p[0] == ".":
                    return False
                elif p[0] + "*" in rp:
                    p = p[1:]
                else:
                    print("p > here")
                    return False
            else:
                p = p[2:]

    if s:
        return False

    # pflag = ""
    # while p:
    #     print("Inside P")
    #     print("pat : {}".format(p))
    #     if not p[1:2] == "*" and not p[0] == pflag:
    #         return False
    #     else:ans
    #         pflag = p[0]
    #         p = p[2:]

    return True

def isMatchUsingDp(text, pattern):
    memo = {}

    def dp(i, j):
        print("i : {} and j : {}".format(i, j))
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
                print("Here")
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[i, j] = ans
            print(memo)
        else:
            print("use memo : i : {} and j : {}".format(i, j))
        return memo[i, j]

    print("len of text : {} and length of pattern : {}".format(len(text), len(pattern)))
    return dp(0, 0)

# print(isMatch("aaa", "a*a"))
# print(isMatch("aaa", "ab*a*c*a"))
# print(isMatch("mississippi", "mis*is*ip*."))
# print(isMatch("aa", "a*"))
# print(isMatch("abcd", "d*"))
# print(isMatch("a", "ab*a"))
# print(isMatch("a", ".*..a*"))
# print(isMatch("ab", ".*.."))

print(isMatchUsingDp("abcd", "d*"))
