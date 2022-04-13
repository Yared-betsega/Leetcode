# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_nums = deque()
        min_nums = deque()
        maxim = 0
        front = 0
        for i in range(len(nums)):
            while max_nums and max_nums[-1] < nums[i]:
                max_nums.pop()
            max_nums.append(nums[i])
            while min_nums and min_nums[-1] > nums[i]:
                min_nums.pop()
            min_nums.append(nums[i])
            
            if max_nums[0] - min_nums[0] <= limit:
                maxim = max(maxim, i - front + 1)
            else:
                if max_nums[0] == nums[front]:
                    max_nums.popleft()
                if min_nums[0] == nums[front]:
                    min_nums.popleft()
                front += 1
        return maxim
            
                
                
