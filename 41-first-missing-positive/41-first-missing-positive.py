class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                nums[int(nums[i]) - 1] += 0.0
        
        for i in range(len(nums)):
            if type(nums[i]) != type(0.0):
                return i + 1
                
        return len(nums) + 1
    
# time and space complexity
# time: O(n)
# space: O(1)