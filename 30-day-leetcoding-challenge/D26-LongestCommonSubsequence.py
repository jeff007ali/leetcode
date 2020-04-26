def longestCommonSubsequence(text1, text2):
    l1 = len(text1)
    l2 = len(text2)

    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1):
        for j in range(l2):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]
    

print(longestCommonSubsequence("abcde", "ace"))
# print(longestCommonSubsequence("abc", "abc"))
# print(longestCommonSubsequence("abc", "def"))