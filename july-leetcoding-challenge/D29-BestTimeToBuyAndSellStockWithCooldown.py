def maxProfit(prices):
    free = 0
    have = cool = float('-inf')
    print("{} : {} : {}".format(free, have, cool))

    for price in prices:
        print("Price: {}".format(price))
        free, have, cool = max(free, cool), max(have, free - price), have + price
        print("{} : {} : {}".format(free, have, cool))

    return max(free, cool)


print(maxProfit([1,2,3,0,2]))