class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.DIR = [[-1,0], [1,0], [0,1], [0,-1]]
        def isValid(tup):
            return True if 0 <= tup[0] < len(board) and 0 <= tup[1] < len(board[0]) else False
        
        def dfs(cord):
            if isValid(cord) and cord not in self.visited:
                if board[cord[0]][cord[1]] == "O":
                    self.visited.add(cord)
                    for tup in self.DIR:
                        neighbor = (cord[0]+tup[0], cord[1]+tup[1])
                        if isValid(neighbor):
                            dfs(neighbor)
            
        self.visited = set()
        for i in range(len(board)):
            if i == 0 or i == len(board) - 1:
                for j in range(len(board[0])):
                    if board[i][j] == "O":
                        dfs((i, j))
            else:
                if board[i][0] == "O":
                        dfs((i, 0))
                    
                if board[i][len(board[0])-1] == "O":
                    dfs((i, len(board[0])-1))
                    
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O" and (i,j) not in self.visited:
                    board[i][j] = "X"
        return board

# time space complexity
# time complexity = O(m*n)
# space  complexity = O(n)
