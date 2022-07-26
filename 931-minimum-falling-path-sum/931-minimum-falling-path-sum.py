class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        isValid = lambda x: 0<=x[0]<len(matrix) and 0<=x[1]<len(matrix)
        n = len(matrix) - 1
        memo = {}
        def dp(row, col):
            if not isValid((row, col)):
                return float("inf")
            if row == n:
                return matrix[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            
            left = dp(row + 1, col - 1)
            down = dp(row + 1, col)
            right = dp(row + 1, col + 1)
            
            memo[(row, col)] = matrix[row][col] + min(left, down, right)
            return memo[(row, col)] 
        
        ans = float("inf")
        for i in range(len(matrix)):
            ans = min(ans, dp(0, i))
        
        return ans