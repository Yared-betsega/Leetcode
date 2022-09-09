class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        start, end = {}, {}
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i
            else:
                end[s[i]] = i
        ans = 0
        for i in start:
            if i in end:
                ans += len(set(s[start[i] + 1: end[i]]))
        return ans
        