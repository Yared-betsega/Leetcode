# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = r = 0
        visited = set()
        ans = 0
        while r < len(s):
            if s[r] in visited:
                ans = max(ans, r-l)
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1
            visited.add(s[r])
            r += 1
        ans = max(ans, r-l)
        return ans

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
