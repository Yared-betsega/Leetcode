# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        isValid = lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[0])
        
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = defaultdict(int)
        def dfs(node):
            if node in visited:
                return visited[node]
            
            ans = 0
            for coord in DIR:
                n = (node[0] + coord[0], node[1] + coord[1])
                if isValid(n) and matrix[n[0]][n[1]] > matrix[node[0]][node[1]]:
                    ans = max(ans, dfs(n))
            visited[node] = 1 + ans 
            return visited[node]  
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in visited:
                    ans = max(ans, visited[(i, j)])
                else:
                    ans = max(ans, dfs((i, j)))
        return ans
                    
                    
