def countSquares(matrix):
    # TODO: go through code once
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
    return sum(map(sum, matrix))


print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(countSquares([[1,0,1],[1,1,0],[1,1,0]]))
