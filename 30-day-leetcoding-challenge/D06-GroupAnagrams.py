def groupAnagrams(strs):
    sortedList = [''.join(sorted(s)) for s in strs]
                            
    ans = {}
    for og,s in zip(strs, sortedList):
        if s in ans:
            ans[s] += [og]
        else:
            ans[s] = [og]
    
    return ans.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))