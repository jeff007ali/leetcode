def minPathSum(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    temp = [float('inf')] * rows
    temp[0] = 0
    for j in range(cols):
        for i in range(rows):
            if i == 0:
                temp[0] += grid[0][j]
            else:
                temp[i] = min(temp[i], temp[i-1]) + grid[i][j]
                
    return temp[-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))