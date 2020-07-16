def myPow(x, n):
    return x**n

def myPow1(x, n):
    return pow(x, n)

# Recursion
def myPow2(x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / myPow2(x, -n)
    if n % 2:
        return x * myPow2(x, n-1)
    return myPow2(x*x, n/2)

# Iterative
def myPow3(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow


print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))






