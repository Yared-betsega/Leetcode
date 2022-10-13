# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         left, right = min(nums), max(nums)
        
#         while left < right:
#             mid = (left + right) // 2
#             sides = self.count(nums, mid, left, right)
#             if sides[0] > sides[1]:
#                 right = mid
#             else:
#                 left = mid + 1
      
#         return right
    
#     def count(self, nums, mid, left, right):
#         leftSide = rightSide = 0
#         for num in nums:
#             if num >= left and num <= right:
#                 if num <= mid:
#                     leftSide += 1
#                 else:
#                     rightSide += 1
                
#         return leftSide, rightSide

# # time and space complexity
# # time complexity = O(mlog(n))
# # n = max(nums) - min(nums)
# # m = len(nums)
# # space complexity = O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = self.count(nums, mid)
            if count > mid:
                right = mid
            else:
                left = mid + 1
      
        return right
    
    def count(self, nums, mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
                
        return count

# time and space complexity
# time complexity = O(mlog(n))
# n = max(nums) - min(nums)
# m = len(nums)
# space complexity = O(1)