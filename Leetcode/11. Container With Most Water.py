def maxArea(self, height: List[int]) -> int:
        begin = 0
        end = len(height)-1
        maxArea = 0
        
        while begin < end:
            area = min(height[begin], height[end]) * (end-begin)
            if area > maxArea:
                maxArea = area
            if height[begin] <= height[end]:
                begin += 1
                continue
            else:
                end -= 1
                
        return maxArea
