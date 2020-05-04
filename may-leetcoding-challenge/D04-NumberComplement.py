def findComplement(num):
    binary = format(num, 'b')
    
    flip = ''.join([str((int(c) ^ 1)) for c in binary])
    
    return int(flip, 2)

# On line solution
def findComplement1(num):
    return int(''.join([str((int(c) ^ 1)) for c in bin(num)[2::]]), 2)


print(findComplement1(5))
print(findComplement1(1))