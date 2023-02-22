class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        pairs, seconds = s.count("01"), 0
        
        while pairs > 0:
            seconds += 1
            s = s.replace("01", "10")
            pairs = s.count("01")
            
            
        return seconds