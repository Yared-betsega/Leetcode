class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin = 0
        end = len(height)-1
        maxArea = 0
        
        while begin < end:
            area = min(height[begin], height[end]) * (end-begin)
            maxArea = max(maxArea, area)
            if height[begin] <= height[end]:
                begin += 1
            else:
                end -= 1
                
        return maxArea