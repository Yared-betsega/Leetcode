# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if i+j >= len(haystack) or haystack[i+j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return -1

# time and space complexity
# n = len(haystack)
# m = len(needle)
# time complexity = O(nm)
# space complexity = O(1)
