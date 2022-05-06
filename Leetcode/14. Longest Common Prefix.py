# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getPref(s1, s2):
            pref = ""
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    return pref
                pref += s1[i]
            return pref
            
        common_pref = strs[0]
        for i in range(1, len(strs)):
            common_pref = getPref(common_pref, strs[i])

        return common_pref
    
# time and space complexity
# time complexity = O(nm)
# space complecity = O(m)
