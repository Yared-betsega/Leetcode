# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxim = 0
        heights.append(0)
        for idx, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                cur = stack.pop()
                if stack:
                    maxim = max(maxim, heights[cur] * (idx-stack[-1]-1))
                else:
                    maxim = max(maxim, heights[cur] * idx)
            stack.append(idx)
        return maxim
