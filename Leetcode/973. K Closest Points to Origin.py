import math
def kClosest(points, k):
    allDistances = []
    ans =[]
    for point in points:
        temp = []
        distance = math.sqrt(point[0]**2 + point[1]**2)
        temp.append(point)
        temp.append(distance)
        allDistances.append(temp)
    allDistances = sorted(allDistances, key=lambda temp:temp[1])
    for i in range(k):
        ans.append(allDistances[i][0])
    return ans