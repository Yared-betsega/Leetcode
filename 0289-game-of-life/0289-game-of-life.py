class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIR = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        isValid = lambda x: 0 <= x[0] < len(board) and 0 <= x[1] < len(board[0])
        liveCount = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                ones = 0
                for dx, dy in DIR:
                    nx, ny = i + dx, j + dy
                    if isValid((nx, ny)) and board[nx][ny] == 1:
                        ones += 1
                liveCount[(i, j)] = ones
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if liveCount[(i, j)] < 2:
                        board[i][j] = 0
                    elif liveCount[(i, j)] > 3:
                        board[i][j] = 0
                else:
                    if liveCount[(i, j)] == 3:
                        board[i][j] = 1
                        
        
    