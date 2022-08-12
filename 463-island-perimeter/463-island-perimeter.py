class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        is_valid = lambda x: 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0]) 
        visited = set()
        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if not is_valid((row, col)) or grid[row][col] == 0:
                return 1
            count = 0
            visited.add((row, col))
            for r, c in DIR:
                newRow, newCol = row + r, col + c
                count += dfs(newRow, newCol)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
                    