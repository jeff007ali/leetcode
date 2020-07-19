def addBinary(a, b):
    print(int(a, 2))
    print(int(b, 2))

    return bin(int(a, 2) + int(b, 2))[2:]


# What we need to do in this problem is just add two numbers given in binary representation. 
# How we can do it? Using usual schoolbook сolumnar addition of course! 
# So, we need to start from the last column and add two digits and also not to forget about carry. 
# We need to stop when we reached beginning of both numbers. 
# d1 and d2 are current processed digits. 
# We form summ string, adding element to the end and in the end we reverse it.

# Complexity: 
# time complexity is O(n + m), where n and m are lengths of numbers, 
# space complexity is O(max(m,n)), because result will have this length.
def addBinary1(a, b):
    i, j, summ, carry = len(a) - 1, len(b) - 1, "", 0
    while i >= 0 or j >= 0 or carry:
        d1 = int(a[i]) if i >= 0 else 0
        d2 = int(b[j]) if j >= 0 else 0
        summ += str((d1 + d2 + carry) % 2)
        carry = (d1 + d2 + carry) // 2
        i, j = i-1, j-1 
    return summ[::-1]


print(addBinary1("11", "1"))
# print(addBinary("1010", "1011"))
