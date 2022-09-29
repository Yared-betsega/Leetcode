class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        l, r = 0, k - 1
        ans = []
        while r < len(nums):
            ans.append(nums[queue[0]])
            if queue[0] == l:
                queue.popleft()
            l += 1
            r += 1
            if r < len(nums):
                while queue and nums[r] > nums[queue[-1]]:
                    queue.pop()
                queue.append(r)
        return ans
    