def maxSubarraySumCircular(A):
    if not A:
        return 0

    currentMax = A[0]
    bestMax = A[0]

    currentMin = A[0]
    bestMin = A[0]

    totalSum = A[0]

    for n in A[1:]:
        currentMax = max(n, currentMax + n)
        bestMax = max(bestMax, currentMax)

        currentMin = min(n, currentMin + n)
        bestMin = min(bestMin, currentMin)

        totalSum += n

    if totalSum == bestMin:
        return bestMax
    else:
        return max(bestMax, totalSum - bestMin)
    


print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([5,-3,5]))
print(maxSubarraySumCircular([3,-1,2,-1]))
print(maxSubarraySumCircular([3,-2,2,-3]))
print(maxSubarraySumCircular([-2,-3,-1]))


# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/633106/Python-O(n)-by-Kadane-algorithm-80%2B-w-Visualization