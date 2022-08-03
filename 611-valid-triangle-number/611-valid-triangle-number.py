class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        def binary_search(l, r, target):
            while l < r:
                mid = ceil((l + r) // 2)
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                last = bisect_left(nums, nums[i] + nums[j], j+1, n)
                ans += last - (j + 1)
        return ans