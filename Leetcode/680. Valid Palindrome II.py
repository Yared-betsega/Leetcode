# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isValid(s[left:right]) or isValid(s[left+1:right+1])
            left += 1
            right -= 1
        return True  

# time and space complexity
# time complexity = O(n)
# space complexity = O(1)
