class Solution:
    def helper(self, mid, row, column, k):
        counter = 0
        for i in range(1, row+1):
            counter += min(mid//i, column)
        return counter
        
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        row, column, left, right = min(m,n), max(m,n), 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            place = self.helper(mid, row, column, k)
            if place < k:
                left = mid + 1
            else:
                right = mid
                
        return right
    
# time and space complexity 
# time complexity = O(mlog(mn))
# space complexity = O(1)
                
            
        
