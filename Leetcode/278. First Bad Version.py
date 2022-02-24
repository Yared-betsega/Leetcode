# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            ver = isBadVersion(mid)
            if ver:
                if left == right:
                    return mid
                right = mid - 1
            else:
                if left == right:
                    right = mid + 1
                left = mid + 1
                
        return mid
      
# space time complexity
# time complexity = O(log(n))
# space complexity = O(1)
            
