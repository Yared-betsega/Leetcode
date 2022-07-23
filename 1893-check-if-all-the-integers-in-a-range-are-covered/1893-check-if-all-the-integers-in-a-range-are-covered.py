class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            notCovered = True
            for j in ranges:
                if i >= j[0] and i <= j[1]:
                    notCovered = False
                    break
            if notCovered:
                return False
        
        return True
            
                