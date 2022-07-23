class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum_l, prefix_sum_r = [nums[0]], [sum(nums)]
        for i in range(1, len(nums)):
            prefix_sum_l.append(prefix_sum_l[i-1] + nums[i])
            prefix_sum_r.append(prefix_sum_r[i-1] - nums[i-1])
        
        for i in range(len(nums)):
            if prefix_sum_l[i] - nums[i] == prefix_sum_r[i] - nums[i]:
                return i
        return -1
    
# time and space complexity
# time: O(n)
# space: O(n)