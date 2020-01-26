def threeSum(nums):
    ans = []
    if not nums:
        return ans
    
    lgh = len(nums)
    if lgh < 3:
        return ans
    
    nums.sort()
    
    for i in range(lgh - 2):
        if nums[i] > 0:
            break
        if i != 0 and nums[i] == nums[i - 1]:
            continue
            
        l, r = i + 1, lgh - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            
            if s == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and r < lgh - 1 and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return ans


print(threeSum([-1, 0, 1, 2, -1, -4]))