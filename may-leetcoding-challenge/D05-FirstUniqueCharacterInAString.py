def firstUniqChar(s):
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
        
    return -1

def firstUniqChar1(s):
    cache = {}

    for c in s:
        if c in cache:
            cache[c] += 1
        else:
            cache[c] = 1
    
    # print(cache)

    for i, c in enumerate(s):
        if cache[c] == 1:
            return i

    return -1

    
import string
def firstUniqChar2(s):
    fc = len(s)
    for c in string.ascii_lowercase:
        left = s.find(c)
        if left != -1 and left == s.rfind(c):
            fc = min(left, fc)
    return fc if fc != len(s) else -1


print(firstUniqChar1("leetcode"))
print(firstUniqChar1("loveleetcode"))