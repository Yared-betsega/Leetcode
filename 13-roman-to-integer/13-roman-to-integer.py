class Solution:
    def romanToInt(self, s: str) -> int:
        integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        for i in range(len(s)):
            if s[i] == "I":
                if i + 1 < len(s) and s[i+1] in ["V", "X"]:
                    ans -= integer[s[i]]
                else:
                    ans += integer[s[i]]
            elif s[i] == "X":
                if i + 1 < len(s) and s[i+1] in ["L", "C"]:
                    ans -= integer[s[i]]
                else:
                    ans += integer[s[i]]
            elif s[i] == "C":
                if i + 1 < len(s) and s[i+1] in ["D", "M"]:
                    ans -= integer[s[i]]
                else:
                    ans += integer[s[i]]
            else:
                ans += integer[s[i]]
        return ans