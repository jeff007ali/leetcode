# Stepwise explanation with different methods : https://leetcode.com/articles/jump-game/

def canJump(nums):
    lastValidPos = len(nums) - 1
        
    for i in range(len(nums) - 1, -1, -1):
        print(i)
        if (i + nums[i] >= lastValidPos):
            lastValidPos = i
        
    return lastValidPos == 0

print(canJump([2,3,1,1,4]))