class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.DIR = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def isValid(tup):
            return True if 0<=tup[0]<len(grid) and 0<=tup[1]<len(grid[0]) else False
        
# Breadth First Search Solution
        def bfs(cord):
            visited = set()
            per = 0
            queue = deque([cord])
            visited.add(cord)
            
            while queue:
                cur = queue.popleft()
                cr = 0
                for i in self.DIR:
                    neighbor = (cur[0]+i[0], cur[1]+i[1])
                    if isValid(neighbor) and grid[neighbor[0]][neighbor[1]] == 1:
                        cr+=1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                per += (4-cr)
            
            return per
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs((i,j))
              
# Depth First Search Solution
        def dfs(cord):
            if isValid(cord):
                self.visited.add(cord)
            
                for i in self.DIR:
                    neighbor = (cord[0]+i[0], cord[1]+i[1])
                    if isValid(neighbor) and grid[neighbor[0]][neighbor[1]] == 1:
                        if neighbor not in self.visited:
                            dfs(neighbor)
                    else:
                        self.per += 1            
            
        self.per = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs((i,j))
                    return self.per
                  
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
