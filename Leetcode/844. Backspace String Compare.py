# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        for i in range(len(s)):
            if s[i] != "#":
                sStack.append(s[i])
            elif sStack:
                sStack.pop()
                
        for i in range(len(t)):
            if t[i] != "#":
                tStack.append(t[i])
            elif tStack:
                tStack.pop()
        return sStack == tStack

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
