# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = list(filter(lambda x: x.isalpha() or x.isdigit(), s))
        l, r = 0, len(lst) - 1
        while l <= r:
            if lst[l].lower() != lst[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

# time = O(n)
# space = O(n)
