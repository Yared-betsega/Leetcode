class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for j in range(len(mat[0]) - 1, -1, -1):
            temp = []
            row, col = 0, j
            while row < len(mat) and col < len(mat[0]):
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row, col = 0, j
            while row < len(mat) and col < len(mat[0]):
                mat[row][col] = temp[row]
                row += 1
                col += 1
        for i in range(1, len(mat)):
            temp = []
            row, col = i, 0
            while row < len(mat) and col < len(mat[0]):
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row, col = i, 0
            while row < len(mat) and col < len(mat[0]):
                mat[row][col] = temp[col]
                row += 1
                col += 1
            
        return mat