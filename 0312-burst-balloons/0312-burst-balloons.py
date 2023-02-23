class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]
        ans = 0
        for left in range(n - 2, 0, -1):
            for right in range(1, n - 1):
                if left <= right:
                    for i in range(left, right + 1):
                        dp[left][right] = max(
                            dp[left][right],
                            nums[left - 1] * nums[i] * nums[right + 1]
                            + dp[left][i - 1]
                            + dp[i + 1][right],
                        )
                    ans = max(ans, dp[left][right])

        return ans