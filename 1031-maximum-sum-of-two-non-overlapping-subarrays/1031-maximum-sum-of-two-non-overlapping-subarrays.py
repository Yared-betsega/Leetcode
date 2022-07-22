class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum = 0
        left_first, right_first = 0, firstLen-1
        firstSum = sum(nums[left_first:right_first + 1])
        while right_first < len(nums):
            left_second, right_second = 0, secondLen-1
            secondSum = sum(nums[left_second: right_second+1])
            while right_second < left_first:
                maxSum = max(firstSum + secondSum, maxSum)
                secondSum -= nums[left_second]
                left_second += 1
                right_second += 1
                secondSum += nums[right_second]
            left_second, right_second = right_first + 1, right_first + secondLen
            secondSum = sum(nums[left_second: right_second + 1])
            while right_second < len(nums):
                maxSum = max(firstSum + secondSum, maxSum)
                secondSum -= nums[left_second]
                left_second += 1
                right_second += 1
                secondSum += nums[right_second] if right_second < len(nums) else 0
            firstSum -= nums[left_first]
            left_first += 1
            right_first += 1
            firstSum += nums[right_first] if right_first < len(nums) else 0
        return maxSum

            
                