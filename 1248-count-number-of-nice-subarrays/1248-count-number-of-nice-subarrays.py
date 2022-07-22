class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        prefix_sum_frequency = defaultdict(int)
        prefixSum = [nums[0]]
        prefix_sum_frequency[prefixSum[0]] += 1
        ans = 0
        if prefixSum[0] == k: # If the first element equals k
                ans += 1
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[i-1]) 
            if prefixSum[-1] == k:
                ans += 1
            ans += prefix_sum_frequency[prefixSum[-1] - k]
            prefix_sum_frequency[prefixSum[-1]] += 1
            
        return ans