class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.DIR = [[-1,0], [1,0], [0,1], [0,-1]]
        
        def isValid(tup):
            return True if 0 <= tup[0] < len(grid) and 0 <= tup[1] < len(grid[0]) else False
        
        def dfs(cord):
            if isValid(cord) and cord not in self.visited:
                if grid[cord[0]][cord[1]] == 1:
                    self.visited.add(cord)
                    for tup in self.DIR:
                        neighbor = (cord[0]+tup[0], cord[1]+tup[1])
                        if isValid(neighbor):
                            dfs(neighbor)
            
        self.visited = set()
        for i in range(len(grid)):
            if i == 0 or i == len(grid) - 1:
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs((i, j))
            else:
                if grid[i][0] == 1:
                        dfs((i, 0))
                    
                if grid[i][len(grid[0])-1] == 1:
                    dfs((i, len(grid[0])-1))
                    
        total = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1 and (i,j) not in self.visited:
                    total += 1
        return total

# time space complexity
# time complexity = O(m*n)
# space  complexity = O(n)
                    
        
