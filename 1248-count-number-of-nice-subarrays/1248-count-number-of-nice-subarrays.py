class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        prefix_sum_frequency = defaultdict(int)
        prefixSum = 0
        prefix_sum_frequency[prefixSum] += 1
        ans = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            ans += prefix_sum_frequency[prefixSum - k]
            prefix_sum_frequency[prefixSum] += 1 

        return ans

# time and space complexity
# time: O(n)
# space: O(1)