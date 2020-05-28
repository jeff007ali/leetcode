def countBits(num):
    res = [0]
    while len(res) <= num:
        res += [i+1 for i in res]
    return res[:num+1]

def countBits1(num):
    res=[0]
    for i in range(1, num+1):
        res.append(res[i>>1] + int(i&1)) # here >>1 means //2 and &1 means %2
    return res

print(countBits(2))
print(countBits(5))
print(countBits(15))