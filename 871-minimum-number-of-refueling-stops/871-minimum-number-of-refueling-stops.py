class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        N = len(stations)
        pq = []
        def push(n):
            heappush(pq, -n)
        def pop():
            return - heappop(pq)
        res = 0 # Number of refueling stops
        i = 0 # Next station index that's not added to the queue
        while startFuel < target:
            while i < N and stations[i][0] <= startFuel:
                push(stations[i][1])
                i += 1
            if not pq:
                return -1
            startFuel += pop()
            res += 1
        return res