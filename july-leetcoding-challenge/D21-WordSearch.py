def exist(board, word):

    # Helper function to check whether can find word, start at (i,j) position    
    def dfs(board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        temp = board[i][j] # first character is found, check the remaining part
        board[i][j] = "*" # avoid visit again 

        res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
        board[i][j] = temp

        return res

    if not board:
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    
    return False


print(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED"))
print(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE"))
print(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCB"))