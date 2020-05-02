def numJewelsInStones(J, S):
    c = 0
    
    for i in S:
        if i in J:
            c += 1
        
    return c

def numJewelsInStones1(J, S):
    c = 0
        
    for i in J:
        c += S.count(i)
        
    return c

print(numJewelsInStones1("aA", "aAAbbbb"))
