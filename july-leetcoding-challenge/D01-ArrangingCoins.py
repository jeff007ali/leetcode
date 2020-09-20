# output limit exceeded
def arrangeCoins(n):
        
    row = 1
    while n >= row:
        print("n = {} and row = {}".format(n, row))

        n -= row
        row += 1
    
    return row - 1

# Reference : https://leetcode.com/articles/arranging-coins/
# Binary search approach
def arrangeCoins1(n):
    return (int)((2 * n + 0.25)**0.5 - 0.5)


print(arrangeCoins(8))