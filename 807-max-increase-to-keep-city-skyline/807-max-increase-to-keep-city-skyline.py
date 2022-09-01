class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        _maxOfRow = defaultdict(int)
        _maxOfCol = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                _maxOfRow[i] = max(_maxOfRow[i], grid[i][j])
                _maxOfCol[j] = max(_maxOfCol[j], grid[i][j])
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(_maxOfRow[i], _maxOfCol[j])) - grid[i][j]
        return ans