# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match, taken = {}, set()
        for i in range(len(s)):
            if s[i] in match:
                if match[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in taken:
                    match[s[i]] = t[i]
                    taken.add(t[i])
                else:
                    return False
                
        return True

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
