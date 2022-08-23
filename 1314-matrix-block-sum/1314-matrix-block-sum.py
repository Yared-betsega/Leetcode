class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pre = [[0] * (len(mat[0]) + 1) for i in range(len(mat) + 1)]
        isValid = lambda x: 0 <= x[0] < len(mat) and 0 <= x[1] < len(mat[0])
        for i in range(1, len(pre)):
            for j in range(1, len(pre[0])):
                pre[i][j] = mat[i-1][j-1]
                pre[i][j] += pre[i - 1][j] 
                pre[i][j] += pre[i][j - 1] 
                pre[i][j] -= pre[i - 1][j - 1] 
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                l, r = min(len(pre) - 1, i + k), min(len(pre[0]) - 1, j + k)
                li, lj = max(i - k - 1, 0), max(0, j - k - 1)
                ans[i-1][j-1] = pre[l][r] - pre[li][r] - pre[l][lj] + pre[li][lj]
        return ans
               