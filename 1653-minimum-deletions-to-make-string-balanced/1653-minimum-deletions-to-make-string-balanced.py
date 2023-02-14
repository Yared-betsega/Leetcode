class Solution:
    def minimumDeletions(self, s: str) -> int:
        countB = []
        ct = 0
        for i in range(len(s)):
            countB.append(ct)
            if s[i] == "b":
                ct +=  1
                
            
        
        countA = 0
        ans = float("inf")
        for i in range(len(s) - 1, -1, -1):
            ans = min(ans, countB[i] + countA)
            countA += s[i] == "a"
        
        return ans
        