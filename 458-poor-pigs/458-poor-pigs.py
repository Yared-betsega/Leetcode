class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        trials = minutesToTest // minutesToDie + 1
        tot, pigs = 1, 0
        while tot < buckets:
            tot *= trials
            pigs += 1
        return pigs
        