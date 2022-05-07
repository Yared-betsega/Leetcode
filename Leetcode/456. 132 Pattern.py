# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, last = [], -float("inf")
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < last:
                return True
            while stack and nums[i] > stack[-1]:
                last = stack.pop()
            stack.append(nums[i])
            
        return False

# time complixity = O(n)
# space complexity = O(n)
                
            
