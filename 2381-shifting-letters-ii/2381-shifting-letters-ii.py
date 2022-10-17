class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftPrefix = [0] * len(s)
        for st, e, d in shifts:
            if d == 1:
                shiftPrefix[st] += 1
                if e + 1 < len(s):
                    shiftPrefix[e + 1] -= 1
            else:
                shiftPrefix[st] -= 1
                if e + 1 < len(s):
                    shiftPrefix[e + 1] += 1
        index = []
        for i in range(97, 123):
            index.append(chr(i))
        prefix = 0
        ans = ""
        for i in range(len(shiftPrefix)):
            prefix += shiftPrefix[i]
            
            ans += index[((ord(s[i]) - 97) + prefix) % 26]
        return ans