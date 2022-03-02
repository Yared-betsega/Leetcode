class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        self.DIR = [[-1,0], [1,0], [0,1], [0,-1],[-1,-1], [1,1], [1,-1],[-1,1]]
        
        def isValid(tup):
            return True if 0 <= tup[0] < len(board) and 0 <= tup[1] < len(board[0]) else False
        
        def dfs(cord):
            if isValid(cord):
                if board[cord[0]][cord[1]] == "M":
                    board[cord[0]][cord[1]] = "X"

                elif board[cord[0]][cord[1]] == "E":
                    cnt = 0
                    for tup in self.DIR:
                        neighbor = (cord[0] + tup[0], cord[1] + tup[1])
                        if isValid(neighbor) and (board[neighbor[0]][neighbor[1]] == "M":
                            cnt += 1
                    if cnt == 0:
                        board[cord[0]][cord[1]] = "B"
                        for tup in self.DIR:
                            neighbor = (cord[0]+tup[0], cord[1]+tup[1])
                            dfs(neighbor)
                    else:
                        board[cord[0]][cord[1]] = str(cnt)
                            
        self.visited = set()
        
        dfs((click[0], click[1]))
        
        return board

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
                        
                        
                         
                        
    
