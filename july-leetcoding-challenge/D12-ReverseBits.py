def reverseBits(n):
    ans = 0

    for _ in range(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    
    return ans

def reverseBits1(n):
    string = '{0:032b}'.format(n)
    reverseString = string[::-1]
    return int(reverseString, 2)


print(reverseBits1(0b00000010100101000001111010011100))