class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordCt = Counter(word)
        boardCt = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardCt[board[i][j]] += 1
        
        for w in word:
            if boardCt[w] < wordCt[w]:
                return False
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        isValid = lambda x: 0 <= x[0] < len(board) and 0 <= x[1] < len(board[0])
        
        def dfs(r, c, i):
            
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            if board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = -1
            for dx, dy in DIR:
                nx, ny = r + dx, c + dy
                if isValid((nx, ny)):
                    if dfs(nx, ny, i + 1):
                        return True
            board[r][c] = temp
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False