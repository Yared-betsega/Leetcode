class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        DIR = [(1,0), (-1,0), (0,1),(0,-1)]
        queue = deque([entrance])
        visited = [[False for i in range(n)] for j in range(m)]
        visited[entrance[0]][entrance[1]] = True
        level = 0
        isValid = lambda r, c: 0 <= r < m and 0 <= c < n
        while queue:
            for _ in range(len(queue)):
                
                row, col = queue.popleft()
                
                if level > 0 and (row == m - 1 or row == 0 or col == 0 or col == n - 1):
                    return level
                
                for dx, dy in DIR:
                    nx, ny = row + dx, col + dy
                    if isValid(nx, ny) and not visited[nx][ny]:
                        if maze[nx][ny] == ".":
                            queue.append([nx, ny])
                            visited[nx][ny] = True
            
            level += 1
        
        return -1
            