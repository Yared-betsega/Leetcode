class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(t1, t2):
            if t1 >= len(text1) or t2 >= len(text2):
                return 0
            if text1[t1] == text2[t2]:
                return 1 + helper(t1 + 1, t2 + 1)
            
            else:
                return max(helper(t1 + 1, t2), helper(t1, t2 + 1))
            
        return helper(0, 0)