class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        startIndex = list(map(lambda x: x[0], events))
        
        @cache
        def attendEvent(i, eventsLeft):
            if eventsLeft == 0:
                return 0
            if i >= len(events):
                return 0
            
            nextEvent = bisect_left(startIndex, events[i][1] + 1)
            
            attend = events[i][2] + attendEvent(nextEvent, eventsLeft - 1)
            dontAttend = attendEvent(i + 1, eventsLeft)
            
            return max(attend, dontAttend)
        
        return attendEvent(0, 2)