def dfs(x, y, board):
    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "O":
        board[x][y] = "A"
        dfs.(x+1, y, board)
        dfs.(x-1, y, board)
        dfs.(x, y+1, board)
        dfs.(x, y-1, board)
def solve (board):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if (i == 0 or i == row -1 or j == 0 or j == col - 1) and board[i][j] == "O":
                dfs.(i, j, board)
    for i in range(row):
        for j in range(col):
            if board[i][j] == "A":
                board[i][j] = "O"
            else:
                board[i][j] = "X"
input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(input)
print(input)