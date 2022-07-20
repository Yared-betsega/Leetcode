class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# time and space complexity
# time: O(nlogn)
# space: O(n)