def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    m = min(strs)
    for i in range(len(m)):
        for s in strs:
            if s[i] != m[i]:
                return m[:i]
            
    return m


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))