# Math solution
def singleNonDuplicate(nums):
    return 2 * sum(set(nums)) - sum(nums)

# XOR solution
def singleNonDuplicate1(nums):
    ans = 0
    for n in nums:
        ans ^= n
    return ans


print(singleNonDuplicate1([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate1([3,3,7,7,10,11,11]))