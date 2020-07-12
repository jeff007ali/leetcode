def subsets(nums):

    result = [[]]
    if not nums:
        return result

    for num in nums:
        result += [curr + [num] for curr in result]
        print(result)

    return result


print(subsets([1, 2]))

