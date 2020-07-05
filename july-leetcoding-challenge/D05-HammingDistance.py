def hammingDistance(x, y):
    return bin(x ^ y).count("1")

def hammingDistance1(x, y):
    x = x ^ y
    y = 0
    while x:
        print("x={} and y={}".format(x, y))
        y += 1
        x = x & (x - 1)
    return y


print(hammingDistance1(1, 4))