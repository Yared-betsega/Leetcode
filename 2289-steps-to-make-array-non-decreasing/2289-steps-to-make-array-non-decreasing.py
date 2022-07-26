class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        delete = [0] * len(nums)
        delete[-1] = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                last = stack.pop()
                delete[i] = max(delete[i] + 1, delete[last])
            stack.append(i)
        return max(delete)

# time and space complexity
# time: O(n)
# space: O(n)