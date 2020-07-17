# Using heapq 
import heapq
from collections import Counter
def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    count = Counter(nums)

    return heapq.nlargest(k, count.keys(), key=count.get)

# Using counter and sorted
def topKFrequent1(nums, k):
    # count = Counter(nums)
    count={}
    for n in nums:
        count[n]=count.get(n,0)+1
    sort = sorted(count, key=lambda k:count[k], reverse=True)
    return sort[:k]


print(topKFrequent1([1,1,1,2,2,3], 2))
