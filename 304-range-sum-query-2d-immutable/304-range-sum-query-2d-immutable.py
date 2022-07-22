class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = [ [0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            self.prefixSum[i][0] = matrix[i][0]
            for j in range(1, len(matrix[i])):
                self.prefixSum[i][j] = self.prefixSum[i][j-1] + matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            total += self.prefixSum[i][col2] - self.prefixSum[i][col1]
            total += self.matrix[i][col1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)