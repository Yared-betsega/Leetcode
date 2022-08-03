class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        
        # DP bottom up implementation
        dp = [cost[i] for i in range(len(cost))]
        plusOne = cost[-2]
        plusTwo = cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            cur = cost[i] + min(plusOne, plusTwo)
            plusTwo = plusOne
            plusOne = cur
        return min(plusOne, plusTwo)
        
        # time and space complexity
        # time: O(n)
        # space: O(1)