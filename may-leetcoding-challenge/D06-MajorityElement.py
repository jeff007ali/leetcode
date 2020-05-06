# Hashmap
def majorityElement(nums):
    threshold = len(nums) // 2

    cache = {}
    for n in nums:
        if n in cache:
            cache[n] += 1
        else:
            cache[n] = 1

    for n in cache:
        if cache[n] > threshold:
            return n

# Brute force - Time limit exceeded
def majorityElement1(nums):
    threshold = len(nums) // 2

    for n in nums:
        if nums.count(n) > threshold:
            return n

# Sorting method
def majorityElement2(nums):
    threshold = len(nums) // 2
    
    nums.sort()
    return nums[threshold]

    


print(majorityElement2([3,2,3]))
print(majorityElement2([2,2,1,1,1,2,2]))