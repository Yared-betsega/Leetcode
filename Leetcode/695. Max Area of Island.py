class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Union Find Solution
        def find_set(i):
            if i == parent[i]:
                return i
            parent[i] = find_set(parent[i])
            return parent[i]
        
        def union_sets(i, j):
            a = find_set(i)
            b = find_set(j)
            if a!=b:
                if size[a] >= size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]
        
        parent, size = {}, {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    parent[(i, j)] = (i, j)
                    size[(i, j)] = 1 
                else:
                    size[(i, j)] = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        union_sets((i, j), (i-1, j))
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        union_sets((i, j), (i, j+1))
             
        return max(size.values())
        
        
        # DFS Solution
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
