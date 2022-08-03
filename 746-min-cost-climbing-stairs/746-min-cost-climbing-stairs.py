class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # DP top down implementation
#         def climb(idx, total, memo):
#             if idx > len(cost) - 1:
#                 return total
#             if (idx,total) in memo:
#                 return memo[(idx, total)]
             
#             value = cost[idx] + min(climb(idx+1, total, memo), climb(idx+2, total, memo))
#             memo[(idx, total)] = value
#             return value
        
#         return min(climb(0, 0, defaultdict(list)), climb(1, 0, defaultdict(list)))
#         # time and space complexity
#         # time: O(n)
#         # space: O(1)
        
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