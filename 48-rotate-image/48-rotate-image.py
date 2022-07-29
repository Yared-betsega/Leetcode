class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                pos[(i, j)] = matrix[i][j]
        for i in range(len(matrix)):
            r = 0
            for j in range(len(matrix) - 1, -1, -1):
                matrix[i][r] = pos[(j, i)]
                r += 1