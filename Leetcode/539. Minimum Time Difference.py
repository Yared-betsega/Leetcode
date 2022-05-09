# https://leetcode.com/problems/minimum-time-difference/

import datetime
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def getDif(t1, t2):
            h1, m1 = list(map(int, t1.split(":")))
            h2, m2 = list(map(int, t2.split(":")))
            a = datetime.datetime(1,1,1,h1,m1,0)
            b = datetime.datetime(1,1,1,h2,m2,0)
            c = a - b
            ans = int(abs(c.total_seconds()/60))
            return ans
        
        timePoints.sort(key = lambda x: [int(x[0]), int(x[1]), int(x[3]), int(x[4])])
        
        back_to_front = getDif(timePoints[0], timePoints[-1])
        ans = min(back_to_front, 1440-back_to_front)
        
        for i in range(len(timePoints)-1):
            ans = min(ans, getDif(timePoints[i], timePoints[i+1]))
            if ans == 0:
                return ans
        
        return ans

# time complexity = O(nlog(n))
# space complexity = O(1)
