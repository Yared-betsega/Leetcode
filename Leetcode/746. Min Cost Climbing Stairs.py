class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(idx, total, memo):
            if idx > len(cost) - 1:
                return total
            if (idx,total) in memo:
                return memo[(idx, total)]
             
            value = cost[idx] + min(climb(idx+1, total, memo), climb(idx+2, total, memo))
            memo[(idx, total)] = value
            return value
        
        return min(climb(0, 0, defaultdict(list)), climb(1, 0, defaultdict(list)))

