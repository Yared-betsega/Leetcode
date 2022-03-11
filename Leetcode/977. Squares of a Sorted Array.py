# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = deque()
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[left] ** 2 >= nums[right]**2:
                answer.appendleft(nums[left]**2)
                left += 1
                
            else:
                answer.appendleft(nums[right]**2)
                right -= 1
        
        return answer

# time and space complexity
# time complexity = O(n)
# space complexity = O(1)
        
