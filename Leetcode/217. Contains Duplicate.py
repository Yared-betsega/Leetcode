# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for i in nums:
            if i not in found:
                found.add(i)
            else:
                return True
        return False

# time = O(n)
# space = O(n)
