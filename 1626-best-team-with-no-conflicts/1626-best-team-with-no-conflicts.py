class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        mapped = sorted(zip(ages, scores), reverse = True)
        ans = 0
        dp = [0] * len(scores)
        for i, [age, score] in enumerate(mapped):
            dp[i] = score
            for j in range(i):
                if score <= mapped[j][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        return ans
        