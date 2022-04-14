# https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def calculateP1(l, r):
            if l > r:
                return 0
            if l == r:
                return nums[l]
            
            chooseLeft = nums[l] + min(calculateP1(l+1, r-1), calculateP1(l+2, r))
            chooseRight = nums[r] + min(calculateP1(l+1, r-1), calculateP1(l, r-2))
            
            return max(chooseLeft, chooseRight)
        
        p1Score = calculateP1(0, len(nums)-1)
        if p1Score >= sum(nums) - p1Score:
            return True
        else:
            return False
            
            
                
