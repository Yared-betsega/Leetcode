class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def find(s, idx):
            for i in range(idx, len(t)):
                if t[i] == s:
                    return i
        temp = -1     
        for i in s:
            temp = find(i, temp+1)
            if temp == None:
                return False
        
        return True
        
        