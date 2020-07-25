def findMin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        middle = low + (high - low) // 2
        print("{}-{}-{}".format(low, middle, high))
        if nums[middle] > nums[high]:
            low = middle + 1
        else:
            high = middle - 1 if nums[high] != nums[middle] else high - 1

    return nums[low]


print(findMin([1,3,5]))
print(findMin([2,2,2,0,1]))