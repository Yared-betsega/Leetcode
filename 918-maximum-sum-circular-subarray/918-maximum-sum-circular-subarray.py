class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums *= 2
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        queue = deque([0])
        ans = nums[0]
        for i in range(1, len(prefix_sum)):
            if queue[0] < i - n:
                queue.popleft()
            
            ans = max(ans, prefix_sum[i] - prefix_sum[queue[0]])
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(i)
        return ans