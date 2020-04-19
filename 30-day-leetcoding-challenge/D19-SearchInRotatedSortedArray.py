// Brute force
def search0(nums, target):
    l = len(nums)
    for i in range(l):
        if nums[i] == target:
            return i
        
    return -1


// Optimized method
def search(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle

        elif nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        else:
            if nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    
    return -1


print(search([4,5,6,7,0,1,2], 0))