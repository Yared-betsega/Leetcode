# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums *= 2
#         prefix_sum = [nums[0]]
#         for i in range(1, len(nums)):
#             prefix_sum.append(prefix_sum[-1] + nums[i])
        
#         queue = deque([0])
#         ans = nums[0]
#         for i in range(1, len(prefix_sum)):
#             if queue[0] < i - n:
#                 queue.popleft()
            
#             ans = max(ans, prefix_sum[i] - prefix_sum[queue[0]])
            
#             while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
#                 queue.pop()
#             queue.append(i)
#         return ans

# # time and space complexity
# # time: O(n)
# # space: O(n)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_dp, min_dp = nums[:], nums[:]
        for i in range(1, len(nums)):
            max_dp[i] = max(nums[i], nums[i] + max_dp[i-1])
            min_dp[i] = min(nums[i], nums[i] + min_dp[i-1])
            
        s, _min, _max = sum(nums), min(min_dp), max(max_dp)
        if s == _min:
            return _max
        return max(_max, s - _min)
    
    
# time and space complexity
# time: O(n)
# space: O(n)