class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1, 0]] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if j == 0:
                    if nums[i] != nums[j]:
                        dp[i] = [dp[j][0] + 1, 1 if nums[i] > nums[j] else -1]
                elif dp[j][1] == 1:
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], [dp[j][0] + 1, -1])
                else:
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], [dp[j][0] + 1, 1])
        return max(dp)[0]
                