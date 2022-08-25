class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetIndex  = self.findTargetList(matrix, target)
        if targetIndex == None:
            return False
        targetList = matrix[targetIndex]
        
        left, right = 0, len(targetList)
        while left <= right:
            mid = (left + right) // 2
            if targetList[mid] == target:
                return True
            elif targetList[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
    def findTargetList(self, matrix, target):
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            selected = matrix[mid]
            if selected[0] <= target and selected[-1] >= target:
                return mid
            elif selected[0] < target:
                left = mid + 1
            else:
                right = mid - 1