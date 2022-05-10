# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2
        answer = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
            
        return answer[: len(nums)//2]

# time complexity = O(n)
# space complexity = O(n)
            
            
