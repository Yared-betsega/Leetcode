class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        _sum = sum(nums)
        runningSum = 0
        ans, minAvg = 0, float("inf")
        for i in range(len(nums)):
            runningSum += nums[i]
            leftAvg = runningSum // (i + 1)
            rightAvg = (_sum - runningSum) // (len(nums) - (i + 1)) if i < len(nums) - 1 else 0
            avgDif = abs(leftAvg - rightAvg)
            if avgDif < minAvg:
                ans, minAvg = i, avgDif
        return ans
            