
# https://leetcode.com/problems/two-city-scheduling/

import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap = []
        for cost in costs:
            heapq.heappush(heap, [-1 * (abs(cost[0]-cost[1])), cost])
        a = 0
        b = 0
        cost = 0
        while heap:
            cur = heapq.heappop(heap)[1]
            if a < len(costs)/2:
                if b < len(costs)/2 and cur[1] < cur[0]:
                    b+=1
                    cost += cur[1]
                else:
                    a+=1
                    cost += cur[0]
            else:
                b+=1
                cost += cur[1]
            
        return cost

# time and space complexity
# time complexity = O(nlog(n))
# space complexity = O(n)
            
