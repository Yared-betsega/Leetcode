class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = total = 0
        best = float("inf")
        while right < len(nums):
            total += nums[right]
            if total >= target:
                while total >= target and left <= right:
                    best = min(best, right - left + 1)
                    total -= nums[left]
                    left += 1
            right += 1
            
        return best if best != float("inf") else 0
                
            