class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        isValid = lambda r ,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def dfs(row, col, total):
            visited.add((row, col))
            total += grid[row][col]
            gone = 0
            for dx, dy in DIR:
                nx, ny = row + dx, col + dy
                if isValid(nx, ny) and grid[nx][ny] > 0 and (nx, ny) not in visited:
                    gone += 1
                    dfs(nx, ny, total)
            if gone == 0:
                answer[0] = max(answer[0], total)
            visited.remove((row, col))
            
        total = 0
        for row in grid:
            total += sum(row)
        DIR = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        n, m = len(grid), len(grid[0])
        answer = [0]
        for row in range(n):
            for col in range(m):
                if grid[row][col] > 0:
                    visited = set()
                    dfs(row, col, 0)
                    if answer[0] == total:
                        return total
        return answer[0]