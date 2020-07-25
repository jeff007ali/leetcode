def findMin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        middle = low + (high - low) // 2
        print("{}-{}-{}".format(low, middle, high))
        if nums[middle] > nums[high]:
            low = middle + 1
        else:
            high = middle - 1

    return nums[low]


print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))