class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = (left + right) // 2
            sides = self.count(nums, mid, left, right)
            if sides[0] > sides[1]:
                right = mid
            else:
                left = mid + 1
      
        return right
    
    def count(self, nums, mid, left, right):
        leftSide = rightSide = 0
        for num in nums:
            if num >= left and num <= right:
                if num <= mid:
                    leftSide += 1
                else:
                    rightSide += 1
                
        return leftSide, rightSide

# time and space complexity
# time complexity = O(mlog(n))
# n = max(nums) - min(nums)
# m = len(nums)
# space complexity = O(1)
        
