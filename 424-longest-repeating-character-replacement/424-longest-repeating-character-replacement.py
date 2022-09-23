class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for char in string.ascii_uppercase:
            l = r = 0
            count = 0
            while r < len(s):
                if s[r] == char:
                    count += 1
                while count + k < r - l + 1:
                    count -= s[l] == char
                    l += 1
                ans = max(ans, r - l + 1)
                r += 1
        
        return ans
                