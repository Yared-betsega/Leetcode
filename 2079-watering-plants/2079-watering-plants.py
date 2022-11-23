class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curAmount = capacity
        for i in range(len(plants)):
            steps += 1
            curAmount -= plants[i]
            if i == len(plants) - 1:
                return steps
            
            if curAmount < plants[i + 1]:
                curAmount = capacity
                steps += 2 * (i + 1)
        