def singleNumber(nums):
    dic = {}
    
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
        
    for k,v in dic.items():
        if v == 1:
            return k


def singleNumber1(nums):
    return (3*sum(set(nums)) - sum(nums))//2


def singleNumber2(nums):
    one = two = 0
    for num in nums:
        print("num: {}".format(num))
        print("before: one - two: {} - {}".format(one, two))
        one = ~two&(one^num)
        two = ~one&(two^num)
        print("after: one - two: {} - {}".format(one, two))
    return one


print(singleNumber2([2,2,3,2]))
# print(singleNumber2([0,1,0,1,0,1,99]))