def productExceptSelf(nums):
    l = len(nums)

    left, right, ans = [0] * l, [0] * l, [0] * l

    left[0] = 1
    for i in range(1, l):
        left[i] = left[i - 1] * nums[i - 1]
    
    right[-1] = 1
    for i in reversed(range(l - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(l):
        ans[i] = left[i] * right[i]

    return ans


def productExceptSelf1(nums):
    l = len(nums)

    ans = [0] * l

    ans[0] = 1
    for i in range(1, l):
        ans[i] = ans[i - 1] * nums[i - 1]
    
    right = 1
    for i in reversed(range(l)):
        ans[i] *= right
        right *= nums[i]

    return ans


print(productExceptSelf1([1,2,3,4]))