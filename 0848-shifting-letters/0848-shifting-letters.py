class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:    
        shift = sum(shifts)
        alphabet = string.ascii_lowercase
        ans = ""
        for i in range(len(s)):
            ans += alphabet[((ord(s[i]) - 97) + shift) % 26]
            shift -= shifts[i]
        return ans