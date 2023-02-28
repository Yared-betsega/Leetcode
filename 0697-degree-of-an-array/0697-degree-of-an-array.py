class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start, end = {}, {}
        for i, num in enumerate(nums):
            if num not in start:
                start[num] = i
            end[num] = i

        count = Counter(nums)
        _mx = max(count.values())
        cands = []
        ans = len(nums)
        for num in set(nums):
            if count[num] == _mx:
                ans = min(ans, end[num] - start[num] + 1)

        return ans