# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return s[l+1: r]
                l -= 1
                r += 1
            return s[l+1: r]
        
        ans = ""
        for i in range(len(s)):
            odd = check(i, i)
            even = check(i, i + 1)
            temp= odd if len(odd) > len(even) else even
            ans = ans if len(ans) > len(temp) else temp
        return ans

# time = O(n**2)
# space = O()
