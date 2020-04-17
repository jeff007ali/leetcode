def numIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1':
                grid[i][j]='0'
                islands += 1
                stack=[[i,j]]
                
                while stack:
                    x,y=stack.pop(0)
                    nextVisit=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
                    
                    for m,n in nextVisit:
                        if 0<=m<rows and 0<=n<cols and grid[m][n]=='1':
                            grid[m][n]='0'
                            stack.append([m,n])
                
    return islands

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))