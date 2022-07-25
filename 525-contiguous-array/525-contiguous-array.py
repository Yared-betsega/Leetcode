class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = [nums[0] if nums[0] == 1 else -1]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + (nums[i] if nums[i] == 1 else -1))
        ans = 0
        last = {0:-1}
        for i in range(len(nums)):
            if prefix_sum[i] in last:
                ans = max(ans, i-last[prefix_sum[i]])
            else:
                last[prefix_sum[i]] = i
        return ans