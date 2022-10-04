class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        _max = total = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                _max = max(_max, neededTime[i])
                total += neededTime[i]
            else:
                total -= _max
                _max = neededTime[i]
                total += _max
            if i == len(colors) - 1:
                total -= _max
        
        return total

# time and space complexity
# time: O(n)
# space: O(1)