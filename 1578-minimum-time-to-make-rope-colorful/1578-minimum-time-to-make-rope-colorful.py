class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        _max = total = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                _max = max(_max, neededTime[i])
                total += neededTime[i]
            else:
                ans += total - _max
                _max = total = neededTime[i]
            if i == len(colors) - 1:
                ans += total - _max
        
        return ans