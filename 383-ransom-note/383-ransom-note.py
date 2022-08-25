class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = Counter(ransomNote)
        mags = Counter(magazine)
        for i in rans:
            if mags[i] < rans[i]:
                return False
        return True