def maxSlidingWindow(nums, k):
    ans = []
    queue = []
    
    for i,v in enumerate(nums):
        
        if queue and queue[0] <= i - k:
            queue = queue[1:]

        while queue and nums[queue[-1]] < v:
            queue.pop()
        
        queue.append(i)

        if i + 1 >= k:
            ans.append(nums[queue[0]])

    return ans

# fast method
def maxSlidingWindow1(nums, k):
    if k == 1:
        return nums
    
    l = len(nums)
    kmax = max(nums[:k])
    ans = [kmax]

    for i in range(k, l):
        if kmax <= nums[i]:
            kmax = nums[i]
        elif nums[i-k] == kmax:
            kmax = max(nums[i-k+1:i+1])
        ans.append(kmax)

    return ans 

print(maxSlidingWindow1([1,3,-1,-3,5,3,6,7], 3))