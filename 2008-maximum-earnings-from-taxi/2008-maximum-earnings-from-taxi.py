class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        startPoints = list(map(lambda x: x[0], rides))
        
        @cache
        def pickPassenger(i):
            if i >= len(rides):
                return 0
            nextIndex = bisect_left(startPoints, rides[i][1])
            pick = (rides[i][1] - rides[i][0] + rides[i][2]) + pickPassenger(nextIndex)
            dontPick = pickPassenger(i + 1)
            return max(pick, dontPick)
        
        return pickPassenger(0)
                    