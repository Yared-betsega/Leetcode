class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        score = 0
        for j in range(1, len(values)):
            score = max(score, values[i] + values[j] + (i - j))
            if values[j] >= values[i]:
                i = j
            elif values[i] - values[j] < j - i:
                i = j
        return score

# time and space complexity
# time: O(n)
# space: O(1)
            