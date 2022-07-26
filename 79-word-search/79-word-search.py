class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        isValid = lambda x: 0 <= x[0] < len(board) and 0 <= x[1] < len(board[0])
        
        def dfs(r, c, i, path):
            
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            if board[r][c] != word[i]:
                return False
            
            path.add((r, c))
            for dx, dy in DIR:
                nx, ny = r + dx, c + dy
                if isValid((nx, ny)) and (nx, ny) not in path:
                    if dfs(nx, ny, i + 1, path):
                        return True
            path.remove((r, c))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False