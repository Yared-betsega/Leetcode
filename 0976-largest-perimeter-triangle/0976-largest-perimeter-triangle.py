class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        largest = 0
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] + nums[i-1] > nums[i-2]:
                if nums[i-1] + nums[i-2] > nums[i]:
                    if nums[i] + nums[i-2] > nums[i-1]:
                        largest = max(largest, nums[i] + nums[i-1] + nums[i-2]) 
        
        return largest