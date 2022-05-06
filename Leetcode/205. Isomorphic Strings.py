# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}
        changed = ""
        taken = set()
        for i in range(len(s)):
            if s[i] in match:
                changed += match[s[i]]
            else:
                if t[i] not in taken:
                    match[s[i]] = t[i]
                    changed += t[i]
                    taken.add(t[i])
                else:
                    return False
        
        for i in range(len(changed)):
            if changed[i] != t[i]:
                return False
        return True

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
