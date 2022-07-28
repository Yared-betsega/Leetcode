class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = Counter(s)
        tcount = Counter(t)
        for i in tcount:
            if scount[i] != tcount[i]:
                return False
        return True

# time and space complexity
# time: O(nlogn)
# space: O(n)