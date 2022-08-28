class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp_max = dp_min = nums[0]
        gloMax = gloMin = abs(nums[0])
        for i in range(1, len(nums)):
            dp_max = max(nums[i], dp_max + nums[i])
            gloMax = max(abs(dp_max), abs(gloMax))
            dp_min = min(nums[i], dp_min + nums[i])
            gloMin = max(abs(dp_min), abs(gloMin))
        
        return max(gloMax, gloMin)

# time and space complexity
# time: O(n)
# space: O(1)

            