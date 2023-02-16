class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = set()
        count = defaultdict(int)
        for i in range(len(nums)):
            if count[nums[i] - k] > 0:
                ans.add((nums[i] - k, nums[i]))
            count[nums[i]] += 1
        
        return len(ans)