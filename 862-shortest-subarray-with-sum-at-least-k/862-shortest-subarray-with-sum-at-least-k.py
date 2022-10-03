class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        ans = float("inf")
        queue = deque()
        for i in range(len(prefix)):
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()
            while queue and prefix[i] - prefix[queue[0]] >= k :
                ans = min(ans, i - queue.popleft())
            queue.append(i)

        return ans if ans != float("inf") else -1

# time and space complexity
# time: O(n)
# space: O(n)