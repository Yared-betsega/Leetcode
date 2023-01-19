class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] += 1
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k
            ans += count[rem]
            count[rem] += 1
        return ans
            