# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_level, right_level = 0, 0
        answer = 0
        while left < right:
            if height[left] <= height[right]:
                left_level = max(left_level, height[left])
                answer += left_level - height[left]
                left += 1
            else:
                right_level = max(right_level, height[right])
                answer += right_level - height[right]
                right -= 1
        
        return answer
    
# time and space complexity 
# time complexity = O(n)
# space complexity = O(1)
