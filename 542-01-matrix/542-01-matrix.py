class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        is_valid = lambda x: 0<=x[0] < len(mat) and 0<=x[1] < len(mat[0])
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        def bfs():
            visited = set()
            while queue:
                (r, c), tot = queue.popleft()
                ans[r][c] = min(ans[r][c], tot)
                for dx, dy in DIR:
                    row, col = (r + dx, c + dy)
                    if is_valid((row, col)):
                        ans[r][c] = min(ans[r][c], ans[row][col] + 1)
                        ans[row][col] = min(ans[row][col], ans[r][c] + 1)
                        if (row, col) not in visited:
                            if mat[row][col] == 0:
                                queue.append([(row, col), 0])
                            else:
                                queue.append([(row, col), ans[row][col]])
                            visited.add((row, col))
        
        ans = [[float("inf") for i in range(len(mat[0]))] for j in range(len(mat))]
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append(((i, j), 0))
        bfs()
        return ans
        
            