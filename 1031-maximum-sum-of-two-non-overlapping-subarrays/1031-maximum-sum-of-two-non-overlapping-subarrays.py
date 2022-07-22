class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum = 0
        left_first, right_first = 0, firstLen
        while right_first <= len(nums):
            firstSum = sum(nums[left_first:right_first])
            left_second, right_second = 0, secondLen
            while right_second <= left_first:
                secondSum = sum(nums[left_second: right_second])
                maxSum = max(firstSum + secondSum, maxSum)
                left_second += 1
                right_second += 1
            left_second, right_second = right_first, right_first + secondLen
            while right_second <= len(nums):
                secondSum = sum(nums[left_second: right_second])
                maxSum = max(firstSum + secondSum, maxSum)
                left_second += 1
                right_second += 1
            left_first += 1
            right_first += 1
            
        return maxSum

            
                