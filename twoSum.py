def twoSum(nums, target):
    temp = {}
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp[target - nums[i]] = i
        else:
            return [temp[nums[i]], i]


print(twoSum([2, 7, 11, 15], 9))
            