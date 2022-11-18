class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                y_change = points[j][1] - points[i][1]
                x_change = points[j][0] - points[i][0]
                if x_change == 0:
                    pointsOnThisLine = 2
                    for k in range(j + 1, len(points)):
                        if points[k][0] == points[i][0]:
                            pointsOnThisLine += 1
                    ans = max(ans, pointsOnThisLine)
                else:
                    slope = y_change / x_change
                    b = points[i][1] - slope * points[i][0]
                    pointsOnThisLine = 2
                    for k in range(j + 1, len(points)):
                        if abs(points[k][1] - (slope * points[k][0] + b)) < 0.00001:
                            pointsOnThisLine += 1
                    ans = max(ans, pointsOnThisLine)
        return ans
        
        