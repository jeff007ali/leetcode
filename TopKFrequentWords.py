def topKFrequent(words, k):
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    
    # -count[k] will reverse the order
    sort = sorted(count, key=lambda k: (-count[k], k))
    
    return sort[:k]


# this method is not giving answer in alphabatical order
def topKFrequent1(words, k):
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    
    sort = sorted(count, key=lambda k:count[k], reverse=True)
    
    return sort[:k]


print(topKFrequent1(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(topKFrequent1(["i", "love", "leetcode", "i", "love", "coding"], 3))