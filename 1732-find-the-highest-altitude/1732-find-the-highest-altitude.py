class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [gain[0]]
        for i in range(1, len(gain)):
            prefix_sum.append(prefix_sum[i-1] + gain[i])
        return max(prefix_sum + [0])

# time and space complexity
# time: O(n)
# space: O(n)