class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def find_cost(target):
            totalCost = 0
            for i in range(len(nums)):
                totalCost += abs(nums[i] - target) * cost[i]
            return totalCost
        
        pairs = sorted(zip(nums, cost))
        prefixCost = [0]
        for pair in pairs:
            prefixCost.append(prefixCost[-1] + pair[1])
        
     
        currentCost = find_cost(pairs[0][0])
        answer = currentCost
        for i in range(1, len(nums)):
            diff = pairs[i][0] - pairs[i - 1][0]
            left = diff * prefixCost[i]
            right = diff * (prefixCost[-1] - prefixCost[i])
            currentCost = currentCost + left - right
            answer = min(answer, currentCost)
        
        return answer
        