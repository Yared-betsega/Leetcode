import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            maxSum = 0
            for  num in nums:
                maxSum += math.ceil(num / mid)
            if maxSum <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left

# space time complexity
# time complexity = O(nlog(n))
# space complexity = O(1)
