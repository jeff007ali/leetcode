# for reference - https://www.youtube.com/watch?v=-q5tHoWhPK0
def maxUncrossedLines(A, B):
    la = len(A)
    lb = len(B)

    dp = [[0] * (lb + 1) for _ in range(la + 1)]

    for i in range(la):
        for j in range(lb):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


print(maxUncrossedLines([1,4,2], [1,2,4]))
print(maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
print(maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))