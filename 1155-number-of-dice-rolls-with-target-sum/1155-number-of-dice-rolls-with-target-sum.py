class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(turn, target):
            if turn > n:
                if target == 0:
                    return 1
                return 0
            ans = 0
            for face in range(1, k + 1):
                ans += dp(turn + 1, target - face)
            return ans
        
        return dp(1, target) % (10 ** 9 + 7)