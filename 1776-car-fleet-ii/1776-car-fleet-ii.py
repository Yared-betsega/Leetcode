class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        ans = [-1]
        curFleet = cars[-1]
        stack = []
        
        for i in range(len(cars) - 2, -1, -1):
            pos, speed = cars[i]
            if speed <= curFleet[1]:
                ans.append(-1)
                curFleet = cars[i]
                stack.clear()
            else:
                while stack and stack[-1][1][1] >= speed:
                    stack.pop()
                time_to_fleet = (curFleet[0] - pos) / (speed - curFleet[1])
                while stack and (stack[-1][1][0] - pos) / (speed - stack[-1][1][1]) > stack[-1][0]:
                    stack.pop()
                if stack:
                    time_to_fleet = (stack[-1][1][0] - pos) / (speed - stack[-1][1][1])
                stack.append((time_to_fleet, cars[i]))
                ans.append(time_to_fleet)
        ans.reverse()
        return ans
        
# time and space complexity
# time: O(n)
# space: O(n)
        