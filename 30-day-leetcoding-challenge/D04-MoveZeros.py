def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    numberOfNonZeroDigit = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            # nums = nums[:i] + nums[i+1:] + [nums[i]]
            nums[numberOfNonZeroDigit], nums[i] = nums[i], nums[numberOfNonZeroDigit]
            numberOfNonZeroDigit += 1
    
    print(nums)

moveZeroes([0,1,0,3,12])