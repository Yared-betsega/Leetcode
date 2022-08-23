class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        isValid = lambda x: 0 <= x[0] < len(matrix) and 0 <= x[1] < len(matrix[0])
        for i in range(1, len(self.pre)):
            for j in range(1, len(self.pre[0])):
                self.pre[i][j] = matrix[i-1][j-1]
                self.pre[i][j] += self.pre[i - 1][j] 
                self.pre[i][j] += self.pre[i][j - 1] 
                self.pre[i][j] -= self.pre[i - 1][j - 1] 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        l, r = row2+1, col2+1
        li, lj = max(row1, 0), max(0, col1)
        return self.pre[l][r] - self.pre[li][r] - self.pre[l][lj] + self.pre[li][lj]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)