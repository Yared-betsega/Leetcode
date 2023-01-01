class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.block = 0
        self.DIR = [[0,1], [0,-1], [1,0], [-1, 0]]
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    self.block += 1
                elif grid[i][j] == 1:
                    self.start = (i, j)
        isValid = lambda x: 0<=x[0]<len(grid) and 0<=x[1]<len(grid[0])
        
        def dfs(cord, cr):
            cr += 1
            self.visited.add(cord)
            if grid[cord[0]][cord[1]] == 2 and cr == len(grid)*len(grid[0]) - self.block:
                self.ans+= 1
            for i in self.DIR:
                neighbor = (cord[0]+i[0], cord[1]+i[1])
                if isValid(neighbor) and grid[neighbor[0]][neighbor[1]]!= -1 and neighbor not in self.visited:
                    dfs(neighbor, cr)

            self.visited.remove(cord)
                
                
        self.ans = 0
        dfs(self.start, 0)
        return self.ans