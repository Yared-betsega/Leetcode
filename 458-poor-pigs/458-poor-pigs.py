class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest // minutesToDie + 1))
    
# time and space complexity
# time: O(1)
# space: O(1)