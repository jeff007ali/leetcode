def isHappy(n):
    doneWith = list()
    
    while n != 1 and n not in doneWith:
        doneWith.append(n)
        n = sum(int(r) ** 2 for r in str(n))
        print(n)
        print(doneWith)

    return n == 1

def isHappy1(n):
    doneWith = set()
    
    while n != 1 and n not in doneWith:
        doneWith.add(n)
        n = sum(int(r) ** 2 for r in str(n))
        print(n)
        print(doneWith)

    return n == 1



print(isHappy1(19))