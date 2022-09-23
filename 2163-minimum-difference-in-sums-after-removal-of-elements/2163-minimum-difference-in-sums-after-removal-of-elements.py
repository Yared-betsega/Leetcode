class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        mins, lefts, _leftSum = [], {}, 0
        for i in range(len(nums)):
            heappush(mins, -nums[i])
            _leftSum += nums[i]
            if len(mins) > len(nums) / 3:
                _leftSum -= -heappop(mins)
            
            lefts[i] = _leftSum
        
        maxes, rights, _rightSum = [], {}, 0
        for i in range(len(nums) - 1, -1, -1):
            rights[i] = _rightSum
            heappush(maxes, nums[i])
            _rightSum += nums[i]
            if len(maxes) > len(nums) / 3:
                _rightSum -= heappop(maxes)
            
        ans = float("inf")
        for i in range(len(nums)):
            if i + 1 >= len(nums) / 3 and len(nums) - i > len(nums) / 3:
                ans = min(ans, lefts[i] - rights[i])
        return ans
        