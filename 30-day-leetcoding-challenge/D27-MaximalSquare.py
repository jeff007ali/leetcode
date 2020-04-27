def maximalSquare(matrix):
    if not matrix:
        return 0
    
    m = len(matrix)
    n = len(matrix[0])
    
    dp = [[0] * (n+1) for _ in range(m+1)]
    ans = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[i+1][j+1] = min(min(dp[i+1][j], dp[i][j+1]), dp[i][j]) + 1
                ans = max(ans, dp[i+1][j+1])
    return ans * ans


print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))