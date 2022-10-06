class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        index = {0:0}
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            if pref % k not in index:
                index[pref % k] = i + 1
            elif index[pref % k] < i:
                return True
            
        return False