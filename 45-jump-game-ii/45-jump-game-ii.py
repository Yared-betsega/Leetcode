class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def chooseIndex(i):
            if i >= len(nums) - 1:
                return 0
            ans = float("inf")
            for j in range(i + 1, i + nums[i] + 1):
                ans = min(ans, chooseIndex(j) + 1)
            return ans
        return chooseIndex(0)