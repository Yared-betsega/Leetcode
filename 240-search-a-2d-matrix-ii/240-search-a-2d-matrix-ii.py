class Solution:
    def search(self, subMatrix, target):
        left, right = 0, len(subMatrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if subMatrix[mid] == target:
                return True
            elif subMatrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            found = self.search(mat, target)
            if found:
                return True
        return False
    
# time and space complexity
# time complexity = O(mlog(n))
# space complexity = O(1)