class Solution:
    def minFlips(self, target: str) -> int:
        cur = target[0]
        ans = 0 if target[0] == "0" else 1
        for i in range(1, len(target)):
            if target[i] != cur:
                ans += 1
                cur = target[i]
        return ans