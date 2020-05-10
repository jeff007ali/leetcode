def findJudge(N, trust):
    judgeRating = [0] * (N + 1)

    for i, j in trust:
        judgeRating[i] -= 1
        judgeRating[j] += 1

    for i in range(1, N + 1):
        if judgeRating[i] == N - 1:
            return i

    return -1


print(findJudge(2, [[1,2]])) # 2
print(findJudge(3, [[1,3],[2,3]])) # 3
print(findJudge(3, [[1,3],[2,3],[3,1]])) # -1
print(findJudge(3, [[1,2],[2,3]])) # 3
print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3