class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev = defaultdict(int)
        prefixSum = [nums[0]]
        prev[prefixSum[0]] += 1
        ans = 0
        if prefixSum[0] == k:
                ans += 1
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[i-1]) 
            if prefixSum[-1] == k:
                ans += 1
            ans += prev[prefixSum[-1] - k]
            prev[prefixSum[-1]] += 1
            
        return ans
    