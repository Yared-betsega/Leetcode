# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        prev = [1,1,1,1,1]
        cur = [1,1,1,1,1]
        ans = [sum(prev)]
        if n == 1:
            return ans[0]
        
        for i in range(2, n+1):
            cur[0] = ans[-1]
            for j in range(1, len(prev)):
                cur[j] = cur[j-1] - prev[j-1]
                prev[j-1] = cur[j-1]
            ans.append(sum(cur))
            
        return ans[-1]
    
# time complexity = O(n)
# space complexity = O(n)
