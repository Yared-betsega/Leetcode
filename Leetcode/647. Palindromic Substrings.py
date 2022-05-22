# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def check(l, r):
            return s[l:r+1] == s[l:r+1][::-1]
        
        ans = 0
        for i in range(len(s)):
            for j in range(i+1):
                ans += check(j, i)
                
        return ans

# time = O(n**3)
# space = O(1)
