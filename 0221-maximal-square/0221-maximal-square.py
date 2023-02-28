class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        dp_table = [[0] * (num_cols+1) for _ in range(num_rows+1)]
        max_square_len = 0

        for i in range(1, num_rows+1):
            for j in range(1, num_cols+1):
                if matrix[i-1][j-1] == '1':
                    dp_table[i][j] = min(dp_table[i][j-1], dp_table[i-1][j], dp_table[i-1][j-1]) + 1
                    max_square_len = max(max_square_len, dp_table[i][j])
        
        return max_square_len * max_square_len
