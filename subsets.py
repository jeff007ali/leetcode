def subsets(nums):

    # def recurr(nums, ans, i):
    #     if i == len(nums):
    #         result = [i for i in ans if i is not None]
    #         print(ans)
    #         final_ans.append(result)
    #     else:
    #         ans[i] = None
    #         recurr(nums, ans, i + 1)
    #         ans[i] = nums[i]
    #         recurr(nums, ans, i + 1)
    #
    # final_ans = []
    # ans = [None] * len(nums)
    # recurr(nums, ans, 0)
    #
    # print(final_ans)

    result = [[]]
    if not nums:
        return result

    for num in nums:
        print(result)
        result += [curr + [num] for curr in result]

    print(result)


subsets([1, 2])
print([[] + [1]])

