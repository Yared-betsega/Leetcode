class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def isValid(tup):
            if tup not in self.visited:
                if 0 <= tup[0] and tup[0] < len(grid) and 0 <= tup[1] and tup[1] < len(grid[0]):
                    return True
            return  False
            
        def dfs(cord):
            self.visited.add(cord)
            neighbors = [(cord[0]+1, cord[1]), (cord[0]-1, cord[1]), (cord[0], cord[1]+1), (cord[0], cord[1]-1)]
            self.area += 1
            for tup in neighbors:
                if isValid(tup) and grid[tup[0]][tup[1]] == 1:
                    dfs((tup[0], tup[1]))
            
        self.visited = set()
        maxim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in self.visited and grid[i][j] == 1:
                    self.area = 0
                    dfs((i, j))
                    if self.area > maxim:
                        maxim = self.area

        return maxim
