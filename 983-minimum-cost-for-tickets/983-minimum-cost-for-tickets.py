class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        dur = [1, 7, 30]
        @cache
        def dp(day, rem):
            if day > 365:
                return 0
            if day not in days:
                return dp(day + 1, max(0, rem - 1))
            if rem > 0:
                return dp(day + 1, rem - 1)
            
            ans = float("inf")
            for i in range(3):
                ans = min(ans, costs[i] + dp(day + 1, dur[i] - 1))
            return ans
        
        return dp(1, 0)
                