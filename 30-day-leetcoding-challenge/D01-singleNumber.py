def singleNumber(nums):
    temp = []
    for n in nums:
        if n not in temp:
            temp.append(n)
        else:
            temp.remove(n)
    return temp[0]

# Math
# 2∗(a+b+c)−(a+a+b+b+c)=c
def singleNumber1(nums):
    return 2 * sum(set(nums)) - sum(nums)

# XOR
def singleNumber2(nums):
    ans = 0
    for n in nums:
        ans ^= n
    return ans
    

print(singleNumber2([4, 2, 1, 2, 1]))