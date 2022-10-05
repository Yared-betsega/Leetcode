class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(copied, toBePasted):
            if toBePasted < 0:
                return float("inf")
            if toBePasted == 0:
                return 0
            if copied > toBePasted:
                return float("inf")
            if copied == 0:
                return 1  + dp(1, toBePasted)
            if copied == n - toBePasted:
                return 1 + dp(copied, toBePasted - copied)
            return 1 + min(dp(n - toBePasted, toBePasted), dp(copied, toBePasted - copied))
        return dp(0, n - 1)