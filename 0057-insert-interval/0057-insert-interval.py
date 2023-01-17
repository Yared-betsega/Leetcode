class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [1, 3], [6, 8]
        [2, 7]
        """
        pos = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                pos = i
                break
                
        intervals.insert(pos, newInterval)    
        if len(intervals) <= 1:
            return intervals   
        mergedIntervals = []
        mergedIntervals.append(intervals[0])
        length = len(intervals)
        for i in range(1, length):
            if intervals[i][0] <= mergedIntervals[-1][1]:
                if intervals[i][1] >= mergedIntervals[-1][1]:
                    mergedIntervals[-1][1] = intervals[i][1]
            else:
                mergedIntervals.append(intervals[i])
        return mergedIntervals
        