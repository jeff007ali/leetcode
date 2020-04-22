# Time limit exceeded
def subarraySum(nums, k):
    count = 0
    l= len(nums)
    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += nums[j]
            if sum == k:
                count += 1

    return count

def subarraySum1(nums, k):
    sums = {0:1} # prefix sum array
    res = s = 0
    for n in nums:
        s += n # increment current sum
        res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
        sums[s] = sums.get(s, 0) + 1 # add current sum to sum count
    return res

print(subarraySum1([1,1,1], 2))