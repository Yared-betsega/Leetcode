class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) ==0:
            return 0
        citations = sorted(citations)
        i = 0
        j = 1
        sw = 0
        while j <= len(citations):
            sw = j - i
            while i < j and sw > citations[i]:
                i += 1
                sw -= 1
            j+=1
            
        return sw
