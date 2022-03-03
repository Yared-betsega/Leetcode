class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(tup):
            return True if tup not in visited and(0<=tup[0]<len(grid) and 0<=tup[1]<len(grid[0]))  else False
        
        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        self.counter = 0
        
        def bfs(cord):
            
            queue = deque()
            for i in cord:
                queue.append(i)
                visited.add(i)
            
            while queue:
                for i in range(len(queue)):
                    cord = queue.popleft()                        
                    for direction in DIR:
                        neighbor = (cord[0] + direction[0], cord[1]+direction[1])
                        if isValid(neighbor) and grid[neighbor[0]][neighbor[1]] == 1:
                            grid[neighbor[0]][neighbor[1]] = 2
                            queue.append(neighbor)
                            visited.add(neighbor)
                if queue:
                    self.counter += 1
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        bfs(rotten)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return self.counter

# time and space complexity 
# time complexity = O(n**2)
# space complexity = O(n)
        
