# O(n) space, O(n) time
def singleNumber(nums):
    dic, res = {}, []
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for k, v in dic.items():
        if v == 1:
            res.append(k)
    return res

# Bit manipulation, O(1) space, O(n) time
def singleNumber1(nums):
    xor = 0
    a = 0
    b = 0
    for num in nums:
        xor ^= num
    mask = 1
    while(xor&mask == 0):
        mask = mask << 1
    for num in nums:
        if num&mask:
            a ^= num
        else:
            b ^= num
    return [a, b]


print(singleNumber1([1,2,1,3,2,5]))