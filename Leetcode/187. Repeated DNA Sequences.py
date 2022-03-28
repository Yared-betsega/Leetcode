
# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) <= 10:
            return ""
        
        repeated = set()
        answer = set()
        
        i, j = 0, 10
        while j <= len(s):
            cur = s[i:j]
            
            if cur in repeated:
                answer.add(cur)

            repeated.add(cur)
            
            i += 1
            j += 1
        
        return answer
    
# sliding window solution
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)

            
            
