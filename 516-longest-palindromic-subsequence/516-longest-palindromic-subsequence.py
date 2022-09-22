class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def check(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            longest = 0
            if s[l] == s[r]:
                if l != r:
                    longest = max(longest, 2 + check(l + 1, r - 1))
                else:
                    longest = max(longest, 1 + check(l + 1, r - 1))
            else:
                longest = max(check(l + 1, r), check(l, r - 1))
            memo[(l, r)] = longest
            return longest
        
        return check(0, len(s) - 1)
        