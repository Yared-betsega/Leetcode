class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = gain[0]
        ans = prefix_sum
        for i in range(1, len(gain)):
            prefix_sum = prefix_sum + gain[i]
            ans = max(ans, prefix_sum)
        return max(0, ans)

# time and space complexity
# time: O(n)
# space: O(1)