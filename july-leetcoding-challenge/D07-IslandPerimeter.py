def islandPerimeter(grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])
    ans = 0

    def countEdges(i, j):
        neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        res = 0
        for x, y in neighbours:
            if x < 0 or x == row or y < 0 or y == col or grid[x][y] == 0:
                res += 1
        return res

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                ans += countEdges(i, j)
    
    return ans

def islandPerimeter1(grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])
    ans = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                ans += 4

                if i > 0 and grid[i-1][j] == 1:
                    ans -= 2
                if j > 0 and grid[i][j-1] == 1:
                    ans -= 2
    return ans


print(islandPerimeter1([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))