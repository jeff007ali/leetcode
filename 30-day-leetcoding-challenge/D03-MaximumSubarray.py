def maxSubArray(nums):
    ans = nums[0]
    temp = nums[0]
    
    for i in range(1, len(nums)):
        temp = max(nums[i], temp + nums[i])
        ans = max(ans, temp)
        
    return ans

def maxSubArray1(nums):
    max_sum = nums[0]
    current_sum = 0
    
    for num in nums:
        current_sum += num
        if (num > current_sum):
            current_sum = num       # this starts the new subarray
        if (current_sum > max_sum):
            max_sum = current_sum
            
    return max_sum

print(maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))