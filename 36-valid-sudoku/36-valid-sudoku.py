class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            values = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in values:
                        return False
                    values.add(board[i][j])
                    
        for i in range(len(board)):
            values = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in values:
                        return False
                    values.add(board[j][i])
        
        # m = k = 0
        # while m < len(board) - 2:
        #     m 
        for m in range(0, len(board) - 2, 3):
            for k in range(0, len(board) - 2, 3):
                values = set()
                for i in range(m, m + 3):
                    for j in range(k, k + 3):
                        if board[i][j] != ".":
                            if board[i][j] in values:
                                return False
                            values.add(board[i][j])

        return True