def frequencySort(s):
    freqDict = {}

    for c in s:
        if c in freqDict:
            freqDict[c] += 1
        else:
            freqDict[c] = 1
    
    ans = ""
    for t in sorted(freqDict.items(), key=lambda x: x[1], reverse=True):
        # print(t)
        ans += t[0] * t[1]

    return ans


print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))