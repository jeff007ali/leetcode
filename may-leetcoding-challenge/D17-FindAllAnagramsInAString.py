# Using sort method which is slow. Suppose string p is very big, then in that case it will take 
# more time to sort string
def findAnagrams(s, p):
    p = list(p)
    p.sort()
    p = ''.join(p)
    res = []
    for i in range(len(s) - len(p) + 1):
        substring = s[i: i + len(p)]
        substring = list(substring)
        substring.sort()
        root = ''.join(substring)
        if root == p:
            res.append(i)
        
    return res

# Using hashmap 
def findAnagrams1(s, p):
    ans = []
    if len(s) < len(p):
        return ans

    pDict = {}
    sDict = {}

    for i in range(len(p)):
        if p[i] in pDict:
            pDict[p[i]] += 1
        else:
            pDict[p[i]] = 1

    for i in range(len(p) - 1):
        if s[i] in sDict:
            sDict[s[i]] += 1
        else:
            sDict[s[i]] = 1

    for i in range(len(p) - 1, len(s)):
        # Add new char key if it does not exists
        if s[i] in sDict:
            sDict[s[i]] += 1
        else:
            sDict[s[i]] = 1
        
        # compare both dict
        if pDict == sDict:
            ans.append(i - len(p) + 1)
        
        # After shifting window, remove old char
        sDict[s[i - len(p) + 1]] -= 1
        if sDict[s[i - len(p) + 1]] == 0:
            del sDict[s[i - len(p) + 1]]

    return ans

# Using dict with all alphabets characters
def findAnagrams2(s, p):
    if len(s) < len(p):
        return []

    pDict = [0]*26
    sDict = [0]*26
    res = []

    for i in range(len(p)):
        pDict[ord(p[i])-ord('a')] += 1
        sDict[ord(s[i])-ord('a')] += 1

    if pDict == sDict:
        res.append(0)

    for i in range(1, len(s)-len(p)+1):
        sDict[ord(s[i-1])-ord('a')] -= 1
        sDict[ord(s[i+len(p)-1])-ord('a')] += 1

        if pDict == sDict:
            res.append(i)

    return res

# TODO: read this code
def findAnagrams3(s, p):
    p = "".join(sorted(p))
    l = len(p)
    ls = len(s)
    res = []
    
    i = l -1
    pre = False
    while i < ls:
        if pre and s[i] == s[i-l]:
            res.append(i-l+1)
            i += 1
        elif s[i] in p:
            if p == "".join(sorted(s[i-l+1:i+1])):
                res.append(i-l+1)
                pre = True
            else:
                pre = False
            i += 1
        else:
            i += l
            pre = False
    return res


print(findAnagrams1("cbaebabacd", "abc"))
print(findAnagrams1("abab", "ab"))