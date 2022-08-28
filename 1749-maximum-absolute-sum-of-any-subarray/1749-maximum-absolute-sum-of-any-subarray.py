class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp_max = nums[:]
        dp_min = nums[:]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i], dp_max[i - 1] + nums[i])
            dp_min[i] = min(dp_min[i], dp_min[i - 1] + nums[i])
        
        return max(max(map(abs, dp_max)), max(map(abs, dp_min)))

            