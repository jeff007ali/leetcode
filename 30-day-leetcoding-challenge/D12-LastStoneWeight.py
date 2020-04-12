def lastStoneWeight(stones):

    while len(stones) > 1:
        stones = sorted(stones)
        remaining = stones[-1] - stones[-2]
        if remaining != 0:
            stones = stones[:-2] + [remaining]
        else:
            stones = stones[:-2]

    return stones[-1] if stones else 0

print(lastStoneWeight([2,7,4,1,8,1]))